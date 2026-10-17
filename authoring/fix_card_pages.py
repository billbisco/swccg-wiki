"""Fix DeckTech deck rows that link a wrong-side card page or a disambiguation page (2026-10-17).

  python3 fix_card_pages.py [--apply] ID...

For each such row, candidates are wiki pages titled "<title> (Side)", "<title> (Side) (<set>)" or "<title> (<set>)"
(found by prefix search) whose side category is the deck's side and that are not disambiguation pages. Exactly one
candidate → swap it. More than one → era/format rule for generic sites (Premiere printing of systems; the Coruscant
printing in Episode I decks) when it picks one; otherwise listed for a person.
"""
import json, re, sys, urllib.parse, urllib.request
import decktech_batch as db
import regen_gemp_from_wiki as R
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
    # follow redirects ("Tatooine (Dark)" -> "Tatooine (Dark) (Premiere)") so a redirect and its target count once
    res = {}
    if out:
        q = api(action="query", titles="|".join(out), redirects=1)["query"]
        red = {r["from"]: r["to"] for r in q.get("redirects", [])}
        res = {t: red.get(t, t) for t in out}
    final = sorted(set(res.values()))
    _alias[key] = res
    _cand[key] = final
    return final

_alias = {}
def is_location(t):
    x = R.page_texts([t]).get(t, "")
    m = re.match(r"#REDIRECT\s*\[\[([^\]|#]+)", x, re.I)
    if m:
        x = R.page_texts([m.group(1).strip()]).get(m.group(1).strip(), "")
    return "|type=Location" in x

FACE = re.compile(r" \((?:Original|PC Errata|Errata)\)$")

def pick(title, side, fmt, cands):
    # a printed-era list means the printed card: drop Virtual (V) pages unless the posted title is a (V);
    # drop the Original / PC Errata face pages when the default page for the card is a candidate
    if "(V)" not in title:
        cands = [c for c in cands if "(V)" not in c]
    cands = [c for c in cands if not (FACE.search(c) and FACE.sub("", c) in cands)]
    if len(cands) == 1:
        return cands[0]
    same_card = all(c.startswith(f"{title} ({side})") or c == f"{title} (Coruscant)" for c in cands)
    if not cands or not (same_card or all(is_location(c) for c in cands)):
        return None  # only reprints of one card are picked by era; other cards need a person
    alias = _alias.get((title, side), {})
    ep1 = fmt == "Episode I Closed Environment"
    pref = [f"{title} ({side}) (Coruscant)"] if ep1 else []
    pref += [f"{title} ({side}) (Premiere)", f"{title} ({side})", f"{title} ({side}) (Special Edition)"]
    for p in pref:
        p = alias.get(p, p)
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
            base = re.sub(r" \([^()]+\)$", "", t)
            if not new and base != t:
                if page_sides([base]).get(base) == side and base not in disambiguation_pages([base]):
                    new = base
                else:
                    new = pick(base, side, d.get("format"), candidates(base, side))
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
