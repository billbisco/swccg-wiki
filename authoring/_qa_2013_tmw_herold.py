#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Brian Herold p26 Light / p27 Dark."""
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
            "[[Brian Herold]]",
            "The Hyperdrive Generator's Gone",
            "Contract Killers",
            "[[Steve Izzo]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Brian Herold LS The Hyperdrive Generator's Gone",
        (
            "[[Brian Herold]]",
            "[[The Hyperdrive Generator's Gone / We'll Need A New One]]",
            "'''Username:''' Carly Rae Cyrus",
            "2x [[Mace Windu, Master Of The Order]]",
            "2x [[Master Qui-Gon]]",
            "[[Lando With Vibro-Ax]]",
            "6x [[Nabrun Leids]]",
            "[[File:2013 Texas Mini Worlds Day 1 p26 Brian Herold LS.png|800px]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Brian Herold DS Contract Killers",
        (
            "[[Brian Herold]]",
            "[[Contract Killers / Feared Throughout The Galaxy]]",
            "'''Username:''' Psy Snootles",
            "3x [[Galen, Secret Apprentice]]",
            "[[Jango Fett, The Assassin]]",
            "[[Ket Maliss, Shadow Killer]]",
            "[[Aurra Sing, Deadly Assassin]]",
            "[[Weapon Of A Sith]]",
            "[[File:2013 Texas Mini Worlds Day 1 p27 Brian Herold DS.png|800px]]",
        ),
        (),
    ),
    (
        "Brian Herold",
        (
            "2013 Texas Mini Worlds",
            "The Hyperdrive Generator's Gone",
            "Contract Killers",
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
        if "p26" in title or "Hyperdrive" in title:
            if "p26" not in html:
                print("  THUMB miss p26")
                fails += 1
        if "p27" in title or (title.endswith("Contract Killers") and "Brian Herold" in title):
            if "p27" not in html:
                print("  THUMB miss p27")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
