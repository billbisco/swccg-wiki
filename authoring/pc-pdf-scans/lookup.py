#!/usr/bin/env python3
"""lookup.py "<text>" [LIGHT|DARK] -> top title matches from the GEMP card DB"""
import json, sys, difflib, re
DB = json.load(open("/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"))
q = sys.argv[1]; side = sys.argv[2].upper() if len(sys.argv) > 2 else None
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
titles = sorted({r["title"] for r in DB if not side or r.get("side") == side})
nq = norm(q)
sc = []
for t in titles:
    nt = norm(t)
    s = difflib.SequenceMatcher(None, nq, nt).ratio()
    if nq and nq in nt: s = max(s, 0.85 + 0.1 * len(nq) / max(len(nt), 1))
    sc.append((s, t))
for s, t in sorted(sc, reverse=True)[:8]:
    print(f"{s:.2f}  {t}")
