#!/usr/bin/env python3
"""2025 tournament hubs + GEMP decks (Worlds, US Nats, GEMPC, Retro, Charity)."""
from __future__ import annotations

import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import update_gempc_start_fields as ug  # noqa: E402
from generate_2026_sdso import LEFT, RIGHT, col, load_bp_simple, parse_gemp_counts, wiki_fname  # noqa: E402
from generate_2026_remaining import FILE_PLAYER, render_deck as render26, upsert_stub  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
MEDIA = ROOT / "2025-media"
TD = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026")

FILE_PLAYER.update(
    {
        "AChu": "Apollo Chu",
        "BChu": "Benji Chu",
        "Chu": "Jonny Chu",
        "JChu": "Jonny Chu",
        "MHT": "Matthew Harrison-Trainor",
        "MatthewHT": "Matthew Harrison-Trainor",
        "RScott": "Randy Scott",
        "MMorrison": "Michael Morrison",
        "Johnson": "Patrick Johnson",
        "Kippel": "Brad Kippel",
        "Feldman": "Paul Todd Feldman",
        "Anis": "Casey Anis",
        "Banger": "Amar Banger",
        "Behm": "Zachary Behm",
        "Branch": "Justin Branch",
        "Bacheler": "Bill Bacheler",
        "Jellison": "Ryan Jellison",
        "Arlandson": "Charlie Arlandson",
        "Amor": "Daniel Amor",
        "Britain": "Conor Britain",
        "Monteith": "Ian Monteith",
        "Hendon": "Robbie Hendon",
        "Howard": "Anthony Howard",
        "Kelly": "Chris Kelly",
        "Wirfs": "Chris Wirfs",
        "Sokol": "Matt Sokol",
        "Skwara": "Ziemowit Skwara",
        "Krueger": "Kyle Krueger",
        "Russell": "Nathan Russell",
        "Lutz": "Matt Lutz",
        "Hawbaker": "Erich Hawbaker",
        "Hickey": "Charles Hickey",
        "Greenwald": "Jared Greenwald",
        "Douglass": "Jack Douglass",
        "Silkwood": "Blake Silkwood",
        "Talaga": "Andy Talaga",
        "Desai": "Justin Desai",
        "Mischke": "Bryan Mischke",
        "Bali": "Vikram Bali",
        "Coggins": "Paul Coggins",
        "Cross": "Ken Cross",
        "Turner": "Mike Turner",
        "Kallin": "Kyle Kallin",
        "Huo": "Ming Huo",
        "Swedal": "Nick Swedal",
        "Billings": "Mark Billings",
        "Reinhold": "Brad Reinhold",
        "Christoffel": "Jeremy Christoffel",
        "Bisco": "Bill Bisco",
        "Christensen": "Abe Christensen",
        "Miyashiro": "Justin Miyashiro",
        "Scott": "Matt Scott",
        "Olson": "Joe Olson",
        "Shaw": "Greg Shaw",
        "Hunter": "Hayes Hunter",
        "Tashima": "Sam Tashima",
        "Fred": "Brian Fred",
        "Horbey": "Joe Horbey",
        "Dusel": "Timo Dusel",
        "Pietig": "Logan Pietig",
        "Lingrell": "Scott Lingrell",
        "Cullen": "Wayne Cullen",
        "Kafer": "Bill Kafer",
        "Gogolen": "Chris Gogolen",
        "Lavigne": "Jeff Lavigne",
        "Kessling": "Mike Kessling",
        "Hatoum": "AJ Hatoum",
        "Koenig": "Karl Koenig",
        "Reinhardt": "Dennis Reinhardt",
        "Aasen": "Phil Aasen",
        "Alperstein": "Barry Alperstein",
        "Baity": "Brandon Baity",
        "Konsker": "Jarad Konsker",
        "Sersen": "Ryan Sersen",
        "Harpster": "Steve Harpster",
        "Spijksma": "Erik Spijksma",
        "Jacobson": "Jonas Jacobson",
        "Grubb": "Grubb",
        "DMorrison": "DMorrison",
        "Harrison Trainor": "Matthew Harrison-Trainor",
        "Pater": "L. Pater",
        "L. Pater": "L. Pater",
        "Werner": "John Werner",
        "Yim": "Gibson Yim",
        "Grubb": "Jonathan Grubb",
        "Morrison": "Michael Morrison",
        "DMorrison": "David Morrison",
        "David Morrison": "David Morrison",
        "Jacobson": "Peter Jacobson",
        "Santosuosso": "Thomas Santosuosso",
        "Behm": "Zachary Behm",
        "Zach Behm": "Zachary Behm",
        "Bacheler": "Bill Bacheler",
        "William Bacheler": "Bill Bacheler",
        "Hickey": "Charles Hickey",
        "Greenwald": "Jared Greenwald",
        "Douglass": "Jack Douglass",
        "Talaga": "Andy Talaga",
        "Hawbaker": "Erich Hawbaker",
        "Veasey": "John Veasey",
        "Baity": "Brandon Baity",
        "Tartaglione": "Dan Tartaglione",
        "Woods": "David Woods",
        "Sersen": "Ryan Sersen",
        "Russell": "Nathan Russell",
        "Lutz": "Matt Lutz",
        "Britain": "Conor Britain",
        "Amor": "Daniel Amor",
        "Skwara": "Ziemowit Skwara",
        "Miyashiro": "Justin Miyashiro",
        "Branch": "Justin Branch",
        "Moss": "Andrew Moss",
        "Cullen": "Wayne Cullen",
        "Halman": "Kendall Halman",
        "Swedal": "Nick Swedal",
        "Larson": "Garrett Larson",
        "Spijksma": "Erik Spijksma",
        "Banger": "Amar Banger",
        "Hendon": "Robbie Hendon",
        "Krueger": "Kyle Krueger",
        "Konsker": "Jarad Konsker",
        "Howard": "Anthony Howard",
        "Kelly": "Chris Kelly",
        "Sokol": "Matt Sokol",
        "Scott": "Matt Scott",
        "Jellison": "Ryan Jellison",
        "Kippel": "Brad Kippel",
        "Wirfs": "Chris Wirfs",
        "Gogolen": "Chris Gogolen",
        "Lavigne": "Jeff Lavigne",
        "Shaw": "Greg Shaw",
        "Tashima": "Sam Tashima",
        "Olson": "Joe Olson",
        "Kafer": "Bill Kafer",
        "Kessling": "Mike Kessling",
        "Fred": "Brian Fred",
        "Reinhardt": "Dennis Reinhardt",
        "Horbey": "Joe Horbey",
        "Pietig": "Logan Pietig",
        "Hatoum": "AJ Hatoum",
        "Koenig": "Karl Koenig",
        "Lingrell": "Scott Lingrell",
        "Silkwood": "Blake Silkwood",
        "Johnson": "Patrick Johnson",
        "MatthewHT": "Matthew Harrison-Trainor",
        "MHT": "Matthew Harrison-Trainor",
    }
)

