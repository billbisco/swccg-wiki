import json, re, sys, collections
sys.path.insert(0, '/tmp/claude-0/ltm/build')
import build2 as B, resolve as R
todo = json.load(open('/tmp/claude-0/ltm/todo.json'))
G = json.load(open('/tmp/claude-0/ltm/dupgroups.json'))
grp = {t: [x for x, _ in g if x != t] for g in G for t, _ in g}
def get(titles):
    out = {}
    for i in range(0, len(titles), 40):
        r = R.q(action='query', titles='|'.join(titles[i:i+40]), prop='revisions', rvprop='content|ids', rvslots='main')
        for p in r['query']['pages']:
            out[p['title']] = (p['revisions'][0]['slots']['main']['content'], p['revisions'][0]['revid']) if 'revisions' in p else (None, None)
    return out
MOVES = {
 "2008 Worlds Day 2 Brian Fried DS Endor Operations": ("2008 Worlds Day 2 Brian Fried DS ISB Operations", "Line 1 on the sheet is ISB (ISB Operations), not Endor Operations", ("Endor Operations", "ISB Operations")),
 "2008 Worlds Day 2 Jim Li DS Agents In The Court": ("2008 Worlds Day 2 Jim Li DS Agents Of Black Sun", "The sheet's objective is Agents (Of Black Sun): Black Sun cards, Dark Side", ("Agents In The Court", "Agents Of Black Sun")),
 "2008 Worlds Day 2 Michael P. Stone LS We Have A Plan": ("2008 Worlds Day 2 Michael Pistone LS We Have A Plan", "Player is Michael Pistone (signed \"Michael P.Stone\"; his Dark Side sheet is under Michael Pistone)", None),
 "2008 Worlds Day 2 Chris Wirs LS It Is The Future You See": ("2008 Worlds Day 2 Chris Wirfs LS It Is The Future You See", "Player name on the sheet: Chris Wirfs", None),
}
PERSON_FIX = {"[[Michael P. Stone]]": "[[Michael Pistone]]", "[[Chris Wirs]]": "[[Chris Wirfs]]"}
REDIRS = {
 "2013 Worlds Day 2 Charles Arlandson LS Quiet Mining Colony": "2013 Worlds Day 2 Charlie Arlandson LS Quiet Mining Colony",
 "2013 Worlds Day 2 Charles Arlandson DS No Money, No Parts, No Deal!": "2013 Worlds Day 2 Charlie Arlandson DS No Money, No Parts, No Deal!",
 "2014 Match Play Championship Day 1 Stephen Skilton LS Plead My Case To The Senate": "2014 Match Play Championship Day 1 Steve Skilton LS Plead My Case To The Senate",
}
ops, talks = [], {}
cur = get([t for t, _ in todo])
SIG = " ~~~~"
for t, f in todo:
    s, rv = cur[t]
    if s is None: print("MISSING", t); continue
    tx = json.load(open('/tmp/claude-0/ltm/tx/' + f.replace(' ', '_')[:-4] + '.json'))
    side = tx['header']['side'] if tx['header']['side'] in ('Light', 'Dark') else ('Light' if ' LS ' in t else 'Dark')
    tbl, first, unres, total = B.build(tx, side, '2008-10-11')
    i = s.index("== Decklist ==") + len("== Decklist ==")
    j = s.index("== Scan ==")
    new = s[:i] + "\n\n" + tbl + "\n\n" + s[j:]
    m = re.search(r"\n'''Objective'''\n\* (\[\[[^\]]+\]\])", tbl)
    if m: new = re.sub(r"(\* '''Starting Card:''' )[^\n]*", lambda mm: mm.group(1) + m.group(1), new, count=1)
    title = t
    if t in MOVES:
        nt, why, lab = MOVES[t]
        new = new.replace(f"'''{t}'''", f"'''{nt}'''")
        for a, b in PERSON_FIX.items(): new = new.replace(a, b)
        ops.append(dict(kind='move', frm=t, to=nt, reason=why)); title = nt
    ops.append(dict(kind='edit', title=title, text=new, baserev=None if t in MOVES else rv,
                    summary="Decklist transcribed from this page's own scanned sheet (the old list was copied from another player's page); era-correct shield printings"))
    dt = (tx['header'].get('deck_title') or '').strip()
    others = [o for o in grp.get(t, []) if o.startswith('2008')]
    msg = TALKH = "== Decklist checked against the scan (2026-10-16) ==\n"
    body = f"The list is now transcribed from the sheet in the Scan section. Before, it was identical to " + \
           ", ".join(f"[[{MOVES.get(o, (o,))[0]}]]" for o in others) + ", so at least one of them was a copy."
    if dt: body += f" Deck title on the sheet: ''{dt}''."
    if t in MOVES: body += f" Page moved from [[{t}]]: {MOVES[t][1]}."
    if unres: body += " Lines not matched to a card, listed as written under ''Not identified'': " + ", ".join(sorted(set(u.strip() for u in unres))) + "."
    body += " Shields marked V link the 2006 [[Virtual Set: Defensive Shields]] printing or the Original Virtual Set printing legal in October 2008."
    talks["Talk:" + title] = TALKH + body + SIG + "\n"
