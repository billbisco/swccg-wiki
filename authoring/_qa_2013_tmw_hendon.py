#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Robbie Hendon p05 Light / p06 Dark."""
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
            "[[Robbie Hendon]]",
            "My Lord, Is That Legal?",
            "Plead My Case To The Senate",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Robbie Hendon LS Plead My Case To The Senate",
        (
            "[[Robbie Hendon]]",
            "[[Plead My Case To The Senate / Sanity And Compassion]]",
            "'''Username:''' /hendon",
            "3x [[Horox Ryyder]]",
            "[[Liana Merian]]",
            "[[Yarna d'al' Gargan]]",
            "[[Threepio With His Parts Showing]]",
            "[[Lady Luck]]",
            "2x [[Sorry About The Mess & •Blaster Proficiency|Sorry About The Mess & Blaster Proficiency]]",
            "[[File:2013 Texas Mini Worlds Day 1 p05 Robbie Hendon LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Robbie Hendon DS My Lord, Is That Legal?",
        (
            "[[Robbie Hendon]]",
            "[[My Lord, Is That Legal? / I Will Make It Legal]]",
            "'''Username:''' /hendon",
            "[[Jango Fett, The Assassin]]",
            "[[Boba Fett, Prepared Hunter]]",
            "3x [[Darth Maul With Lightsaber]]",
            "3x [[Lott Dod]]",
            "[[This Is Outrageous!]]",
            "[[File:2013 Texas Mini Worlds Day 1 p06 Robbie Hendon DS.png|800px]]",
        ),
        ("The Mandalorian",),
    ),
    (
        "Robbie Hendon",
        (
            "2013 Texas Mini Worlds",
            "My Lord, Is That Legal?",
            "Plead My Case To The Senate",
            "2026 Tenth Annual GEMPC",
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
        if "Plead My Case" in title:
            if "p05" not in html:
                print("  THUMB miss p05")
                fails += 1
        if "My Lord" in title and title.startswith("2013 Texas Mini Worlds Day 1"):
            if "p06" not in html:
                print("  THUMB miss p06")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
