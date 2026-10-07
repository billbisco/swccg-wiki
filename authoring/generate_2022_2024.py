#!/usr/bin/env python3
"""2022–2024 tournament hubs + GEMP decks + player stubs."""
from __future__ import annotations

import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2026_remaining as g26  # noqa: E402
import update_gempc_start_fields as ug  # noqa: E402
from generate_2026_remaining import upsert_stub  # noqa: E402
from generate_2026_sdso import load_bp_simple, parse_gemp_counts, wiki_fname  # noqa: E402
from parse_gemp_names import parse_name  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
MEDIA = ROOT / "y2022-2024-media"
TD = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026")
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
EC = PAGES / "European_Championships.wiki"

EVENTS = [
    {
        "key": "24worlds",
        "folders": ["2024-worlds"],
        "title": "2024 World Championship",
        "year": "2024",
        "tag": "2024-09",
        "dates": "19–22 September 2024",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2024 World Championship''' was the Players Committee World Championship in Bochum, Germany, 19–22 September 2024. [[Joe Olson]] defeated [[Emil Wallin]] in the Final Confrontation. Friday team event winners: [[Emil Wallin]] and [[Brian Fred]].",
        "pc": "https://www.starwarsccg.org/2024-09-world-championships-bochum-germany-19-22-september-2024/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=84844",
        "deck_prefix": "2024 Worlds",
        "list_label": "World Championship",
    },
    {
        "key": "24nac",
        "folders": ["2024-nac", "2024-nac-t8"],
        "title": "2024 North American Continental Championship",
        "year": "2024",
        "tag": "2024-08",
        "dates": "9–11 August 2024",
        "site": "New Brunswick, New Jersey",
        "format": "[[Open]]",
        "winner": "Brian Fred",
        "lead": "'''2024 North American Continental Championship''' was the Players Committee North American Continental Championship at the Heldrich Hotel in New Brunswick, New Jersey, 9–11 August 2024. [[Brian Fred]] finished 1st in the Day 2 Top 8 cut.",
        "pc": "https://www.starwarsccg.org/2024-08-north-american-continental-championship-new-brunswick-new-jersey-august-9-112024/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?p=1427819#p1427819",
        "deck_prefix": "2024 NAC",
        "list_label": "North American Continental Championship",
    },
    {
        "key": "24retro",
        "folders": ["2024-retro"],
        "title": "2024 Online Retro Event for Charity",
        "year": "2024",
        "tag": "2024-07",
        "dates": "11 May – 6 July 2024",
        "site": "GEMP",
        "format": "[[Premiere - Death Star II]]",
        "winner": "Patrick Lima",
        "lead": "'''2024 Online Retro Event for Charity''' was the Players Committee Classic No-V (Premiere to Death Star II) charity event on GEMP. [[Patrick Lima]] finished 1st among the published lists.",
        "pc": "https://www.starwarsccg.org/2024-07-online-retro-event-for-charity-classic-no-v/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?p=1426779#p1426779",
        "deck_prefix": "2024 Charity",
        "list_label": "Online Retro Event for Charity (Classic No-V)",
    },
    {
        "key": "24eclipse",
        "folders": ["2024-eclipse"],
        "title": "2024 Eclipse Major",
        "year": "2024",
        "tag": "2024-04",
        "dates": "5–7 April 2024",
        "site": "Indianapolis, Indiana",
        "format": "[[Open]]",
        "winner": "Sam Tashima",
        "lead": "'''2024 Eclipse Major''' was a Players Committee major event in Indianapolis, Indiana, 5–7 April 2024. [[Sam Tashima]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2024-04-eclipse-major-indianapolis-indiana-apr-5-7/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=84424",
        "deck_prefix": "2024 Eclipse",
        "list_label": "Eclipse Major",
    },
    {
        "key": "24sss",
        "folders": ["2024-sss"],
        "title": "2024 Supreme Southern Showdown",
        "year": "2024",
        "tag": "2024-01",
        "dates": "12–14 January 2024",
        "site": "Atlanta, Georgia",
        "format": "[[Open]]",
        "winner": "Jeff Lavigne",
        "lead": "'''2024 Supreme Southern Showdown''' was a Players Committee major event in Atlanta, Georgia, 12–14 January 2024. [[Jeff Lavigne]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2024-01-supreme-southern-showdown-atlanta-georgia-jan-12-14/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?p=1420146#p1420146",
        "deck_prefix": "2024 SSS",
        "list_label": "Supreme Southern Showdown",
    },
    {
        "key": "23ocs",
        "folders": ["2023-ocs"],
        "title": "2023 Online Championship Series Playoffs",
        "year": "2023",
        "tag": "2023-10",
        "dates": "October–November 2023",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Justin Desai",
        "lead": "'''2023 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP. [[Justin Desai]] defeated [[Timo Dusel]] in the Finals.",
        "pc": "https://www.starwarsccg.org/2023-10-2023-online-championship-series-playoffs/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?p=1417683",
        "deck_prefix": "2023 OCS",
        "list_label": "Online Championship Series Playoffs",
    },
    {
        "key": "23outrider",
        "folders": ["2023-outrider"],
        "title": "2023 Outrider Cup III",
        "year": "2023",
        "tag": "2023-11",
        "dates": "16–28 January 2024",
        "site": "GEMP (teams)",
        "format": "[[Open]]",
        "winner": "[[Team USA]]",
        "lead": "'''2023 Outrider Cup III''' was the Players Committee biennial Europe versus United States team event on GEMP, 16–28 January 2024. Team USA defeated Team Europe 7–5.",
        "pc": "https://www.starwarsccg.org/2023-11-outrider-cup-iii/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?p=1420092",
        "deck_prefix": "2023 Outrider Cup III",
        "list_label": "Outrider Cup III",
    },
    {
        "key": "23retro",
        "folders": ["2023-retro"],
        "title": "2023 Online Retro Event",
        "year": "2023",
        "tag": "2023-06",
        "dates": "April–June 2023",
        "site": "GEMP",
        "format": "[[Premiere - Special Edition]]",
        "winner": "[[Timo Dusel]]",
        "lead": "'''2023 Online Retro Event''' was the Players Committee Premiere–Special Edition retro event on GEMP, April–June 2023. [[Timo Dusel]] finished 1st.",
        "pc": "https://www.starwarsccg.org/2023-06-annual-online-retro-event-premiere-special-edition-april-june-2023/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=83197",
        "deck_prefix": "2023 Retro",
        "list_label": "Online Retro Event (Premiere–Special Edition)",
    },
    {
        "key": "23egp",
        "folders": ["2023-egp"],
        "title": "2023 Endor Grand Prix",
        "year": "2023",
        "tag": "2023-09",
        "dates": "27–29 October 2023",
        "site": "Seattle, Washington",
        "format": "[[Open]]",
        "winner": "Hayes Hunter",
        "lead": "'''2023 Endor Grand Prix''' was a Players Committee major event in Seattle, Washington, 27–29 October 2023. [[Hayes Hunter]] finished 1st in Day 2. Friday team event winners: [[Blake Silkwood]] and [[Ryan Sersen]].",
        "pc": "https://www.starwarsccg.org/2023-08-endor-grand-prix-seattle-washington-oct-27-29/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=83759",
        "deck_prefix": "2023 EGP",
        "list_label": "Endor Grand Prix",
    },
    {
        "key": "23gempc",
        "folders": ["2023-gempc"],
        "title": "2023 Seventh Annual GEMPC",
        "year": "2023",
        "tag": "2023-05",
        "dates": "January–April 2023",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Tom Strother",
        "lead": "'''2023 Seventh Annual GEMPC''' (GEMPC7) was the Players Committee online match-play championship on GEMP, January–April 2023. [[Tom Strother]] defeated [[Mike Kessling]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2023-05-gempc7-match-play-tournament-jan-april-2023/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?p=1404368",
        "deck_prefix": "2023 GEMPC",
        "list_label": "Seventh Annual GEMPC",
    },
    {
        "key": "23nats",
        "folders": ["2023-nats"],
        "title": "2023 U.S. National Championship",
        "year": "2023",
        "tag": "2023-04",
        "dates": "1–2 April 2023",
        "site": "Minneapolis, Minnesota",
        "format": "[[Open]]",
        "winner": "Hayes Hunter",
        "lead": "'''2023 U.S. National Championship''' was the Players Committee U.S. National Championship in Minneapolis, Minnesota, 1–2 April 2023. [[Hayes Hunter]] finished 1st in the Top 8.",
        "pc": "https://www.starwarsccg.org/2023-04-us-nationals-minneapolis-minnesota-april-1-2/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=82668",
        "deck_prefix": "2023 US Nationals",
        "list_label": "U.S. National Championship",
    },
    {
        "key": "23worlds",
        "folders": ["2023-worlds"],
        "title": "2023 World Championship",
        "year": "2023",
        "tag": "2023-07",
        "dates": "11–13 August 2023",
        "site": "Morristown, New Jersey",
        "format": "[[Open]]",
        "winner": "Hayes Hunter",
        "lead": "'''2023 World Championship''' was the Players Committee World Championship in Morristown, New Jersey, 11–13 August 2023. [[Hayes Hunter]] finished 1st in Day 2. Friday team event winners: [[Justin Desai]] and [[Jonny Chu]] (Kashyyyk Train of Dominance); runners-up [[Scott Lingrell]] and [[Bill Bacheler]].",
        "pc": "https://www.starwarsccg.org/2023-07-world-championships-morristown-new-jersey-aug-11-13/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=83395",
        "deck_prefix": "2023 Worlds",
        "list_label": "World Championship",
    },
    {
        "key": "22worlds",
        "folders": ["2022-worlds", "2022-worlds-rest"],
        "title": "2022 World Championship",
        "year": "2022",
        "tag": "2022-10",
        "dates": "13–16 October 2022",
        "site": "Atlanta, Georgia",
        "format": "[[Open]]",
        "winner": "Justin Desai",
        "lead": "'''2022 World Championship''' was the Players Committee World Championship in Atlanta, Georgia, 13–16 October 2022. [[Justin Desai]] finished 1st in the Top 8.",
        "pc": "https://www.starwarsccg.org/2022-swccg-world-championship/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=81726",
        "deck_prefix": "2022 Worlds",
        "list_label": "World Championship",
    },
    {
        "key": "22nats",
        "folders": ["2022-nats-d1", "2022-nats-d2"],
        "title": "2022 U.S. National Championship",
        "year": "2022",
        "tag": "2022-07",
        "dates": "15–17 July 2022",
        "site": "Minneapolis, Minnesota",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2022 U.S. National Championship''' was the Players Committee U.S. National Championship in Minneapolis, Minnesota, 15–17 July 2022. [[Joe Olson]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2022-07-us-national-championship/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=81186",
        "deck_prefix": "2022 US Nationals",
        "list_label": "U.S. National Championship",
    },
    {
        "key": "22retro",
        "folders": ["2022-retro"],
        "title": "2022 Decipher Cards Only Retro Event",
        "year": "2022",
        "tag": "2022-05",
        "dates": "April–May 2022",
        "site": "GEMP",
        "format": "[[Premiere - Theed Palace]]",
        "winner": "Jonny Chu",
        "lead": "'''2022 Decipher Cards Only Retro Event''' was a Players Committee Decipher-pool retro event on GEMP (Premiere through Theed Palace). [[Jonny Chu]] defeated [[Steve Baroni]] in the Final Confrontation (concession).",
        "pc": "https://www.starwarsccg.org/2022-05-decipher-cards-only-retro-event/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=80902",
        "deck_prefix": "2022 Retro DCO",
        "list_label": "Decipher Cards Only Retro Event",
    },
    {
        "key": "22pc20",
        "folders": ["2022-pc20"],
        "title": "2022 PC20 Tournament",
        "year": "2022",
        "tag": "2022-04",
        "dates": "30 April 2022",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Tom Strother",
        "lead": "'''2022 PC20 Tournament''' was the Players Committee 20th-anniversary constructed event on GEMP. [[Tom Strother]] defeated [[Mike Kessling]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2022-04-pc20-tournament/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=80756",
        "deck_prefix": "2022 PC20",
        "list_label": "PC20 Tournament",
    },
    {
        "key": "22egp",
        "folders": ["2022-egp"],
        "title": "2022 Endor Grand Prix",
        "year": "2022",
        "tag": "2022-04",
        "dates": "8–10 April 2022",
        "site": "Seattle, Washington",
        "format": "[[Open]]",
        "winner": "Jeff Lavigne",
        "lead": "'''2022 Endor Grand Prix''' was a Players Committee major event in Seattle, Washington, 8–10 April 2022. [[Jeff Lavigne]] finished 1st in the Top 8.",
        "pc": "https://www.starwarsccg.org/2022-endor-grand-prix/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=80665",
        "deck_prefix": "2022 EGP",
        "list_label": "Endor Grand Prix",
    },
    {
        "key": "22gempc",
        "folders": ["2022-gempc"],
        "title": "2022 Sixth Annual GEMPC",
        "year": "2022",
        "tag": "2022-03",
        "dates": "January–March 2022",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Matthew Harrison-Trainor",
        "lead": "'''2022 Sixth Annual GEMPC''' (Batmouse's 6th GEMPC) was the Players Committee online match-play championship on GEMP. [[Matthew Harrison-Trainor]] defeated [[Mike Kessling]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2022-gempc-batmouses-6th-gempc/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=80594",
        "deck_prefix": "2022 GEMPC",
        "list_label": "Sixth Annual GEMPC",
    },
    {
        "key": "22mpc",
        "folders": ["2022-mpc"],
        "title": "2022 Match Play Championship",
        "year": "2022",
        "tag": "2022-01",
        "dates": "21–23 January 2022",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Drew Lichtenstein",
        "lead": "'''2022 Match Play Championship''' was the Players Committee match-play championship on GEMP. [[Drew Lichtenstein]] finished 1st in the published Top 8.",
        "pc": "https://www.starwarsccg.org/2022-match-play-championship/",
        "forum": "https://forum.starwarsccg.org/viewtopic.php?t=80062",
        "deck_prefix": "2022 MPC",
        "list_label": "Match Play Championship",
    },
]

BY_KEY = {e["key"]: e for e in EVENTS}

T8_ORDER = {
    "24worlds": [
        "Joe Olson",
        "Emil Wallin",
        "Hayes Hunter",
        "Jonas Hagen Nørregaard",
        "Timo Dusel",
        "Patrik Csapi",
        "Eric Hunter",
        "Dan Tartaglione",
    ],
    "24nac": [
        "Brian Fred",
        "Greg Shaw",
        "Bill Kafer",
        "Joe Olson",
        "Chris Gogolen",
        "Sam Tashima",
        "Phil Aasen",
        "Matt Sokol",
    ],
    "24eclipse": [
        "Sam Tashima",
        "Jeff Lavigne",
        "Casey Anis",
        "Hayes Hunter",
        "Chris Kelly",
        "Stephen Cellucci",
        "Mike Kessling",
        "Justin Carulli",
    ],
    "24sss": [
        "Jeff Lavigne",
        "Hayes Hunter",
        "Dennis Reinhardt",
        "Bill Kafer",
        "Sam Tashima",
        "Scott Lingrell",
        "Matthew Harrison-Trainor",
        "Robbie Hendon",
    ],
    "24retro": [
        "Patrick Lima",
        "Jonathan Chu",
        "Brad Kippel",
        "Michael Pistone",
        "Joe Horbey",
        "Paul Feldman",
        "Eddie Szwabowski",
        "David Garcia",
    ],
    "23worlds": [
        "Hayes Hunter",
        "Casey Anis",
        "Ryan Jellison",
        "Brian Fred",
        "Bryan Mischke",
        "Anthony Howard",
        "Jonny Chu",
        "Joe Olson",
    ],
    "23egp": [
        "Hayes Hunter",
        "Chris Wirfs",
        "Anthony Howard",
        "Steve Brentson",
        "Mike Kessling",
        "Jacy Smith",
        "Sam Tashima",
        "Ryan Sersen",
    ],
    "23nats": [
        "Hayes Hunter",
        "Charlie Arlandson",
        "Anthony Howard",
        "Conor Britain",
        "Greg Shaw",
        "Jeff Lavigne",
        "Sam Tashima",
        "Joe Olson",
    ],
    "23gempc": ["Tom Strother", "Mike Kessling"],
    "22worlds": [
        "Justin Desai",
        "Matthew Harrison-Trainor",
        "Joe Olson",
        "Hayes Hunter",
        "Ryan Jellison",
        "Greg Shaw",
        "Kyle Krueger",
        "Jeremy DiPaolo",
    ],
    "22nats": [
        "Joe Olson",
        "Brad Reinhold",
        "Brian Fred",
        "Jeff Lavigne",
        "Charlie Arlandson",
        "Greg Shaw",
        "Mike Kessling",
        "Matt Wadden",
    ],
    "22egp": [
        "Jeff Lavigne",
        "Brad Reinhold",
        "Brian Fred",
        "Joe Olson",
        "Koen Meijssen",
        "Bill Kafer",
        "Jeremy DiPaolo",
        "Kyle Kallin",
    ],
    "22gempc": ["Matthew Harrison-Trainor", "Mike Kessling"],
    "22mpc": [
        "Drew Lichtenstein",
        "Eric Hunter",
        "Charlie Arlandson",
        "Mike d'Amboise",
        "Mike Kessling",
        "Matt Sokol",
        "Justin Miyashiro",
        "Greg Shaw",
    ],
    "22pc20": ["Tom Strother", "Mike Kessling"],
    "22retro": ["Jonny Chu", "Steve Baroni", "Justin Desai", "Casey Anis"],
}


def ordered_players(found: list[str], preferred: list[str]) -> list[str]:
    seen = []
    have = set(found)
    for p in preferred:
        if p in have and p not in seen:
            seen.append(p)
    for p in found:
        if p not in seen:
            seen.append(p)
    return seen


def deck_title(ev, player, t8, side, obj, stage):
    meta = BY_KEY[ev]
    pfx = meta["deck_prefix"]
    if stage == "final":
        pfx = f"{pfx} Finals"
    elif stage == "t4":
        pfx = f"{pfx} Semifinals"
    elif stage == "qf":
        pfx = f"{pfx} Quarterfinals"
    elif stage == "t16":
        pfx = f"{pfx} Top 16"
    elif t8:
        pfx = f"{pfx} Top 8"
    title = f"{pfx} {player} {side} {obj}"
    return re.sub(r"[#<>\[\]\|\{\}]", "", title).replace("  ", " ").strip()


def event_title(ev):
    return BY_KEY[ev]["title"]


def refs():
    return """{{#if:1|<nowiki />
<h2>References</h2>
<references />}}"""


def people_table(heading, players, dt, hl, t8):
    bits = ['{| class="wikitable sortable"', f"! {heading} !! Player !! Dark !! Light"]
    for i, p in enumerate(players, 1):
        bits += [
            "|-",
            f"| {i} || [[{p}]] || {cell(dt, hl, p, t8, 'DS')} || {cell(dt, hl, p, t8, 'LS')}",
        ]
    bits.append("|}")
    return "\n".join(bits)


def cell(dt, hl, player, t8, side):
    page = dt.get((player, t8, side))
    if not page:
        return "—"
    return f"[[{page}|{hl.get(page, page)}]]"


def write_hub(meta, dt, hl, t8_players, d1_players):
    t8_tbl = people_table("Finish", t8_players, dt, hl, True) if t8_players else ""
    d1_tbl = people_table("Day 1", d1_players, dt, hl, False) if d1_players else ""
    t8_sec = f"== Top 8 ==\n\n{t8_tbl}\n\n" if t8_tbl else ""
    d1_sec = f"== Day 1 ==\n\nPublished constructed lists (every published pair, not Top 8 only).\n\n{d1_tbl}\n\n" if d1_tbl else ""
    if not t8_sec and d1_sec:
        d1_sec = d1_sec.replace("== Day 1 ==", "== Decklists ==")
    fmt_env = meta["format"]
    body = f"""{meta["lead"]}<ref name="pc">{meta["pc"]}</ref>

== Format ==

* '''Environment:''' {fmt_env}
* '''Site:''' {meta["site"]}
* '''Dates:''' {meta["dates"]}
* '''GEMP importable decks:''' [{meta["forum"]} forum]

{t8_sec}{d1_sec}== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [{meta["pc"]} PC results]

== Sources ==

* [{meta["pc"]} {meta["title"]}], starwarsccg.org
* [{meta["forum"]} GEMP Importable Decklists]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:{meta["year"]}]]
"""
    (PAGES / wiki_fname(meta["title"])).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


HTML_STUBS = [
    {
        "title": "2024 Online Championship Series Playoffs",
        "year": "2024",
        "tag": "2024-10",
        "dates": "October–November 2024",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Matthew Harrison-Trainor",
        "lead": "'''2024 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP, October–November 2024. [[Matthew Harrison-Trainor]] won the Finals.",
        "pc": "https://www.starwarsccg.org/2024-10-online-championship-series-ocs-playoffs-oct-nov-2024/",
        "list_label": "Online Championship Series Playoffs",
    },
    {
        "title": "2024 Retro Online Championship Series Playoffs",
        "year": "2024",
        "tag": "2024-11",
        "dates": "December 2024",
        "site": "GEMP",
        "format": "[[Premiere - Death Star II]]",
        "winner": "Paul Todd Feldman",
        "lead": "'''2024 Retro Online Championship Series Playoffs''' (ROCS) was the Players Committee retro OCS playoff on GEMP, December 2024. [[Paul Todd Feldman]] won the Finals.",
        "pc": "https://www.starwarsccg.org/2024-11-retro-online-championship-series-rocs-playoffs-dec-2024/",
        "list_label": "Retro Online Championship Series Playoffs",
    },
    {
        "title": "2024 Champions League",
        "year": "2024",
        "tag": "2024-12",
        "dates": "December 2024 – February 2025",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Matthew Harrison-Trainor",
        "lead": "'''2024 Champions League''' was the Players Committee Champions League knockout on GEMP, December 2024 to February 2025. [[Matthew Harrison-Trainor]] won the Finals.",
        "pc": "https://www.starwarsccg.org/2024-12-champions-league-dec-2024-feb-2025/",
        "list_label": "Champions League",
    },
    {
        "title": "2024 European Championship",
        "year": "2024",
        "tag": "2024-06",
        "dates": "17 May 2024",
        "site": "Copenhagen, Denmark",
        "format": "[[Open]]",
        "winner": "Casper Jørgensen",
        "lead": "'''2024 European Championship''' was the Players Committee European Championship in Copenhagen, Denmark, 17 May 2024. [[Casper Jørgensen]] finished 1st (7–1, SOS over [[Emil Wallin]]).",
        "pc": "https://www.starwarsccg.org/2024-06-european-championships-copenhagen-denmark-may-17th-2024/",
        "list_label": "European Championship",
    },
    {
        "title": "2024 Jawa Cup",
        "year": "2024",
        "tag": "2024-03",
        "dates": "13–25 February 2024",
        "site": "GEMP",
        "format": "[[Jawa Format]]",
        "winner": "Conor Britain",
        "lead": "'''2024 Jawa Cup''' was the Players Committee Jawa Format event on GEMP, 13–25 February 2024. [[Conor Britain]] finished 1st in the published Top 8.",
        "pc": "https://www.starwarsccg.org/2024-03-jawa-cup-top-8-feb-13-25-on-gemp/",
        "list_label": "Jawa Cup",
    },
    {
        "title": "2024 Eighth Annual GEMPC",
        "year": "2024",
        "tag": "2024-05",
        "dates": "February–May 2024",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Matthew Harrison-Trainor",
        "lead": "'''2024 Eighth Annual GEMPC''' was the Players Committee online match-play championship on GEMP, February–May 2024. [[Matthew Harrison-Trainor]] won the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/8th-annual-gempc-feb-may-2024/",
        "list_label": "Eighth Annual GEMPC",
    },
    {
        "title": "2024 Regional Championships",
        "year": "2024",
        "tag": "2024-02",
        "dates": "3 February – 17 November 2024",
        "site": "various",
        "format": "[[Open]]",
        "winner": "—",
        "lead": "'''2024 Regional Championships''' were the Players Committee regional constructed events in 2024.",
        "pc": "https://www.starwarsccg.org/2024-02-regional-championships/",
        "list_label": "Regional Championships",
    },
    {
        "title": "2023 European Championship",
        "year": "2023",
        "tag": "2023-08",
        "dates": "8–10 September 2023",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Cedrik Vanderhaegen",
        "lead": "'''2023 European Championship''' was the Players Committee European Championship in Bochum, Germany, 8–10 September 2023. [[Cedrik Vanderhaegen]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2023-08-european-championships-bochum-germany-sept-8-10/",
        "list_label": "European Championship",
    },
    {
        "title": "2023 Champions League",
        "year": "2023",
        "tag": "2023-01",
        "dates": "January 2023",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2023 Champions League''' was the Players Committee Champions League knockout on GEMP. [[Joe Olson]] won the Finals.",
        "pc": "https://www.starwarsccg.org/2023-1-champions-league-knockout-round/",
        "list_label": "Champions League",
    },
    {
        "title": "2023 San Diego Super Open",
        "year": "2023",
        "tag": "2023-02",
        "dates": "20–22 January 2023",
        "site": "San Diego, California",
        "format": "[[Open]]",
        "winner": "Drew Lichtenstein",
        "lead": "'''2023 San Diego Super Open''' was a Players Committee major event in San Diego, California. [[Drew Lichtenstein]] is listed first among the published constructed pairs.",
        "pc": "https://www.starwarsccg.org/2023-02-san-diego-super-open/",
        "list_label": "San Diego Super Open",
    },
    {
        "title": "2023 Regional Championships",
        "year": "2023",
        "tag": "2023-03",
        "dates": "4 February – 12 November 2023",
        "site": "various",
        "format": "[[Open]]",
        "winner": "—",
        "lead": "'''2023 Regional Championships''' were the Players Committee regional constructed events in 2023.",
        "pc": "https://www.starwarsccg.org/2023-03-2023-regional-championship-events/",
        "list_label": "Regional Championships",
    },
    {
        "title": "2022 Online Championship Series Playoffs",
        "year": "2022",
        "tag": "2022-11",
        "dates": "October–November 2022",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Justin Desai",
        "lead": "'''2022 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP. [[Justin Desai]] defeated [[Bastian Winkelhaus]] in the Finals.",
        "pc": "https://www.starwarsccg.org/2022-ocs-playoffs/",
        "list_label": "Online Championship Series Playoffs",
    },
    {
        "title": "2022 European Championship",
        "year": "2022",
        "tag": "2022-09",
        "dates": "9–11 September 2022",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Emil Wallin",
        "lead": "'''2022 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 9–11 September 2022. [[Emil Wallin]] defeated [[Jonas Hagen Nørregaard]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2022-09-european-championship/",
        "list_label": "European Championship",
    },
    {
        "title": "2022 Regional Championships",
        "year": "2022",
        "tag": "2022-06",
        "dates": "14 May – 5 November 2022",
        "site": "various",
        "format": "[[Open]]",
        "winner": "—",
        "lead": "'''2022 Regional Championships''' were the Players Committee regional constructed events in 2022.",
        "pc": "https://www.starwarsccg.org/2022-06-2022-regional-championship-events/",
        "list_label": "Regional Championships",
    },
    {
        "title": "2022 Jawa Cup",
        "year": "2022",
        "tag": "2022-02",
        "dates": "November 2021 – 13 February 2022",
        "site": "GEMP",
        "format": "[[Jawa Format]]",
        "winner": "Kevin Jaap",
        "lead": "'''2022 Jawa Cup''' was the Players Committee Jawa Format event on GEMP. [[Kevin Jaap]] defeated [[Ryan Jellison]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2021-jawa-cup-top-8/",
        "list_label": "Jawa Cup",
    },
]


