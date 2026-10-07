#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Greg Shaw p07 Dark."""
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
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Greg Shaw DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Greg Shaw]]",
            "[[Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)]]",
            "4x [[Galen Marek, Starkiller]]",
            "[[Rogue Shadow]]",
            "[[Juno Eclipse, Black Leader]]",
            "[[Sith Fury & End This Destructive Conflict]]",
            "[[They're Still Coming Through!]]",
            "[[File:2013 Texas Mini Worlds Day 1 p07 Greg Shaw DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "Greg Shaw",
        (
            "2013 Texas Mini Worlds",
            "Hunt Down And Destroy The Jedi (V)",
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
        if "Hunt Down" in title and title.startswith("2013 Texas Mini Worlds Day 1"):
            if "p07" not in html:
                print("  THUMB miss p07")
                fails += 1
        if title == "2013 Texas Mini Worlds":
            # Light unpublished Same as Barry
            row_ok = "Hunt Down And Destroy The Jedi (V)" in text
            if not row_ok:
                print("  HUB Dark still empty")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
