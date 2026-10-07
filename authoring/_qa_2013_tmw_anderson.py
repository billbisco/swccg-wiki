#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 John Anderson p30 Dark / p31 Light."""
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
            "[[John Anderson]]",
            "Contract Killers",
            "Watch Your Step",
            "[[Blake Huffman]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 John Anderson LS Watch Your Step",
        (
            "[[John Anderson]]",
            "[[Watch Your Step / This Place Can Be A Little Rough]]",
            "'''Username:''' puck71",
            "3x [[Han Solo, Innocent Scoundrel]]",
            "[[Han's Blaster, So Uncivilized]]",
            "[[Lady Luck]]",
            "2x [[Rebel Agent]]",
            "[[Can You Growl]]",
            "[[Tala Verde]]",
            "[[Jabba's Prize]]",
            "[[File:2013 Texas Mini Worlds Day 1 p31 John Anderson LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 John Anderson DS Contract Killers",
        (
            "[[John Anderson]]",
            "[[Contract Killers / Feared Throughout The Galaxy]]",
            "'''Username:''' Puck71",
            "[[Jango Fett, The Assassin]]",
            "3x [[Galen, Secret Apprentice]]",
            "3x [[Arica (V) (Dark)|Arica (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p30 John Anderson DS.png|800px]]",
        ),
        (),
    ),
    (
        "John Anderson",
        (
            "2013 Texas Mini Worlds",
            "Contract Killers",
            "Watch Your Step",
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
        if "Watch Your Step" in title and "John Anderson" in title:
            if "p31" not in html:
                print("  THUMB miss p31")
                fails += 1
        if title.endswith("Contract Killers") and "John Anderson" in title:
            if "p30" not in html:
                print("  THUMB miss p30")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
