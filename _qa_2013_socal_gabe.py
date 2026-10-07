#!/usr/bin/env python3
"""Live QA: 2013 SoCal Day 1 Gabe p03 Light / p04 Dark."""
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
    "Typed slang printout",
    "Typed 2013 Print Form",
)
CHECKS = [
    (
        "2013 SoCal Grand Prix",
        (
            "[[Gabe]]",
            "Plead My Case To The Senate",
            "Set Your Course For Alderaan",
            "[[Phil Aasen]]",
        ),
        (),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Gabe LS Plead My Case To The Senate",
        (
            "[[Gabe]]",
            "[[Plead My Case To The Senate / Sanity And Compassion]]",
            "2x [[Han, Chewie, And The Falcon]]",
            "2x [[Luke Skywalker, Jedi Knight]]",
            "[[Mace Windu (V) (Virtual Block 5)|Mace Windu (V)]]",
            "[[File:2013 SoCal Grand Prix Day 1 p03 Gabe LS.png|800px]]",
        ),
        ("'''Username:'''", "Plead My Case To The Senate (V)"),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Gabe DS Set Your Course For Alderaan",
        (
            "[[Gabe]]",
            "[[Set Your Course For Alderaan / The Ultimate Power In The Universe]]",
            "3x [[Darth Maul With Lightsaber]]",
            "3x [[We Must Accelerate Our Plans]]",
            "[[Jango Fett, The Assassin]]",
            "[[File:2013 SoCal Grand Prix Day 1 p04 Gabe DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "Gabe",
        (
            "2013 SoCal Grand Prix",
            "Plead My Case To The Senate",
            "Set Your Course For Alderaan",
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
