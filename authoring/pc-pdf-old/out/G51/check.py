#!/usr/bin/env python3
import json, glob, os, sys, urllib.request, urllib.parse
OUT = os.path.dirname(os.path.abspath(__file__))
DB = json.load(open("/home/claude/billbisco/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"))
by = {}
for r in DB: by.setdefault(r["title"], set()).add(r.get("side"))
miss = {}
for f in sorted(glob.glob(OUT + "/*.json")):
    d = json.load(open(f)); side = "DARK" if d["side"] == "DS" else "LIGHT"
    for x in d["lines"] + d["shields"] + [{"card": d["start"]}]:
        c = x["card"]
        if not c: continue
        for part in c.split(" / "):
            s = by.get(part)
            if s is None or side not in s:
                miss.setdefault(part, []).append((os.path.basename(f)[-8:], side, s))
wiki = {}
ts = list(miss)
for i in range(0, len(ts), 40):
    q = urllib.parse.urlencode({"action": "query", "titles": "|".join(ts[i:i+40]), "format": "json", "redirects": 1})
    r = json.load(urllib.request.urlopen("https://wiki.swccg.com/api.php?" + q))
    norm = {n["from"]: n["to"] for n in r["query"].get("normalized", [])}
    red = {n["from"]: n["to"] for n in r["query"].get("redirects", [])}
    pages = {p["title"]: ("missing" not in p) for p in r["query"]["pages"].values()}
    for t in ts[i:i+40]:
        t2 = norm.get(t, t); t3 = red.get(t2, t2)
        wiki[t] = (pages.get(t3), t3 if t3 != t else "")
for k, v in miss.items():
    print(k, v[:2], "WIKI:", wiki.get(k))
