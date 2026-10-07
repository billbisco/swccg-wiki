#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Bobby Hilbun p16 Dark / p17 Light."""
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
            "[[Bobby Hilbun]]",
            "Ralltiir Operations",
            "Communing",
            "[[Steve Baroni]]",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Bobby Hilbun DS Ralltiir Operations",
        (
            "[[Bobby Hilbun]]",
            "[[Ralltiir Operations / In The Hands Of The Empire]]",
            "[[Ysanne Isard (Dark)|Ysanne Isard]]",
            "[[Maarek Stele, The Emperor's Reach (Dark)|Maarek Stele, The Emperor's Reach]]",
            "[[Occupier]]",
            "[[Ghhhk & Those Rebels Won't Escape Us]]",
            "[[Abyss (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p16 Bobby Hilbun DS.png|800px]]",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Bobby Hilbun LS Communing",
        (
            "[[Bobby Hilbun]]",
            "[[Communing (Virtual Block 7)|Communing]]",
            "[[Artoo-Detoo In Red 5]]",
            "[[Luke Skywalker, Strong In The Force]]",
            "[[Chewbacca's Bowcaster]]",
            "[[Run Luke, Run! (V)]]",
            "[[Chasm (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p17 Bobby Hilbun LS.png|800px]]",
        ),
        ("'''Username:'''", "Chewbacca's Crossbow"),
    ),
    (
        "Bobby Hilbun",
        (
            "2013 Texas Mini Worlds",
            "Ralltiir Operations",
            "Communing",
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
        if "Ralltiir Operations" in title and "Bobby Hilbun" in title:
            if "p16" not in html:
                print("  THUMB miss p16")
                fails += 1
        if "Communing" in title and "Bobby Hilbun" in title:
            if "p17" not in html:
                print("  THUMB miss p17")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
