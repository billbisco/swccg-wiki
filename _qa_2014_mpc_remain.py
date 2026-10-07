#!/usr/bin/env python3
"""Live API QA for remaining 2014 MPC Xerox dests applied this turn."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    ("2014 Match Play Championship Day 2 Stephen Cellucci DS Agents Of Black Sun", "Agents Of Black Sun"),
    ("2014 Match Play Championship Day 2 Stephen Cellucci LS It Is The Future You See (V)", "Same as Day 1"),
    ("2014 Match Play Championship Day 2 Matthew Harrison-Trainor DS Ralltiir Operations", "Ralltiir Operations"),
    ("2014 Match Play Championship Day 2 Matthew Harrison-Trainor LS Watch Your Step (V)", "Watch Your Step"),
    ("2014 Match Play Championship Consolation Tim Simon LS It Is The Future You See (V)", "It Is The Future You See"),
    ("2014 Match Play Championship Day 1 Aaron Kingery DS Separatist Uprising", "Separatist Uprising"),
    ("2014 Match Play Championship Day 1 Aaron Kingery LS Yavin 4 (V)", "Yavin 4"),
    ("2014 Match Play Championship Day 1 Kyle Krueger DS Carbon Chamber Testing", "Carbon Chamber Testing"),
    ("2014 Match Play Championship Day 1 Kyle Krueger LS Communing", "Communing"),
    ("2014 Match Play Championship Day 1 Cole Lepine DS Wookiee Slaving Operation", "Wookiee Slaving Operation"),
    ("2014 Match Play Championship Day 1 Cole Lepine LS Quiet Mining Colony", "Quiet Mining Colony"),
    ("2014 Match Play Championship Day 1 Josh Mack DS Kessel", "Kessel"),
    ("2014 Match Play Championship", "Stephen Cellucci"),
    ("2014 Match Play Championship Day 2 Stephen Cellucci DS Agents Of Black Sun", "nolimit"),
    ("2014 Match Play Championship Day 1 Kyle Krueger DS Carbon Chamber Testing", "Meto"),
    ("2014 Match Play Championship Day 1 Cole Lepine LS Quiet Mining Colony", "clepine"),
    ("2014 Match Play Championship Consolation Tim Simon LS It Is The Future You See (V)", "Aglets"),
]
DUMPS = (" dested ", "dittos inherit", "Handwritten 2010 Xerox", "Handwritten 2013 Xerox")


def parse(title: str) -> str:
    q = urllib.parse.urlencode(
        {"action": "parse", "page": title, "prop": "wikitext", "format": "json"}
    )
    with urllib.request.urlopen(API + "?" + q, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["parse"]["wikitext"]["*"]


def flagged(title: str) -> tuple[int, int]:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    with urllib.request.urlopen(API + "?" + q, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    page = next(iter(data["query"]["pages"].values()))
    latest = int(page.get("lastrevid") or 0)
    stable = int((page.get("flagged") or {}).get("stable_revid") or 0)
    return latest, stable


def main() -> None:
    fails = 0
    for title, needle in CHECKS:
        try:
            text = parse(title)
            latest, stable = flagged(title)
        except Exception as e:
            print(f"{title!r} ERROR {e}")
            fails += 1
            continue
        ok_n = needle in text
        ok_f = latest == stable and latest > 0
        dump = [d for d in DUMPS if d.lower() in text.lower()]
        print(
            f"{title!r} needle={ok_n} latest={latest} stable={stable} "
            f"equal={ok_f} dumps={dump}"
        )
        if not ok_n or not ok_f or dump:
            fails += 1
            if not ok_n:
                print("  missing", needle)
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
