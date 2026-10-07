#!/usr/bin/env python3
"""Live QA for 2012 Texas Mini Worlds leftover Xerox dests.

python _qa_2012_tmw_xerox.py --delta   # last pair + hub
python _qa_2012_tmw_xerox.py --full    # every CHECK (default)
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2012 Texas Mini Worlds Day 1 Mike Richards LS Yavin 4 (V)",
        ["Yavin 4", "Restore Freedom To The Galaxy", "Anger, Fear, Aggression", "Mike Richards"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Mike Richards DS Invasion",
        ["Invasion / In Complete Control", "Darth Maul", "Knowledge And Defense", "Mike Richards"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Brian Herold LS Hidden Base (V)",
        ["Hidden Base", "Mon Calamari Star Cruiser", "Anger, Fear, Aggression", "Brian Herold"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Brian Herold DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Grievous, Hunter Of Jedi", "Knowledge And Defense", "Brian Herold"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Scott Lingrell LS Hidden Base (V)",
        ["Hidden Base", "Bravo 1", "Anger, Fear, Aggression", "Scott Lingrell"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Scott Lingrell DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Trophy Of A Kill", "Knowledge And Defense", "Scott Lingrell"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Greg Shaw LS Watch Your Step (V)",
        ["Watch Your Step", "Millennium Falcon", "Anger, Fear, Aggression", "Greg Shaw"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Greg Shaw DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Grievous, Hunter Of Jedi", "Knowledge And Defense", "Greg Shaw"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 James Barnes LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Coruscant: Jedi Council Chamber", "James Barnes"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 James Barnes DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Death Star", "Knowledge And Defense", "James Barnes"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Robbie Hendon LS Communing",
        ["Communing", "Tatooine: Slave Quarters", "Anger, Fear, Aggression", "Robbie Hendon"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Robbie Hendon DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Robbie Hendon"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 John Anderson LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Heading For The Medical Frigate", "Anger, Fear, Aggression", "John Anderson"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 John Anderson DS A Stunning Move",
        ["A Stunning Move", "Knowledge And Defense", "John Anderson"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Matt Lush LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Yavin 4: Massassi Throne Room", "Matt Lush"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Matt Lush DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Matt Lush"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Nick Reisch LS Communing",
        ["Communing", "Anger, Fear, Aggression", "Tatooine: Slave Quarters", "Nick Reisch"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Nick Reisch DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Nick Reisch"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Evan Kirkpatrick LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Tatooine: Slave Quarters", "Communing", "Evan Kirkpatrick"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Evan Kirkpatrick DS A Stunning Move",
        ["A Stunning Move", "Knowledge And Defense", "Evan Kirkpatrick"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 John Veasey LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Kashyyyk", "John Veasey"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 John Veasey DS A Stunning Move",
        ["A Stunning Move", "Knowledge And Defense", "John Veasey"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Amar Banger LS You Can Either Profit By This",
        ["You Can Either Profit By This", "Anger, Fear, Aggression", "Amar Banger"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Amar Banger DS Court Of The Vile Gangster",
        ["Court Of The Vile Gangster", "Knowledge And Defense", "Amar Banger"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Steve Skilton LS Let The Wookiee Win (V)",
        ["Let The Wookiee Win", "Yavin 4: Massassi Throne Room", "Steve Skilton"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Steve Skilton DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Steve Skilton"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Jeremy Gardner LS Watch Your Step (V)",
        ["Watch Your Step", "Anger, Fear, Aggression", "Jeremy Gardner"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Jeremy Gardner DS Imperial Entanglements",
        ["Imperial Entanglements", "Knowledge And Defense", "Jeremy Gardner"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Charley Joe LS You Can Either Profit By This",
        ["You Can Either Profit By This", "Anger, Fear, Aggression", "Charley Joe"],
    ),
    (
        "2012 Texas Mini Worlds Day 1 Charley Joe DS Court Of The Vile Gangster",
        ["Court Of The Vile Gangster", "Knowledge And Defense", "Charley Joe"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Mike Richards LS Hidden Base (V)",
        ["Hidden Base", "Anger, Fear, Aggression", "Mike Richards"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Mike Richards DS Kessel",
        ["Kessel", "Knowledge And Defense", "Mike Richards"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Scott Lingrell LS You Can Either Profit By This",
        ["You Can Either Profit By This", "Anger, Fear, Aggression", "Scott Lingrell"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Scott Lingrell DS Court Of The Vile Gangster",
        ["Court Of The Vile Gangster", "Knowledge And Defense", "Scott Lingrell"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Brian Herold LS Hidden Base (V)",
        ["Hidden Base", "Anger, Fear, Aggression", "Brian Herold"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Brian Herold DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Knowledge And Defense", "Brian Herold"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 James Barnes LS Center Of Tyranny",
        ["Center Of Tyranny", "Anger, Fear, Aggression", "James Barnes"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 James Barnes DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "James Barnes"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Greg Shaw LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Anger, Fear, Aggression", "Greg Shaw"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Greg Shaw DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "First Strike", "Greg Shaw"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Robbie Hendon LS Watch Your Step (V)",
        ["Watch Your Step", "Anger, Fear, Aggression", "Robbie Hendon"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Robbie Hendon DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Knowledge And Defense", "Robbie Hendon"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 John Anderson LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Anger, Fear, Aggression", "John Anderson"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 John Anderson DS Endor Operations",
        ["Endor Operations", "Knowledge And Defense", "John Anderson"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Matt Lush LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Yavin 4: Massassi Throne Room", "Matt Lush"],
    ),
    (
        "2012 Texas Mini Worlds Day 2 Matt Lush DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Matt Lush"],
    ),
    (
        "2012 Texas Mini Worlds",
        ["Mike Richards", "Brian Herold", "Scott Lingrell", "Greg Shaw", "James Barnes", "Robbie Hendon", "John Anderson", "Matt Lush", "Nick Reisch", "Evan Kirkpatrick", "John Veasey", "Amar Banger", "Steve Skilton", "Jeremy Gardner", "Charley Joe", "27–29 April 2012"],
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
    hub = [c for c in CHECKS if c[0] == "2012 Texas Mini Worlds"]
    decks = [c for c in CHECKS if c[0] != "2012 Texas Mini Worlds"]
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
