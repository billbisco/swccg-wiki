#!/usr/bin/env python3
"""Live API QA for Tony G → Tony Garcia leftover."""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"

CHECKS = [
    ("Tony G", "#REDIRECT [[Tony Garcia]]"),
    ("Tony Garcia", "2013 Match Play Championship Day 1 Tony G"),
    ("Unknown players", "Tony Garcia"),
    ("2013 Match Play Championship", "[[Tony Garcia]]"),
    ("2013 Match Play Championship Day 1 Tony G LS Communing", "played by [[Tony Garcia]]"),
]


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
        print(f"{title!r} needle={ok_n} latest={latest} stable={stable} equal={ok_f}")
        if not ok_n or not ok_f:
            fails += 1
            if not ok_n:
                print("  missing", needle)
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
