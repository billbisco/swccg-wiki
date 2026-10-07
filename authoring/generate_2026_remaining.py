#!/usr/bin/env python3
"""2026 remaining tournament hubs + GEMP decks (US Nats, BWC, Outrider)."""
from __future__ import annotations

import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import update_gempc_start_fields as ug  # noqa: E402
from generate_2026_sdso import (  # noqa: E402
    CAT_LABEL,
    LEFT,
    RIGHT,
    col,
    load_bp_simple,
    parse_gemp_counts,
    wiki_fname,
)

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
MEDIA = ROOT / "remaining-2026-media"
TD = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026")

FILE_PLAYER = {
    "Aasen": "Phil Aasen",
    "Alperstein": "Barry Alperstein",
    "Avery": "Brian Avery",
    "Baity": "Brandon Baity",
    "Cullen": "Wayne Cullen",
    "Fred": "Brian Fred",
    "BFred": "Brian Fred",
    "Fredericks": "Noah Frederiks",
    "Frederiks": "Noah Frederiks",
    "Fredriks": "Noah Frederiks",
    "Gogolen": "Chris Gogolen",
    "Halman": "Kendall Halman",
    "Hatoum": "AJ Hatoum",
    "Horbey": "Joe Horbey",
    "Hunter": "Hayes Hunter",
    "Kafer": "Bill Kafer",
    "Konsker": "Jarad Konsker",
    "Lavigne": "Jeff Lavigne",
    "MScott": "Matt Scott",
    "Olson": "Joe Olson",
    "Pinto": "Joe Pinto",
    "PJohnson": "Patrick Johnson",
    "Shaw": "Greg Shaw",
    "Silkwood": "Blake Silkwood",
    "Tashima": "Sam Tashima",
    "TKelly": "Tom Kelly",
    "Aldred": "Cal Aldred",
    "Brentson": "Steve Brentson",
    "Harpster": "Steve Harpster",
    "Kessling": "Mike Kessling",
    "Koenig": "Karl Koenig",
    "Lingrell": "Scott Lingrell",
    "Moss": "Andrew Moss",
    "Pietig": "Logan Pietig",
    "Reinhardt": "Dennis Reinhardt",
    "Santosuosso": "Thomas Santosuosso",
    "Sersen": "Ryan Sersen",
    "Csapi": "Patrik Csapi",
    "Dusel": "Timo Dusel",
    "Jorgensen": "Casper Jørgensen",
    "Noerregaard": "Jonas Hagen Nørregaard",
    "Vanderhaegen": "Cedrik Vanderhaegen",
    "Wallin": "Emil Wallin",
}

NATS_T8 = [
    "Hayes Hunter",
    "Sam Tashima",
    "Matt Scott",
    "Joe Olson",
    "Phil Aasen",
    "Brian Fred",
    "Jarad Konsker",
    "Greg Shaw",
]
NATS_D1 = [
    "Matt Scott",
    "Hayes Hunter",
    "Joe Olson",
    "Sam Tashima",
    "Phil Aasen",
    "Brian Fred",
    "Jarad Konsker",
    "Greg Shaw",
    "AJ Hatoum",
    "Patrick Johnson",
    "Joe Horbey",
    "Brandon Baity",
    "Jeff Lavigne",
    "Chris Gogolen",
    "Barry Alperstein",
    "Joe Pinto",
    "Bill Kafer",
    "Wayne Cullen",
    "Tom Kelly",
    "Blake Silkwood",
    "Kendall Halman",
    "Brian Avery",
    "Noah Frederiks",
]
BWC_T8 = [
    "Phil Aasen",
    "Hayes Hunter",
    "Sam Tashima",
    "Joe Horbey",
    "Greg Shaw",
    "Andrew Moss",
    "Joe Olson",
    "AJ Hatoum",
]
BWC_D1 = [
    "Hayes Hunter",
    "Phil Aasen",
    "Sam Tashima",
    "Greg Shaw",
    "Andrew Moss",
    "Joe Olson",
    "Joe Horbey",
    "AJ Hatoum",
    "Scott Lingrell",
    "Dennis Reinhardt",
    "Brian Fred",
    "Barry Alperstein",
    "Logan Pietig",
    "Mike Kessling",
    "Ryan Sersen",
    "Jeff Lavigne",
    "Karl Koenig",
    "Steve Harpster",
    "Cal Aldred",
    "Brian Avery",
    "Jarad Konsker",
    "Noah Frederiks",
    "Steve Brentson",
    "Thomas Santosuosso",
]
OC_EUROPE = [
    "Emil Wallin",
    "Casper Jørgensen",
    "Cedrik Vanderhaegen",
    "Jonas Hagen Nørregaard",
    "Patrik Csapi",
    "Timo Dusel",
]
OC_USA = [
    "Joe Olson",
    "Brian Fred",
    "Chris Gogolen",
    "Greg Shaw",
    "Hayes Hunter",
    "Sam Tashima",
]


