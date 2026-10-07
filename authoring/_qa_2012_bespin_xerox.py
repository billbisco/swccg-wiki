#!/usr/bin/env python3
"""Live QA for 2012 Bespin Regionals leftover Xerox dests.

python _qa_2012_bespin_xerox.py --delta   # last pair + hub
python _qa_2012_bespin_xerox.py --full    # every CHECK (default)
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2012 Bespin Regionals Mitch Nieland LS Quiet Mining Colony",
        ["Quiet Mining Colony", "Bespin", "Mitch Nieland"],
    ),
    (
        "2012 Bespin Regionals Mitch Nieland DS Ralltiir Operations",
        ["Ralltiir Operations", "Knowledge And Defense", "Mitch Nieland"],
    ),
    (
        "2012 Bespin Regionals Charlie Arlandson LS Naboo: Boss Nass' Chambers",
        ["Naboo", "Charlie Arlandson"],
    ),
    (
        "2012 Bespin Regionals Charlie Arlandson DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Knowledge And Defense", "Charlie Arlandson"],
    ),
    (
        "2012 Bespin Regionals Scott Morgan LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Scott Morgan"],
    ),
    (
        "2012 Bespin Regionals Scott Morgan DS A Stunning Move",
        ["A Stunning Move", "Knowledge And Defense", "Scott Morgan"],
    ),
    (
        "2012 Bespin Regionals Conrad Simmering LS Watch Your Step (V)",
        ["Watch Your Step", "Conrad Simmering"],
    ),
    (
        "2012 Bespin Regionals Conrad Simmering DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Conrad Simmering"],
    ),
    (
        "2012 Bespin Regionals Cooleo LS Rebel Strike Team (V)",
        ["Rebel Strike Team", "Cooleo"],
    ),
    (
        "2012 Bespin Regionals Cooleo DS Executor: Meditation Chamber",
        ["Executor", "Knowledge And Defense", "Cooleo"],
    ),
    (
        "2012 Bespin Regionals Brandon Brist DS Combat Readiness (V)",
        ["Combat Readiness", "Knowledge And Defense", "Brandon Brist"],
    ),
    (
        "2012 Bespin Regionals Calvin Kurten LS There Is Good In Him",
        ["There Is Good In Him", "Calvin Kurten"],
    ),
    (
        "2012 Bespin Regionals Calvin Kurten DS Bring Him Before Me",
        ["Bring Him Before Me", "Knowledge And Defense", "Calvin Kurten"],
    ),
    (
        "2012 Bespin Regionals Mark Peterson LS We'll Handle This (V)",
        ["We'll Handle This", "Mark Peterson"],
    ),
    (
        "2012 Bespin Regionals Mark Peterson DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "Mark Peterson"],
    ),
    (
        "2012 Bespin Regionals Nick Rambo LS You Can Either Profit By This...",
        ["You Can Either Profit By This", "Nick Rambo"],
    ),
    (
        "2012 Bespin Regionals Nick Rambo DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "Nick Rambo"],
    ),
    (
        "2012 Bespin Regionals Jim Li LS Watch Your Step",
        ["Watch Your Step", "Jim Li"],
    ),
    (
        "2012 Bespin Regionals Jim Li DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Knowledge And Defense", "Jim Li"],
    ),
    (
        "2012 Bespin Regionals Brian Herold LS Infiltration",
        ["Infiltration", "Brian Herold"],
    ),
    (
        "2012 Bespin Regionals Brian Herold DS Combat Readiness (V)",
        ["Combat Readiness", "Knowledge And Defense", "Brian Herold"],
    ),
    (
        "2012 Bespin Regionals Morgan Dwyer LS Mind What You Have Learned (V)",
        ["Mind What You Have Learned", "Morgan Dwyer"],
    ),
    (
        "2012 Bespin Regionals Morgan Dwyer DS Combat Readiness",
        ["Combat Readiness", "Knowledge And Defense", "Morgan Dwyer"],
    ),
    (
        "2012 Bespin Regionals John Anderson LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "John Anderson"],
    ),
    (
        "2012 Bespin Regionals John Anderson DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "John Anderson"],
    ),
    (
        "2012 Bespin Regionals Jake Nelson LS Quiet Mining Colony",
        ["Quiet Mining Colony", "Jake Nelson"],
    ),
    (
        "2012 Bespin Regionals Jake Nelson DS Combat Readiness (V)",
        ["Combat Readiness", "Knowledge And Defense", "Jake Nelson"],
    ),
    (
        "2012 Bespin Regionals Matt Hanson LS Mind What You Have Learned",
        ["Mind What You Have Learned", "Matt Hanson"],
    ),
    (
        "2012 Bespin Regionals Matt Hanson DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Matt Hanson"],
    ),
    (
        "2012 Bespin Regionals Mike (2012 Bespin Regionals) DS Endor Operations",
        ["Endor Operations", "Mike (2012 Bespin Regionals)"],
    ),
    (
        "2012 Bespin Regionals Mark Walseth LS Careful Planning (V)",
        ["Careful Planning", "Mark Walseth"],
    ),
    (
        "2012 Bespin Regionals Mark Walseth DS Endor Operations",
        ["Endor Operations", "Mark Walseth"],
    ),
    (
        "2012 Bespin Regionals",
        ["Mitch Nieland", "Charlie Arlandson", "Scott Morgan", "Conrad Simmering", "Cooleo", "Brandon Brist", "Calvin Kurten", "Mark Peterson", "Nick Rambo", "Jim Li", "Brian Herold", "Morgan Dwyer", "John Anderson", "Jake Nelson", "Matt Hanson", "Mike (2012 Bespin Regionals)", "Mark Walseth", "14 July 2012"],
    ),
]


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "text|revid|displaytitle",
            "format": "json",
            "disablelimitreport": 1,
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def flagged(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    return next(iter(pages.values()))


def select_checks(delta: bool) -> list:
    if not delta:
        return CHECKS
    hub = [c for c in CHECKS if c[0] == "2012 Bespin Regionals"]
    decks = [c for c in CHECKS if c[0] != "2012 Bespin Regionals"]
    return decks[-2:] + hub


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--delta", action="store_true", help="last pair + hub")
    ap.add_argument("--full", action="store_true", help="every CHECK (default)")
    args = ap.parse_args()
    checks = select_checks(args.delta and not args.full)
    fail = 0
    for title, needles in checks:
        data = parse(title)
        if "error" in data:
            print("FAIL", title, data["error"])
            fail += 1
            continue
        html = data["parse"]["text"]["*"]
        missing = [n for n in needles if n not in html]
        fl = flagged(title)
        latest = fl.get("lastrevid")
        stable = (fl.get("flagged") or {}).get("stable_revid")
        fr = "OK" if latest and stable and int(latest) == int(stable) else f"latest={latest} stable={stable}"
        if missing or fr != "OK":
            print("FAIL", title, "missing", missing, "fr", fr)
            fail += 1
        else:
            print("OK", title, "fr", fr)
    mode = "delta" if args.delta and not args.full else "full"
    print("TOTAL", fail, "n", len(checks), mode)


if __name__ == "__main__":
    main()
