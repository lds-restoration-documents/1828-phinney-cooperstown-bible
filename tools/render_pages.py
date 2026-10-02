#!/usr/bin/env python3
"""Render PDF pages into the inputs used for transcription.

For each page N this writes, under <out>/:
  img/pNNNN_0_overview.jpg     whole page, low resolution (layout only)
  img/pNNNN_1_lefttop.jpg      four overlapping crops at 2x, readable for
  img/pNNNN_2_leftbottom.jpg   small print (the halves overlap slightly in
  img/pNNNN_3_righttop.jpg     the middle)
  img/pNNNN_4_rightbottom.jpg
  ocr/pNNNN.txt                the PDF's embedded (very noisy) OCR text

Requires: pypdfium2 and Pillow.

Usage:
  python3 tools/render_pages.py scan.pdf --out work               # all pages
  python3 tools/render_pages.py scan.pdf --out work --pages 1-16,302
"""
import argparse
from pathlib import Path

import pypdfium2 as pdfium


def parse_pages(spec, total):
    if not spec:
        return list(range(1, total + 1))
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            pages.extend(range(int(a), int(b) + 1))
        else:
            pages.append(int(part))
    return pages


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", help="path to the scan PDF")
    ap.add_argument("--out", default="work", help="output directory (default: ./work)")
    ap.add_argument("--pages", help="pages to render, e.g. 1-16,302 (default: all)")
    args = ap.parse_args()

    out = Path(args.out)
    (out / "img").mkdir(parents=True, exist_ok=True)
    (out / "ocr").mkdir(parents=True, exist_ok=True)

    doc = pdfium.PdfDocument(args.pdf)
    for n in parse_pages(args.pages, len(doc)):
        page = doc[n - 1]
        (out / "ocr" / f"p{n:04d}.txt").write_text(page.get_textpage().get_text_range())
        im = page.render(scale=2).to_pil().convert("RGB")
        w, h = im.size
        mx, my = w // 2, h // 2
        crops = {
            "1_lefttop": (0, 0, mx + 25, my + 40),
            "2_leftbottom": (0, my - 40, mx + 25, h),
            "3_righttop": (mx - 25, 0, w, my + 40),
            "4_rightbottom": (mx - 25, my - 40, w, h),
        }
        for name, box in crops.items():
            im.crop(box).save(out / "img" / f"p{n:04d}_{name}.jpg", quality=85)
        im.resize((w // 3, h // 3)).save(out / "img" / f"p{n:04d}_0_overview.jpg", quality=70)


if __name__ == "__main__":
    main()