def write_html_stub(meta):
    body = f"""{meta["lead"]}<ref name="pc">{meta["pc"]}</ref>

== Format ==

* '''Environment:''' {meta["format"]}
* '''Site:''' {meta["site"]}
* '''Dates:''' {meta["dates"]}

== Decklists ==

Published constructed lists from the PC results page (full tables in the HTML pass).

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [{meta["pc"]} PC results]

== Sources ==

* [{meta["pc"]} {meta["title"]}], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:{meta["year"]}]]
"""
    (PAGES / wiki_fname(meta["title"])).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def patch_indexes(year_rows: dict[str, list[str]]):
    text = LIST.read_text(encoding="utf-8")
    block = []
    for year in ("2024", "2023", "2022"):
        rows = year_rows.get(year) or []
        if not rows:
            continue
        section = f"""== {year} ==

{{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
{chr(10).join(rows)}
|}}

"""
        block.append(section)
    for year in ("2024", "2023", "2022"):
        rows = year_rows.get(year) or []
        if not rows:
            continue
        section = f"""== {year} ==

{{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
{chr(10).join(rows)}
|}}

"""
        if f"== {year} ==" in text:
            text = re.sub(
                rf"== {year} ==.*?(?=\n== )",
                section,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.replace(
                "== Decipher World Championships ==",
                section + "== Decipher World Championships ==",
                1,
            )
    for y in ("2024", "2023", "2022"):
        if f"[[Category:{y}]]" not in text:
            text = text.replace("[[Category:2025]]", f"[[Category:2025]]\n[[Category:{y}]]")
    LIST.write_text(text, encoding="utf-8", newline="\n")

    if EC.exists():
        et = EC.read_text(encoding="utf-8")
        et = et.replace(
            "| 2024 || 2024 European Championship || Copenhagen, Denmark || — || [[Casper Jørgensen]]",
            "| 2024 || [[2024 European Championship]] || Copenhagen, Denmark || [[Open]] || [[Casper Jørgensen]]",
        )
        et = et.replace(
            "| 2023 || 2023 European Championship || Bochum, Germany || — || —",
            "| 2023 || [[2023 European Championship]] || Bochum, Germany || [[Open]] || [[Cedrik Vanderhaegen]]",
        )
        et = et.replace(
            "| 2023 || [[2023 European Championship]] || Bochum, Germany || [[Open]] || —",
            "| 2023 || [[2023 European Championship]] || Bochum, Germany || [[Open]] || [[Cedrik Vanderhaegen]]",
        )
        et = et.replace(
            "| 2022 || 2022 European Championship || Bochum, Germany || — || [[Emil Wallin]]",
            "| 2022 || [[2022 European Championship]] || Bochum, Germany || [[Open]] || [[Emil Wallin]]",
        )
        EC.write_text(et, encoding="utf-8", newline="\n")


def process(year_filter: str | None = None):
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()
    MEDIA.mkdir(parents=True, exist_ok=True)
    STUBS.mkdir(parents=True, exist_ok=True)

    list_rows = defaultdict(list)
    titles = []
    total = 0
    for meta in EVENTS:
        if year_filter and meta["year"] != year_filter:
            continue
        ev = meta["key"]
        parsed = []
        for folder in meta["folders"]:
            d = TD / folder
            if not d.exists():
                print("NOFOLDER", d)
                continue
            for path in sorted(d.glob("*")):
                if not path.is_file():
                    continue
                info = parse_name(folder, path.name)
                if not info:
                    print("SKIP", folder, path.name)
                    continue
                player, t8, side, obj, stage, media = info
                try:
                    counts, cards = parse_gemp_counts(path, by_id, by_title)
                except Exception as e:
                    print("BADXML", path.name, e)
                    continue
                if sum(counts.values()) < 8:
                    print("THIN", path.name, sum(counts.values()))
                    continue
                dest_media = MEDIA / media
                if dest_media.exists() and dest_media.resolve() != path.resolve():
                    media = f"{folder}-{media}"
                    dest_media = MEDIA / media
                shutil.copy2(path, dest_media)
                parsed.append((player, t8, side, obj, media, counts, cards, stage))

        deck_titles = {}
        hub_labels = {}
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            deck_titles[(player, t8, side)] = deck_title(ev, player, t8, side, obj, stage)

        g26.deck_title = lambda e, p, t, s, o, ev=ev, stage_hold=None: deck_title(
            ev, p, t, s, o, "t8" if t else "d1"
        )
        g26.event_title = lambda e, ev=ev: event_title(ev)

        for player, t8, side, obj, media, counts, cards, stage in parsed:
            g26.deck_title = lambda e, p, t, s, o, ev=ev, stage=stage: deck_title(
                ev, p, t, s, o, stage
            )
            other = "LS" if side == "DS" else "DS"
            companion = deck_titles.get((player, t8, other))
            title, body, hub = g26.render_deck(
                ev, player, t8, side, obj, counts, cards, media, companion, bp, dests, title_map
            )
            body = body.replace("[[Category:2026]]", f"[[Category:{meta['year']}]]")
            fmt = meta["format"]
            body = body.replace("* '''Format:''' [[Open]]", f"* '''Format:''' {fmt}")
            stage_label = {
                "final": "Finals",
                "t4": "Semifinals",
                "qf": "Quarterfinals",
                "t16": "Top 16",
                "t8": "Top 8",
                "d1": "Day 1",
            }.get(stage, "Day 1")
            body = re.sub(r"\* '''Stage:''' [^\n]+", f"* '''Stage:''' {stage_label}", body, count=1)
            (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
            hub_labels[title] = hub
            titles.append((title, f"pages/{wiki_fname(title)}"))
            total += 1

        dt, hl = {}, {}
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            title = deck_title(ev, player, t8, side, obj, stage)
            dt[(player, t8, side)] = title
            hl[title] = hub_labels.get(title, title)

        t8_players = []
        d1_players = []
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            if t8:
                if player not in t8_players:
                    t8_players.append(player)
            else:
                if player not in d1_players:
                    d1_players.append(player)
        t8_players = ordered_players(t8_players, T8_ORDER.get(ev, []))
        d1_players = ordered_players(d1_players, T8_ORDER.get(ev, []))
        if ev == "23outrider":
            # Hub and player Finish rows are owned by generate_outrider_teams.py
            print("SKIPHUB", meta["title"])
            list_rows[meta["year"]].append(
                f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || {meta['winner']}"
            )
            continue
        write_hub(meta, dt, hl, t8_players, d1_players)
        titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))

        by_p = defaultdict(list)
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            by_p[player].append(t8)
        for player, t8s in by_p.items():
            rows = []
            if any(t8s):
                rows.append(
                    f"|- \n| {meta['dates']} || [[{meta['title']}]] (Top 8) || {meta['format']} || — || {cell(dt, hl, player, True, 'DS')} || {cell(dt, hl, player, True, 'LS')}"
                )
            if any(not x for x in t8s):
                rows.append(
                    f"|- \n| {meta['dates']} || [[{meta['title']}]] (Day 1) || {meta['format']} || — || {cell(dt, hl, player, False, 'DS')} || {cell(dt, hl, player, False, 'LS')}"
                )
            rows = [r for r in rows if "|| — || —" not in r or "Top 8" in r]
            if rows:
                upsert_stub(player, rows, meta["title"], meta["pc"])
                sp = STUBS / (player.replace(" ", "_") + ".wiki")
                if sp.exists():
                    st = sp.read_text(encoding="utf-8")
                    cat = f"[[Category:{meta['year']}]]"
                    if cat not in st:
                        st = st.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
                        sp.write_text(st, encoding="utf-8", newline="\n")
                    titles.append((player, f"pages/player-stubs/{sp.name}"))

        win = meta["winner"]
        win_cell = f"[[{win}]]" if win not in ("—", "") else "—"
        list_rows[meta["year"]].append(
            f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || {win_cell}"
        )
        print("event", meta["title"], "decks", len(parsed), "t8", len(t8_players), "d1", len(d1_players))

    for meta in HTML_STUBS:
        if year_filter and meta["year"] != year_filter:
            continue
        write_html_stub(meta)
        titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))
        win = meta["winner"]
        win_cell = f"[[{win}]]" if win not in ("—", "") else "—"
        list_rows[meta["year"]].append(
            f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || {win_cell}"
        )
        print("stub", meta["title"])

    def tag_key(row: str) -> str:
        m = re.search(r"\| (\d{4}-\d{2})", row)
        return m.group(1) if m else ""

    for year in list_rows:
        list_rows[year] = sorted(list_rows[year], key=tag_key, reverse=True)

    patch_indexes(list_rows)
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.append(("European Championships", "pages/European_Championships.wiki"))
    seen = {}
    for t, r in titles:
        seen[t] = r
    tsv = ROOT / "y2022-2024-titles.tsv"
    tsv.write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8", newline="\n")
    print("titles", len(seen), "decks", total, "->", tsv)


if __name__ == "__main__":
    year = sys.argv[1] if len(sys.argv) > 1 else None
    process(year)
