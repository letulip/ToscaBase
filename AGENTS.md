# ToscaBase

Bilingual (EN default, RU) offline-capable PWA knowledge base about Tricentis Tosca.
Built with Astro + Starlight, hosted on GitHub Pages at https://letulip.github.io/ToscaBase/.

## Layout

- `src/content/docs/` English docs (source of truth). `src/content/docs/ru/` mirrors it in Russian.
  A missing RU page falls back to EN automatically, so EN may be ahead of RU.
- `raw/transcripts/<videoId>.md` cleaned transcripts produced by the ingest pipeline. Committed.
- `raw/audio/` downloaded audio. Not committed.
- `raw/manifest.json` registry of ingested videos and which docs were produced from each.
- `scripts/ingest.py` video -> transcript pipeline (yt-dlp + faster-whisper). Python venv in `.venv`.
- `CONTENT_GUIDE.md` rules for writing and translating docs. Read it before touching content.

## Adding a new video

1. `npm run ingest -- <youtube url or playlist url>` writes `raw/transcripts/<id>.md`.
2. In a Claude Code session: run the deduplication step from `CONTENT_GUIDE.md` (find existing
   docs on the same topics, write a merge plan), then update or create topic docs, then translate
   every touched page into `ru/`. Add new docs to `reference/learning-path.md`.
3. Record the produced doc paths in `raw/manifest.json` under that video.
4. `npm run build` must pass. Commit and push; GitHub Actions deploys.

## Development

Start the dev server in background mode: `astro dev --background`.
Manage it with `astro dev stop`, `astro dev status`, `astro dev logs`.

Astro docs: https://docs.astro.build. Starlight docs: https://starlight.astro.build.
