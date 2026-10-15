#!/usr/bin/env python3
"""Collect transcribed PDF decks (out/<group>/*.json) into a decks list for canon.py / gen_pc_decks.py.

python3 assemble.py <out_root> <decks.json>
Each deck gets cards/shields aggregated from the sheet lines (blank cards left out of cards, kept in lines),
plus `verified` = every line identified and no UNSURE note (phase 4 grouped + GEMP); otherwise the page is
published as the sheet's numbered list (phases 1-3).
"""
import glob, json, os, sys
from collections import OrderedDict

root, outp = sys.argv[1], sys.argv[2]
DB = json.load(open("/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"))
VT = {r["title"].lower() + " (v)" for r in DB if r.get("hasVirtualSuffix")}
import re
decks, seen = [], set()
for f in sorted(glob.glob(os.path.join(root, "*", "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    if d["title"] in seen:
        print("DUP", d["title"], f); continue
    seen.add(d["title"])

    for l in d["lines"] + d["shields"]:
        c = (l.get("card") or "").strip()
        if not c and re.match(r"^\s*golden\s*rod\s*$", l.get("text") or "", re.I):
            l["card"] = c = "Goldenrod"
        if l.get("v") and c and " / " not in c and f"{c.lower()} (v)" not in VT and not c.endswith("(V)"):
            l["v"] = False  # (V) box ticked on a card with no (V) version
    def agg(lines):
        acc = OrderedDict()
        for l in lines:
            c = (l.get("card") or "").strip()
            if not c:
                continue
            k = (c, bool(l.get("v")))
            acc[k] = acc.get(k, 0) + 1
        return [[q, c, v] for (c, v), q in acc.items()]

    blanks = sum(1 for l in d["lines"] + d["shields"] if not (l.get("card") or "").strip())
    unsure = [n for n in d.get("notes", []) if n.upper().startswith(("UNSURE", "ILLEGIBLE", "INCOMPLETE"))]
    d2 = dict(title=d["title"], player=d["player"], side=d["side"], event=d["event"], stage=d.get("stage") or "Day 1",
              format_link="[[Open]]", start=d.get("start", ""), cards=agg(d["lines"]), shields=agg(d["shields"]),
              lines=d["lines"], shield_lines=d["shields"], pdf=d["pdf"], page=d["page"],
              pages=d.get("pages") or [d["page"]], username=d.get("username", ""), notes=d.get("notes", []),
              verified=(blanks == 0 and not unsure), group=os.path.basename(os.path.dirname(f)))
    decks.append(d2)
json.dump(decks, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(decks), "decks;", sum(d["verified"] for d in decks), "fully identified;",
      sum(1 for d in decks if sum(c[0] for c in d["cards"]) != 60), "not 60")
