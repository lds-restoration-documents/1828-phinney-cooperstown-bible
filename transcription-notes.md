# Transcription notes — H. & E. Phinney Bible (1828)

Companion to the `phinney-bible-pages/` folder (one markdown file per PDF page). This file records how the text was produced, the conventions used, and every place where the transcription is doubtful, illegible, or reflects a judgment call.

## 1. Source and method

- **Source:** `holybiblecontain00cann.pdf`, 884 page images (scans of the 1828 H. & E. Phinney stereotype edition, Cooperstown, N.Y.; library copy with a bookplate). Page numbers in the file names (`page-001.md` … `page-884.md`) are **PDF page numbers**, not the printed folio numbers. The printed folio is recorded in each page's `Footer:` line when visible.
- **Process:** each page was rendered at 2x and cut into four overlapping crops (top/bottom of each column) plus a low-resolution overview. An AI model read the crops and the embedded (very noisy) OCR text and wrote the page. **The image was treated as authoritative; the OCR text was only a helper.** Pages were processed in batches of 16 by separate agents.
- **Models:** pages 1–329 were transcribed by Claude Opus 5.5, except pages 213, 214, 230, 246 and 274–278, 290–294, 308–310, 324–326, which were done by Claude Sonnet 5.5 (gap fills after a usage-limit interruption). Pages 330–884 were transcribed by Claude Sonnet 5.5. A two-page comparison (pages 75 and 124) found similar quality: identical verse text apart from one italic word, with differences mostly in the tiny marginal-reference digits.
- **Redone pages:** pages 213, 214, 230, 246, 274, 275, 276, 277 were first produced from OCR text only (the image tool failed) and were then redone from the page images. No OCR-only pages remain.
- **Review:** (1) a scripted consistency pass checked structure and formatting for all 884 files; (2) the 309 Opus-written pages (PDF 1–329 except the 20 Sonnet gap-fill pages) were **audited page by page against the scans** for silent corrections (see §6); (3) the Sonnet-written pages (330–884 and the gap fills) have **not** been audited this way, though they were written under the stricter 'write what the scan shows' rule. No page has been proofread by a person.

## 2. Conventions

- One markdown file per page, starting with `<!-- PDF page NNN -->`.
- `**Header:**` line = running head as printed, left/centre/right parts separated by ` | ` (omitted if the page has none, e.g. pages that open with a book title).
- Book titles are `# ¶ …` headings; chapter headings are `## CHAPTER X.`; chapter summaries are plain upright text (they are printed upright), running heads and Psalm titles are italic.
- One paragraph per verse, verse number first. The first verse of a chapter has no number (large drop-cap initial in the original); its first word is written in full.
- Reading order is left column top to bottom, then right column. Where a full-width title or rule interrupts the columns, logical reading order was used and an HTML comment describes the layout; some such pages use `### Left column` / `### Right column` subheadings.
- Italic type (words supplied by the translators) is `*italic*`. Small-capital LORD/GOD are written in capitals.
- Reference letters and symbols printed in the text (a, b, c…, †, ‡, §, ‖, ¶, `*`) are `<sup>x</sup>` placed immediately before the word they mark. A literal asterisk mark is written `<sup>\*</sup>`.
- Hyphenated line-end words are joined; words hyphenated in the original stay hyphenated. 1828 spelling and punctuation are kept as printed, including printer's errors (flagged where noticed).
- Marginal notes (cross-references, dates such as "Before CHRIST 2247.", "Heb." alternative readings) are listed in a `### Marginal notes` section after a `---` rule: left margin first, then right margin, top to bottom. A note whose letter is not visible is listed without a letter.
- Printed signature marks (e.g. "3 B") and page numbers are on `Footer:` lines. A page where no folio is visible has no Footer line (page 434).
- Blank pages, covers and stamps are a short descriptive HTML comment. Tables and indexes use markdown tables.
- Doubtful readings are marked in place with `<!-- uncertain: … -->`; unreadable text is `[illegible]`.

## 3. Silent corrections and judgment calls

The early Opus batches (PDF pages 1–329) were written before the rule 'never silently correct a reading' existed, and some readings were quietly changed. These pages were **audited against the scans** (§6) and the corrections were reversed where the scan clearly showed otherwise. Confirmed examples:

