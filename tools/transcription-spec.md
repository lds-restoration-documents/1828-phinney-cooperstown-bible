# Transcription spec — 1828 H. & E. Phinney Bible (public-domain KJV printing)

These are the instructions the transcribing agents were given, one batch of pages at a time.
`<WORKDIR>` is the directory produced by `tools/render_pages.py`.

Inputs for PDF page N (NNNN = 4-digit zero-padded) in `<WORKDIR>`:
- `img/pNNNN_0_overview.jpg`: whole page, low-res (use to understand layout only)
- `img/pNNNN_1_lefttop.jpg`, `_2_leftbottom.jpg`, `_3_righttop.jpg`, `_4_rightbottom.jpg`: readable crops
  (crops overlap slightly at the middle; do not duplicate lines that appear in both top and bottom crops)
- `ocr/pNNNN.txt`: noisy OCR draft of the same page. Use it only as a helper; the IMAGE is authoritative.

Output: `phinney-bible-pages/page-NNN.md` (3-digit zero-padded PDF page number, e.g. `page-021.md`).

Procedure per page: read the overview, then all 4 crops, then the OCR draft; write the corrected text.
Read carefully; accuracy matters more than speed. Transcribe exactly what is printed (1828 spelling, punctuation;
words split across lines by a hyphen should be JOINED into the whole word; words hyphenated in the original compound stay hyphenated).

## Markdown format

```
<!-- PDF page NNN -->
**Header:** *The building of Babel.* | CHAPTER XI....XII. | *God calleth Abram.*   <- running head as printed, parts separated by " | " (omit line if none)

## CHAPTER XI.                         <- chapter headings as ##; book titles as #

1 One language in the world....3 The building of Babel....5 The confusion of tongues.   <- chapter summary: printed in upright (roman) type, so NO asterisks

30 And their dwelling was from Mesha, as thou goest unto Sephar, a <sup>r</sup>mount of the east.

31 These *are* the sons of Shem, ...
```

Rules:
- One paragraph per verse (blank line between verses). Verse number at the start as printed. The first verse of a chapter has no number (large initial); write it as plain text starting with the full word ("AND the whole...").
- Reading order: left column top to bottom, then right column top to bottom (unless the page is clearly single-column or laid out otherwise, in which case use sensible markdown; tables allowed). Where a full-width title or rule interrupts the columns, use logical reading order and describe the layout in an HTML comment.
- Italic words (supplied words in KJV) are `*italic*`. Small caps "LORD"/"GOD" are written LORD / GOD in capitals.
- Superscript reference letters/symbols in the text (a, b, c…, †, ‡, °, ||) are `<sup>a</sup>`, `<sup>†</sup>` etc., placed immediately before the word they mark.
- Pilcrows ¶ keep as ¶.
- A verse continuing from the previous page or onto the next page: just transcribe the fragment as it appears.
- Footer items (printed page numbers, signature marks, catchwords) go under the notes section as "Footer: ...".
- Library stamps, bookplates, blank pages: describe briefly in an HTML comment, and transcribe any legible text.

After the main text, add the marginal notes (outer-margin cross-references, dates like "Before CHRIST 2247.", and † "Heb." alternative-reading notes) as:

```

---

### Marginal notes

- Before CHRIST 2247.
- <sup>r</sup> Num. 23. 7.
- <sup>†</sup> Heb. *lip.*
```

listed in top-to-bottom order, left column's margin first then right column's. Omit the section if there are none.

Do not add commentary, summaries, or modern corrections. If a word is truly illegible write `[illegible]`.

## Addenda

Never silently "correct" a reading to what you think it should be. Write what the scan shows; if a reading is doubtful
or looks like a printer's error, keep it and add an HTML comment right after it, e.g. `ch. 11, 40 <!-- uncertain: maybe 1, 40 -->`.

Italic type is easy to miss. Check EVERY verse for italic words and write them as `*italic*`: supplied words (e.g. "*are*", "*is*", "*was*", "*the guilty;*"), italic words at the start of a verse (e.g. "44 *Of* the children…"), italic running heads, and italic words inside marginal notes (e.g. "Heb. *banner*"). Italic letters are slanted; compare against the surrounding roman type before deciding.

Chapter summaries (the short line under each chapter heading, e.g. "1 Solomon's buildings....17 He fetcheth gold from Ophir.") are printed in UPRIGHT roman type: write them as plain text, NOT italic. Running heads in the top margin ARE italic (as in the format example).

## How the agents were run (not part of the spec they saw)

- The agent had to view the crop images for every page. If the image tool failed, it stopped and reported the page as failed; transcribing from the OCR text alone was not allowed.
- Pages were processed in batches of 16, one page at a time, writing each file right after reading it; a batch skipped pages whose output file already existed, so an interrupted batch could resume.
