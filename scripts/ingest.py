#!/usr/bin/env python3
"""ToscaBase video ingest: YouTube video/playlist -> raw/transcripts/<id>.md

Usage:
    ingest.py <url-or-id>... [--playlist URL] [--model medium|large-v3|small]
              [--source whisper|subs] [--lang en] [--force] [--dry-run]

Pipeline per video:
    1. metadata via `yt-dlp -J --skip-download`
    2. audio   -> raw/audio/<id>.m4a            (source=whisper)
       subs    -> raw/subs/<NN->-<id>.<lang>.vtt (source=subs)
    3. transcript segments (faster-whisper or parsed VTT)
    4. raw/transcripts/<id>.md + raw/transcripts/<id>.segments.json
    5. raw/manifest.json updated (deduped by id, `docs` preserved)

Stdlib only, plus faster_whisper (imported lazily for --source whisper).
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator, Optional
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
AUDIO_DIR = RAW_DIR / "audio"
SUBS_DIR = RAW_DIR / "subs"
TRANSCRIPTS_DIR = RAW_DIR / "transcripts"
MANIFEST_PATH = RAW_DIR / "manifest.json"

TOSCA_PROMPT = (
    "Tricentis Tosca, Tosca Commander, Module, TestCase, TestStep, ExecutionList, "
    "TBox, XScan, Buffer, Business Parameter, Configuration Parameter, ActionMode, "
    "DokuSnapper, Steering, TestStepBlock, API Scan."
)

VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
PARAGRAPH_MIN_SEC = 30.0
PARAGRAPH_MAX_SEC = 60.0


# --------------------------------------------------------------------------- data

@dataclass
class VideoRef:
    """Something to ingest, before metadata is known."""
    id: str
    url: str
    playlist: Optional[str] = None
    playlist_index: Optional[int] = None


@dataclass
class VideoMeta:
    id: str
    title: str
    url: str
    channel: str
    duration: Optional[int]
    upload_date: Optional[str]
    playlist: Optional[str] = None
    playlist_index: Optional[int] = None


@dataclass
class Segment:
    start: float
    end: float
    text: str

    def to_dict(self) -> dict:
        return {"start": round(self.start, 3), "end": round(self.end, 3), "text": self.text}


@dataclass
class Options:
    model: str
    source: str
    lang: str
    force: bool
    dry_run: bool


@dataclass
class Result:
    id: str
    status: str  # done | skipped | failed | dry-run
    detail: str = ""
    elapsed: float = 0.0


@dataclass
class Summary:
    results: list[Result] = field(default_factory=list)

    def add(self, r: Result) -> None:
        self.results.append(r)


# --------------------------------------------------------------------------- helpers

def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def run(cmd: list[str], capture: bool = True) -> subprocess.CompletedProcess:
    """Run a subprocess, raising RuntimeError with stderr on failure."""
    proc = subprocess.run(cmd, capture_output=capture, text=True)
    if proc.returncode != 0:
        err = (proc.stderr or "").strip().splitlines()
        tail = err[-1] if err else f"exit {proc.returncode}"
        raise RuntimeError(f"{cmd[0]} failed: {tail}")
    return proc


def yt_json(url: str, extra: Iterable[str] = ()) -> dict:
    proc = run(["yt-dlp", "-J", "--skip-download", "--no-warnings", *extra, url])
    return json.loads(proc.stdout)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def fmt_ts(seconds: float) -> str:
    s = int(seconds)
    if s >= 3600:
        return f"{s // 3600}:{(s % 3600) // 60:02d}:{s % 60:02d}"
    return f"{s // 60:02d}:{s % 60:02d}"


def yaml_str(value: object) -> str:
    """Render a scalar as YAML. Strings are JSON-quoted, which YAML accepts."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


# --------------------------------------------------------------------------- input resolution

