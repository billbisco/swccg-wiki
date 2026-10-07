#!/usr/bin/env python3
"""Live QA: 2013 SoCal Day 1 Nathan p41 Light / p42 Dark."""
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
            "[[Nathan]]",
            "We Have A Plan",
            "Set Your Course For Alderaan",
            "[[Josh]]",
        ),
        (),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Nathan LS We Have A Plan",
        (
            "[[Nathan]]",
            "[[We Have A Plan / They Will Be Lost And Confused]]",
            "'''Username:''' SolaGratia",
            "[[File:2013 SoCal Grand Prix Day 1 p41 Nathan LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Nathan DS Set Your Course For Alderaan",
        (
            "[[Nathan]]",
            "[[Set Your Course For Alderaan / The Ultimate Power In The Universe]]",
            "'''Username:''' SolaGratia",
            "[[File:2013 SoCal Grand Prix Day 1 p42 Nathan DS.png|800px]]",
        ),
        (),
    ),
    (
        "Nathan",
        (
            "2013 SoCal Grand Prix",
            "We Have A Plan",
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
        if title.startswith("2013 SoCal Grand Prix Day"):
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
