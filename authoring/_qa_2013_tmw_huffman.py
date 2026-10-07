#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Blake Huffman p28 Dark / p29 Light."""
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
            "[[Blake Huffman]]",
            "Carbon Chamber Testing",
            "The Hyperdrive Generator's Gone",
            "[[Brian Herold]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Blake Huffman LS The Hyperdrive Generator's Gone",
        (
            "[[Blake Huffman]]",
            "[[The Hyperdrive Generator's Gone / We'll Need A New One]]",
            "[[Han Solo, Innocent Scoundrel]]",
            "[[Armed And Dangerous & •Krayt Dragon Howl|Armed And Dangerous & Krayt Dragon Howl]]",
            "2x [[Mace Windu (V) (Virtual Block 5)|Mace Windu (V)]]",
            "[[Chewbacca, Walking Carpet]]",
            "[[File:2013 Texas Mini Worlds Day 1 p29 Blake Huffman LS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Blake Huffman DS Carbon Chamber Testing",
        (
            "[[Blake Huffman]]",
            "[[Carbon Chamber Testing / My Favorite Decoration]]",
            "[[Luuke]]",
            "[[Jabba's Prize]]",
            "[[Jango Fett, The Assassin]]",
            "3x [[Emperor Palpatine]]",
            "[[File:2013 Texas Mini Worlds Day 1 p28 Blake Huffman DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "Blake Huffman",
        (
            "2013 Texas Mini Worlds",
            "Carbon Chamber Testing",
            "The Hyperdrive Generator's Gone",
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
        if "Hyperdrive" in title:
            if "p29" not in html:
                print("  THUMB miss p29")
                fails += 1
        if title.endswith("Carbon Chamber Testing") and "Blake Huffman" in title:
            if "p28" not in html:
                print("  THUMB miss p28")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
