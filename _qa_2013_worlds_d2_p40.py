#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Haid / Harrison-Trainor / Herold."""
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
            "[[Tom Haid]]",
            "[[Matthew Harrison-Trainor]]",
            "[[Brian Herold]]",
            "You Can Either Profit By This...",
            "Wookiee Slaving Operation",
            "Watch Your Step (V)",
            "Imperial Occupation (V)",
            "Infiltration",
            "Hunt Down And Destroy The Jedi (V)",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Tom Haid LS You Can Either Profit By This...",
        (
            "[[Tom Haid]]",
            "'''Username:''' Xenth",
            "You Can Either Profit By This...",
            "Son Of Skywalker",
            "Wesa Gotta Grand Army",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Tom Haid DS Wookiee Slaving Operation",
        (
            "[[Tom Haid]]",
            "'''Username:''' Xenth",
            "Wookiee Slaving Operation",
            "Ability, Ability, Ability",
            "Ghhhk & Those Rebels Won't Escape Us",
            "[[File:",
        ),
        ("'''Creature'''",),
    ),
    (
        "2013 Worlds Day 2 Matthew Harrison-Trainor LS Watch Your Step (V)",
        (
            "[[Matthew Harrison-Trainor]]",
            "Watch Your Step (V)",
            "Evacuation Control",
            "Obi-Wan In Radiant VII",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Matthew Harrison-Trainor DS Imperial Occupation (V)",
        (
            "[[Matthew Harrison-Trainor]]",
            "Imperial Occupation (V)",
            "Hoth Blockade",
            "After Her!",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Brian Herold LS Infiltration",
        (
            "[[Brian Herold]]",
            "'''Username:''' Zero Cool",
            "Infiltration",
            "Kyle Katarn",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Brian Herold DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Brian Herold]]",
            "'''Username:''' Crash Override",
            "Hunt Down And Destroy The Jedi (V)",
            "Galen's Fighter",
            "[[File:",
        ),
        (),
    ),
    (
        "Tom Haid",
        ("2013 World Championship", "You Can Either Profit By This..."),
        (),
    ),
    (
        "Matthew Harrison-Trainor",
        ("2013 World Championship", "Watch Your Step (V)"),
        (),
    ),
    (
        "Brian Herold",
        ("2013 World Championship", "Infiltration"),
        (),
    ),
]


def parse(title: str) -> str:
    q = urllib.parse.urlencode(
        {"action": "parse", "page": title, "prop": "wikitext", "format": "json"}
    )
    with urllib.request.urlopen(f"{API}?{q}", timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data.get("parse", {}).get("wikitext", {}).get("*", "")


def main() -> None:
    fails = 0
    for title, need, ban in CHECKS:
        text = parse(title)
        oldid = ""
        q = urllib.parse.urlencode(
            {
                "action": "query",
                "titles": title,
                "prop": "info|flagged",
                "format": "json",
            }
        )
        with urllib.request.urlopen(f"{API}?{q}", timeout=60) as r:
            pages = json.loads(r.read().decode("utf-8"))["query"]["pages"]
        rec = next(iter(pages.values()))
        oldid = rec.get("lastrevid")
        flagged = rec.get("flagged") or {}
        stable = flagged.get("stable_revid")
        bad = []
        for n in need:
            if n not in text:
                bad.append(f"missing {n!r}")
        for b in ban:
            if b in text:
                bad.append(f"unexpected {b!r}")
        for d in DUMP:
            if d in text:
                bad.append(f"dest dump {d!r}")
        if bad:
            fails += 1
            print("FAIL", title, "oldid", oldid, "stable", stable, bad)
        else:
            print("OK", title, "oldid", oldid)
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
