#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Lepine / Lingrell / Littauer."""
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
            "[[Cole Lepine]]",
            "[[Scott Lingrell]]",
            "[[Ross Littauer]]",
            "Wookiee Slaving Operation",
            "Watch Your Step (V)",
            "Agents Of Black Sun",
            "You Can Either Profit By This...",
            "Hunt Down And Destroy The Jedi (V)",
            "Infiltration",
            "2013 Worlds Day 1 Ross Littauer",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Cole Lepine LS Watch Your Step (V)",
        (
            "[[Cole Lepine]]",
            "'''Username:''' clepines",
            "Watch Your Step (V)",
            "Relian (V)",
            "BoShek's Modified Light Freighter (V)",
            "Han's Toolkit (V)",
            "The Force Unleashed (V)",
            "[[File:2013 Worlds Day 2 p56 Cole Lepine LS.png",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Cole Lepine DS Wookiee Slaving Operation",
        (
            "[[Cole Lepine]]",
            "'''Username:''' clepine",
            "Wookiee Slaving Operation / Indentured To The Empire",
            "Kashyyyk: Security Tower",
            "Mercenary Slavers",
            "The Mandalorian (V)",
            "[[File:2013 Worlds Day 2 p57 Cole Lepine DS.png",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Scott Lingrell DS Agents Of Black Sun",
        (
            "[[Scott Lingrell]]",
            "Agents Of Black Sun / Vengeance Of The Dark Prince",
            "ComScan Detection (V)",
            "Sebulba's Podracer",
            "Trophy Of A Kill",
            "[[File:2013 Worlds Day 2 p58 Scott Lingrell DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Scott Lingrell LS You Can Either Profit By This...",
        (
            "[[Scott Lingrell]]",
            "Day 2 Light sheet has a blank name box. Listed here as Scott Lingrell",
            "You Can Either Profit By This... / Or Be Destroyed",
            "Captain Yutani With Blaster Cannon",
            "A Jedi's Concentration",
            "[[File:2013 Worlds Day 2 p59 Scott Lingrell LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Ross Littauer DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Ross Littauer]]",
            "Day 2 Dark is the same as the Day 1 Hunt Down list",
            "Hunt Down And Destroy The Jedi (V)",
            "Jango Fett",
            "Vader's Obsession",
            "[[File:2013 Worlds Day 2 p60 Ross Littauer DS.png",
            "[[File:2013 Worlds Day 1 p05 Ross Littauer DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Ross Littauer LS Infiltration",
        (
            "[[Ross Littauer]]",
            "Infiltration / Unlikely Allies",
            "Han's Blaster, So Uncivilized",
            "Mechanical Failure",
            "[[File:2013 Worlds Day 2 p61 Ross Littauer LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "Cole Lepine",
        (
            "2013 Worlds Day 2 Cole Lepine DS Wookiee Slaving Operation",
            "2013 Worlds Day 2 Cole Lepine LS Watch Your Step (V)",
        ),
        (),
    ),
    (
        "Scott Lingrell",
        (
            "2013 Worlds Day 2 Scott Lingrell DS Agents Of Black Sun",
            "2013 Worlds Day 2 Scott Lingrell LS You Can Either Profit By This...",
            "2013 Match Play Championship Day 1 Scott Lingrell",
        ),
        (),
    ),
    (
        "Ross Littauer",
        (
            "2013 Worlds Day 2 Ross Littauer DS Hunt Down And Destroy The Jedi (V)",
            "2013 Worlds Day 2 Ross Littauer LS Infiltration",
            "2013 Worlds Day 1 Ross Littauer DS Hunt Down And Destroy The Jedi (V)",
        ),
        (),
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
