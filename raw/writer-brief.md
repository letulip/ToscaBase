# Writer brief (for doc-writing agents)

You are writing one section of ToscaBase. Repo: /Users/letulip/Projects/Claude/ToscaBase.
Read first: `CONTENT_GUIDE.md` (rules, frontmatter, taxonomy, levels, dedup), `raw/topic-map.md`
(which videos feed which doc), and the existing `src/content/docs/<section>/index.md`.

## Finding sources
`raw/manifest.json` lists every ingested video: id, title, playlist, playlist_index.
P2 lessons: match the title text "Lesson N". P1 parts: match "Part N" / "Part-N".
Transcript: `raw/transcripts/<id>.md` (frontmatter + `[mm:ss]` paragraphs).
Subtitle-based transcripts have no punctuation; read them as speech. Do not quote them.

## What to produce, per doc in your section
- `src/content/docs/<section>/<slug>.md` in English, then `src/content/docs/ru/<section>/<slug>.md`
  in Russian, same frontmatter with translated `title`/`description`. Both in the same pass.
- Frontmatter exactly as in CONTENT_GUIDE.md: `title`, `description`, `level`, `sidebar.order`
  (10, 20, 30... in learning order), `sources` (id, title, url, and `at` = mm:ss where the topic starts).
- Rewrite your section's `index.md` into a short overview that links every doc in the section,
  and create the `ru/<section>/index.md` twin.
- Internal links use the site base: `/ToscaBase/<section>/<slug>/` (EN) and `/ToscaBase/ru/<section>/<slug>/` (RU).
  Linking to a doc planned in `raw/topic-map.md` but not written yet is fine.
- Facts come from the transcripts only. Where the speaker is unclear or contradicts himself, say so in
  a `:::note`. Never invent UI paths, option names or values.
- Cover everything substantive from the source videos. The reader should not need the video.

## Do not
- Do not edit `raw/manifest.json`, `reference/*`, other sections, `astro.config.mjs`, or any file outside
  your section (EN and RU). Do not run `npm run build`, `astro dev`, or `astro check` (the coordinator
  builds after all sections land). Do not commit.
- Do not add glossary entries yourself; list new terms in your report.

## Report (keep under 60 lines)
1. Docs written: path, level, word count (EN), source ids used.
2. New glossary terms with a one-line definition each (EN).
3. Transcript ids that were missing or too garbled, with timestamps where a Whisper re-transcription would help.
4. Any topic from your rows in topic-map.md you deliberately merged, split, or skipped, and why.
