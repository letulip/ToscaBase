# ToscaBase

Bilingual (English default, Russian) offline-capable knowledge base about **Tricentis Tosca**,
reworked from video tutorials into topic articles. Built with [Astro Starlight](https://starlight.astro.build),
searchable offline (Pagefind + service worker), installable as a PWA.

Live: https://letulip.github.io/ToscaBase/

## Structure

Docs are grouped into four mastery levels, each holding topic sections:

1. **Foundations**: getting started, modules, test cases
2. **Building tests**: test case design, standard modules, expressions, data and parameters, execution
3. **Specialised**: engines, API testing, requirements and reporting, best practices, troubleshooting
4. **Enterprise**: administration

Plus a reference section with a glossary and a curated learning path. Every page shows its level
and links back to the source videos with timestamps.

## Develop

```bash
npm install
npm run dev        # http://localhost:4321/ToscaBase/
npm run build      # static site in dist/ with service worker and search index
npm run preview
python3 scripts/check_links.py   # after a build: internal links that point nowhere
```

## Add content from a video

```bash
python3.11 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
npm run ingest -- "https://www.youtube.com/watch?v=..."            # Whisper (default)
npm run ingest -- --source subs "https://www.youtube.com/playlist?list=..."   # YouTube auto-subs, fast
```

Transcripts land in `raw/transcripts/`, the registry in `raw/manifest.json`. Then follow
`CONTENT_GUIDE.md` (deduplicate against existing docs, write or update EN docs, translate to RU,
add to the learning path). `raw/topic-map.md` records which videos feed which doc. See `AGENTS.md`
for the workflow and `scripts/README.md` for pipeline details.

## Sources

Content is reworked from the YouTube playlists "Tosca Tutorial from Scratch" (LambdaGeeks) and
"Tosca Tutorial" (QASCRIPT). Each page cites the exact videos it was derived from.
