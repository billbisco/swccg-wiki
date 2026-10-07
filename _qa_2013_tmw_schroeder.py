#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Olaf Schroeder p38 Dark / p39 Light."""
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
)
CHECKS = [
    (
        "2013 Texas Mini Worlds",
        (
            "[[Olaf Schroeder]]",
            "Hunt Down And Destroy The Jedi (V)",
            "Plead My Case To The Senate",
            "[[Allen Gamble]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Olaf Schroeder LS Plead My Case To The Senate",
        (
            "[[Olaf Schroeder]]",
            "'''Username:''' Joe Freedom",
            "[[Plead My Case To The Senate / Sanity And Compassion]]",
            "[[Coruscant: Galactic Senate]]",
            "3x [[Redemption (V) (Virtual Block 2)|Redemption (V)]]",
            "3x [[Qui-Gon Jinn With Lightsaber]]",
            "[[Artoo, Brave Little Droid (V)]]",
            "[[Lando Calrissian, Scoundrel]]",
            "[[File:2013 Texas Mini Worlds Day 1 p39 Olaf Schroeder LS.png|800px]]",
        ),
        ("Artoo-Detoo In Red 5",),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Olaf Schroeder DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Olaf Schroeder]]",
            "'''Username:''' Joe Freedom",
            "[[Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)]]",
            "3x [[Galen Marek, Starkiller]]",
            "3x [[Darth Vader, Dark Lord Of The Sith]]",
            "[[Grievous, Hunter Of Jedi]]",
            "[[Grievous' Lightsabers]]",
            "[[Myn Kyneusk (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p38 Olaf Schroeder DS.png|800px]]",
        ),
        (),
    ),
    (
        "Olaf Schroeder",
        (
            "2013 Texas Mini Worlds",
            "Hunt Down And Destroy The Jedi (V)",
            "Plead My Case To The Senate",
            "Endor Operations",
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
        "rvslots": "main",
        "titles": title,
    }
    data = api(params)
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))
    revs = page.get("revisions") or []
    text = ""
    if revs:
        text = revs[0].get("slots", {}).get("main", {}).get("*") or ""
    return page, text


def main() -> None:
    fails = 0
    for title, must, must_not in CHECKS:
        page, text = fetch(title)
        flagged = page.get("flagged") or {}
        latest = page.get("lastrevid")
        stable = flagged.get("stable_revid")
        print(f"TITLE {title} pageid={page.get('pageid')} latest={latest} stable={stable}")
        if not text:
            print("  FAIL empty")
            fails += 1
            continue
        if latest and stable and int(latest) != int(stable):
            print(f"  FAIL flagged latest={latest} stable={stable}")
            fails += 1
        for s in must:
            if s not in text:
                print(f"  FAIL missing {s!r}")
                fails += 1
        for s in must_not:
            if s in text:
                print(f"  FAIL has {s!r}")
                fails += 1
        for s in DUMP:
            if s in text:
                print(f"  FAIL dest-dump {s!r}")
                fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
