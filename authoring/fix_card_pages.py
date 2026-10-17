"""Fix DeckTech deck rows that link a wrong-side card page or a disambiguation page (2026-10-17).

  python3 fix_card_pages.py [--apply] ID...

For each such row, candidates are wiki pages titled "<title> (Side)", "<title> (Side) (<set>)" or "<title> (<set>)"
(found by prefix search) whose side category is the deck's side and that are not disambiguation pages. Exactly one
candidate → swap it. More than one → era/format rule for generic sites (Premiere printing of systems; the Coruscant
printing in Episode I decks) when it picks one; otherwise listed for a person.
"""
import json, re, sys, urllib.parse, urllib.request
import decktech_batch as db
from dt_validate import page_sides, disambiguation_pages

def api(**k):
    k.update(format="json", formatversion=2)
    return json.load(urllib.request.urlopen(urllib.request.Request(db.API + "?" + urllib.parse.urlencode(k), headers=db.UA), timeout=60))

_cand = {}
def candidates(title, side):
    key = (title, side)
    if key in _cand:
        return _cand[key]
    r = api(action="query", list="prefixsearch", pssearch=title + " (", pslimit=50)
    titles = [p["title"] for p in r["query"]["prefixsearch"] if re.fullmatch(re.escape(title) + r"( \([^()]+\))+", p["title"])]
    sides = page_sides(titles) if titles else {}
    dis = disambiguation_pages(titles) if titles else set()
    out = [t for t in titles if sides.get(t) == side and t not in dis]
    _cand[key] = out
    return out

def pick(title, side, fmt, cands):
    if len(cands) == 1:
        return cands[0]
    ep1 = fmt == "Episode I Closed Environment"
    pref = [f"{title} ({side}) (Coruscant)"] if ep1 else []
    pref += [f"{title} ({side}) (Premiere)", f"{title} ({side})", f"{title} ({side}) (Special Edition)"]
    for p in pref:
        if p in cands:
            return p
    return None

def main(argv):
    apply = "--apply" in argv
    ids = [a for a in argv if a.isdigit()]
    manual = []
    changed = []
    for pid in ids:
        p = db.DECKS / f"{pid}.json"
        raw = p.read_text(encoding="utf-8")
        d = json.loads(raw)
        side = d["side"]; other = "Light" if side == "Dark" else "Dark"
        rows = d["cards"] + d.get("shields", [])
        titles = [r[1] for r in rows if not r[1].startswith(("??", "UNKNOWN")) and "(Virtual Set" not in r[1]]
        sides = page_sides(titles)
        dis = disambiguation_pages(titles) - {"Sense", "Alter", "Control"}
        bad = {t for t in titles if sides.get(t) == other} | dis
        swaps = {}
        for t in sorted(bad):
            new = pick(t, side, d.get("format"), candidates(t, side))
            if new:
                swaps[t] = new
            else:
                manual.append((pid, t, candidates(t, side)))
        if not swaps:
            continue
        for r in rows:
            if r[1] in swaps:
                r[1] = swaps[r[1]]
        st = d.get("starting") or {}
        for k, v in list(st.items()):
            if v in swaps:
                st[k] = swaps[v]
        changed.append((pid, swaps))
        if apply:
            ind = 1 if raw.startswith('{\n "') else 2
            p.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")
    for pid, s in changed:
        print("FIX", pid, "; ".join(f"{a} -> {b}" for a, b in s.items()))
    for pid, t, c in manual:
        print("MANUAL", pid, t, c[:6])
    print("decks changed", len(changed), "manual rows", len(manual))

if __name__ == "__main__":
    main(sys.argv[1:])
