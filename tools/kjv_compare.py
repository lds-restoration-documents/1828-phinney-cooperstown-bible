#!/usr/bin/env python3
"""Compare the Phinney transcription with a reference KJV text, word by word.

Used by make_typo_catalog.py; also runnable on its own to list the differences.
The reference is the Project Gutenberg King James Version (ebook #10, plain text,
https://www.gutenberg.org/cache/epub/10/pg10.txt), which is NOT stored in this repo.
It has no Apocrypha, so only the 66 canonical books are compared.

What it does
  1. Parses the reference into book / chapter / verse, and phinney-bible-sparse.txt
     into book / chapter / paragraph (the same 66 books, in order).
  2. Per chapter, aligns the two word streams (lower-cased, punctuation and hyphens
     removed) with difflib and collects every difference, with the KJV verse.
  3. Sets aside differences that are the edition's own conventions rather than slips:
     spacing only (`burnt-offering` vs `burnt offering`) and any pair that recurs 4 or
     more times (`a`/`an`, `thy`/`thine`, `wo`/`woe`, ...).
  4. Checks each paragraph's printed verse number against the verse its text aligns to.
  5. Finds the PDF page of each difference by searching the page files.

A difference from the reference is not necessarily a printer's error: KJV editions
differ from each other, so most of what is left is an edition variant. Telling the two
apart is done by hand (see make_typo_catalog.py).

Usage:  python3 tools/kjv_compare.py --kjv pg10.txt [--summary]
"""
import argparse
import collections
import difflib
import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compile_markdown  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# PDF page ranges that hold the canonical text (see make_sparse.py): Old and New Testament.
CANON_PAGES = [(15, 580), (689, 864)]

CHAPTER_RE = re.compile(r'^[—–-]*\s*(CHAPTER|PSALM)[-\s]*([IVXLC]+)\.?\s*$')


# ---------------------------------------------------------------- reference KJV
def parse_kjv(path):
    """Return [{'title', 'chs': {chapter: [[verse, text], ...]}}] for the 66 books."""
    L = Path(path).read_text(encoding='utf-8').split('\n')
    s = next(i for i, l in enumerate(L) if l.startswith('*** START'))
    testaments = ('The Old Testament of the King James Version of the Bible',
                  'The New Testament of the King James Bible')
    toc, i = [], s + 1
    while True:
        l = L[i].strip()
        i += 1
        if l in testaments or not l:
            continue
        toc.append(l)
        if l.startswith('The Revelation'):
            break
    assert len(toc) == 66, len(toc)
    pos, j = [], i
    for t in toc:
        while L[j].strip() != t or L[j - 1].strip() != '':
            j += 1
        pos.append(j)
        j += 1
    pos.append(next(k for k, l in enumerate(L) if l.startswith('*** END')))
    books = []
    for b, t in enumerate(toc):
        seg = ' '.join(x.strip() for x in L[pos[b] + 1:pos[b + 1]])
        seg = seg[re.search(r'\b1:1\s', seg).start():]
        toks = re.split(r'(\b\d+:\d+)(?=\s)', seg)
        ch = vs = 0
        chapters = {}
        for k in range(1, len(toks), 2):
            c, v = map(int, toks[k].split(':'))
            if (c == ch and v == vs + 1) or (c == ch + 1 and v == 1):
                ch, vs = c, v
                chapters.setdefault(c, []).append([v, toks[k + 1].strip()])
            else:  # a chapter:verse look-alike inside the text
                chapters[ch][-1][1] += ' ' + toks[k] + toks[k + 1]
        books.append({'title': t, 'chs': chapters})
    return books


# ---------------------------------------------------------------- Phinney text
def norm_words(t):
    """Words for comparison: lower case, no punctuation, hyphenated words closed up."""
    t = t.replace('’', "'").replace('¶', ' ').replace('||', ' ')
    t = re.sub(r"['‘]", '', t)
    t = re.sub(r'(?<=\w)[-–—](?=\w)', '', t)
    t = re.sub(r'[-–—]', ' ', t)
    return re.findall(r'[A-Za-z0-9]+', t.lower())


def parse_phinney(md_path, sparse_path):
    """The 66 canonical books from the sparse file: [{'title', 'chs': [(heading, [para])]}]."""
    md = Path(md_path).read_text(encoding='utf-8')
    heads = {re.sub(r'\s+', ' ', l[2:].replace('*', '')).strip() for l in md.split('\n') if l.startswith('# ')}
    books, cur = [], None
    for p in Path(sparse_path).read_text(encoding='utf-8').split('\n\n'):
        p = p.strip()
        if not p:
            continue
        if p in heads:
            cur = {'title': p, 'chs': [('(none)', [])]}
            books.append(cur)
            continue
        if cur is not None and CHAPTER_RE.match(p):
            if cur['chs'][-1][0] == '(none)' and not cur['chs'][-1][1]:
                cur['chs'].pop()
            cur['chs'].append((p, []))
        elif cur is not None:
            cur['chs'][-1][1].append(p)
    i = next(k for k, b in enumerate(books) if 'MATTHEW' in b['title'])
    return books[:39] + books[i:i + 27]


def label_split(p):
    """Split a verse paragraph into (printed verse label or None, text)."""
    m = re.match(r'^(\d+|[a-z]|[A-Za-z]?\d[\dA-Za-z]*)\s+(.*)$', p, re.S)
    return (m.group(1), m.group(2)) if m else (None, p)