def parse_name(name: str):
    m = re.match(
        r"26(Nats|BWC|OC)(?: T8)? (\S+)(?: (DS|LS))? (.+)\.(txt|html)$",
        name,
    )
    if not m:
        return None
    ev, token, side, obj, _ext = m.groups()
    player = FILE_PLAYER.get(token, token)
    t8 = " T8 " in f" {name} "
    if side is None:
        side = "LS"
    return ev, player, t8, side, obj, name


def deck_title(ev: str, player: str, t8: bool, side: str, obj: str) -> str:
    if ev == "Nats":
        prefix = "2026 US Nationals Top 8" if t8 else "2026 US Nationals"
    elif ev == "BWC":
        prefix = "2026 BWC Top 8" if t8 else "2026 BWC"
    else:
        prefix = "2026 Outrider Cup IV"
    return f"{prefix} {player} {side} {obj}"


def event_title(ev: str) -> str:
    return {
        "Nats": "2026 U.S. National Championship",
        "BWC": "2026 Boston Winter Classic",
        "OC": "2026 Outrider Cup IV",
    }[ev]


def render_deck(ev, player, t8, side, obj_short, counts, cards, media_name, companion, bp, dests, title_map):
    side_word = "Dark" if side == "DS" else "Light"
    title_dest, obj, ints, effs, loc_title, loc_note, has_ltww = ug.analyze(
        cards, bp, dests, title_map
    )
    if not obj and not loc_title:
        for cid, title, tag in cards:
            if tag == "card" and title == "Yavin 4: Massassi Throne Room":
                loc_title = title
                loc_note = "inferred: no Objective; Throne Room Mains start"
                break
    cat_map = defaultdict(list)
    for (cat, title), n in sorted(counts.items(), key=lambda x: (x[0][0], x[0][1].lower())):
        cat_map[cat].append((n, title, title_dest.get(title)))
    loc_bits = []
    if loc_title:
        ld = title_dest.get(loc_title) or loc_title
        bit = ug.wiki_link(loc_title, ld if ld != loc_title else loc_title)
        if loc_note:
            bit += f" <small>({loc_note})</small>"
        loc_bits.append(bit)
    if obj:
        loc_bits.append(ug.link_pair(obj[0], obj[2]))
    loc_line = "* '''Starting Card:''' " + (" · ".join(loc_bits) if loc_bits else "—")
    int_line = "* '''Starting Interrupt:''' " + (
        " · ".join(ug.link_pair(t, d) for t, c, d in ints) if ints else "—"
    )
    extra = [c for c in cat_map if c not in LEFT and c not in RIGHT]
    left = col(cat_map, LEFT)
    right = col(cat_map, RIGHT)
    if extra:
        right = (right + "\n\n" + col(cat_map, extra)).strip()
    title = deck_title(ev, player, t8, side, obj_short)
    et = event_title(ev)
    stage = "Top 8" if t8 else ("Team event" if ev == "OC" else "Day 1")
    info = [
        f"* '''Player:''' [[{player}]]",
        f"* '''Event:''' [[{et}]]",
        f"* '''Stage:''' {stage}",
        "* '''Format:''' [[Open]]" if ev != "OC" else "* '''Format:''' [[Open]] (team)",
        f"* '''Side:''' [[{side_word}]]",
        loc_line,
        int_line,
        f"* '''GEMP Importable deck:''' [[Media:{media_name}|Download]]",
    ]
    if obj:
        hub_label = ug.visible_label(obj[0], obj[2])
        if obj[2] and " / " in obj[2]:
            hub_label = obj[2].split(" / ")[0]
            if ug.dest_has_v(obj[2]) and not hub_label.endswith(" (V)"):
                hub_label += " (V)"
    else:
        strat = [t for t, c, d in ints if t not in ug.GENERIC_START]
        if strat:
            d = next(d for x, c, d in ints if x == strat[0])
            hub_label = ug.visible_label(strat[0], d)
        elif loc_title:
            hub_label = loc_title
        else:
            hub_label = obj_short
    companion_line = f"* [[{companion}]]" if companion else ""
    body = f"""== Deck info ==
{chr(10).join(info)}

== Decklist ==

{{| class="wikitable" style="width:100%;"
|-
| style="width:50%; vertical-align:top;" |
{left}

| style="width:50%; vertical-align:top;" |
{right}

|}}

== See also ==
* [[{et}]]
* [[List of SWCCG tournaments]]
{companion_line}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:{side_word} Side decks]]
[[Category:2026]]
"""
    return title, body.replace("\r\n", "\n"), hub_label