WORLDS_T8 = [
    "Greg Shaw",
    "Joe Olson",
    "Brian Fred",
    "Hayes Hunter",
    "Matthew Harrison-Trainor",
    "Patrick Johnson",
    "Sam Tashima",
    "Benji Chu",
]
NATS_T8 = [
    "Matt Scott",
    "Hayes Hunter",
    "Brian Fred",
    "Chris Kelly",
    "Andrew Moss",
    "Matthew Harrison-Trainor",
    "Joe Horbey",
    "Benji Chu",
]
GEMPC_T8 = [
    "Matthew Harrison-Trainor",
    "Chris Gogolen",
    "Greg Shaw",
    "Jeff Lavigne",
    "Timo Dusel",
    "Ryan Jellison",
    "Chris Wirfs",
    "Brad Kippel",
]
CHARITY_T8 = [
    "Joe Horbey",
    "Scott Lingrell",
    "Wayne Cullen",
    "Casey Anis",
    "Brad Kippel",
    "Logan Pietig",
    "Timo Dusel",
    "Ian Monteith",
]


def tidy_player(n: str) -> str:
    n = re.sub(r"\s+", " ", n).strip()
    n = n.replace("Pat Johnson", "Patrick Johnson")
    n = n.replace("Samuel Tashima", "Sam Tashima")
    n = n.replace("Robert Hendon", "Robbie Hendon")
    n = n.replace("Ian Montieth", "Ian Monteith")
    n = n.replace("Zach Behm", "Zachary Behm")
    n = n.replace("William Bacheler", "Bill Bacheler")
    n = n.replace("Mike D’Ambroise", "Mike d'Amboise")
    n = n.replace("Mike D'Ambroise", "Mike d'Amboise")
    n = n.replace("Kendal Halman", "Kendall Halman")
    return n


def numbered(path: Path, after: str) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    i = text.find(after)
    if i < 0:
        return []
    chunk = text[i + len(after) :]
    stop = re.search(r"\n(Day 2|Posted|Top 8:|Round of)", chunk)
    if stop:
        chunk = chunk[: stop.start()]
    names = []
    for m in re.finditer(r"#\d+\s+([^–\n]+?)\s+–", chunk):
        n = tidy_player(m.group(1))
        if n not in names:
            names.append(n)
    if names:
        return names
    for m in re.finditer(r"(?:^|\n)([A-Z][^–\n]+?)\s+–\s+https://", chunk):
        n = tidy_player(m.group(1))
        if n not in names:
            names.append(n)
    return names


def canon(token: str) -> str:
    token = token.replace("_", " ").strip()
    return FILE_PLAYER.get(token, token)


