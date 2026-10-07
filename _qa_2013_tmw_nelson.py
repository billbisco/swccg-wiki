#!/usr/bin/env python3
"""Live QA: 2013 TMW Day 1 Aaron Nelson p03 Light / p04 Dark."""
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
            "[[Aaron Nelson]]",
            "No Money, No Parts, No Deal!",
            "Watch Your Step (V)",
        ),
        (),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Aaron Nelson LS Watch Your Step (V)",
        (
            "[[Aaron Nelson]]",
            "[[Watch Your Step (V) / This Place Can Be A Little Rough (V)]]",
            "'''Username:''' Airdog2003",
            "3x [[Luke Skywalker, Jedi Knight]]",
            "[[Padme Naberrie (V) (Virtual Block 5)|Padme Naberrie (V)]]",
            "[[Captain Han Solo]]",
            "2x [[Naboo: Boss Nass' Chambers]]",
            "[[All Wings Report In & •Darklighter Spin|All Wings Report In & Darklighter Spin]]",
            "[[Executor: Docking Bay]]",
            "[[Have You Seen These Stormtroopers?]]",
            "[[Nobility (V)]]",
            "[[Home One]]",
            "[[File:2013 Texas Mini Worlds Day 1 p03 Aaron Nelson LS.png|800px]]",
        ),
        ("Jake Nelson",),
    ),
    (
        "2013 Texas Mini Worlds Day 1 Aaron Nelson DS No Money, No Parts, No Deal!",
        (
            "[[Aaron Nelson]]",
            "[[No Money, No Parts, No Deal! / You're A Slave?]]",
            "'''Username:''' Airdog2003",
            "[[The Mandalorian]]",
            "[[Myn Kyneugh (V) (Dark)|Myn Kyneugh (V)]]",
            "[[Fear Is My Ally]]",
            "[[Tatooine: Jabba's Palace]]",
            "[[Evader & Concentrate Fire (V)]]",
            "2x [[Surface Bombardment (V)]]",
            "[[What Have You Done? (V)]]",
            "[[File:2013 Texas Mini Worlds Day 1 p04 Aaron Nelson DS.png|800px]]",
        ),
        ("Jake Nelson", "Jango Fett, The Assassin"),
    ),
    (
        "Aaron Nelson",
        (
            "2013 Texas Mini Worlds",
            "No Money, No Parts, No Deal!",
            "Watch Your Step (V)",
            "2013 World Championship",
            "2013 Match Play Championship",
        ),
        ("Jake Nelson",),
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
        if "p03 Aaron Nelson LS" in title or title.endswith("Watch Your Step (V)"):
            if "p03" not in html or "Aaron" not in html:
                if "p03_Aaron_Nelson" not in html.replace(" ", "_") and "p03 Aaron Nelson" not in html:
                    print("  THUMB miss p03")
                    fails += 1
        if "p04" in title or "No Money, No Parts, No Deal!" in title:
            if "Day 1 Aaron Nelson DS" in title:
                if "p04" not in html:
                    print("  THUMB miss p04")
                    fails += 1
        if title == "2013 Texas Mini Worlds":
            if "No Money, No Parts, No Deal!" not in text:
                print("  HUB Dark still empty")
                fails += 1
    print("TOTAL", fails)
    raise SystemExit(fails)


if __name__ == "__main__":
    main()
