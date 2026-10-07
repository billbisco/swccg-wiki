#!/usr/bin/env python3
"""Generate 10th Annual GEMPC hub + two-column deck pages from 2026 Gempc.zip."""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
MEDIA = ROOT / "gempc-2026-media"
DECK_DIR = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026\2026-gempc")
BP_PATH = Path(
    r"C:\Users\gythe\.grok\tmp-swccg-gemp\src\gemp-swccg-cards\src\main\resources\card_blueprint_database.json"
)
T8_ZIP = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026\2026 Gempc Top 8.zip")

EVENT = "2026 Tenth Annual GEMPC"
EVENT_TITLE = "2026 Tenth Annual GEMPC"
PC_HUB = "https://www.starwarsccg.org/2026-06-tenth-annual-gempc-may-to-july-2026/"
PC_DECKS = "https://forum.starwarsccg.org/viewtopic.php?t=86845"
PC_FORUM = "https://forum.starwarsccg.org/viewforum.php?f=1595"
YT = "https://www.youtube.com/playlist?list=PLQSFYZX0M9YQOr2wLL2JQMshuie6hLniG"

# PC Top 8 finish order (name, short DS, short LS)
TOP8 = [
    ("Pat Johnson", "TDIGWATT(V)", "Luke Saga"),
    ("Drew Lichtenstein", "Verge", "TIGIH"),
    ("Sam Tashima", "MKOS", "Luke Saga"),
    ("Jarad Konsker", "MKOS", "Path"),
    ("Joe Olson", "EOps", "Luke Saga"),
    ("Matthew Harrison-Trainor", "TDIGWATT(V)", "TIGIH"),
    ("Greg Shaw", "Hunt Down", "MWYHL(V)"),
    ("Jeff Lavigne", "MKOS", "Path"),
]

# R64 as published (seed order)
R64 = [
    ("Joe Olson", "EOps", "WYS"),
    ("Matthew Harrison-Trainor", "TDIGWATT(V)", "TIGIH"),
    ("Greg Shaw", "SC", "Luke Saga"),
    ("Sam Tashima", "TDIGWATT(V)", "WHAP"),
    ("Jeff Lavigne", "EOps", "WYS"),
    ("Brian Fred", "Verge", "WHAP"),
    ("Chris Gogolen", "HD(V)", "HITCO"),
    ("Timo Dusel", "EOps", "OA"),
    ("Drew Lichtenstein", "SC", "MWYHL(V)"),
    ("Pat Johnson", "Court", "WYS"),
    ("Daniel Amor", "MKOS", "Legend"),
    ("Brad Kippel", "ISB", "Zero Hour"),
    ("Chris Kelly", "Court", "Luke Saga"),
    ("Ryan Jellison", "EOps", "No Idea"),
    ("Matt Scott", "MKOS", "No Idea"),
    ("Charlie Arlandson", "TDIGWATT(V)", "Luke Saga"),
    ("Joe Horbey", "EOps", "Legend"),
    ("Chris Wirfs", "Watto", "Diplo"),
    ("Ziemowit Skwara", "EOps", "WYS"),
    ("Bill Kafer", "Verge", "WYS"),
    ("Anthony Howard", "HD(V)", "Luke Saga"),
    ("Andrew Moss", "TDIGWATT(V)", "MWYHL(V)"),
    ("Dennis Reinhardt", "MKOS", "WHAP"),
    ("Justin Miyashiro", "EOps", "Luke Saga"),
    ("AJ Hatoum", "HD(V)", "WYS"),
    ("Kyle Krueger", "EOps", "WYS"),
    ("Jarad Konsker", "HD(V)", "Path"),
    ("Robbie Hendon", "Senate", "Chewie's Hut"),
    ("Matt Wadden", "Court", "Luke Saga"),
    ("Nathan Russell", "HD(V)", "Luke Saga"),
    ("Logan Pietig", "SC", "Luke Saga"),
    ("Scott Lingrell", "EOps", "Luke Saga"),
    ("Keith Brown", "SC", "MWYHL(V)"),
    ("Wayne Cullen", "IE", "Luke Saga"),
    ("Ryan Sersen", "AOBS", "Luke Saga"),
    ("Karl Koenig", "EOps", "WYS"),
    ("Mike Turner", "TTO", "Hidden Base"),
    ("Amar Banger", "EOps", "LTWW(V)"),
    ("Garrett Larson", "Senate", "WHAP"),
    ("David Woods", "IE", "No Idea"),
    ("Blake Silkwood", "IE", "Rey Saga"),
    ("Justin Carulli", "Senate", "Hyperdrive (V)"),
    ("Dan Tartaglione", "HD(V)", "WHAP"),
    ("Bill Bacheler", "TDIGWATT(V)", "WYS"),
    ("John Veasey", "Senate", "MWYHL(V)"),
    ("Kendall Halman", "Court", "TIGIH"),
    ("Brandon Baity", "SC", "Profit"),
    ("Kyle Kallin", "Invasion", "WYS"),
    ("Nick Swedal", "ASM", "No Idea"),
    ("Randy Scott", "ROTS Vader", "Luke Saga"),
    ("John Werner", "TDIGWATT(V)", "WYS"),
    ("Gregor Romanik", "MKOS", "Hyperdrive(V)"),
    ("Casey Johnson", "Hunt Down", "HITCO"),
    ("Chad Lawrence", "EOps", "Luke Saga"),
    ("Pierre Dubreuil", "BHBM", "Luke Saga"),
    ("Jared Greenwald", "TDIGWATT(V)", "Path"),
    ("Charles Hickey", "MKOS", "Luke Saga"),
    ("Jack Douglass", "ROTS Dooku", "Legend"),
    ("Erich Hawbaker", "TDIGWATT(V)", "Diplo"),
    ("Sam Olson", "TDIGWATT(V)", "Luke Saga"),
    ("Matt Bugbee", "TDIGWATT(V)", "Luke Saga"),
    ("Matthew Ford", "MKOS", "Luke Saga"),
]

