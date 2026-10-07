#!/usr/bin/env python3
"""Live QA for 2012 Yavin 4 Regionals leftover Xerox dests.

python _qa_2012_yavin_xerox.py --delta   # last pair + hub
python _qa_2012_yavin_xerox.py --full    # every CHECK (default)
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2012 Yavin 4 Regionals Chris Westergard LS There Is Good In Him",
        ["There Is Good In Him", "Chris Westergard"],
    ),
    (
        "2012 Yavin 4 Regionals Chris Westergard DS Endor Operations",
        ["Endor Operations", "Chris Westergard"],
    ),
    (
        "2012 Yavin 4 Regionals Scott LS Hidden Base (V)",
        ["Hidden Base", "Scott"],
    ),
    (
        "2012 Yavin 4 Regionals Scott DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Scott"],
    ),
    (
        "2012 Yavin 4 Regionals Steve Skilton LS Infiltration",
        ["Infiltration", "Steve Skilton"],
    ),
    (
        "2012 Yavin 4 Regionals Steve Skilton DS Contract Killers",
        ["Contract Killers", "Steve Skilton"],
    ),
    (
        "2012 Yavin 4 Regionals Vincent Rossi LS We Have A Plan",
        ["We Have A Plan", "Vincent Rossi"],
    ),
    (
        "2012 Yavin 4 Regionals Vincent Rossi DS Carbon Chamber Testing",
        ["Carbon Chamber Testing", "Vincent Rossi"],
    ),
    (
        "2012 Yavin 4 Regionals Joe Orthner LS Hidden Base",
        ["Hidden Base", "Joe Orthner"],
    ),
    (
        "2012 Yavin 4 Regionals Joe Orthner DS Court Of The Vile Gangster",
        ["Court Of The Vile Gangster", "Joe Orthner"],
    ),
    (
        "2012 Yavin 4 Regionals Matt Schmaltz LS Tatooine: Slave Quarters",
        ["Tatooine: Slave Quarters", "Matt Schmaltz"],
    ),
    (
        "2012 Yavin 4 Regionals Matt Schmaltz DS This Deal Is Getting Worse All The Time",
        ["This Deal Is Getting Worse All The Time", "Matt Schmaltz"],
    ),
    (
        "2012 Yavin 4 Regionals Alex Klimenko LS Dantooine Base Operations",
        ["Dantooine Base Operations", "Alex Klimenko"],
    ),
    (
        "2012 Yavin 4 Regionals Alex Klimenko DS Imperial Occupation (V)",
        ["Imperial Occupation", "Alex Klimenko"],
    ),
    (
        "2012 Yavin 4 Regionals Ben Brummett LS Local Uprising (V)",
        ["Local Uprising", "Ben Brummett"],
    ),
    (
        "2012 Yavin 4 Regionals Ben Brummett DS Imperial Occupation (V)",
        ["Imperial Occupation", "Ben Brummett"],
    ),
    (
        "2012 Yavin 4 Regionals Tom Haid LS Watch Your Step (V)",
        ["Watch Your Step", "Tom Haid"],
    ),
    (
        "2012 Yavin 4 Regionals Tom Haid DS Imperial Occupation (V)",
        ["Imperial Occupation", "Tom Haid"],
    ),
    (
        "2012 Yavin 4 Regionals Greg Shaw LS Infiltration",
        ["Infiltration", "Greg Shaw"],
    ),
    (
        "2012 Yavin 4 Regionals Greg Shaw DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Greg Shaw"],
    ),
    (
        "2012 Yavin 4 Regionals Vikram Bali LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Vikram Bali"],
    ),
    (
        "2012 Yavin 4 Regionals Vikram Bali DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Vikram Bali"],
    ),
    (
        "2012 Yavin 4 Regionals Michael Klimenko LS Local Uprising (V)",
        ["Local Uprising", "Michael Klimenko"],
    ),
    (
        "2012 Yavin 4 Regionals Michael Klimenko DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Michael Klimenko"],
    ),
    (
        "2012 Yavin 4 Regionals Bentley Boyd LS The Hyperdrive Generator's Gone",
        ["The Hyperdrive Generator's Gone", "Bentley Boyd"],
    ),
    (
        "2012 Yavin 4 Regionals Bentley Boyd DS Let Them Make The First Move",
        ["Let Them Make The First Move", "Bentley Boyd"],
    ),
    (
        "2012 Yavin 4 Regionals Tim Murray LS Rebel Strike Team (V)",
        ["Rebel Strike Team", "Tim Murray"],
    ),
    (
        "2012 Yavin 4 Regionals Tim Murray DS Let Them Make The First Move",
        ["Let Them Make The First Move", "Tim Murray"],
    ),
    (
        "2012 Yavin 4 Regionals",
        ["Chris Westergard", "Scott", "Steve Skilton", "Vincent Rossi", "Joe Orthner", "Matt Schmaltz", "Alex Klimenko", "Ben Brummett", "Tom Haid", "Greg Shaw", "Vikram Bali", "Michael Klimenko", "Bentley Boyd", "Tim Murray", "2012"],
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
    hub = [c for c in CHECKS if c[0] == "2012 Yavin 4 Regionals"]
    decks = [c for c in CHECKS if c[0] != "2012 Yavin 4 Regionals"]
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
