#!/usr/bin/env python3
"""Live parse-API QA for Decklists / DeckTech first ingest."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "Decklists",
        ["Decipher deck designs", "DeckTech decks", "Game Players Network"],
    ),
    (
        "DeckTech",
        [
            "3,923",
            "stephenskilton.com",
            "DeckTech decks",
            "decktech.net/starwarsccg/deck/26555",
            "/starwarsccg/deck/{id}",
        ],
    ),
    (
        "DeckTech decks",
        [
            "2002 World Championship Angelo Consoli DS",
            "No Money, No Parts, No Deal!",
            "2002 World Championship Greg Shaw Force Lightning is TECH",
            "Hunt Down And Destroy The Jedi",
            "2002 World Championship Greg Shaw DCon2k2 Runner Up - LS",
            "There Is Good In Him",
            "decktech.net/starwarsccg/deck/26555",
            "decktech.net/starwarsccg/deck/26297",
            "decktech.net/starwarsccg/deck/26204",
        ],
    ),
    (
        "DeckTech tournament reports",
        ["sokols-dcon-2000-reportd1327", "Yannick Lapointe"],
    ),
    (
        "2002 World Championship Greg Shaw Force Lightning is TECH",
        [
            "Hunt Down And Destroy The Jedi",
            "Prophetess (V) (Virtual Set 1)",
            "Hyperwave Scan (V) (Virtual Set 3)",
            "Molator (V) (Virtual Set 2)",
            "We Must Accelerate Our Plans",
            "Green 1",
            "Blue 7",
            "VS1O-12-Prophetess.png",
            "== Original post ==",
            "Force Lightning is TECH",
            "MAKE SURE YOU WRITE FORCE LIGHTNING",
            "decktech.net/starwarsccg/deck/26555",
            "mw-collapsed",
            "Published title",
            "==== WYS ====",
            "HDADTJ",
        ],
    ),
    (
        "2002 World Championship",
        [
            "Angelo Consoli",
            "Greg Shaw",
            "1–3 November 2002",
            "2002 World Championship Angelo Consoli DS",
            "No Money, No Parts, No Deal!",
            "2002 World Championship Greg Shaw Force Lightning is TECH",
            "2002 World Championship Greg Shaw DCon2k2 Runner Up - LS",
            "There Is Good In Him",
            "decktech.net/starwarsccg/deck/26555",
            "decktech.net/starwarsccg/deck/26297",
            "decktech.net/starwarsccg/deck/26204",
        ],
    ),
    ("DecipherCon 2002", ["Chesapeake Conference Center", "2002 World Championship"]),
    ("Main Page", ["Decklists", "== Decklists ==", "== Expansions =="]),
    (
        "Greg Shaw",
        [
            "2002 World Championship Greg Shaw Force Lightning is TECH",
            "2002 World Championship Greg Shaw DCon2k2 Runner Up - LS",
            "decktech.net/starwarsccg/deck/26555",
            "decktech.net/starwarsccg/deck/26204",
            "Premiere - Original VS3",
            "TychoCelchu",
            "TychoCelchu''')<ref",
        ],
    ),
    (
        "2002 World Championship Angelo Consoli DS",
        [
            "No Money, No Parts, No Deal!",
            "Ket Maliss (V) (Virtual Set 3)",
            "Reegesk (V) (Virtual Set 3)",
            "Prophetess (V) (Virtual Set 1)",
            "I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)",
            "Reactor Terminal (V) (Virtual Set 3)",
            "Executor (Dark)",
            "We Must Accelerate Our Plans",
            "VS3O-38-Ket_Maliss.png",
            "Held by Fear Is My Ally",
            "== Original post ==",
            "Bastian Winkelhaus, for inventing this decktype",
            "Martin Falke, for Reegesk",
            "decktech.net/starwarsccg/deck/26297",
            "mw-collapsed",
            "==== Props to ====",
            "<nowiki>*g*</nowiki>",
        ],
    ),
    (
        "2002 World Championship Greg Shaw DCon2k2 Runner Up - LS",
        [
            "There Is Good In Him",
            "Tawss Khaa",
            "Orrimaarko",
            "Merc Sunlet",
            "Honor Of The Jedi",
            "Goo Nee Tay",
            "Sorry About The Mess & Blaster Proficiency",
            "== Original post ==",
            "DCon2k2 Runner Up - LS",
            "The beatdown tripler",
            "Lingrell Tech",
            "decktech.net/starwarsccg/deck/26204",
            "mw-collapsed",
            "Published title",
            "==== The Lingrell Tech ====",
        ],
    ),
    (
        "Angelo Consoli",
        [
            "2002 World Championship Angelo Consoli DS",
            "1–3 November 2002",
            "No Money, No Parts, No Deal!",
            "decktech.net/starwarsccg/deck/26297",
            "Premiere - Original VS3",
            "GravShadow",
            "GravShadow''')<ref",
        ],
    ),
]


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "format": "json",
            "page": title,
            "prop": "text|wikitext|displaytitle",
            "disablelimitreport": "1",
        }
    )
    req = urllib.request.Request(
        API + "?" + q, headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> None:
    failed = 0
    for title, needles in CHECKS:
        try:
            data = parse(title)
        except Exception as e:
            print("FAIL", title, "fetch", e)
            failed += 1
            continue
        if "error" in data:
            print("FAIL", title, data["error"])
            failed += 1
            continue
        p = data.get("parse") or {}
        html = (p.get("text") or {}).get("*") or ""
        wt = (p.get("wikitext") or {}).get("*") or ""
        blob = html + "\n" + wt
        missing = [n for n in needles if n not in blob]
        errs = []
        if "class=\"error\"" in html or "Parser error" in html:
            errs.append("parser-error")
        if missing:
            errs.append("missing:" + ",".join(missing))
        if "Fear Is My Ally" in title:
            pass
        if title == "Main Page":
            d = wt.find("== Decklists ==")
            e = wt.find("== Expansions ==")
            if d < 0 or e < 0 or d > e:
                errs.append("Decklists section not above Expansions")
        if title in ("Greg Shaw", "Angelo Consoli"):
            if "Premiere - Theed Palace]] + [[Virtual Set 3" in wt:
                errs.append("compound 2002 format cell")
        if title == "2002 World Championship Greg Shaw Force Lightning is TECH":
            if "V21-D-hyperwavescan" in blob:
                errs.append("current-virtual Hyperwave art")
            if "VB1-D-prophetess" in blob:
                errs.append("Virtual Block Prophetess art")
            if "VB1-D-molator" in blob:
                errs.append("Virtual Block Molator art")
            if "GEMP Importable" in blob:
                errs.append("GEMP Download on incomplete 60")
            if "== Original post ==" not in wt:
                errs.append("missing original post")
            if "mw-collapsed" not in wt:
                errs.append("original card list not collapsed")
            if "          Author:" in wt:
                errs.append("old nowiki dump still on original post")
        if title == "2002 World Championship Greg Shaw DCon2k2 Runner Up - LS":
            if "GEMP Importable" in blob:
                errs.append("GEMP Download on incomplete 60")
            if "== Original post ==" not in wt:
                errs.append("missing original post")
            if "mw-collapsed" not in wt:
                errs.append("original card list not collapsed")
            if "          Author:" in wt:
                errs.append("old nowiki dump still on original post")
        if title == "2002 World Championship Angelo Consoli DS":
            if "VB1-D-ketmaliss" in blob:
                errs.append("Virtual Block Ket Maliss art")
            if "VB1-D-reegesk" in blob:
                errs.append("Virtual Block Reegesk art")
            if "VB1-D-prophetess" in blob:
                errs.append("Virtual Block Prophetess art")
            if "VSh-D-ifindyourlackoffaith" in blob:
                errs.append("Virtual Shields Lack Of Faith art")
            if "VSh-D-reactorterminal" in blob:
                errs.append("Virtual Shields Reactor Terminal art")
            if "GEMP Importable" in blob:
                errs.append("GEMP Download on original-VS 60")
            if "== Original post ==" not in wt:
                errs.append("missing original post")
            if "mw-collapsed" not in wt:
                errs.append("original card list not collapsed")
            if "          Author:" in wt:
                errs.append("old nowiki dump still on original post")
            dt = p.get("displaytitle") or ""
            lead = wt.split("\n", 1)[0]
            if any(s in dt or s in lead for s in ("Fresse", "D1ck")):
                errs.append("vulgar published title on dest title")
        if errs:
            print("FAIL", title, "; ".join(errs))
            failed += 1
        else:
            print("OK", title)
    print("TOTAL", failed)


if __name__ == "__main__":
    main()
