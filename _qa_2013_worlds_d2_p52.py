#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Kinser / Koswicki."""
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
            "[[Aaron Kinser]]",
            "[[Jack Koswicki]]",
            "Imperial Occupation (V)",
            "The Hyperdrive Generator's Gone",
            "Endor Operations",
            "There Is Good In Him",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Aaron Kinser DS Imperial Occupation (V)",
        (
            "[[Aaron Kinser]]",
            "Imperial Occupation (V)",
            "The Mandalorian (V)",
            "Black Leader (V)",
            "Anger, Fear, Aggression & Struggle Of The Throne",
            "Leave Them To Me (V)",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Aaron Kinser LS The Hyperdrive Generator's Gone",
        (
            "[[Aaron Kinser]]",
            "The Hyperdrive Generator's Gone",
            "Republic Gunship Wing",
            "Master Qui-Gon (V)",
            "Crush Of The Saber",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Jack Koswicki DS Endor Operations",
        (
            "[[Jack Koswicki]]",
            "Name as written on the Day 2 sheet.",
            "Endor Operations",
            "Establish Control",
            "The Emperor's Shield",
            "Forgot Ops",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Jack Koswicki LS There Is Good In Him",
        (
            "[[Jack Koswicki]]",
            "Name as written on the Day 2 sheet.",
            "There Is Good In Him",
            "Han Solo, Innocent Scoundrel",
            "11-4D",
            "Nocoo!",
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
