#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Micah Wall."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
    "Handwritten 2013 Xerox Print Form",
    "Typed 2013 Xerox Print Form",
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[Micah Wall]]",
            "[[John Veasey]]",
            "2013 Worlds Day 2 Micah Wall",
            "Imperial Occupation",
            "You Can Either Profit By This...",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Micah Wall LS You Can Either Profit By This...",
        (
            "[[Micah Wall]]",
            "You Can Either Profit By This... / Or Be Destroyed",
            "Skywalker Avenger",
            "Ben Kenobi",
            "[[File:2013 Worlds Day 2 p102 Micah Wall LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Micah Wall DS Imperial Occupation",
        (
            "[[Micah Wall]]",
            "Imperial Occupation / Imperial Control",
            "Marquand In Blizzard 6",
            "He Hasn't Come Back Yet",
            "BP, DH",
            "[[File:2013 Worlds Day 2 p101 Micah Wall DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "Micah Wall",
        (
            "2013 World Championship",
            "Imperial Occupation",
            "You Can Either Profit By This...",
            "2013 Match Play Championship",
        ),
        ("#REDIRECT",),
    ),
]


def raw(title: str) -> str:
    q = urllib.parse.urlencode(
        {"action": "parse", "page": title, "prop": "wikitext", "format": "json"}
    )
    with urllib.request.urlopen(f"{API}?{q}", timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data.get("parse", {}).get("wikitext", {}).get("*", "") or ""


def main() -> None:
    fails = 0
    for title, need, forbid in CHECKS:
        text = raw(title)
        print("PAGE", title, "len", len(text))
        if not text:
            print("  FAIL empty")
            fails += 1
            continue
        for s in need:
            if s not in text:
                print("  FAIL missing", s)
                fails += 1
        for s in forbid:
            if s in text:
                print("  FAIL forbidden", s)
                fails += 1
        for s in DUMP:
            if s in text:
                print("  FAIL dump", s)
                fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
