#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Tom H / Jellison / Kin."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[Tom H]]",
            "[[Ryan Jellison]]",
            "[[Stephen Kin]]",
            "Ralltiir Operations",
            "Watch Your Step (V)",
            "My Lord, Is That Legal?",
            "Local Uprising (V)",
            "A Stunning Move",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Tom H LS Watch Your Step (V)",
        (
            "[[Tom H]]",
            "Name as written on the Day 2 sheet.",
            "Watch Your Step (V)",
            "Luke Skywalker, Jedi Knight",
            "Romas 'Lock' Navander",
            "Mirax Terrik",
            "[[File:",
        ),
        ("'''Username:'''", "Tom Haid"),
    ),
    (
        "2013 Worlds Day 2 Tom H DS Ralltiir Operations",
        (
            "[[Tom H]]",
            "Name as written on the Day 2 sheet.",
            "Ralltiir Operations",
            "Executor: Meditation Chamber",
            "We'll Let Fate-a Decide, Huh?",
            "[[File:",
        ),
        ("'''Username:'''", "Tom Haid"),
    ),
    (
        "2013 Worlds Day 2 Ryan Jellison DS My Lord, Is That Legal?",
        (
            "[[Ryan Jellison]]",
            "'''Username:''' sac89837",
            "My Lord, Is That Legal?",
            "Accepting Trade Federation Control",
            "Astromech Shortage",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Ryan Jellison LS Local Uprising (V)",
        (
            "[[Ryan Jellison]]",
            "'''Username:''' sac89837",
            "Local Uprising (V)",
            "Republic Gunship Wing",
            "Were You Looking For Me?",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Stephen Kin DS A Stunning Move",
        (
            "[[Stephen Kin]]",
            "Name as written on the Day 2 sheet.",
            "A Stunning Move",
            "Galen, Secret Apprentice",
            "Grievous, Hunter Of Jedi",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Stephen Kin LS Watch Your Step (V)",
        (
            "[[Stephen Kin]]",
            "Name as written on the Day 2 sheet.",
            "Watch Your Step (V)",
            "Luke Skywalker, Jedi Knight",
            "Wesa Gotta Grand Army",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
]


def parse(title: str) -> str:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "wikitext|revid",
            "format": "json",
        }
    )
    with urllib.request.urlopen(f"{API}?{q}", timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    parse = data.get("parse") or {}
    return parse.get("wikitext", {}).get("*", "")


def flagged(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    with urllib.request.urlopen(f"{API}?{q}", timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    return next(iter(pages.values()), {})


def main() -> None:
    fails = 0
    for title, need, ban in CHECKS:
        text = parse(title)
        info = flagged(title)
        last = info.get("lastrevid")
        stable = (info.get("flagged") or {}).get("stable_revid")
        print(f"TITLE {title} last={last} stable={stable}")
        if not text:
            print("  FAIL empty")
            fails += 1
            continue
        if last and stable and last != stable:
            print(f"  FAIL flagged last={last} stable={stable}")
            fails += 1
        for n in need:
            if n not in text:
                print(f"  FAIL missing {n!r}")
                fails += 1
        for b in ban:
            if b in text:
                print(f"  FAIL unexpected {b!r}")
                fails += 1
        for d in DUMP:
            if d in text:
                print(f"  FAIL dest dump {d!r}")
                fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
