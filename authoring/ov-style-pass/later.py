#!/usr/bin/env python3
"""Add a 'Later printings' table + float-clear fix to Original Virtual Set pages.

usage: later.py N [N ...]   reads live/ovsN.wiki, writes final/ovsN.wiki and final/reportN.json
"""
import json, re, sys, difflib, os

ROWS = json.load(open(os.path.join(os.path.dirname(__file__), 'rows.json')))
MODERN_MIN = 0.5   # modern card counts as a re-use only when its game text is this close to the OV text


def norm(s):
    s = re.sub(r'\((V|Light|Dark|AI|Holo AI|C-Slip AI \d*|C-Slip AI)\)', '', s)
    s = re.sub(r'\(Virtual (Set|Block)[^)]*\)', '', s)
    s = s.replace('•', '').replace('’', "'").replace('&amp;', '&').lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def clean(t):
    t = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', t)
    t = t.replace('&lt;', '<').replace('‘', "'").replace('’', "'").replace('•', '')
    return re.sub(r'\s+', ' ', t).strip().lower()


IDX = {}
for r in ROWS:
    halves = [h for h in re.split(r'\s*/\s*', r['disp']) if h]
    keys = [norm(r['disp'])]
    if len(halves) > 1:   # two-sided objective rows: index each half under the half its image shows
        imgkey = re.sub(r'[^a-z0-9]', '', r['img'].lower())
        keys = [norm(h) for h in halves if re.sub(r'[^a-z0-9]', '', norm(h)) in imgkey] or keys
    for k in keys:
        IDX.setdefault((k, r['side']), []).append(r)


def setnum(s):
    m = re.search(r'(\d+)$', s)
    return int(m.group(1)) if m else -1


def ov_rows(w):
    side, out = None, []
    for l in w.split('\n'):
        m = re.match(r'^===\s*\[\[(Light|Dark)', l)
        if m:
            side = m.group(1); continue
        m = re.match(r'^\| (\d+) \|\| .*?\|\| \[\[File:([^|]+)\|320px.*?\|\| \[\[File:([^|]+)\|200px.*?\|\| style="white-space:nowrap" \| \[\[([^|\]]+)\|?([^\]]*)\]\] \|\| .*?\|\| (.*)$', l)
        if m:
            out.append(dict(num=m.group(1), slip=m.group(2), rem=m.group(3), target=m.group(4),
                            disp=m.group(5) or m.group(4), side=side, text=m.group(6)))
    return out


def img_cell(r, label_extra=''):
    link = r['target'] if '(V)' in r['target'] else r['set']
    cap = f"[[{r['set']}]]" + label_extra
    return f"[[File:{r['img']}|120px|link={link}]]<br />{cap}"


def build_section(w):
    rows_out, rep = [], []
    for o in ov_rows(w):
        hits = IDX.get((norm(o['disp']), o['side']), [])
        vb = sorted([h for h in hits if h['set'].startswith('Virtual Block')], key=lambda h: setnum(h['set']))
        mod = []
        for h in hits:
            if h['set'].startswith('Virtual Block') or not h['text']:
                continue
            sim = difflib.SequenceMatcher(None, clean(o['text']), clean(h['text'])).ratio()
            rep.append(dict(num=o['num'], card=o['disp'], later=h['disp'], set=h['set'], sim=round(sim, 2)))
            if sim >= MODERN_MIN:
                mod.append((h, sim))
        if not vb and not mod:
            continue
        mod.sort(key=lambda x: setnum(x[0]['set']))
        vbc = ' '.join(img_cell(h) for h in vb)
        mc = ' '.join(img_cell(h, ' (same text)' if s > 0.97 else ' (revised text)') for h, s in mod)
        card = f"[[{o['target']}|{o['disp']}]]"
        rows_out.append(f"|-\n| {o['num']} || style=\"white-space:nowrap\" | {card} || [[File:{o['rem']}|120px|link={o['target']}]] || {vbc} || {mc}")
    if not rows_out:
        return None, rep
    head = ('{| class="wikitable" style="text-align:center;"\n'
            '! # !! Card !! This set !! [[:Category:Virtual Legacy sets|Virtual Block]] (2009) !! Virtual Sets (2014 onward)')
    return head + '\n' + '\n'.join(rows_out) + '\n|}', rep


REORG_RE = re.compile(r'In the 2009 reorganisation the Committee regrouped the Original Virtual cards into the \[\[:Category:Virtual Legacy sets\|Virtual Blocks\]\]\.(<ref name="reorg2009">.*?</ref>)')


def finalize(w):
    table, rep = build_section(w)
    m = REORG_RE.search(w)
    ref = m.group(1)
    intro = ("In the [[2009 Virtual Block Reorganization|2009 reorganisation]] the Committee regrouped these cards into the "
             "[[:Category:Virtual Legacy sets|Virtual Blocks]]." + ref)
    if table:
        intro += (" Some returned in the [[:Category:Current Virtual sets|Virtual Sets]] released after the 2014 Reset with the same "
                  "or revised game text.")
        new = intro + "\n\n=== Later printings ===\n" + table
    else:
        new = intro
    w = w[:m.start()] + new + w[m.end():]
    if '<div style="clear:both;"></div>\n== Cards ==' not in w:
        w = w.replace('\n== Cards ==', '\n<div style="clear:both;"></div>\n== Cards ==', 1)
    if '__TOC__' not in w:
        w = w.replace('\n<div style="clear:both;"></div>\n== Cards ==', '\n__TOC__\n<div style="clear:both;"></div>\n== Cards ==', 1)
    return w, rep


if __name__ == '__main__':
    os.makedirs('final', exist_ok=True)
    for n in sys.argv[1:]:
        w, rep = finalize(open(f'live/ovs{n}.wiki').read())
        open(f'final/ovs{n}.wiki', 'w').write(w)
        json.dump(rep, open(f'final/report{n}.json', 'w'), indent=1)
        print(n, 'rows', w.count('120px|link=') , 'modern candidates', len(rep))
