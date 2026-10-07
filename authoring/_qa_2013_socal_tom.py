#!/usr/bin/env python3
"""Live QA: 2013 SoCal Day 1 Tom p21 Light / p22 Dark."""
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
            "[[Tom]]",
            "Watch Your Step",
            "Agents Of Black Sun",
            "[[Steve Harpster]]",
            "[[Brian Fred]]",
        ),
        (),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Tom LS Watch Your Step",
        (
            "[[Tom]]",
            "[[Watch Your Step / This Place Can Be A Little Rough]]",
            "[[Let The Wookiee Win (V) (Virtual Block 6)|Let The Wookiee Win (V)]]",
            "[[File:2013 SoCal Grand Prix Day 1 p21 Tom LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 SoCal Grand Prix Day 1 Tom DS Agents Of Black Sun",
        (
            "[[Tom]]",
            "[[Agents Of Black Sun / Vengeance Of The Dark Prince]]",
            "[[Velken Tezeri (V) (Dark)|Velken Tezeri (V)]]",
            "[[File:2013 SoCal Grand Prix Day 1 p22 Tom DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "Tom",
        (
            "2013 SoCal Grand Prix",
            "Watch Your Step",
            "Agents Of Black Sun",
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
