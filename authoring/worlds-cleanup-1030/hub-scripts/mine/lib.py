import re, json, sys
sys.path.insert(0, '.')
from parse import sections, tables, links

EX = json.load(open('exists.json'))
INFO = json.load(open('info.json'))

AWARDS = ('[https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org. '
          'Preserved copy: [https://web.archive.org/web/20230817222457/https://www.starwarsccg.org/community/awards/ '
          'Internet Archive, 17 August 2023]; current page preserved at '
          '[https://swccg.com/snapshots/pc/community-awards.html swccg.com snapshot] (12 October 2026)')
WIKIPEDIA = ('[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], '
             'Wikipedia (World Championship table)')

ORD = {17: '22nd', 18: '23rd', 19: '24th', 20: '25th', 21: '26th', 22: '27th', 23: '28th', 24: '29th', 25: '30th', 26: '31st'}


def norm_player(cell):
    """Point player links at the canonical person page."""
    def fix(m):
        inner = m.group(1)
        tgt, _, disp = inner.partition('|')
        tgt = re.sub(r'\s+', ' ', tgt.strip())
        disp = disp.strip() or tgt
        canon = EX.get(tgt) or tgt
        if canon == tgt:
            return f'[[{tgt}|{disp}]]' if disp != tgt else f'[[{tgt}]]'
        if tgt.startswith(canon) or disp.startswith(canon):
            return f'[[{canon}]]'
        return f'[[{canon}|{disp}]]'
    return re.sub(r'\[\[([^\]]+)\]\]', fix, cell)


def norm_deck(cell):
    def fix(m):
        inner = m.group(1)
        tgt, _, disp = inner.partition('|')
        tgt = re.sub(r'\s+', ' ', tgt.strip())
        to = INFO.get(tgt, {}).get('to')
        if to:
            tgt = to
        return f'[[{tgt}|{disp.strip()}]]' if disp else f'[[{tgt}]]'
    return re.sub(r'\[\[([^\]]+)\]\]', fix, cell)


def get_tables(txt):
    out = {}
    for name, sec in sections(txt):
        for hdr, rows in tables(sec):
            out.setdefault(name, []).extend(rows)
    return out


def table(col0, rows, extra_hdr=None):
    h = f'! {col0} !! Player !! Dark !! Light'
    if extra_hdr:
        h += ' !! ' + extra_hdr
    s = ['{| class="wikitable sortable"', h]
    for r in rows:
        cells = [r[0], norm_player(r[1]), norm_deck(r[2]) if r[2] else '—', norm_deck(r[3]) if r[3] else '—'] + list(r[4:])
        s.append('|-')
        s.append('| ' + ' || '.join(cells))
    s.append('|}')
    return '\n'.join(s)


def infobox(y, photo, caption, dates, venue, fmt, players, champ, runner):
    yy = y % 100
    prev = f'[[{y-1} World Championship|{y-1}]]'
    nxt = f'[[{y+1} World Championship|{y+1}]]' if y < 2026 else '—'
    rows = ['{| class="wikitable expansion-infobox" style="float:right; margin:0 0 1em 1em; width:300px;"',
            f'! colspan="2" | {y} World Championship']
    if photo:
        rows += ['|-', f'| colspan="2" style="text-align:center;" | [[File:{photo}|280px]]<br/><small>{caption}</small>']
    for k, v in [('Edition', ORD[yy]), ('Organizer', '[[Players Committee]]'), ('Dates', dates), ('Venue', venue),
                 ('Format', fmt), ('Players', players), ('Champion', champ), ('Runner-up', runner),
                 ('Previous / Next', f'{prev} · {nxt}')]:
        if v:
            rows += ['|-', f'! {k}', f'| {v}']
    rows.append('|}')
    return '\n'.join(rows)


def resolve_refs(text, defs):
    """{{R|name}} -> full <ref> on first use, short form afterwards."""
    seen = set()
    def rep(m):
        n = m.group(1)
        if n in seen:
            return f'<ref name="{n}" />'
        seen.add(n)
        return f'<ref name="{n}">{defs[n]}</ref>'
    out = re.sub(r'\{\{R\|([^}]+)\}\}', rep, text)
    unused = set(defs) - seen
    return out, unused


def gallery(items):
    return '<gallery>\n' + '\n'.join(f'File:{f}|{c}' for f, c in items) + '\n</gallery>'


FOOT = '{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}'


def cats(y):
    return f'[[Category:Tournaments]]\n[[Category:Championships]]\n[[Category:World Championships]]\n[[Category:{y}]]'


def see_also(y, extra=()):
    s = ['* [[World Championships]]', f'* [[{y-1} World Championship]]']
    if y < 2026:
        s.append(f'* [[{y+1} World Championship]]')
    s.append('* [[Open]]')
    s += [f'* {e}' for e in extra]
    s.append('* [[List of SWCCG tournaments]]')
    return '\n'.join(s)


def check(y, text, deckset):
    linked = [norm_deck('[[' + l + ']]')[2:-2] for l in links(text)]
    from collections import Counter
    c = Counter(l for l in linked if l in deckset)
    dups = [k for k, v in c.items() if v > 1]
    missing = sorted(deckset - set(c))
    return len(c), dups, missing
