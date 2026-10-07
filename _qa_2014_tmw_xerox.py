#!/usr/bin/env python3
"""Live API QA for 2014 TMW leftover Xerox."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"

CHECKS = [
    (
        "2014 Texas Mini Worlds Day 1 Greg Shaw DS Separatist Uprising",
        "[[Separatist Uprising / At War With Itself]]",
    ),
    (
        "2014 Texas Mini Worlds Day 1 Greg Shaw LS It Is The Future You See (V)",
        "It Is The Future You See",
    ),
    ("2014 Texas Mini Worlds", "Greg Shaw"),
    ("Greg Shaw", "2014 Texas Mini Worlds Day 1 Greg Shaw DS Separatist Uprising"),
    ("2014 Texas Mini Worlds", "John Anderson"),
    ("2014 Texas Mini Worlds", "James Barnes"),
    ("2014 Texas Mini Worlds", "Mike Richards"),
    ("2014 Texas Mini Worlds", "Chris Schoenthal"),
    ("2014 Texas Mini Worlds", "Ganden Yanaga"),
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
        text = parse(title)
        latest, stable = flagged(title)
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