FILE_PLAYER = {
    "Amor": "Daniel Amor",
    "Arlandson": "Charlie Arlandson",
    "Bacheler": "Bill Bacheler",
    "Baity": "Brandon Baity",
    "Banger": "Amar Banger",
    "Brown": "Keith Brown",
    "Bugbee": "Matt Bugbee",
    "CJohnson": "Casey Johnson",
    "Cullen": "Wayne Cullen",
    "Douglass": "Jack Douglass",
    "Dubreuil": "Pierre Dubreuil",
    "Dusel": "Timo Dusel",
    "Ford": "Matthew Ford",
    "Fred": "Brian Fred",
    "Gogolen": "Chris Gogolen",
    "Greenwald": "Jared Greenwald",
    "Halman": "Kendall Halman",
    "HarrisonTrainor": "Matthew Harrison-Trainor",
    "Hatoum": "AJ Hatoum",
    "Hawbaker": "Erich Hawbaker",
    "Hickey": "Charles Hickey",
    "Horbey": "Joe Horbey",
    "Howard": "Anthony Howard",
    "Jellison": "Ryan Jellison",
    "Kallin": "Kyle Kallin",
    "Kafer": "Bill Kafer",
    "Kelly": "Chris Kelly",
    "Kippel": "Brad Kippel",
    "Koenig": "Karl Koenig",
    "Konsker": "Jarad Konsker",
    "Krueger": "Kyle Krueger",
    "Lawrence": "Chad Lawrence",
    "Lavigne": "Jeff Lavigne",
    "Lichtenstein": "Drew Lichtenstein",
    "Lingrell": "Scott Lingrell",
    "Larson": "Garrett Larson",
    "MHT": "Matthew Harrison-Trainor",
    "Miyashiro": "Justin Miyashiro",
    "Moss": "Andrew Moss",
    "Olson": "Joe Olson",
    "PJohnson": "Pat Johnson",
    "Pietig": "Logan Pietig",
    "Reinhardt": "Dennis Reinhardt",
    "Romanik": "Gregor Romanik",
    "Russell": "Nathan Russell",
    "Sersen": "Ryan Sersen",
    "Scott": "Matt Scott",
    "Shaw": "Greg Shaw",
    "Silkwood": "Blake Silkwood",
    "Skwara": "Ziemowit Skwara",
    "Swedal": "Nick Swedal",
    "Tashima": "Sam Tashima",
    "Tartaglione": "Dan Tartaglione",
    "Turner": "Mike Turner",
    "Veasey": "John Veasey",
    "Wadden": "Matt Wadden",
    "Werner": "John Werner",
    "Wirfs": "Chris Wirfs",
    "Woods": "David Woods",
    "Carulli": "Justin Carulli",
    "Hendon": "Robbie Hendon",
    "Johnson": "Pat Johnson",  # T8
    "JCarulli": "Justin Carulli",
    "JOlson": "Joe Olson",
    "MScott": "Matt Scott",
    "RScott": "Randy Scott",
    "SOlson": "Sam Olson",
}

