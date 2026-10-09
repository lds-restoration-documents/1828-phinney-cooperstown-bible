#!/usr/bin/env python3
"""Build printer-typos.md: a catalog of the printer's slips in the 1828 Phinney text.

Three parts:
  1. Printer's typos: a curated list of forms (below). The script finds every
     occurrence in the page files, with its PDF page and a snippet of context, so page
     numbers and contexts stay current if the pages are edited.
  2. Verse numbers printed wrongly or left off, found by comparing each paragraph's
     number with the verse its text matches in the reference KJV.
  3. Variants: every word difference from the reference KJV that is not a typo and not
     an edition-wide convention. Most are differences between KJV editions, not errors.

Parts 2 and 3 need the reference text (Project Gutenberg ebook #10, not stored here):
    curl -o pg10.txt https://www.gutenberg.org/cache/epub/10/pg10.txt
The marginal notes (cross-references) are deliberately left out of all three parts.

Usage:  python3 tools/make_typo_catalog.py --kjv pg10.txt [--out FILE]
"""
import argparse
import collections
import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kjv_compare  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# PDF pages 1-329 were audited against the scan, except these (see CLAUDE.md).
UNAUDITED = {213, 214, 230, 246, 308, 309, 310, 324, 325, 326} | set(range(274, 279)) | set(range(290, 295))


def audited(pg):
    return 1 <= pg <= 329 and pg not in UNAUDITED


# Dropped words listed under typos, as (PDF page, reference word); left out of the variants.
DROPPED = {(73, 'ye')}

# (printed, should be, note). `printed` is a whole word (case-insensitive) or a tuple
# (phrase to find, the printed word inside it).
SECTIONS = [
    ('Letter or letters dropped', [
        ('assemby', 'assembly', ''), ('cites', 'cities', ''), ('familes', 'families', ''),
        (('nd except those days', 'nd'), 'and', 'the first letter missing'),
        (('Bu he answered', 'Bu'), 'but', 'the last letter missing'),
        (('congregation of he LORD', 'he'), 'the', 'a real word'), ('remnat', 'remnant', 'in the Apocrypha'),
        (('sabbat fo rest', 'sabbat'), 'sabbath', ''),
        (('at this ime prince', 'ime'), 'time', 'in the Apocrypha'), (('thou has dreamed', 'has'), 'hast', 'a real word'),
    ]),
    ('Word dropped', [
        (('14 shall keep the sabbath therefore', '14'), 'Ye', 'the word "Ye" is not printed: a blank gap and a stray mark follow the verse number (Ex. 31:14)'),
    ]),
    ('Letter added or doubled', [
        ('Mannasseh', 'Manasseh', 'a name'),
    ]),
    ('Letters transposed', [
        ('daivd', 'David', ''), ('brethern', 'brethren', ''), ('tna', 'that', ''), ('hunrded', 'hundred', ''),
        ('straeks', 'strakes', ''), (('Lord fo heaven', 'fo'), 'of', ''), (('sabbat fo rest', 'fo'), 'of', ''),
    ]),
    ('Wrong letter (one letter printed for another)', [
        (('and 1 have broken', '1'), 'I', 'a numeral 1 for the capital I'), ('anb', 'and', ''), ('mv', 'my', 'worn type: the second letter looks like a v'), ('tride', 'tribe', ''), ('hunbred', 'hundred', ''), ('israei', 'Israel', ''),
        (('ana my concubine', 'ana'), 'and', ''), (('work of Ged', 'Ged'), 'God', 'worn type: the G and e are damaged'),
        (('shall not five by bread', 'five'), 'live', 'worn type: the first letter has an f shape'),
        (('measures of the alter', 'alter'), 'altar', 'a real word'),
        ('feraful', 'fearful', 'in the Apocrypha'), ('wno', 'who', 'in the Apocrypha'),
        ('baptizm', 'baptism', 'in a chapter summary'), ('aescribed', 'described', 'in a Psalm summary, italic'),
        ('inspirea', 'inspired', 'in a running head, italic'), (('false teachers, ana their', 'ana'), 'and', 'in a running head, italic'),
        ('anotner', 'another', 'in a chapter summary'), ('wcrld', 'world', 'in a chapter summary'),
        ('peovle', 'people', 'in a running head'),
    ]),
    ('Words run together or divided wrongly', [
        ('hastbrought', 'hast brought', ''), (('Cursed be them an that', 'them an'), 'the man', 'the break between the words is in the wrong place'),
    ]),
]

