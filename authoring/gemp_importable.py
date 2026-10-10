#!/usr/bin/env python3
"""Wiki / title lists → GEMP-importable deck XML (.txt).

GEMP Deck Builder Import uses the filename (minus .txt) as the saved deck name.
PC GEMP caps that name at 40 characters. Sites are horizontal=true; systems are not.

Usage (cwd wiki/):
  python gemp_importable.py --from-wiki pages/1996_Decipher_World_Championship_Joe_Alread_LS.wiki
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
GEMP_ROOT = ROOT.parent
CARD_DB = (
    GEMP_ROOT
    / "src"
    / "gemp-swccg-cards"
    / "src"
    / "main"
    / "resources"
    / "card_blueprint_database.json"
)
FORMATS_JSON = (
    GEMP_ROOT
    / "src"
    / "gemp-swccg-server"
    / "src"
    / "main"
    / "resources"
    / "swccgFormats.json"
)

# Cloud / repo-only runs: fall back to snapshots in authoring/gemp-data/.
if not CARD_DB.exists():
    CARD_DB = ROOT / "gemp-data" / "card_blueprint_database.json"
if not FORMATS_JSON.exists():
    FORMATS_JSON = ROOT / "gemp-data" / "swccgFormats.json"

# Suggested filename tokens. Keep ASCII. PC GEMP import name = filename, max 40.
FORMAT_ABBR = {
    "Premiere - A New Hope": "PANH",
    "premiere_anh": "PANH",
    "Premiere - Hoth": "PHoth",
    "premiere_hoth": "PHoth",
    "Premiere - Cloud City": "PCC",
    "premiere_cc": "PCC",
    "Premiere - Special Edition": "PSE",
    "premiere_se": "PSE",
    "Premiere - Endor": "PEndor",
    "premiere_endor": "PEndor",
    "Premiere - Death Star II": "PDS2",
    "premiere_ds2": "PDS2",
    "Premiere - Reflections II": "PR2",
    "premiere_ref2": "PR2",
    "Premiere - Reflections III": "PR3",
    "premiere_reflections3": "PR3",
    "Premiere - Coruscant": "PCor",
    "Premiere - Theed Palace": "PTheed",
    "open_no_virtual": "DCO",
    "Decipher Cards Only": "DCO",
    "Premiere - Dagobah": "PDag",
    "premiere_dagobah": "PDag",
    "Premiere - Jabba's Palace": "PJP",
    "premiere_jp": "PJP",
    "Premiere - Tatooine": "PTat",
    "premiere_tatooine": "PTat",
    "Premiere - Original VS1": "POVS1",
    "Premiere - Original VS2": "POVS2",
    "Premiere - Original VS3": "POVS3",
    "Premiere - Original VS4": "POVS4",
    "Premiere - Original VS5": "POVS5",
    "Premiere - Original VS6": "POVS6",
    "Premiere - Original VS7": "POVS7",
    "Premiere": "Prem",
    "premiere": "Prem",
    "Open": "Open",
    "open": "Open",
    "Legacy Open": "Legacy",
    "Anything Goes": "AG",
}

ARCHETYPE_ABBR = {
    "Throne Room Mains": "TRM",
    "Yavin 4: Massassi Throne Room": "TRM",
    "Revolution": "Revolut",
    "Dark Maneuvers": "DarkMan",
    "Mains": "Mains",
    "Mains & Toys": "MnT",
    "Death Star": "DeathStar",
    "Ralltiir Operations": "ROps",
    "Endor Operations": "EOps",
    "Hidden Base": "HB",
    "Watch Your Step": "WYS",
    "Quiet Mining Colony": "QMC",
    "Hunt Down And Destroy The Jedi": "HD",
    "You Can Either Profit By This… Or Be Destroyed": "Profit",
    "You Can Either Profit By This... Or Be Destroyed": "Profit",
    "You Can Either Profit By This...": "Profit",
    "Start Your Engines!": "Engines",
    "Quiet Mining Colony": "QMC",
    "Hoth: Echo Command Center (War Room)": "ECC",
    "Tatooine: Desert Landing Site": "DLS",
    "Agents In The Court": "Court",
    "My Kind Of Scum": "MKOS",
    "We'll Handle This": "WHT",
    "Let Them Make The First Move": "FirstMove",
    "Carbon Chamber Testing": "CCT",
    "Bring Him Before Me": "BHBM",
    "This Deal Is Getting Worse All The Time": "Deal",
    "Court Of The Vile Gangster": "Vile",
    "Rebel Strike Team": "RST",
    "No Money, No Parts, No Deal!": "NMNPND",
    "Plead My Case To The Senate": "Senate",
    "Echo Base Operations": "EBO",
    "Agents Of Black Sun": "AOBS",
    "My Kind Of Scum": "MKOS",
    "Endor Operations": "EOps",
    "Lightsaber Combat": "FirstMove",
    "My Kind Of Scum": "MKOS",
    "My Lord, Is That Legal?": "Legal",
    "Lightsaber Combat": "Saber",
    "Agents Of Black Sun": "AOBS",
    "ISB Operations": "ISB",
    "Hunt Down": "HD",
    "Hunt Down And Destroy The Jedi": "HD",
    "Rescue The Princess": "RTP",
    "Rescue The Princess / Sometimes I Amaze Even Myself": "RTP",
    "Local Uprising": "LU",
    "Operatives": "Ops",
    "Operatives / Speeders": "OpsSpd",
    "Imperial Occupation": "IOcc",
    "Hoth: Main Power Generators (1st Marker)": "MPG",
    "Death Star: Docking Bay 327": "DSDB",
    "Tatooine: Jabba's Palace": "TatJP",
    "Cloud City": "CC",
    "Bespin: Cloud City": "CC",
    "Death Star II: Throne Room": "DS2TR",
    "Yavin 4": "Y4",
    "Dagobah turtle": "Turtle",
    "Dagobah Miner's Guild": "Miner",
    "Dagobah manipulator": "Manip",
    "Mind What You Have Learned": "MWYHL",
    "Tatooine: Obi-Wan's Hut": "OWHut",
    "Endor: Chief Chirpa's Hut": "Chirpa",
    "Defender of Tatooine": "DefTat",
    "T-16 Swarm V1.0": "T16",
    "Bring Him Before Me": "BHBM",
    "Set Your Course For Alderaan": "SYCFA",
    "There Is Good In Him": "TIGIH",
    "Echo Base Operations": "EBO",
    "Watch Your Step": "WYS",
}

PC_NAME_MAX = 40
LINE_RE = re.compile(
    r"^\*?\s*(\d+)x\s*(?:"
    r"\{\{CardLink\|([^}|]+)\|[^}|]+(?:\|label=[^}]+)?\}\}"
    r"|\[\[([^\]|]+)(?:\|[^\]]+)?\]\]"
    r"|(.+?))\s*$",
    re.M,
)
INFO_RE = re.compile(
    r"^\*\s*'''(Player|Event|Format|Side|Starting Card|Strategy):'''\s*(.+)$",
    re.M,
)

_CARDS: list[dict] | None = None
_FORMATS: dict[str, set[int]] | None = None


def load_cards() -> list[dict]:
    global _CARDS
    if _CARDS is None:
        _CARDS = json.loads(CARD_DB.read_text(encoding="utf-8"))
    return _CARDS


def load_format_sets() -> dict[str, set[int]]:
    global _FORMATS
    if _FORMATS is None:
        out: dict[str, set[int]] = {}
        for row in json.loads(FORMATS_JSON.read_text(encoding="utf-8")):
            code = row.get("code")
            sets = row.get("set")
            if code and sets:
                out[code] = set(sets)
                name = row.get("name")
                if name:
                    out[name] = set(sets)
        _FORMATS = out
    return _FORMATS


def ascii_name(text: str) -> str:
    n = unicodedata.normalize("NFKD", text)
    return "".join(c for c in n if not unicodedata.combining(c)).replace("ø", "o").replace("Ø", "O")


def last_name(player: str) -> str:
    player = ascii_name(player).strip()
    parts = [p for p in re.split(r"\s+", player) if p]
    return parts[-1] if parts else player


def archetype_from_info(info: dict[str, str]) -> str:
    strat = (info.get("Strategy") or "").strip()
    if strat:
        return strat
    start = info.get("Starting Card") or ""
    if "Massassi Throne Room" in start:
        return "Throne Room Mains"
    if start:
        return start
    return "Deck"


def safe_deck_filename(name: str) -> str:
    """PC import uses the filename. Strip characters Windows / MediaWiki File: reject."""
    name = re.sub(r'[<>:"/\\|?*#\[\]{}]', "", name)
    return re.sub(r"\s+", " ", name).strip()


def deck_name(
    format_name: str,
    archetype: str,
    player: str,
    side: str,
    year: str | int | None,
    event: str,
    max_len: int = PC_NAME_MAX,
) -> str:
    fmt = FORMAT_ABBR.get(format_name, format_name)
    arch = ARCHETYPE_ABBR.get(archetype, archetype)
    who = last_name(player)
    sd = side.upper()
    if sd in {"LIGHT", "L"}:
        sd = "LS"
    elif sd in {"DARK", "D"}:
        sd = "DS"
    year_s = "" if year in (None, "") else str(year)
    tokens = [fmt, arch, who, sd, year_s, event]
    tokens = [t for t in tokens if t]
    name = " ".join(tokens)
    if len(name) <= max_len:
        return name
    drop = [event, year_s]
    for d in drop:
        if d in tokens:
            tokens.remove(d)
            name = " ".join(tokens)
            if len(name) <= max_len:
                return name
    return name[:max_len].rstrip()


def parse_info(text: str) -> dict[str, str]:
    info: dict[str, str] = {}
    for m in INFO_RE.finditer(text):
        val = m.group(2).strip()
        val = re.sub(
            r"\{\{CardLink\|([^}|]+)\|[^}|]+(?:\|label=[^}]+)?\}\}",
            r"\1",
            val,
        )
        val = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", val).strip()
        info[m.group(1)] = val
    return info


def parse_wiki_cards(text: str) -> list[tuple[int, str, str | None]]:
    """Return (qty, dest_title, side_hint). side_hint is DARK when dest is Title (Dark)."""
    rows: list[tuple[int, str, str | None]] = []
    for m in LINE_RE.finditer(text):
        qty = int(m.group(1))
        dest = (m.group(2) or m.group(3) or m.group(4) or "").strip()
        dest = dest.split("  #")[0].strip()
        side_hint = None
        title = dest
        if dest.endswith(" (Dark)"):
            title = dest[: -len(" (Dark)")]
            side_hint = "DARK"
        if title:
            rows.append((qty, title, side_hint))
    return rows


def set_num(card_id: str) -> int:
    return int(card_id.split("_", 1)[0])


def card_id_key(card_id: str) -> tuple:
    a, b = (card_id.split("_", 1) + ["0"])[:2]
    try:
        ai = int(a)
    except ValueError:
        ai = 0
    if b.isdigit():
        return (ai, 0, int(b))
    return (ai, 1, b)


def is_horizontal(card: dict) -> bool:
    subtype = (card.get("cardSubtype") or "").upper()
    return subtype == "SITE"


# Wiki dest / Decipher slang -> GEMP printed title when they differ.
TITLE_ALIAS = {
    "Short-range Fighters": "Short Range Fighters",
    "What Are You Trying To Push On Us?": "What're You Tryin' To Push On Us?",
    "What're you trying to push on us?": "What're You Tryin' To Push On Us?",
    "R2 in Red 5": "Artoo-Detoo In Red 5",
    "R2-D2 In Red 5": "Artoo-Detoo In Red 5",
    "Fall of the Legend": "Fall Of The Legend",
    "Come Here You Big Coward!": "Come Here You Big Coward",
    "Prepared Defense": "Prepared Defenses",
    "Home1: Docking Bay": "Home One: Docking Bay",
    "Leia with Blaster Rifle": "Leia With Blaster Rifle",
    "Obi-wan with Lightsaber": "Obi-Wan With Lightsaber",
    "Luke with Lightsaber": "Luke With Lightsaber",
    "Wege Antilles": "Wedge Antilles",
    "Do or Do Not": "Do, Or Do Not",
    "There'll be Hell to Pay": "There'll Be Hell To Pay",
    "Twilek Advisor": "Twi'lek Advisor",
    "You are Beaten": "You Are Beaten",
    "The Circle is Now Complete": "The Circle Is Now Complete",
    "Dreadnaught": "Dreadnaught-Class Heavy Cruiser",
    "Dreadnaught Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Dreadnaught-class Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Bossk in Hounds Tooth": "Bossk In Hound's Tooth",
    "Bossk In Hounds Tooth": "Bossk In Hound's Tooth",
    "Chimaer": "Chimaera",
    "Prfepared Defenses": "Prepared Defenses",
    "Lt. Pol Treidun": "Lt. Pol Treidum",
    "Jabba": "Jabba The Hutt",
    "Jabba the Hutt": "Jabba The Hutt",
    "Anger, Fear, Agression": "Anger, Fear, Aggression",
    "Orrimarko": "Orrimaarko",
    "ECC IG-88": "IG-88 With Riot Gun",
    "IG-88 with Riot Gun": "IG-88 With Riot Gun",
    "I'll Take the Leader": "I'll Take The Leader",
    "Kal Fal'nl C'ndros": "Kal'Falnl C'ndros",
    "Boba Fett in Slave 1": "Boba Fett In Slave I",
    "U-3PO": "U-3PO (Yoo-Threepio)",
    "How Did We Get Into This Mess": "How Did We Get Into This Mess?",
    "Cloud City: Docking Bay": "Cloud City: Platform 327 (Docking Bay)",
    "Endor: Docking Bay": "Endor: Landing Platform (Docking Bay)",
    "Blue Squadron B-wing": "Blue Squadron B-Wing",
    "Obi With Light Saber": "Obi-Wan With Lightsaber",
    "Obi with Light Saber": "Obi-Wan With Lightsaber",
    "Luke With Light Saber": "Luke With Lightsaber",
    "Luke with Light Saber": "Luke With Lightsaber",
    "Leia With Blaster": "Leia With Blaster Rifle",
    "Leia with Blaster": "Leia With Blaster Rifle",
    "Han With Blaster": "Han With Heavy Blaster Pistol",
    "Han with Blaster": "Han With Heavy Blaster Pistol",
    "Jeroen Web": "Jeroen Webb",
    "Do Or Do Not": "Do, Or Do Not",
    "Yarna da al Gargan": "Yarna d'al' Gargan",
    "Yarna d'al Gargan": "Yarna d'al' Gargan",
    "What Are You Trying To Push On Us": "What're You Tryin' To Push On Us?",
    "Wise Advise": "Wise Advice",
    "Grimtash": "Grimtaash",
    "Obi-Wans Lightsaber": "Obi-Wan's Lightsaber",
    "Obi-Wan's Lightsaber": "Obi-Wan's Lightsaber",
    "Millenium Falcon": "Millennium Falcon",
    "Bo Shek": "BoShek",
    "BoShek": "BoShek",
    "There Is Good In Him/I Can Save Him": "There Is Good In Him",
    "There Is Good In Him": "There Is Good In Him",
    "I Feel The Conflict": "I Feel The Conflict",
    "Yoda's Gimer Stick": "Yoda's Gimer Stick",
    "Anger, Fear, Aggression": "Anger, Fear, Aggression",
    "Insurrection (start)": "Insurrection",
    "Squadron Assignments (start)": "Squadron Assignments",
    "Wise Advice (start)": "Wise Advice",
    "X-Wing": "X-Wing",
    "All Wings Report In": "All Wings Report In",
    "Organized Attack": "Organized Attack",
    "Transmission Terminated": "Transmission Terminated",
    "The Planet It's Furthest From": "The Planet It's Furthest From",
    "Cloud City Celebration": "Cloud City Celebration",
    "Don't Forget The Droids": "Don't Forget The Droids",
    "Hijinx": "Houjix",
    "Hiujix": "Houjix",
    "Huijix": "Houjix",
    "Houjix": "Houjix",
    "Nabrun Leids": "Nabrun Leids",
    "Weapon Levitation": "Weapon Levitation",
    "Smoke Screen": "Smoke Screen",
    "Clash Of Sabers": "Clash Of Sabers",
    "Bothan Spy": "Bothan Spy",
    "Rebel Fleet": "Rebel Fleet",
    "Goo Nee Tay": "Goo Nee Tay",
    "Uncontrollable Fury": "Uncontrollable Fury",
    "Tawss Khaa": "Tawss Khaa",
    "Rayc Ryjerd": "Rayc Ryjerd",
    "Tantive IV": "Tantive IV",
    "Rendezvous Point": "Rendezvous Point",
    "Home One: Docking Bay": "Home One: Docking Bay",
    "Hoth: Echo Docking Bay": "Hoth: Echo Docking Bay",
    "Spaceport Docking Bay": "Spaceport Docking Bay",
    "Endor: Chief Chirpa's Hut": "Endor: Chief Chirpa's Hut",
    "Luke Skywalker, Jedi Knight": "Luke Skywalker, Jedi Knight",
    "Captain Han Solo": "Captain Han Solo",
    "Lieutenant Blount": "Lieutenant Blount",
    "R2-D2 (Artoo-Detoo)": "R2-D2 (Artoo-Detoo)",
    "Effective Repairs": "Effective Repairs",
    "Hyper Escape": "Hyper Escape",
    "It Could Be Worse": "It Could Be Worse",
    "Out Of Nowhere": "Out Of Nowhere",
    "Punch It!": "Punch It!",
    "Tunnel Vision": "Tunnel Vision",
    "A Few Maneuvers": "A Few Maneuvers",
    "Legendary Starfighter": "Legendary Starfighter",
    "Projection Of A Skywalker": "Projection Of A Skywalker",
    "Yoda's Hut": "Dagobah: Yoda's Hut",
    "Dagobah: Yoda's Hut": "Dagobah: Yoda's Hut",
    "Yavin IV: Massassi Throne Room": "Yavin 4: Massassi Throne Room",
    "Yavin IV: Massassi Headquarters": "Yavin 4: Massassi Headquarters",
    "Yavin IV: Massassi War Room": "Yavin 4: Massassi War Room",
    "Yavin IV": "Yavin 4",
    "Yavin4: Docking Bay": "Yavin 4: Docking Bay",
    "Jeroem Webb": "Jeroen Webb",
    "Commander Vanden Williard": "Commander Vanden Willard",
    "Run Luke Run": "Run Luke, Run!",
    "Obi-Wans Apparition": "Obi-Wan's Apparition",
    "Obi-Wan's Apparition": "Obi-Wan's Apparition",
    "Swing And A Miss": "Swing-And-A-Miss",
    "Gold Leader In Gold One": "Gold Leader In Gold 1",
    "Red Leader In Red One": "Red Leader In Red 1",
    "Narbun Leids": "Nabrun Leids",
    "Nar Shadda Wind Chimes": "Nar Shaddaa Wind Chimes",
    "Nar Shudda Wind Chimes": "Nar Shaddaa Wind Chimes",
    "Leia with Blaster Pistol": "Leia With Blaster Rifle",
    "Kal'Fal C'ndros": "Kal'Falnl C'ndros",
    "Kal'Faul Lndros": "Kal'Falnl C'ndros",
    "Bo'Shek": "BoShek",
    "Han with Han's Heavy Blaster": "Han With Heavy Blaster Pistol",
    "Tatooine: Toschi Station": "Tatooine: Tosche Station",
    "Yarna d'al Garnan": "Yarna d'al' Gargan",
    "Sic Six": "Sic-Six",
    "Rebel Speeder": "Rebel Snowspeeder",
    "It's A Trap": "It's A Trap!",
    "Executor: Holotheater": "Executor: Holotheatre",
    "Darth Vader Dark Lord Of The Sith": "Darth Vader, Dark Lord Of The Sith",
    "Miyoom Onith": "M'iiyoom Onith",
    "Miiyoom Onith": "M'iiyoom Onith",
    "Monnock": "Monnok",
    "Tatooine: Jabba's Palace Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Those Rebels Wont Escape Us": "Those Rebels Won't Escape Us",
    "Vaders Obsession": "Vader's Obsession",
    "Dreadnought-Class Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Dreadnaught Class Heavy Cruisers": "Dreadnaught-Class Heavy Cruiser",
    "Twi'ilek Advisor": "Twi'lek Advisor",
    "Raltiir Operations": "Ralltiir Operations",
    "Raltiir": "Ralltiir",
    "Tatooine: Lar's Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Sal'Ttorr Kal Fas": "Sai'torr Kal Fas",
    "Sal'Torr Kal Fas": "Sai'torr Kal Fas",
    "Anakin's Lightsabre": "Anakin's Lightsaber",
    "Jedi Lightsabre": "Jedi Lightsaber",
    "Jedi Lightsabres": "Jedi Lightsaber",
    "Dark Jedi Lightsabre": "Dark Jedi Lightsaber",
    "Obi's Lightsabre": "Obi-Wan's Lightsaber",
    "Obi's Lightsaber": "Obi-Wan's Lightsaber",
    "Lightsabre Proficiency": "Lightsaber Proficiency",
    "Lightsabre Profenciecy": "Lightsaber Proficiency",
    "Owen": "Owen Lars",
    "Beru": "Beru Lars",
    "Obi": "Obi-Wan Kenobi",
    "Falcon": "Millennium Falcon",
    "Red-1": "Red 1",
    "Luke X-34": "Luke's X-34 Landspeeder",
    "Dont Get Cocky": "Don't Get Cocky",
    "Tatooine: Obi's Hut": "Tatooine: Obi-Wan's Hut",
    "Yavin 4 Docking Bay": "Yavin 4: Docking Bay",
    "Corellian Corvettes": "Corellian Corvette",
    "F'igrin Dan": "Figrin D'an",
    "Bantha Droid": "WED-9-M1 'Bantha' Droid",
    "2X": "2X-3KPR (Tooex)",
    "Tatooine Utility Belt for +2 at night": "Tatooine Utility Belt",
    "Proton Torps": "Proton Torpedoes",
    "Hans Pistol": "Han's Heavy Blaster Pistol",
    "Leias Pistol": "Leia's Blaster Rifle",
    "Obis Cape": "Obi-Wan's Cape",
    "Warriors Courage": "Warrior's Courage",
    "Neibrum Leids": "Nabrun Leids",
    "Leias Back": "Leia's Back",
    "Lukes Back": "Luke's Back",
    "Obi Wan Kenobi": "Obi-Wan Kenobi",
    "Anakins Lightsaber": "Anakin's Lightsaber",
    "Anakin's Lightsaber": "Anakin's Lightsaber",
    "Lieutenant Greeve": "Lieutenant Greeve",
    "Do, Or Not Do!": "Do, Or Do Not",
    "Bossk In Hounds' Tooth": "Bossk In Hound's Tooth",
    "Bossk in Hound's Tooth": "Bossk In Hound's Tooth",
    "Star Destroyer: Launch Bar": "Star Destroyer: Launch Bay",
    "Star Destroyer:Launch Bar": "Star Destroyer: Launch Bay",
    "Imperial Class Star Destroyer": "Imperial-Class Star Destroyer",
    "Victory Class Star Destroyer": "Victory-Class Star Destroyer",
    "VictoryClass Star Destroyer": "Victory-Class Star Destroyer",
    "TIE Advanced": "TIE Advanced x1",
    "TIE Advx1": "TIE Advanced x1",
    "Tie Advancedx1": "TIE Advanced x1",
    "Tie AdvancedX1": "TIE Advanced x1",
    "Colonel Wulf Yularen": "Colonel Wullf Yularen",
    "Beseiged": "Besieged",
    "Lietenant Cabbel": "Lieutenant Cabbel",
    "Lt. Cabbel": "Lieutenant Cabbel",
    "Admial Motti": "Admiral Motti",
    "Adimiral Motti": "Admiral Motti",
    "Dr.Evazan": "Dr. Evazan",
    "Datcha": "Dathcha",
    "Djas Pur": "Djas Puhr",
    "Kashyyk": "Kashyyyk",
    "What're You Trying To Push On Us?": "What're You Tryin' To Push On Us?",
    "Tattoine System": "Tatooine",
    "Tatooine System": "Tatooine",
    "Dantooine System": "Dantooine",
    "Kessel System": "Kessel",
    "Death Star (starting)": "Death Star",
    "Death Star (Starting Location)": "Death Star",
    "Dagobah (starting)": "Dagobah",
    "Dagobah (starting location)": "Dagobah",
    "Tatooine: Jawa Camp(Starting)": "Tatooine: Jawa Camp",
    "Jabba's Palace: Audience Chamber (Starting)": "Jabba's Palace: Audience Chamber",
    "Ability, Ability, Ability (Starting)": "Ability, Ability, Ability",
    "Order to Engage": "Order To Engage",
    "Out of Nowhere": "Out Of Nowhere",
    "The Force is Strong With This One": "The Force Is Strong With This One",
    "You Have Failed Me For The Last Time": "You Have Failed Me For The Last Time",
    "Derek \"Hobbie\" Kilivan": "Derek 'Hobbie' Klivian",
    "Derek \"Hobbie\" Klivian": "Derek 'Hobbie' Klivian",
    "No Disintegration": "No Disintegrations!",
    "Do, Or Not Do!": "Do, Or Do Not",
    "Do Or Not Do": "Do, Or Do Not",
    "Kal'Faul Lndros": "Kal'Falnl C'ndros",
    "Obi Wan Kenobi": "Obi-Wan Kenobi",
    "Millenium Falcon": "Millennium Falcon",
    "Electrobinaculars": "Electrobinoculars",
    "Full Throtle": "Full Throttle",
    "Don't get Cocky": "Don't Get Cocky",
    "Return Of a Jedi": "Return Of A Jedi",
    "Lightsabre Proficiency": "Lightsaber Proficiency",
    "Noble Sacrifice x": "Noble Sacrifice",
    "Lt. Pol Tredium": "Lt. Pol Treidum",
    "Tatooine: Lars Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Tattoine Lars Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Tattoine Docking Bay 94": "Tatooine: Docking Bay 94",
    "Dark Jedi Presense": "Dark Jedi Presence",
    "I Have You Know": "I Have You Now",
    "Turboblaser Battery": "Turbolaser Battery",
    "The Empires Back": "The Empire's Back",
    "Ponda Boba": "Ponda Baba",
    "Imperial Star Destroyer": "Imperial-Class Star Destroyer",
    "Imperial Class Star Destroyers": "Imperial-Class Star Destroyer",
    "Devestator": "Devastator",
    "Ubrikian": "Ubrikkian 9000 Z001",
    "Ubrikkian": "Ubrikkian 9000 Z001",
    "Ubrikkian 9000-Z001": "Ubrikkian 9000 Z001",
    "Vader's Saber": "Vader's Lightsaber",
    "Boring Conversation": "Boring Conversation Anyway",
    "Jedi Presence": "Jedi Presence",
    "I've Lost Artoo": "I've Lost Artoo!",
    "Blaser Rifle": "Blaster Rifle",
    "LIN-V8M (mining droid)": "LIN-V8M (Elleyenin-Veeateemm)",
    "WED15-17\"Septoid\" Droid": "WED-15-17 'Septoid' Droid",
    "WED15-17 'Septoid' Droid": "WED-15-17 'Septoid' Droid",
    "WED15-17 \"Septoid\" Droid": "WED-15-17 'Septoid' Droid",
    "Death Star: Level 4 Military": "Death Star: Level 4 Military Corridor",
    "Scruffy Looking Nerf-Herder": "Scruffy-Looking Nerf Herder",
    "TIE Vangaurd": "TIE Vanguard",
    "Gallid": "Gailid",
    "Twi'lek Advisor x4 (Starting)": "Twi'lek Advisor",
    "Black2": "Black 2",
    "Black3": "Black 3",
    "Black4": "Black 4",
    "2 U-3PO": "U-3PO (Yoo-Threepio)",
    "2 Presence of the Force": "Presence Of The Force",
    "Well Guarded": "Well-Guarded",
    "Vader's Personal Shuttle": "Vader's Personal Shuttle",
    "Spaceport Prefects Office": "Spaceport Prefect's Office",
    "Sergeant Torrent": "Sergeant Torent",
    "In Hounds Tooth": "Bossk In Hound's Tooth",
    "Hidden Base/Systems Will Slip Through Your Fingers": "Hidden Base",
    "Imperial Occupation/Imperial Control": "Imperial Occupation",
    "Mind What You Have Learned": "Mind What You Have Learned",
    "Goo Nee Tay": "Goo Nee Tay",
    "Cloud City: Downtown Plaza": "Cloud City: Downtown Plaza",
    "All Wings Report In": "All Wings Report In",
    "What Are You Trying To Push On Us?": "What're You Tryin' To Push On Us?",
    "Cloud City Celebration": "Cloud City Celebration",
    "The Planet It's Furthest From": "The Planet It's Furthest From",
    "Bothan Spy": "Bothan Spy",
    "Tantive IV": "Tantive IV",
    "T-47 Battle Formation": "T-47 Battle Formation",
    "Nar Shaddaa Wind Chimes": "Nar Shaddaa Wind Chimes",
    "Owen Lars & Beru lars": "Owen Lars & Beru Lars",
    "Artoo & Threepio": "Artoo & Threepio",
}

# Scomp gempId for printed cards this worktree JSON still omits (GEMP 5_23 Frozen Assets).
MISSING_BLUEPRINTS = {
    ("LIGHT", "Frozen Assets"): {
        "cardId": "5_23",
        "title": "Frozen Assets",
        "cardSubtype": "EFFECT",
        "side": "LIGHT",
    },
    ("LIGHT", "Sabotage"): {
        "cardId": "2_56",
        "title": "Sabotage",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("DARK", "Navy Trooper Vesden"): {
        "cardId": "8_110",
        "title": "Navy Trooper Vesden",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "DARK",
    },
    ("DARK", "Informant"): {
        "cardId": "2_134",
        "title": "Informant",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "DARK",
    },
    ("DARK", "IG-88's Pulse Cannon"): {
        "cardId": "4_178",
        "title": "IG-88's Pulse Cannon",
        "cardSubtype": "WEAPON",
        "cardCategory": "WEAPON",
        "side": "DARK",
    },
    ("DARK", "Go For Help!"): {
        "cardId": "8_133",
        "title": "Go For Help!",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "DARK",
    },
    ("DARK", "3B3-21"): {
        "cardId": "14_71",
        "title": "3B3-21",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "DARK",
    },
    ("LIGHT", "Desperate Times"): {
        "cardId": "13_13",
        "title": "Desperate Times",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("LIGHT", "Armament Dismantled"): {
        "cardId": "13_7",
        "title": "Armament Dismantled",
        "cardSubtype": "EFFECT",
        "cardCategory": "EFFECT",
        "side": "LIGHT",
    },
    ("LIGHT", "Clinging To The Edge"): {
        "cardId": "13_10",
        "title": "Clinging To The Edge",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("DARK", "Heart Of The Chasm"): {
        "cardId": "5_143",
        "title": "Heart Of The Chasm",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "DARK",
    },
    ("LIGHT", "Astromech Translator"): {
        "cardId": "4_8",
        "title": "Astromech Translator",
        "cardSubtype": "DEVICE",
        "cardCategory": "DEVICE",
        "side": "LIGHT",
    },
    ("LIGHT", "Captain Yutani"): {
        "cardId": "8_1",
        "title": "Captain Yutani",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "LIGHT",
    },
    ("DARK", "The Ebb Of Battle"): {
        "cardId": "13_88",
        "title": "The Ebb Of Battle",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "DARK",
    },
    ("LIGHT", "Officer Ellberger"): {
        "cardId": "14_21",
        "title": "Officer Ellberger",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "LIGHT",
    },
    ("DARK", "Laser Gate"): {
        "cardId": "2_113",
        "title": "Laser Gate",
        "cardSubtype": "DEVICE",
        "cardCategory": "DEVICE",
        "side": "DARK",
    },
    ("DARK", "Precise Attack"): {
        "cardId": "1_265",
        "title": "Precise Attack",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "DARK",
    },
    ("LIGHT", "Ewok Rescue"): {
        "cardId": "8_49",
        "title": "Ewok Rescue",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("LIGHT", "Targeting Computer"): {
        "cardId": "1_39",
        "title": "Targeting Computer",
        "cardSubtype": "DEVICE",
        "cardCategory": "DEVICE",
        "side": "LIGHT",
    },
    ("LIGHT", "Medium Repeating Blaster Cannon"): {
        "cardId": "3_77",
        "title": "Medium Repeating Blaster Cannon",
        "cardSubtype": "WEAPON",
        "cardCategory": "WEAPON",
        "side": "LIGHT",
    },
    ("DARK", "E-web Blaster"): {
        "cardId": "3_159",
        "title": "E-web Blaster",
        "cardSubtype": "WEAPON",
        "cardCategory": "WEAPON",
        "side": "DARK",
    },
    ("LIGHT", "Lieutenant Greeve"): {
        "cardId": "8_18",
        "title": "Lieutenant Greeve",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "LIGHT",
    },
    ("DARK", "MSE-6 'Mouse' Droid"): {
        "cardId": "1_188",
        "title": "MSE-6 'Mouse' Droid",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "DARK",
    },
    ("LIGHT", "Through The Force Things You Will See"): {
        "cardId": "4_64",
        "title": "Through The Force Things You Will See",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("LIGHT", "Combined Attack"): {
        "cardId": "1_75",
        "title": "Combined Attack",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("LIGHT", "Innocent Scoundrel"): {
        "cardId": "5_53",
        "title": "Innocent Scoundrel",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("LIGHT", "Lost Relay"): {
        "cardId": "4_56",
        "title": "Lost Relay",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("LIGHT", "They'd Be Crazy To Follow Us"): {
        "cardId": "4_61",
        "title": "They'd Be Crazy To Follow Us",
        "cardSubtype": "INTERRUPT",
        "cardCategory": "INTERRUPT",
        "side": "LIGHT",
    },
    ("DARK", "Besieged"): {
        "cardId": "2_117",
        "title": "Besieged",
        "cardSubtype": "EFFECT",
        "cardCategory": "EFFECT",
        "side": "DARK",
    },
    ("DARK", "IM4-099 (Eyeemmfour)"): {
        "cardId": "7_181",
        "title": "IM4-099 (Eyeemmfour)",
        "cardSubtype": "CHARACTER",
        "cardCategory": "CHARACTER",
        "side": "DARK",
    },
    ("DARK", "Flagship"): {
        "cardId": "4_122",
        "title": "Flagship",
        "cardSubtype": "EFFECT",
        "cardCategory": "EFFECT",
        "side": "DARK",
    },
}


def titles_to_try(title: str) -> list[str]:
    t = title.strip()
    out: list[str] = []

    def add(x: str) -> None:
        x = x.strip()
        if x and x not in out:
            out.append(x)

    add(t)
    if " / " in t:
        add(t.split(" / ", 1)[0])
    if t.endswith(" (V)"):
        add(t[: -len(" (V)")].strip())
    if t.endswith(" (AI)"):
        add(t[: -len(" (AI)")].strip())
    for key in list(out):
        if key in TITLE_ALIAS:
            add(TITLE_ALIAS[key])
        saber = re.sub(r"(?i)sabres\b", "saber", key)
        saber = re.sub(r"(?i)sabre\b", "saber", saber)
        if saber != key:
            add(saber)
            if saber in TITLE_ALIAS:
                add(TITLE_ALIAS[saber])
    return out


def lookup(
    title: str,
    side: str,
    allowed_sets: set[int] | None,
) -> dict:
    side_u = side.upper()
    if side_u in {"LS", "LIGHT"}:
        side_u = "LIGHT"
    elif side_u in {"DS", "DARK"}:
        side_u = "DARK"
    pool = [
        c
        for c in load_cards()
        if (c.get("side") or "").upper() == side_u
        and (c.get("cardCategory") or "").upper() != "DEFENSIVE_SHIELD"
    ]
    cands: list[dict] = []
    for t in titles_to_try(title):
        exact = [c for c in pool if c.get("title") == t]
        if exact:
            cands = exact
            break
    if not cands:
        for t in titles_to_try(title):
            cf = t.casefold()
            exact = [c for c in pool if (c.get("title") or "").casefold() == cf]
            if exact:
                cands = exact
                break
    if not cands:
        for t in titles_to_try(title):
            pref = [
                c
                for c in pool
                if (c.get("title") or "").startswith(t + " (")
                or (c.get("title") or "").startswith(t + " /")
                or (c.get("title") or "").startswith(t + ",")
            ]
            if pref and not title.strip().endswith(" (V)"):
                printed_pref = []
                for c in pref:
                    try:
                        virt = c.get("hasVirtualSuffix") or set_num(c.get("cardId") or "0") >= 200
                    except Exception:
                        virt = False
                    if not virt:
                        printed_pref.append(c)
                pref = printed_pref
            if len(pref) == 1:
                cands = pref
                break
            if allowed_sets:
                in_pool = [c for c in pref if set_num(c["cardId"]) in allowed_sets]
                if len(in_pool) == 1:
                    cands = in_pool
                    break
            if pref:
                pref.sort(key=lambda c: (len(c.get("title") or ""),) + card_id_key(c["cardId"]))
                cands = [pref[0]]
                break
    if allowed_sets and cands:
        in_pool = [c for c in cands if set_num(c["cardId"]) in allowed_sets]
        if in_pool:
            cands = in_pool
    orig = title.strip()
    if orig.endswith(" (V)"):
        virt = [c for c in cands if c.get("hasVirtualSuffix") or set_num(c["cardId"]) >= 200]
        if virt:
            cands = virt
    if orig.endswith(" (AI)"):
        ai = [c for c in cands if c.get("hasAlternateImageSuffix")]
        if ai:
            cands = ai
    if not cands or all(set_num(c.get("cardId") or "") >= 200 for c in cands):
        for t in titles_to_try(title):
            miss = MISSING_BLUEPRINTS.get((side_u, t))
            if miss:
                return miss
        if not cands:
            raise KeyError(f"no blueprint for {side_u!r} {title!r}")
    cands.sort(key=lambda c: card_id_key(c["cardId"]))
    return cands[0]


def xml_for(
    rows: list[tuple[int, str, str | None]],
    side: str,
    format_key: str,
) -> tuple[str, list[str]]:
    allowed = load_format_sets().get(format_key)
    cards: list[dict] = []
    notes: list[str] = []
    for qty, title, hint in rows:
        use_side = hint or side
        card = lookup(title, use_side, allowed)
        if allowed and set_num(card["cardId"]) not in allowed:
            notes.append(f"OUT-OF-POOL {title} -> {card['cardId']}")
        for _ in range(qty):
            cards.append(card)
    lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        "<deck>",
    ]
    for card in cards:
        hid = "true" if is_horizontal(card) else "false"
        lines.append(
            f'    <card blueprintId="{escape(card["cardId"])}" '
            f'horizontal="{hid}" title="{escape(card["title"])}"/>'
        )
    lines.append("</deck>")
    lines.append("")
    return "\n".join(lines), notes


def wiki_download_line(filename: str) -> str:
    """Deck-info bullet used on championship pages (2026 Retro GEMPC template)."""
    return f"* '''GEMP Importable deck:''' [[Media:{filename} |Download]]"


def wiki_import_section(filename: str, xml: str) -> str:
    return wiki_download_line(filename)


def from_wiki_page(path: Path, format_key: str | None = None, event_token: str = "Worlds") -> dict:
    text = path.read_text(encoding="utf-8")
    info = parse_info(text)
    side = info.get("Side", "Light")
    fmt = format_key or info.get("Format") or "premiere_anh"
    rows = parse_wiki_cards(text)
    xml, notes = xml_for(rows, side, fmt if fmt in load_format_sets() else info.get("Format", fmt))
    year = None
    m = re.search(r"(\d{4})", info.get("Event", path.name))
    if m:
        year = m.group(1)
    name = safe_deck_filename(
        deck_name(
            info.get("Format", fmt),
            archetype_from_info(info),
            info.get("Player", "Player"),
            side,
            year,
            event_token,
        )
    )
    filename = name + ".txt"
    qty = sum(q for q, _, _ in rows)
    return {
        "info": info,
        "rows": rows,
        "xml": xml,
        "notes": notes,
        "name": name,
        "filename": filename,
        "qty": qty,
        "wiki_section": wiki_import_section(filename, xml),
    }


def inject_wiki_section(path: Path, section: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"\n== GEMP import ==.*?(?=\n== |\Z)",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    line = section.strip()
    if "GEMP Importable deck:" in text:
        text = re.sub(r"\* '''GEMP Importable deck:'''[^\n]+", line, text, count=1)
    else:
        inserted = False
        for field in ("Strategy", "Starting Card", "Side"):
            pat = rf"(\* '''{field}:'''[^\n]+)"
            if re.search(pat, text):
                text = re.sub(pat, rf"\1\n{line}", text, count=1)
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n" + line + "\n"
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-wiki", nargs="*", type=Path, default=[])
    ap.add_argument("--glob", default=None)
    ap.add_argument("--from-text", type=Path, default=None)
    ap.add_argument("--side", default=None)
    ap.add_argument("--name", default=None)
    ap.add_argument("--format", default=None)
    ap.add_argument("--event", default="Worlds")
    ap.add_argument("--out", type=Path, default=ROOT / "gemp-import")
    ap.add_argument("--inject", action="store_true")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    fail = 0
    if args.from_text:
        text = args.from_text.read_text(encoding="utf-8")
        side = args.side or "Light"
        fmt = args.format or "premiere_anh"
        rows = parse_wiki_cards(text)
        xml, notes = xml_for(rows, side, fmt)
        name = safe_deck_filename(args.name or args.from_text.stem)
        dest = args.out / (name + ".txt")
        dest.write_text(xml, encoding="utf-8", newline="\n")
        extra = f" notes={notes}" if notes else ""
        print(f"OK {dest.name} qty={sum(q for q,_,_ in rows)} len={len(name)}{extra}")
        return 0
    paths = list(args.from_wiki)
    if args.glob:
        paths.extend(sorted(ROOT.glob(args.glob)))
    paths = [p for p in paths if p.is_file()]
    if not paths:
        print("pass --from-wiki, --glob, or --from-text", file=sys.stderr)
        return 2
    for path in paths:
        try:
            result = from_wiki_page(path, args.format, args.event)
        except KeyError as e:
            print("FAIL", path.name, e)
            fail += 1
            continue
        dest = args.out / result["filename"]
        dest.write_text(result["xml"], encoding="utf-8", newline="\n")
        extra = f" notes={result['notes']}" if result["notes"] else ""
        print(
            f"OK {result['filename']} qty={result['qty']} "
            f"len={len(result['name'])}{extra}"
        )
        if args.inject:
            inject_wiki_section(path, result["wiki_section"])
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