LEFT = ["CHARACTER", "DEVICE", "EFFECT", "EPIC_EVENT", "LOCATION", "OBJECTIVE", "JEDI_TEST", "PODRACER"]
RIGHT = ["STARSHIP", "VEHICLE", "WEAPON", "INTERRUPT", "DEFENSIVE_SHIELD", "ADMIRAL'S_ORDER", "ADMIRALS_ORDER"]

CAT_LABEL = {
    "CHARACTER": "Character",
    "DEVICE": "Device",
    "EFFECT": "Effect",
    "EPIC_EVENT": "Epic Event",
    "LOCATION": "Location",
    "OBJECTIVE": "Objective",
    "STARSHIP": "Starship",
    "VEHICLE": "Vehicle",
    "WEAPON": "Weapon",
    "INTERRUPT": "Interrupt",
    "DEFENSIVE_SHIELD": "Defensive Shield",
    "ADMIRAL'S_ORDER": "Admiral's Order",
    "ADMIRALS_ORDER": "Admiral's Order",
    "JEDI_TEST": "Jedi Test",
    "PODRACER": "Podracer",
}


def load_bp():
    rows = json.loads(BP_PATH.read_text(encoding="utf-8"))
    by_id = {}
    by_title = {}
    for r in rows:
        cid = str(r.get("cardId") or "")
        title = r.get("title") or ""
        cat = (r.get("cardCategory") or "UNKNOWN").upper()
        rec = {"title": title, "cat": cat, "side": r.get("side")}
        by_id[cid] = rec
        by_id[cid.replace("^", "")] = rec
        by_title[title.lower()] = rec
    return by_id, by_title


def parse_gemp(path: Path, by_id, by_title):
    text = path.read_text(encoding="utf-8")
    # GEMP sometimes uses & in titles already escaped
    root = ET.fromstring(text)
    counts = Counter()
    meta = {}
    for card in root.findall("card"):
        bid = (card.get("blueprintId") or "").strip()
        title = (card.get("title") or "").replace("&amp;", "&").strip()
        rec = by_id.get(bid) or by_id.get(bid.replace("^", "")) or by_title.get(title.lower())
        cat = rec["cat"] if rec else "UNKNOWN"
        key = (cat, title)
        counts[key] += 1
        if cat == "OBJECTIVE" and "objective" not in meta:
            meta["objective"] = title
    return counts, meta


def wiki_title_player(name: str) -> str:
    return name


def deck_page_title(player: str, side: str, obj_short: str, t8: bool) -> str:
    prefix = "2026 GEMPC Top 8" if t8 else "2026 GEMPC"
    side_l = "DS" if side == "DS" else "LS"
    slug = re.sub(r"[^\w]+", " ", obj_short).strip()
    slug = slug.replace(" ", "_")
    # readable title
    return f"{prefix} {player} {side_l} {obj_short}"


def fname(title: str) -> str:
    return title.replace(" ", "_").replace("/", "_") + ".wiki"


def link_card(title: str) -> str:
    return f"[[{title}]]"


