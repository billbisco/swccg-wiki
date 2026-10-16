#!/usr/bin/env python3
"""Check a finished decktech-decks/<id>.json: card titles exist for the deck's side, qty total, leftovers.

    python3 dt_validate.py 20570 [20562 ...]
"""
import json, re, sys, urllib.parse, urllib.request
from pathlib import Path
import decktech_batch as db

def wiki_pages(titles):
    out = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        q = urllib.parse.urlencode({"action": "query", "titles": "|".join(titles[i:i+50]), "redirects": 1, "format": "json", "formatversion": 2})
        r = json.load(urllib.request.urlopen(urllib.request.Request(db.API + "?" + q, headers=db.UA), timeout=60))
        miss = {p["title"] for p in r["query"]["pages"] if p.get("missing")}
        norm = {x["from"]: x["to"] for x in r["query"].get("normalized", [])}
        for t in titles[i:i+50]:
            out[t] = norm.get(t, t) not in miss
    return out

for pid in sys.argv[1:]:
    d = json.loads((db.DECKS / f"{pid}.json").read_text(encoding="utf-8"))
    side = d["side"]; c = db.canon()
    sidecards = {t for k, ts in c.items() if k.startswith(side + "|") for t in ts}
    other = {t for k, ts in c.items() if not k.startswith(side + "|") for t in ts}
    probs = []; maybe = []
    rows = d["cards"] + d.get("shields", [])
    for q, t, kind, note in rows:
        if t.startswith("??"):
            probs.append(f"UNRESOLVED {t}")
        elif re.search(r"\(Virtual Set \d+(: [^)]+)?\)$", t) or t in db.gd.ORIGINAL_VS:
            pass
        elif t not in sidecards:
            maybe.append(t)
    if maybe:
        ex = wiki_pages(maybe)
        for t in maybe:
            if not ex[t]:
                probs.append(f"NO WIKI PAGE and not a {side} GEMP title: {t}" + (" (title exists on other side)" if t in other else ""))
    tot = sum(r[0] for r in d["cards"])
    st = d.get("starting") or {}
    for k in ("card", "interrupt", "effect"):
        if st.get(k) and st[k] not in {r[1] for r in d["cards"]}:
            probs.append(f"starting.{k} not in cards: {st[k]}")
    if d.get("player_page") in ("existing", "new") and d.get("player"):
        ex = wiki_pages([d["player"]])[d["player"]]
        if ex and d["player_page"] == "new": probs.append(f"player page EXISTS on wiki but player_page=new: {d['player']}")
        if not ex and d["player_page"] == "existing": probs.append(f"player page MISSING but player_page=existing: {d['player']}")
    print(f"{pid}: {d['side']} total {tot} (+{sum(r[0] for r in d.get('shields', []))} shields) " + ("OK" if not probs else ""))
    for p in probs: print("   -", p)
