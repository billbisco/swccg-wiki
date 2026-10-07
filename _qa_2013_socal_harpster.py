#!/usr/bin/env python3
"""Live QA: 2013 SoCal Day 1 Steve Harpster p13 Light / p14 Dark."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
    "Handwritten 2009 Print Form",
    "Handwritten 2013 Print Form",
    "Typed slang printout",
    "Typed 2013 Print Form",
)
CHECKS = [
    (
        "2013 SoCal Grand Prix",
        (
            "[[Steve Harpster]]",
            "Watch Your Step (V)",
            "Ralltiir Operations",
            "[[Brian Fred]]",
            "[[Steve Brentson]]",
            "[[Gabe]]",
        ),
        (),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Steve Harpster LS Watch Your Step (V)",
        (
            "[[Steve Harpster]]",
            "[[Watch Your Step (V) / This Place Can Be A Little Rough (V)]]",
            "2x [[Let The Wookiee Win (V) (Virtual Block 6)|Let The Wookiee Win (V)]]",
            "2x [[Antilles Maneuver (V) (Virtual Block 1)|Antilles Maneuver (V)]]",
            "[[Leia With Blaster Rifle]]",
            "[[File:2013 SoCal Grand Prix Day 1 p13 Steve Harpster LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Steve Harpster DS Ralltiir Operations",
        (
            "[[Steve Harpster]]",
            "[[Ralltiir Operations / In The Hands Of The Empire]]",
            "[[Ysanne Isard (Dark)|Ysanne Isard]]",
            "[[Maarek Stele, The Emperor's Reach (Dark)|Maarek Stele, The Emperor's Reach]]",
            "3x [[Imperial Command]]",
            "[[File:2013 SoCal Grand Prix Day 1 p14 Steve Harpster DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "Steve Harpster",
        (
            "2013 SoCal Grand Prix",
            "Watch Your Step (V)",
            "Ralltiir Operations",
        ),
        (),
    ),
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
        "prop": "revisions|flagged|info",
        "rvprop": "content|ids",
        "titles": title,
    }
    data = api(params)
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))
    revs = page.get("revisions") or []
    text = revs[0]["*"] if revs else ""
    return page, text


def main() -> None:
    failed = 0
    for title, must, must_not in CHECKS:
        page, text = fetch(title)
        flagged = page.get("flagged") or {}
        latest = (page.get("revisions") or [{}])[0].get("revid")
        stable = flagged.get("stable_revid")
        print(f"== {title} pageid={page.get('pageid')} latest={latest} stable={stable}")
        if not text:
            print(" FAIL empty")
            failed += 1
            continue
        if latest and stable and latest != stable:
            print(f" FAIL flagged latest {latest} != stable {stable}")
            failed += 1
        for s in must:
            if s not in text:
                print(f" FAIL missing {s!r}")
                failed += 1
        for s in must_not:
            if s in text:
                print(f" FAIL has {s!r}")
                failed += 1
        if title.startswith("2013 SoCal Grand Prix Day"):
            for s in DUMP:
                if s in text:
                    print(f" FAIL dest-dump {s!r}")
                    failed += 1
    print("TOTAL", failed)


if __name__ == "__main__":
    main()