CONVENTIONS = """## Not included: the edition's own conventions

These differ from the reference text, or from modern spelling, but are the edition's regular practice and not slips. The first group
is counted live from the comparison (every pair that recurs four or more times); the rest is noted by hand.

- **Compounds printed hyphenated or closed up** where the reference has two words (`burnt-offering`, `sin-offering`, `shittim-wood`, `he-goat`; 1,900 differences in all). The compiled text closes them up only at a page break when the compound is not printed hyphenated elsewhere.
- **Archaic and 1769-style forms:** `-eth` and `-est` verbs, `shew`, `wo`, `to-day`, `to-morrow`, `every where`, `for ever`, `thine` before a vowel.
- **Words the printer kept on one line break:** a hyphen at the end of a page (`Abra-` / `ham`) is closed up in the compiled text.
"""


def page_texts(pages_dir):
    """PDF page -> that page's text: main text and running head, no marginal notes, tags or comments."""
    out = {}
    for f in sorted(glob.glob(str(Path(pages_dir) / 'page-*.md'))):
        t = Path(f).read_text(encoding='utf-8')
        t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
        t = re.split(r'\n---\s*\n+### Marginal notes', t)[0].split('### Marginal notes')[0]
        t = re.sub(r'(?m)^\*\*Header:\*\*', '', t)
        t = re.sub(r'(?m)^(- )?Footer:.*$', '', t)
        t = re.sub(r'<sup>.*?</sup>', '', t).replace('\\*', '*').replace('*', '')
        out[int(f[-6:-3])] = re.sub(r'\s+', ' ', t)
    return out


def find(pages, spec):
    """Yield (page, snippet with the hit in bold, printed form) for each occurrence."""
    if isinstance(spec, tuple):
        phrase, hit = spec
        rx = re.compile(re.escape(phrase))
    else:
        phrase, hit = spec, spec
        rx = re.compile(r'(?<![A-Za-z])' + re.escape(spec) + r'(?![A-Za-z])', re.I)
    for pg, t in pages.items():
        for m in rx.finditer(t):
            a, b = max(0, m.start() - 36), min(len(t), m.end() + 30)
            s = t[a:b]
            i = (m.start() - a) + (re.search(r'(?<![A-Za-z])' + re.escape(hit) + r'(?![A-Za-z])', phrase).start() if isinstance(spec, tuple) else 0)
            form = s[i:i + len(hit)]
            s = s[:i] + '**' + form + '**' + s[i + len(hit):]
            yield pg, ('…' if a else '') + s.strip() + ('…' if b < len(t) else ''), form


def basis(pg, form=None):
    """Every row was compared with the scan at zoom for this catalog; pages 1-329 were also audited earlier."""
    return 'audit + scan' if audited(pg) else 'scan'


ABBR = [('Genesis', 'Gen.'), ('Exodus', 'Ex.'), ('Leviticus', 'Lev.'), ('Numbers', 'Num.'), ('Deuteronomy', 'Deut.'),
        ('Joshua', 'Josh.'), ('Judges', 'Judg.'), ('Ruth', 'Ruth'), ('First Book of Samuel', '1 Sam.'),
        ('Second Book of Samuel', '2 Sam.'), ('First Book of the Kings', '1 Kings'), ('Second Book of the Kings', '2 Kings'),
        ('First Book of the Chronicles', '1 Chron.'), ('Second Book of the Chronicles', '2 Chron.'), ('Ezra', 'Ezra'),
        ('Nehemiah', 'Neh.'), ('Esther', 'Esth.'), ('Job', 'Job'), ('Psalms', 'Ps.'), ('Proverbs', 'Prov.'),
        ('Ecclesiastes', 'Eccl.'), ('Song of Solomon', 'Song'), ('Isaiah', 'Isa.'), ('Jeremiah', 'Jer.'),
        ('Lamentations', 'Lam.'), ('Ezekiel', 'Ezek.'), ('Daniel', 'Dan.'), ('Hosea', 'Hos.'), ('Joel', 'Joel'),
        ('Amos', 'Amos'), ('Obadiah', 'Obad.'), ('Jonah', 'Jonah'), ('Micah', 'Mic.'), ('Nahum', 'Nah.'),
        ('Habakkuk', 'Hab.'), ('Zephaniah', 'Zeph.'), ('Haggai', 'Hag.'), ('Zechariah', 'Zech.'), ('Malachi', 'Mal.'),
        ('Matthew', 'Matt.'), ('Mark', 'Mark'), ('Luke', 'Luke'), ('Gospel According to Saint John', 'John'),
        ('Acts', 'Acts'), ('Romans', 'Rom.'), ('First Epistle of Paul the Apostle to the Corinthians', '1 Cor.'),
        ('Second Epistle of Paul the Apostle to the Corinthians', '2 Cor.'), ('Galatians', 'Gal.'),
        ('Ephesians', 'Eph.'), ('Philippians', 'Phil.'), ('Colossians', 'Col.'),
        ('First Epistle of Paul the Apostle to the Thessalonians', '1 Thess.'),
        ('Second Epistle of Paul the Apostle to the Thessalonians', '2 Thess.'),
        ('First Epistle of Paul the Apostle to Timothy', '1 Tim.'), ('Second Epistle of Paul the Apostle to Timothy', '2 Tim.'),
        ('Titus', 'Titus'), ('Philemon', 'Philem.'), ('Hebrews', 'Heb.'), ('James', 'James'),
        ('First Epistle General of Peter', '1 Pet.'), ('Second General Epistle of Peter', '2 Pet.'),
        ('First Epistle General of John', '1 John'), ('Second Epistle General of John', '2 John'),
        ('Third Epistle General of John', '3 John'), ('Jude', 'Jude'), ('Revelation', 'Rev.')]


