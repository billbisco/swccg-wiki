#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 Justin Desai Light p31."""
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
        "2013 World Championship",
        (
            "[[Justin Desai]]",
            "Imperial Occupation (V)",
            "Mind What You Have Learned (V)",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Justin Desai LS Mind What You Have Learned (V)",
        (
            "[[Justin Desai]]",
            "[[Mind What You Have Learned (V) / Save You It Can (V)]]",
            "[[Strong Is Vader]]",
            "[[Republic Gunship Wing]]",
            "[[Honor Of The Jedi]]",
            "[[Surprise Assault]]",
            "[[Let The Wookiee Win (V) (Virtual Block 6)|Let The Wookiee Win (V)]]",
            "[[Great Warrior]]",
            "[[File:2013 Worlds Day 2 p31 Justin Desai LS.png|800px]]",
            "Name box on the Day 2 Light sheet is blank",
        ),
        ("'''Username:'''",),
    ),
    (
        "Justin Desai",
        (
            "2013 World Championship",
            "Imperial Occupation (V)",
            "Mind What You Have Learned (V)",
            "It Is The Future You See (V)",
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
        if title.startswith("2013 Worlds Day 2 Justin Desai LS"):
            if "/images/" not in html or "p31_Justin_Desai" not in html.replace(" ", "_"):
                if "2013_Worlds_Day_2_p31" not in html and "p31 Justin Desai" not in html:
                    print("  THUMB miss p31")
                    fails += 1
        if title == "2013 World Championship" and "—" in text:
            # Day 2 Desai Light must no longer be an empty cell.
            if "Mind What You Have Learned (V)" not in text:
                print("  HUB Light still empty")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
