#!/usr/bin/env python3
"""Live QA for 2013 MPC seven-player leftover."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship Day 1 Mike D'Ambrosio DS Contract Killers",
    "2013 Match Play Championship Day 1 Mike D'Ambrosio LS Communing",
    "2013 Match Play Championship Day 1 Scott Lingrell DS Agents Of Black Sun",
    "2013 Match Play Championship Day 1 Scott Lingrell LS Hidden Base (V)",
    "2013 Match Play Championship Day 1 Nick Reisch DS Set Your Course For Alderaan",
    "2013 Match Play Championship Day 1 Nick Reisch LS Let The Wookiee Win (V)",
    "2013 Match Play Championship Day 1 Greg Shaw DS Hunt Down And Destroy The Jedi (V)",
    "2013 Match Play Championship Day 1 Greg Shaw LS There Is Good In Him",
    "2013 Match Play Championship Day 1 Peter Tenneson DS Ralltiir Operations",
    "2013 Match Play Championship Day 1 Peter Tenneson LS Anger, Fear, Aggression (V)",
    "2013 Match Play Championship Day 1 Michael Thomas DS Invasion",
    "2013 Match Play Championship Day 1 Michael Thomas LS Local Uprising (V)",
    "2013 Match Play Championship Day 1 John Veasey DS A Stunning Move",
    "2013 Match Play Championship Day 1 John Veasey LS Communing",
    "2013 Match Play Championship",
    "Mike D'Ambrosio",
    "Scott Lingrell",
    "Nick Reisch",
    "Greg Shaw",
    "Peter Tenneson",
    "Michael Thomas",
    "John Veasey",
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
                "Mike D'Ambrosio",
                "Scott Lingrell",
                "Nick Reisch",
                "Greg Shaw",
                "Peter Tenneson",
                "Michael Thomas",
                "John Veasey",
            ):
                if f"[[{name}]]" not in text:
                    got.append(f"HUB_MISSING_{name}")
        dest_needles = {
            "D'Ambrosio DS Contract Killers": [
                "Contract Killers / Feared Throughout The Galaxy",
                "Tatooine: Jabba's Palace",
                "Jodo Kast",
                "Nevar Yalnal",
                "Coruscant: Private Platform (Docking Bay)",
            ],
            "D'Ambrosio LS Communing": [
                "[[Communing (Virtual Block 7)|Communing]]",
                "Lady Luck",
                "Luke With Lightsaber",
                "Anger, Fear, Aggression (V)",
            ],
            "Lingrell DS Agents Of Black Sun": [
                "Agents Of Black Sun / Vengeance Of The Dark Prince",
                "Prophetess (V)",
                "Mist Hunter (V)",
                "Kitik Keed'kak",
            ],
            "Lingrell LS Hidden Base (V)": [
                "Hidden Base (V) / Systems Will Slip Through Your Fingers (V)",
                "Officer Dolphe",
                "Are You Brain Dead?!",
                "I Don't Need Their Scum, Either (V)",
            ],
            "Reisch DS Set Your Course For Alderaan": [
                "Set Your Course For Alderaan / The Ultimate Power In The Universe",
                "Commence Primary Ignition (V)",
            ],
            "Reisch LS Let The Wookiee Win (V)": [
                "Let The Wookiee Win (V)",
                "Tarfful, Wookiee Insurgent",
                "Grrrghrrrgh!",
            ],
            "Shaw DS Hunt Down And Destroy The Jedi (V)": [
                "Dengar With Blaster Carbine",
                "Rogue Shadow",
                "Juno Eclipse, Black Leader",
                "General Nevar",
                "Garindan (V)",
            ],
            "Shaw LS There Is Good In Him": [
                "There Is Good In Him / I Can Save Him",
            ],
            "Tenneson DS Ralltiir Operations": [
                "Ralltiir Operations / In The Hands Of The Empire",
                "Kir Kanos With Force Pike",
                "Maarek Stele, The Emperor's Reach",
                "Ysanne Isard",
            ],
            "Tenneson LS Anger, Fear, Aggression (V)": [
                "Yavin 4: Massassi Throne Room",
                "Armed And Dangerous & •Krayt Dragon Howl",
            ],
            "Thomas DS Invasion": [
                "Invasion / In Complete Control",
                "Master, Destroyers!",
                "3,720 To 1 (V)",
            ],
            "Thomas LS Local Uprising (V)": [
                "Local Uprising (V) / Liberation (V)",
                "Wedge Antilles, Red Squadron Leader",
            ],
            "Veasey DS A Stunning Move": [
                "A Stunning Move / A Valuable Hostage",
                "Grievous, Hunter Of Jedi",
                "He Is Not Ready",
            ],
            "Veasey LS Communing": [
                "Lady Luck",
                "Anakin Skywalker, Padawan Learner",
            ],
        }
        for suffix, needles in dest_needles.items():
            if t.endswith(suffix) or suffix in t:
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
