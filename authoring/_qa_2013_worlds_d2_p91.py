#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Matt Sokol."""
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
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[Matt Sokol]]",
            "[[RSmith]]",
            "Walker Garrison (V)",
            "You Can Either Profit By This...",
            "2013 Worlds Day 2 Matt Sokol",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Matt Sokol LS You Can Either Profit By This...",
        (
            "[[Matt Sokol]]",
            "Name as written on the Day 2 sheet.",
            "You Can Either Profit By This... / Or Be Destroyed",
            "[[IL-19]]",
            "Jabba's Prize",
            "GHTM & BP",
            "Don't Forget The Droids",
            "[[File:2013 Worlds Day 2 p92 Matt Sokol LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Matt Sokol DS Walker Garrison (V)",
        (
            "[[Matt Sokol]]",
            "Walker Garrison (V)",
            "Cyclone Walker",
            "You May Start Your Landing",
            "We're In Attack Position Now",
            "[[File:2013 Worlds Day 2 p91 Matt Sokol DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "Matt Sokol",
        (
            "2013 World Championship",
            "Walker Garrison (V)",
            "You Can Either Profit By This...",
        ),
        (),
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