def extract_video_id(arg: str) -> Optional[str]:
    if VIDEO_ID_RE.match(arg):
        return arg
    parsed = urlparse(arg)
    if parsed.netloc.endswith("youtu.be"):
        cand = parsed.path.strip("/").split("/")[0]
        return cand if VIDEO_ID_RE.match(cand) else None
    qs = parse_qs(parsed.query)
    if "v" in qs and VIDEO_ID_RE.match(qs["v"][0]):
        return qs["v"][0]
    m = re.search(r"/(?:shorts|embed|live)/([A-Za-z0-9_-]{11})", parsed.path)
    return m.group(1) if m else None


def extract_playlist_id(arg: str) -> Optional[str]:
    parsed = urlparse(arg)
    qs = parse_qs(parsed.query)
    return qs["list"][0] if "list" in qs else None


def resolve_playlist(url: str) -> list[VideoRef]:
    """Flat-list a playlist, preserving order and 1-based index."""
    log(f"Resolving playlist {url}")
    data = yt_json(url, ["--flat-playlist"])
    title = data.get("title") or data.get("id") or url
    refs: list[VideoRef] = []
    for i, entry in enumerate(data.get("entries") or [], start=1):
        vid = entry.get("id")
        if not vid:
            continue
        refs.append(VideoRef(
            id=vid,
            url=entry.get("url") or f"https://www.youtube.com/watch?v={vid}",
            playlist=title,
            playlist_index=int(entry.get("playlist_index") or i),
        ))
    log(f"Playlist '{title}': {len(refs)} videos")
    return refs


def resolve_inputs(items: list[str], playlist: Optional[str]) -> list[VideoRef]:
    refs: list[VideoRef] = []
    seen: set[str] = set()

    def add(ref: VideoRef) -> None:
        if ref.id not in seen:
            seen.add(ref.id)
            refs.append(ref)

    sources = list(items)
    if playlist:
        sources.append(playlist)
    for arg in sources:
        list_id = extract_playlist_id(arg)
        vid = extract_video_id(arg)
        if list_id and (arg == playlist or not vid or "playlist" in arg):
            for ref in resolve_playlist(f"https://www.youtube.com/playlist?list={list_id}"):
                add(ref)
        elif vid:
            add(VideoRef(id=vid, url=f"https://www.youtube.com/watch?v={vid}"))
        else:
            log(f"WARNING: cannot parse '{arg}', skipping")
    return refs


# --------------------------------------------------------------------------- metadata / download

def fetch_metadata(ref: VideoRef) -> VideoMeta:
    data = yt_json(ref.url, ["--no-playlist"])
    duration = data.get("duration")
    return VideoMeta(
        id=data.get("id") or ref.id,
        title=data.get("title") or ref.id,
        url=data.get("webpage_url") or ref.url,
        channel=data.get("channel") or data.get("uploader") or "",
        duration=int(duration) if duration else None,
        upload_date=data.get("upload_date"),
        playlist=ref.playlist,
        playlist_index=ref.playlist_index,
    )


def download_audio(meta: VideoMeta) -> Path:
    target = AUDIO_DIR / f"{meta.id}.m4a"
    if target.exists():
        log(f"  audio present: {target.relative_to(ROOT)}")
        return target
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    log("  downloading audio ...")
    run([
        "yt-dlp", "--no-playlist", "--no-warnings",
        "-f", "bestaudio[ext=m4a]/bestaudio",
        "-x", "--audio-format", "m4a",
        "-o", str(AUDIO_DIR / "%(id)s.%(ext)s"),
        meta.url,
    ])
    if not target.exists():
        raise RuntimeError(f"audio not produced at {target}")
    return target


def find_subs(video_id: str, lang: str) -> Optional[Path]:
    """Existing VTT for this id: `<NN>-<id>.<lang>.vtt` or `<id>.<lang>.vtt` (not -orig)."""
    for cand in sorted(SUBS_DIR.glob(f"*{video_id}.{lang}.vtt")):
        stem = cand.name[: -len(f".{lang}.vtt")]
        if stem == video_id or stem.endswith(f"-{video_id}"):
            return cand
    return None