def parse_gemp(path: Path):
    name = path.name
    folder = path.parent.name.lower()
    if name.startswith("2024"):
        return None
    t8 = (
        " T8 " in f" {name} "
        or name.startswith("25Charity")
        or folder.endswith("-t8")
        or folder == "top 8"
    )
    stage = "t8" if t8 else "d1"
    if " Final " in name:
        stage = "final"
        t8 = True
    elif " T4 " in name:
        stage = "t4"
        t8 = True
    rest = None
    ev = None
    for pref, e in [
        ("25Worlds T8 ", "worlds"),
        ("25Worlds ", "worlds"),
        ("25Nats T8 ", "nats"),
        ("25Nats ", "nats"),
        ("25GEMPC T8 ", "gempc"),
        ("25GEMPC ", "gempc"),
        ("25Gempc ", "gempc"),
        ("25CharityV3 ", "charity"),
        ("25RetroMPC Final ", "retro"),
        ("25RetroMPC T4 ", "retro"),
        ("25RetroMPC T8 ", "retro"),
        ("25RetroMPC ", "retro"),
    ]:
        if name.startswith(pref):
            ev, rest = e, name[len(pref) :]
            break
    if not ev:
        return None
    rest = rest[: -4] if rest.endswith(".txt") else rest
    m = re.search(r" (DS|LS|LA) ", rest)
    if not m:
        return None
    player = canon(rest[: m.start()])
    side = "LS" if m.group(1) == "LA" else m.group(1)
    obj = rest[m.end() :]
    return ev, player, t8, side, obj, name, stage


def event_title(ev: str) -> str:
    return {
        "worlds": "2025 World Championship",
        "nats": "2025 U.S. National Championship",
        "gempc": "2025 Ninth Annual GEMPC",
        "retro": "2025 Retro GEMP Match Play Championship (Premiere to DSII)",
        "charity": "2025 Online Retro Event for Charity",
    }[ev]


def deck_title(ev, player, t8, side, obj, stage):
    if ev == "worlds":
        pfx = "2025 Worlds Top 8" if t8 else "2025 Worlds"
    elif ev == "nats":
        pfx = "2025 US Nationals Top 8" if t8 else "2025 US Nationals"
    elif ev == "gempc":
        pfx = "2025 GEMPC Top 8" if t8 else "2025 GEMPC"
    elif ev == "retro":
        pfx = {
            "final": "2025 Retro GEMPC Finals",
            "t4": "2025 Retro GEMPC Semifinals",
            "t8": "2025 Retro GEMPC Top 8",
        }.get(stage, "2025 Retro GEMPC")
    else:
        pfx = "2025 Charity Top 8"
    return f"{pfx} {player} {side} {obj}"


def render_deck(ev, player, t8, side, obj, counts, cards, media, companion, bp, dests, title_map, stage):
    # reuse 2026 renderer by monkeypatching its title helpers
    import generate_2026_remaining as g

    g.deck_title = lambda e, p, t, s, o, ev=ev, stage=stage: deck_title(ev, p, t, s, o, stage)
    g.event_title = lambda e, ev=ev: event_title(ev)
    title, body, hub = g.render_deck(
        ev, player, t8, side, obj, counts, cards, media, companion, bp, dests, title_map
    )
    body = body.replace("[[Category:2026]]", "[[Category:2025]]")
    body = body.replace("* [[List of SWCCG tournaments]]", "* [[List of SWCCG tournaments]]\n* [[European Championships]]" if ev == "euro" else "* [[List of SWCCG tournaments]]")
    return title, body, hub


def cell(dt, hl, player, t8, side):
    page = dt.get((player, t8, side))
    if not page:
        return "—"
    return f"[[{page}|{hl.get(page, page)}]]"


def people_table(title, players, dt, hl, t8):
    bits = ['{| class="wikitable sortable"', f"! {title} !! Player !! Dark !! Light"]
    for i, p in enumerate(players, 1):
        bits += ["|-", f"| {i} || [[{p}]] || {cell(dt, hl, p, t8, 'DS')} || {cell(dt, hl, p, t8, 'LS')}"]
    bits.append("|}")
    return "\n".join(bits)


def write_page(name, body):
    (PAGES / name).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def refs():
    return """{{#if:1|<nowiki />
<h2>References</h2>
<references />}}"""


