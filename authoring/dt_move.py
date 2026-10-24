#!/usr/bin/env python3
"""Move wiki pages (with Talk) listed in a TSV: old<TAB>new[<TAB>noredirect]. Claude 2026-10-24.
   set -a; . ../wiki-bot-password.env; set +a; python3 dt_move.py moves.tsv "reason" """
import sys
from wiki_api_apply import Wiki

w = Wiki()
for line in open(sys.argv[1], encoding="utf-8"):
    p = line.rstrip("\n").split("\t")
    if len(p) < 2:
        continue
    q = dict(action="move", to=p[1], movetalk="1", reason=sys.argv[2], token=w.csrf)
    q["from"] = p[0]
    if len(p) > 2 and p[2] == "noredirect":
        q["noredirect"] = "1"
    d = w.post(**q)
    print(p[0], "->", p[1], d.get("error", {}).get("code") or ("ok" + (" (talk)" if d.get("move", {}).get("talkto") else "")))
