#!/usr/bin/env python3
"""Live QA: 2013 Alderaan leftover Xerox Tom / Shannon / Schoenthal / Nathan."""
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
        "2013 Alderaan Regionals",
        (
            "[[Tom]]",
            "[[Kevin Shannon]]",
            "[[Chris Schoenthal]]",
            "[[Nathan]]",
            "Watch Your Step (V)",
            "Carbon Chamber Testing",
            "Quiet Mining Colony",
            "Yavin 4: Throne Room",
        ),
        (),
    ),
    (
        "2013 Alderaan Regionals Tom LS Watch Your Step (V)",
        (
            "[[Tom]]",
            "[[Watch Your Step (V) / This Place Can Be A Little Rough (V)]]",
            "[[File:2013 Alderaan Regionals p03 Tom LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Alderaan Regionals Tom DS Agents Of Black Sun",
        (
            "[[Tom]]",
            "[[Agents Of Black Sun / Vengeance Of The Dark Prince]]",
            "[[File:2013 Alderaan Regionals p04 Tom DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Alderaan Regionals Kevin Shannon LS Quiet Mining Colony",
        (
            "[[Kevin Shannon]]",
            "[[Quiet Mining Colony / Independent Operation]]",
            "[[File:2013 Alderaan Regionals p08 Kevin Shannon LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Alderaan Regionals Kevin Shannon DS Carbon Chamber Testing",
        (
            "[[Kevin Shannon]]",
            "[[Carbon Chamber Testing / My Kind Of Scum]]",
            "[[File:2013 Alderaan Regionals p07 Kevin Shannon DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Alderaan Regionals Chris Schoenthal LS Watch Your Step",
        (
            "[[Chris Schoenthal]]",
            "[[Watch Your Step / This Place Can Be A Little Rough]]",
            "'''Username:''' imrhil327",
            "[[File:2013 Alderaan Regionals p21 Chris Schoenthal LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Alderaan Regionals Chris Schoenthal DS Ralltiir Operations",
        (
            "[[Chris Schoenthal]]",
            "[[Ralltiir Operations / In The Hands Of The Empire]]",
            "'''Username:''' imrhil327",
            "[[File:2013 Alderaan Regionals p22 Chris Schoenthal DS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Alderaan Regionals Nathan LS Yavin 4: Throne Room",
        (
            "[[Nathan]]",
            "[[Yavin 4: Throne Room]]",
            "'''Username:''' SolaGratia",
            "[[File:2013 Alderaan Regionals p26 Nathan LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Alderaan Regionals Nathan DS Ralltiir Operations",
        (
            "[[Nathan]]",
            "[[Ralltiir Operations / In The Hands Of The Empire]]",
            "'''Username:''' SolaGratia",
            "[[File:2013 Alderaan Regionals p25 Nathan DS.png|800px]]",
        ),
        (),
    ),
    (
        "Tom",
        (
            "2013 Alderaan Regionals",
            "Watch Your Step (V)",
            "Agents Of Black Sun",
        ),
        (),
    ),
    (
        "Kevin Shannon",
        (
            "2013 Alderaan Regionals",
            "Quiet Mining Colony",
            "Carbon Chamber Testing",
        ),
        (),
    ),
    (
        "Chris Schoenthal",
        (
            "2013 Alderaan Regionals",
            "Watch Your Step",
            "Ralltiir Operations",
        ),
        (),
    ),
    (
        "Nathan",
        (
            "2013 Alderaan Regionals",
            "Yavin 4: Throne Room",
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
    text = revs[0].get("*") or revs[0].get("slots", {}).get("main", {}).get("*") or ""
    return page, text


def main() -> None:
    fail = 0
    for title, need, forbid in CHECKS:
        page, text = fetch(title)
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        print(f"TITLE {title} pageid={page.get('pageid')} latest={latest} stable={stable}")
        if not text:
            print("  FAIL empty")
            fail += 1
            continue
        if title.startswith("2013 Alderaan Regionals ") and title != "2013 Alderaan Regionals":
            for needle in DUMP:
                if needle in text:
                    print(f"  FAIL dump {needle!r}")
                    fail += 1
        for needle in need:
            if needle not in text:
                print(f"  FAIL missing {needle!r}")
                fail += 1
        for needle in forbid:
            if needle in text:
                print(f"  FAIL forbidden {needle!r}")
                fail += 1
        if stable and latest and int(stable) != int(latest):
            print(f"  FAIL flagged {stable} != {latest}")
            fail += 1
    print("TOTAL", fail)


if __name__ == "__main__":
    main()
