#!/usr/bin/env python3
"""Build the sparse plain-text file (biblical text only) from phinney-bible.md.

Keeps book titles, chapter/Psalm headings, verses, Psalm titles and epistle
subscriptions. Drops chapter summaries, the front matter, tables, indexes,
essays, the Ecclesiasticus prologue and the end markers.

The compiled Markdown carries <!-- page NNN --> markers, which this script uses
to decide what is in range. The page ranges and the special cases below are
specific to this edition (1828 H. & E. Phinney, 884 PDF pages).

Usage:  python3 tools/make_sparse.py [--md FILE] [--out FILE] [--verbose]
"""
import argparse
import collections
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# PDF page ranges that hold Bible text: Old Testament, Apocrypha, New Testament.
# Excluded between them: tables and family record (581-586), the New Testament
# title page and dates table (687-688), and the index/tables/essays after 864.
PAGE_RANGES = [(15, 580), (587, 685), (689, 864)]

# Introductory notes that are not chapter summaries by shape, so they are named.
INTRO_NOTE_PREFIXES = ('This Psalm containeth', 'Set apart from the Beginning')

# Translator's prologue to Ecclesiasticus (introductory material, dropped).
PROLOGUE_TITLE_PREFIX = '# *The Prologue'

END_MARKERS = re.compile(r'(END OF THE (OLD TESTAMENT|APOCRYPHA)\.?|FINIS\.?|\*?FINIS\.?\*?)')


def in_range(pg):
    return pg is not None and any(a <= pg <= b for a, b in PAGE_RANGES)


def versey(p):
    """True if p opens like a chapter's unnumbered first verse (an all-caps first word)."""
    w = p.split()
    if not w:
        return False
    a = re.sub(r"[^A-Za-z'’]", '', w[0])
    if len(a) > 1 and a.isupper():
        return True
    if len(a) == 1 and len(w) > 1:  # "I SAID", "O LORD", "A WISE"
        b = re.sub(r"[^A-Za-z'’]", '', w[1])
        return len(b) > 1 and b.isupper()
    return False


def annotate(md_text):
    """Split into paragraphs, each tagged with the PDF page it starts on."""
    page = None
    items = []
    for p in md_text.split('\n\n'):
        ms = re.findall(r'<!-- page (\d+) -->', p)
        clean = re.sub(r'\s*<!-- page \d+ -->\s*', ' ', p).strip()
        if ms and p.startswith('<!-- page'):
            page = int(ms[0])
        if clean == '':
            continue
        items.append([page, clean])
        if ms and not p.startswith('<!-- page'):
            page = int(ms[-1])
    return items


def select(items):
    out, dropped, diag = [], [], []
    i, n = 0, len(items)
    while i < n:
        pg, p = items[i]
        if not in_range(pg):
            i += 1
            continue
        if p.startswith(PROLOGUE_TITLE_PREFIX):
            dropped.append((pg, 'PROLOGUE ' + p[:50]))
            i += 1
            while i < n and not items[i][1].startswith('#'):
                dropped.append((items[i][0], 'prologue text ' + items[i][1][:40]))
                i += 1
            continue
        if END_MARKERS.fullmatch(p.strip('* ')):
            dropped.append((pg, p))
            i += 1
            continue
        out.append((pg, p))
        if p.startswith('#'):
            # Drop the chapter summary / intro paragraph(s) that follow a heading;
            # keep italic sub-headings (Psalm titles) and stop at the first verse.
            j = i + 1
            while j < n and in_range(items[j][0]) and not items[j][1].startswith('#'):
                p1 = items[j][1]
                p2 = items[j + 1][1] if j + 1 < n else ''
                summ = False
                if '....' in p1:
                    summ = True
                elif re.match(r'\d+ ', p1):
                    summ = not (re.match(r'\d+ ', p2) or p2.startswith('#'))
                elif p1.startswith('*'):
                    out.append(items[j])
                    j += 1
                    continue
                elif versey(p1):
                    break
                else:
                    summ = (versey(p2) or p2.startswith('*') or p2.startswith('#')
                            or p1.startswith(INTRO_NOTE_PREFIXES))
                    if not summ:
                        diag.append(('KEPT-nonverse-after-heading', items[j][0], p[:30], '|', p1[:60]))
                if summ:
                    dropped.append((items[j][0], 'SUMMARY ' + p1[:50]))
                    j += 1
                    continue
                break
            i = j
            continue
        i += 1
    return out, dropped, diag


def plain(l):
    l = l.replace('**', '').replace('*', '')
    l = re.sub(r'^#{1,6}[ \t]+', '', l)
    l = re.sub(r'</?[a-zA-Z][^>]*>', '', l)
    return re.sub(r'(?<=\S) {2,}(?=\S)', ' ', l).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--md', default=str(ROOT / 'phinney-bible.md'))
    ap.add_argument('--out', default=str(ROOT / 'phinney-bible-sparse.txt'))
    ap.add_argument('--verbose', action='store_true', help='print what was dropped or kept unexpectedly')
    args = ap.parse_args()

    items = annotate(Path(args.md).read_text(encoding='utf-8'))
    out, dropped, diag = select(items)
    text = '\n\n'.join(plain(p) for pg, p in out if plain(p)) + '\n'
    text = re.sub(r'\n{3,}', '\n\n', text)
    Path(args.out).write_text(text, encoding='utf-8')

    print(f'kept {len(out)} paragraphs, dropped {len(dropped)}, {len(text.split())} words -> {args.out}')
    print(dict(collections.Counter(d[1].split()[0] for d in dropped)))
    if args.verbose:
        for d in diag:
            print(d)
        for d in dropped:
            if not d[1].startswith(('SUMMARY', 'prologue')):
                print(d)


if __name__ == '__main__':
    main()
