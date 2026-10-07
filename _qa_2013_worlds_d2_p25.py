#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Cellucci D2 / Consoli / Desai / Fred."""
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
            "[[Stephen Cellucci]]",
            "[[Angelo Consoli]]",
            "[[Justin Desai]]",
            "[[Brian Fred]]",
            "Endor Operations",
            "Plead My Case To The Senate",
            "Wookiee Slaving Operation",
            "You Can Either Profit By This",
            "Imperial Occupation (V)",
            "Watch Your Step",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Stephen Cellucci DS Endor Operations",
        (
            "[[Stephen Cellucci]]",
            "'''Username:''' Nolimit",
            "Endor Operations",
            "Corporal Misik",
            "[[File:",
        ),
        ("Corporal Midge",),
    ),
    (
        "2013 Worlds Day 2 Stephen Cellucci LS Plead My Case To The Senate",
        (
            "[[Stephen Cellucci]]",
            "'''Username:''' Nolimit",
            "Day 2 Light is the same as the Day 1 Plead My Case To The Senate list.",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Angelo Consoli DS Wookiee Slaving Operation",
        (
            "[[Angelo Consoli]]",
            "'''Username:''' Gravityslada",
            "Wookiee Slaving Operation",
            "Turn It Off! Turn It Off!",
            "We'll Let Fate-A Decide, Huh?",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Angelo Consoli LS You Can Either Profit By This...",
        (
            "[[Angelo Consoli]]",
            "'''Username:''' Gravityslada",
            "You Can Either Profit By This",
            "Han (V)",
            "[[File:",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Justin Desai DS Imperial Occupation (V)",
        (
            "[[Justin Desai]]",
            "Imperial Occupation (V)",
            "Imperial Control (V)",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Brian Fred DS Endor Operations",
        ("[[Brian Fred]]", "Endor Operations", "[[File:"),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Brian Fred LS Watch Your Step",
        (
            "[[Brian Fred]]",
            "Watch Your Step",
            "Palace Raider",
            "Boshek's Modified Light Freighter",
            "[[File:",
        ),
        ("'''Username:'''",),
    ),
    ("Stephen Cellucci", ("2013 World Championship",), ()),
    ("Angelo Consoli", ("2013 World Championship", "Wookiee Slaving"), ()),
    ("Justin Desai", ("2013 World Championship",), ()),
    ("Brian Fred", ("2013 World Championship",), ()),
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch(title: str) -> tuple[dict, str]:
    params = {
        "action": "query",
        "format": "json",
        "prop": "info|flagged|revisions",
        "rvprop": "ids|content",
        "rvslots": "main",
        "titles": title,
        "redirects": "1",
    }
    data = api(params)
    page = next(iter(data["query"]["pages"].values()))
    text = ""
    revs = page.get("revisions") or []
    if revs:
        text = revs[0].get("slots", {}).get("main", {}).get("*", "")
    return page, text


def main() -> int:
    n = 0
    for title, want, ban in CHECKS:
        page, text = fetch(title)
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        missing = [w for w in want if w not in text]
        dumped = [b for b in ban if b in text]
        dest = [d for d in DUMP if d in text]
        ok = (not missing) and (not dumped) and (not dest) and stable == latest
        if not ok:
            n += 1
            print("FAIL", title)
            if missing:
                print("  missing", missing)
            if dumped:
                print("  banned", dumped)
            if dest:
                print("  dest-dump", dest)
            if stable != latest:
                print("  flagged", stable, "latest", latest)
        else:
            print("OK", title, "oldid", latest)
    print("TOTAL", n)
    return n


if __name__ == "__main__":
    raise SystemExit(main())
