#!/usr/bin/env python3
"""Compile phinney-bible-pages/page-*.md into one Markdown file (main text only).

Removes: HTML comments, the Marginal notes section, Footer: lines, **Header:**
running heads, layout-only column subheadings, superscript reference marks
(<sup>..</sup>) and the inline printed parallel mark "||" (they only point to
margin notes).
Joins verses/paragraphs that run across a page break (the page comment
<!-- page NNN --> is left at the join), and puts a <!-- page NNN --> comment
at the start of each page's text.

Usage:  python3 tools/compile_markdown.py [--pages-dir DIR] [--out FILE]
"""
import argparse
import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean_page(t):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.split(r'\n---\s*\n+### Marginal notes', t)[0]
    t = t.split('### Marginal notes')[0]
    t = re.sub(r'(?m)^\*\*Header:\*\*.*\n?', '', t)
    t = re.sub(r'(?m)^(- )?Footer:.*\n?', '', t)
    t = re.sub(r'(?mi)^### .*\b(left|right) column\b.*$\n?', '', t)
    t = re.sub(r'<sup>.*?</sup>', '', t)
    t = t.replace('\\*', '*')
    t = re.sub(r'(?<=\S)[ \t]{2,}(?=\S)', ' ', t)
    t = re.sub(r'[ \t]+$', '', t, flags=re.M)
    t = re.sub(r'\n{3,}', '\n\n', t).strip('\n')
    return t


def compile_pages(files):
    out = []
    joined = 0
    for f in files:
        n = int(f[-6:-3])
        t = clean_page(open(f, encoding='utf-8').read())
        if not t.strip():
            continue
        paras = t.split('\n\n')
        first = paras[0]
        isbody = (not re.match(r'(\d|#|\||\*\d|[-*] |¶ ?\d)', first)) and '\n' not in first.strip()
        # A page whose first paragraph continues the previous page's last paragraph.
        # (An all-caps opening word marks a title or a chapter's first verse, not a
        # continuation; LORD/GOD are the exception.)
        if (out and isbody
                and not re.match(r'(?!LORD|GOD)[A-Z]{4,}', first.lstrip('*'))
                and not out[-1].startswith(('#', '|', '<!--'))):
            prev = out[-1].rstrip()
            cont = (first[:1].islower()
                    or (first.startswith('*') and first[1:2].islower())
                    or prev[-1] not in '.?!:;"\'')
            if cont:
                if prev.endswith('-') and first[:1].islower() and not prev.endswith(' -'):
                    out[-1] = prev[:-1] + first + f' <!-- page {n:03d} -->'
                else:
                    out[-1] = prev + ' ' + f'<!-- page {n:03d} -->' + ' ' + first
                joined += 1
                out.extend(paras[1:])
                continue
        out.append(f'<!-- page {n:03d} -->')
        out.extend(paras)

    # Mid-page joins: a lowercase-start paragraph after one that stops mid-sentence
    # (a paragraph split across a column break).
    fixed = []
    for p in out:
        if (fixed and p[:1].islower()
                and not fixed[-1].startswith(('#', '|', '<!--')) and '\n' not in p):
            q = re.sub(r'<!--.*?-->', '', fixed[-1]).rstrip().rstrip('*').rstrip()
            if q and q[-1] not in '.?!:"\')”’':
                if q.endswith('-') and not q.endswith(' -'):
                    fixed[-1] = fixed[-1].rstrip()[:-1] + p
                else:
                    fixed[-1] = fixed[-1].rstrip() + ' ' + p
                joined += 1
                continue
        fixed.append(p)

    text = '\n\n'.join(fixed) + '\n'
    return re.sub(r'\n{3,}', '\n\n', text), joined


def strip_parallel_marks(text):
    """Remove the inline printed parallel mark '||' from non-table lines."""
    lines = text.split('\n')
    removed = 0
    for i, l in enumerate(lines):
        if l.startswith('|') or '||' not in l:
            continue
        removed += l.count('||')
        l2 = re.sub(r' ?\|\| ?', ' ', l)
        if not l2.startswith(' '):
            l2 = re.sub(r'(?<=\S) {2,}(?=\S)', ' ', l2).strip(' ')
        lines[i] = l2
    return '\n'.join(lines), removed


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pages-dir', default=str(ROOT / 'phinney-bible-pages'))
    ap.add_argument('--out', default=str(ROOT / 'phinney-bible.md'))
    args = ap.parse_args()

    files = sorted(glob.glob(str(Path(args.pages_dir) / 'page-*.md')))
    text, joined = compile_pages(files)
    text, marks = strip_parallel_marks(text)
    Path(args.out).write_text(text, encoding='utf-8')
    print(f'{len(files)} pages, {joined} joins, {marks} parallel marks removed, {len(text.split())} words -> {args.out}')


if __name__ == '__main__':
    main()