def process_gemp():
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()
    MEDIA.mkdir(parents=True, exist_ok=True)
    folders = [
        TD / "2025-worlds",
        TD / "2025-worlds-t8",
        TD / "2025-nats",
        TD / "2025-nats-t8",
        TD / "2025-gempc",
        TD / "2025-gempc-t8",
        TD / "2025-retro-mpc",
        TD / "2025-charity",
    ]
    parsed = []
    for d in folders:
        for path in d.rglob("*.txt"):
            info = parse_gemp(path)
            if not info:
                print("SKIP", path.name)
                continue
            ev, player, t8, side, obj, media, stage = info
            try:
                counts, cards = parse_gemp_counts(path, by_id, by_title)
            except Exception as e:
                print("BADXML", path.name, e)
                continue
            shutil.copy2(path, MEDIA / media)
            parsed.append((ev, player, t8, side, obj, media, counts, cards, stage))

    deck_titles = {}
    hub_labels = {}
    for ev, player, t8, side, obj, media, counts, cards, stage in parsed:
        deck_titles[(ev, player, t8, side, stage)] = deck_title(
            ev, player, t8, side, obj, stage
        )
    for ev, player, t8, side, obj, media, counts, cards, stage in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = deck_titles.get((ev, player, t8, other, stage))
        title, body, hub = render_deck(
            ev, player, t8, side, obj, counts, cards, media, companion, bp, dests, title_map, stage
        )
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub
        print("deck", title, "->", hub, "n", sum(counts.values()))

    def subset(ev):
        dt, hl, st = {}, {}, {}
        for (e, player, t8, side, stage), title in deck_titles.items():
            if e != ev:
                continue
            dt[(player, t8, side)] = title
            st[(player, stage, side)] = title
            hl[title] = hub_labels.get(title, title)
        return dt, hl, st

    worlds_d1 = numbered(ROOT / "encyclopedia/pc-2025/worlds.txt", "Day 1")
    nats_d1 = numbered(ROOT / "encyclopedia/pc-2025/usnats.txt", "Day 1")
    wdt, whl, _ = subset("worlds")
    ndt, nhl, _ = subset("nats")
    gdt, ghl, _ = subset("gempc")
    rdt, rhl, rst = subset("retro")
    cdt, chl, _ = subset("charity")
    write_worlds(wdt, whl, worlds_d1)
    write_nats(ndt, nhl, nats_d1)
    gempc_r64 = numbered(ROOT / "encyclopedia/pc-2025/gempc.txt", "Round of 64")
    write_gempc(gdt, ghl, gempc_r64)
    write_retro(rdt, rhl, rst)
    write_charity(cdt, chl)

    src = {
        "worlds": (
            "https://www.starwarsccg.org/2025-09-world-championship-seattle-washington-october-4-5-2025/",
            "4–5 October 2025",
        ),
        "nats": (
            "https://www.starwarsccg.org/2025-07-u-s-national-championship-columbus-ohio-aug-23-24-2025/",
            "23–24 August 2025",
        ),
        "gempc": (
            "https://www.starwarsccg.org/2025-05-9th-annual-gempc-may-to-july-2025/",
            "May–July 2025",
        ),
        "retro": (
            "https://www.starwarsccg.org/2025-04-retro-gemp-match-play-championship-premiere-to-dsii-may-to-july-2025/",
            "May–July 2025",
        ),
        "charity": (
            "https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/",
            "May–June 2025",
        ),
    }
    by_p = defaultdict(list)
    for ev, player, t8, side, obj, media, counts, cards, stage in parsed:
        by_p[(ev, player)].append(t8)
    for (ev, player), t8s in by_p.items():
        et = event_title(ev)
        url, date = src[ev]
        dt, hl, _st = subset(ev)
        rows = []
        if any(t8s):
            fin = "—"
            order = {
                "worlds": WORLDS_T8,
                "nats": NATS_T8,
                "gempc": GEMPC_T8,
                "charity": CHARITY_T8,
            }.get(ev, [])
            if player in order:
                fin = f"#{order.index(player)+1}"
            rows.append(
                f"|- \n| {date} || [[{et}]] (Top 8) || [[Open]] || {fin} || {cell(dt, hl, player, True, 'DS')} || {cell(dt, hl, player, True, 'LS')}"
            )
        if (not all(t8s)) or ev in ("worlds", "nats", "gempc"):
            if any(not t for t in t8s) or ev in ("worlds", "nats", "gempc"):
                if not any(t8s) or True:
                    if any(not x for x in t8s):
                        rows.append(
                            f"|- \n| {date} || [[{et}]] (Day 1) || [[Open]] || — || {cell(dt, hl, player, False, 'DS')} || {cell(dt, hl, player, False, 'LS')}"
                        )
        # dedupe empty day1
        rows = [r for r in rows if "|| — || —" not in r or "Top 8" in r]
        if rows:
            upsert_stub(player, rows, et, url)
            sp = STUBS / (player.replace(" ", "_") + ".wiki")
            if sp.exists():
                st = sp.read_text(encoding="utf-8")
                if "[[Category:2025]]" not in st:
                    st = st.replace("[[Category:2026]]", "[[Category:2026]]\n[[Category:2025]]")
                    sp.write_text(st, encoding="utf-8", newline="\n")
    print("gemp decks", len(parsed))
    return subset


def write_worlds(dt, hl, d1):
    body = f"""'''2025 World Championship''' was the 30th annual Players Committee World Championship at the Hampton Inn & Suites in SeaTac, Washington, 3–5 October 2025 (constructed 4–5 October). [[Greg Shaw]] defeated [[Joe Olson]] in the Final Confrontation.<ref name="pc">https://www.starwarsccg.org/2025-09-world-championship-seattle-washington-october-4-5-2025/</ref><ref name="wrap">https://www.starwarsccg.org/world-championship-2025-wrap-up-greg-shaw-wins-his-crown/</ref>

The main event is [[Open]] constructed: Day 1 Swiss (55 players), then Top 8. Friday team event winners: [[Brian Fred]] and [[Jonny Chu]]. Streaming: [[Dan Tartaglione]] and [[Garrett Larson]].<ref name="wrap" />

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' SeaTac, Washington
* '''Dates:''' 3–5 October 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1563 2025 World Championship Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?p=1440976#p1440976 forum p=1440976]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YQ_9BL8VcsfvHD371AW5aWM YouTube playlist]

== Top 8 ==

{people_table("Finish", WORLDS_T8, dt, hl, True)}

== Day 1 ==

{people_table("Day 1", d1, dt, hl, False)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Championships]] · [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/2025-09-world-championship-seattle-washington-october-4-5-2025/ PC results]
* [https://www.starwarsccg.org/world-championship-2025-wrap-up-greg-shaw-wins-his-crown/ Wrap-up]

== Sources ==

* [https://www.starwarsccg.org/2025-09-world-championship-seattle-washington-october-4-5-2025/ 2025-09 World Championship – Seattle, Washington (October 4-5, 2025)], starwarsccg.org
* [https://www.starwarsccg.org/world-championship-2025-wrap-up-greg-shaw-wins-his-crown/ World Championship 2025 Wrap-Up: Greg Shaw Wins his Crown]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
"""
    write_page("2025_World_Championship.wiki", body)