def upsert_stub(player: str, rows: list[str], et: str, src: str):
    STUBS.mkdir(parents=True, exist_ok=True)
    path = STUBS / (player.replace(" ", "_") + ".wiki")
    extra = f"* [{src} {et}], starwarsccg.org\n"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        text = re.sub(rf"\|-\s*\n\| [^\n]*\[\[{re.escape(et)}\]\][^\n]*\n", "", text)
        if "|}" in text and "Tournament Results" in text:
            text = text.replace("|}\n", "\n".join(rows) + "\n|}\n", 1)
        if f"[[{et}]]" not in text.split("== Tournament Results ==")[0] and "* [[Championships]]" in text:
            text = text.replace("* [[Championships]]", f"* [[{et}]]\n* [[Championships]]", 1)
        if "== Sources ==" in text and src not in text:
            text = text.replace("== Sources ==\n", "== Sources ==\n" + extra, 1)
        path.write_text(text, encoding="utf-8", newline="\n")
        return
    body = f"""'''{player}''' played the [[{et}]].<ref name="pc-rem">[{src} {et}], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{chr(10).join(rows)}
|}}

== See also ==

* [[{et}]]
* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [{src} {et}], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2026]]
"""
    path.write_text(body, encoding="utf-8", newline="\n")


def cell(deck_titles, hub_labels, player, t8, side):
    page = deck_titles.get((player, t8, side))
    if not page:
        return "—"
    return f"[[{page}|{hub_labels.get(page, page)}]]"


