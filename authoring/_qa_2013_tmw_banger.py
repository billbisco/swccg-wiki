#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Amar Banger p34 Light / p35 Dark."""
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
)
CHECKS = [
    (
        "2013 Texas Mini Worlds",
        (
            "[[Amar Banger]]",
            "Anger, Fear, Aggression (V)",
            "Knowledge And Defense (V)",
            "[[Barry Alperstein]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Amar Banger LS Anger, Fear, Aggression (V)",
        (
            "[[Amar Banger]]",
            "[[Anger, Fear, Aggression (V) (Virtual Block 4)|Anger, Fear, Aggression (V)]]",
            "'''Username:''' abanger",
            "[[Dash In Rogue 10]]",
            "3x [[Rebel Leadership (V) (Virtual Block 3)|Rebel Leadership (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p34 Amar Banger LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Amar Banger DS Knowledge And Defense (V)",
        (
            "[[Amar Banger]]",
            "[[Knowledge And Defense (V) (Dark)|Knowledge And Defense (V)]]",
            "'''Username:''' abanger",
            "5x [[We Must Accelerate Our Plans]]",
            "[[Gardulla The Hutt (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p35 Amar Banger DS.png|800px]]",
        ),
        (),
    ),
    (
        "Amar Banger",
        (
            "2013 Texas Mini Worlds",
            "Anger, Fear, Aggression (V)",
            "Knowledge And Defense (V)",
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