def render_deck(player, side, obj_short, counts, media_name, t8, companion):
    side_word = "Dark" if side == "DS" else "Light"
    cat_map = defaultdict(list)
    for (cat, title), n in sorted(counts.items(), key=lambda x: (x[0][0], x[0][1].lower())):
        cat_map[cat].append((n, title))
    obj = None
    for n, title in cat_map.get("OBJECTIVE", []):
        obj = title
        break
    if not obj:
        obj = obj_short

    def col(cats):
        bits = []
        for cat in cats:
            items = cat_map.get(cat) or []
            if not items:
                continue
            bits.append(f"'''{CAT_LABEL.get(cat, cat.title())}'''")
            for n, title in items:
                bits.append(f"* {n}x {link_card(title)}")
            bits.append("")
        return "\n".join(bits).rstrip()

    left = col(LEFT)
    right = col(RIGHT)
    extra = [c for c in cat_map if c not in LEFT and c not in RIGHT]
    extra_txt = col(extra) if extra else ""
    if extra_txt:
        right = (right + "\n\n" + extra_txt).strip()

    event_link = f"[[{EVENT_TITLE}]]"
    prefix = "2026 GEMPC Top 8" if t8 else "2026 GEMPC"
    title = deck_page_title(player, side, obj_short, t8)
    companion_line = f"* [[{companion}]]" if companion else ""
    body = f"""== Deck info ==
* '''Player:''' [[{player}]]
* '''Event:''' {event_link}
* '''Format:''' [[Open]]
* '''Side:''' [[{side_word}]]
* '''Objective:''' {link_card(obj)}
* '''GEMP Importable deck:''' [[Media:{media_name}|Download]]

== Decklist ==

{{| class="wikitable" style="width:100%;"
|-
| style="width:50%; vertical-align:top;" |
{left}

| style="width:50%; vertical-align:top;" |
{right}

|}}

== See also ==
* {event_link}
{companion_line}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:{side_word} Side decks]]
[[Category:2026]]
"""
    return title, body.replace("\r\n", "\n")


def parse_filename(name: str):
    m = re.match(r"26Gempc (T8 )?(\S+) (DS|LS) (.+)\.txt$", name)
    if not m:
        return None
    t8 = bool(m.group(1))
    token = m.group(2)
    side = m.group(3)
    obj = m.group(4)
    player = FILE_PLAYER.get(token)
    if not player:
        player = token
    obj_map = {
        "Deal": "TDIGWATT(V)",
        "EOps": "EOps",
        "Eops": "EOps",
        "HyperdriveV": "Hyperdrive (V)",
        "LTWWv": "LTWW(V)",
        "HD": "Hunt Down",
        "HDv": "HD(V)",
        "Hunt Down": "Hunt Down",
        "MKOS": "MKOS",
        "SC": "SC",
        "Verge": "Verge",
        "Court": "Court",
        "ISB": "ISB",
        "IE": "IE",
        "TTO": "TTO",
        "Watto": "Watto",
        "Senate": "Senate",
        "Invasion": "Invasion",
        "BHBM": "BHBM",
        "AOBS": "AOBS",
        "ASM": "ASM",
        "ROTS Dooku": "ROTS Dooku",
        "ROTS Vader": "ROTS Vader",
        "Luke Saga": "Luke Saga",
        "TIGIH": "TIGIH",
        "Path": "Path",
        "MWYHLv": "MWYHL(V)",
        "WYS": "WYS",
        "WHAP": "WHAP",
        "HITCO": "HITCO",
        "OA": "OA",
        "No Idea": "No Idea",
        "Legend": "Legend",
        "Zero Hour": "Zero Hour",
        "Diplo": "Diplo",
        "LTWWv": "LTWW(V)",
        "Profit": "Profit",
        "HB": "Hidden Base",
        "Hyperdrive v": "Hyperdrive (V)",
        "Rey Saga": "Rey Saga",
    }
    obj_short = obj_map.get(obj, obj)
    return player, side, obj_short, t8


