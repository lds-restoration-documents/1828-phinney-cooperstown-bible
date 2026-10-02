# Audit spec — restoring silent corrections in an existing transcription

These are the instructions the auditing agents were given for the first pass of pages (PDF 1–329, the pages written before
the "never silently correct" rule existed). `<WORKDIR>` is the directory produced by `tools/render_pages.py`.

Context: `phinney-bible-pages/page-NNN.md` are transcriptions of the 1828 H. & E. Phinney Bible (public domain). They were
written by an earlier model that, in some cases, SILENTLY CORRECTED what the scan shows to what it believed was right. The
rule is: the file must show EXACTLY what is printed on the page image, including printer's errors, odd spellings, odd
reference numbers and letters, odd dates, odd punctuation. See `tools/transcription-spec.md` for the file format.

Inputs per PDF page N (NNNN = 4-digit, NNN = 3-digit) in `<WORKDIR>`: `img/pNNNN_1_lefttop.jpg`, `_2_leftbottom`, `_3_righttop`,
`_4_rightbottom` (readable crops, slight overlap at the middle), `img/pNNNN_0_overview.jpg` (layout only), `ocr/pNNNN.txt` (noisy helper).
If the crops are too small for margin digits, render zoomed strips of the margins from the PDF at 300–500 dpi and read those.

## Per-page procedure

1. View all 4 crops (overview only if layout unclear). Read the existing `page-NNN.md`.
2. Compare line by line, verse by verse, and note by note. Look especially for:
   - words/spellings changed from print (printer's typos like "tride", "peovle", "hunbred", "fo" for "of" etc. silently fixed);
   - marginal-note numbers (chapter/verse/book abbreviations) altered to a more plausible value, and dates (cir./Before CHRIST/Anno DOMINI) or folio numbers changed;
   - reference LETTERS in the text or margin that were assigned by sequence instead of copied (e.g. text shows 'r' but file says 'p');
   - wrong verse numbers, summary numbering (e.g. "17" printed where "1" expected) or running-head text/punctuation changed;
   - italics missing/added, words dropped or added, whole lines or notes missing, notes in the wrong margin order;
   - marginal notes that exist in the scan but are absent in the file (add them, in the correct place).
3. For every discrepancy, edit the page file (minimal change, never rewrite the whole file) so it matches the scan exactly.
   If the scan is genuinely unreadable at that spot, leave the existing reading and make sure it carries an
   `<!-- uncertain: ... -->` comment (add one if missing). Do not add uncertain comments to readings you can read clearly.
   Only change a marginal digit when you can read it clearly; do not swap one guess for another.
   Do NOT fix real errors by "improving" them: if the scan prints "assemby", the file must say "assemby".
   Keep existing uncertain/layout comments unless you verified them and they are now wrong.
4. If a change log was requested, append an entry after each page: `## Page NNN`, then either `- no changes` or one line per
   change: `- <where>: was "<old>" -> now "<new>" (<reason>)`. A log also lets an interrupted run resume by skipping logged pages.

CRITICAL: if the image tool fails or errors for a page, do not guess from the OCR; skip that page, do not record it as audited,
and list it as failed. If you hit an API/usage-limit error, just stop. Final reply: pages audited, total changes, pages failed (brief).
