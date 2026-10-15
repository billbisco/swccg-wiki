#!/usr/bin/env python3
"""check.py <out/group dir> -> per deck: line count, empty cards, titles not in GEMP DB"""
import json, sys, glob, os, re
DB = json.load(open("/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"))
T = {}
for r in DB: T.setdefault(r["title"].lower(), set()).add(r.get("side"))
for f in sorted(glob.glob(os.path.join(sys.argv[1], "*.json"))):
    d = json.load(open(f)); sd = "DARK" if d["side"] == "DS" else "LIGHT"
    unk = [l["card"] for l in d["lines"] + d["shields"] if l["card"] and l["card"].lower() not in T
           and l["card"].split(" / ")[0].lower() not in T]
    wrong = [l["card"] for l in d["lines"] if l["card"].lower() in T and sd not in T[l["card"].lower()]]
    blank = sum(1 for l in d["lines"] if not l["card"])
    ns = [l["n"] for l in d["lines"]]
    print(f"{os.path.basename(f)}: lines {len(d['lines'])} shields {len(d['shields'])} blank {blank}"
          + (f" | not-in-GEMP {unk}" if unk else "") + (f" | other-side {wrong}" if wrong else "")
          + (" | numbering gaps" if ns != list(range(1, len(ns) + 1)) else ""))
