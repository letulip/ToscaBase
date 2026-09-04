# Note-resolution brief

Context: ToscaBase docs were written from YouTube auto-subtitle transcripts. Writers left
`:::note` / `:::caution` admonitions wherever the subtitles were unclear (inaudible syntax,
garbled names, uncertain values, "as spoken in the source"). The videos listed in
`raw/whisper-wanted.txt` have since been re-transcribed with Whisper: `raw/transcripts/<id>.md`
now has `source: "whisper:medium"` and punctuated, much cleaner text. All 14 P1 videos
(LambdaGeeks "Part N") are Whisper transcripts too.

Task, for every EN doc in your sections (and its RU twin under `src/content/docs/ru/`):
1. Find admonitions about transcript uncertainty (grep for: subtitle, transcript, audible,
   inaudible, unclear, heard, spoken, garbled, "not shown", "not stated", "cannot confirm",
   uncertain, reconstructed, phonetic, "as spoken"). Also look at `<sep>` placeholders and
   "probably"/"most likely" hedges near syntax.
2. For each, open the Whisper transcript of the cited video (the doc's `sources`, use the `at`
   timestamp and search nearby) and decide:
   - RESOLVE: the transcript now makes it clear -> state the fact plainly in the body, delete the note.
   - TIGHTEN: still ambiguous (e.g. the value is only shown on screen, never spoken) -> keep a
     shorter note saying exactly what is unverified, drop the "subtitle" explanation.
   - KEEP: genuinely unverifiable -> leave as is.
3. While reading the transcript for a note, if you notice a nearby fact in the doc that the
   Whisper transcript contradicts (a value, a menu path, a name), fix it and mention it in the report.
   Do not rewrite anything else; do not restructure docs.
4. Mirror every change in the RU twin (same rules as CONTENT_GUIDE.md: Tosca terms in English,
   « — » dashes).
5. Frontmatter: do not change `sources` except to correct an `at` timestamp if it was clearly wrong.

Do not touch files outside your sections. No builds, no commits.

Report (under 30 lines): per doc, each note -> RESOLVED (the fact) / TIGHTENED / KEPT (why);
any contradictions fixed.
