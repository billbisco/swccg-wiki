#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 JW Millet p20 Light / p21 Dark."""
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
        "2013 Texas Mini Worlds",
        (
            "[[JW Millet]]",
            "A Stunning Move",
            "There Is Good In Him",
            "[[Bobby Hilbun]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 JW Millet DS A Stunning Move",
        (
            "[[JW Millet]]",
            "'''Username:''' Asphalizo",
            "[[A Stunning Move / A Valuable Hostage (Virtual Block 7)|A Stunning Move / A Valuable Hostage]]",
            "[[Jango Fett, The Assassin]]",
            "[[Grievous, Hunter Of Jedi]]",
            "[[Galen, Secret Apprentice]]",
            "[[Lurke]]",
            "[[Jabba's Haven (Dark)|Jabba's Haven]]",
            "[[File:2013 Texas Mini Worlds Day 1 p21 JW Millet DS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 JW Millet LS There Is Good In Him",
        (
            "[[JW Millet]]",
            "'''Username:''' Asphalizo",
            "[[There Is Good In Him / I Can Save Him]]",
            "2x [[Wookiee Roar (V) (Virtual Block 5)|Wookiee Roar (V)]]",
            "[[Odin Nesloor & •First Aid (Virtual Block 6)|Odin Nesloor & First Aid]]",
            "[[File:2013 Texas Mini Worlds Day 1 p20 JW Millet LS.png|800px]]",
        ),
        (),
    ),
    (
        "JW Millet",
        (
            "2013 Texas Mini Worlds",
            "A Stunning Move",
            "There Is Good In Him",
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
        text = revs[0].get("slots", {}).get("main", {}).get("*", "") or ""
    return page, text


def parse_html(title: str) -> str:
    params = {
        "action": "parse",
        "format": "json",
        "page": title,
        "prop": "text",
        "disablelimitreport": "1",
    }
    data = api(params)
    return data.get("parse", {}).get("text", {}).get("*", "") or ""


def main() -> None:
    fails = 0
    for title, need, forbid in CHECKS:
        page, text = fetch(title)
        print("PAGE", title, "id", page.get("pageid"), "latest", page.get("lastrevid"))
        flagged = page.get("flagged") or {}
        print("  flagged", flagged.get("stable_revid"), "pending", flagged.get("pending_since"))
        if flagged.get("stable_revid") and flagged.get("stable_revid") != page.get("lastrevid"):
            print("  UNSTABLE latest", page.get("lastrevid"), "stable", flagged.get("stable_revid"))
            fails += 1
        for s in need:
            if s not in text:
                print("  MISS", s)
                fails += 1
        for s in forbid:
            if s in text:
                print("  FORBID", s)
                fails += 1
        for s in DUMP:
            if s in text:
                print("  DUMP", s)
                fails += 1
        html = parse_html(title)
        if "A Stunning Move" in title and "JW Millet" in title:
            if "p21" not in html:
                print("  THUMB miss p21")
                fails += 1
        if "There Is Good In Him" in title and "JW Millet" in title:
            if "p20" not in html:
                print("  THUMB miss p20")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