def abbr(title):
    for key, a in ABBR:
        if key in title:
            return a
    return title


def snippet(d):
    hit = ' '.join(d['p']) or '▲'  # ▲ marks where the reference has a word the Phinney text lacks
    return '…' + ' '.join(d['before'][-3:]) + ' **' + hit + '** ' + ' '.join(d['after'][:3]) + '…'


def variants_section(diffs, typo_hits, pages):
    names = {}
    rows = collections.defaultdict(list)
    for d in diffs:
        if d['cls'] is not None or d['p'] == ['1'] or (not d['p'] and (d['page'], ' '.join(d['k'])) in DROPPED) or any((d['page'], w) in typo_hits for w in d['p']):
            continue
        p, k = ' '.join(d['p']), ' '.join(d['k'])
        if not d['k']:
            cat = 'Words in the Phinney text that the reference lacks'
        elif not d['p']:
            cat = 'Words in the reference that the Phinney text lacks'
        elif len(d['p']) == 1 and len(d['k']) == 1:
            a, b = d['p'][0], d['k'][0]
            text = pages.get(d['page'], '')
            if b in (a + 's', a + 'es') or a in (b + 's', b + 'es'):
                cat = 'Singular or plural'
            elif re.search(r'(?<![.!?] )(?<!^)\b' + a[:1].upper() + a[1:] + r'\b', text) and a not in ('i',):
                cat = 'Names spelled differently'
            else:
                cat = 'Other spelling or word differences'
        else:
            cat = 'Longer differences'
        rows[cat].append('| %s | %s | %s %d:%d | %s | %s |' % (
            ('`%s`' % p) if p else '—', ('`%s`' % k) if k else '—', abbr(d['book']), d['ch'], d['v'],
            d['page'] or '?', snippet(d).replace('|', '\\|')))
    order = ['Singular or plural', 'Names spelled differently', 'Other spelling or word differences',
             'Words in the Phinney text that the reference lacks', 'Words in the reference that the Phinney text lacks',
             'Longer differences']
    out, total = [], 0
    for cat in order:
        r = rows.get(cat, [])
        total += len(r)
        out.append('\n### %s (%d)\n\n| Phinney | Reference | Verse | PDF p. | Context (lower case, no punctuation) |\n|---|---|---|---|---|\n%s'
                   % (cat, len(r), '\n'.join(r)))
    return total, '\n'.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--kjv', required=True, help='path to the Gutenberg KJV plain text (pg10.txt)')
    ap.add_argument('--out', default=str(ROOT / 'printer-typos.md'))
    args = ap.parse_args()

    pages = page_texts(ROOT / 'phinney-bible-pages')
    body, total, missing, typo_hits = [], 0, [], set()
    hdr = '| Printed | Should be | PDF p. | In context | Checked |\n|---|---|---|---|---|'
    for title, items in SECTIONS:
        rows = []
        for spec, should, note in items:
            hits = list(find(pages, spec))
            if not hits:
                missing.append(spec)
            word = spec[1] if isinstance(spec, tuple) else spec
            for pg, snip, form in hits:
                typo_hits.add((pg, form.lower()))
                rows.append((pg, '| `%s` | %s | %d | %s%s | %s |' % (
                    form, should, pg, snip.replace('|', '\\|'), (' (%s)' % note) if note else '', basis(pg, form))))
        rows.sort(key=lambda x: x[0])
        total += len(rows)
        body.append('\n## %s (%d)\n\n%s\n%s\n' % (title, len(rows), hdr, '\n'.join(r for _, r in rows)))

    diffs, anomalies = kjv_compare.load(args.kjv, ROOT)
    arows = []
    for a in anomalies:
        if a['label'] is None and a['verse'] is None:
            continue  # Psalm titles and epistle subscriptions
        if 'Psalms' in a['book'] and a['label'] is None:
            continue
        arows.append(a)
    fin = kjv_compare.PageFinder(*kjv_compare.page_stream(ROOT / 'phinney-bible-pages'))
    vrows = []
    for a in arows:
        txt = a['text'][len(a['label']):].strip() if a['label'] else a['text']
        pg = fin.find(kjv_compare.norm_words(txt)[:6])
        vrows.append('| %s %d:%d | %s | %s | %s |' % (abbr(a['book']), a['ch'], a['verse'], '`%s`' % a['label'] if a['label'] else 'none (unnumbered)',
                                                  pg or '?', basis(pg) if pg else 'scan'))
    vsec = ('\n## Verse numbers printed wrongly or left off (%d)\n\nThe verse a paragraph\'s text matches in the reference, against the number the page prints. '
            'Every row was compared with the scan at zoom. Unnumbered first verses of a chapter are the edition\'s practice and are not listed.\n\n'
            '| Verse | Printed number | PDF p. | Checked |\n|---|---|---|---|\n%s' % (len(vrows), '\n'.join(vrows)))

    vtotal, vsec2 = variants_section(diffs, typo_hits, pages)
    sysn = collections.Counter(' '.join(d['p']) + ' / ' + ' '.join(d['k']) for d in diffs if d['cls'] == 'systematic')
    top = ', '.join('`%s` (%d×)' % (k, n) for k, n in sysn.most_common(14) if '/ ' in k)
    counts = collections.Counter(d['cls'] for d in diffs)

    intro = f"""# Printer's slips in the 1828 Phinney Bible

A catalog of the places where the printing itself has a slip of the type, as the transcription records it: {total} occurrences of
{sum(len(i) for _, i in SECTIONS)} forms, plus {len(vrows)} wrongly printed or missing verse numbers, and a section of {vtotal} variants from a reference KJV that are mostly *not* errors.
**Marginal notes and their cross-references are left out entirely.**

**What is and is not here.** The transcription keeps every printed error as printed (nothing was corrected from the KJV), so each form below is
in the page files as printed. The typo list is **likely, not exhaustive**. It comes from comparing the whole text with the Project Gutenberg KJV
(ebook #10) word by word, from a dictionary scan of the words the comparison cannot reach (the Apocrypha, chapter summaries and running heads), and from the slips already
noted in `transcription-notes.md`, then triaged by hand. A slip that gives another real word is caught only where the comparison happened to flag it.

**How each row was checked.** Every row of the typo list and the verse-number table was compared with the scanned page at zoom, one by one, and the printed
letters match the transcription in all of them, so none is a transcription error. The *Checked* column says `audit + scan` for pages 1–329 (written by Opus 5.5 and
audited against the scan earlier; the unaudited exceptions listed in CLAUDE.md are excluded) and `scan` for pages 330 and up (written by Sonnet 5.5, not otherwise audited). Where the
type is worn and the letter could be read two ways (`mv`, `Ged`, `five`), the row says so. The variants section was checked too (see its heading).

Generated by `tools/make_typo_catalog.py` from the live text and the reference KJV (`tools/kjv_compare.py`).
{''.join(body)}
{vsec}

## Variants from the reference KJV ({vtotal})

Word differences between this text and the Gutenberg KJV that are **not** in the typo list above and are not edition-wide conventions. Most reflect
different KJV editions (the Gutenberg text is a later standardization, and the 1828 text follows an earlier one) or the edition's own spellings, not printer's errors. A few are
slips in the reference itself (for example `took`/`look` in Jonah 1:15). Some are slips in this edition that could not be told from a variant: a one-letter difference
in a name (`Arvan` for `Arvad`, Ezek. 27:11) is the most likely kind. Treat a row as a lead, not a finding. **Checked against the scan:** about 200 variants where the PDF's own text layer did not clearly agree with the transcription were each compared with the scan at zoom, and the rest agree with the text layer or repeat a pattern already seen; none of them was found to be a transcription error. (The text layer is noisy, so that second group is a weaker check than the first.) Counts of the differences set aside: {counts['spacing']} that differ only in spacing, {counts['systematic']} edition-wide pairs ({top}), and {counts['title']} Psalm titles and epistle subscriptions the reference lacks.
{vsec2}

{CONVENTIONS}"""
    Path(args.out).write_text(intro, encoding='utf-8')
    print(f'{total} typo occurrences, {len(vrows)} verse-number rows, {vtotal} variants -> {args.out}')
    if missing:
        print('NOT FOUND in the text:', missing)


if __name__ == '__main__':
    main()
