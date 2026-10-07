#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Greg Shaw p09 Dark / p10 Light."""
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
            "[[Greg Shaw]]",
            "Hunt Down And Destroy The Jedi (V)",
            "Agents Of Black Sun",
            "There Is Good In Him",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Greg Shaw DS Agents Of Black Sun",
        (
            "[[Greg Shaw]]",
            "[[Agents Of Black Sun / Vengeance Of The Dark Prince]]",
            "2x [[Vigo (V) (Dark)|Vigo (V)]]",
            "[[Bossk (V) (Dark)|Bossk (V)]]",
            "[[Lana Dobreed & •Sacrifice (Dark)|Lana Dobreed & Sacrifice]]",
            "[[Look Sir, Droids]]",
            "[[Cease Fire!]]",
            "[[Ghhhk & Those Rebels Won't Escape Us]]",
            "[[Lightsaber Proficiency (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p09 Greg Shaw DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Greg Shaw LS There Is Good In Him",
        (
            "[[Greg Shaw]]",
            "[[There Is Good In Him / I Can Save Him]]",
            "[[Grimtaash]]",
            "[[The Bith Shuffle & Desperate Reach]]",
            "2x [[Let The Wookiee Win (V) (Virtual Block 6)|Let The Wookiee Win (V)]]",
            "3x [[Rebel Leadership (V) (Virtual Block 3)|Rebel Leadership (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p10 Greg Shaw LS.png|800px]]",
        ),
        ("'''Username:'''", "Scrambled Transmission"),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Greg Shaw DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Greg Shaw]]",
            "[[Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)]]",
            "4x [[Galen Marek, Starkiller]]",
        ),
        (),
    ),
    (
        "Greg Shaw",
        (
            "2013 Texas Mini Worlds",
            "Hunt Down And Destroy The Jedi (V)",
            "Agents Of Black Sun",
            "There Is Good In Him",
            "2013 Match Play Championship",
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
        if "Agents Of Black Sun" in title:
            if "p09" not in html:
                print("  THUMB miss p09")
                fails += 1
        if "There Is Good In Him" in title and title.startswith("2013 Texas Mini Worlds Day 1"):
            if "p10" not in html:
                print("  THUMB miss p10")
                fails += 1
        if title == "2013 Texas Mini Worlds":
            if text.count("|[[Greg Shaw]]") < 2 and text.count("| [[Greg Shaw]]") < 2:
                print("  HUB missing two Greg Shaw rows")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