def write_nats(deck_titles, hub_labels):
    def row(finish, player, t8):
        return f"| {finish} || [[{player}]] || {cell(deck_titles, hub_labels, player, t8, 'DS')} || {cell(deck_titles, hub_labels, player, t8, 'LS')}"

    t8_rows = ['{| class="wikitable sortable"', "! Finish !! Player !! Dark !! Light"]
    for i, p in enumerate(NATS_T8, 1):
        t8_rows += ["|-", row(i, p, True)]
    t8_rows.append("|}")
    d1_rows = ['{| class="wikitable sortable"', "! Day 1 !! Player !! Dark !! Light"]
    for i, p in enumerate(NATS_D1, 1):
        d1_rows += ["|-", row(i, p, False)]
    d1_rows.append("|}")
    body = f"""'''2026 U.S. National Championship''' was the Players Committee U.S. National Championship at the Heldrich Hotel in New Brunswick, New Jersey, 31 July – 2 August 2026 (constructed 1–2 August). [[Hayes Hunter]] defeated [[Sam Tashima]] in the Final Confrontation.<ref name="pc">https://www.starwarsccg.org/2026-08-u-s-national-championship-new-brunswick-new-jersey-aug-1-2-2026/</ref><ref name="wrap">https://www.starwarsccg.org/2026-us-nationals-wrap-up-win-for-hayes-hunter/</ref>

The main event is [[Open]] constructed: Day 1 Swiss, then Top 8. Friday Warm-Up was won by [[Chris Gogolen]]; Sunday Consolation by [[Patrick Johnson]]. Same weekend: [[2026 Retro U.S. Nationals]], won undefeated by [[Jonny Chu]]. Tournament Advocate / director: [[Chris Schoenthal]]. Streaming: [[Dan Tartaglione]] and [[Garrett Larson]].<ref name="wrap" />

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' New Brunswick, New Jersey (Heldrich Hotel)
* '''Dates:''' 31 July – 2 August 2026
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1597 2026 U.S. Nationals Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=86892 forum t=86892]
* '''Video:''' [https://www.youtube.com/playlist?list=PLI7PBER0cHZw YouTube playlist]

== Top 8 ==

Day 2 finish as published.<ref name="pc" />

{chr(10).join(t8_rows)}

== Day 1 ==

Day 1 lists as published (order on the PC page). Top 8 lists can differ from Day 1.<ref name="pc" />

{chr(10).join(d1_rows)}

== See also ==

* [[2026 Retro U.S. Nationals]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2026-08-u-s-national-championship-new-brunswick-new-jersey-aug-1-2-2026/ PC results]
* [https://www.starwarsccg.org/2026-us-nationals-wrap-up-win-for-hayes-hunter/ Wrap-up]

== Sources ==

* [https://www.starwarsccg.org/2026-08-u-s-national-championship-new-brunswick-new-jersey-aug-1-2-2026/ 2026-08 U.S. National Championship – New Brunswick, New Jersey (Aug. 1-2, 2026)], starwarsccg.org
* [https://www.starwarsccg.org/2026-us-nationals-wrap-up-win-for-hayes-hunter/ 2026 US Nationals Wrap-Up – Win for Hayes Hunter]
* [https://forum.starwarsccg.org/viewtopic.php?t=86892 GEMP Importable Decklists], t=86892
* [https://forum.starwarsccg.org/viewforum.php?f=1597 Forum], f=1597

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""
    (PAGES / "2026_U.S._National_Championship.wiki").write_text(body, encoding="utf-8", newline="\n")


def write_bwc(deck_titles, hub_labels):
    def row(finish, player, t8):
        return f"| {finish} || [[{player}]] || {cell(deck_titles, hub_labels, player, t8, 'DS')} || {cell(deck_titles, hub_labels, player, t8, 'LS')}"

    t8_rows = ['{| class="wikitable sortable"', "! Finish !! Player !! Dark !! Light"]
    for i, p in enumerate(BWC_T8, 1):
        t8_rows += ["|-", row(i, p, True)]
    t8_rows.append("|}")
    d1_rows = ['{| class="wikitable sortable"', "! Day 1 !! Player !! Dark !! Light"]
    for i, p in enumerate(BWC_D1, 1):
        d1_rows += ["|-", row(i, p, False)]
    d1_rows.append("|}")
    body = f"""'''2026 Boston Winter Classic''' was a Players Committee major event in Boston, Massachusetts, 9–11 January 2026 (constructed 10–11 January). [[Phil Aasen]] defeated [[Hayes Hunter]] in the Final Confrontation.<ref name="pc">https://www.starwarsccg.org/2026-01-boston-winter-classic-boston-massachusetts-jan-10-to-11-2026/</ref><ref name="wrap">https://www.starwarsccg.org/2026-boston-winter-classic-wrap-up-phil-aasen-victorious/</ref>

The main event is [[Open]] constructed: Day 1 Swiss, then Top 8. Friday warmup was won by [[Scott Lingrell]]; Sunday Consolation by [[Barry Alperstein]]. Tournament director: [[Casey Anis]]. Streaming: [[Dan Tartaglione]] and [[Garrett Larson]].<ref name="wrap" />

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' Boston, Massachusetts
* '''Dates:''' 9–11 January 2026
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1576 2026 Boston Winter Classic Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?p=1445659#p1445659 forum p=1445659]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YSLTWbvHWtx5fUpPGtT0xII YouTube playlist]

== Top 8 ==

Day 2 finish as published.<ref name="pc" />

{chr(10).join(t8_rows)}

== Day 1 ==

Day 1 lists as published.<ref name="pc" />

