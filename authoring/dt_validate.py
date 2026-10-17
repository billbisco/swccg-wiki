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

def page_sides(titles):
    """title -> 'Light' / 'Dark' from the card page's side category (after redirects); titles without one are left out."""
    out = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        q = urllib.parse.urlencode({"action": "query", "titles": "|".join(titles[i:i+50]), "redirects": 1, "prop": "categories",
                                    "clcategories": "Category:Light|Category:Dark", "cllimit": "max", "format": "json", "formatversion": 2})
        r = json.load(urllib.request.urlopen(urllib.request.Request(db.API + "?" + q, headers=db.UA), timeout=60))
        back = {}
        for x in r["query"].get("normalized", []) + r["query"].get("redirects", []):
            back[x["to"]] = back.get(x["from"], x["from"])
        for p in r["query"]["pages"]:
            cats = {c["title"][9:] for c in p.get("categories", [])}
            if len(cats) == 1:
                out[back.get(p["title"], p["title"])] = cats.pop()
    return out


DISAMBIG_OK = {"Sense", "Alter", "Control"}  # kept plain on purpose unless the post says Type II (batch 27 ruling)


def disambiguation_pages(titles):
    """Titles (after redirects) that are in Category:Disambiguation — a card row must link a card page, not one of these."""
    out = set()
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        q = urllib.parse.urlencode({"action": "query", "titles": "|".join(titles[i:i+50]), "redirects": 1, "prop": "categories",
                                    "clcategories": "Category:Disambiguation", "format": "json", "formatversion": 2})
        r = json.load(urllib.request.urlopen(urllib.request.Request(db.API + "?" + q, headers=db.UA), timeout=60))
        back = {x["to"]: x["from"] for x in r["query"].get("normalized", []) + r["query"].get("redirects", [])}
        for p in r["query"]["pages"]:
            if p.get("categories"):
                t = p["title"]
                out.add(back.get(back.get(t, t), back.get(t, t)))
    return out


for pid in sys.argv[1:]:
    d = json.loads((db.DECKS / f"{pid}.json").read_text(encoding="utf-8"))
    side = d["side"]; c = db.canon()
    sidecards = {t for k, ts in c.items() if k.startswith(side + "|") for t in ts}
    other = {t for k, ts in c.items() if not k.startswith(side + "|") for t in ts}
    probs = []; maybe = []
    rows = d["cards"] + d.get("shields", [])
    for row in rows:
        q, t = row[0], row[1]
        if t.startswith("??"):
            probs.append(f"UNRESOLVED {t}")
        elif re.search(r"\(Virtual Set \d+(: [^)]+)?\)$", t) or t in db.gd.ORIGINAL_VS:
            pass
        elif t not in sidecards:
            maybe.append(t)
    other_side = "Light" if side == "Dark" else "Dark"
    for t, s2 in sorted(page_sides([r[1] for r in rows if not r[1].startswith(("??", "UNKNOWN"))]).items()):
        if s2 == other_side:  # the linked wiki page is the other side's card (e.g. Light Audience Chamber in a Dark deck)
            probs.append(f"WRONG SIDE PAGE: {t} is a {other_side} card page")
    for t in sorted(disambiguation_pages([r[1] for r in rows if not r[1].startswith(("??", "UNKNOWN"))]) - DISAMBIG_OK):
        probs.append(f"DISAMBIGUATION PAGE (pick the printing): {t}")
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