EXTRA = {"2008 Worlds Day 2 Chris Wirs DS Hunt Down And Destroy The Jedi": "2008 Worlds Day 2 Chris Wirfs DS Hunt Down And Destroy The Jedi",
         "2008 Worlds Team Chris Wirs LS Watch Your Step": "2008 Worlds Team Chris Wirfs LS Watch Your Step"}
ex = get(list(EXTRA))
for old, nt in EXTRA.items():
    s0, rv = ex[old]
    n0 = s0.replace(f"'''{old}'''", f"'''{nt}'''").replace("[[Chris Wirs]]", "[[Chris Wirfs]]")
    ops.append(dict(kind='move', frm=old, to=nt, reason="Player name: Chris Wirfs (as written on his 2008 Day 2 Light Side sheet)"))
    ops.append(dict(kind='edit', title=nt, text=n0, baserev=None, summary="Player name: Chris Wirfs"))
    MOVES[old] = (nt, "Player name: Chris Wirfs", None)
# link fixes on pages that point at moved titles
bl = collections.defaultdict(set)
for old in list(MOVES) + list(REDIRS):
    for b in R.q(action='query', list='backlinks', bltitle=old, bllimit=200, blnamespace=0)['query']['backlinks']:
        bl[b['title']].add(old)
moved_new = {v[0] for v in MOVES.values()}
cur2 = get(sorted(t for t in bl if t not in MOVES and t not in REDIRS and t not in moved_new))
for p, olds in bl.items():
    if p not in cur2 or cur2[p][0] is None: continue
    s, rv = cur2[p]; n = s
    for old in olds:
        if old in MOVES:
            nt, _, lab = MOVES[old]
            if lab: n = n.replace(f"[[{old}|{lab[0]}]]", f"[[{nt}|{lab[1]}]]")
            n = n.replace(f"[[{old}|", f"[[{nt}|").replace(f"[[{old}]]", f"[[{nt}]]")
        else:
            nt = REDIRS[old]
            if f"[[{nt}" in n:
                n = "\n".join(l for l in n.split("\n") if f"[[{old}" not in l)
            else:
                n = n.replace(f"[[{old}|", f"[[{nt}|").replace(f"[[{old}]]", f"[[{nt}]]")
    # drop exact duplicate table rows created by the redirects
    lines, seen, outl = n.split("\n"), set(), []
    for l in lines:
        key = re.sub(r"<ref[^>]*>[^<]*</ref>|<ref[^>]*/>", "", l).replace(" ", "")
        if l.startswith("| ") and "[[20" in l and key in seen: continue
        seen.add(key); outl.append(l)
    n = "\n".join(outl)
    while "\n|-\n|-\n" in n: n = n.replace("\n|-\n|-\n", "\n|-\n")
    if n != s: ops.append(dict(kind='edit', title=p, text=n, baserev=rv, summary="Links: decklist pages renamed or merged after checking the scans"))
for old, new in REDIRS.items():
    ops.append(dict(kind='edit', title=old, text=f"#REDIRECT [[{new}]]\n", baserev=None,
                    summary=f"Duplicate of [[{new}]] (same scanned sheet, other spelling of the player's name)"))
json.dump(dict(ops=ops, talks=talks), open('/tmp/claude-0/ltm/build/payload2.json', 'w'), ensure_ascii=False, indent=0)
print(len(ops), "ops", len(talks), "talks")
for o in ops:
    if o['kind'] == 'move' or not o['title'].startswith('2008 Worlds'): print(o['kind'], o.get('title') or o.get('frm'))