def hub(deck_titles):
    def row(finish, player, ds, ls, t8=False):
        ds_t = deck_titles.get((player, "DS", t8))
        ls_t = deck_titles.get((player, "LS", t8))
        ds_cell = f"[[{ds_t}|{ds}]]" if ds_t else ds
        ls_cell = f"[[{ls_t}|{ls}]]" if ls_t else ls
        return f"| {finish} || [[{player}]] || {ds_cell} || {ls_cell}"

    t8_rows = ["{| class=\"wikitable sortable\"", "! Finish !! Player !! Dark !! Light"]
    for i, (p, ds, ls) in enumerate(TOP8, 1):
        t8_rows += ["|-", row(i, p, ds, ls, t8=True)]
    t8_rows.append("|}")

    r64_rows = ["{| class=\"wikitable sortable\"", "! Seed !! Player !! Dark !! Light"]
    for i, (p, ds, ls) in enumerate(R64, 1):
        r64_rows += ["|-", row(i, p, ds, ls, t8=False)]
    r64_rows.append("|}")

    return f"""'''{EVENT_TITLE}''' (also '''Batmouse's 10th Annual GEMPC''') was the Players Committee online match-play championship on GEMP in the [[Open]] format. Play ran May–July 2026. The Players Committee results page is dated 4 July 2026 (updated 16 July 2026).<ref name="pc">{PC_HUB}</ref>

[[Pat Johnson]] won with TDIGWATT(V) (Dark) and Luke Saga (Light) in the Top 8. [[Drew Lichtenstein]] finished second; [[Sam Tashima]] third.<ref name="pc" /> Round-of-64 lists on that page are the Swiss/R64 pair; Top 8 lists can differ (Johnson's R64 pair is Court / WYS).

== Format ==

* '''Environment:''' [[Open]]
* '''Platform:''' SWCCG GEMP
* '''Structure:''' Seeded match play (64-player published field)
* '''Forum:''' [{PC_FORUM} 10th Annual GEMPC Forum]
* '''GEMP importable decks:''' [{PC_DECKS} forum t=86845] (inner zip <code>2026 Gempc.zip</code> / Top 8 <code>2026 Gempc Top 8.zip</code>)
* '''Video:''' [{YT} YouTube playlist]

== Top 8 ==

Finals pair as published on the PC results page.<ref name="pc" />

{chr(10).join(t8_rows)}

== Round of 64 (by seed) ==

As listed on the PC results page. Dark/Light cells link to the GEMP import files from <code>2026 Gempc.zip</code>.<ref name="pc" />

{chr(10).join(r64_rows)}

== See also ==

* [[2026 Retro GEMP Match Play Championship (Premiere to DSII)]]
* [[Championships]] · [[Formats]] · [[GEMP]]
* [{PC_HUB} PC results]
* [{PC_DECKS} GEMP importable decks]
* [{PC_FORUM} Forum]
* [{YT} YouTube playlist]

== Sources ==

* [{PC_HUB} 2026-06 Tenth Annual GEMPC (May to July 2026)], starwarsccg.org (4 July 2026)
* [{PC_DECKS} 10th Annual GEMPC Gemp Importable Decks], forum.starwarsccg.org t=86845
* [{PC_FORUM} 10th Annual GEMPC Forum]

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Championships]]
[[Category:Tournaments]]
[[Category:GEMP]]
[[Category:2026]]
"""


def main():
    by_id, by_title = load_bp()
    MEDIA.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)

    # extract T8
    import zipfile
    t8dir = DECK_DIR.parent / "2026-gempc-t8"
    t8dir.mkdir(exist_ok=True)
    with zipfile.ZipFile(T8_ZIP) as zf:
        zf.extractall(t8dir)

    files = list(DECK_DIR.glob("26Gempc *.txt")) + list(t8dir.glob("26Gempc T8 *.txt"))
    deck_titles = {}  # (player, side, t8) -> page title
    companions = defaultdict(dict)

    parsed = []
    for path in files:
        info = parse_filename(path.name)
        if not info:
            print("SKIP", path.name)
            continue
        player, side, obj_short, t8 = info
        counts, meta = parse_gemp(path, by_id, by_title)
        media_name = path.name
        dest = MEDIA / media_name
        dest.write_bytes(path.read_bytes())
        parsed.append((player, side, obj_short, t8, counts, media_name))
        companions[player][("T8" if t8 else "R64", side)] = None  # fill after titles

    # titles first
    for player, side, obj_short, t8, counts, media_name in parsed:
        title = deck_page_title(player, side, obj_short, t8)
        deck_titles[(player, side, t8)] = title

    for player, side, obj_short, t8, counts, media_name in parsed:
        other_side = "LS" if side == "DS" else "DS"
        companion = deck_titles.get((player, other_side, t8))
        title, body = render_deck(player, side, obj_short, counts, media_name, t8, companion)
        fp = PAGES / fname(title)
        fp.write_text(body, encoding="utf-8", newline="\n")
        print("deck", title)

    hub_body = hub(deck_titles)
    (PAGES / "2026_Tenth_Annual_GEMPC.wiki").write_text(hub_body, encoding="utf-8", newline="\n")
    print("hub", EVENT_TITLE, "decks", len(parsed))


if __name__ == "__main__":
    main()
