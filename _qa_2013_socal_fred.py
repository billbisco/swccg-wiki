#!/usr/bin/env python3
"""Live QA: 2013 SoCal Day 1 Brian Fred p11 Light / p12 Dark."""
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
            "[[Brian Fred]]",
            "Mind What You Have Learned (V)",
            "Knowledge And Defense",
            "[[Steve Brentson]]",
            "[[Gabe]]",
            "[[Phil Aasen]]",
        ),
        (),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Brian Fred LS Mind What You Have Learned (V)",
        (
            "[[Brian Fred]]",
            "[[Mind What You Have Learned (V) / Save You It Can (V)]]",
            "4x [[Let The Wookiee Win (V) (Virtual Block 6)|Let The Wookiee Win (V)]]",
            "3x [[Luke Skywalker, Strong In The Force]]",
            "[[Strong Is Vader]]",
            "[[Anger, Fear, Aggression (V) (Virtual Block 4)|Anger, Fear, Aggression (V)]]",
            "[[File:2013 SoCal Grand Prix Day 1 p11 Brian Fred LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Brian Fred DS Knowledge And Defense (V)",
        (
            "[[Brian Fred]]",
            "[[Knowledge And Defense (V) (Dark)|Knowledge And Defense (V)]]",
            "[[Sneak Attack (V) (Dark)|Sneak Attack (V)]]",
            "[[Maarek Stele, The Emperor's Reach (Dark)|Maarek Stele, The Emperor's Reach]]",
            "[[Jango Fett, The Assassin]]",
            "[[Control & Set For Stun]]",
            "[[File:2013 SoCal Grand Prix Day 1 p12 Brian Fred DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "Brian Fred",
        (
            "2013 SoCal Grand Prix",
            "Mind What You Have Learned (V)",
            "Knowledge And Defense",
            "2013 World Championship",
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
