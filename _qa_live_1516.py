#!/usr/bin/env python3
from __future__ import annotations

import re
import urllib.request

UA = {"User-Agent": "swccg-wiki-historian/1.0"}


def html(title: str) -> str:
    url = "https://wiki.swccg.com/index.php?title=" + title.replace(" ", "_")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


issues: list[str] = []
lst = html("List_of_SWCCG_tournaments")
years = re.findall(r'id="(\d{4}|Decipher_World_Championships)"', lst)
print("headings", years)
need = ["2026", "2018", "2017", "2016", "2015", "Decipher_World_Championships"]
pos = [years.index(y) if y in years else -1 for y in need]
print("pos", list(zip(need, pos)))
if not (pos[1] < pos[2] < pos[3] < pos[4] < pos[5]):
    issues.append(f"year order {pos}")
if re.search(r"<th[^>]*>Wiki</th>", lst):
    issues.append("Wiki column")
if "Ziemowit Skwara" not in lst:
    issues.append("list missing Skwara")
if "Steve Baroni" not in lst:
    issues.append("list missing Baroni")

ks = html("Kevin_Shannon")
if "<table" not in ks:
    issues.append("shannon no table")
if "San Diego Grand Prix" not in ks:
    issues.append("shannon no sdgp")
if "pending changes" in ks.lower() and "stable version" in ks.lower():
    issues.append("shannon pending")

egp = html("2016_Endor_Grand_Prix")
if "Brian Fred" not in egp:
    issues.append("egp missing Fred")
if "Joe Olson" not in egp:
    issues.append("egp missing Olson")

mpc = html("2015_Match_Play_Championship")
if "Kevin Shannon" not in mpc or "Reid Smith" not in mpc:
    issues.append("mpc day2 names")

w15 = html("2015_World_Championship")
if "Joe Olson" not in w15 or "Justin Desai" not in w15:
    issues.append("15worlds names")
if "pending changes" in w15.lower() and "This is a pending" in w15:
    issues.append("15worlds pending")

print("n_issues", len(issues))
for x in issues:
    print(x)
