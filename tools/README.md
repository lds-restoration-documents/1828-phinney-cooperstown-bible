# tools

The scripts and instructions used to produce the files in this repository. The page files in
`../phinney-bible-pages/` are the source of truth; the three combined text files are generated from them.

## Pipeline

1. **Render the scan** (needs the scan PDF, which is not in this repo, and `pip install pypdfium2 pillow`):
   `python3 tools/render_pages.py holybiblecontain00cann.pdf --out work [--pages 1-16,302]`
   writes four readable crops, a low-resolution overview and the PDF's own noisy OCR text for each page.
2. **Transcribe**: AI agents (Claude) read the crops and wrote one `page-NNN.md` per page following
   [transcription-spec.md](transcription-spec.md). Pages 1–329 were then audited against the scan per
   [audit-spec.md](audit-spec.md). This step is done by agents, not by a script.
3. **Rebuild the combined files** from the page files (Python 3, standard library only; run from anywhere):
   ```
   python3 tools/compile_markdown.py     # -> phinney-bible.md
   python3 tools/make_plaintext.py       # -> phinney-bible.txt        (from phinney-bible.md)
   python3 tools/make_sparse.py          # -> phinney-bible-sparse.txt (from phinney-bible.md)
   ```
   Each script writes to the repo root by default; `--out` redirects the output. Run in that order.

Run against the committed page files, the three scripts reproduce `phinney-bible.md`, `phinney-bible.txt` and
`phinney-bible-sparse.txt` byte for byte. If you change a page file, re-run step 3 so the combined files stay in sync.

4. **Rebuild the typo catalog** (needs the Project Gutenberg KJV, which is not in this repo):
   ```
   curl -o pg10.txt https://www.gutenberg.org/cache/epub/10/pg10.txt
   python3 tools/make_typo_catalog.py --kjv pg10.txt     # -> printer-typos.md
   ```
   `kjv_compare.py` aligns each chapter with the reference word by word, sets aside spacing-only differences and any pair that recurs four or more times
   (the edition's own conventions), and checks each paragraph's printed verse number against the verse its text matches. `make_typo_catalog.py` holds the curated
   typo list, finds each form in the page files with its page and context, and writes the verse-number and variants sections. Marginal notes are not compared.

## Notes on the scripts

- `compile_markdown.py` strips the marginal notes, footers, running heads, comments and reference marks, rejoins verses split across
  pages, and removes the printed parallel mark `||`. At a page or column break it closes up a hyphenated word (`Abra-` / `ham`) but keeps the hyphen when the
  compound is printed hyphenated elsewhere and never closed up (`shittim-wood`); a reference mark with a letter on both sides becomes a space so the two words are not fused. See `../transcription-notes.md` §7 for the full list.
- `make_sparse.py` has edition-specific constants at the top: the page ranges that hold Bible text, two named intro notes that are
  dropped like chapter summaries, and the Ecclesiasticus prologue title. Changing the source scan or its page layout means
  revisiting these.