def write_nats(dt, hl, d1):
    body = f"""'''2025 U.S. National Championship''' was the Players Committee U.S. National Championship in Columbus, Ohio, 22–24 August 2025 (constructed 23–24 August). [[Matt Scott]] defeated [[Hayes Hunter]] in the Final Confrontation.<ref name="pc">https://www.starwarsccg.org/2025-07-u-s-national-championship-columbus-ohio-aug-23-24-2025/</ref><ref name="wrap">https://www.starwarsccg.org/2025-us-nationals-wrap-up-matt-scott-takes-it-down/</ref>

Friday warmup was won by [[AJ Hatoum]]; Sunday Consolation by [[Joe Olson]].<ref name="wrap" />

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' Columbus, Ohio
* '''Dates:''' 22–24 August 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1560 2025 U.S. Nationals Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=85896 forum t=85896]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YQ7P-amyYKPKPRsHqvWVGoT YouTube playlist]

== Top 8 ==

{people_table("Finish", NATS_T8, dt, hl, True)}

== Day 1 ==

{people_table("Day 1", d1, dt, hl, False)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2025-07-u-s-national-championship-columbus-ohio-aug-23-24-2025/ PC results]
* [https://www.starwarsccg.org/2025-us-nationals-wrap-up-matt-scott-takes-it-down/ Wrap-up]

== Sources ==

* [https://www.starwarsccg.org/2025-07-u-s-national-championship-columbus-ohio-aug-23-24-2025/ 2025-07 U.S. National Championship – Columbus, Ohio (Aug. 23-24, 2025)], starwarsccg.org
* [https://www.starwarsccg.org/2025-us-nationals-wrap-up-matt-scott-takes-it-down/ 2025 US Nationals Wrap-Up – Matt Scott Takes it Down]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
"""
    write_page("2025_U.S._National_Championship.wiki", body)


def write_gempc(dt, hl, r64):
    body = f"""'''2025 Ninth Annual GEMPC''' was the Players Committee online match-play championship on GEMP in the [[Open]] format, May–July 2025. The published Top 8 list starts with [[Matthew Harrison-Trainor]].<ref name="pc">https://www.starwarsccg.org/2025-05-9th-annual-gempc-may-to-july-2025/</ref>

== Format ==

* '''Environment:''' [[Open]]
* '''Platform:''' GEMP
* '''Dates:''' May–July 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1558 9th Annual GEMPC Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=85666 forum t=85666]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YRcSzce7qXC2-eP2cROWz4- YouTube playlist]

== Top 8 ==

As published (list order).<ref name="pc" />

{people_table("Finish", GEMPC_T8, dt, hl, True)}

== Round of 64 ==

Round of 64 lists as published on the PC results page (order on that page). Top 8 lists can differ from the Round of 64 pair.<ref name="pc" />

{people_table("R64", r64, dt, hl, False)}

== See also ==

* [[List of SWCCG tournaments]]
* [[2026 Tenth Annual GEMPC]]
* [[Tournaments]] · [[Formats]] · [[GEMP]]
* [https://www.starwarsccg.org/2025-05-9th-annual-gempc-may-to-july-2025/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2025-05-9th-annual-gempc-may-to-july-2025/ 2025-05 9th Annual GEMPC (May to July 2025)], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
"""
    write_page("2025_Ninth_Annual_GEMPC.wiki", body)