def download_subs(meta: VideoMeta, lang: str) -> Path:
    existing = find_subs(meta.id, lang)
    if existing:
        log(f"  subs present: {existing.relative_to(ROOT)}")
        return existing
    SUBS_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"{meta.playlist_index:02d}-{meta.id}" if meta.playlist_index else meta.id
    log("  downloading auto subs ...")
    run([
        "yt-dlp", "--no-playlist", "--no-warnings", "--skip-download",
        "--write-auto-subs", "--sub-langs", lang, "--sub-format", "vtt",
        "-o", str(SUBS_DIR / stem),
        meta.url,
    ])
    found = find_subs(meta.id, lang)
    if not found:
        raise RuntimeError(f"no auto subtitles ({lang}) available for {meta.id}")
    return found


# --------------------------------------------------------------------------- VTT parsing

VTT_TIME_RE = re.compile(r"(\d+):(\d\d):(\d\d)\.(\d{3})|(\d\d):(\d\d)\.(\d{3})")
CUE_LINE_RE = re.compile(r"^(\S+)\s+-->\s+(\S+)")
TAG_RE = re.compile(r"<[^>]+>")
INLINE_TIME_RE = re.compile(r"<(\d+:\d\d:\d\d\.\d{3})>")
NOISE_RE = re.compile(r"^\[[^\]]*\]$")  # [Music], [Applause], ...


def parse_vtt_time(s: str) -> float:
    m = VTT_TIME_RE.match(s)
    if not m:
        raise ValueError(f"bad timestamp {s!r}")
    if m.group(1) is not None:
        h, mi, se, ms = (int(m.group(i)) for i in (1, 2, 3, 4))
    else:
        h, mi, se, ms = 0, int(m.group(5)), int(m.group(6)), int(m.group(7))
    return h * 3600 + mi * 60 + se + ms / 1000


def clean_caption_line(line: str) -> str:
    text = TAG_RE.sub("", line)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def iter_vtt_cues(text: str) -> Iterator[tuple[float, float, list[str]]]:
    """Yield (start, end, raw_lines) for each cue block."""
    blocks = re.split(r"\n\s*\n", text.replace("\r\n", "\n"))
    for block in blocks:
        lines = block.strip("\n").split("\n")
        idx = next((i for i, ln in enumerate(lines) if "-->" in ln), None)
        if idx is None:
            continue
        m = CUE_LINE_RE.match(lines[idx].strip())
        if not m:
            continue
        yield parse_vtt_time(m.group(1)), parse_vtt_time(m.group(2)), lines[idx + 1:]


def parse_rolling_vtt(path: Path) -> list[Segment]:
    """Turn YouTube rolling auto-captions into non-overlapping segments.

    In the rolling format every spoken line appears twice: once with word
    timing tags (`hello<00:00:15.679><c> friends</c>`) in the cue where it is
    spoken, and once as a plain repeat at the top of the next cue. Lines with
    inline tags are the "new" lines; a plain line is emitted only if it differs
    from the previous emitted line (this also covers non-rolling VTTs).
    """
    segments: list[Segment] = []
    last_text = ""
    for start, end, raw_lines in iter_vtt_cues(path.read_text(encoding="utf-8")):
        for raw in raw_lines:
            text = clean_caption_line(raw)
            if not text or NOISE_RE.match(text):
                continue
            has_timing = "<c>" in raw or INLINE_TIME_RE.search(raw) is not None
            if not has_timing and text == last_text:
                continue
            segments.append(Segment(start=start, end=end, text=text))
            last_text = text
    # tighten ends so segments don't overlap the next start
    for a, b in zip(segments, segments[1:]):
        if a.end > b.start:
            a.end = b.start
    return segments


# --------------------------------------------------------------------------- whisper