{chr(10).join(d1_rows)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2026-01-boston-winter-classic-boston-massachusetts-jan-10-to-11-2026/ PC results]
* [https://www.starwarsccg.org/2026-boston-winter-classic-wrap-up-phil-aasen-victorious/ Wrap-up]

== Sources ==

* [https://www.starwarsccg.org/2026-01-boston-winter-classic-boston-massachusetts-jan-10-to-11-2026/ 2026-01 Boston Winter Classic – Boston, Massachusetts (Jan. 10 to 11, 2026)], starwarsccg.org
* [https://www.starwarsccg.org/2026-boston-winter-classic-wrap-up-phil-aasen-victorious/ 2026 Boston Winter Classic Wrap-up – Phil Aasen Victorious]
* [https://forum.starwarsccg.org/viewtopic.php?p=1445659#p1445659 GEMP Importable Decklists]
* [https://forum.starwarsccg.org/viewforum.php?f=1576 Forum], f=1576

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""
    (PAGES / "2026_Boston_Winter_Classic.wiki").write_text(body, encoding="utf-8", newline="\n")


def write_oc(deck_titles, hub_labels):
    def team_table(name, players):
        bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
        for p in players:
            cap = " <small>(captain)</small>" if p in ("Emil Wallin", "Joe Olson") else ""
            bits += [
                "|-",
                f"| [[{p}]]{cap} || {cell(deck_titles, hub_labels, p, False, 'DS')} || {cell(deck_titles, hub_labels, p, False, 'LS')}",
            ]
        bits.append("|}")
        return f"=== {name} ===\n\n" + "\n".join(bits)

    body = f"""'''2026 Outrider Cup IV''' was the Players Committee biennial Europe vs United States team event on GEMP, January–February 2026. Each side fielded six players. Team Europe's captain was [[Emil Wallin]]; Team USA's captain was [[Joe Olson]].<ref name="pc">https://www.starwarsccg.org/2026-02-outrider-cup-iv/</ref>

The event is [[Open]] constructed. The PC results page lists the two rosters and their lists; this wiki uses the GEMP import zip for printed titles.

== Format ==

* '''Environment:''' [[Open]]
* '''Platform:''' GEMP (teams)
* '''Dates:''' January–February 2026
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1588 Outrider Cup IV Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=86478 forum t=86478]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YTcnh-wm5_BUu8YGPYwH-Ut YouTube playlist]

== Rosters ==

{team_table("Team Europe", OC_EUROPE)}

{team_table("Team USA", OC_USA)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2026-02-outrider-cup-iv/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2026-02-outrider-cup-iv/ 2026-02 Outrider Cup IV], starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?t=86478 Decklist files], t=86478
* [https://forum.starwarsccg.org/viewforum.php?f=1588 Forum], f=1588

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""
    (PAGES / "2026_Outrider_Cup_IV.wiki").write_text(body, encoding="utf-8", newline="\n")


def write_jawa():
    body = """'''2026 Jawa Cup''' was the Players Committee [[Jawa]] format championship on GEMP, December 2025 – March 2026. [[Justin Miyashiro]] (ISB / Watch Your Step in the Finals) defeated [[Andrew Moss]].<ref name="pc">https://www.starwarsccg.org/2026-03-jawa-cup-dec-2025-to-mar-2026/</ref>

== Format ==

* '''Environment:''' [[Jawa]]
* '''Platform:''' GEMP
* '''Dates:''' December 2025 – March 2026
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1587 2026 Jawa Cup Forum]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YT2GfXh-UzVT0r4VU30gAXP Top 8 YouTube playlist]

== Bracket ==

As published on the PC results page (PC strategy labels in Sources links).<ref name="pc" />

{| class="wikitable"
! Round !! Winner !! Defeated
|-
| Finals || [[Justin Miyashiro]] || [[Andrew Moss]]
|-
| Semifinals || [[Justin Miyashiro]] || [[Jason Riendeau]]
|-
| Semifinals || [[Andrew Moss]] || [[Justin Branch]]
|-
| Quarterfinals || [[Justin Miyashiro]] || [[Matt Sokol]]
|-
| Quarterfinals || [[Jason Riendeau]] || [[Chris Kelly]]
|-
| Quarterfinals || [[Andrew Moss]] || [[Bill Bacheler]]
|-
| Quarterfinals || [[Justin Branch]] || [[Sean Luhks]]
|}

== See also ==

* [[List of SWCCG tournaments]]
* [[Jawa]] · [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/2026-03-jawa-cup-dec-2025-to-mar-2026/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2026-03-jawa-cup-dec-2025-to-mar-2026/ 2026-03 Jawa Cup (Dec. 2025 to Mar. 2026)], starwarsccg.org
* [https://forum.starwarsccg.org/viewforum.php?f=1587 Forum], f=1587

{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""
    (PAGES / "2026_Jawa_Cup.wiki").write_text(body, encoding="utf-8", newline="\n")


def write_retro_usnats():
    rows = [
        (1, "Jonny Chu"),
        (2, "Matthew Ford"),
        (3, "Matt Sokol"),
        (4, "Andy Talaga"),
        (5, "Apollo Chu"),
        (6, "Joe Giannetti"),
        (7, "Steve Sanders"),
        (8, "Matt Manning"),
    ]
    bits = ['{| class="wikitable sortable"', "! Finish !! Player"]
    for n, p in rows:
        bits += ["|-", f"| {n} || [[{p}]]"]
    bits.append("|}")
    body = f"""'''2026 Retro U.S. Nationals''' was the Premiere-to-Death Star II side event at the [[2026 U.S. National Championship]] weekend in New Brunswick, New Jersey, 1 August 2026. [[Jonny Chu]] won undefeated.<ref name="pc">https://www.starwarsccg.org/2026-07-retro-u-s-nationals-prem-to-dsii-new-brunswick-new-jersey-aug-1-2026/</ref><ref name="wrap">https://www.starwarsccg.org/2026-us-nationals-wrap-up-win-for-hayes-hunter/</ref>

== Format ==

* '''Environment:''' [[Premiere - Death Star II]]
* '''Site:''' New Brunswick, New Jersey
* '''Date:''' 1 August 2026
* '''Forum:''' [https://forum.starwarsccg.org/viewtopic.php?t=86770 forum t=86770]

== Results ==

Finish as published on the PC results page.<ref name="pc" />

{chr(10).join(bits)}

== See also ==

* [[2026 U.S. National Championship]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/2026-07-retro-u-s-nationals-prem-to-dsii-new-brunswick-new-jersey-aug-1-2026/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2026-07-retro-u-s-nationals-prem-to-dsii-new-brunswick-new-jersey-aug-1-2026/ 2026-07 Retro U.S. Nationals – Prem to DSII – New Brunswick, New Jersey (Aug. 1, 2026)], starwarsccg.org
* [https://www.starwarsccg.org/2026-us-nationals-wrap-up-win-for-hayes-hunter/ 2026 US Nationals Wrap-Up]

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2026]]
"""
    (PAGES / "2026_Retro_U.S._Nationals.wiki").write_text(body, encoding="utf-8", newline="\n")


def write_regionals():
    events = [
        ("Nal Hutta Regionals", "Indianapolis, Indiana", "6 September 2026", "Matt Scott"),
        ("Endor Regionals", "Federal Way, Washington", "22 August 2026", "Chris Wirfs"),
        ("Yavin 4 Regionals", "Windsor Mill, Maryland", "11 July 2026", "Ryan Sersen"),
        ("Bespin Regionals", "South Saint Paul, Minnesota", "27 June 2026", "Carson Stockman"),
        ("Naboo Regionals", "Liverpool, United Kingdom", "13 June 2026", "Chris Menzel"),
        ("Ryloth Regionals", "Vleuten, The Netherlands", "23 May 2026", "Floris de Vries"),
    ]
    bits = ['{| class="wikitable sortable"', "! Event !! Date !! Site !! Winner"]
    for name, site, date, winner in events:
        bits += ["|-", f"| {name} || {date} || {site} || [[{winner}]]"]
    bits.append("|}")
    body = f"""'''2026 Regional Championships''' are the Players Committee 2026 regional events, posted together on one PC results page.<ref name="pc">https://www.starwarsccg.org/2026-05-regional-championships/</ref>

== Results ==

Winners as published (newest first on that page).<ref name="pc" />

{chr(10).join(bits)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2026-05-regional-championships/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2026-05-regional-championships/ 2026-05 Regional Championships], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2026]]
"""
    (PAGES / "2026_Regional_Championships.wiki").write_text(body, encoding="utf-8", newline="\n")


def process_gemp():
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()
    MEDIA.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)

    folders = {
        "Nats": [TD / "2026-nats-d1", TD / "2026-nats-t8"],
        "BWC": [TD / "2026-bwc-d1", TD / "2026-bwc-t8"],
        "OC": [TD / "2026-outrider"],
    }
    parsed = []
    for ev, dirs in folders.items():
        for d in dirs:
            for path in sorted(d.glob("*.txt")):
                info = parse_name(path.name)
                if not info:
                    print("SKIP", path.name)
                    continue
                ev2, player, t8, side, obj, media = info
                shutil.copy2(path, MEDIA / media)
                counts, cards = parse_gemp_counts(path, by_id, by_title)
                parsed.append((ev2, player, t8, side, obj, media, counts, cards))

    deck_titles = {}
    hub_labels = {}
    for ev, player, t8, side, obj, media, counts, cards in parsed:
        deck_titles[(ev, player, t8, side)] = deck_title(ev, player, t8, side, obj)

    for ev, player, t8, side, obj, media, counts, cards in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = deck_titles.get((ev, player, t8, other))
        title, body, hub_label = render_deck(
            ev, player, t8, side, obj, counts, cards, media, companion, bp, dests, title_map
        )
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub_label
        print("deck", title, "->", hub_label, "n", sum(counts.values()))

    def titles_for(ev):
        out = {}
        labs = {}
        for (e, player, t8, side), title in deck_titles.items():
            if e != ev:
                continue
            out[(player, t8, side)] = title
            labs[title] = hub_labels.get(title, title)
        return out, labs

    nt, nl = titles_for("Nats")
    write_nats(nt, nl)
    bt, bl = titles_for("BWC")
    write_bwc(bt, bl)
    # Outrider Cup IV hub is owned by generate_outrider_teams.py
    print("SKIPHUB 2026 Outrider Cup IV")

    src = {
        "Nats": (
            "https://www.starwarsccg.org/2026-08-u-s-national-championship-new-brunswick-new-jersey-aug-1-2-2026/",
            "1–2 August 2026",
        ),
        "BWC": (
            "https://www.starwarsccg.org/2026-01-boston-winter-classic-boston-massachusetts-jan-10-to-11-2026/",
            "10–11 January 2026",
        ),
        "OC": ("https://www.starwarsccg.org/2026-02-outrider-cup-iv/", "January–February 2026"),
    }
    by_player = defaultdict(list)
    for ev, player, t8, side, obj, media, counts, cards in parsed:
        by_player[(ev, player)].append((t8, side))
    for (ev, player), sides in by_player.items():
        et = event_title(ev)
        url, date = src[ev]
        t8 = any(s[0] for s in sides)
        ds = cell(*titles_for(ev), player, t8 if ev != "OC" else False, "DS") if ev == "OC" else cell(*titles_for(ev), player, t8, "DS")
        # build rows: T8 then D1
        rows = []
        dt, dl = titles_for(ev)
        if ev != "OC" and any(t for t, s in sides if t):
            fin = "—"
            order = NATS_T8 if ev == "Nats" else BWC_T8
            if player in order:
                fin = f"#{order.index(player)+1}"
            rows.append(
                f"|- \n| {date} || [[{et}]] (Top 8) || [[Open]] || {fin} || {cell(dt, dl, player, True, 'DS')} || {cell(dt, dl, player, True, 'LS')}"
            )
        if ev != "OC" and any(not t for t, s in sides):
            fin = "—"
            order = NATS_D1 if ev == "Nats" else BWC_D1
            if player in order:
                fin = f"#{order.index(player)+1}"
            rows.append(
                f"|- \n| {date} || [[{et}]] (Day 1) || [[Open]] || {fin} || {cell(dt, dl, player, False, 'DS')} || {cell(dt, dl, player, False, 'LS')}"
            )
        if ev == "OC":
            # Player Finish rows are owned by generate_outrider_teams.py
            continue
        if rows:
            upsert_stub(player, rows, et, url)
    print("gemp decks", len(parsed))


def main():
    process_gemp()
    write_jawa()
    write_retro_usnats()
    write_regionals()
    print("hubs written")


if __name__ == "__main__":
    main()