def write_retro(dt, hl, st):
    def cell_st(p, stage, side):
        page = st.get((p, stage, side))
        if not page:
            return "—"
        return f"[[{page}|{hl.get(page, page)}]]"

    def stage_table(heading, players, stage):
        bits = ['{| class="wikitable sortable"', f"! {heading} !! Player !! Dark !! Light"]
        for i, p in enumerate(players, 1):
            bits += [
                "|-",
                f"| {i} || [[{p}]] || {cell_st(p, stage, 'DS')} || {cell_st(p, stage, 'LS')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    finals = ["Timo Dusel", "Patrick Johnson"]
    t4 = ["Timo Dusel", "Patrick Johnson", "Paul Todd Feldman", "Brad Kippel"]
    t8 = [
        "Timo Dusel",
        "Patrick Johnson",
        "Paul Todd Feldman",
        "Brad Kippel",
        "Jeremy Christoffel",
        "Jonny Chu",
        "Joe Horbey",
        "Bill Bisco",
    ]
    body = f"""'''2025 Retro GEMP Match Play Championship (Premiere to DSII)''' was the Players Committee retro match-play event on GEMP, May–July 2025. [[Timo Dusel]] defeated [[Patrick Johnson]] in the Finals.<ref name="pc">https://www.starwarsccg.org/2025-04-retro-gemp-match-play-championship-premiere-to-dsii-may-to-july-2025/</ref>

== Format ==

* '''Environment:''' [[Premiere - Death Star II]]
* '''Platform:''' GEMP
* '''Dates:''' May–July 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1482 2025 Retro GEMPC Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=85775 forum t=85775]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YTCrWDXcWybAWlrzF3kph1q YouTube playlist]

== Bracket ==

{{| class="wikitable"
! Round !! Winner !! Defeated
|-
| Finals || [[Timo Dusel]] || [[Patrick Johnson]]
|-
| Semifinals || [[Patrick Johnson]] || [[Brad Kippel]]
|-
| Semifinals || [[Timo Dusel]] || [[Paul Todd Feldman]]
|-
| Quarterfinals || [[Paul Todd Feldman]] || [[Jeremy Christoffel]]
|-
| Quarterfinals || [[Timo Dusel]] || [[Jonny Chu]]
|-
| Quarterfinals || [[Patrick Johnson]] || [[Joe Horbey]]
|-
| Quarterfinals || [[Brad Kippel]] || [[Bill Bisco]]
|}}

== Finals ==

{stage_table("Finish", finals, "final")}

== Semifinals ==

{stage_table("Finish", t4, "t4")}

== Top 8 ==

{stage_table("Finish", t8, "t8")}

== See also ==

* [[List of SWCCG tournaments]]
* [[2026 Retro GEMP Match Play Championship (Premiere to DSII)]]
* [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/2025-04-retro-gemp-match-play-championship-premiere-to-dsii-may-to-july-2025/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2025-04-retro-gemp-match-play-championship-premiere-to-dsii-may-to-july-2025/ 2025-04 Retro Gemp Match Play Championship (Premiere to DSII) – May to July 2025], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:2025]]
"""
    write_page("2025_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki", body)


def write_charity(dt, hl):
    body = f"""'''2025 Online Retro Event for Charity''' was a Players Committee Premiere-to-Virtual Set 3 event on GEMP. The published Top 8 starts with [[Joe Horbey]].<ref name="pc">https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/</ref>

== Format ==

* '''Environment:''' Premiere to Virtual Set 3
* '''Platform:''' GEMP
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1559 2025 Retro Charity Event Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?p=1439519#p1439519 forum p=1439519]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YR-JV379jsT7S5GYTvy_hkk YouTube playlist]

== Top 8 ==

{people_table("Finish", CHARITY_T8, dt, hl, True)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/ 2025-06 Online Retro Event for Charity – Premiere to Virtual Set 3], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:2025]]
"""
    write_page("2025_Online_Retro_Event_for_Charity.wiki", body)


def write_standings_hubs():
    # Euro / OCS / Vegas / Morristown / Regionals hubs with Dark/Light deck
    # tables are owned by generate_html_missing.py and generate_vegas_morris.py.
    return
    euro_t4 = ["Emil Wallin", "Justin Branch", "Patrik Csapi", "Cedrik Vanderhaegen"]
    euro_d1 = numbered(ROOT / "encyclopedia/pc-2025/euro.txt", "Day 1")
    e_rows = ['{| class="wikitable sortable"', "! Finish !! Player"]
    for i, p in enumerate(euro_t4, 1):
        e_rows += ["|-", f"| {i} || [[{p}]]"]
    e_rows.append("|}")
    d_rows = ['{| class="wikitable sortable"', "! Day 1 !! Player"]
    for i, p in enumerate(euro_d1, 1):
        d_rows += ["|-", f"| {i} || [[{p}]]"]
    d_rows.append("|}")
    write_page(
        "2025_European_Championship.wiki",
        f"""'''2025 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 20–21 September 2025. [[Emil Wallin]] won.<ref name="pc">https://www.starwarsccg.org/2025-08-european-championship-bochum-germany-sept-20-21-2025/</ref>

This year is listed with other ECs on [[European Championships]].

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' Bochum, Germany
* '''Dates:''' 20–21 September 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1561 2025 European Championship Forum]

== Top 4 ==

{chr(10).join(e_rows)}

== Day 1 ==

{chr(10).join(d_rows)}

== See also ==

* [[European Championships]]
* [[2026 European Championship]]
* [[List of SWCCG tournaments]]
* [https://www.starwarsccg.org/2025-08-european-championship-bochum-germany-sept-20-21-2025/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2025-08-european-championship-bochum-germany-sept-20-21-2025/ 2025-08 European Championship – Bochum, Germany (Sept. 20-21, 2025)], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
""",
    )

    write_page(
        "2025_Online_Championship_Series_Playoffs.wiki",
        f"""'''2025 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP, October–November 2025. [[Patrick Johnson]] (seed 6) defeated [[Greg Shaw]] (seed 9) in the Finals.<ref name="pc">https://www.starwarsccg.org/2025-10-online-championship-series-ocs-playoffs-oct-to-nov-2025/</ref>

== Format ==

* '''Environment:''' [[Open]]
* '''Platform:''' GEMP
* '''Dates:''' October–November 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1543 2025 OCS Playoffs Forum]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YSYv6Dzhaem9Vt_IGBvO5gf YouTube playlist]

== Bracket ==

{{| class="wikitable"
! Round !! Winner !! Defeated
|-
| Finals || [[Patrick Johnson]] || [[Greg Shaw]]
|-
| Semifinals || [[Patrick Johnson]] || [[Matthew Harrison-Trainor]]
|-
| Semifinals || [[Greg Shaw]] || [[Joe Olson]]
|-
| Quarterfinals || [[Matthew Harrison-Trainor]] || [[Brad Kippel]]
|-
| Quarterfinals || [[Patrick Johnson]] || [[Kyle Krueger]]
|-
| Quarterfinals || [[Joe Olson]] || [[Anthony Howard]]
|-
| Quarterfinals || [[Greg Shaw]] || [[Jarad Konsker]]
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/2025-10-online-championship-series-ocs-playoffs-oct-to-nov-2025/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2025-10-online-championship-series-ocs-playoffs-oct-to-nov-2025/ 2025-10 Online Championship Series (OCS) Playoffs – Oct. to Nov. 2025], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
""",
    )

    vegas_t8 = numbered(ROOT / "encyclopedia/pc-2025/vegas.txt", "Day 2") or [
        "Joe Olson",
        "Sam Tashima",
        "Logan Pietig",
        "Jeff Lavigne",
        "Mike Kessling",
        "Dennis Reinhardt",
        "Brad Reinhold",
        "Karl Koenig",
    ]
    v_rows = ['{| class="wikitable sortable"', "! Finish !! Player"]
    for i, p in enumerate(vegas_t8[:8], 1):
        v_rows += ["|-", f"| {i} || [[{p}]]"]
    v_rows.append("|}")
    write_page(
        "2025_Las_Vegas_Grand_Prix.wiki",
        f"""'''2025 Las Vegas Grand Prix''' was a Players Committee major event in Las Vegas, Nevada, 11–12 January 2025. [[Joe Olson]] won.<ref name="pc">https://www.starwarsccg.org/2025-01-las-vegas-grand-prix-las-vegas-nevada-jan-11-12-2025/</ref><ref name="wrap">https://www.starwarsccg.org/2025-las-vegas-grand-prix-wrap-up-joe-olson-starts-the-year-off-strong/</ref>

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' Las Vegas, Nevada
* '''Dates:''' 11–12 January 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1541 2025 Las Vegas Grand Prix Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=85271 forum t=85271]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YQyN9rdxO76-KtAPoVIbhCA YouTube playlist]

== Top 8 ==

{chr(10).join(v_rows)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]]
* [https://www.starwarsccg.org/2025-01-las-vegas-grand-prix-las-vegas-nevada-jan-11-12-2025/ PC results]
* [https://www.starwarsccg.org/2025-las-vegas-grand-prix-wrap-up-joe-olson-starts-the-year-off-strong/ Wrap-up]

== Sources ==

* [https://www.starwarsccg.org/2025-01-las-vegas-grand-prix-las-vegas-nevada-jan-11-12-2025/ 2025-01 Las Vegas Grand Prix, Las Vegas, Nevada (Jan. 11-12, 2025)], starwarsccg.org
* [https://www.starwarsccg.org/2025-las-vegas-grand-prix-wrap-up-joe-olson-starts-the-year-off-strong/ 2025 Las Vegas Grand Prix Wrap-Up: Joe Olson Starts the Year off Strong]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
""",
    )

    morris_t8 = [
        "Greg Shaw",
        "Jeff Lavigne",
        "Hayes Hunter",
        "Chris Gogolen",
        "Bill Kafer",
        "Mike Kessling",
        "AJ Hatoum",
        "Matt Sokol",
    ]
    m_rows = ['{| class="wikitable sortable"', "! Finish !! Player"]
    for i, p in enumerate(morris_t8, 1):
        m_rows += ["|-", f"| {i} || [[{p}]]"]
    m_rows.append("|}")
    write_page(
        "2025_Morristown_Melee.wiki",
        f"""'''2025 Morristown Melee''' was a Players Committee major event in Morristown, New Jersey, 24–27 April 2025. [[Greg Shaw]] defeated [[Jeff Lavigne]] in the Final Confrontation.<ref name="pc">https://www.starwarsccg.org/2025-02-morristown-melee-morristown-new-jersey-apr-24-27-2025/</ref><ref name="wrap">https://www.starwarsccg.org/2025-morristown-melee-wrap-up-greg-shaw-victorious/</ref>

Friday team event: [[Matt Sokol]] and [[Mike d'Amboise]]. Sunday Consolation: [[Jarad Konsker]]. Tournament Advocate: [[Chris Schoenthal]]. Streaming: [[Robbie Hendon]] and [[Garrett Larson]].<ref name="wrap" />

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' Morristown, New Jersey
* '''Dates:''' 24–27 April 2025
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1554 2025 Morristown Melee Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=85566 forum t=85566]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YRDizhlUKOtAE2RXQamMzwr YouTube playlist]

== Top 8 ==

{chr(10).join(m_rows)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]]
* [https://www.starwarsccg.org/2025-02-morristown-melee-morristown-new-jersey-apr-24-27-2025/ PC results]
* [https://www.starwarsccg.org/2025-morristown-melee-wrap-up-greg-shaw-victorious/ Wrap-up]

== Sources ==

* [https://www.starwarsccg.org/2025-02-morristown-melee-morristown-new-jersey-apr-24-27-2025/ 2025-02 Morristown Melee, Morristown, New Jersey (Apr. 24-27, 2025)], starwarsccg.org
* [https://www.starwarsccg.org/2025-morristown-melee-wrap-up-greg-shaw-victorious/ 2025 Morristown Melee Wrap-up – Greg Shaw Victorious]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2025]]
""",
    )

    regs = [
        ("Coruscant Regionals", "Long Island City, New York", "15 November 2025", "Greg Shaw"),
        ("Corellia Regionals", "Columbus, Ohio", "8 November 2025", "Hayes Hunter"),
        ("Nal Hutta Regionals", "Indianapolis, Indiana", "21 September 2025", "Brian Fred"),
        ("Tatooine Regionals", "Denver, Colorado", "14 September 2025", "Mark Billings"),
        ("Endor Regionals", "Federal Way, Washington", "16 August 2025", "Justin Miyashiro"),
        ("Bespin Regionals", "St. Paul, Minnesota", "28 June 2025", "Charlie Arlandson"),
        ("Naboo Regionals", "Liverpool, United Kingdom", "21 June 2025", "Hayes Hunter"),
    ]
    r_rows = ['{| class="wikitable sortable"', "! Event !! Date !! Site !! Winner"]
    for name, site, date, w in regs:
        r_rows += ["|-", f"| {name} || {date} || {site} || [[{w}]]"]
    r_rows.append("|}")
    write_page(
        "2025_Regional_Championships.wiki",
        f"""'''2025 Regional Championships''' are the Players Committee 2025 regional events, posted together on one PC results page.<ref name="pc">https://www.starwarsccg.org/2025-03-regional-championships/</ref>

== Results ==

Winners as published (newest first on that page).<ref name="pc" />

{chr(10).join(r_rows)}

== See also ==

* [[List of SWCCG tournaments]]
* [[2026 Regional Championships]]
* [[Tournaments]]
* [https://www.starwarsccg.org/2025-03-regional-championships/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2025-03-regional-championships/ 2025-03 Regional Championships], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:2025]]
""",
    )


def patch_list():
    p = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = p.read_text(encoding="utf-8")
    if "== 2025 ==" in text:
        return
    block = """
== 2025 ==

{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Winner
|-
| 2025-10 || [[2025 Online Championship Series Playoffs|Online Championship Series Playoffs]] || October–November 2025 || GEMP || [[Patrick Johnson]]
|-
| 2025-09 || [[2025 World Championship|World Championship]] || 4–5 October 2025 || Seattle, Washington || [[Greg Shaw]]
|-
| 2025-08 || [[2025 European Championship|European Championship]] || 20–21 September 2025 || Bochum, Germany || [[Emil Wallin]]
|-
| 2025-07 || [[2025 U.S. National Championship|U.S. National Championship]] || 23–24 August 2025 || Columbus, Ohio || [[Matt Scott]]
|-
| 2025-06 || [[2025 Online Retro Event for Charity|Online Retro Event for Charity]] || May–June 2025 || GEMP || [[Joe Horbey]]
|-
| 2025-05 || [[2025 Ninth Annual GEMPC|Ninth Annual GEMPC]] || May–July 2025 || GEMP || [[Matthew Harrison-Trainor]]
|-
| 2025-04 || [[2025 Retro GEMP Match Play Championship (Premiere to DSII)|Retro GEMP Match Play Championship (Premiere to DSII)]] || May–July 2025 || GEMP || [[Timo Dusel]]
|-
| 2025-03 || [[2025 Regional Championships|Regional Championships]] || 2025 || various || —
|-
| 2025-02 || [[2025 Morristown Melee|Morristown Melee]] || 24–27 April 2025 || Morristown, New Jersey || [[Greg Shaw]]
|-
| 2025-01 || [[2025 Las Vegas Grand Prix|Las Vegas Grand Prix]] || 11–12 January 2025 || Las Vegas, Nevada || [[Joe Olson]]
|}

"""
    text = text.replace("== Decipher World Championships ==", block + "== Decipher World Championships ==")
    if "[[Category:2025]]" not in text:
        text = text.replace("[[Category:2026]]", "[[Category:2026]]\n[[Category:2025]]")
    p.write_text(text, encoding="utf-8", newline="\n")


def write_cat():
    write_page(
        "Category_2025.wiki",
        """Pages for 2025 events, players, and decklists.

* [[List of SWCCG tournaments]]
* [[2025 World Championship]]
* [[European Championships]]

[[Category:Tournaments]]
""",
    )


def main():
    PAGES.mkdir(parents=True, exist_ok=True)
    process_gemp()
    write_standings_hubs()
    patch_list()
    write_cat()
    # link 2025 EC on European Championships
    ep = PAGES / "European_Championships.wiki"
    t = ep.read_text(encoding="utf-8")
    t = t.replace(
        "| 2025 || 2025 European Championship || Bochum, Germany || [[Emil Wallin]]",
        "| 2025 || [[2025 European Championship]] || Bochum, Germany || [[Emil Wallin]]",
    )
    ep.write_text(t, encoding="utf-8", newline="\n")
    print("2025 hubs done")


if __name__ == "__main__":
    main()
