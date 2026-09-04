# Merge brief (adding a new playlist into existing docs)

Read first: CONTENT_GUIDE.md (rules, dedup, RU rules) and the "Playlist 3" table at the end of
raw/topic-map.md. Transcripts: raw/transcripts/<id>.md; ids and titles are in raw/manifest.json
(playlist "TRICENTIS Tosca Automation Tutorial", titles "TRICENTIS Tosca 16.0 - Lesson NN | ...").
These transcripts are subtitle-based (no punctuation); read them as speech, never quote them.

For each lesson assigned to you:
1. Read the transcript fully. List the facts it adds that the target doc does not have yet
   (Tosca 16 UI paths, new options, extra examples, a clearer explanation) and the facts that
   contradict the doc.
2. Read the target EN doc. Merge: add the new facts into the right existing section (or a new
   `##` if the doc has no place for them), keep the doc's structure and voice, do not duplicate
   what is already there, do not restate the same procedure twice. If P3 contradicts an earlier
   source, say so in a short `:::note` naming both lessons rather than silently picking one.
3. Add the lesson to the doc's `sources` (id, exact title from manifest, url, `at` = where the
   relevant part starts). Keep the doc under ~1250 words: if merging pushes it over, trim
   redundancy first; split only if truly needed and say so.
4. Mirror every change in the RU twin (same rules: Tosca terms in English, « — » dashes).
5. NEW docs marked in the topic map: write them from scratch per CONTENT_GUIDE (frontmatter,
   level of their section, sidebar.order after the existing docs, RU twin, links from the
   section index.md in both languages).
6. Do not touch docs outside your sections; if a lesson's fact belongs to another section's
   doc, put it in your report under "for other sections" instead of writing it there.
7. Do not edit reference/, raw/manifest.json, astro.config.mjs. No builds, no commits.

Report (under 40 lines): per target doc, what was added (2–5 bullets), contradictions noted,
new docs written with word counts, "for other sections" items, lessons you judged fully
redundant (nothing new) — still add them to `sources` of the doc they confirm.