def transcribe_whisper(audio: Path, model_size: str, lang: str) -> list[Segment]:
    from faster_whisper import WhisperModel  # lazy: heavy import

    t0 = time.time()
    log(f"  loading faster-whisper '{model_size}' (cpu, int8) ...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    log(f"  model ready in {time.time() - t0:.1f}s, transcribing ...")

    segments_iter, info = model.transcribe(
        str(audio),
        language=lang,
        beam_size=5,
        vad_filter=True,
        initial_prompt=TOSCA_PROMPT,
    )
    total = info.duration or 0.0
    out: list[Segment] = []
    t1 = time.time()
    for seg in segments_iter:
        text = re.sub(r"\s+", " ", seg.text).strip()
        if not text:
            continue
        out.append(Segment(start=float(seg.start), end=float(seg.end), text=text))
        if len(out) % 20 == 0:
            done = seg.end
            pct = f"{100 * done / total:.0f}%" if total else "?"
            log(f"    {len(out)} segments | {fmt_ts(done)} / {fmt_ts(total)} ({pct}) "
                f"| {time.time() - t1:.0f}s elapsed")
    log(f"  transcribed {len(out)} segments in {time.time() - t1:.1f}s "
        f"(audio {fmt_ts(total)})")
    return out


# --------------------------------------------------------------------------- output

def build_paragraphs(segments: list[Segment]) -> list[str]:
    """Group segments into ~30-60 s paragraphs, each prefixed with [mm:ss]."""
    paragraphs: list[str] = []
    buf: list[str] = []
    buf_start = 0.0
    buf_end = 0.0

    def flush() -> None:
        if buf:
            text = re.sub(r"\s+", " ", " ".join(buf)).strip()
            paragraphs.append(f"[{fmt_ts(buf_start)}] {text}")
            buf.clear()

    for seg in segments:
        if not buf:
            buf_start = seg.start
        buf.append(seg.text)
        buf_end = seg.end
        span = buf_end - buf_start
        sentence_end = seg.text.rstrip().endswith((".", "!", "?"))
        if span >= PARAGRAPH_MAX_SEC or (span >= PARAGRAPH_MIN_SEC and sentence_end):
            flush()
    flush()
    return paragraphs


def write_transcript(meta: VideoMeta, segments: list[Segment], source: str, lang: str) -> Path:
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    md_path = TRANSCRIPTS_DIR / f"{meta.id}.md"
    json_path = TRANSCRIPTS_DIR / f"{meta.id}.segments.json"

    front = {
        "id": meta.id,
        "title": meta.title,
        "url": meta.url,
        "channel": meta.channel,
        "playlist": meta.playlist,
        "playlist_index": meta.playlist_index,
        "duration": meta.duration,
        "upload_date": meta.upload_date,
        "source": source,
        "language": lang,
        "transcribed_at": now_iso(),
        "status": "raw",
    }
    lines = ["---", *(f"{k}: {yaml_str(v)}" for k, v in front.items()), "---", ""]
    lines.append(f"# {meta.title}")
    lines.append("")
    for para in build_paragraphs(segments):
        lines.append(para)
        lines.append("")
    md_path.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")
    json_path.write_text(
        json.dumps([s.to_dict() for s in segments], ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    return md_path


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        try:
            data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("videos"), list):
                return data
        except json.JSONDecodeError as exc:
            log(f"WARNING: manifest unreadable ({exc}), starting fresh")
    return {"videos": []}


def update_manifest(meta: VideoMeta, transcript: Path, source: str) -> None:
    manifest = load_manifest()
    by_id: dict[str, dict] = {v["id"]: v for v in manifest["videos"] if "id" in v}
    prev = by_id.get(meta.id, {})
    by_id[meta.id] = {
        "id": meta.id,
        "title": meta.title,
        "url": meta.url,
        "playlist": meta.playlist if meta.playlist is not None else prev.get("playlist"),
        "playlist_index": (meta.playlist_index if meta.playlist_index is not None
                           else prev.get("playlist_index")),
        "duration": meta.duration,
        "transcript": transcript.relative_to(ROOT).as_posix(),
        "source": source,
        "ingested_at": now_iso(),
        "docs": list(prev.get("docs") or []),
    }
    manifest["videos"] = sorted(
        by_id.values(),
        key=lambda v: (v.get("playlist") or "", v.get("playlist_index") or 0, v.get("title") or ""),
    )
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")


# --------------------------------------------------------------------------- per-video driver

def source_label(opts: Options) -> str:
    return f"whisper:{opts.model}" if opts.source == "whisper" else "youtube-subs"


def ingest_one(ref: VideoRef, opts: Options) -> Result:
    transcript = TRANSCRIPTS_DIR / f"{ref.id}.md"
    if transcript.exists() and not opts.force:
        return Result(ref.id, "skipped", "transcript exists (use --force)")
    if opts.dry_run:
        need = "audio" if opts.source == "whisper" else "subs"
        have = (AUDIO_DIR / f"{ref.id}.m4a").exists() if need == "audio" else bool(
            find_subs(ref.id, opts.lang))
        return Result(ref.id, "dry-run",
                      f"would transcribe via {source_label(opts)}; {need} "
                      f"{'cached' if have else 'to download'}")

    t0 = time.time()
    meta = fetch_metadata(ref)
    log(f"  '{meta.title}' ({fmt_ts(meta.duration or 0)})")
    if opts.source == "whisper":
        audio = download_audio(meta)
        segments = transcribe_whisper(audio, opts.model, opts.lang)
    else:
        vtt = download_subs(meta, opts.lang)
        segments = parse_rolling_vtt(vtt)
        log(f"  parsed {len(segments)} caption lines from {vtt.name}")
    if not segments:
        raise RuntimeError("no speech segments produced")

    label = source_label(opts)
    path = write_transcript(meta, segments, label, opts.lang)
    update_manifest(meta, path, label)
    elapsed = time.time() - t0
    log(f"  wrote {path.relative_to(ROOT)} ({len(segments)} segments, {elapsed:.1f}s)")
    return Result(ref.id, "done", f"{label} -> {path.relative_to(ROOT)}", elapsed)


# --------------------------------------------------------------------------- CLI

def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Ingest YouTube videos into raw/transcripts/ (yt-dlp + faster-whisper).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Pipeline per video:")[0],
    )
    p.add_argument("items", nargs="*", metavar="url-or-id",
                   help="video URLs, bare 11-char ids, or playlist URLs")
    p.add_argument("--playlist", metavar="URL", help="playlist URL to ingest in order")
    p.add_argument("--model", default="medium", choices=["small", "medium", "large-v3"],
                   help="faster-whisper model (default: medium)")
    p.add_argument("--source", default="whisper", choices=["whisper", "subs"],
                   help="whisper transcription (default) or YouTube auto-subtitles")
    p.add_argument("--lang", default="en", help="language code (default: en)")
    p.add_argument("--force", action="store_true", help="re-transcribe existing transcripts")
    p.add_argument("--dry-run", action="store_true", help="only list what would be done")
    args = p.parse_args(argv)
    if not args.items and not args.playlist:
        p.error("give at least one url/id or --playlist")
    return args


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    opts = Options(model=args.model, source=args.source, lang=args.lang,
                   force=args.force, dry_run=args.dry_run)
    try:
        refs = resolve_inputs(args.items, args.playlist)
    except (RuntimeError, json.JSONDecodeError) as exc:
        log(f"ERROR: {exc}")
        return 2
    if not refs:
        log("Nothing to ingest.")
        return 1

    summary = Summary()
    for n, ref in enumerate(refs, start=1):
        tag = f"[{n}/{len(refs)}] {ref.id}"
        if ref.playlist_index:
            tag += f" (#{ref.playlist_index} in '{ref.playlist}')"
        log(tag)
        try:
            summary.add(ingest_one(ref, opts))
        except KeyboardInterrupt:
            log("Interrupted.")
            summary.add(Result(ref.id, "failed", "interrupted"))
            break
        except Exception as exc:  # one failure must not abort the batch
            log(f"  ERROR: {exc}")
            summary.add(Result(ref.id, "failed", str(exc)))

    log("")
    log("Summary:")
    for r in summary.results:
        extra = f" [{r.elapsed:.0f}s]" if r.elapsed else ""
        log(f"  {r.status:8s} {r.id}  {r.detail}{extra}")
    counts = {s: sum(1 for r in summary.results if r.status == s)
              for s in ("done", "skipped", "failed", "dry-run")}
    log("  " + ", ".join(f"{k}={v}" for k, v in counts.items() if v))
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