# ---------------------------------------------------------------- page lookup
def page_stream(pages_dir):
    """All canonical-page words (no numerals) as parallel lists (words, pages), in reading order."""
    words, pages = [], []
    for f in sorted(glob.glob(str(Path(pages_dir) / 'page-*.md'))):
        n = int(f[-6:-3])
        if not any(a <= n <= b for a, b in CANON_PAGES):
            continue
        w = [x for x in norm_words(compile_markdown.clean_page(Path(f).read_text(encoding='utf-8')))
             if not x.isdigit()]  # verse numbers are not part of the compared text
        words += w
        pages += [n] * len(w)
    return words, pages


class PageFinder:
    """Locate a short word sequence in the page stream, preferring the next hit after the last one."""

    def __init__(self, words, pages):
        self.words, self.pages, self.ptr = words, pages, 0
        self.index = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.index[w].append(i)

    def find(self, seq, offset=0):
        """Page of word `offset` of `seq` (default: the first word)."""
        seq = [w for w in seq if w]
        if not seq:
            return None
        hits = [i for i in self.index.get(seq[0], ()) if self.words[i:i + len(seq)] == seq]
        ahead = [i for i in hits if i >= self.ptr]
        if ahead or len(hits) == 1:  # else ambiguous and behind us: give up rather than guess
            i = (ahead or hits)[0]
            self.ptr = max(self.ptr, i) if ahead else self.ptr
            return self.pages[i + offset]
        return None


# ---------------------------------------------------------------- comparison
def compare(kjv, phinney, finder=None):
    """Return (diffs, label_anomalies). `diffs` keep Bible order."""
    diffs, anomalies = [], []
    for kb, pb in zip(kjv, phinney):
        for ci, (heading, paras) in enumerate(pb['chs'], 1):
            kv = kb['chs'][ci]
            kt, kmap = [], []
            for v, t in kv:
                w = norm_words(t)
                kt += w
                kmap += [v] * len(w)
            pt, pmap, plab = [], [], []
            for pi, p in enumerate(paras):
                lab, txt = label_split(p)
                plab.append(lab)
                w = norm_words(txt)
                pt += w
                pmap += [pi] * len(w)
            sm = difflib.SequenceMatcher(None, pt, kt, autojunk=False)
            ops = sm.get_opcodes()
            votes = collections.defaultdict(collections.Counter)
            for tag, i1, i2, j1, j2 in ops:
                if tag == 'equal':
                    for d in range(i2 - i1):
                        votes[pmap[i1 + d]][kmap[j1 + d]] += 1
            for pi, lab in enumerate(plab):
                v = votes[pi].most_common(1)[0][0] if votes[pi] else None
                if lab is None:
                    if pi == 0 or v == 1:
                        continue
                elif lab.isdigit() and (v is None or int(lab) == v):
                    continue
                anomalies.append(dict(book=kb['title'], ch=ci, verse=v, label=lab, text=paras[pi],
                                      page=None))
            for tag, i1, i2, j1, j2 in ops:
                if tag == 'equal':
                    continue
                v = kmap[j1] if j1 < len(kmap) else kmap[-1]
                diffs.append(dict(book=kb['title'], ch=ci, v=v, tag=tag, p=pt[i1:i2], k=kt[j1:j2],
                                  before=pt[max(0, i1 - 4):i1], after=pt[i2:i2 + 4], page=None))
    if finder:
        for d in diffs:
            seq = d['before'] + d['p'] + d['after']
            d['page'] = (finder.find(seq, len(d['before'])) if d['p'] else finder.find(seq, max(len(d['before']) - 1, 0))) \
                or finder.find(d['before'][-2:] + d['p'], len(d['before'][-2:]))
    return diffs, anomalies


def classify(diffs):
    """Mark each diff 'spacing', 'systematic', 'title' or None (a candidate)."""
    key = lambda d: (' '.join(d['p']), ' '.join(d['k']))
    for d in diffs:
        d['cls'] = 'spacing' if ''.join(d['p']) == ''.join(d['k']) else None
    n = collections.Counter(key(d) for d in diffs if d['cls'] is None)
    for d in diffs:
        if d['cls'] is None and n[key(d)] >= 4:
            d['cls'] = 'systematic'
        elif d['cls'] is None and not d['k'] and (
                ('Psalms' in d['book'] and len(d['p']) >= 2) or 'was written' in ' '.join(d['p'])):
            d['cls'] = 'title'  # Psalm titles and epistle subscriptions: absent from the reference
    return diffs


def load(kjv_path, root=ROOT):
    kjv = parse_kjv(kjv_path)
    phin = parse_phinney(root / 'phinney-bible.md', root / 'phinney-bible-sparse.txt')
    finder = PageFinder(*page_stream(root / 'phinney-bible-pages'))
    diffs, anomalies = compare(kjv, phin, finder)
    return classify(diffs), anomalies


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--kjv', required=True, help='path to the Gutenberg KJV plain text (pg10.txt)')
    ap.add_argument('--summary', action='store_true', help='print counts only')
    args = ap.parse_args()
    diffs, anomalies = load(args.kjv)
    print(collections.Counter(d['cls'] for d in diffs), 'verse-label anomalies:', len(anomalies))
    if args.summary:
        return
    for d in diffs:
        if d['cls'] is None:
            print(f"p.{d['page']} {d['book']} {d['ch']}:{d['v']} {d['tag']}: {' '.join(d['p'])!r} vs {' '.join(d['k'])!r}")


if __name__ == '__main__':
    main()
