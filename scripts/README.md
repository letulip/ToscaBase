# scripts/ — video ingest pipeline

`ingest.py` turns a YouTube video or playlist into `raw/transcripts/<id>.md`
(YAML frontmatter + timestamped paragraphs) and registers it in `raw/manifest.json`.

## Setup (once)

System tools on PATH: `yt-dlp` and `ffmpeg` (`brew install yt-dlp ffmpeg`).

```sh
python3.11 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
```

Whisper models are downloaded on first use into `~/.cache/huggingface/hub`
(`Systran/faster-whisper-<model>`), roughly 0.5 GB (small), 1.5 GB (medium), 3 GB (large-v3).

## Usage

```sh
.venv/bin/python scripts/ingest.py <url-or-id>... [--playlist URL] \
    [--model medium|large-v3|small] [--source whisper|subs] [--lang en] [--force] [--dry-run]
```

Examples:

```sh
# one video, default Whisper "medium"
.venv/bin/python scripts/ingest.py k_paxCad6Kw

# whole playlist in order (playlist title + 1-based index recorded in frontmatter/manifest)
.venv/bin/python scripts/ingest.py --playlist "https://www.youtube.com/playlist?list=PLBu9owL7sQV9BRWQvGzBi-KkmqMR6qWK8"

# a watch URL that carries list= is treated as the playlist
.venv/bin/python scripts/ingest.py "https://www.youtube.com/watch?v=k_paxCad6Kw&list=PLBu9..."

# see what would happen without downloading anything
.venv/bin/python scripts/ingest.py --playlist URL --dry-run

# YouTube auto-captions instead of Whisper (fast, no punctuation, weaker on Tosca terms)
.venv/bin/python scripts/ingest.py k_paxCad6Kw --source subs

# redo an existing transcript with a bigger model
.venv/bin/python scripts/ingest.py k_paxCad6Kw --model large-v3 --force
```

`npm run ingest -- <url>` is the same thing if `package.json` wires it to this script.

## Flags

| flag | meaning |
|------|---------|
| `--source whisper` (default) | download audio, transcribe with faster-whisper (CPU, int8, beam 5, VAD, Tosca vocabulary prompt) |
| `--source subs` | download YouTube auto-subtitles (`raw/subs/NN-<id>.en.vtt`, reused if present), de-duplicate the rolling captions |
| `--model` | `small` / `medium` (default) / `large-v3` |
| `--lang` | language passed to Whisper / subtitle language (default `en`) |
| `--force` | re-transcribe even if `raw/transcripts/<id>.md` exists |
| `--dry-run` | list the plan (skip / transcribe / what is cached) and exit |

A video with an existing transcript is skipped unless `--force`. Errors on one
video are reported and the batch continues; a summary is printed at the end and
the exit code is 1 if anything failed.

## Model choice (Apple M4, 16 GB, CPU)

Measured on a 5-minute video (`k_paxCad6Kw`):

| source | wall time | notes |
|--------|-----------|-------|
| `subs` | 3 s | no punctuation, casing, or sentence breaks; brand/term spelling from YouTube ASR |
| `whisper --model medium` | 148 s (≈0.4x real time; 230 s incl. audio download) | punctuated, clean, Tosca terms mostly right; no hallucinated repeats |
| `whisper --model large-v3` | 642 s (≈1.8x real time) | slightly better brand spelling, but repeated a sentence twice and split "Scratchbook"; ~3 GB RAM |

Use `medium` for bulk runs (recommended). `large-v3` is 4x slower and was not
better on this material. `small` is only useful for smoke tests.

## Outputs

| path | content | committed |
|------|---------|-----------|
| `raw/audio/<id>.m4a` | downloaded audio (skipped if present) | no |
| `raw/subs/NN-<id>.en.vtt` | YouTube auto-captions (`--source subs`) | yes |
| `raw/transcripts/<id>.md` | frontmatter (id, title, url, channel, playlist, playlist_index, duration, upload_date, source, language, transcribed_at, status: raw) + paragraphs of ~30–60 s each starting with `[mm:ss]` | yes |
| `raw/transcripts/<id>.segments.json` | raw segments `[{start, end, text}]` | yes |
| `raw/manifest.json` | registry of ingested videos; `docs` per video is preserved across re-ingests and filled in by hand when docs are written | yes |
