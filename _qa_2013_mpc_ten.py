#!/usr/bin/env python3
"""Live QA for 2013 MPC ten-player leftover."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship Day 1 Matt Fink DS Cloud City: Security Tower (V)",
    "2013 Match Play Championship Day 1 Matt Fink LS Communing",
    "2013 Match Play Championship Day 1 Aaron Kinser DS Imperial Occupation (V)",
    "2013 Match Play Championship Day 1 Aaron Kinser LS Local Uprising (V)",
    "2013 Match Play Championship Day 1 Tuan Le DS A Stunning Move",
    "2013 Match Play Championship Day 1 Tuan Le LS You Can Either Profit By This...",
    "2013 Match Play Championship Day 1 Josh Mack DS Kessel",
    "2013 Match Play Championship Day 1 Josh Mack LS Watch Your Step",
    "2013 Match Play Championship Day 1 Aaron Nelson DS Imperial Occupation (V)",
    "2013 Match Play Championship Day 1 Aaron Nelson LS Plead My Case To The Senate",
    "2013 Match Play Championship Day 1 Cuong Nguyen DS Carbon Chamber Testing",
    "2013 Match Play Championship Day 1 Cuong Nguyen LS Watch Your Step (V)",
    "2013 Match Play Championship Day 1 Chris O'Hara DS Kessel",
    "2013 Match Play Championship Day 1 Chris O'Hara LS Yavin 4: Massassi Throne Room",
    "2013 Match Play Championship Day 1 Matt Paragano DS On The Hunt",
    "2013 Match Play Championship Day 1 Matt Paragano LS Leia, Rebel Princess",
    "2013 Match Play Championship Day 1 Mike Richards DS Kessel: Spice Mines - Administrator's Office",
    "2013 Match Play Championship Day 1 Mike Richards LS Mind What You Have Learned (V)",
    "2013 Match Play Championship Day 1 Rustin Sharer DS Contract Killers",
    "2013 Match Play Championship Day 1 Rustin Sharer LS We'll Handle This (V)",
    "2013 Match Play Championship",
    "Matt Fink",
    "Aaron Kinser",
    "Tuan Le",
    "Josh Mack",
    "Aaron Nelson",
    "Cuong Nguyen",
    "Chris O'Hara",
    "Matt Paragano",
    "Mike Richards",
    "Rustin Sharer",
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def section(text: str, heading: str) -> str:
    m = re.search(
        r"'''" + re.escape(heading) + r"'''(.*?)(?:'''|\|})",
        text,
        re.S,
    )
    return m.group(1) if m else ""


def main() -> int:
    n = 0
    for t in TITLES:
        data = api(
            {
                "action": "query",
                "format": "json",
                "prop": "info|flagged|revisions",
                "rvprop": "ids|content",
                "rvslots": "main",
                "titles": t,
            }
        )
        page = next(iter(data["query"]["pages"].values()))
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        text = ""
        revs = page.get("revisions") or []
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        got: list[str] = []
        if "missing" in page:
            got.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            got.append(f"UNSTABLE stable={stable} latest={latest}")
        if t.startswith("2013 Match Play Championship Day 1"):
            if '{| style="margin:0 auto;border:0' not in text:
                got.append("MISSING_SCAN_TABLE")
            if "|center|" in text:
                got.append("CENTER_SCAN")
            if "|800px]]" not in text:
                got.append("MISSING_800PX")
            if "[[:File:2013 Match Play Championship.pdf]]" not in text:
                got.append("MISSING_CITE")
            if "Anger, Fear, Aggression (V)" in text:
                effect = section(text, "Effect")
                interrupt = section(text, "Interrupt")
                if "Anger, Fear, Aggression (V)" not in effect:
                    got.append("AFA_V_NOT_EFFECT")
                if "Anger, Fear, Aggression (V)" in interrupt:
                    got.append("AFA_V_IN_INTERRUPT")
        if t == "2013 Match Play Championship":
            for name in (
                "Matt Fink",
                "Aaron Kinser",
                "Tuan Le",
                "Josh Mack",
                "Aaron Nelson",
                "Cuong Nguyen",
                "Chris O'Hara",
                "Matt Paragano",
                "Mike Richards",
                "Rustin Sharer",
            ):
                if f"[[{name}]]" not in text:
                    got.append(f"HUB_MISSING_{name}")
        dest_needles = {
            "Fink LS Communing": ["Communing", "Anakin Skywalker, Padawan Learner"],
            "Fink DS Cloud City: Security Tower (V)": [
                "Cloud City: Security Tower",
                "Grievous, Hunter Of Jedi",
                "Jango Fett, The Assassin",
            ],
            "Kinser LS Local Uprising (V)": ["Local Uprising (V) / Liberation (V)"],
            "Kinser DS Imperial Occupation (V)": [
                "Imperial Occupation (V) / Imperial Control (V)",
                "Jango Fett, The Assassin",
            ],
            "Tuan Le DS A Stunning Move": [
                "A Stunning Move / A Valuable Hostage",
                "Grievous, Hunter Of Jedi",
                "Grievous' Lightsabers",
            ],
            "Tuan Le LS You Can Either Profit By This...": [
                "You Can Either Profit By This... / Or Be Destroyed",
                "Lady Luck",
                "Shmi Skywalker",
            ],
            "Mack LS Watch Your Step": [
                "Watch Your Step / This Place Can Be A Little Rough"
            ],
            "Nelson LS Plead My Case To The Senate": [
                "Plead My Case To The Senate / Senators In Laager"
            ],
            "Nelson DS Imperial Occupation (V)": [
                "Imperial Occupation (V) / Imperial Control (V)"
            ],
            "Nguyen DS Carbon Chamber Testing": [
                "Carbon Chamber Testing / My Favorite Decoration"
            ],
            "Nguyen LS Watch Your Step (V)": [
                "Watch Your Step (V) / This Place Can Be A Little Rough (V)"
            ],
            "O'Hara LS Yavin 4: Massassi Throne Room": [
                "Yavin 4: Massassi Throne Room",
                "Qui-Gon Jinn With Lightsaber",
            ],
            "Paragano DS On The Hunt": [
                "On The Hunt",
                "Jango Fett, The Assassin",
            ],
            "Richards LS Mind What You Have Learned (V)": [
                "Mind What You Have Learned (V) / Save You It Can (V)",
                "Anger, Fear, Aggression (V)",
            ],
            "Richards DS Kessel: Spice Mines - Administrator's Office": [
                "Kessel: Spice Mines - Administrator's Office",
                "Combat Response",
            ],
            "Sharer LS We'll Handle This (V)": [
                "We'll Handle This (V) / Duel Of The Fates (V)"
            ],
            "Sharer DS Contract Killers": [
                "Contract Killers / Feared Throughout The Galaxy",
                "Mist Hunter (V)",
            ],
        }
        for suffix, needles in dest_needles.items():
            if suffix in t:
                for needle in needles:
                    if needle not in text:
                        got.append(f"MISSING_{needle}")
        if got:
            n += 1
            print("FAIL", t, got)
        else:
            print("OK", t)
    print("TOTAL", n)
    return n


if __name__ == "__main__":
    raise SystemExit(main())