- **p. 63:** running head restored to the printed "peovle" (printer's error for "people").
- **p. 124:** "Increased 3100" restored to "31000" as printed.
- **p. 95:** "2 Sam. 38, 12" is printed that way (a printer's error for 13:12) and is now kept; "Gen. 19, 33" as printed.
- **p. 73:** "sabbat fo rest" and "Ged" restored; **p. 21:** "wcrld"; **p. 100:** "and 1 have broken"; **p. 125:** "of he LORD"; **p. 184:** "Israei said"; **p. 190:** "ana my concubine"; **p. 175:** "2 Chren. 15, 2"; **p. 162:** "Sinar"; **p. 70:** "sittings of stones".
- **p. 134:** the margin note "ch. 11, 40" is as printed.
- **p. 113:** period after "My lord Moses." as printed; many margin notes across the Opus range had commas/periods added or dropped to match the print.
- **Page 30 running head:** the type is damaged; it was changed to "Kevekun" with an uncertain comment (may be "Rebekah").
- **Page 209:** a † note reads "toth-day of this business" (uncertain).

Hundreds of marginal digits (chapter/verse numbers) were also changed during the audit only where they could be read clearly in zoomed (400–600 dpi) renders. Where digits such as 3/5/8/9 could not be told apart even zoomed, the earlier reading was kept with an `<!-- uncertain -->` comment.

Residual risk in the Sonnet-written pages (330–884 and the 20 gap-fill pages): the agents reported a few places where they chose the sequence-implied reference letter or reading over what the scan showed (e.g. p. 475 v. 5 "the man that"; pp. 501, 503, 415 reference letters; p. 861 "Babylon"), each flagged by a comment. They have not been audited against the scans.

Other deliberate decisions:

- Chapter-summary numbering that looks wrong in print (e.g. p. 324 "17 The decree of Artaxerxes…", p. 808 "3…") is kept as printed and flagged.
- Running heads that name a different chapter range than the page content (e.g. p. 119 "CHAPTER XX.", p. 571 "CHAPTER I.") are kept as printed.
- Page 754's folio looks like "641" where the sequence implies 644; recorded as read.
- Printed typos are kept (e.g. "hunbred" p. 103, "tride" p. 103, "assemby" p. 116, "mv" p. 382, "hastbrought" p. 389, "Lord fo heaven" p. 782, "wno" p. 649).
- Headings partly cut off by the scan edge or a fold are written as far as legible (e.g. p. 861 "upon Ba…" completed as "Babylon" and flagged).
## 4. Totals (after the audit)

- Pages: 884
- `uncertain` comments: 2355
- `[illegible]` marks: 237
- Other explanatory comments (layout, blank pages, stamps, printer oddities): 166

**Important:** counts are not a measure of accuracy. The audit removed uncertain comments where a zoom read clearly and added them where it did not, so the Opus pages are now flagged comparably to the later pages. Even so, the small marginal print probably still contains unflagged misreads.

### By section (uncertain / illegible / other)

| Section | uncertain | illegible | other |
|---|---:|---:|---:|
| Front matter | 0 | 0 | 7 |
| HOLY BIBLE, | 0 | 0 | 1 |
| CONTENTS | 0 | 0 | 5 |
| THE FIRST BOOK OF MOSES, CALLED †GENESIS. | 22 | 5 | 14 |
| The SECOND Book of Moses, called EXODUS. | 16 | 13 | 1 |
| The THIRD Book of Moses, called LEVITICUS. | 10 | 6 | 0 |
| The FOURTH Book of Moses, called NUMBERS. | 11 | 4 | 0 |
| The FIFTH Book of Moses, called DEUTERONOMY. | 35 | 5 | 0 |
| The BOOK of JOSHUA. | 20 | 4 | 0 |
| The BOOK of JUDGES. | 17 | 19 | 0 |
| The BOOK of RUTH. | 8 | 1 | 0 |
| The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. | 77 | 8 | 3 |
| The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. | 49 | 21 | 5 |
| The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. | 54 | 14 | 10 |
| The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. | 35 | 13 | 19 |
| The FIRST Book of the CHRONICLES. | 48 | 18 | 5 |
| The SECOND Book of the CHRONICLES. | 85 | 13 | 1 |
| EZRA. | 18 | 2 | 1 |
| The BOOK of NEHEMIAH. | 20 | 1 | 0 |
| The BOOK of ESTHER. | 10 | 1 | 0 |
| The BOOK of JOB. | 56 | 1 | 0 |
| The BOOK of PSALMS. | 114 | 4 | 4 |
| The PROVERBS. | 30 | 0 | 2 |
| ECCLESIASTES, or the PREACHER. | 9 | 0 | 0 |
| The SONG of SOLOMON. | 7 | 0 | 0 |
| The BOOK of the Prophet ISAIAH. | 66 | 3 | 3 |
| The BOOK of the Prophet JEREMIAH. | 70 | 3 | 0 |
| The LAMENTATIONS of JEREMIAH. | 15 | 1 | 0 |
| The Book of the Prophet EZEKIEL. | 59 | 4 | 0 |
| The Book of DANIEL. | 22 | 0 | 1 |
| HOSEA. | 13 | 2 | 0 |
| JOEL. | 9 | 0 | 1 |
| AMOS. | 13 | 1 | 0 |
| OBADIAH. | 7 | 0 | 0 |
| JONAH. | 3 | 0 | 0 |
| MICAH. | 12 | 3 | 0 |
| NAHUM. | 1 | 0 | 0 |
| HABAKKUK. | 9 | 0 | 0 |
| ZEPHANIAH. | 3 | 0 | 0 |
| HAGGAI. | 2 | 0 | 0 |
| ZECHARIAH. | 13 | 1 | 0 |
| MALACHI. | 6 | 0 | 0 |
| A Table | 4 | 0 | 1 |
| A TABLE OF OFFICES AND CONDITIONS OF MEN. | 1 | 0 | 1 |
| Family Record. | 0 | 0 | 4 |
| I. ESDRAS, | 43 | 1 | 0 |
| II. ESDRAS, | 38 | 0 | 0 |
| TOBIT. | 11 | 0 | 2 |
| JUDITH. | 23 | 0 | 3 |
| The WISDOM of SOLOMON. | 17 | 0 | 6 |
| The Wisdom of JESUS the Son of SIRACH, OR, ECCLESIASTICUS. | 1 | 0 | 0 |
| The Prologue of the Wisdom of JESUS, the Son of SIRACH. | 46 | 3 | 0 |
| BARUCH. | 6 | 0 | 0 |
| The EPISTLE of JEREMY. | 1 | 0 | 0 |
| The SONG of the Three Holy Children, | 6 | 0 | 0 |
| The History of SUSANNA, | 1 | 0 | 1 |
| The Prayer of MANASSES, king of Judah, when he was holden captive in Babylon. | 2 | 0 | 1 |
| The First Book of the MACCABEES. | 50 | 2 | 0 |
| The Second Book of the MACCABEES. | 9 | 1 | 3 |
| The GOSPEL according to St. MATTHEW. | 71 | 3 | 0 |
| The GOSPEL according to St. MARK. | 40 | 2 | 2 |
| The GOSPEL according to St. LUKE. | 64 | 7 | 1 |
| The GOSPEL according to St. JOHN. | 37 | 8 | 1 |
| The ACTS of the Apostles. | 71 | 2 | 0 |
| The Epistle of PAUL, the Apostle, to the ROMANS. | 151 | 0 | 0 |
| The First Epistle of PAUL, the Apostle, to the CORINTHIANS. | 107 | 1 | 2 |
| The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. | 53 | 0 | 6 |
| The Epistle of PAUL, the Apostle, to the GALATIANS. | 33 | 0 | 4 |
| The Epistle of PAUL, the Apostle, to the EPHESIANS. | 53 | 0 | 4 |
| The Epistle of PAUL, the Apostle, to the PHILIPPIANS. | 17 | 1 | 0 |
| The Epistle of PAUL, the Apostle, to the COLOSSIANS. | 6 | 0 | 0 |
| The First Epistle of PAUL, the Apostle, to the THESSALONIANS. | 5 | 0 | 0 |
| The Second Epistle of PAUL, the Apostle, to the THESSALONIANS. | 2 | 1 | 0 |
| The First Epistle of PAUL, the Apostle, to TIMOTHY. | 9 | 1 | 1 |
| The Second Epistle of PAUL, the Apostle, to TIMOTHY. | 9 | 1 | 0 |
| The Epistle of PAUL, to TITUS. | 1 | 0 | 0 |
| The Epistle of PAUL to PHILEMON. | 5 | 0 | 0 |
| The Epistle of PAUL, the Apostle, to the HEBREWS. | 67 | 9 | 2 |
| The general Epistle of JAMES. | 29 | 1 | 3 |
| The First Epistle General of PETER. | 27 | 1 | 2 |
| The Second Epistle general of PETER. | 25 | 0 | 3 |
| The First Epistle general of JOHN. | 19 | 0 | 3 |
| The Second Epistle of JOHN. | 11 | 0 | 2 |
| The General Epistle of JUDE. | 9 | 0 | 2 |
| The REVELATION of St. JOHN the Divine. | 39 | 1 | 3 |
| AN INDEX TO THE HOLY BIBLE; | 31 | 13 | 8 |
| TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: | 31 | 7 | 12 |

## 5. Per-page log

Every flagged item as it currently stands, in page order ("Section" = most recent book title; quotes are from the page files in `phinney-bible-pages/`).

### Page 001 — Front matter (Opus 5.5)

- *Note:* front cover: worn dark brown leather binding, no legible text

### Page 002 — Front matter (Opus 5.5)

- *Note:* inside front cover (pastedown): library bookplate, yellow with red border, illustration of a cowboy on a rearing horse; barcode label below. Rest of page blank.
- *Note:* library bookplate:
LIBRARY
Brigham Young University
AMERICANA /Rare
BS
185
1828
copy 6 (struck through; "C6" handwritten below)
barcode label: BRIGHAM YOUNG UNIVERSITY — 3 1197 22194 9792

### Page 003 — Front matter (Opus 5.5)

- *Note:* blank flyleaf

### Page 004 — Front matter (Opus 5.5)

- *Note:* blank flyleaf

### Page 005 — Front matter (Opus 5.5)

- *Note:* blank flyleaf

### Page 006 — Front matter (Opus 5.5)

- *Note:* blank flyleaf

### Page 007 — HOLY BIBLE, (Opus 5.5)

- *Note:* title page; faint pencilled call number in upper left margin, partly legible: "Mor 220.53 B47 1828" (uncertain)

### Page 010 — CONTENTS (Opus 5.5)

- *Note:* printed in four columns; read column by column. "chap." appears after the first entry of each book and at the head of each column.

### Page 011 — CONTENTS (Opus 5.5)

- *Note:* printed in four columns; read column by column.

### Page 012 — CONTENTS (Opus 5.5)

- *Note:* printed in four columns; read column by column.

### Page 013 — CONTENTS (Opus 5.5)

- *Note:* printed in four columns; read column by column.

### Page 014 — CONTENTS (Opus 5.5)

- *Note:* printed in four columns; read column by column. Lower half of page blank.

### Page 015 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Note:* reference partly cut off at page edge; uncertain

### Page 016 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Note:* chapter number partly obscured
- *Note:* second reference uncertain
- *Note:* numbers uncertain
- *Note:* first reference uncertain
- *Uncertain:* verse number smudged

### Page 017 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Note:* verse number 2 not visible in the scan
- *Note:* reference faint; uncertain
- *Note:* numbers faint; uncertain
- *Note:* last number uncertain
- *Note:* right margin cropped and blurred; several numbers uncertain
- *Note:* faint; attribution uncertain
- *Uncertain:* 
- *Illegible near:* `- [illegible] Ezek. 9, 4. ch. 6, 11. <!-- f`

### Page 018 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Note:* faint; uncertain
- *Note:* last digit partly clipped
- *Note:* faint; uncertain
- *Uncertain:* digits degraded, maybe 2118 or 2113
- *Uncertain:* faint, reads 3, 1?

### Page 020 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* second reference number clipped, scan shows ", 17."
- *Illegible near:* `- <sup>c</sup> Prov. 10, [illegible], 17. Gal. 6, 1. <!-- uncertai`

### Page 021 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* second number degraded, maybe 19

### Page 022 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* last digit degraded, may be 3
- *Uncertain:* 16 degraded, may be 18

### Page 025 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* first digit degraded, may be 24

### Page 026 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* number degraded, scan shows "1?, 1"
- *Uncertain:* last digit degraded, may be 68

### Page 027 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* second letter of "sojourned" looks like q, stray tail on o
- *Uncertain:* chapter number degraded, scan shows "1?"

### Page 030 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* damaged type, may be Rebekah
- *Uncertain:* last digit degraded, may be 36
- *Uncertain:* chapter number in chap. reference degraded, scan shows "3?"

### Page 031 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* scan degraded, reads "Ps. 3 ?5, 10"
- *Uncertain:* last digits of Zech. and Psalm refs clipped
- *Illegible near:* `- <sup>y</sup> ch. 21, 25. Song 4, 15. Ps. [illegible], 10. <!-- uncertain: scan deg`

### Page 032 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* last digit degraded

### Page 035 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Illegible near:* `- <sup>s</sup> Ex. 3, 7. Eph. 1, [illegible]`

### Page 038 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Illegible near:* `- <sup>t</sup> 1 Tim. 6, 10. Mat. 8, 19, 20. [illegible] 6, 28.`

### Page 049 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* second digit maybe 6 (26, 8)

### Page 050 — THE FIRST BOOK OF MOSES, CALLED †GENESIS. (Opus 5.5)

- *Uncertain:* maybe 33
- *Uncertain:* last digit maybe 3

### Page 051 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* word(s) after "she" partly obscured in scan

### Page 057 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* scan degraded
- *Uncertain:* scan degraded
- *Uncertain:* scan degraded; reads ch. 9, 2?
- *Uncertain:* scan degraded

### Page 058 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* scan shows "insti'uted" (letters damaged/printed oddly)
- *Uncertain:* last digit blotted (28 or 29)

### Page 060 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* 15 vs 13

### Page 062 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* terminal punctuation may be period

### Page 063 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* printed "peovle" (printer's error for people)

### Page 069 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* scan shows only "ch. 30," with the number faded or missing
- *Uncertain:* final number faded in scan

### Page 070 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Illegible near:* `- <sup>m</sup> Num. [illegible] 17. 1 Chron. [illegible] 1. A`
- *Illegible near:* `- <sup>m</sup> Num. [illegible] 17. 1 Chron. [illegible] 1. Acts 1, 21.`
- *Illegible near:* `- <sup>n</sup> ch. 29, 3[illegible]. Ps. 93, 5. Zech. 14, 20.`
- *Illegible near:* `- <sup>b</sup> ch. 12, [illegible]`
- *Illegible near:* `- <sup>c</sup> ch. 30, [illegible] 1 John 2, [illegible]`
- *Illegible near:* `- <sup>c</sup> ch. 30, [illegible] 1 John 2, [illegible]`
- *Illegible near:* `- <sup>e</sup> ch. 26, [illegible] Acts 14, [illegible] & 6, 5,`
- *Illegible near:* `- <sup>e</sup> ch. 26, [illegible] Acts 14, [illegible] & 6, 5, 6.`
- *Illegible near:* `- <sup>f</sup> ch. 30, [illegible] Isa. 1, 16. 1 Tim. 3, 2, 3. T`

### Page 072 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Uncertain:* verse number printed as a small "o" (damaged 8?)

### Page 073 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Note:* printed in small caps
- *Uncertain:* "Ye" not printed in scan, only a stray mark
- *Uncertain:* dagger not visible in scan, only a speck after "holy"
- *Uncertain:* printed "Ged" (damaged o?)

### Page 079 — The SECOND Book of Moses, called EXODUS. (Opus 5.5)

- *Illegible near:* `- <sup>n</sup> ch. 38, 30. 1 Kings 8, [illegible]`
- *Illegible near:* `- <sup>o</sup> Heb. 5, [illegible]`
- *Illegible near:* `- <sup>r</sup> Gen. 1, 31. chap. [illegible]`
- *Illegible near:* `- <sup>s</sup> Gen. 14, 19. 1 Tim. 1, [illegible]`

### Page 082 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* chapter digits faint, perhaps 28, 9

### Page 083 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* last digit unclear, perhaps 6
- *Illegible near:* `- <sup>n</sup> Ex. 12, [illegible] <!-- uncertain: last digit un`

### Page 084 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* verse digit smudged, looks like 8 or 9
- *Illegible near:* `- <sup>a</sup> ch. 5, [illegible] <!-- uncertain: verse digit s`

### Page 089 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* chapter digit blurred, could be 3 or 5

### Page 092 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* printed margin letter looks like b or h, not a
- *Uncertain:* last digit prints like a broken t/6

### Page 093 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* print reads like 15/13, 18 (damaged)

### Page 095 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* first chapter digit damaged (looks like ?9); verse digits print as 33
- *Uncertain:* first digit heavy/blotted, reads 3 not 1; second 8

### Page 096 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Uncertain:* last digit faint, 3 or 5

### Page 097 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Illegible near:* `- <sup>k</sup> Deut. 16, 12. Luke 3, [illegible] Acts 4, [illegible] Rom. 8, 2`
- *Illegible near:* `k</sup> Deut. 16, 12. Luke 3, [illegible] Acts 4, [illegible] Rom. 8, 2. Gal. 3, 2. Eph. 1,`
- *Illegible near:* `- <sup>l</sup> ch. 19, 9. Deut. 24, [illegible]`

### Page 101 — The THIRD Book of Moses, called LEVITICUS. (Opus 5.5)

- *Illegible near:* `on,* ver. 28, 29. Num. 18, 14. & 21, 2. Deut. 17. [illegible]`

### Page 104 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* first chapter digit pair partly damaged, reads 12
- *Illegible near:* `- [illegible]ses 1, 2. chap. 1, 13. verse 2`

### Page 105 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* last digit may be 3
- *Uncertain:* chapter number may be 25 or 26

### Page 113 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Illegible near:* `- <sup>t</sup> Acts [illegible]`

### Page 115 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* print too small/damaged; first ref looks like "Deut. 1, 4?" and second "Isa. 9, 12"
- *Uncertain:* Deut. 8, 3 vs 8, 8; last digit damaged
- *Illegible near:* `- <sup>g</sup> [illegible] 1, 4. [illegible]s. 9, 12. <!`
- *Illegible near:* `- <sup>g</sup> [illegible] 1, 4. [illegible]s. 9, 12. <!-- uncertain: prin`

### Page 122 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* scan may print "ch. 28, 2"; first digit of chapter looks like 8 or 3
- *Uncertain:* last digit smudged (9 vs 5)

### Page 127 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* second digit of chapter smudged (28 vs 25 vs 23)

### Page 129 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* print blurred, appears "Isaiah 46 :"
- *Uncertain:* print reads "Josh. 17." with faint/blurred marks after 17

### Page 131 — The FOURTH Book of Moses, called NUMBERS. (Opus 5.5)

- *Uncertain:* last number appears as 6, 13 in print; too blurred to be sure

### Page 133 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* final digit looks like 1 in print (Num. 14, 21?); too faint to be sure

### Page 134 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* last digit blurred, may be 9
- *Uncertain:* print blurred, first letter and final digits unclear (Rev./Lev. 17, 1?)

### Page 135 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* first number after "Num. 20," is 3 or 8

### Page 137 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Illegible near:* `- <sup>o</sup> 2 Pet. 1, [illegible]`

### Page 138 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* print small, last digit may be 1
- *Uncertain:* print small, last digit may be 3

### Page 139 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* print small, 136, 15 possible
- *Uncertain:* print small, 106, 19 possible
- *Uncertain:* print small, Luke 12, 43 possible

### Page 141 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* summary number prints like "1S", possibly 18

### Page 142 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* print small, last digit may be 3
- *Uncertain:* print small, chapter digit may be 3
- *Uncertain:* print small and blurred

### Page 143 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* print small, may read 18, 20

### Page 144 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* print small, last digit may be 0

### Page 147 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* scan shows only a broken dot where the reference letter should be; margin has n Ps. 44, 2, 3, 4
- *Uncertain:* last number prints as 12,16 or 12,18, too small to be sure

### Page 149 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* chapter digit prints as 2, 3 or 8 (small/damaged)
- *Uncertain:* last digit damaged, looks like 3 or 8

### Page 151 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* digit before '4.' looks like 3 or 8
- *Uncertain:* last digit of 'ch. 11, 30' is partly clipped (reads 3 then 0-like); Judges 9, 7 last digit blurred
- *Uncertain:* first number blurred, could be 3 or 8
- *Illegible near:* `- <sup>s</sup> Gen. 29, [illegible] 4.`

### Page 152 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* first digit before Chron. damaged
- *Uncertain:* 51 may be 31; last number small/damaged
- *Uncertain:* 28 or 23

### Page 153 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* Ps. number may read 85
- *Uncertain:* scan reads roughly 'ch. 4, 3?. / 34. & 17, 19'; digits small

### Page 154 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* note label, if any, illegible
- *Uncertain:* scan reads roughly 'Acts 2?, 30'
- *Illegible near:* `- <sup>u</sup> ch. 29, 18. Acts [illegible] <!-- uncertain: scan reads ro`

### Page 155 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* last number may read 31
- *Uncertain:* 28 damaged

### Page 156 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* book name garbled, perhaps Lam.
- *Uncertain:* reference letter not visible in scan
- *Uncertain:* last digit small/clipped, may be 3
- *Illegible near:* `- <sup>i</sup> [illegible] 2, 6. <!-- uncertain: book na`

### Page 157 — The FIFTH Book of Moses, called DEUTERONOMY. (Opus 5.5)

- *Uncertain:* second line is a blot, roughly 'P.'
- *Illegible near:* `- <sup>u</sup> Num. 16, [illegible] <!-- uncertain: second line i`

### Page 158 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* number garbled in scan
- *Illegible near:* `- <sup>f</sup> ch. [illegible], 5. <!-- uncertain: number ga`

### Page 159 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* book abbreviation garbled in scan, possibly Rev.
- *Uncertain:* number under a blot, roughly 'Ps. 29, 10'
- *Illegible near:* `- <sup>b</sup> Ps. [illegible], 10. & 77, 19. <!-- uncertain`

### Page 160 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* no period visible at end of head, a stray mark follows
- *Uncertain:* print reads roughly 'Ps. 65; 8.' last digit 3 or 8
- *Uncertain:* print reads roughly 'Num. 13.' then '29.'
- *Uncertain:* last digit may be 8

### Page 161 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* last digit may be 3

### Page 163 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* last digit may be 8
- *Uncertain:* 135 partly smudged

### Page 165 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* second digit may be 3

### Page 167 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* last digit may be 8
- *Uncertain:* 18 partly damaged, may be 13

### Page 170 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* first digit 1 appears missing or faded in print

### Page 171 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* chapter number and first words of the Num. reference are blotted in print
- *Uncertain:* digits blotted in print
- *Illegible near:* `- <sup>d</sup> Num. 35, 25. John [illegible], 36. <!-- uncertain: chapter`
- *Illegible near:* `- <sup>e</sup> ch. 21, 32. 2 Kings 15, 2[illegible]. <!-- uncertain: digits blott`

### Page 173 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* first number may be 13

### Page 174 — The BOOK of JOSHUA. (Opus 5.5)

- *Uncertain:* "God" letters damaged in print
- *Uncertain:* print may read "2 Cpr."
- *Uncertain:* last digit may be 9

### Page 175 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* last digit blotted (may be 8)
- *Uncertain:* leading number blotted
- *Illegible near:* `- <sup>o</sup> Deut. 34, 5. 2 Tim. 4, [illegible] <!-- uncertain: last digit bl`
- *Illegible near:* `- <sup>r</sup> [illegible] Kings 1, 2. <!-- uncertain: l`

### Page 176 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* chapter and verse digits blotted
- *Uncertain:* digits blotted
- *Uncertain:* print cut off after "Ps. 4"
- *Illegible near:* `- <sup>s</sup> ch. 4, 19. Ps. 44, [illegible] <!-- uncertain: print cut off`

### Page 179 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* print blurred, second number may read 18
- *Uncertain:* last digit blurred, 33 or 34

### Page 182 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* last digit blurred

### Page 183 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* last digit blurred
- *Uncertain:* last digit cut/blurred
- *Uncertain:* last digit blurred, 13 or 18
- *Uncertain:* last digit blurred
- *Illegible near:* `- <sup>u</sup> 2 Sam. 1[illegible] 21.`
- *Illegible near:* `- <sup>c</sup> Gen. 31, 48. Num. 32, [illegible]`
- *Illegible near:* `- <sup>h</sup> ch. 2, 1[illegible]`
- *Illegible near:* `- <sup>k</sup> 1 Sam. [illegible] 2.`
- *Illegible near:* `- <sup>n</sup> 2 Chr. [illegible] 5.`

### Page 185 — The BOOK of JUDGES. (Opus 5.5)

- *Illegible near:* `red, however to be consecrated to God,* Lev. 27, 1[illegible]. Isaiah 66, 3.`
- *Illegible near:* `- <sup>g</sup> Lev. 11, [illegible]`
- *Illegible near:* `- <sup>i</sup> Num. 6, [illegible]`
- *Illegible near:* `- <sup>k</sup> 1 Sam. [illegible] 13. 2 Sam. 8, [illegible]`
- *Illegible near:* `- <sup>k</sup> 1 Sam. [illegible] 13. 2 Sam. 8, [illegible]`
- *Illegible near:* `- <sup>l</sup> Josh. 14, 6. 2 Kings 4, [illegible] 1 Tim. 6, 11.`
- *Illegible near:* `- <sup>m</sup> 1 Tim. [illegible] 9.`
- *Illegible near:* `- <sup>o</sup> Ps. [illegible] Mat. 7, [illegible]`
- *Illegible near:* `- <sup>o</sup> Ps. [illegible] Mat. 7, [illegible]`

### Page 186 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* terminal mark may be a colon
- *Illegible near:* `- <sup>c</sup> 1 Sam. 15, 3[illegible] 1 Cor. 12, 21.`

### Page 187 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* second digit of chapter damaged, may read 16

### Page 188 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* last digit looks like 6 (not 8), no final period

### Page 190 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* print blurred; digits may read Gen. 24, ch. 19, 28

### Page 191 — The BOOK of JUDGES. (Opus 5.5)

- *Uncertain:* print may show a period after 8 instead of comma
- *Illegible near:* `, 27. Ps. 103, 9. Isa. 1, 9. Jer. 14, 7. Lam. 3, 5[illegible] Hab. 3, 2.`

### Page 192 — The BOOK of RUTH. (Opus 5.5)

- *Uncertain:* second digit damaged in print, may read 1912 or 1512
- *Illegible near:* `- <sup>†</sup> Heb. [illegible] *cried peace,* Ps. 78, 38. Is`

### Page 193 — The BOOK of RUTH. (Opus 5.5)

- *Uncertain:* printed 'tna.' (printer's error for 'that'?)
- *Uncertain:* end of note clipped at page edge

### Page 194 — The BOOK of RUTH. (Opus 5.5)

- *Uncertain:* last digit obscured
- *Uncertain:* last digit of Prov. reference smudged (26 or 28?)
- *Uncertain:* chapter number smudged, may read 10
- *Uncertain:* last digit may be 13
- *Uncertain:* first digit of 113 damaged

### Page 195 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* first digit damaged
- *Uncertain:* last digit blotted, may be 6
- *Uncertain:* 130 and Jonah verse number blotted
- *Uncertain:* second '3' may be 5; '8.' printed on next line
- *Uncertain:* last digits blotted
- *Illegible near:* `- <sup>d</sup> Eccl. 9, 7. Rom. 1[illegible] 13.`

### Page 196 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* last digit could be 6 or 8

### Page 197 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Note:* no reference letter printed before this note in the margin (text mark is l)
- *Uncertain:* first digit after ch. is 1 or 4, blotted
- *Illegible near:* `- <sup>u</sup> ch. [illegible], 9. <!-- uncertain: first dig`

### Page 198 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Note:* no reference letter printed in margin before this note (text mark is i)
- *Uncertain:* second digit blotted (3 or 5?)
- *Illegible near:* `- <sup>m</sup> Lev. 2[illegible], 16. <!-- uncertain: second d`

### Page 199 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* maybe 2, 16
- *Uncertain:* maybe 8, 29
- *Uncertain:* last digits blotted
- *Uncertain:* last digit clipped
- *Uncertain:* digits after 44 blotted
- *Uncertain:* digits blotted
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* blotted
- *Illegible near:* `- <sup>g</sup> Josh. [illegible]`

### Page 200 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* maybe 2 Kings
- *Uncertain:* number partly cut off
- *Uncertain:* last digit blotted, reads 23 (not 20)

### Page 201 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* first reference digits unclear
- *Uncertain:* 
- *Uncertain:* remainder clipped at page edge
- *Uncertain:* 
- *Uncertain:* 

### Page 202 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* maybe 8, 5
- *Uncertain:* maybe 31
- *Uncertain:* margin letter printed looks like p (text mark is b)
- *Uncertain:* 

### Page 203 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* last number unclear
- *Uncertain:* 
- *Uncertain:* maybe 13, 6
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 
- *Illegible near:* `- <sup>s</sup> Josh. 9, 14. ch. 13, 1[illegible]. verse 24.`

### Page 204 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* stop printed with space, maybe colon
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* maybe 18, 10
- *Uncertain:* maybe 26

### Page 205 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* 

### Page 206 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* maybe 3, 9, 10
- *Uncertain:* maybe 16, 11
- *Uncertain:* 

### Page 207 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* maybe 16, 14

### Page 208 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* printed mark looks like ?, maybe ;
- *Uncertain:* printed 31 (maybe 21)
- *Uncertain:* Jer. 3, 3 vs 9, 3
- *Uncertain:* 
- *Uncertain:* 

### Page 209 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* first word printed "toth-" with line-end mark, perhaps "to the day"

### Page 211 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Note:* note partly cut off; Rom. chapter number printed too small/blurred, could be 13
- *Uncertain:* 
- *Uncertain:* maybe 26
- *Uncertain:* partly cut off
- *Uncertain:* partly cut off
- *Illegible near:* `- <sup>u</sup> ch. 22, 7. verse 14. 2 Chr. 6, [illegible] Ps. 54, 3, 4.`
- *Illegible near:* `- <sup>†</sup> Heb. [illegible] Micah 3, 1. Rom. 12, 1. <!--`
- *Illegible near:* `- <sup>a</sup> ch. 22, [illegible]`

### Page 212 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* last number blurred, could be 125, 3

### Page 213 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* label letter obscured by stain; maybe 15, 18
- *Uncertain:* maybe 8, 12
- *Uncertain:* Ps. 53, 10
- *Uncertain:* Ps. reference partly illegible

### Page 214 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* reference as scanned
- *Uncertain:* reference as scanned

### Page 215 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* last figure poorly printed
- *Uncertain:* figures unclear

### Page 216 — The FIRST Book of SAMUEL, otherwise called The FIRST Book of the KINGS. (Opus 5.5)

- *Uncertain:* chapter figure unclear
- *Uncertain:* second figure unclear

### Page 217 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* figure unclear
- *Uncertain:* chapter figure blurred, could be 10
- *Illegible near:* `- <sup>z</sup> 1 Sam. 9, [illegible]`
- *Illegible near:* `- <sup>a</sup> Judg. 1, 1. 1 Sam. 23, [illegible] Ezra [illegible] Ezek. [illeg`
- *Illegible near:* `p>a</sup> Judg. 1, 1. 1 Sam. 23, [illegible] Ezra [illegible] Ezek. [illegible]`
- *Illegible near:* `1. 1 Sam. 23, [illegible] Ezra [illegible] Ezek. [illegible]`

### Page 218 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Note:* sic
- *Uncertain:* last figure unclear
- *Uncertain:* last figure unclear

### Page 219 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* figures unclear
- *Uncertain:* chapter figure unclear
- *Uncertain:* verse figure blurred, may read 2
- *Illegible near:* `- <sup>h</sup> 1 Kings [illegible], 5.`
- *Illegible near:* `- <sup>g</sup> Ps. 12, [illegible]`
- *Illegible near:* `- <sup>h</sup> ch. 2, 23. [illegible]`

### Page 220 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* figures unclear

### Page 221 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* first reference unclear
- *Uncertain:* figures unclear
- *Illegible near:* `- <sup>r</sup> 1 Kings [illegible], 20. Acts 13, 36.`
- *Illegible near:* `- <sup>c</sup> Jer. 23, [illegible] Mat. 23, 20. <!-- uncertain -`
- *Illegible near:* `- <sup>l</sup> Isa. 44, [illegible]`

### Page 223 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Note:* no punctuation visible after "fields"
- *Uncertain:* first words blurred in print, may read "with the return"
- *Uncertain:* figure unclear
- *Uncertain:* figures unclear
- *Uncertain:* margin damaged
- *Illegible near:* `h make up the number of 7000,* chap. 8, 4. 1 Chr. [illegible] 18.`
- *Illegible near:* `- <sup>r</sup> Ps. 18, [illegible] & 33, 16.`
- *Illegible near:* `against the face of the strongest battle.* chap. [illegible] Ps. 51, [illegible] Jer. 16,`
- *Illegible near:* `the strongest battle.* chap. [illegible] Ps. 51, [illegible] Jer. 16, 28. <!-- uncertain:`

### Page 224 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* chapter figure unclear
- *Uncertain:* maybe 7, 9
- *Illegible near:* `up> 2 Chron 23, 4. Isa. 26, 16. & 38, 7. Jer. 18, [illegible] & 50, 4. Zech. 12, 10, 11.`
- *Illegible near:* `- <sup>c</sup> [illegible]`

### Page 225 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Note:* no marker letter printed
- *Uncertain:* figures unclear
- *Uncertain:* marker letter unclear, maybe m
- *Uncertain:* chapter figure unclear
- *Uncertain:* figure unclear

### Page 226 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* verse figure may read 33
- *Uncertain:* figures unclear
- *Uncertain:* last figure may read 23
- *Illegible near:* `- <sup>r</sup> Num. 34, [illegible]`

### Page 227 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* maybe 15, 20
- *Uncertain:* figures unclear
- *Uncertain:* 
- *Uncertain:* maybe 3, 18

### Page 228 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* chapter figure of Acts unclear
- *Uncertain:* maybe 29, 4
- *Uncertain:* figure unclear
- *Illegible near:* `- <sup>†</sup> Heb. *I bow myself down,* ch. [illegible] 22.`

### Page 229 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* last figure unclear
- *Uncertain:* figures unclear
- *Uncertain:* first reference unclear
- *Uncertain:* chapter figure unclear

### Page 230 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* label letter faint
- *Uncertain:* reference as scanned

### Page 231 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* second line faint
- *Uncertain:* "21" partly blotted
- *Uncertain:* print blotted, may read 1, 47
- *Uncertain:* blotted

### Page 232 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* first number faint

### Page 233 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint
- *Illegible near:* `- <sup>t</sup> Ps. [illegible]`

### Page 234 — The SECOND Book of SAMUEL, otherwise called The SECOND Book of the KINGS. (Opus 5.5)

- *Note:* left edge cut off; probably "i Rom."
- *Note:* left edge cut off
- *Uncertain:* faint
- *Illegible near:* `- [illegible]om. 3, 3. <!-- left edge cut o`
- *Illegible near:* `- [illegible]uke 19, <!-- left edge cut off`

### Page 235 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* may read 28
- *Uncertain:* second numeral unclear

### Page 236 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint
- *Illegible near:* `- <sup>r</sup> ch. 12, [illegible] & 22, 8. 2 Kings 25, 8. 2 Chr`

### Page 237 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* left edge partly cut off
- *Note:* last digit unclear
- *Uncertain:* faint
- *Uncertain:* may read 3, 7
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* last digit blotted
- *Uncertain:* faint
- *Illegible near:* `- <sup>b</sup> Ps. 45, 9. Mat. 21, 2[illegible]`
- *Illegible near:* `- <sup>p</sup> 1 Samuel 2, 33. Mat. [illegible] & 27, 5. John 12, 38. & 16, 2`

### Page 238 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* may read 6, 8
- *Illegible near:* `- <sup>q</sup> Num. 23, [illegible]`

### Page 239 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* last word partly cut off at page edge
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint

### Page 240 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* blotted
- *Uncertain:* faint
- *Uncertain:* may read 13
- *Uncertain:* faint
- *Uncertain:* faint
- *Illegible near:* `- <sup>q</sup> Ezek. 41, [illegible]`

### Page 241 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* superscript before "two" faint
- *Uncertain:* may read 3, 8
- *Uncertain:* faint
- *Uncertain:* blotted

### Page 242 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* print unclear
- *Uncertain:* may read 10, 1, 15
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* may read 35
- *Uncertain:* faint
- *Illegible near:* `- <sup>q</sup> Ex. 40, 35. [illegible] 1, 14.`

### Page 243 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* letter faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* blotted
- *Uncertain:* blotted

### Page 244 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* tiny stray superscript mark (maybe p) printed after 'came'
- *Uncertain:* faint
- *Uncertain:* may read 2, 20
- *Uncertain:* faint

### Page 245 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* may read 63
- *Uncertain:* blotted
- *Uncertain:* last digit blotted
- *Uncertain:* faint
- *Uncertain:* faint
- *Illegible near:* `- <sup>d</sup> [illegible]`
- *Illegible near:* `- <sup>f</sup> [illegible]`

### Page 246 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* 7, 13
- *Uncertain:* last number 12 or 13

### Page 247 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* margin damaged
- *Illegible near:* `p>†</sup> Heb. *strengthened himself,* 1 Sam. 30, [illegible]`
- *Illegible near:* `- <sup>z</sup> ch. [illegible] verse [illegible] 2 Chr [ille`
- *Illegible near:* `- <sup>z</sup> ch. [illegible] verse [illegible] 2 Chr [illegible] <!-- uncert`
- *Illegible near:* `p>z</sup> ch. [illegible] verse [illegible] 2 Chr [illegible] <!-- uncertain: margin damage`
- *Illegible near:* `- <sup>f</sup> Ex. 1, 10 Isaiah 30, [illegible]`

### Page 248 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* print shows a raised dot (·) rather than a period
- *Uncertain:* reading

### Page 250 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* letter not visible in scan
- *Note:* as printed

### Page 252 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* superscript faint; appears to be s

### Page 253 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* faint

### Page 254 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Illegible near:* `- <sup>u</sup> 1 Sam. [illegible] 8. Ps. 75, 5.`

### Page 255 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Note:* letter printed faintly; could be e

### Page 256 — The FIRST Book of the KINGS, commonly called The THIRD Book of the KINGS. (Opus 5.5)

- *Uncertain:* margin blurred
- *Uncertain:* faint

### Page 257 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Uncertain:* "6, 17" faint

### Page 258 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Illegible near:* `- <sup>t</sup> Mark 16, 19. Heb. 9, 6 & 11 [illegible]`
- *Illegible near:* `- <sup>h</sup> ch. 8, [illegible]`

### Page 259 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Uncertain:* letter looks like "a"; text marker is z
- *Illegible near:* `- <sup>b</sup> 1 Tim. 6, [illegible]`

### Page 261 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Illegible near:* `- <sup>q</sup> verse 8. Ps. 50, 15. [illegible]`

### Page 263 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Uncertain:* "death" poorly printed in scan
- *Uncertain:* reference as printed, possibly incomplete

### Page 264 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Uncertain:* numbers faint
- *Uncertain:* maybe 16, 18

### Page 265 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* left edge of the left margin is cut off in the scan for the first few notes
- *Note:* partly cut off
- *Note:* partly cut off
- *Note:* partly cut off
- *Note:* partly cut off
- *Note:* partly cut off
- *Illegible near:* `- <sup>a</sup> 1 Kings [illegible]1.`

### Page 266 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Uncertain:* worn type, probably Jehoahaz

### Page 267 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* no period printed
- *Note:* verse number not legible
- *Uncertain:* as printed, chapter/verse incomplete
- *Uncertain:* last digit damaged
- *Uncertain:* character after "Kings 1" damaged

### Page 268 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* rest of reference not legible
- *Note:* partly cut off
- *Uncertain:* maybe 6, 2
- *Uncertain:* maybe 26, 1, 3

### Page 269 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Uncertain:* first reference faint
- *Uncertain:* last digit faint

### Page 270 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* partly cut off
- *Note:* partly obscured at bottom of margin
- *Illegible near:* `- [illegible] 10, 2. <!-- partly obscured a`

### Page 271 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* no closing punctuation visible in scan
- *Uncertain:* numbers faint
- *Uncertain:* right-margin print may read 728, last digit unclear
- *Uncertain:* numbers faint
- *Uncertain:* 8 or 9
- *Uncertain:* numbers faint

### Page 272 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* right edge cut off
- *Note:* right edge cut off
- *Note:* right edge cut off
- *Note:* right edge cut off
- *Note:* right edge cut off
- *Uncertain:* numbers faint
- *Uncertain:* faint
- *Uncertain:* numbers faint
- *Uncertain:* right edge cut off
- *Uncertain:* first digit may be 6 in print
- *Illegible near:* `- <sup>l</sup> ch. 17, 3, [illegible] 2 Chr. [illegible] <!-- right`
- *Illegible near:* `- <sup>l</sup> ch. 17, 3, [illegible] 2 Chr. [illegible]`
- *Illegible near:* `- <sup>q</sup> Rev. 1[illegible], 16. <!-- right edge cut off`
- *Illegible near:* `- <sup>r</sup> ch. 18, [illegible]`
- *Illegible near:* `- <sup>d</sup> Num. [illegible]4, 9. <!-- right edge cut off`

### Page 273 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Opus 5.5)

- *Note:* faint, partly illegible
- *Illegible near:* `- <sup>a</sup> [illegible] 3. [illegible] 13, 35. verse`
- *Illegible near:* `- <sup>a</sup> [illegible] 3. [illegible] 13, 35. verse 6. <!-- faint,`

### Page 274 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* reference as scanned
- *Uncertain:* maybe 3, 4, 5

### Page 275 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* "places" partly smudged in scan
- *Uncertain:* label letter faint
- *Uncertain:* reference as scanned
- *Uncertain:* reference as scanned
- *Uncertain:* reference as scanned

### Page 276 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* Ps. 63, 9
- *Uncertain:* reference as scanned

### Page 277 — The SECOND Book of the KINGS, commonly called The FOURTH Book of the KINGS. (Sonnet 5.5)

- *Uncertain:* Jer. reference as scanned
- *Uncertain:* last references partly blurred in scan

### Page 278 — The FIRST Book of the CHRONICLES. (Sonnet 5.5)

- *Uncertain:* small marginal print

### Page 279 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* date digits faint
- *Uncertain:* verse number faint
- *Uncertain:* verse number faint
- *Uncertain:* maybe 35, 1, 5

### Page 280 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* maybe Amon
- *Uncertain:* numbers faint
- *Uncertain:* maybe 19, 1

### Page 281 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Note:* cut off at page edge; probably Heb. in the house
- *Uncertain:* psalm number faint
- *Uncertain:* psalm number faint
- *Uncertain:* last reference faint
- *Illegible near:* `- <sup>†</sup> H[illegible] *the h[illegible]* <!-- cut o`
- *Illegible near:* `- <sup>†</sup> H[illegible] *the h[illegible]* <!-- cut off at page edge; p`
- *Illegible near:* `t page edge; probably Heb. in the house --> 1 King[illegible] 2 Chr. [illegible] 10. & 26,`
- *Illegible near:* `ly Heb. in the house --> 1 King[illegible] 2 Chr. [illegible] 10. & 26, [illegible] Zech. 4`
- *Illegible near:* `-> 1 King[illegible] 2 Chr. [illegible] 10. & 26, [illegible] Zech. 4, 9.`

### Page 282 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Note:* smudged
- *Uncertain:* maybe 134, 1, 2
- *Uncertain:* maybe 35, 15
- *Uncertain:* blurred
- *Illegible near:* `sup>x</sup> ch. 15, 19. & 16, 5, 7, 37. Ps. 50. & [illegible] title.`
- *Illegible near:* `- <sup>z</sup> verse 44. [illegible] 12, 47. <!-- uncertain: blurr`

### Page 283 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* maybe 21, 34

### Page 284 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* maybe 15, 63
- *Uncertain:* maybe 6, 37

### Page 286 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* verse number faint
- *Uncertain:* faint
- *Uncertain:* maybe 23, 8
- *Uncertain:* numbers faint
- *Uncertain:* book name partly cut off

### Page 287 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* numbers faint

### Page 288 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* maybe 68, 25

### Page 289 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint

### Page 290 — The FIRST Book of the CHRONICLES. (Sonnet 5.5)

- *Uncertain:* small marginal print

### Page 291 — The FIRST Book of the CHRONICLES. (Sonnet 5.5)

- *Note:* right running head appears cut off at "overcome"
- *Uncertain:* small marginal print
- *Uncertain:* small marginal print
- *Uncertain:* small marginal print

### Page 292 — The FIRST Book of the CHRONICLES. (Sonnet 5.5)

- *Uncertain:* superscript mark after "have" is smudged
- *Uncertain:* small marginal print
- *Uncertain:* "2 Kings" partly cut

### Page 293 — The FIRST Book of the CHRONICLES. (Sonnet 5.5)

- *Note:* marginal note beside "days" appears cut off: only a dagger visible
- *Uncertain:* small marginal print
- *Uncertain:* small marginal print

### Page 295 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* last number partly cut off
- *Uncertain:* last digit may read 3 (16, 33)
- *Uncertain:* "32" smudged
- *Uncertain:* number smudged

### Page 296 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* may read 1, 8
- *Uncertain:* number smudged
- *Uncertain:* last number partly cut off
- *Uncertain:* number partly cut off

### Page 297 — The FIRST Book of the CHRONICLES. (Opus 5.5)

- *Note:* the left edge of the left-column margin is trimmed in the scan; the start of several notes is lost
- *Uncertain:* margin trimmed
- *Uncertain:* margin trimmed
- *Uncertain:* margin trimmed
- *Uncertain:* maybe 6, 18
- *Uncertain:* smudged
- *Uncertain:* last digit smudged, may read 8
- *Illegible near:* `- [illegible] Deut. 4, [illegible] 9, 24. [`
- *Illegible near:* `- [illegible] Deut. 4, [illegible] 9, 24. [illegible]sea 4, 1. [`
- *Illegible near:* `- [illegible] Deut. 4, [illegible] 9, 24. [illegible]sea 4, 1. [illegible]n 17, 3.`
- *Illegible near:* `Deut. 4, [illegible] 9, 24. [illegible]sea 4, 1. [illegible]n 17, 3. <!-- uncertain: margi`
- *Illegible near:* `- [illegible] Kings [illegible] 3. <!-- unc`
- *Illegible near:* `- [illegible] Kings [illegible] 3. <!-- uncertain: margin tri`
- *Illegible near:* `- [illegible] Sam. 16, [illegible] 7, 9. &`
- *Illegible near:* `- [illegible] Sam. 16, [illegible] 7, 9. & [illegible] 9, 2. Jer`
- *Illegible near:* `- [illegible] Sam. 16, [illegible] 7, 9. & [illegible] 9, 2. Jer. 17, 10. Heb. 4, 13`
- *Illegible near:* `- <sup>b</sup> [illegible] Chr. 9, [illegible] & 12, 13`
- *Illegible near:* `- <sup>b</sup> [illegible] Chr. 9, [illegible] & 12, 13 <!-- uncertain: smud`

### Page 298 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* print may read Deut. 28, 53. and 1 Kings 5, 3; too faint to be sure
- *Illegible near:* `- <sup>o</sup> 1 Sam. 9, [illegible]`

### Page 299 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* maybe 22, 8
- *Uncertain:* "8, 22" smudged
- *Uncertain:* "1 Kings" smudged, may read 2

### Page 300 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* "16" smudged
- *Illegible near:* `- <sup>n</sup> [illegible] Kings 7, 12.`

### Page 301 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* "29" smudged
- *Uncertain:* last number smudged

### Page 302 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* maybe 3, 5
- *Uncertain:* last numbers smudged

### Page 303 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* "36" may be 30
- *Uncertain:* last number smudged
- *Illegible near:* `- <sup>h</sup> 1 Chr. [illegible], 29. Isa. 9, 6. Luke 1, 32.`
- *Illegible near:* `- <sup>†</sup> Heb. *hence an*[illegible]`

### Page 304 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* first number may read 16, 28 in print
- *Uncertain:* smudged
- *Uncertain:* maybe 12, 10
- *Uncertain:* heavily smudged

### Page 305 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* "21" may be 2
- *Uncertain:* smudged, may read 18, 24, 28
- *Uncertain:* smudged
- *Uncertain:* "on" smudged
- *Uncertain:* "22" may be 12
- *Illegible near:* `- <sup>m</sup> Deut. 28, [illegible]`
- *Illegible near:* `- <sup>s</sup> 1 Kings [illegible], 29.`
- *Illegible near:* `- <sup>z</sup> 1 Kings [illegible], 10. <!-- uncertain: smudged`
- *Illegible near:* `- <sup>o</sup> 1 Sam. [illegible] 3, 5.`

### Page 307 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* this note is smudged; several numbers doubtful

### Page 308 — The SECOND Book of the CHRONICLES. (Sonnet 5.5)

- *Uncertain:* small marginal print
- *Uncertain:* small marginal print

### Page 311 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* last digit faint
- *Uncertain:* maybe 19, 16
- *Uncertain:* 
- *Uncertain:* maybe 7, 12
- *Uncertain:* 
- *Uncertain:* scan reads "21, 9"
- *Uncertain:* reading of this note unclear
- *Uncertain:* last digit faint
- *Uncertain:* 
- *Uncertain:* maybe 10, 26
- *Uncertain:* maybe 13, 6
- *Illegible near:* `- <sup>†</sup> Heb. *thresholds,* 2 Kings 12, [illegible]`

### Page 312 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* may be 2 Kings
- *Uncertain:* maybe 2, 8
- *Uncertain:* may be 2 Kings
- *Uncertain:* faint
- *Uncertain:* edge cut off; maybe 9, 5
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* spelling
- *Uncertain:* several numbers faint

### Page 313 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* maybe 1, 3
- *Uncertain:* faint
- *Uncertain:* partly cut off
- *Uncertain:* faint; maybe 25, 2
- *Uncertain:* faint
- *Uncertain:* 

### Page 314 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* last number may read 33 or 38 (print blurred, no comma after 15)
- *Uncertain:* faint

### Page 315 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint

### Page 316 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* cut off
- *Uncertain:* faint
- *Uncertain:* 

### Page 317 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* several numbers faint
- *Uncertain:* "29" faint

### Page 318 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Illegible near:* `- <sup>h</sup> verses 2[illegible] 24.`

### Page 319 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* maybe 20, 13
- *Uncertain:* cut off
- *Uncertain:* cut off
- *Uncertain:* last digit cut off
- *Uncertain:* last digits faint
- *Uncertain:* faint
- *Illegible near:* `sup>d</sup> 1 Sam. 1, 24. Ps. 119, 9. Prov. 4, 3, [illegible] & 22, 6. Eccl. 12, 1, 2. 2 Ti`

### Page 320 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* faint

### Page 321 — The SECOND Book of the CHRONICLES. (Opus 5.5)

- *Note:* date, blotted
- *Uncertain:* faint
- *Uncertain:* last digit cut off
- *Uncertain:* cut off
- *Uncertain:* faint
- *Uncertain:* faint
- *Illegible near:* `- [illegible]`
- *Illegible near:* `- <sup>n</sup> Jer. 27, [illegible]`

### Page 322 — EZRA. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* digit after 20 blurred, could be 5

### Page 323 — EZRA. (Opus 5.5)

- *Uncertain:* faint
- *Uncertain:* maybe 7, 39
- *Uncertain:* maybe 7, 89
- *Uncertain:* several numbers faint

### Page 324 — EZRA. (Sonnet 5.5)

- *Uncertain:* "17" as printed; perhaps should be "1"
- *Uncertain:* small marginal print

### Page 325 — EZRA. (Sonnet 5.5)

- *Uncertain:* small marginal print
- *Uncertain:* scan reads "c. 7, 8."

### Page 327 — EZRA. (Opus 5.5)

- *Note:* right edge cut off
- *Uncertain:* edge of scan unclear
- *Uncertain:* edge of scan unclear
- *Uncertain:* edge of scan unclear
- *Uncertain:* last digit cut off at edge
- *Uncertain:* edge of scan unclear
- *Uncertain:* maybe 29, 39
- *Uncertain:* last digit smudged
- *Illegible near:* `- <sup>a</sup> Mat. 23, [illegible] Rom. 2, 1[illegible]. 21. <!-`
- *Illegible near:* `- <sup>a</sup> Mat. 23, [illegible] Rom. 2, 1[illegible]. 21. <!-- right edge cut off`

### Page 328 — EZRA. (Opus 5.5)

- *Uncertain:* print may show period after lands

### Page 329 — The BOOK of NEHEMIAH. (Opus 5.5)

- *Uncertain:* first number smudged
- *Uncertain:* last digit at edge
- *Illegible near:* `- <sup>q</sup> Ezra 10, [illegible]`

### Page 330 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* printed as Hat?ush, a blemish over the second t
- *Uncertain:* maybe 26, 9
- *Uncertain:* second reference small

### Page 331 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* small print

### Page 333 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* last reference smudged

### Page 334 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* the reference letter is not shown in the margin
- *Uncertain:* maybe 16, 11

### Page 335 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print

### Page 336 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* reference letter not visible in margin
- *Uncertain:* maybe 23, 17

### Page 337 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* maybe 15, 28
- *Uncertain:* small print
- *Uncertain:* maybe 18, 25

### Page 338 — The BOOK of NEHEMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 339 — The BOOK of ESTHER. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* label unclear, perhaps a dagger
- *Uncertain:* label letter not visible

### Page 340 — The BOOK of ESTHER. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* reference cut off or illegible after Deut. 3
- *Uncertain:* Gen. reference blurred, maybe 41, 42

### Page 341 — The BOOK of ESTHER. (Sonnet 5.5)

- *Uncertain:* label not visible
- *Uncertain:* small print
- *Illegible near:* `- <sup>g</sup> Zech. 1, [illegible]. John 16, 24.`

### Page 343 — The BOOK of ESTHER. (Sonnet 5.5)

- *Uncertain:* label letter not visible
- *Uncertain:* small print

### Page 344 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* reference blurred, possibly Rev. 1, 18
- *Uncertain:* small print
- *Illegible near:* `- <sup>l</sup> [illegible] <!-- uncertain: reference blu`

### Page 345 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* small print, maybe 48, 2
- *Uncertain:* verse number not legible
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* last number blurred

### Page 346 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* letter p not visible in scan
- *Uncertain:* 
- *Uncertain:* maybe 14, 4
- *Uncertain:* maybe 50

### Page 347 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* last number
- *Uncertain:* 
- *Uncertain:* smudged

### Page 348 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* 1 Cor. reference

### Page 349 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* last reference smudged
- *Uncertain:* 1 Cor. reference
- *Uncertain:* 
- *Uncertain:* maybe 1, 6
- *Uncertain:* 

### Page 350 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* running head may read Eliphaz
- *Uncertain:* 
- *Uncertain:* 

### Page 351 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* as printed
- *Uncertain:* 
- *Uncertain:* 

### Page 352 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* scan may read "anotner"
- *Uncertain:* maybe 118

### Page 353 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* 
- *Uncertain:* maybe 55, 25
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 

### Page 354 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* 
- *Uncertain:* Gen. reference chapter number

### Page 355 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 

### Page 356 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* Isa. reference
- *Uncertain:* maybe Mal.
- *Uncertain:* 

### Page 357 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* 
- *Uncertain:* 

### Page 359 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* chapter numerals span the column break; maybe XXXV....XXXVI....XXXVII
- *Uncertain:* maybe 18, 7
- *Uncertain:* 

### Page 360 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* letter not visible in scan

### Page 361 — The BOOK of JOB. (Sonnet 5.5)

- *Uncertain:* chapter numerals span the column break; maybe XXXIX....XL....XLI
- *Uncertain:* Gen. reference
- *Uncertain:* scan reads "eb."
- *Uncertain:* 
- *Uncertain:* smudged
- *Uncertain:* 

### Page 362 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* the mark before "uttered" is hard to read
- *Uncertain:* Exod. 5 2 punctuation unclear
- *Uncertain:* label not visible; maybe b, Gen. 18, 14
- *Uncertain:* number hard to read
- *Uncertain:* date hard to read
- *Uncertain:* maybe 17, 2, 4

### Page 363 — The BOOK of PSALMS. (Sonnet 5.5)

- *Illegible near:* `- <sup>q</sup> Zech. 2, [illegible].`

### Page 364 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* maybe Ps. 88, 30
- *Uncertain:* further small fragments "4, 6." and "18." at the left edge, labels unclear

### Page 365 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* first letter of "aescribed" as printed; probably d
- *Uncertain:* a digit is obscured

### Page 367 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* Gen. reference as printed; maybe 49, 8

### Page 370 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* verse number not clearly legible

### Page 371 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* the mark before "rejoice" resembles r, though the margin note is lettered p
- *Uncertain:* label not visible
- *Uncertain:* last reference partly obscured

### Page 372 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* number hard to read
- *Uncertain:* reference as printed

### Page 373 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* reference as printed
- *Uncertain:* number hard to read

### Page 374 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* reference as printed
- *Uncertain:* reference hard to read

### Page 375 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* Rev. reference as printed
- *Uncertain:* reference hard to read
- *Uncertain:* reference as printed
- *Uncertain:* numbers hard to read
- *Illegible near:* `- <sup>q</sup> Gen. 7, [illegible].`

### Page 376 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* label printed as a

### Page 377 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* last word(s) of the running head partly obscured
- *Uncertain:* reference as printed
- *Uncertain:* verse number hard to read
- *Uncertain:* reference hard to read
- *Uncertain:* reference as printed
- *Uncertain:* numbers hard to read
- *Illegible near:* `- <sup>i</sup> Eph. [illegible].`
- *Illegible near:* `- <sup>f</sup> Gen. 1, [illegible].`

### Page 378 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* first reference partly obscured by stain

### Page 379 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* maybe 20, 3
- *Uncertain:* first reference small/blurred
- *Uncertain:* reading of reference
- *Uncertain:* small print

### Page 381 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* letter obscured by stain
- *Uncertain:* maybe Judg. 5, 12
- *Uncertain:* small print

### Page 382 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* printed "mv", probably my
- *Uncertain:* maybe 5, 25
- *Uncertain:* Deut. reference small
- *Uncertain:* printed abbreviation and number small

### Page 383 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 384 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* printed numeral looks like 373

### Page 385 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* right running head cut off at crop edge ("disobedien")
- *Uncertain:* small print, a stray "23." nearby
- *Uncertain:* small print
- *Uncertain:* small print

### Page 386 — The BOOK of PSALMS. (Sonnet 5.5)

- *Note:* illegible: number cut off
- *Uncertain:* small print

### Page 388 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* label letter not visible, probably l

### Page 389 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* printed without space, "hastbrought"
- *Uncertain:* maybe 3, 21
- *Uncertain:* small print
- *Uncertain:* small print

### Page 390 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* last word of right running head blurred
- *Uncertain:* small print
- *Uncertain:* book abbreviation partly obscured

### Page 391 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 392 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print

### Page 393 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small superscript-like mark before "the"; no matching marginal note
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 394 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* maybe 19, 1, 3
- *Uncertain:* small print
- *Uncertain:* numbers small

### Page 395 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* second reference smudged

### Page 396 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print

### Page 397 — The BOOK of PSALMS. (Sonnet 5.5)

- *Note:* small dot mark before "the righteous"
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* first word small print
- *Uncertain:* small print
- *Uncertain:* marker glyph unclear
- *Uncertain:* small print

### Page 398 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print

### Page 399 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe 4, 25
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 400 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 401 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* first reference small print

### Page 402 — The BOOK of PSALMS. (Sonnet 5.5)

- *Note:* printed with a hyphen: "As-for"
- *Uncertain:* probably "Before CHRIST 1058."
- *Uncertain:* maybe 3, 6, 7
- *Uncertain:* small print

### Page 403 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* left running head smudged
- *Uncertain:* small print
- *Uncertain:* small print

### Page 404 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* right running head smudged
- *Uncertain:* image may read 63

### Page 406 — The BOOK of PSALMS. (Sonnet 5.5)

- *Note:* stray superscript mark after "him?"

### Page 407 — The BOOK of PSALMS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 409 — The PROVERBS. (Sonnet 5.5)

- *Note:* letter not printed before this note
- *Uncertain:* small print

### Page 410 — The PROVERBS. (Sonnet 5.5)

- *Note:* one blurred margin note between i and k, illegible
- *Uncertain:* maybe 5, 19
- *Uncertain:* maybe 5, 28
- *Uncertain:* no letter visible

### Page 411 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* maybe 7, 26
- *Uncertain:* small print, 1 Cor. reference doubtful
- *Uncertain:* small print, chap. reference doubtful

### Page 412 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* no letter visible, presumably m
- *Uncertain:* maybe 13, 41

### Page 413 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* smudged
- *Uncertain:* small print

### Page 414 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* small print, reading doubtful
- *Uncertain:* partly cut off

### Page 415 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* letter looks like r in crop, but margin sequence gives p
- *Uncertain:* small print
- *Uncertain:* maybe 21, 30

### Page 416 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* small print, maybe Eph. 3, 10

### Page 417 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* small print

### Page 418 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* letter not clearly matched in text
- *Uncertain:* prefix unclear, probably 1 Cor.
- *Uncertain:* small print

### Page 419 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* Ps. reference small print, maybe 75, 8
- *Uncertain:* second reference small print
- *Uncertain:* partly obscured, may read Ps. 7, 4

### Page 420 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* word partly obscured by a blemish
- *Uncertain:* small print
- *Uncertain:* verse number unclear

### Page 422 — The PROVERBS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* maybe 13, 22 or 18, 22
- *Uncertain:* small print

### Page 423 — ECCLESIASTES, or the PREACHER. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print

### Page 424 — ECCLESIASTES, or the PREACHER. (Sonnet 5.5)

- *Uncertain:* maybe 20, 21

### Page 425 — ECCLESIASTES, or the PREACHER. (Sonnet 5.5)

- *Uncertain:* 1 John 3, 2 appears without its own letter

### Page 426 — ECCLESIASTES, or the PREACHER. (Sonnet 5.5)

- *Uncertain:* printed as 1
- *Uncertain:* printed as 1
- *Uncertain:* a tiny superscript mark may precede "knoweth"

### Page 427 — ECCLESIASTES, or the PREACHER. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print, followed by 1 Tim. 6, 18

### Page 428 — The SONG of SOLOMON. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 429 — The SONG of SOLOMON. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 430 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* printed "Amos 34"
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 431 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 432 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* summary line cut off at the column edge/fold, probably "sin"
- *Uncertain:* small print
- *Illegible near:* `The great confusion which cometh by si[illegible] <!-- uncertain: summary line`

### Page 433 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 434 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print

### Page 435 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* label looks like "v" in print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 436 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* label blurred
- *Uncertain:* label blurred
- *Uncertain:* label blurred

### Page 438 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* reference cut off in print

### Page 439 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Note:* scan damage: a strip near the top of the page is torn/obscured across both columns
- *Uncertain:* head partly torn; "confusion" printed with long s and last word cut off
- *Uncertain:* second line torn, reading from the overview
- *Uncertain:* line torn; "look to his Maker" partly obscured
- *Uncertain:* line torn; only partly legible
- *Uncertain:* printed "anb"
- *Uncertain:* word damaged
- *Uncertain:* printed "wasteu"
- *Uncertain:* letter missing in print
- *Uncertain:* printed "thev"
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* reference cut off in print

### Page 440 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print

### Page 441 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print

### Page 442 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* printed Eph. 14, 18

### Page 444 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Note:* letter before this note not legible
- *Uncertain:* 1 Tim. 1, 29 as printed
- *Uncertain:* letter printed p, text mark is n

### Page 445 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Note:* stray letter at top of left margin, no note text
- *Illegible near:* `- <sup>x</sup> ch. 11, 6. Rom. 8, [illegible].`
- *Illegible near:* `- <sup>a</sup> [illegible] 17, 2.`

### Page 446 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* digit smudged, maybe 5, 21

### Page 447 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* ch. 64, 8 smudged
- *Uncertain:* the digits after 2 Kings 18, are unclear

### Page 448 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* chapter number of Rev. reference unclear

### Page 452 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* chapter digit smudged
- *Uncertain:* reference text crowded

### Page 453 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* verse number after 2 Thes. 2, unclear

### Page 455 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* Hab. 5, 4 as printed

### Page 457 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* maybe Jam. 5, 20

### Page 458 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* letter looks like n/a
- *Uncertain:* small print
- *Uncertain:* notes q/r/s run together

### Page 459 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* maybe 698
- *Uncertain:* maybe 8, 44
- *Uncertain:* letter may read n

### Page 460 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* Num. 1, 23 / 11, 23
- *Uncertain:* small print

### Page 461 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* stained

### Page 462 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print

### Page 463 — The BOOK of the Prophet ISAIAH. (Sonnet 5.5)

- *Uncertain:* italic extent
- *Uncertain:* maybe 13, 4

### Page 464 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* maybe 28, 19
- *Uncertain:* letter not visible in scan
- *Uncertain:* maybe 3, 39 / 8, 39
- *Uncertain:* small print

### Page 465 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* digits smudged

### Page 466 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* numbers cut off
- *Uncertain:* letter not visible
- *Uncertain:* letter not visible
- *Uncertain:* cut off
- *Illegible near:* `- <sup>z</sup> 2 Chr. 36, [illegible]. Ps. 73, 36. <!-- uncertain:`
- *Illegible near:* `- <sup>h</sup> Lam. 4, [illegible].`

### Page 467 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* maybe 24, 10
- *Uncertain:* small print

### Page 468 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe 3, 17

### Page 469 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* italic extent
- *Uncertain:* small print
- *Uncertain:* maybe Ps. 11, 2
- *Uncertain:* maybe Ps. 79
- *Uncertain:* maybe 23, 2

### Page 471 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe Isai. 56, 10
- *Uncertain:* Jam. 1, 23

### Page 472 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print

### Page 473 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Illegible near:* `- <sup>h</sup> 1 Sam. 1[illegible]. Lam. 4, 17. <!-- uncertain:`

### Page 474 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* Deut. reference as printed small

### Page 475 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* scan reads "them an that"

### Page 479 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* numerals small

### Page 481 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* maybe 26, 61
- *Uncertain:* blurred

### Page 483 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* maybe 28, 48

### Page 484 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* maybe 18, 20

### Page 485 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print

### Page 488 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* numerals small

### Page 490 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* ch. 23, 13, 11
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 491 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* 22, 10 maybe 22, 16
- *Uncertain:* 
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 492 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred

### Page 493 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* 
- *Uncertain:* 

### Page 494 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* 2, 10, 33 maybe 2, 10, 13

### Page 496 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* 
- *Uncertain:* small print blurred

### Page 497 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 498 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 499 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* maybe 30, 10
- *Uncertain:* small print blurred

### Page 500 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 501 — The BOOK of the Prophet JEREMIAH. (Sonnet 5.5)

- *Uncertain:* reference letter looks like c in the scan; margin note is d
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 502 — The LAMENTATIONS of JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 503 — The LAMENTATIONS of JEREMIAH. (Sonnet 5.5)

- *Uncertain:* reference letter before "is righteous" looks like p in the scan
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Uncertain:* small print blurred
- *Illegible near:* `- <sup>x</sup> 2 Chr. 15, 3. Amos 7, [illegible]`

### Page 505 — The LAMENTATIONS of JEREMIAH. (Sonnet 5.5)

- *Uncertain:* small print blurred
- *Uncertain:* small print blurred

### Page 508 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* "9, 1, 3." line preceded by a smudged letter

### Page 509 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* scan may read 6, 31.

### Page 510 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* scan shows "Num. 25," then "1 Kings 11, 7."

### Page 512 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* first reference smudged
- *Uncertain:* middle reference may be 12, 16 or 42, 18

### Page 513 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* marker letter and last number
- *Uncertain:* scan shows "ch. 20, 1?," then "13."
- *Uncertain:* last number smudged
- *Uncertain:* numbers smudged

### Page 514 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* first reference
- *Uncertain:* reading
- *Uncertain:* maybe 5, 22
- *Uncertain:* scan "12, 19"

### Page 515 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* reading
- *Uncertain:* 27, 15

### Page 516 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* first reference

### Page 517 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* reference numbers
- *Illegible near:* `- <sup>u</sup> ch. 33, [illegible].`

### Page 518 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* reading

### Page 520 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* superscript printed as d, perhaps b

### Page 521 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* reading

### Page 522 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* reference letter before "I have" printed as p (the margin also lists q 2 Chr. 36, 15 with no matching letter seen in text)
- *Uncertain:* maybe Ps. or Pr. 17, 6

### Page 523 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* "Pr." as printed, probably Ps.
- *Uncertain:* layout of these two lines (k and l)
- *Uncertain:* small print, maybe Rev. 11, 13 / 18, 13

### Page 524 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* maybe Isa. 2, 13
- *Uncertain:* small print, partly illegible
- *Uncertain:* maybe 29, 20 or 30, 11
- *Uncertain:* margin note cut off/garbled at page edge
- *Illegible near:* `- <sup>l</sup> Pr. [illegible], 17 <!-- uncertain: margin no`

### Page 525 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* "2 Sam. 18, 17" small print
- *Uncertain:* maybe 18, 21
- *Uncertain:* small print partly obscured

### Page 526 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* first reference partly obscured by ornament
- *Illegible near:* `- <sup>p</sup> 1 Sam. 12, [illegible] Rev. 19, 18. <!-- uncertain:`

### Page 528 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* second digit hard to read, maybe 8
- *Uncertain:* "Ezra" as printed, digits small
- *Uncertain:* line order of the Rev. 16, 9 reference
- *Uncertain:* smudged

### Page 529 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print, smudged

### Page 531 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* maybe Isaiah 26, 19
- *Uncertain:* maybe 14, 1
- *Uncertain:* digits small, maybe 8, 1
- *Uncertain:* small print

### Page 533 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* "art" may be roman rather than italic
- *Uncertain:* "Gen. 33, 20" as it appears in scan
- *Uncertain:* small print
- *Uncertain:* "Ps. .02" first digit unclear

### Page 535 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* maybe 16, 9

### Page 536 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* reference smudged, probably Rev. 21, 3
- *Uncertain:* tail of reference
- *Illegible near:* `- <sup>g</sup> Rev. 21, [illegible] <!-- uncertain: reference smu`

### Page 537 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* Acts 3, 41 as printed
- *Uncertain:* small italic note, partly hard to read

### Page 539 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* Acts 15, 48 as printed
- *Uncertain:* Acts 10, 8 and Gal. 3, 28 hard to read

### Page 540 — The Book of the Prophet EZEKIEL. (Sonnet 5.5)

- *Uncertain:* Acts 25, 7, 9 and Rom. 4, 11 as read from small print
- *Uncertain:* Mat. 11, 8
- *Uncertain:* 1 Chron. 3, 3, 7
- *Uncertain:* Ps. 104, 4
- *Uncertain:* Num. 23, 23 and Mat. 16, 14

### Page 541 — The Book of DANIEL. (Sonnet 5.5)

- *Note:* horizontal rule across the page separates Ezekiel from Daniel
- *Uncertain:* superscript letters read as d, e, f, g; margin has a "c Esth. 6" note with no c marker seen (possibly the mark after "commanded")
- *Uncertain:* Titus 1, 15
- *Uncertain:* reference cut off in print/scan
- *Uncertain:* maybe 4, 8
- *Uncertain:* reference cut off

### Page 542 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* Acts 28, 24 as read

### Page 543 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* as printed
- *Uncertain:* as printed
- *Uncertain:* Job 27, 9 as printed

### Page 544 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* reference partly obscured

### Page 546 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* as read from small print
- *Uncertain:* as read

### Page 547 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* as read

### Page 548 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* superscript on "prince" read as z (could be a); margin letters y, z not legible
- *Uncertain:* marker letter l (may print as 1)
- *Uncertain:* margin letter not legible
- *Uncertain:* margin letter not legible
- *Uncertain:* margin letter not legible
- *Uncertain:* letter printed as l/1
- *Uncertain:* 11, 23 or 11, 25
- *Uncertain:* 1, 12 or 1, 6

### Page 549 — The Book of DANIEL. (Sonnet 5.5)

- *Uncertain:* as printed

### Page 551 — HOSEA. (Sonnet 5.5)

- *Uncertain:* smudged, last note at bottom right margin

### Page 552 — HOSEA. (Sonnet 5.5)

- *Uncertain:* figures small
- *Uncertain:* reference letter unclear, may be o
- *Uncertain:* reference letter unclear

### Page 553 — HOSEA. (Sonnet 5.5)

- *Uncertain:* figures small
- *Uncertain:* figures smudged
- *Uncertain:* figures smudged
- *Uncertain:* figures smudged
- *Illegible near:* `- <sup>f</sup> Rom. 1, [illegible]`
- *Illegible near:* `- <sup>i</sup> Isai. [illegible]`

### Page 554 — HOSEA. (Sonnet 5.5)

- *Uncertain:* maybe 78, 34
- *Uncertain:* figures smudged

### Page 555 — HOSEA. (Sonnet 5.5)

- *Uncertain:* "Lord GOD" as printed, first word appears in mixed case
- *Uncertain:* figures small
- *Uncertain:* figures small

### Page 556 — JOEL. (Sonnet 5.5)

- *Uncertain:* reference letter not visible in scan
- *Uncertain:* reference letter not visible; figures unclear
- *Uncertain:* reference letter not visible in scan
- *Uncertain:* reference letter unclear
- *Uncertain:* figures small
- *Uncertain:* remainder smudged

### Page 557 — JOEL. (Sonnet 5.5)

- *Note:* printed "p stures" with the a missing in the scan
- *Uncertain:* figures small
- *Uncertain:* figures small
- *Uncertain:* figures partly smudged

### Page 558 — AMOS. (Sonnet 5.5)

- *Uncertain:* "Lord" appears in mixed case, GOD in small caps

### Page 559 — AMOS. (Sonnet 5.5)

- *Uncertain:* reads Ezra, maybe Ezek.
- *Uncertain:* figures small
- *Uncertain:* figures smudged
- *Uncertain:* figures small
- *Illegible near:* `- <sup>d</sup> Deut. 2[illegible]. Ezek. 12, 5. <!-- uncertain:`

### Page 560 — AMOS. (Sonnet 5.5)

- *Uncertain:* figures small
- *Uncertain:* last figure unclear
- *Uncertain:* figures small
- *Uncertain:* figures small
- *Uncertain:* figures small

### Page 561 — AMOS. (Sonnet 5.5)

- *Uncertain:* figures small
- *Uncertain:* figures small
- *Uncertain:* figures small

### Page 562 — OBADIAH. (Sonnet 5.5)

- *Uncertain:* reference letter unclear
- *Uncertain:* figures small
- *Uncertain:* reference letter unclear
- *Uncertain:* figures small
- *Uncertain:* figures small
- *Uncertain:* figures small
- *Uncertain:* figures small

### Page 563 — JONAH. (Sonnet 5.5)

- *Uncertain:* second reference letter looks like e, same as the first
- *Uncertain:* maybe 12, 40
- *Uncertain:* figures small

### Page 564 — MICAH. (Sonnet 5.5)

- *Uncertain:* figures small
- *Uncertain:* figures small
- *Uncertain:* figures partly smudged

### Page 565 — MICAH. (Sonnet 5.5)

- *Uncertain:* maybe 1, 15
- *Uncertain:* figures after Psal. 107 partly hidden
- *Uncertain:* figures small
- *Uncertain:* reference letter looks like q
- *Uncertain:* figures small

### Page 566 — MICAH. (Sonnet 5.5)

- *Uncertain:* reference letter not visible in scan
- *Uncertain:* Psal. figures small
- *Uncertain:* figures smudged
- *Uncertain:* smudged
- *Illegible near:* `- <sup>m</sup> Psal. 37, 24. Rev. 18, 2[illegible] <!-- uncertain: figures smudg`
- *Illegible near:* `- <sup>n</sup> Ps. 59, [illegible] Lam. 1, [illegible] <!-- unce`
- *Illegible near:* `- <sup>n</sup> Ps. 59, [illegible] Lam. 1, [illegible]`

### Page 567 — NAHUM. (Sonnet 5.5)

- *Uncertain:* reading of this reference is unclear

### Page 568 — HABAKKUK. (Sonnet 5.5)

- *Uncertain:* numbers smudged
- *Uncertain:* reference smudged
- *Uncertain:* reference smudged

### Page 569 — HABAKKUK. (Sonnet 5.5)

- *Uncertain:* reference as printed, possibly 50, 9
- *Uncertain:* last number faint
- *Uncertain:* first reference faint
- *Uncertain:* reference faint
- *Uncertain:* reference faint
- *Uncertain:* reference faint

### Page 570 — ZEPHANIAH. (Sonnet 5.5)

- *Uncertain:* a small mark (possibly a reference symbol) appears before "the threshold"
- *Uncertain:* numbers small
- *Uncertain:* faint

### Page 571 — HAGGAI. (Sonnet 5.5)

- *Uncertain:* as printed; text on page is Zeph. 2-3 and Haggai 1
- *Uncertain:* maybe Lev. 26, 19

### Page 572 — ZECHARIAH. (Sonnet 5.5)

- *Uncertain:* last reference garbled
- *Illegible near:* `- <sup>e</sup> 2 Chr. 36, 15, 16. Jer. 44, [illegible] <!-- uncertain: last referenc`

### Page 573 — ZECHARIAH. (Sonnet 5.5)

- *Uncertain:* maybe Amos 9, 14
- *Uncertain:* first number faint

### Page 574 — ZECHARIAH. (Sonnet 5.5)

- *Uncertain:* reference small
- *Uncertain:* Psal. reference small

### Page 575 — ZECHARIAH. (Sonnet 5.5)

- *Uncertain:* numbers small
- *Uncertain:* faint
- *Uncertain:* numbers small

### Page 576 — ZECHARIAH. (Sonnet 5.5)

- *Uncertain:* Ps. reference small
- *Uncertain:* numbers small
- *Uncertain:* Gen. reference small

### Page 577 — ZECHARIAH. (Sonnet 5.5)

- *Uncertain:* numbers small
- *Uncertain:* numbers small

### Page 578 — MALACHI. (Sonnet 5.5)

- *Uncertain:* date as printed
- *Uncertain:* reference letter not visible; text has a mark i at "mountains"
- *Uncertain:* reference small
- *Uncertain:* date as printed

### Page 579 — MALACHI. (Sonnet 5.5)

- *Uncertain:* as printed
- *Uncertain:* numbers small

### Page 581 — A Table (Sonnet 5.5)

- *Note:* Layout: three-column table page; each entry is chapter number followed by the quoted text and the New Testament reference. Read column 1, then column 2, then column 3.
- *Uncertain:* references as they appear; maybe Mat. 15, 4. Mark 7, 10.
- *Uncertain:* Luke reference as printed
- *Uncertain:* reference small
- *Uncertain:* reference as printed

### Page 582 — A TABLE OF OFFICES AND CONDITIONS OF MEN. (Sonnet 5.5)

- *Note:* Layout: top section "A Chronological Index" in four columns; middle "A Table of Time." in a row of boxed columns; bottom "A Table of Offices and Conditions of Men" in two columns.
- *Uncertain:* 150 as it appears

### Page 583 — Family Record. (Sonnet 5.5)

- *Note:* Family Record page with ornamental border; two blank columns, each headed MARRIAGES. No other text.

### Page 584 — Family Record. (Sonnet 5.5)

- *Note:* Family Record page with ornamental border; two blank columns, each headed BIRTHS. No other text.

### Page 585 — Family Record. (Sonnet 5.5)

- *Note:* Family Record page with ornamental border; two blank columns, each headed BIRTHS. No other text.

### Page 586 — Family Record. (Sonnet 5.5)

- *Note:* Family Record page with ornamental border; two blank columns, each headed DEATHS. No other text.

### Page 587 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* summary text faint/blurred; verse numbers 32, 33, 58 partly unclear
- *Uncertain:* word(s)/reference mark smudged here, probably a superscript letter a
- *Uncertain:* word before "Lord" obscured/blotted in scan
- *Uncertain:* reference mark (probably ||) smudged
- *Uncertain:* marginal note b not visibly marked in text
- *Uncertain:* possible reference mark (||) before "exceedingly"
- *Uncertain:* last digits faint, may be 59x

### Page 588 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* the mark before "horses" looks like a T-shaped glyph, probably †
- *Uncertain:* a mark (probably †) before "Rathumus" smudged
- *Uncertain:* gap/mark before "Semellius" (probably †)
- *Uncertain:* "cir." faint or absent
- *Uncertain:* first word could be Bahumus or Rahumus
- *Uncertain:* faint

### Page 589 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* small print, partly unclear

### Page 590 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* "Reclius" could be Reelius
- *Uncertain:* reference mark (probably q) faint before Kiriathiarius
- *Uncertain:* reference mark (probably q) missing before Phaleas
- *Uncertain:* reference mark (probably b) faint
- *Uncertain:* partly obscured
- *Uncertain:* maybe Delaiah

### Page 591 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* reference mark (probably k) faint before Addus
- *Uncertain:* gap here, probably reference mark † (margin: Heb. Urim and Thummim)
- *Uncertain:* gap/mark before "men-servants", probably ||
- *Uncertain:* second letter(s) of first word damaged, probably "To"
- *Uncertain:* "temple" printed as "temp'" (final letters damaged)
- *Uncertain:* number 8 before "Darius" not clearly legible
- *Uncertain:* printed "Barzelai."
- *Illegible near:* `49 T[illegible] offer burnt-sacrifices upon i`

### Page 592 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* a reference mark (probably ||, margin: Or, place) may be near "do"
- *Uncertain:* mark (probably ||) faint before Meremoth

### Page 593 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* gap before "all", probably a reference mark (margin has † Heb. of those that know)
- *Uncertain:* reference marks for margin notes a, ||, || not clearly visible in text here
- *Uncertain:* margin print is very small; many readings below are best-effort

### Page 594 — I. ESDRAS, (Sonnet 5.5)

- *Uncertain:* gap before "food", probably reference mark † (margin: Heb. life)
- *Uncertain:* gap before "aloft", probably reference mark || (margin: Or, exalted)
- *Uncertain:* gap before "stay", probably reference mark || (margin: Or, stand)
- *Uncertain:* gap/mark before Joribus
- *Uncertain:* gap before "rams", probably reference mark † (margin: Heb. a ram)
- *Uncertain:* gap before "errors", probably reference mark || (margin: Or, purification)
- *Uncertain:* no visible mark before Sameius (margin has b)
- *Uncertain:* first mark may be c or e; margin sequence suggests e
- *Uncertain:* gap before Tolbanes, probably reference mark m
- *Uncertain:* marks before Eliadas/Elisimus/Othonias read as x, y, z in sequence; and the mark before Sardeus is faint
- *Uncertain:* printed "Amathcis"

### Page 596 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* faint mark before "Wheresoever" (probably b); printed "Wherefoever"-like long s
- *Uncertain:* gap before "shut", probably reference mark † (margin: Lat. conclude)
- *Uncertain:* last digit possibly cut off

### Page 597 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* faint mark before "then" (probably l)
- *Uncertain:* gap before "floods", probably reference mark || (margin: Or, waves)
- *Uncertain:* no visible text mark for margin note b (Isa. 55, 8, 9)
- *Uncertain:* faint

### Page 598 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* printed form faint

### Page 599 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* right edge cut off in crop; maybe 1, 3

### Page 600 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* maybe 3, 4 or 30, 4; small print
- *Uncertain:* small print
- *Uncertain:* small, blurred print
- *Uncertain:* small print

### Page 601 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* position of || mark not visible in the text; placed before "thou" at a gap
- *Uncertain:* position of reference mark b faint
- *Uncertain:* position of reference mark c faint
- *Uncertain:* "is" before "shewed" faint
- *Uncertain:* small print, maybe 6, 1 or 8, 1
- *Uncertain:* small print

### Page 602 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* maybe 40

### Page 603 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* position of reference mark i not clearly visible in the text
- *Uncertain:* printed "Amos 6, 1" with "6." on next line

### Page 604 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* reference letter b before "they" barely legible; margin shows b

### Page 605 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* reference mark u not visible in the text; gap before "seven"
- *Uncertain:* reference mark before "all" is tiny; margin shows b
- *Uncertain:* maybe 16, 19; small print
- *Uncertain:* chapter number smudged

### Page 606 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* reference letter and numbers small; next entry printed without a letter
- *Uncertain:* maybe 21, 5
- *Uncertain:* first chapter number blurred
- *Uncertain:* Isa. reference small

### Page 607 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* reference mark before "like" faint; margin shows h
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe 43 or 46

### Page 608 — II. ESDRAS, (Sonnet 5.5)

- *Uncertain:* reference mark f before "The Lord" seen in scan, but no matching marginal note
- *Uncertain:* reference mark u not visible in text; gap before "plagues"
- *Uncertain:* reference mark b not visible in text; gap before "and take"

### Page 609 — TOBIT. (Sonnet 5.5)

- *Note:* layout: left column holds II Esdras 16:68-73, a double rule and the TOBIT title (spanning the page width), then Tobit 1:1-21; right column holds II Esdras 16:74-78, the rule and title continuing, then Tobit 1:21 onward
- *Note:* double horizontal rule across the page
- *Uncertain:* maybe 10, 23; small print

### Page 610 — TOBIT. (Sonnet 5.5)

- *Uncertain:* verse number at start of summary printed small, could be 1
- *Uncertain:* maybe 6, 20
- *Uncertain:* maybe 4, 20 or 6, 20

### Page 611 — TOBIT. (Sonnet 5.5)

- *Uncertain:* reference letter before "that" appears as a small mark; margin entry "ch. 3, 8." printed without a letter
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* smudged

### Page 612 — TOBIT. (Sonnet 5.5)

- *Uncertain:* left running head cut off at the page edge after "Apocr"; presumably "Apocrypha."
- *Uncertain:* reference letter small

### Page 613 — JUDITH. (Sonnet 5.5)

- *Note:* layout: left column holds Tobit 12:12-13:14, a double rule, the JUDITH title (spanning the page width) and Judith 1:1-3; right column holds Tobit 13:14-14:15, the rule and title continuing, then Judith 1:3-6
- *Note:* double horizontal rule across the page
- *Uncertain:* position of reference mark i not clearly visible; a dot appears before "and shew"
- *Uncertain:* small print

### Page 614 — JUDITH. (Sonnet 5.5)

- *Uncertain:* small print, maybe 2, 14
- *Uncertain:* small print

### Page 616 — JUDITH. (Sonnet 5.5)

- *Uncertain:* superscript mark before "the fountain" is faint, shown as a dot; margin has "i verse 7."
- *Uncertain:* superscript mark before "covered" faint; margin has "q ch. 2, 7."
- *Uncertain:* superscript mark before "Ozias" faint; margin has "u ch. 6, 15."

### Page 617 — JUDITH. (Sonnet 5.5)

- *Uncertain:* superscript mark before "the barley-harvest" faint; margin has "b Ruth 1, 22."
- *Uncertain:* superscript mark before "that" faint; margin has "b Ps. 141, 2."
- *Uncertain:* superscript mark before "are" faint; margin has "i ch. 2, 15, 16, 17."
- *Uncertain:* reading of the italic margin word

### Page 619 — JUDITH. (Sonnet 5.5)

- *Uncertain:* position of superscript e not visible in the scan; margin has "e ch. 11, 17."; placed at the wide gap before "may"
- *Uncertain:* no superscript visible in the scan; margin has "b Ecclus. 31, 20, 25."
- *Uncertain:* "32." partly illegible

### Page 620 — JUDITH. (Sonnet 5.5)

- *Note:* a tiny stray mark resembling "7" at bottom of left column on the left-bottom crop, not transcribed as a footer
- *Uncertain:* superscript letter here reads m, duplicating the m at verse 15
- *Uncertain:* last number faint
- *Uncertain:* "44" printed faintly, looks like 11

### Page 621 — JUDITH. (Sonnet 5.5)

- *Uncertain:* superscript mark before "honourable" is faint, shown as a dot; margin has "o 1 Sam. 2, 30."
- *Uncertain:* superscript b not clearly visible; placed at the faint mark before "And"; margin has "b Esth. 2, 21. & 6, 2."
- *Uncertain:* reference digits faint
- *Uncertain:* reference digits faint
- *Uncertain:* reference digits faint
- *Uncertain:* reference digits faint

### Page 623 — The WISDOM of SOLOMON. (Sonnet 5.5)

- *Note:* a small mark follows "ungodly" in the scan; not clearly a reference letter
- *Uncertain:* superscript mark before "is hanged" is faint; margin has "i Esther 7, 9, 10."
- *Uncertain:* superscript mark before "Therefore" is faint; margin has "n See Daniel 3, 29"
- *Uncertain:* superscript mark for "i Ps. 10, 8." appears only as a dot before the verse number
- *Uncertain:* last digits faint
- *Uncertain:* maybe Ex. 16, 4

### Page 625 — The WISDOM of SOLOMON. (Sonnet 5.5)

- *Uncertain:* superscript mark before "ministers" is faint, shown as a dot; margin has "c Rom. 13, 4."
- *Uncertain:* superscript mark before "being" is faint, shown as a dot; margin has "b Job 10, 10."
- *Uncertain:* "of the sun" may be italic; margin has "i Gen. 8, 22." but no superscript i is visible in the text

### Page 626 — The WISDOM of SOLOMON. (Sonnet 5.5)

- *Note:* the margin letter i (Gen. 14, 8) has no visible matching mark in the text
- *Uncertain:* maybe 3, 9
- *Uncertain:* the "7" is faint

### Page 627 — The WISDOM of SOLOMON. (Sonnet 5.5)

- *Note:* the margin letter q (Prov. 3, 11, 12) has no visible matching mark in the text
- *Uncertain:* maybe Isa. 44, 13

### Page 628 — The WISDOM of SOLOMON. (Sonnet 5.5)

- *Note:* the margin letter d (Heb. 11, 7) has no visible matching mark in the text
- *Note:* the margin letter e (2 Tim. 2, 20) has no visible matching mark in the text
- *Uncertain:* some letters of "secret ceremonies" are damaged in the scan
- *Uncertain:* placement of superscript q; the scan shows a small stray mark inside "manslaughter"; margin has "q John 8, 44."
- *Uncertain:* maybe Rom. 9, 21

### Page 629 — The WISDOM of SOLOMON. (Sonnet 5.5)

- *Note:* the margin letter i (Ps. 107, 20) and the † Gr. stung note have no clearly visible matching marks in the text
- *Uncertain:* a gap before "continually" suggests a faint mark; margin has "|| Or, never drawn from."
- *Uncertain:* superscript mark before "great" is faint; the margin has no matching "a" note
- *Uncertain:* margin letter looks like e, but sequence and text give c

### Page 630 — The Wisdom of JESUS the Son of SIRACH, OR, ECCLESIASTICUS. (Sonnet 5.5)

- *Uncertain:* second digit of first verse number faint

### Page 631 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* marker before "prophets" is a faint dot, possibly †
- *Uncertain:* maybe 17, 3

### Page 632 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* faint gap here, possibly the reference letter q
- *Uncertain:* reference mark † position faint, a gap before "when"
- *Uncertain:* a stray small mark (c or e) after "thee."
- *Uncertain:* last numbers faint

### Page 633 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* reference mark before "Whereas" is faint

### Page 634 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* blurred, maybe Ps. 75, 6, 7

### Page 635 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* reference mark i before "An enemy" is faint

### Page 636 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* summary line damaged/blurred in scan
- *Uncertain:* marks <sup>a</sup> before BLESSED and || before multitude; both faint
- *Uncertain:* "by" damaged
- *Uncertain:* words damaged
- *Uncertain:* words damaged
- *Uncertain:* "[his]" damaged in scan
- *Uncertain:* placement of marks i and k; faint marks before "All" and before "for"
- *Uncertain:* maybe ch. 19, 16
- *Uncertain:* blurred
- *Uncertain:* maybe 8, 34
- *Illegible near:* `1 A good conscience maketh [illegible]....[illegible] doeth good to`
- *Illegible near:* `1 A good conscience maketh [illegible]....[illegible] doeth good to none....18 But`
- *Illegible near:* `e....18 But do thou good....20 Men are happy that [illegible] near to wisdom. <!-- uncertai`

### Page 637 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* margin has a reference i (Acts 3, 19) but no marker i is visible in the text
- *Uncertain:* first numbers faint

### Page 640 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* reference mark b before "slipped" is faint
- *Uncertain:* mark || before "prudence" is faint

### Page 641 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* reference mark † before "the slander" is a faint gap
- *Uncertain:* maybe 18, 23
- *Uncertain:* a digit may be missing or blurred, maybe 21, 28

### Page 642 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* margin has o (See James 2, 1, 2, 3.) but no marker o is visible in the text
- *Uncertain:* first reference smudged
- *Uncertain:* faint numbers

### Page 643 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* reference mark i before "considerate" is a faint dot
- *Uncertain:* marker looks like d, but margin order suggests e (Gen. 1, 14)

### Page 645 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* faint mark || before "like"
- *Uncertain:* reference letter (presumably h) not visible in scan
- *Uncertain:* faint numbers

### Page 646 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* scan reads "Phil. 4, 1" followed by "1 Tim. 6, 6"

### Page 647 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* a faint mark after "a" in "blowing a furnace" resembles a superscript
- *Uncertain:* trailing digits unclear

### Page 648 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* the † mark before "he beautified" is faint

### Page 649 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* printed "wno", probably "who"
- *Uncertain:* letter and numbers partly smudged

### Page 650 — The Prologue of the Wisdom of JESUS, the Son of SIRACH. (Sonnet 5.5)

- *Uncertain:* reference letter before "He directed" is faint, maybe b
- *Uncertain:* margin has a † note but no † mark seen in text
- *Uncertain:* numbers partly unclear
- *Uncertain:* reference letter and text smudged
- *Uncertain:* reference letter before this entry not legible
- *Uncertain:* final punctuation maybe !

### Page 651 — BARUCH. (Sonnet 5.5)

- *Uncertain:* margin has a || note but no mark seen in text; small gap before "and so"
- *Uncertain:* reference letter before "Behold" is faint
- *Uncertain:* letter before "wept" may be a or c
- *Uncertain:* maybe 43, 28

### Page 652 — BARUCH. (Sonnet 5.5)

- *Uncertain:* text mark looks like y; margin letter looks like v
- *Uncertain:* letter looks like v, text mark looks like y

### Page 653 — The EPISTLE of JEREMY. (Sonnet 5.5)

- *Uncertain:* continuation obscured

### Page 654 — The SONG of the Three Holy Children, (Sonnet 5.5)

- *Uncertain:* margin has "i Judges 18, 24." but no reference mark seen in this line
- *Uncertain:* † mark before "gnawed" is faint
- *Uncertain:* reference letter before "they cannot rise" looks like n but margin letter is m
- *Uncertain:* mark before "abuse" printed like ,,
- *Uncertain:* "are" may be roman

### Page 655 — The SONG of the Three Holy Children, (Sonnet 5.5)

- *Uncertain:* printed "ime", probably "time"

### Page 656 — The History of SUSANNA, (Sonnet 5.5)

- *Note:* No running head on this page; the title of the History of Susanna spans both columns
- *Uncertain:* maybe verse 24

### Page 657 — The Prayer of MANASSES, king of Judah, when he was holden captive in Babylon. (Sonnet 5.5)

- *Note:* fragment: word continues on next page
- *Uncertain:* word smudged in title, reads "Destruc..."
- *Uncertain:* printed like "sucn"

### Page 658 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* mark before "neither have any release" is faint
- *Uncertain:* a faint reference mark (b?) before "went"
- *Uncertain:* † mark before "we have" is faint
- *Uncertain:* reference mark before "Her sanctuary" is faint

### Page 659 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* reference mark before "they set up" is faint
- *Uncertain:* † mark before "dwell" is faint
- *Uncertain:* a faint mark follows "righteousness", no matching margin note seen
- *Uncertain:* letter looks like n; no matching mark seen in text
- *Uncertain:* numerals unclear

### Page 660 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* mark before "that he should" looks like i, but margin note is †
- *Uncertain:* reference letter smudged
- *Uncertain:* reference unclear

### Page 661 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* reference mark before "were building" is faint
- *Uncertain:* word smudged, appears "suv <> j.nn"
- *Uncertain:* numerals read oddly, maybe 156

### Page 662 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* printed "Bo or", a letter faint

### Page 663 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* first number glyph looks like 8 or S; maybe 1
- *Uncertain:* position of || marker in text; only a small mark visible before "he"
- *Uncertain:* corresponding marker in text not clearly seen

### Page 664 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* left margin date cropped at page edge; only "ST" visible
- *Illegible near:* `- [illegible]ST <!-- uncertain: left margin`

### Page 665 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* the marks before "gotten" and "to abide" are faint; reference symbols inferred from the margin notes
- *Uncertain:* text partly cropped/blurred

### Page 666 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* no reference mark seen in text for the margin note "Bacchides and his company"
- *Uncertain:* no reference mark clearly seen for the margin note "Which when Bacchides understood..."
- *Uncertain:* reads "Ambri." in one crop and "Amori." in the overlapping crop; reference mark placed at "Jambri" in verse 36 by inference
- *Uncertain:* reads "Tecou."

### Page 667 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* reference letter looks like y or z; notes list y at v. 58 and z at v. 60-61
- *Uncertain:* no reference mark clearly seen for margin note "a verse 1."
- *Uncertain:* positions of i and k marks inferred from faint marks in text
- *Uncertain:* reads "1s."
- *Uncertain:* last numbers small, maybe ch. 9, 14

### Page 668 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* two margin notes (as though he would pass through it / led his company) but only one || mark clearly seen in text
- *Uncertain:* reference letter (presumably i) not visible
- *Uncertain:* reference letter (presumably l) not visible

### Page 669 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* no reference mark seen in text for margin note "u verse 33."
- *Uncertain:* last number blurred, maybe 14, 38 or 14, 68

### Page 670 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* no reference mark seen in text for margin note "† Gr. and service."
- *Uncertain:* no reference mark clearly seen for margin note "i verse 67."
- *Uncertain:* last number looks like 10, maybe 19
- *Uncertain:* reference letter not clearly visible
- *Uncertain:* tiny italic, may read "then went away"

### Page 671 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* no reference mark seen in text for margin note "t ch. 7, 10."
- *Uncertain:* no reference mark seen in text for margin note "u Prov. 14, 15. ch. 7, 10."
- *Uncertain:* second summary number could be 36 or 86; first number 8
- *Uncertain:* digits read as 123, maybe 143

### Page 672 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* final period not visible at crop edge

### Page 673 — The First Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* word before "have wasted" is a smudged glyph looking like "y" or "y)"; maybe "ye"
- *Uncertain:* spelling small
- *Uncertain:* last digit blurred
- *Uncertain:* printed glyph could be read 67
- *Illegible near:* `29 The borders thereof [illegible] have wasted, and done great h`

### Page 674 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* no reference mark seen in text for margin note "|| Or, Which when he had set on fire..."
- *Uncertain:* a dot/mark appears between "priest" and "son-in-law"
- *Uncertain:* no clear reference mark seen for margin note "b Lev. 23. Num. 29."
- *Uncertain:* maybe 23, 34

### Page 678 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* the || mark before "a desperate mind" is faint/blurred in the scan; margin note reads "|| Or, madness or, pride."

### Page 680 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* reference mark before "maimed" is faint; margin note reads "§ Or, lamed."

### Page 681 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* the reference mark before "they" and the mark of the margin note "Or, Simon." are small and blurred
- *Uncertain:* reference numbers blurred in scan

### Page 684 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Uncertain:* text mark appears as || but margin note mark looks like §

### Page 686 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Note:* Blank page (verso, apparently following the end of the Apocrypha). Heavily foxed/stained paper with faint, reversed show-through of text from the opposite side (a title-page layout, with a large line of display capitals around the lower middle); nothing is legibly printed on this side. [illegible]
- *Illegible near:* `middle); nothing is legibly printed on this side. [illegible] -->`

### Page 687 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Note:* Title page of the New Testament; foxed paper, no stamps. Display lettering: "NEW TESTAMENT" in large shaded (3-D) capitals; a short ornamental rule beneath the top line and another horizontal rule above the imprint.

### Page 688 — The Second Book of the MACCABEES. (Sonnet 5.5)

- *Note:* Foxed paper; faint reversed show-through of the title page's display lettering in the upper half (not transcribed). The printed content is a two-part table with a vertical rule between the left and right halves.

### Page 689 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* a tiny mark (') appears before "Azor" in the scan, possibly a reference letter
- *Uncertain:* last number looks like 23 in the scan
- *Uncertain:* numbers small/blurred
- *Uncertain:* right edge of note cut/blurred
- *Uncertain:* faint

### Page 690 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* "Bu" (missing t?) and "five" (probably damaged "live") appear as printed in the scan
- *Uncertain:* small print, some numbers blurred
- *Uncertain:* small print, some numbers blurred
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* last number cut off/blurred
- *Illegible near:* `Dan. 2, 44. chap. 9, 35. Mark 1, 28. Luke 4, 31, [illegible]. <!-- uncertain: last number`

### Page 691 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* marginal reference print is very small; several numbers below are best readings
- *Uncertain:* a possible separate letter before "1 Cor. 14, 33"; digits small
- *Uncertain:* "Luke 16, 8" number blurred
- *Illegible near:* `- <sup>y</sup> Gen. 32, 3. Luke 12, 5[illegible].`
- *Illegible near:* `- <sup>g</sup> Ps. 48, 2. & 87, 2. Isa. 66, [illegible].`

### Page 692 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* split of notes e/f and g in left margin
- *Uncertain:* maybe 12, 24
- *Uncertain:* printed "aa"; some figures small/blurred

### Page 693 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* reference letter printed f again (margin ff)
- *Uncertain:* reference letter printed s again (margin ss)
- *Uncertain:* reference letter printed t again (margin tt)
- *Uncertain:* small print, numbers partly blurred

### Page 694 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* small print

### Page 695 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe 15, 20
- *Uncertain:* small print
- *Uncertain:* last reference cut off at crop edge

### Page 696 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* Luke 16, 16 may belong to i or k
- *Uncertain:* small print
- *Uncertain:* small print

### Page 697 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* reference letter printed f again
- *Uncertain:* Mark 2, 22 as printed
- *Uncertain:* punctuation of Luke 1, 33 / 16, 11, 20
- *Uncertain:* small print
- *Uncertain:* printed ff

### Page 699 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* maybe John 6, 15
- *Uncertain:* small print

### Page 700 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* reading of verse number
- *Uncertain:* small print
- *Uncertain:* small print

### Page 701 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* last reference small print

### Page 702 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* order/small print
- *Uncertain:* line-broken "throat-ed him"
- *Uncertain:* Prov. reference small print

### Page 703 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* first reference small print
- *Uncertain:* small print

### Page 704 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* John reference small print

### Page 705 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print

### Page 706 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* maybe 32, 11, 12
- *Uncertain:* small print

### Page 707 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* initial letter appears missing; probably "And"
- *Uncertain:* maybe James 5, 8
- *Uncertain:* small print

### Page 708 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* maybe 2, 26
- *Uncertain:* maybe 25, 34
- *Uncertain:* leading letter mark unclear
- *Uncertain:* letter looks like v, text mark is y

### Page 709 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* maybe 16, 32
- *Uncertain:* 12, 19 / 4, 19 digits small
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 

### Page 710 — The GOSPEL according to St. MATTHEW. (Sonnet 5.5)

- *Uncertain:* scan looks like 58
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* 

### Page 711 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Note:* Layout: two columns; Matthew 27 (left) and Matthew 28 (right) above a rule; below the rule a full-width heading for St. Mark, with Mark 1:1 in the left column and 1:2-3 in the right. Transcribed Matthew first, then Mark.
- *Uncertain:* final punctuation, possibly colon; bottom of line partly faded
- *Uncertain:* 
- *Uncertain:* 

### Page 712 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* reference letter before "spread" is tiny; w inferred from margin note whose letter is hard to read
- *Uncertain:* line breaks make "13, 14, 44" doubtful
- *Uncertain:* letter hard to read
- *Uncertain:* end of note faint

### Page 713 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* left head letters worn, reads "heaieth ... pausy"

### Page 714 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* reference letter reads s again; sequence would suggest t
- *Uncertain:* reference letter (f) not visible in margin

### Page 715 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* numbers hard to read
- *Uncertain:* letter/attribution of this note unclear
- *Uncertain:* numbers hard to read
- *Uncertain:* 

### Page 716 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* last reference faint

### Page 718 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* scan reads 6, 5; parallel would be 16, 5
- *Uncertain:* 
- *Uncertain:* Luke 9, 16 vs 18
- *Uncertain:* 

### Page 719 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Note:* signature mark "4 B" at bottom of left column; page number 609
- *Uncertain:* Isa. 13, 16 reference odd

### Page 720 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* digits at line breaks possibly cut off, perhaps 20, 13 and 19, 11
- *Uncertain:* Job 31, 21 / Prov. 11, 18 digits
- *Uncertain:* 

### Page 721 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* reference letter not clearly visible
- *Uncertain:* 8, 29
- *Uncertain:* reference letter not clearly visible
- *Uncertain:* maybe 22, 24

### Page 722 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* reference letter not clearly visible
- *Uncertain:* maybe cut off
- *Uncertain:* digits small

### Page 723 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* reference digits small
- *Uncertain:* scan reads 16, 21; maybe 26, 11
- *Uncertain:* 

### Page 724 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* 20, 22
- *Uncertain:* small and smudged; letter c and reference unclear
- *Uncertain:* maybe 18, 16, 18
- *Illegible near:* `- <sup>c</sup> 2 Sam. 30, [illegible] <!-- uncertain: small and smu`
- *Illegible near:* `- <sup>†</sup> Gr. *Rabbi, Rabbi,* [illegible]`

### Page 725 — The GOSPEL according to St. MARK. (Sonnet 5.5)

- *Uncertain:* "so" appears italic in scan
- *Uncertain:* maybe 19, 29
- *Uncertain:* Ps. 22 verse number small
- *Uncertain:* maybe 19, 14

### Page 726 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Note:* layout: Mark 16 ends at top of right column; the Luke title (with rule above) spans both columns across the middle. Mark text is given continuously here before the title.
- *Uncertain:* Judg. 13, 32 small print
- *Uncertain:* Judg. reference smudged
- *Uncertain:* Isa. 40, 5 maybe 40, 3

### Page 727 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* maybe & 51, 5
- *Uncertain:* Ezek. 29, 11
- *Uncertain:* scan may read 6, 33

### Page 728 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* last number maybe 2, 17
- *Uncertain:* ch. 19, 11 maybe 13, 11
- *Uncertain:* 1 Sam. 2, 1

### Page 729 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* note is smudged, partly illegible
- *Uncertain:* first Ezek. number smudged
- *Illegible near:* `Greek translation. Some think Arphaxad should be* [illegible] *Sala by his son Cainan,* 1 C`
- *Illegible near:* `be* [illegible] *Sala by his son Cainan,* 1 Chr. [illegible] <!-- uncertain: note is smudg`

### Page 730 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* maybe 4, 48
- *Uncertain:* small print

### Page 731 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* Ezek. number may read 47, 40

### Page 732 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* small print, maybe 34, 6

### Page 733 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* Mat. 10, 3 small print
- *Uncertain:* & 26, 31 smudged
- *Uncertain:* scan may be Mat. 14, 5. & 21, 26.

### Page 734 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* 2 Cor. number may read 8, 5, 14

### Page 736 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* note cut off at bottom of crop
- *Uncertain:* "9, 3, 61" reading

### Page 737 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* final letters of "scorpion" damaged in scan
- *Uncertain:* "it" in "it was dumb" printed faintly like 't
- *Uncertain:* 1 Cor. 19, 13 as it appears

### Page 738 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* "findeth" partly obscured by smudge
- *Uncertain:* maybe 1, 28

### Page 739 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* "this know" partly obscured by ink blot
- *Uncertain:* note cut off at crop boundary
- *Uncertain:* small print, maybe 25, 26
- *Uncertain:* Acts reference blurred

### Page 740 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* word blotted by ink stain, reads "whose"
- *Uncertain:* maybe 18, 24
- *Uncertain:* margin letter looks like i/f; text mark is f

### Page 741 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* partly blotted by ink stain
- *Uncertain:* partly blotted
- *Uncertain:* partly blotted
- *Uncertain:* "all that he" partly blotted by ink stain
- *Uncertain:* "is good" blotted; "is" may not be italic
- *Uncertain:* "36, 6" as printed

### Page 742 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* "had" partly blotted by ink stain
- *Uncertain:* "and kissed" partly blotted
- *Uncertain:* "calf" partly blotted by ink stain
- *Uncertain:* lower right corner blurred/faded; middle of this line illegible
- *Uncertain:* blurred
- *Uncertain:* blurred
- *Illegible near:* `ray thee therefore, father, that thou wouldest sen[illegible] to my father's house; <!-- un`
- *Illegible near:* `28 For I have five bre[illegible] that he may testify unto them`
- *Illegible near:* `] that he may testify unto them, lest they also co[illegible] this place of torment. <!-- u`
- *Illegible near:* `29 <sup>m</sup>Abraham saith [illegible] They have Moses and the proph`
- *Illegible near:* `ith [illegible] They have Moses and the prophets; [illegible] them. <!-- uncertain: blurred`

### Page 743 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* "Noe" partly blotted by ink stain
- *Uncertain:* partly blotted
- *Uncertain:* "all" partly blotted
- *Uncertain:* "shall" partly blotted
- *Uncertain:* "2?, 43" second digit unclear; "21, 3" may be 21, 8

### Page 744 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* margin letter not visible
- *Uncertain:* as printed; maybe 7, 50

### Page 745 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* line faded in scan; "wept" hard to read
- *Uncertain:* start of verse faded; superscript o placement inferred from margin
- *Uncertain:* "21, 15" as read; may be another number

### Page 746 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* maybe 38, 8
- *Uncertain:* last digit blotted; maybe 19, 43

### Page 747 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* "called" partly blurred
- *Uncertain:* "but" partly blurred
- *Uncertain:* "younger" partly blurred
- *Uncertain:* "26, 11" as read; possibly 26, 14

### Page 748 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* maybe 53, 3

### Page 749 — The GOSPEL according to St. LUKE. (Sonnet 5.5)

- *Uncertain:* Mat. digits unclear; John maybe 19, 17
- *Uncertain:* "Mark 15, 24" as read

### Page 750 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Note:* horizontal rule across the page: end of St. Luke, start of St. John
- *Uncertain:* "12, 16" and "2, 8" as read; last digits unclear

### Page 751 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* "And" partly smudged
- *Uncertain:* "3, 28" as read
- *Uncertain:* last references unclear
- *Uncertain:* margin entry cut off at bottom edge

### Page 752 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* last reference unclear

### Page 753 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* last digits as read
- *Uncertain:* reference text small and unclear

### Page 754 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* letter and numbers faint in scan
- *Uncertain:* "Luke 23, 43" first reference unclear
- *Uncertain:* "1, 46" as read
- *Uncertain:* printed page number looks like 641 though sequence implies 644

### Page 755 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* "verse 15" as read
- *Uncertain:* "12" as read

### Page 756 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* faint mark after the question mark, perhaps a superscript letter
- *Uncertain:* first reference "ch. 3, 2"
- *Uncertain:* cut off at crop edge
- *Illegible near:* `- <sup>u</sup> verse 1[illegible] <!-- uncertain: cut off at cr`

### Page 757 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* blurred
- *Uncertain:* first reference small and blurred
- *Uncertain:* small print
- *Illegible near:* `up> Isa. 9, 1, 2. Mat. 4, 15. chap. 1, 46. verse 4[illegible]`

### Page 758 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* first reference "ch. 3, 27"

### Page 759 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* chapter number cut off
- *Uncertain:* last digit obscured
- *Illegible near:* `- <sup>d</sup> Ezek. 3[illegible], 11. verse 11. 2 Tim. 2, 19.`
- *Illegible near:* `- <sup>k</sup> ch. 10, 2[illegible] <!-- uncertain: last digit ob`

### Page 760 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* reference order/digits small
- *Uncertain:* last digit cut off
- *Uncertain:* digit cut off
- *Illegible near:* `- <sup>f</sup> ch. 9, 3[illegible] <!-- uncertain: last digit cu`
- *Illegible near:* `- <sup>h</sup> ch. 5, 2[illegible] & 6, 39, 44. <!-- uncertain:`

### Page 762 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* second reference might read "3, 10"
- *Uncertain:* maybe 18, 21
- *Uncertain:* last number small

### Page 763 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* margin letter prints as e, but text marker at verse 12 is g
- *Uncertain:* last reference small, maybe 6, 19

### Page 764 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* Eph. reference small
- *Uncertain:* reference cut at line end
- *Illegible near:* `33. & 8, 14, 21. & 9, 39. & 11, 27. & 12, 46. & 1[illegible] 28. verses 5, 16. <!-- uncert`

### Page 765 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* blurred
- *Illegible near:* `- <sup>h</sup> ch. 11, [illegible]`

### Page 766 — The GOSPEL according to St. JOHN. (Sonnet 5.5)

- *Uncertain:* the margin note for this verse has no letter printed
- *Uncertain:* no letter printed
- *Uncertain:* "chap. 1, 50"

### Page 768 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* maybe verse 19
- *Uncertain:* first reference might read Gen. 2, 2

### Page 769 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* last letter of "inspired" smudged, prints like "inspirea"
- *Uncertain:* "Mat. 34, 36" as printed
- *Uncertain:* reference letter not printed/legible; sits beside verse 25 (y)
- *Uncertain:* Isa. 44, 8 small print

### Page 770 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* scan has gaps in "delivered" and "foreknowledge"
- *Uncertain:* letter and reference partly cut off at bottom of crop
- *Uncertain:* final two marginal lines at crop edge; may also include ch. 1, 11

### Page 771 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* last number small
- *Uncertain:* margin letter prints like a, text marker at verse 30 is z
- *Uncertain:* "verse 30" blurred, may read 33

### Page 772 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* printed as a raised dot rather than a colon

### Page 773 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* margin note is smudged and hard to read

### Page 774 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* margin letter looks like n; text superscript at verse 40 is a
- *Uncertain:* maybe 44, 9

### Page 775 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* last number hard to read

### Page 776 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* maybe 5, 8

### Page 777 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* maybe 8, 1
- *Uncertain:* margin letter looks like o; text superscript at verse 41 is c
- *Uncertain:* no letter printed; small and hard to read
- *Uncertain:* maybe 21

### Page 778 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* verse number printed looks like 9
- *Uncertain:* maybe 26, 5

### Page 779 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* reference hard to read
- *Uncertain:* maybe 28, 24
- *Uncertain:* number partly obscured
- *Uncertain:* reference hard to read
- *Uncertain:* reference hard to read
- *Uncertain:* maybe 13, 12

### Page 780 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* maybe 26, 65
- *Uncertain:* digit before Kings unclear
- *Uncertain:* some numbers hard to read
- *Uncertain:* numbers hard to read
- *Uncertain:* numbers hard to read
- *Uncertain:* numbers hard to read

### Page 781 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* margin letter for verse 1 looks like n; text superscript printed as a
- *Uncertain:* last number hard to read
- *Uncertain:* numbers hard to read
- *Uncertain:* maybe 6, 5
- *Uncertain:* maybe 9, 12
- *Uncertain:* maybe 6, 5
- *Uncertain:* reference smudged
- *Illegible near:* `- <sup>o</sup> Luke 10, 30. Rev. [illegible] <!-- uncertain: reference smu`

### Page 782 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* last number hard to read
- *Uncertain:* partly obscured

### Page 783 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* verse number not visible
- *Uncertain:* last number hard to read
- *Uncertain:* maybe 6, 18

### Page 785 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* year smudged, reads like cc.
- *Uncertain:* last reference partly cut off
- *Illegible near:* `- <sup>g</sup> ch. 20, 23. & 21, 33. & 24, 27. & 2[illegible], 14. & 26, 29. Eph. 6, 20. Ph`

### Page 786 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* numbers hard to read
- *Uncertain:* partly obscured

### Page 788 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* reading doubtful

### Page 789 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* small print, some numbers doubtful
- *Uncertain:* second reference doubtful
- *Uncertain:* 
- *Uncertain:* very small print, numbers doubtful
- *Uncertain:* reading doubtful
- *Uncertain:* small print
- *Uncertain:* very small print
- *Uncertain:* very small print, numbers doubtful

### Page 790 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 791 — The ACTS of the Apostles. (Sonnet 5.5)

- *Uncertain:* maybe 28, 1 as printed
- *Uncertain:* first reference appears as "ch. 24. &"
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* blurred, possibly Luke 2, 30 or other

### Page 792 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print, numbers doubtful
- *Uncertain:* small print, numbers doubtful
- *Uncertain:* small print
- *Uncertain:* small print; notes e through l run together in the left margin and could not be separated reliably
- *Uncertain:* transcribed in printed order without letter attribution; unreliable
- *Uncertain:* 
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 793 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* this note and the next two seem attached to verses 10-13 in printed order
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; letter attribution doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* blurred
- *Uncertain:* blurred
- *Uncertain:* small print
- *Uncertain:* small print

### Page 794 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print, numbers doubtful
- *Uncertain:* maybe 11, 16
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe John 1, 16
- *Uncertain:* small print

### Page 795 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* "HERE is," after the drop-cap T appears to be in italic type
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* reading doubtful
- *Uncertain:* maybe John 3, 34 or 1 John 3, 8
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, partly doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* letter attribution doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 796 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, numbers doubtful
- *Uncertain:* letter not visible
- *Uncertain:* letter attribution doubtful
- *Uncertain:* 
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, numbers doubtful

### Page 797 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* reference letter glyph at verse 25 looks like t; sequence suggests z
- *Uncertain:* continuation of an earlier note, top of left margin
- *Uncertain:* letter glyph unclear; small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 798 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* letter doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, letters between e and g unreliable
- *Uncertain:* small print, partly illegible
- *Uncertain:* top of right margin, begins mid-note
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; letter doubtful

### Page 799 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; reading of this run is doubtful
- *Uncertain:* small print
- *Uncertain:* very faint at top of right margin
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint, largely illegible
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint
- *Uncertain:* faint

### Page 800 — The Epistle of PAUL, the Apostle, to the ROMANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; reading of the run is doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* letters d and e run together
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 801 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print; this run sits in the left margin beside Romans 16, 23 and below
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* reading doubtful
- *Uncertain:* small print
- *Uncertain:* small print; notes to Romans 16, 25
- *Uncertain:* 
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* reading doubtful
- *Uncertain:* small print
- *Uncertain:* small print, partly illegible
- *Uncertain:* small print, partly illegible
- *Uncertain:* small print, partly illegible
- *Uncertain:* small print, partly illegible

### Page 802 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* "according" partly smudged in scan
- *Uncertain:* left margin blurred
- *Uncertain:* left margin blurred
- *Uncertain:* left margin blurred
- *Uncertain:* left margin blurred
- *Uncertain:* left margin blurred
- *Uncertain:* left margin blurred
- *Uncertain:* left margin blurred
- *Uncertain:* top of right margin
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Illegible near:* `- [illegible] (left margin notes for the re`

### Page 803 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, largely blurred
- *Uncertain:* small print, largely blurred
- *Uncertain:* small print, largely blurred
- *Uncertain:* small print, largely blurred
- *Uncertain:* small print, largely blurred
- *Uncertain:* small print, largely blurred; letter attribution doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 804 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* a bullet-like mark in the margin beside verse 14, no letter
- *Uncertain:* small mark before "Art" in the scan, perhaps a stray apostrophe or reference mark
- *Uncertain:* 2 Pet. reference
- *Uncertain:* line breaks in margin, 2 Tim. 2, 19 may belong to b or c
- *Uncertain:* some references hard to read

### Page 805 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* no letter visible in scan
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* Mat. reference
- *Uncertain:* Heb. 11, 26 and Jude 5 order
- *Uncertain:* small print
- *Uncertain:* bottom lines cramped; last reference unclear

### Page 806 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* margin small, grouping of lines under m/n
- *Uncertain:* small print, some numbers unclear
- *Uncertain:* small print

### Page 807 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, numbers unclear
- *Uncertain:* small print, numbers unclear
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 808 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* summary begins with "3" as printed, not "1"
- *Uncertain:* reference letter and numbers small
- *Uncertain:* reference letter and number small; maybe a / 3, 15
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 809 — The First Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* maybe 20, 14
- *Uncertain:* reference letter looks like a; content and sequence unclear
- *Uncertain:* letter looks like 1
- *Uncertain:* maybe Dan. 12, 3
- *Uncertain:* small print
- *Uncertain:* small print

### Page 810 — The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* Layout note: the two columns of I. Corinthians 16 are followed by a full-width rule and the title of II. Corinthians, which begins in the lower part of the left column and continues in the right column; transcribed here in logical order: 1 Cor. 16:3-13 (left), 14-24 and subscription (right), then the title and chapter I (left column 1-11, right column 11-24).
- *Uncertain:* small print; 1 Tim. 1, 3 may be a separate entry
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 811 — The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many numbers are uncertain and the grouping of lines under letters is partly inferred from position.
- *Uncertain:* a stray mark/blot printed beside the p of "preach"
- *Uncertain:* small print
- *Uncertain:* maybe 6, 1
- *Uncertain:* Rom. 3, 37 / 8, 37
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* number illegible
- *Uncertain:* grouping under c
- *Uncertain:* small print
- *Uncertain:* small print, partly illegible
- *Uncertain:* beginning of this note not legible
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 812 — The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in extremely small print; many references are uncertain and the grouping of lines under letters is partly inferred from position.
- *Uncertain:* reference letter looks like n
- *Uncertain:* small print
- *Uncertain:* first reference unclear
- *Uncertain:* grouping and numbers
- *Uncertain:* small print
- *Uncertain:* continues below the page crop

### Page 813 — The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in very small print; some references and the grouping of lines under letters are uncertain.
- *Uncertain:* continuation of a note begun on the previous page
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, reference letter unclear
- *Uncertain:* Luke 13, 13 / 18, 13
- *Uncertain:* small print

### Page 814 — The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in very small print; some references and the grouping of lines under letters are uncertain.
- *Uncertain:* small print; "& 8" before "1, 6, 19" not clearly legible
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 815 — The Second Epistle of PAUL, the Apostle, to the CORINTHIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in extremely small print; some references and the grouping of lines under letters are uncertain.
- *Uncertain:* small print
- *Uncertain:* next line begins with a letter that looks like s before "Rom. 16, 17"
- *Uncertain:* grouping of lines under r/s/t is unclear; the line beginning 1 Cor. 4, 18 appears to be lettered t in the scan
- *Uncertain:* small print
- *Uncertain:* small print

### Page 816 — The Epistle of PAUL, the Apostle, to the GALATIANS. (Sonnet 5.5)

- *Note:* Layout note: the two columns of II. Corinthians 12-13 end with a full-width rule and the title of Galatians (title begins in the left column and continues in the right column); transcribed in logical order: 2 Cor. 12:21-13:5 (left), 13:6-14 and subscription (right), title and Galatians chapters I-II (left column to v15, right column from v15).
- *Note:* Marginal notes are in extremely small print; some references and the grouping of lines under letters are uncertain.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; the break between the notes for d and e is not clear in the scan
- *Uncertain:* small print
- *Uncertain:* 1 Cor. 6, 20 may be 16, 20
- *Uncertain:* small print

### Page 817 — The Epistle of PAUL, the Apostle, to the GALATIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in extremely small print; some references and the grouping of lines under letters are uncertain.
- *Uncertain:* small print
- *Uncertain:* last reference unclear
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 818 — The Epistle of PAUL, the Apostle, to the GALATIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in extremely small print; some references and the grouping of lines under letters are uncertain.
- *Uncertain:* the second number after Gen. 12, looks like 12 or 3
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print and grouping
- *Uncertain:* small print

### Page 819 — The Epistle of PAUL, the Apostle, to the EPHESIANS. (Sonnet 5.5)

- *Note:* Layout note: the Epistle to the Galatians ends in the right column with a subscription; a full-width rule and the title of Ephesians follow (title begins in the left column and continues in the right column). Transcribed in logical order: Gal. 5:19-6:5 (left), 6:6-18 and subscription (right), then the title and Ephesians chapter I (left column 1-10, right column 10-20).
- *Note:* Marginal notes are in extremely small print; many references and the grouping of lines under letters are uncertain.
- *Uncertain:* printed as "TER 1." (probably VI)
- *Uncertain:* reference letter unclear
- *Uncertain:* small print
- *Uncertain:* reference letter not legible
- *Uncertain:* last reference
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 820 — The Epistle of PAUL, the Apostle, to the EPHESIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in extremely small print; many references and the grouping of lines under letters are uncertain.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; further references to Rom. 2, 4 / Acts 15, 11 / Titus 3, 5 may belong here
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* reference letter and grouping
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* continuation of note u
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 821 — The Epistle of PAUL, the Apostle, to the EPHESIANS. (Sonnet 5.5)

- *Note:* Marginal notes are in extremely small print; many references and the grouping of lines under letters are uncertain.
- *Uncertain:* grouping of lines under d/e
- *Uncertain:* grouping
- *Uncertain:* 2 Cor. 15, 24 as printed
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 822 — The Epistle of PAUL, the Apostle, to the PHILIPPIANS. (Sonnet 5.5)

- *Uncertain:* initial glyph looks like 7, probably z
- *Uncertain:* Mat. 17, 5
- *Uncertain:* Prov. 19, 8 / & 20, 17 as printed
- *Uncertain:* grouping of these lines
- *Uncertain:* Heb. 12, 3 or 13, 3
- *Uncertain:* letter
- *Uncertain:* faint, last number
- *Uncertain:* small print

### Page 823 — The Epistle of PAUL, the Apostle, to the PHILIPPIANS. (Sonnet 5.5)

- *Uncertain:* Mark 10, 12
- *Uncertain:* Heb. 3, 4
- *Uncertain:* first letter/number and Acts 2, 36
- *Uncertain:* first reference smudged
- *Uncertain:* second reference
- *Illegible near:* `- <sup>t</sup> Rom. 1[illegible], 21. 1 Thes. 3, 2. <!-- uncer`

### Page 824 — The Epistle of PAUL, the Apostle, to the PHILIPPIANS. (Sonnet 5.5)

- *Uncertain:* letter looks like c or e
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* numbers

### Page 825 — The Epistle of PAUL, the Apostle, to the COLOSSIANS. (Sonnet 5.5)

- *Uncertain:* last group of numbers, small print
- *Uncertain:* Gen. reference
- *Uncertain:* last numbers

### Page 826 — The Epistle of PAUL, the Apostle, to the COLOSSIANS. (Sonnet 5.5)

- *Uncertain:* & 3, 24
- *Uncertain:* Rev. 22, 15
- *Uncertain:* Eph. reference

### Page 827 — The First Epistle of PAUL, the Apostle, to the THESSALONIANS. (Sonnet 5.5)

- *Uncertain:* letter before Ro. 15, 19; Philem. 22 placement
- *Uncertain:* Acts 14, 8, 19
- *Uncertain:* 1 Peter 3, 21

### Page 828 — The First Epistle of PAUL, the Apostle, to the THESSALONIANS. (Sonnet 5.5)

- *Uncertain:* 1 Cor. 14, second number not clear
- *Uncertain:* Eccl. 8, 22 and Eph. 6, 10

### Page 829 — The Second Epistle of PAUL, the Apostle, to the THESSALONIANS. (Sonnet 5.5)

- *Uncertain:* & 28, 4
- *Uncertain:* last line partly cut off at crop edge; a possible further 1 Tim. 5, 13 line between i and k was not clearly seen
- *Illegible near:* `- <sup>m</sup> Eph. 4, 28. 1 Thess. [illegible] <!-- uncertain: last line par`

### Page 831 — The First Epistle of PAUL, the Apostle, to TIMOTHY. (Sonnet 5.5)

- *Note:* not legible
- *Uncertain:* left margin small print on this page is very compressed; letters and some numbers below are best readings
- *Uncertain:* reading of this note
- *Uncertain:* 2 Sam. 2, 24
- *Uncertain:* this whole group was not legible; reconstructed from partial reading
- *Uncertain:* 
- *Uncertain:* 
- *Uncertain:* very small print; numbers as best read
- *Uncertain:* & 14, 6
- *Uncertain:* small print
- *Illegible near:* `- <sup>g</sup> Isa. 58, 7. Luke 12, 4[illegible]. Gal. 6, 10. 2 Tim. 3, 5. Tit`

### Page 832 — The Second Epistle of PAUL, the Apostle, to TIMOTHY. (Sonnet 5.5)

- *Uncertain:* margin print on this page is very small; readings are best effort
- *Uncertain:* & 3, 17 may be 8, 17
- *Uncertain:* Prov. 27, 26
- *Uncertain:* Prov. 25, 4
- *Uncertain:* 2 Tim. 3, 6
- *Uncertain:* 1 Thes. 1, 9
- *Uncertain:* several numbers in this group
- *Illegible near:* `2, 22. 1 Tim. 1, 2, 18. chapter 2, 1. 1 Peter 1, [illegible]`

### Page 833 — The Second Epistle of PAUL, the Apostle, to TIMOTHY. (Sonnet 5.5)

- *Uncertain:* 1 Tim. 1, 1
- *Uncertain:* Rom. reference as printed "1, 9, & 1, & 14, 9"

### Page 834 — The Epistle of PAUL, to TITUS. (Sonnet 5.5)

- *Uncertain:* grouping of these lines

### Page 835 — The Epistle of PAUL to PHILEMON. (Sonnet 5.5)

- *Uncertain:* Acts 21, 15 and Col. 1, 7
- *Uncertain:* & 26, 13
- *Uncertain:* second number
- *Uncertain:* Rom. 2, 20 as printed
- *Uncertain:* Heb. 13, 2

### Page 836 — The Epistle of PAUL, the Apostle, to the HEBREWS. (Sonnet 5.5)

- *Uncertain:* margin print on this page is very small; some references are best readings
- *Uncertain:* Num. reference
- *Uncertain:* Rom. reference
- *Uncertain:* Luke 1, 31 and & 10, 3
- *Uncertain:* small print
- *Uncertain:* letter and numbers
- *Uncertain:* Acts 5, 34
- *Uncertain:* Mat. 12, 24
- *Uncertain:* 1 Sam. reference

### Page 837 — The Epistle of PAUL, the Apostle, to the HEBREWS. (Sonnet 5.5)

- *Uncertain:* small print
- *Uncertain:* Mat. 12, 19
- *Uncertain:* grouping
- *Uncertain:* Isa. reference

### Page 838 — The Epistle of PAUL, the Apostle, to the HEBREWS. (Sonnet 5.5)

- *Uncertain:* small print, some numbers hard to read
- *Uncertain:* small print, some numbers hard to read
- *Uncertain:* small print
- *Uncertain:* small print

### Page 839 — The Epistle of PAUL, the Apostle, to the HEBREWS. (Sonnet 5.5)

- *Uncertain:* "Which" looks italic, "stood" roman; italics may extend differently
- *Uncertain:* reference letter looks like n; it stands against chapter 9 v. 1 (sup a)
- *Uncertain:* letter in first crop looks like h; note runs across both left crops; small print
- *Uncertain:* small print, some numbers hard to read
- *Uncertain:* small print
- *Uncertain:* maybe 3, 13
- *Uncertain:* small print
- *Uncertain:* small print

### Page 840 — The Epistle of PAUL, the Apostle, to the HEBREWS. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* letter looks like h
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, letters and extent doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print and letters
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; letters doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Illegible near:* `- <sup>b</sup> Lev. 16, [illegible]. Philip. 7, [illegible]. 27.`
- *Illegible near:* `- <sup>b</sup> Lev. 16, [illegible]. Philip. 7, [illegible]. 27. & 9, 7. <!-- uncertain:`
- *Illegible near:* `- <sup>l</sup> [illegible] 1 Pet. 3, 14. ch. 6, 10. & 12`
- *Illegible near:* `- <sup>a</sup> 1 Thes. [illegible]. 2 Thes. 2, 1. chapter 6, [il`
- *Illegible near:* `up> 1 Thes. [illegible]. 2 Thes. 2, 1. chapter 6, [illegible]. Rom. 8, 24. 2 Cor. 4, 1. <!-`

### Page 841 — The Epistle of PAUL, the Apostle, to the HEBREWS. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* letter looks like v; position suggests y
- *Uncertain:* small print
- *Uncertain:* letter and extent doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; two notes' lines are interleaved
- *Uncertain:* small print; letters not legible against these lines
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, heavily garbled
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, partly guessed from garbled text
- *Uncertain:* letter i may belong to the later portion; small print
- *Uncertain:* small print
- *Uncertain:* small print; letter o/n doubtful
- *Uncertain:* small print
- *Illegible near:* `14, 26. Rom. 6, 4. & 12, 12. 1 Cor. 9, 24. & 10, [illegible]. Eph. 4, 22. Phil. 3, 13, 14.`
- *Illegible near:* `, 1. & 6, 12. & 4, 1, 11. & 6, 12. & 9, 25. & 10, [illegible]. <!-- uncertain: small print,`
- *Illegible near:* `Luke 24, 26, 46. Acts 3, 15. & 5, 31. Philip. 2, [illegible]. ch. 1, 3, 13. & 2, 10. & 5,`
- *Illegible near:* `- <sup>d</sup> 1 Cor. 10, 13. ch. 10, [illegible]. <!-- uncertain: small print`

### Page 842 — The general Epistle of JAMES. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* letter looks like r
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, letter not read

### Page 843 — The general Epistle of JAMES. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* printed "assemb'ly" with an apostrophe-like mark
- *Uncertain:* first line's letter looks like o
- *Uncertain:* letter not clear
- *Uncertain:* small print
- *Uncertain:* small print; lines interleaved
- *Uncertain:* small print
- *Uncertain:* "Ex." and some numbers small print
- *Illegible near:* `- <sup>p</sup> Gen. [illegible], 25. Mat. 7, 21. Luke 6, 46.`

### Page 844 — The general Epistle of JAMES. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* "fig-tree" and "olive-berries" partly obscured by a mark in the scan
- *Uncertain:* small print
- *Uncertain:* letter looks like n
- *Uncertain:* letter looks like n; position suggests this is the note for chap. 4, 1 (a)
- *Uncertain:* small print
- *Uncertain:* letter obscured
- *Uncertain:* small print

### Page 845 — The First Epistle General of PETER. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; letter doubtful
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 846 — The First Epistle General of PETER. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* "wives" partly obscured in the scan
- *Uncertain:* initial "t" of "they" not visible in the scan
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* letter obscured; position suggests this may belong to m
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Illegible near:* `- <sup>d</sup> 1 Cor. 4, 13. James 2, [illegible]. chap. 2, 12. & 3, 9, 16. <!-`

### Page 847 — The Second Epistle general of PETER. (Sonnet 5.5)

- *Note:* Layout: left column holds 1 Peter 4:5-19, then a rule and the title and chapter 1 (verses 1-6) of the Second Epistle of Peter; right column holds 1 Peter chapter 5, then a rule and 2 Peter 1:7-14.
- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, several numbers guessed
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print, mostly illegible

### Page 848 — The Second Epistle general of PETER. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 849 — The First Epistle general of JOHN. (Sonnet 5.5)

- *Note:* Layout: left column holds 2 Peter 3:10-14, then a rule with the title and 1 John chapter 1 and chapter 2:1-4; right column holds 2 Peter 3:14-18, then a rule and 1 John 2:4-18.
- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* final word smudged in the scan
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; the first line and the letter c are on different lines
- *Uncertain:* small print; letter not read
- *Uncertain:* small print
- *Uncertain:* small print; letter not read
- *Uncertain:* small print
- *Uncertain:* small print

### Page 850 — The First Epistle general of JOHN. (Sonnet 5.5)

- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* small print, two notes (a and b) run together in the margin
- *Uncertain:* small print
- *Uncertain:* small print; two notes' lines interleaved
- *Uncertain:* first reference as printed "1 John 13, 34" (probably John)
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; notes z and a run together
- *Uncertain:* small print
- *Uncertain:* small print

### Page 851 — The Second Epistle of JOHN. (Sonnet 5.5)

- *Note:* Layout: left column holds 1 John 4:9-21, chapter 5:1-4, then a rule with the title and 2 John 1-3; right column holds 1 John 5:5-21, then a rule and 2 John 4-7.
- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; probably John
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 852 — The General Epistle of JUDE. (Sonnet 5.5)

- *Note:* Layout: three tiers separated by rules. Left column: end of 2 John (vv. 7-10), the Third Epistle of John (1-7), the General Epistle of Jude (1-7). Right column: 2 John 10-13, 3 John 8-14, Jude 7-15.
- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* scan looks like "ana their punishment"
- *Uncertain:* "themselves over to" and "are set forth" partly smudged in the scan
- *Uncertain:* small print; letters b and c lines may be interleaved
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* first reference as printed "1 John 17, 13" (probably John)
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 853 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Note:* Layout: left column holds Jude 15-19, then a rule with the Revelation title and chapter 1:1-13; right column holds Jude 20-25, then a rule and Revelation 1:14-20 and chapter 2:1-8.
- *Note:* All marginal notes on this page are in very small print; many are only partly legible. Letters are given where they could be read or inferred from position.
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print; letter o may belong with this
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print
- *Uncertain:* small print

### Page 854 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* final punctuation after "nations" unclear, looks like a raised dot
- *Uncertain:* tail of this note is small/blurred

### Page 855 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* "& 14" before "& 22, 5" is small
- *Uncertain:* last numbers small

### Page 856 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* "& 3, 8 & 9, 13" is small and unclear
- *Uncertain:* reference letter l not visible in margin
- *Uncertain:* maybe Ezek. 9, 4
- *Uncertain:* year looks like 98 in right margin

### Page 857 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* italic middle of note is illegible
- *Illegible near:* `- <sup>||</sup> That is, *the Turks* [illegible] Christians, 1 Sam. 23, 26. ch`

### Page 858 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* verse number after 1 Kings 17 faint

### Page 859 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* year looks like 98 in left margin, 96 in right
- *Uncertain:* numbers small

### Page 860 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* tail of this note small and partly unclear

### Page 861 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* last word partly hidden by fold
- *Uncertain:* margin note for ch. 18 v. 1 (a) mostly not visible

### Page 862 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* last numbers small

### Page 863 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Uncertain:* maybe 3, 13

### Page 864 — The REVELATION of St. JOHN the Divine. (Sonnet 5.5)

- *Note:* FINIS. printed centred low on the page; remainder of page blank with stains
- *Uncertain:* final punctuation after "him" looks like a semicolon/dot
- *Uncertain:* "10." in this note may be a stray line

### Page 865 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Title page of the chronological index; two-column table layout (left column then right column), columns headed "Before Christ" | "Genesis" | text. Year and reference cells with several lines are separated by <br>.
- *Uncertain:* "29" faint
- *Uncertain:* "Sea" partly hidden by stain
- *Uncertain:* words after "to" obscured by stain; maybe "Lot"
- *Illegible near:* `e 100th year of Abraham's age. Not long after, to [illegible] are born Moab and Ammon, his`

### Page 866 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Two-column table layout (left column then right column), each headed "Before Christ" | book reference | text. Year and reference cells with several lines are separated by <br>.

### Page 867 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Two-column table layout (left column then right column), each headed "Before Christ" | book reference | text. Year and reference cells with several lines are separated by <br>.
- *Uncertain:* scan reads XXIII. (perhaps XIII.)
- *Uncertain:* year may be 1085
- *Uncertain:* year digits unclear

### Page 868 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Two-column table layout (left column then right column), each headed "Before Christ" | book reference | text. Year and reference cells with several lines are separated by <br>.
- *Uncertain:* reference letters before "25." blotted
- *Uncertain:* year partly obscured by fold

### Page 869 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Two-column table layout (left column then right column), each headed "Before Christ" | book reference | text. Year and reference cells with several lines are separated by <br>.
- *Uncertain:* number partly dark
- *Uncertain:* chapter number partly obscured
- *Uncertain:* figure looks like 468
- *Uncertain:* this italic label stands in the year column, apparently a margin label

### Page 870 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Back matter: chronological INDEX TO THE HOLY BIBLE, page 760, "The sixth Age". Printed in two columns, each with a margin of dates (Before Christ) and scripture references beside the text. Rendered here as tables: Before Christ | References | Text.
- *Uncertain:* "m[illegible]." is smudged in the scan (probably "man")
- *Uncertain:* second XLIV. may be XLV.
- *Uncertain:* "desir[illegible]" smudged in scan
- *Uncertain:* 300 or 500
- *Uncertain:* smudged words after "as many" and "many [illegible]s"
- *Illegible near:* `30 days no petition shall be made to any god or m[illegible]., but to himself only. Which`
- *Illegible near:* `nce and fear the God of Daniel. <!-- uncertain: "m[illegible]." is smudged in the scan (pro`
- *Illegible near:* `bestoweth on the Jews whatever favours they desir[illegible], and departeth. <!-- uncertai`
- *Illegible near:* `[illegible], and departeth.  |`
- *Illegible near:* `th 40,000 of the inhabitants, and selleth as many [illegible] [illegible] He endeavoureth a`
- *Illegible near:* `the inhabitants, and selleth as many [illegible] [illegible] He endeavoureth also to aboli`
- *Illegible near:* `o to abolish the worship of God, and forceth many [illegible]s to forsake their religion. T`
- *Illegible near:* `ncertain: smudged words after "as many" and "many [illegible]s" --> |`

### Page 871 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Back matter: chronological INDEX TO THE HOLY BIBLE, page 761 (the left column ends the "sixth Age", the right column begins the "seventh Age"). Printed in two columns, each with a margin of dates and scripture references beside the text; rendered here as tables Before Christ | References | Text. Alignment of margin references to individual paragraphs is approximate.
- *Uncertain:* "to o...ige him" smudged in scan (probably "to oblige")
- *Uncertain:* "Zabdiel" is blurred in the scan
- *Uncertain:* "famous" partly smudged
- *Uncertain:* "sur...ed" smudged (probably "surnamed")
- *Uncertain:* parts of this italic caption are smudged; "week" vs "weeks"
- *Uncertain:* last line partly smudged in scan
- *Illegible near:* `ul to obtain the friendship of Jonathan, and, to o[illegible]ige him, confers on him the hi`
- *Illegible near:* `y. The next year following he is by the senate sur[illegible]ed Augustus. <!-- uncertain: "`

### Page 872 — AN INDEX TO THE HOLY BIBLE; (Sonnet 5.5)

- *Note:* Back matter: chronological INDEX TO THE HOLY BIBLE, page 762, "The seventh Age". Printed in two columns, each with a margin of dates (After Christ) and scripture references beside the text; rendered here as tables After Christ | References | Text. Alignment of margin references to individual paragraphs is approximate.
- *Uncertain:* date partly smudged
- *Uncertain:* a few letters in "had not the apostles" are smudged in the scan
- *Uncertain:* date at top of column partly cut off
- *Uncertain:* first line of reference cut off at crop edge
- *Uncertain:* "like" partly smudged
- *Uncertain:* "Aq...a" (probably Aquila) and "...ere" (probably Here) smudged
- *Uncertain:* maybe 18
- *Uncertain:* date as printed; sequence suggests 66
- *Illegible near:* `| | XVIII. | Paul at Corinth meets with Aq[illegible]a and Priscilla, not long befo`
- *Illegible near:* `g before banished Rome by the decree of Claudius. [illegible]ere he continues a year and si`

### Page 873 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back matter: "Tables of Scripture Measures, Weights, and Coins" (page 763). Two columns beneath a full-width title; the left column holds the introduction and Tables I-IV, the right column continues with the Roman money table and the Appendix.
- *Uncertain:* 21.888/6 would be 3.648; scan shows 3.684
- *Uncertain:* fraction in this cell hard to read
- *Uncertain:* fraction hard to read
- *Uncertain:* fraction hard to read
- *Uncertain:* 438 read from the scan; OCR gave 433
- *Uncertain:* a further small mark follows the fraction in the scan
- *Uncertain:* a further small mark follows the fraction in the scan
- *Uncertain:* scan may read 81862.5
- *Uncertain:* fraction hard to read
- *Uncertain:* fraction hard to read
- *Uncertain:* the expression after "thus," (fractions/ratio) is unclear in the scan
- *Uncertain:* maybe xxvii. 18
- *Uncertain:* maybe 3 Roods
- *Illegible near:* `which must be reduced to our Foot measure, thus, [illegible]. The product of these numbers`

### Page 874 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back matter: end of the Appendix to the Tables of Scripture Measures (two columns), then a full-width "Analysis of the Old and New Testaments", a "Table of Kindred and Affinity", and the beginning of "Judea, Palestine, or the Holy Land" (two columns). Page 764.
- *Uncertain:* Greek word, hard to read
- *Uncertain:* the arrangement of the right-hand list beside the left-hand numbers is approximate; the Old Testament figures and the New Testament figures are printed in one column on the left and the notes in a second column on the right. "6,855" for Jehovah is partly smudged in the scan.
- *Uncertain:* degree and minute marks after 31, 33 and 40 are faint in the scan
- *Uncertain:* "lump," with a comma-like mark
- *Uncertain:* several words in this paragraph ("circumference", "the north", "supposed") are smudged in the scan
- *Uncertain:* perhaps Jaffa
- *Uncertain:* smudged

### Page 875 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back matter: end of "Judea, Palestine, or the Holy Land" (two columns), then the start of "An Alphabetical Table of the Proper Names in the Old and New Testaments" in five columns headed AD, AM, AZ, BE, CH. Page 765. Many letters in the name table are smudged or faint in the scan; some entries were read with the help of the recognizable surrounding names.
- *Uncertain:* a few words in the Mount Carmel paragraph are blotted in the scan
- *Uncertain:* last word smudged
- *Uncertain:* name smudged, probably Ahikam
- *Uncertain:* name smudged
- *Uncertain:* smudged
- *Uncertain:* name smudged, probably Ammah
- *Uncertain:* scan reads approximately "Ba alim"; position suggests Balaam
- *Illegible near:* `montory, called the point of Carmel. There are a n[illegible] of grottos, gardens, and conv`
- *Illegible near:* `unt; as also many cisterns for receiving the rain [illegible]. On this mountain was a fortr`
- *Illegible near:* `Ahi'[illegible]am, a brother who raises up <!`
- *Illegible near:* `Ahi'[illegible]ud, a brother born <!-- uncert`
- *Illegible near:* `Am'[illegible]ah, my people <!-- uncertain:`

### Page 876 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back matter: continuation of the Alphabetical Table of Proper Names, five columns headed EL, GA, HE, JE, LA (column heads are printed at the top of each column). Page 766. Several letters are smudged in the scan; the more doubtful entries are flagged.
- *Uncertain:* second Elha'nan; scan may be a different spelling
- *Uncertain:* first word smudged
- *Uncertain:* first word smudged

### Page 877 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back matter: continuation of the Alphabetical Table of Proper Names, five columns headed MI, OR, RA, SC, SH (column heads are printed at the top of each column). Page 767. Several letters are smudged in the scan; the more doubtful entries are flagged.

### Page 878 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back matter: end of the Alphabetical Table of Proper Names, five columns headed TA, TH, UL, ZE, ZU (column heads printed at the top of each column). Page 768. The lower part of the page below the text is blank (aged paper, no printing).
- *Uncertain:* name partly blotted
- *Illegible near:* `Zab'[illegible], portion, dowry <!-- uncertai`

### Page 879 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Blank page: aged, yellowed paper with no printing and no legible text.

### Page 880 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Blank page: aged, yellowed paper with no printing and no legible text (a thin dark strip of binding/edge along the left side).

### Page 881 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Blank page: plain tan paper (flyleaf or lining), no printing and no legible text.

### Page 882 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Blank page: plain greenish-tan paper (endpaper/lining) with a crease near the lower right; no printing and no legible text.

### Page 883 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Blank page: plain tan paper with a vertical fold line and a brown stain near the top; no printing and no legible text.

### Page 884 — TABLES OF SCRIPture MEASURES, WEIGHTS, AND COINS: (Sonnet 5.5)

- *Note:* Back cover of the volume: dark reddish-brown leather, scuffed and worn, with a lighter cloth-covered spine strip along the right edge. No title, stamp or legible text.


## 6. Audit of the Opus pages (silent-correction check)

- **Scope:** 309 pages (PDF 1–329 excluding 213, 214, 230, 246, 274–278, 290–294, 308–310, 324–326, which Sonnet wrote). Each page was compared with its scan in 20 batches by Sonnet 5.5 agents.
- **Result:** 197 pages had at least one edit (about 500 individual changes); the remaining pages needed none. Changes were mainly (a) marginal digits fixed where clearly legible at zoom, (b) punctuation restored (periods/commas that are not in the print, or are), (c) printer's errors restored (see §3), (d) uncertain comments added or removed.
- **Re-audits:** pages 177, 178, 180, 186, 188, 189, 191, 261, 262, 263, 266, 282 and 322 were audited a second time because the first pass could not view the images (the image viewer returned 'media removed'); the second pass used zoomed renders.
- **Thin spots:** pages 209–217 (read only from zoomed strips), 153–155 and 160, 261, 303, 305, 311, 317 had weaker checks than the rest. In many small margin notes digits 3/5/8/9 are indistinguishable even at 600 dpi; those keep their uncertain comments. Digit changes made in the zoomed-strip passes carry some risk of replacing one guess with another.
- **Not audited:** pages 330–884 and the 20 Sonnet gap-fill pages (their authors were told to transcribe exactly what the scan shows).

## 7. Compiled text (`phinney-bible.md`)

`phinney-bible.md` (project root) is generated from the 884 page files by a script and contains only the main text, in page order:

- **Removed:** the `### Marginal notes` sections, `Footer:` lines (signature marks and printed folios), the `**Header:**` running heads, all HTML comments (including the `uncertain` comments), the superscript reference marks (`a`, `b`, `†`, `‖`, `§` …, which only point to the margin notes), and the layout-only subheadings that named a column.
- **Kept:** book titles, chapter headings and summaries, verses with their italics and ¶ marks, tables and indexes, and `[illegible]` marks (28 in the main text). A `<!-- page NNN -->` comment (invisible when rendered) marks the start of each page's text so any passage can be traced back to its page file.
- **Joined across page breaks:** a verse or paragraph that runs over a page break is rejoined into one paragraph (about 370 joins; end-of-line hyphenations at a page break are closed up). The page comment sits at the join point.
- **Reordered:** pages 847, 849, 851 and 853 (and 852's joins) were fixed in the page files, because the transcription had written two-tier left/right columns in strict column order, which split verses and interleaved books. They now read in true reading order.
- **Kept as printed:** printer's errors survive in the compiled text, e.g. Ex. 30:8 is numbered "o" in print (p. 72), Gen. 4:2 has no verse number (p. 17), Num. 1:32 is numbered "23" (p. 103), and many final periods missing in print.
- **Not in the compiled text:** the covers, blank pages and bookplate (comment-only pages), and every marginal cross-reference and date.

`phinney-bible.txt` (project root) is the same text as `phinney-bible.md` with all markup removed: no `#` headings, no `*` italics or `**` bold, no page comments, no horizontal rules. Headings and chapter summaries are plain lines; tables are tab-separated rows (cells that held line breaks are joined with a space). Both files also had the inline printed parallel marks `||` (146 occurrences, mostly in the Apocrypha) removed, since like the superscript letters they only point to margin notes; the page files still contain them.

`phinney-bible-sparse.txt` (project root) is the plain-text biblical text only, generated from `phinney-bible.md` (pages 15–580, 587–685 and 689–864):

- **Included:** book titles, chapter and Psalm headings, verses (with ¶ marks), Psalm titles ("To the chief Musician…") and the Psalm 119 letter headings, epistle subscriptions ("¶ Written from Rome…"), and the Apocrypha (as a separate block starting at "APOCRYPHA.", including the Additions to Esther, the Song of the Three Children, Susanna, Bel and the Dragon, and the Prayer of Manasses).
- **Excluded:** the title page, tables of books and contents, preface, family-record pages, the Table of Passages and chronological/time/offices tables (pp. 581–582), the New Testament title page and dates table (687–688), the index, weights/measures tables, essays and name tables (865+), the chapter summaries ("1 The creation of heaven and earth….", 1,350 of them, including unnumbered ones and the Psalm 119 and Susanna argument notes), the translator's Prologue to Ecclesiasticus (p. 631), and the end markers ("END OF THE OLD TESTAMENT", "END OF THE APOCRYPHA", "FINIS").
- **As printed:** the first verse of each chapter is unnumbered (large initial in the original), and the one-chapter books (Obadiah, Philemon, 2 and 3 John, Jude) have no chapter heading. A sanity check against the standard King James verse counts gave 23,141 (OT, standard 23,145) and 7,953 + 4 one-chapter-book first verses (NT, standard 7,957).
