#!/usr/bin/env python3
"""Generate Format-column indexes + Decipher Worlds 1996-2001 hubs and decks."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
SW = ROOT / "encyclopedia" / "swccgdb-worlds"
CARDS = json.loads((SW / "cards.json").read_text(encoding="utf-8"))

OBJ_DEST = {
    "Hidden Base/Systems Will Slip Through Your Fingers": (
        "Hidden Base / Systems Will Slip Through Your Fingers",
        "Hidden Base",
    ),
    "Local Uprising/Liberation": ("Local Uprising / Liberation", "Local Uprising"),
    "Hunt Down And Destroy The Jedi/Their Fire Has Gone Out Of The Universe": (
        "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe",
        "Hunt Down And Destroy The Jedi",
    ),
    "ISB Operations/Empire's Sinister Agents": (
        "ISB Operations / Empire's Sinister Agents",
        "ISB Operations",
    ),
    "Imperial Occupation/Imperial Control": (
        "Imperial Occupation / Imperial Control",
        "Imperial Occupation",
    ),
}
DARK_SHARED = {"Alter", "Sense", "Control"}
TYPE_ORDER = [
    "Objective",
    "Character",
    "Creature",
    "Device",
    "Weapon",
    "Starship",
    "Vehicle",
    "Location",
    "Effect",
    "Interrupt",
    "Jedi Test",
]
CATS = """
{{#if:1|<nowiki />
<h2>References</h2>
<references />}}
"""
TITLES: list[tuple[str, str]] = []


def slug_file(title: str) -> str:
    return title.replace(" ", "_").replace("/", "-") + ".wiki"


def write_page(title: str, body: str) -> None:
    PAGES.mkdir(parents=True, exist_ok=True)
    path = PAGES / slug_file(title)
    text = body.strip() + "\n"
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    TITLES.append((title, f"pages/{path.name}"))


def wiki_card(name: str, side: str) -> str:
    if name in OBJ_DEST:
        dest, vis = OBJ_DEST[name]
        return f"[[{dest}|{vis}]]"
    dest = name
    if side == "dark" and name in DARK_SHARED:
        dest = f"{name} (Dark)"
        return f"[[{dest}|{name}]]"
    return f"[[{name}]]"


def decklist_table(slots: dict[str, int], side: str) -> str:
    groups: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for code, qty in slots.items():
        c = CARDS[code]
        groups[c["type_name"]].append((c["name"], qty))
    ordered = []
    for t in TYPE_ORDER:
        if t in groups:
            rows = sorted(groups[t], key=lambda x: x[0].lower())
            ordered.append((t, rows))
    extra = [t for t in groups if t not in TYPE_ORDER]
    for t in sorted(extra):
        ordered.append((t, sorted(groups[t], key=lambda x: x[0].lower())))
    mid = (len(ordered) + 1) // 2
    left, right = ordered[:mid], ordered[mid:]

    def col(parts: list) -> str:
        chunks = []
        for t, rows in parts:
            chunks.append(f"'''{t}'''")
            for name, qty in rows:
                chunks.append(f"* {qty}x {wiki_card(name, side)}")
            chunks.append("")
        return "\n".join(chunks).rstrip()

    return (
        '{| class="wikitable" style="width:100%;"\n'
        "|-\n"
        '| style="width:50%; vertical-align:top;" |\n'
        f"{col(left)}\n"
        '| style="width:50%; vertical-align:top;" |\n'
        f"{col(right)}\n"
        "|}"
    )


def load_deck(i: int) -> dict:
    return json.loads((SW / f"{i}.json").read_text(encoding="utf-8"))


def objective_of(deck: dict) -> str | None:
    for code in deck["slots"]:
        c = CARDS[code]
        if c["type_name"] == "Objective":
            return c["name"]
    return None


def starting_cell(obj_name: str | None, fallback: str) -> str:
    if obj_name:
        return OBJ_DEST[obj_name][1]
    return fallback


# ---------------------------------------------------------------------------
# Format stubs
# ---------------------------------------------------------------------------
def write_format_stubs() -> None:
    stubs = [
        (
            "Premiere - A New Hope",
            """{{Hatnote|This page documents a constructed card pool. Official tournament documents remain authoritative.}}
'''Premiere &ndash; A New Hope''' (display name '''Premiere - A New Hope''') is a constructed environment whose legal pool is the printed Decipher sets from [[Premiere]] through [[A New Hope]]. Premium products legal at the time (for example [[Jedi Pack]] and [[Rebel Leader Packs]]) sat in that same early-game pool.

The [[1996 Decipher World Championship]] in Vail, Colorado was played in this format.

== See also ==

* [[Formats]]
* [[Premiere - Cloud City]]
* [[Championships]]
* [[1996 Decipher World Championship]]

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
        (
            "Premiere - Cloud City",
            """{{Hatnote|This page documents a constructed card pool. Official tournament documents remain authoritative.}}
'''Premiere &ndash; Cloud City''' (display name '''Premiere - Cloud City''') is a constructed environment whose legal pool is the printed Decipher sets from [[Premiere]] through [[Cloud City]] (including [[Dagobah]]).

The [[1997 Decipher World Championship]] in Norfolk, Virginia was played in this format.

== See also ==

* [[Formats]]
* [[Premiere - A New Hope]]
* [[Premiere - Special Edition]]
* [[Championships]]
* [[1997 Decipher World Championship]]

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
        (
            "Premiere - Special Edition",
            """{{Hatnote|This page documents a constructed card pool. Official tournament documents remain authoritative.}}
'''Premiere &ndash; Special Edition''' (display name '''Premiere - Special Edition''') is a constructed environment whose legal pool is the printed Decipher sets from [[Premiere]] through [[Special Edition]].

The [[1998 Decipher World Championship]] was timed with Special Edition's release. Decipher's 20 November 1998 Worlds packet is the contemporary procedure document for that event.

== See also ==

* [[Formats]]
* [[Premiere - Cloud City]]
* [[Premiere - Endor]]
* [[Championships]]
* [[1998 Decipher World Championship]]
* [[Tournaments#1998 World Championship packet|1998 World Championship packet]]

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
        (
            "Premiere - Endor",
            """{{Hatnote|This page documents a constructed card pool. Official tournament documents remain authoritative.}}
'''Premiere &ndash; Endor''' (display name '''Premiere - Endor''') is a constructed environment whose legal pool is the printed Decipher sets from [[Premiere]] through [[Endor]].

The [[1999 Decipher World Championship]] at DecipherCon in Virginia Beach was played in this format.

== See also ==

* [[Formats]]
* [[Premiere - Special Edition]]
* [[Premiere - Death Star II]]
* [[Championships]]
* [[1999 Decipher World Championship]]

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
        (
            "Premiere - Reflections III",
            """{{Hatnote|This page documents a constructed card pool. Official tournament documents remain authoritative.}}
'''Premiere &ndash; Reflections III''' (display name '''Premiere - Reflections III''') is a constructed environment whose legal pool is the printed Decipher sets from [[Premiere]] through [[Reflections III]].

The [[2001 Decipher World Championship]] (FreedomCon, after Decipher cancelled DecipherCon 2001) was played in this format. It was the last Worlds of the Decipher era.

== See also ==

* [[Formats]]
* [[Premiere - Death Star II]]
* [[Championships]]
* [[2001 Decipher World Championship]]

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
        (
            "Jawa Format",
            """{{Hatnote|This page is the constructed format, not the [[Jawa]] card.}}
'''Jawa Format''' is a Players Committee constructed format. The current definition, banned list, and version notes live on the PC site; this wiki does not copy that document.

The [[2026 Jawa Cup]] is the published Jawa Format championship on GEMP.

== See also ==

* [[Formats]]
* [[2026 Jawa Cup]]
* [https://www.starwarsccg.org/jawa/ Jawa Format] at starwarsccg.org

== Sources ==

* [https://www.starwarsccg.org/jawa/ Jawa Format], starwarsccg.org

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
        (
            "Premiere to Virtual Set 3",
            """{{Hatnote|This page documents a Players Committee constructed pool used for a published event.}}
'''Premiere to Virtual Set 3''' is a constructed environment used for the [[2025 Online Retro Event for Charity]]: printed Decipher cards plus Virtual Sets through [[Virtual Set 3]].

This is not the same pool as [[Premiere - Death Star II]] (no current virtual cards) and not [[Open]] (not the full current virtual pool).

== See also ==

* [[Formats]]
* [[2025 Online Retro Event for Charity]]
* [[Premiere - Death Star II]]
* [[Open]]

== Sources ==

* [https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/ 2025-06 Online Retro Event for Charity – Premiere to Virtual Set 3], starwarsccg.org

[[Category:Formats]]
[[Category:Meta]]
""",
        ),
    ]
    for title, body in stubs:
        write_page(title, body)
    write_page(
        "Premiere – A New Hope",
        "#REDIRECT [[Premiere - A New Hope]]\n",
    )
    write_page(
        "Premiere – Cloud City",
        "#REDIRECT [[Premiere - Cloud City]]\n",
    )
    write_page(
        "Premiere – Special Edition",
        "#REDIRECT [[Premiere - Special Edition]]\n",
    )
    write_page(
        "Premiere – Endor",
        "#REDIRECT [[Premiere - Endor]]\n",
    )
    write_page(
        "Premiere – Reflections III",
        "#REDIRECT [[Premiere - Reflections III]]\n",
    )
    write_page("Jawa (format)", "#REDIRECT [[Jawa Format]]\n")


def write_indexes() -> None:
    write_page(
        "List of SWCCG tournaments",
        r"""This is the chronological index of Star Wars CCG tournaments this wiki has sourced. The history of Swiss, ratings, and decklist sheets is on [[Tournaments]]. Worlds hubs start at [[Championships]]. European Championship years are on [[European Championships]].

The Players Committee posts results newest-first at [https://www.starwarsccg.org/tournaments/ starwarsccg.org/tournaments] and [https://www.starwarsccg.org/category/tournament-decklists/ Tournament Decklists]. This table follows that desk: '''newest first''' within a year, then earlier years. The Event name is a wiki link when this wiki has a hub for that tournament. '''Format''' is the constructed pool named for that event.

== 2026 ==

{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
|-
| 2026-10 || [[2026 European Championship]] || 19–20 September 2026 || Bochum, Germany || [[Open]] || [[Timo Dusel]]
|-
| 2026-09 || [[2026 Retro GEMP Match Play Championship (Premiere to DSII)|Retro GEMP Match Play Championship (Premiere to DSII)]] || July–September 2026 || GEMP || [[Premiere - Death Star II]] || [[Timo Dusel]]
|-
| 2026-08 || [[2026 U.S. National Championship|U.S. National Championship]] || 1–2 August 2026 || New Brunswick, New Jersey || [[Open]] || [[Hayes Hunter]]
|-
| 2026-07 || [[2026 Retro U.S. Nationals|Retro U.S. Nationals (Prem to DSII)]] || 1 August 2026 || New Brunswick, New Jersey || [[Premiere - Death Star II]] || [[Jonny Chu]]
|-
| 2026-06 || [[2026 Tenth Annual GEMPC|Tenth Annual GEMPC]] || May–July 2026 || GEMP || [[Open]] || [[Patrick Johnson]]
|-
| 2026-05 || [[2026 Regional Championships|Regional Championships]] || 2026 || various || [[Open]] || —
|-
| 2026-04 || [[2026 San Diego Super Open|San Diego Super Open]] || 10–12 April 2026 || San Diego, California || [[Open]] || [[Joe Olson]]
|-
| 2026-03 || [[2026 Jawa Cup|Jawa Cup]] || December 2025 – March 2026 || GEMP || [[Jawa Format]] || [[Justin Miyashiro]]
|-
| 2026-02 || [[2026 Outrider Cup IV|Outrider Cup IV]] || 13 January – 4 February 2026 || GEMP (teams) || [[Open]] || Team USA
|-
| 2026-01 || [[2026 Boston Winter Classic|Boston Winter Classic]] || 10–11 January 2026 || Boston, Massachusetts || [[Open]] || [[Phil Aasen]]
|}

== 2025 ==

{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
|-
| 2025-10 || [[2025 Online Championship Series Playoffs|Online Championship Series Playoffs]] || October–November 2025 || GEMP || [[Open]] || [[Patrick Johnson]]
|-
| 2025-09 || [[2025 World Championship|World Championship]] || 4–5 October 2025 || Seattle, Washington || [[Open]] || [[Greg Shaw]]
|-
| 2025-08 || [[2025 European Championship|European Championship]] || 20–21 September 2025 || Bochum, Germany || [[Open]] || [[Emil Wallin]]
|-
| 2025-07 || [[2025 U.S. National Championship|U.S. National Championship]] || 23–24 August 2025 || Columbus, Ohio || [[Open]] || [[Matt Scott]]
|-
| 2025-06 || [[2025 Online Retro Event for Charity|Online Retro Event for Charity]] || May–June 2025 || GEMP || [[Premiere to Virtual Set 3]] || [[Joe Horbey]]
|-
| 2025-05 || [[2025 Ninth Annual GEMPC|Ninth Annual GEMPC]] || May–July 2025 || GEMP || [[Open]] || [[Matthew Harrison-Trainor]]
|-
| 2025-04 || [[2025 Retro GEMP Match Play Championship (Premiere to DSII)|Retro GEMP Match Play Championship (Premiere to DSII)]] || May–July 2025 || GEMP || [[Premiere - Death Star II]] || [[Timo Dusel]]
|-
| 2025-03 || [[2025 Regional Championships|Regional Championships]] || 2025 || various || [[Open]] || —
|-
| 2025-02 || [[2025 Morristown Melee|Morristown Melee]] || 24–27 April 2025 || Morristown, New Jersey || [[Open]] || [[Greg Shaw]]
|-
| 2025-01 || [[2025 Las Vegas Grand Prix|Las Vegas Grand Prix]] || 11–12 January 2025 || Las Vegas, Nevada || [[Open]] || [[Joe Olson]]
|}

== Decipher World Championships ==

Decipher ran six World Championships, 1996–2001. Each year is a dedicated hub. The constructed pool each year was the printed sets from [[Premiere]] through the newest expansion named in the Format column.

{| class="wikitable sortable"
|-
! Year !! Event !! Site !! Format !! Winner !! Runner-up
|-
| 2001 || [[2001 Decipher World Championship]] || FreedomCon, Virginia Beach, Virginia || [[Premiere - Reflections III]] || [[Bastian Winkelhaus]] || [[Martin Akesson]]
|-
| 2000 || [[2000 Decipher World Championship]] || DecipherCon, Kissimmee, Florida || [[Premiere - Death Star II]] || [[Matt Sokol]] || [[Yannick Lapointe]]
|-
| 1999 || [[1999 Decipher World Championship]] || DecipherCon, Virginia Beach, Virginia || [[Premiere - Endor]] || [[Gary Carman]] || [[Steven Lewis]]
|-
| 1998 || [[1998 Decipher World Championship]] || Cavalier Hotel, Virginia Beach, Virginia || [[Premiere - Special Edition]] || [[Matt Potter]] || [[Michael Riboulet]]
|-
| 1997 || [[1997 Decipher World Championship]] || Marriott Hotel, Norfolk, Virginia || [[Premiere - Cloud City]] || [[Philipp Jacobs]] || [[Michael Riboulet]]
|-
| 1996 || [[1996 Decipher World Championship]] || Vail, Colorado || [[Premiere - A New Hope]] || [[Raphael Asselin]] || [[Bjørn Sørgjerd]]
|}

== See also ==

* [[Tournaments]]
* [[Championships]]
* [[European Championships]]
* [[Formats]]
* [https://www.starwarsccg.org/category/tournament-decklists/ PC Tournament Decklists]
* [https://www.starwarsccg.org/tournaments/ PC tournament desk]

== Sources ==

* [https://www.starwarsccg.org/category/tournament-decklists/ Tournament Decklists Archives], starwarsccg.org
* [https://www.starwarsccg.org/tournaments/ Tournaments], starwarsccg.org
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia (World Champions table)
* [https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org
* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]] (Wayback)
* [https://web.archive.org/web/20001026043505/http://www.decipher.com/deciphercon/2000/events/results/starwars.html DecipherCon 2000 Day 2]
* [https://web.archive.org/web/20010303120030/http://decipher.com/deciphercon/2000/events/results/starwars3.html DecipherCon 2000 Day 3]
* [https://blog.categoryonegames.com/wp-content/uploads/2013/07/1998-World-Championship.pdf 1998 World Championship packet]

"""
        + CATS
        + """
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
[[Category:2025]]
""",
    )

    write_page(
        "European Championships",
        r"""The '''European Championship''' (also '''European Championships''', '''EC''') is a Players Committee major event, usually held in September at Zu Den Vier Winden in Bochum, Germany. Some years have been elsewhere (Copenhagen 2024) or skipped (2020–2021 hiatus). Year pages list the field and decklists when this wiki has them.

How Swiss, ratings, and decklist sheets work: [[Tournaments]]. The chronological event index is [[List of SWCCG tournaments]]. Worlds hubs start at [[Championships]].

{| class="wikitable sortable"
|-
! Year !! Event !! Site !! Format !! Winner
|-
| 2026 || [[2026 European Championship]] || Bochum, Germany || [[Open]] || [[Timo Dusel]]
|-
| 2025 || [[2025 European Championship]] || Bochum, Germany || [[Open]] || [[Emil Wallin]]
|-
| 2024 || 2024 European Championship || Copenhagen, Denmark || — || [[Casper Jørgensen]]
|-
| 2023 || 2023 European Championship || Bochum, Germany || — || —
|-
| 2022 || 2022 European Championship || Bochum, Germany || — || [[Emil Wallin]]
|-
| 2021 || — || hiatus || — || —
|-
| 2020 || — || hiatus || — || —
|-
| 2019 || 2019 European Championships || Bochum, Germany || — || [[Emil Wallin]]
|-
| 2018 || 2018 European Championship || — || — || —
|-
| 2017 || 2017 European Championship || — || — || [[Bastian Winkelhaus]]
|-
| 2016 || 2016 European Championship || — || — || [[Emil Wallin]]
|-
| 2015 || 2015 European Championship || — || — || —
|-
| 2014 || 2014 European Championship || — || — || [[Casper Jørgensen]]
|-
| 2013 || 2013 European Championship || — || — || [[Emil Wallin]]
|-
| 2012 || 2012 European Championship || — || — || [[Emil Wallin]]
|-
| 2006 || 2006 European Championship || — || — || [[Bastian Winkelhaus]]
|-
| 2004 || 2004 European Championship || — || — || [[Bastian Winkelhaus]]
|-
| 2003 || 2003 European Championship || — || — || [[Bastian Winkelhaus]]
|-
| 2002 || 2002 European Championship || — || — || [[Angelo Consoli]]
|-
| 2001 || 2001 European Championship || — || — || [[Bastian Winkelhaus]]
|}

Years without a wiki article still belong on this list so later hubs can fill in. 2020–2021 are the two-year gap named in the 2022 wrap-up. Format is filled when this wiki has a sourced pool for that year (2025–2026 [[Open]]).

== See also ==

* [[2026 European Championship]]
* [[List of SWCCG tournaments]]
* [[Championships]] · [[Tournaments]] · [[Formats]]
* [https://www.starwarsccg.org/category/tournament-decklists/ PC Tournament Decklists]

== Sources ==

* [https://www.starwarsccg.org/2026-10-european-championship-bochum-germany-sept-19-20-2026/ 2026-10 European Championship – Bochum, Germany (Sept. 19-20, 2026)]
* [https://www.starwarsccg.org/2025-08-european-championship-bochum-germany-sept-20-21-2025/ 2025-08 European Championship – Bochum, Germany (Sept. 20-21, 2025)]
* [https://www.starwarsccg.org/2024-european-championship-wrap-up-casper-takes-the-crown/ 2024 European Championship Wrap-Up – Casper Takes the Crown]
* [https://www.starwarsccg.org/2022-european-championship-wrap-up-wallin-victorious/ 2022 European Championship Wrap-up – Wallin Victorious]
* [https://www.starwarsccg.org/2019-european-championships/ 2019 European Championships]
* [https://www.starwarsccg.org/2016-european-championships/ 2016 European Championships]
* [https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame] (Emil Wallin 2012–2013; Angelo Consoli 2002; Bastian Winkelhaus 2001, 2003, 2004, 2006, 2017)

"""
        + CATS
        + """
[[Category:Tournaments]]
[[Category:Championships]]
""",
    )

    write_page(
        "Championships",
        """Flagship history: '''Decipher World Championships 1996–2001'''. Each year has a hub (location, field, top cut, narrative, sourced decklists). Lists come from public pages after an archive.org / archive.today snapshot.

How the circuit was run (Swiss, ratings, decklist sheets): [[Tournaments]]. Event index: [[List of SWCCG tournaments]]. European Championship years: [[European Championships]].

{| class="wikitable"
|-
! Year !! Hub !! Format !! Champion
|-
| 1996 || [[1996 Decipher World Championship]] || [[Premiere - A New Hope]] || [[Raphael Asselin]]
|-
| 1997 || [[1997 Decipher World Championship]] || [[Premiere - Cloud City]] || [[Philipp Jacobs]]
|-
| 1998 || [[1998 Decipher World Championship]] || [[Premiere - Special Edition]] || [[Matt Potter]]
|-
| 1999 || [[1999 Decipher World Championship]] || [[Premiere - Endor]] || [[Gary Carman]]
|-
| 2000 || [[2000 Decipher World Championship]] || [[Premiere - Death Star II]] || [[Matt Sokol]]
|-
| 2001 || [[2001 Decipher World Championship]] || [[Premiere - Reflections III]] || [[Bastian Winkelhaus]]
|}

Players Committee Worlds from 2002 on are indexed on [[List of SWCCG tournaments]] (this wiki currently has year hubs for 2025–2026).

[[Category:Championships]]
""",
    )


def patch_formats() -> None:
    path = PAGES / "Formats.wiki"
    text = path.read_text(encoding="utf-8")
    needle = "== GEMP environments =="
    block = """== Decipher-era constructed pools ==

Decipher Worlds used the printed sets legal at the time, from [[Premiere]] through the newest expansion:

* [[Premiere - A New Hope]] — [[1996 Decipher World Championship]]
* [[Premiere - Cloud City]] — [[1997 Decipher World Championship]]
* [[Premiere - Special Edition]] — [[1998 Decipher World Championship]]
* [[Premiere - Endor]] — [[1999 Decipher World Championship]]
* [[Premiere - Death Star II]] — [[2000 Decipher World Championship]] (also the modern GEMP Retro / Premiere-to-DSII environment)
* [[Premiere - Reflections III]] — [[2001 Decipher World Championship]]

Later Players Committee events also use [[Open]], [[Jawa Format]], and (for the 2025 charity event) [[Premiere to Virtual Set 3]].

"""
    if "== Decipher-era constructed pools ==" not in text:
        text = text.replace(needle, block + needle)
    # Jawa already in Other labeled formats; add wiki links
    text = text.replace(
        "[https://www.starwarsccg.org/jawa/ Jawa Format]",
        "[[Jawa Format]] ([https://www.starwarsccg.org/jawa/ PC page])",
        1,
    )
    path.write_text(text, encoding="utf-8", newline="\n")
    TITLES.append(("Formats", "pages/Formats.wiki"))


def patch_premiere_ds2() -> None:
    path = PAGES / "Premiere_-_Death_Star_II.wiki"
    text = path.read_text(encoding="utf-8")
    if "2000 Decipher World Championship" not in text:
        text = text.replace(
            "* [[2026 Retro GEMP Match Play Championship (Premiere to DSII)]]",
            "* [[2000 Decipher World Championship]] &mdash; last Decipher Worlds played in this printed pool (Death Star II was the newest expansion).\n* [[2026 Retro GEMP Match Play Championship (Premiere to DSII)]]",
        )
        path.write_text(text, encoding="utf-8", newline="\n")
    TITLES.append(("Premiere - Death Star II", "pages/Premiere_-_Death_Star_II.wiki"))


def patch_jawa_cup() -> None:
    path = PAGES / "2026_Jawa_Cup.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace("* '''Environment:''' [[Jawa]]", "* '''Environment:''' [[Jawa Format]]")
    text = text.replace("[[Jawa]] format championship", "[[Jawa Format]] championship")
    path.write_text(text, encoding="utf-8", newline="\n")
    TITLES.append(("2026 Jawa Cup", "pages/2026_Jawa_Cup.wiki"))


def patch_charity() -> None:
    path = PAGES / "2025_Online_Retro_Event_for_Charity.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "* '''Environment:''' Premiere to Virtual Set 3",
        "* '''Environment:''' [[Premiere to Virtual Set 3]]",
    )
    path.write_text(text, encoding="utf-8", newline="\n")
    TITLES.append(
        (
            "2025 Online Retro Event for Charity",
            "pages/2025_Online_Retro_Event_for_Charity.wiki",
        )
    )


def patch_tournaments_akesson() -> None:
    path = PAGES / "Tournaments.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    old = "several players on 10 points missed the cut on differential ([[Martin Akesson]] +69 made it; others on 10 with +57 down to +15 did not)."
    new = "twelve advanced. The last slot was [[Dominic Gaudreault]] 10 (+70); [[Martin Akesson]] 10 (+69) missed by one differential, and the remaining 10-point players (+57 down to +15) also missed."
    if old in text:
        text = text.replace(old, new)
        path.write_text(text, encoding="utf-8", newline="\n")
        TITLES.append(("Tournaments", "pages/Tournaments.wiki"))


REF = CATS

DECK_META = [
    dict(
        id=1,
        year=1996,
        player="Raphael Asselin",
        side="light",
        place="1st",
        start="Yavin 4: Massassi War Room",
        theme="Mains",
        src="https://swccgdb.com/decklist/view/1/1996-world-champion-light-1.0",
    ),
    dict(
        id=2,
        year=1996,
        player="Raphael Asselin",
        side="dark",
        place="1st",
        start="Death Star",
        theme="Mains",
        src="https://swccgdb.com/decklist/view/2/1996-world-champion-dark-1.0",
    ),
    dict(
        id=3,
        year=1997,
        player="Philipp Jacobs",
        side="dark",
        place="1st",
        start=None,
        theme="Mains & Toys",
        src="https://swccgdb.com/decklist/view/3/mains-toys-1997-world-champion-1.0",
    ),
    dict(
        id=4,
        year=1997,
        player="Philipp Jacobs",
        side="light",
        place="1st",
        start=None,
        theme="Dagobah turtle",
        src="https://swccgdb.com/decklist/view/4/dagobah-turtle-1997-world-champion-1.0",
    ),
    dict(
        id=12,
        year=1997,
        player="Michael Riboulet",
        side="dark",
        place="2nd",
        start=None,
        theme="Dagobah manipulator",
        src="https://swccgdb.com/decklist/view/12/dagobah-a-manipulator-2nd-at-worlds-1997-1.0",
    ),
    dict(
        id=13,
        year=1997,
        player="Michael Riboulet",
        side="light",
        place="2nd",
        start=None,
        theme="Dagobah Miner's Guild",
        src="https://swccgdb.com/decklist/view/13/dagobah-miner-s-guild-2nd-at-worlds-1997-1.0",
    ),
    dict(
        id=5,
        year=1998,
        player="Matt Potter",
        side="light",
        place="1st",
        start=None,
        theme="Operatives",
        src="https://swccgdb.com/decklist/view/5/operatives-1998-world-champion-1.0",
    ),
    dict(
        id=6,
        year=1998,
        player="Matt Potter",
        side="dark",
        place="1st",
        start=None,
        theme="Operatives",
        src="https://swccgdb.com/decklist/view/6/operatives-1998-world-champion-1.0",
    ),
    dict(
        id=7,
        year=1999,
        player="Gary Carman",
        side="dark",
        place="1st",
        start=None,
        theme="ISB Operations",
        src="https://swccgdb.com/decklist/view/7/isb-1999-world-champion-1.0",
    ),
    dict(
        id=8,
        year=1999,
        player="Gary Carman",
        side="light",
        place="1st",
        start=None,
        theme="Hidden Base",
        src="https://swccgdb.com/decklist/view/8/hidden-base-1999-world-champion-1.0",
    ),
    dict(
        id=14,
        year=1999,
        player="Steven Lewis",
        side="light",
        place="2nd",
        start=None,
        theme="Operatives / Speeders",
        src="https://swccgdb.com/decklist/view/14/operatives-speeders-2nd-at-worlds-1999-1.0",
    ),
    dict(
        id=15,
        year=1999,
        player="Steven Lewis",
        side="dark",
        place="2nd",
        start=None,
        theme="Hunt Down",
        src="https://swccgdb.com/decklist/view/15/hunt-down-2nd-at-worlds-1999-1.0",
    ),
    dict(
        id=9,
        year=2000,
        player="Matt Sokol",
        side="light",
        place="1st",
        start=None,
        theme="Hidden Base",
        src="https://swccgdb.com/decklist/view/9/hidden-base-2000-world-champion-1.0",
    ),
    dict(
        id=10,
        year=2000,
        player="Matt Sokol",
        side="dark",
        place="1st",
        start=None,
        theme="ISB Operations",
        src="https://swccgdb.com/decklist/view/10/isb-2000-world-champion-1.0",
    ),
]


def deck_title(meta: dict) -> str:
    sd = "LS" if meta["side"] == "light" else "DS"
    return f"{meta['year']} Decipher World Championship {meta['player']} {sd}"


def hub_cell(meta: dict) -> str:
    deck = load_deck(meta["id"])
    obj = objective_of(deck)
    label = starting_cell(obj, meta["start"] or meta["theme"])
    return f"[[{deck_title(meta)}|{label}]]"


def write_swccgdb_deck(meta: dict) -> None:
    deck = load_deck(meta["id"])
    side = meta["side"]
    obj = objective_of(deck)
    start = starting_cell(obj, meta["start"] or "—")
    if obj:
        dest, vis = OBJ_DEST[obj]
        start_field = f"[[{dest}|{vis}]]"
    elif meta["start"]:
        start_field = f"[[{meta['start']}]]"
    else:
        start_field = "—"
    side_title = "Light" if side == "light" else "Dark"
    event = f"{meta['year']} Decipher World Championship"
    note = ""
    if meta["year"] == 1996:
        note = (
            "\nThis reconstruction on SWCCGDB (2018) tracks the contemporary Scrye magazine "
            "championship lists (Gravity Shadow from [[Jedi Pack]]; Gold Leader In Gold 1 / "
            "Red Leader In Red 1 from [[Rebel Leader Packs]]). Starting location is the Scrye-starred site.\n"
        )
    if meta["id"] == 6:
        note = (
            "\n[[Trandosite]] printed this as Potter's '''day one''' Dark deck. "
            "Saturday-night deck changes were allowed at 1998 Worlds.\n"
        )
    if meta["id"] == 3:
        note = (
            "\n[[Trandosite]] also printed Jacobs' Dark list from the final. "
            "The SWCCGDB reconstruction is the 60-card copy used here; both are cited.\n"
        )
    body = f"""== Deck info ==
* '''Player:''' [[{meta['player']}]]
* '''Event:''' [[{event}]]
* '''Stage:''' Finals
* '''Finish:''' {meta['place']}
* '''Format:''' {format_link(meta['year'])}
* '''Side:''' [[{side_title}]]
* '''Starting Card:''' {start_field}
* '''Strategy:''' {meta['theme']}
{note}
== Decklist ==

{decklist_table(deck['slots'], side)}

== See also ==

* [[{event}]]
* [[{meta['player']}]]
* [[Championships]]

== Sources ==

* [{meta['src']} {deck.get('name')}] on SWCCGDB
* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]] (Wayback)

{REF}
[[Category:Decklists]]
[[Category:Championships]]
[[Category:{meta['year']}]]
"""
    write_page(deck_title(meta), body)


def format_link(year: int) -> str:
    return {
        1996: "[[Premiere - A New Hope]]",
        1997: "[[Premiere - Cloud City]]",
        1998: "[[Premiere - Special Edition]]",
        1999: "[[Premiere - Endor]]",
        2000: "[[Premiere - Death Star II]]",
        2001: "[[Premiere - Reflections III]]",
    }[year]


def write_reitzel_decks() -> None:
    ls = [
        ("Location", [(1, "Yavin 4: Massassi Throne Room"), (1, "Yavin 4"), (1, "Dantooine"), (1, "Kashyyyk"), (1, "Tatooine"), (2, "Kessel")]),
        ("Character", [(2, "Obi-Wan Kenobi"), (2, "Luke Skywalker"), (2, "Han Solo"), (1, "Leia Organa"), (1, "Chewbacca"), (1, "Wedge Antilles"), (1, "Biggs Darklighter"), (1, "Pops"), (1, "Tiree"), (1, "Jek Porkins"), (1, "BoShek"), (1, "Momaw Nadon"), (1, "Kal'Falnl C'ndros"), (1, "Figrin D'an"), (1, "R2-D2 (Artoo-Detoo)")]),
        ("Weapon", [(2, "Obi-Wan's Lightsaber")]),
        ("Starship", [(1, "Millennium Falcon"), (1, "Red Leader In Red 1"), (1, "Gold Leader In Gold 1"), (1, "Gold 2"), (1, "Red 6"), (1, "Tantive IV"), (3, "Corellian Corvette")]),
        ("Effect", [(1, "Traffic Control"), (1, "Demotion"), (2, "Revolution"), (3, "Undercover")]),
        ("Interrupt", [(2, "Grimtaash"), (4, "Sense"), (3, "Alter"), (1, "Rebel Barrier"), (1, "Don't Get Cocky"), (2, "The Force Is Strong With This One"), (2, "Gift Of The Mentor"), (2, "Double Agent")]),
    ]
    ds = [
        ("Location", [(1, "Death Star"), (1, "Kiffex"), (1, "Yavin 4"), (2, "Kashyyyk"), (1, "Tatooine"), (1, "Kessel")]),
        ("Character", [(2, "Darth Vader"), (2, "Grand Moff Tarkin"), (1, "Admiral Motti"), (1, "General Tagge"), (1, "Chief Bast"), (1, "Officer Evax"), (1, "DS-61-2"), (1, "DS-61-3"), (1, "DS-61-4"), (1, "Captain Khurgee"), (1, "Djas Puhr"), (1, "Dr. Evazan"), (1, "Danz Borin"), (1, "Labria"), (1, "Garindan"), (1, "U-3PO (Yoo-Threepio)")]),
        ("Weapon", [(2, "Vader's Lightsaber")]),
        ("Starship", [(1, "Devastator"), (1, "Conquest"), (6, "Victory-Class Star Destroyer")]),
        ("Effect", [(2, "Presence Of The Force"), (1, "Reactor Terminal"), (2, "Undercover")]),
        ("Interrupt", [(2, "Monnok"), (2, "Scanning Crew"), (4, "Sense"), (3, "Alter"), (1, "Imperial Barrier"), (1, "Boring Conversation Anyway"), (1, "Dark Collaboration"), (2, "Charming To The Last"), (2, "I Have You Now"), (2, "Nevar Yalnal")]),
    ]

    def table(groups, side):
        mid = (len(groups) + 1) // 2
        def col(parts):
            chunks = []
            for t, rows in parts:
                chunks.append(f"'''{t}'''")
                for qty, name in rows:
                    chunks.append(f"* {qty}x {wiki_card(name, side)}")
                chunks.append("")
            return "\n".join(chunks).rstrip()
        return (
            '{| class="wikitable" style="width:100%;"\n|-\n'
            f'| style="width:50%; vertical-align:top;" |\n{col(groups[:mid])}\n'
            f'| style="width:50%; vertical-align:top;" |\n{col(groups[mid:])}\n|}}'
        )

    fb = "https://www.facebook.com/kevin.reitzel/posts/its-been-30-years-my-star-wars-ccg-1996-championship-deck-lists-that-i-used-at-t/10241711434940142/"
    common_src = f"""* [{fb} Kevin Reitzel, 1996 championship deck lists] (Facebook, 29 April 2026; Reitzel kept the physical 1996 decks)
* Dan Murray, on Reitzel's 2025 posting of the same lists, recalled them in Scrye magazine

{REF}
[[Category:Decklists]]
[[Category:Championships]]
[[Category:1996]]
"""
    write_page(
        "1996 Decipher World Championship Kevin Reitzel LS",
        f"""== Deck info ==
* '''Player:''' [[Kevin Reitzel]]
* '''Event:''' [[1996 Decipher World Championship]]
* '''Stage:''' Finals (4th)
* '''Format:''' [[Premiere - A New Hope]]
* '''Side:''' [[Light]]
* '''Starting Card:''' [[Yavin 4: Massassi Throne Room]]

Reitzel published these as the 60-card Light deck he played at Vail. Spelling normalized to printed titles (Tatooine, not Tattooine).

== Decklist ==

{table(ls, 'light')}

== See also ==

* [[1996 Decipher World Championship]]
* [[Kevin Reitzel]]

== Sources ==

{common_src}
""",
    )
    write_page(
        "1996 Decipher World Championship Kevin Reitzel DS",
        f"""== Deck info ==
* '''Player:''' [[Kevin Reitzel]]
* '''Event:''' [[1996 Decipher World Championship]]
* '''Stage:''' Finals (4th)
* '''Format:''' [[Premiere - A New Hope]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' [[Death Star]]

Reitzel published this as the 60-card Dark deck he played at Vail. Titles normalized (Monnok, Boring Conversation Anyway, I Have You Now, Tatooine).

== Decklist ==

{table(ds, 'dark')}

== See also ==

* [[1996 Decipher World Championship]]
* [[Kevin Reitzel]]

== Sources ==

{common_src}
""",
    )


def write_hubs() -> None:
    a_ls = hub_cell(DECK_META[0])
    a_ds = hub_cell(DECK_META[1])
    write_page(
        "1996 Decipher World Championship",
        f"""'''1996 Decipher World Championship''' was the first Star Wars CCG World Championship, played in Vail, Colorado. [[Raphael Asselin]] (Canada) defeated [[Bjørn Sørgjerd]] (Norway) in the final. [[Joe Alread]] finished 3rd and [[Kevin Reitzel]] 4th.<ref name="trando">[https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]]</ref><ref name="wp">[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia</ref>

The constructed pool was [[Premiere - A New Hope]]. Mains decks dominated: there was still little to counter [[Sense]] / [[Alter]], or the raw power of Obi-Wan and Vader. Trandosite notes Joe Alread using seven [[Dark Maneuvers]] in his Dark deck.<ref name="trando" />

== Format ==

* '''Environment:''' [[Premiere - A New Hope]]
* '''Site:''' Vail, Colorado
* '''Field:''' 32 (Wikipedia Round 1 count)<ref name="wp" />

== Finalists ==

The twelve finalists, alphabetical, from Trandosite (via Alex Tennet): [[Joe Alread]], [[Raphael Asselin]], Sergio Domenech, [[Paul Todd Feldman]], Greg Hefner, Brent Johnson, [[Maarten Logghe]], Wayne Martinez, [[Kevin Reitzel]], Dennis Shea, [[Bjørn Sørgjerd]], Rusty Zion.<ref name="trando" />

Several finalists later became Decipher staff or [[Squadron Members]] (Kevin Reitzel, and on Trandosite's list Tom Lischke, Kyle Heuer, Carl Mike Hardy, Paul Todd Feldman).<ref name="trando" />

== Results ==

{{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Raphael Asselin]] || {a_ds} || {a_ls}
|-
| 2 || [[Bjørn Sørgjerd]] || — || —
|-
| 3 || [[Joe Alread]] || — || —
|-
| 4 || [[Kevin Reitzel]] || [[1996 Decipher World Championship Kevin Reitzel DS|Death Star]] || [[1996 Decipher World Championship Kevin Reitzel LS|Yavin 4: Massassi Throne Room]]
|}}

Asselin's lists are the Scrye-era championship lists as reconstructed on SWCCGDB (2018). Reitzel published his own 1996 pair in 2025–2026 from the decks he kept; a commenter remembered those lists in Scrye.

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]
* [[Raphael Asselin]] · [[Bjørn Sørgjerd]] · [[Joe Alread]] · [[Kevin Reitzel]]

== Sources ==

* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], Trandosite (Wayback 17 May 2005)
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Wikipedia: Star Wars Customizable Card Game] (World Champions table)
* [https://swccgdb.com/decklist/view/1/1996-world-champion-light-1.0 1996 World Champion (Light)], SWCCGDB
* [https://swccgdb.com/decklist/view/2/1996-world-champion-dark-1.0 1996 World Champion (Dark)], SWCCGDB
* [https://www.facebook.com/kevin.reitzel/posts/its-been-30-years-my-star-wars-ccg-1996-championship-deck-lists-that-i-used-at-t/10241711434940142/ Kevin Reitzel, 1996 championship deck lists] (Facebook)

{REF}
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:1996]]
""",
    )

    j_ds = hub_cell(next(m for m in DECK_META if m["id"] == 3))
    j_ls = hub_cell(next(m for m in DECK_META if m["id"] == 4))
    r_ds = hub_cell(next(m for m in DECK_META if m["id"] == 12))
    r_ls = hub_cell(next(m for m in DECK_META if m["id"] == 13))
    write_page(
        "1997 Decipher World Championship",
        f"""'''1997 Decipher World Championship''' was the second Star Wars CCG World Championship, at the Marriott Hotel in Norfolk, Virginia.<ref name="jacobs">[https://web.archive.org/web/20050405/http://trandosite.mcmail.com/iv6.htm Philipp Jacobs interview], [[Trandosite]] (24 August 2000)</ref> [[Philipp Jacobs]] (Germany) defeated [[Michael Riboulet]] (United Kingdom) in the final. It was the first Worlds final for either country.<ref name="trando">[https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]]</ref>

The constructed pool was [[Premiere - Cloud City]]. Cloud City had just hit the shelves. Defending champion [[Raphael Asselin]] made the final twelve (12th). Asselin later said he lost a game by 2 to Gavin Palmer on a [[DS-61-4]] passenger / [[Devastator]] ruling.<ref name="asselin">[https://web.archive.org/web/20041026204829/http://www.trandosite.mcmail.com/iv11.htm Raphael Asselin interview], Trandosite (21 September 2000)</ref>

Jacobs barely made day 2, rebuilt Saturday night, and in the final opened with a 23-Force win on Dark Mains & Toys against Riboulet's manipulator. Riboulet's Light was a Dagobah deck Jacobs had beaten the previous round. The prize Jacobs named was a 10-day trip Washington–Las Vegas–Los Angeles.<ref name="jacobs" /><ref name="trando" />

Joe Alread called Riboulet's manipulator "a truly great deck....that I had never seen before." Trandosite treats 1997 as the birthplace of that strategy.<ref name="trando" />

== Format ==

* '''Environment:''' [[Premiere - Cloud City]]
* '''Site:''' Marriott Hotel, Norfolk, Virginia
* '''Field:''' 52 (Wikipedia Round 1 count)<ref name="wp">[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia</ref>

== Final twelve ==

As listed on Trandosite: [[Philipp Jacobs]], [[Michael Riboulet]], [[Paul Todd Feldman]], Gavin Palmer, [[Joe Alread]], Enriue Pascal (Trandosite spelling; likely Enrique), [[Bastian Winkelhaus]], Reiner Zetsche, Thaddeus Chenoweth, Michael Krause, [[Yannick Lapointe]], [[Raphael Asselin]].<ref name="trando" />

== Results ==

{{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Philipp Jacobs]] || {j_ds} || {j_ls}
|-
| 2 || [[Michael Riboulet]] || {r_ds} || {r_ls}
|}}

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]
* [[Philipp Jacobs]] · [[Michael Riboulet]]

== Sources ==

* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], Trandosite
* [https://web.archive.org/web/20050405/http://trandosite.mcmail.com/iv6.htm Philipp Jacobs interview], Trandosite (24 August 2000)
* [https://web.archive.org/web/20041026204829/http://www.trandosite.mcmail.com/iv11.htm Raphael Asselin interview], Trandosite
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Wikipedia World Champions table]
* [https://swccgdb.com/decklist/view/3/mains-toys-1997-world-champion-1.0 Mains & Toys: 1997 World Champion], SWCCGDB
* [https://swccgdb.com/decklist/view/4/dagobah-turtle-1997-world-champion-1.0 Dagobah turtle: 1997 World Champion], SWCCGDB
* [https://swccgdb.com/decklist/view/13/dagobah-miner-s-guild-2nd-at-worlds-1997-1.0 Dagobah Miner's Guild: 2nd at Worlds 1997], SWCCGDB
* [https://arstechnica.com/gaming/2015/12/that-one-time-i-played-in-the-star-wars-card-game-world-championship/ That one time I played in the Star Wars card game world championship], Ars Technica (5 December 2015; Texas regional winner at Norfolk, 64-competitor recollection)

{REF}
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:1997]]
""",
    )

    p_ls = hub_cell(next(m for m in DECK_META if m["id"] == 5))
    p_ds = hub_cell(next(m for m in DECK_META if m["id"] == 6))
    write_page(
        "1998 Decipher World Championship",
        f"""'''1998 Decipher World Championship''' was the third Star Wars CCG World Championship. Decipher's packet is dated 20 November 1998 over Kendrick Summers' letterhead. Play was Saturday 21 and Sunday 22 November at the Cavalier Hotel, Virginia Beach, Virginia.<ref name="pkt">[https://blog.categoryonegames.com/wp-content/uploads/2013/07/1998-World-Championship.pdf 1998 World Championship packet]</ref> Trandosite later called the site Norfolk; the packet is the Decipher document and names the Cavalier.<ref name="trando">[https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]]</ref>

[[Matt Potter]] (United States) defeated [[Michael Riboulet]] (United Kingdom) 2 (+9). Riboulet won game 1 by 19 with Dark Operatives; Potter won game 2 by 28, also on Operatives. Potter was the first American World Champion. Riboulet became the first player in two Grand Finals.<ref name="trando" />

The constructed pool was [[Premiere - Special Edition]], timed with that expansion. Operatives defined the weekend. Tomoya Suzuki led day 1, with Lucas Hernandez just behind. Evan Fergusson finished 14th of 55, the highest finisher Trandosite names who did not play Operatives. Jacobs just missed the twelve; Riboulet made it.<ref name="trando" />

Lucas Hernandez dominated day 2 until Riboulet beat him by a large margin in the last game and took the final slot. After the event Decipher errata hit Spaceport Speeders (Jon Van Der Meer's timeout Light), then Operatives, Floating Refineries, and Hidden Base.<ref name="trando" />

== Format ==

* '''Environment:''' [[Premiere - Special Edition]]
* '''Site:''' Cavalier Hotel, Virginia Beach, Virginia
* '''Field:''' 56 finalists (packet); Trandosite uses 55 contenders for Fergusson's 14th<ref name="pkt" /><ref name="trando" />

Packet structure (see [[Tournaments#1998 World Championship packet]]): Saturday Swiss, 4 rounds / eight games, top twelve advance. Those twelve may change decks Saturday night only. Sunday the twelve restart at 0 for four 60-minute games; top two play a two-game final. Everyone outside the twelve plays Sunday sealed.

== Final twelve ==

As listed on Trandosite: [[Matt Potter]], [[Michael Riboulet]], Adam Ankrum, [[Lucas Hernandez]], Jon Vandermeer, Stuart Jones, Hak Soo Kim, Michael Bergum, Dominik Probst, Chris Janiak, Tomoya Suzuki, James Lafferty.<ref name="trando" />

== Results ==

{{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Matt Potter]] || {p_ds} || {p_ls}
|-
| 2 || [[Michael Riboulet]] || — || —
|}}

Potter's Dark list on SWCCGDB / Trandosite is the '''day one''' Operatives deck.

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]
* [[Tournaments#1998 World Championship packet]]
* [[Matt Potter]] · [[Michael Riboulet]]

== Sources ==

* [https://blog.categoryonegames.com/wp-content/uploads/2013/07/1998-World-Championship.pdf 1998 World Championship packet] (20 November 1998)
* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], Trandosite
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Wikipedia World Champions table]
* [https://swccgdb.com/decklist/view/5/operatives-1998-world-champion-1.0 Operatives: 1998 World Champion] (Light), SWCCGDB
* [https://swccgdb.com/decklist/view/6/operatives-1998-world-champion-1.0 Operatives: 1998 World Champion] (Dark), SWCCGDB

{REF}
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:1998]]
""",
    )

    c_ds = hub_cell(next(m for m in DECK_META if m["id"] == 7))
    c_ls = hub_cell(next(m for m in DECK_META if m["id"] == 8))
    l_ls = hub_cell(next(m for m in DECK_META if m["id"] == 14))
    l_ds = hub_cell(next(m for m in DECK_META if m["id"] == 15))
    write_page(
        "1999 Decipher World Championship",
        f"""'''1999 Decipher World Championship''' was the fourth Star Wars CCG World Championship, at DecipherCon in Virginia Beach, Virginia. [[Gary Carman]] (United Kingdom) defeated [[Steven Lewis]] (United States) 2 (+19) and became the first British World Champion.<ref name="trando">[https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]]</ref><ref name="wp">[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia</ref>

The constructed pool was [[Premiere - Endor]]. Qualification was more exclusive than 1997–1998 (one player per region plus Open / Wild Card / invitational seats). Trandosite records that the regional structure drew heavy criticism and was not kept for 2000. A Wild Card tournament (100+ players) put [[John Arendt]] and James Lafferty into the World Finals; Lafferty played all three days. [[Joe Alread]] won Ironman and missed the main event for the first time.<ref name="trando" />

Day 1 (32 players, eight games): [[Bastian Winkelhaus]] led, then [[Clint Hays]]; Carman finished third after a strong close. That evening Carman lost his decks and rebuilt overnight, borrowing and adjusting Markus Wuest's Light.<ref name="trando" />

Day 2 (four games): [[Yannick Lapointe]] was the early leader; Winkelhaus and Hays took early losses. Lewis was the only undefeated and met Carman (Naboo region) in the final.

Final game 1: Carman [[ISB Operations / Empire's Sinister Agents|ISB Operations]] (Outer Rim Scout) against Lewis's Clak'dor VII Operative Speeder ([[Local Uprising / Liberation|Local Uprising]]). Carman won by 22. Game 2: Carman [[Hidden Base / Systems Will Slip Through Your Fingers|Hidden Base]] inserts against Lewis [[Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe|Hunt Down]]. Lewis probed the Hidden Base (Security Precautions), Carman resolved Never Tell Me The Odds for 8 after Grimtaash stripped Torture, and Lewis won by 3 with Lateral Damage. Combined, Carman 2 (+19).<ref name="trando" />

== Format ==

* '''Environment:''' [[Premiere - Endor]]
* '''Site:''' DecipherCon, Virginia Beach, Virginia
* '''Field:''' 32<ref name="wp" />

== Results ==

{{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Gary Carman]] || {c_ds} || {c_ls}
|-
| 2 || [[Steven Lewis]] || {l_ds} || {l_ls}
|}}

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]
* [[Gary Carman]] · [[Steven Lewis]]

== Sources ==

* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], Trandosite
* [https://web.archive.org/web/20041026204829/http://www.trandosite.mcmail.com/iv13.htm Gary Carman interview], Trandosite (29 September 2000)
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Wikipedia World Champions table]
* [https://swccgdb.com/decklist/view/7/isb-1999-world-champion-1.0 ISB: 1999 World Champion], SWCCGDB
* [https://swccgdb.com/decklist/view/8/hidden-base-1999-world-champion-1.0 Hidden Base: 1999 World Champion], SWCCGDB
* [https://swccgdb.com/decklist/view/14/operatives-speeders-2nd-at-worlds-1999-1.0 Operatives/Speeders: 2nd at Worlds 1999], SWCCGDB
* [https://swccgdb.com/decklist/view/15/hunt-down-2nd-at-worlds-1999-1.0 Hunt Down: 2nd at Worlds 1999], SWCCGDB

{REF}
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:1999]]
""",
    )

    s_ls = hub_cell(next(m for m in DECK_META if m["id"] == 9))
    s_ds = hub_cell(next(m for m in DECK_META if m["id"] == 10))
    write_page(
        "2000 Decipher World Championship",
        f"""'''2000 Decipher World Championship''' was the fifth Star Wars CCG World Championship, at DecipherCon in Kissimmee, Florida. [[Matt Sokol]] (United States) defeated [[Yannick Lapointe]] (Canada) in the Final Confrontation.<ref name="wp">[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia</ref><ref name="sokol">[https://web.archive.org/web/20041026224145/http://www.trandosite.mcmail.com/iv16.htm Matt Sokol interview], [[Trandosite]] (25 October 2000)</ref>

The constructed pool was [[Premiere - Death Star II]]. Wikipedia lists 72 Day 1 players. Sokol was player 36 on Day 1. He lost the first final game and won the second by one more Force.<ref name="sokol" /><ref name="wp" />

== Format ==

* '''Environment:''' [[Premiere - Death Star II]]
* '''Site:''' DecipherCon, Kissimmee, Florida
* '''Dates:''' mid-October 2000 (Day 2 results archived 26 October 2000)
* '''Field:''' 72 Day 1 (Wikipedia); 58 Day 2 (Decipher results page)<ref name="wp" /><ref name="d2">[https://web.archive.org/web/20001026043505/http://www.decipher.com/deciphercon/2000/events/results/starwars.html DecipherCon 2000 Day 2]</ref>

Day 2 was eight games (4 Light / 4 Dark). Twelve advanced to Day 3. Day 3 reset those twelve for four games (2 Light / 2 Dark); top two played the Final Confrontation.<ref name="d3">[https://web.archive.org/web/20010303120030/http://decipher.com/deciphercon/2000/events/results/starwars3.html DecipherCon 2000 Day 3]</ref>

The last Day 2 slot was [[Dominic Gaudreault]] 10 (+70). [[Martin Akesson]] 10 (+69) missed by one differential. On Day 3, [[Kevin Shannon]]'s Game 2 Dark vs [[Steve Brentson]] was a '''Modified Win by 14''' (+1 victory point). A full win there would have moved Shannon past Sokol on the cut math; that example is on [[Tournaments#2000 World Championship — Sokol, Shannon, and a modified win]].<ref name="d3" />

== Day 2 (twelve advancing) ==

From the Decipher Day 2 page, the twelve who appear on Day 3, with Day 2 totals:<ref name="d2" />

{{| class="wikitable sortable"
! Day 2 !! Player !! Points (diff)
|-
| 1 || [[Clint Hays]] || 14 (85)
|-
| 2 || [[Kyle Craft]] || 14 (65)
|-
| 3 || Martin Falke || 13 (54)
|-
| 4 || [[Yannick Lapointe]] || 12 (75)
|-
| 5 || [[Raphael Asselin]] || 12 (67)
|-
| 6 || Brian Rippetoe || 12 (62)
|-
| 7 || Steve Brentson || 12 (47)
|-
| 8 || [[Matt Sokol]] || 12 (6)
|-
| 9 || [[Paul Todd Feldman]] || 11 (52)
|-
| 10 || [[Kevin Shannon]] || 10 (111)
|-
| 11 || [[Gary Carman]] || 10 (99)
|-
| 12 || Dominic Gaudreault || 10 (70)
|}}

The remaining Day 2 field (through 58th) is on the Decipher results page.

== Day 3 ==

{{| class="wikitable sortable"
! Finish !! Player !! Points (diff) !! Notes
|-
| 1 || [[Yannick Lapointe]] || 8 (47) || advanced
|-
| 2 || [[Matt Sokol]] || 6 (23) || advanced
|-
| 3 || [[Kyle Craft]] || 6 (2) ||
|-
| 4 || [[Kevin Shannon]] || 5 (29) || Game 2 Dark vs Steve Brentson: Modified Win by 14
|-
| 5 || Dominic Gaudreault || 4 (28) ||
|-
| 6 || Martin Falke || 4 (10) ||
|-
| 7 || [[Raphael Asselin]] || 4 (4) ||
|-
| 8 || [[Clint Hays]] || 4 (−17) ||
|-
| 9 || Brian Rippetoe || 2 (−19) ||
|-
| 10 || [[Gary Carman]] || 2 (−38) ||
|-
| 11 || [[Paul Todd Feldman]] || 2 (−39) ||
|-
| 12 || Steve Brentson || 0 (−30) ||
|}}

== Final Confrontation ==

Sokol's published pair:<ref name="sokol" />

{{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Matt Sokol]] || {s_ds} || {s_ls}
|-
| 2 || [[Yannick Lapointe]] || — || —
|}}

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]
* [[Tournaments#2000 World Championship — Sokol, Shannon, and a modified win]]
* [[Matt Sokol]] · [[Yannick Lapointe]]

== Sources ==

* [https://web.archive.org/web/20001026043505/http://www.decipher.com/deciphercon/2000/events/results/starwars.html DecipherCon 2000 Day 2] (Wayback 26 October 2000)
* [https://web.archive.org/web/20010303120030/http://decipher.com/deciphercon/2000/events/results/starwars3.html DecipherCon 2000 Day 3] (Wayback 3 March 2001)
* [https://web.archive.org/web/20041026224145/http://www.trandosite.mcmail.com/iv16.htm Matt Sokol interview], Trandosite (25 October 2000)
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Wikipedia World Champions table]
* [https://swccgdb.com/decklist/view/9/hidden-base-2000-world-champion-1.0 Hidden Base: 2000 World Champion], SWCCGDB
* [https://swccgdb.com/decklist/view/10/isb-2000-world-champion-1.0 ISB: 2000 World Champion], SWCCGDB

{REF}
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2000]]
""",
    )

    write_page(
        "2001 Decipher World Championship",
        """'''2001 Decipher World Championship''' was the sixth and last Decipher-era Star Wars CCG World Championship. Decipher had scheduled DecipherCon 2001 for 15–18 November at the Sheraton Oceanfront Hotel in Virginia Beach, with a $50,000 cash purse across its games.<ref name="tf">[https://www.theforce.net/ccg/story/DecipherCon_2001_72163.asp DecipherCon 2001], TheForce.Net (15 June 2001)</ref><ref name="pr">[http://www.theonering.net/torwp/OLDNEWS-3-996631229 DecipherCon 2001 press release] (26 June 2001; TheOneRing.net copy)</ref>

On 3 October 2001 Warren Holland cancelled the convention, citing September 11 airline-safety concerns. Decipher donated the $50,000 championship purse to September 11 relief.<ref name="cancel">[https://www.theonering.net/torwp/2001/10/03/27367-deicphercon-cancelled/ DecipherCon Cancelled], TheOneRing.net (3 October 2001)</ref><ref name="holland">[https://www.theforce.net/ccg/story/Special_message_from_Decipher_CEO_Warren_Holland_70685.asp Special message from Decipher CEO Warren Holland], TheForce.Net (3 October 2001)</ref> Players ran a replacement, '''FreedomCon''', in Virginia Beach under the same qualification rules. [[Bastian Winkelhaus]] (Germany) defeated [[Martin Akesson]] (Sweden).<ref name="wp">[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia</ref><ref name="awards">[https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org</ref>

A February 2002 press release on Game Players Network, copied to TheForce.Net, named Winkelhaus as the previous year's FreedomCon champion (returning Day 2 bye for 2002, with [[Matt Sokol]]).<ref name="hs">[https://www.theforce.net/ccg/story/The_Hyperspace_Lane_to_the_World_Championships_68998.asp The Hyperspace Lane to the World Championships], TheForce.Net (9 February 2002)</ref>

The constructed pool was [[Premiere - Reflections III]]. Full published 2001 constructed lists remain sparse; this hub records the champion, runner-up, site, format, and the cancellation.

Decipher's Star Wars, Young Jedi, and Jedi Knights licenses ended 31 December 2001. Tournament support moved to the volunteer [[Players Committee]].<ref name="ann">[https://web.archive.org/web/20030111000000/http://www.decipher.com/starwars/index.html Decipher Star Wars announcement] (Wayback)</ref>

== Format ==

* '''Environment:''' [[Premiere - Reflections III]]
* '''Site:''' FreedomCon, Virginia Beach, Virginia (player-run replacement for cancelled DecipherCon)
* '''Scheduled DecipherCon:''' 15–18 November 2001, Sheraton Oceanfront, Virginia Beach (cancelled 3 October 2001)

== Results ==

{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Bastian Winkelhaus]] || — || —
|-
| 2 || [[Martin Akesson]] || — || —
|}

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]
* [[History of the Players Committee]]
* [[Bastian Winkelhaus]] · [[Martin Akesson]]

== Sources ==

* [https://www.theforce.net/ccg/story/DecipherCon_2001_72163.asp DecipherCon 2001 dates], TheForce.Net (15 June 2001)
* [https://www.theforce.net/ccg/story/Special_message_from_Decipher_CEO_Warren_Holland_70685.asp Special message from Decipher CEO Warren Holland], TheForce.Net (3 October 2001)
* [https://www.theonering.net/torwp/2001/10/03/27367-deicphercon-cancelled/ DecipherCon Cancelled] (Holland letter, 3 October 2001)
* [https://web.archive.org/web/20050208232221/http://www.decipher.com/rfd/100501transcript.html Radio Free Decipher 99 transcript] (5 October 2001; Holland on the cancellation)
* [https://www.theforce.net/ccg/story/The_Hyperspace_Lane_to_the_World_Championships_68998.asp The Hyperspace Lane to the World Championships], TheForce.Net (9 February 2002)
* [https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Wikipedia World Champions table]
* [https://web.archive.org/web/20030111000000/http://www.decipher.com/starwars/index.html Decipher Star Wars index] (license end)

"""
        + REF
        + """
[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2001]]
""",
    )

    for year in range(1996, 2002):
        write_page(
            f"World Championship {year}",
            f"#REDIRECT [[199{year - 1990} Decipher World Championship]]\n"
            if year < 2000
            else f"#REDIRECT [[{year} Decipher World Championship]]\n",
        )
        write_page(
            f"{year} World Championship",
            f"#REDIRECT [[{year} Decipher World Championship]]\n",
        )
    write_page(
        "World Championship 1996",
        "#REDIRECT [[1996 Decipher World Championship]]\n",
    )


def insert_tourney(path: Path, title: str, bullets: str, lead: str | None = None) -> None:
    text = path.read_text(encoding="utf-8")
    if lead:
        text = re.sub(r"^'''.*?'''[^\n]*\n", lead.rstrip() + "\n", text, count=1)
    if "== Tournament results ==" in text:
        path.write_text(text, encoding="utf-8", newline="\n")
        TITLES.append((title, f"pages/{path.name}"))
        return
    block = "\n== Tournament results ==\n\n" + bullets.strip() + "\n"
    if "== See also ==" in text:
        text = text.replace("== See also ==", block + "\n== See also ==", 1)
    elif "== Sources ==" in text:
        text = text.replace("== Sources ==", block + "\n== Sources ==", 1)
    else:
        text = text.rstrip() + "\n" + block
    path.write_text(text, encoding="utf-8", newline="\n")
    TITLES.append((title, f"pages/{path.name}"))


def stub_person(title: str, lead: str, bullets: str, extra_src: str = "") -> None:
    body = f"""'''{title}''' {lead}

This page is a '''fan encyclopedia''' stub. Facts below are from published SWCCG tournament sources. It does not add unsourced biography.

== Tournament results ==

{bullets.strip()}

== See also ==

* [[Championships]]
* [[List of SWCCG tournaments]]

== Sources ==

* [https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm History of the World Finals], [[Trandosite]] (Wayback)
* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia
{extra_src}

{REF}
[[Category:People]]
[[Category:Players]]
[[Category:History]]
"""
    write_page(title, body)


def write_people() -> None:
    insert_tourney(
        PAGES / "Raphael_Asselin.wiki",
        "Raphael Asselin",
        "* 1st, [[1996 Decipher World Championship]] (def. [[Bjørn Sørgjerd]])\n* 12th, [[1997 Decipher World Championship]]\n* Day 3 (7th), [[2000 Decipher World Championship]]",
    )
    insert_tourney(
        PAGES / "Philipp_Jacobs.wiki",
        "Philipp Jacobs",
        "* 1st, [[1997 Decipher World Championship]] (def. [[Michael Riboulet]])\n* missed the 1998 final twelve",
    )
    insert_tourney(
        PAGES / "Gary_Carman.wiki",
        "Gary Carman",
        "* 1st, [[1999 Decipher World Championship]] (def. [[Steven Lewis]] 2 (+19))\n* Day 3 (10th), [[2000 Decipher World Championship]]",
    )
    insert_tourney(
        PAGES / "Matt_Sokol.wiki",
        "Matt Sokol",
        "* 1st, [[2000 Decipher World Championship]] (def. [[Yannick Lapointe]])\n* 1998 Worlds (Coruscant regional winner); 1999 Wildcard 3rd",
    )
    insert_tourney(
        PAGES / "Bastian_Winkelhaus.wiki",
        "Bastian Winkelhaus",
        "* final twelve, [[1997 Decipher World Championship]]\n* Day 1 leader, [[1999 Decipher World Championship]]\n* 1st, [[2001 Decipher World Championship]] (def. [[Martin Akesson]], FreedomCon)\n* 1st, 2018 and 2019 World Championships (Players Committee era; [https://www.starwarsccg.org/community/awards/ PC Hall of Fame])",
        lead="'''Bastian Winkelhaus''' is the 2001 SWCCG World Champion (FreedomCon, Virginia Beach). He was a World Finalist in 1997 and 1999. [[Trandosite]] interviewed him on 26 May 2000, before that title.<ref name=\"trando-iv3\">[https://web.archive.org/web/20041026204829/http://www.trandosite.mcmail.com/iv3.htm Bastian Winkelhaus interview], [[Trandosite]] (26 May 2000)</ref>\n",
    )
    insert_tourney(
        PAGES / "Martin_Akesson.wiki",
        "Martin Akesson",
        "* European Champion 2000\n* 2nd, [[2001 Decipher World Championship]]\n* Day 2 of [[2000 Decipher World Championship]]: 10 (+69), missed the twelve by one differential",
        lead="'''Martin Akesson''' was European Champion 2000 and runner-up at the [[2001 Decipher World Championship]]. [[Trandosite]] interviewed him on 31 August 2000.<ref name=\"trando-iv7\">[https://web.archive.org/web/20041026204829/http://www.trandosite.mcmail.com/iv7.htm Martin Akesson interview], [[Trandosite]] (31 August 2000)</ref>\n",
    )
    insert_tourney(
        PAGES / "Steven_Lewis.wiki",
        "Steven Lewis",
        "* 2nd, [[1999 Decipher World Championship]]",
    )
    insert_tourney(
        PAGES / "Yannick_Lapointe.wiki",
        "Yannick Lapointe",
        "* final twelve, [[1997 Decipher World Championship]]\n* 2nd, [[2000 Decipher World Championship]] (led Day 3; lost the Final Confrontation to [[Matt Sokol]])",
    )
    insert_tourney(
        PAGES / "Clint_Hays.wiki",
        "Clint Hays",
        "* Day 1 2nd, [[1999 Decipher World Championship]]\n* Day 2 leader (14 / +85), [[2000 Decipher World Championship]]; 8th on Day 3",
    )
    insert_tourney(
        PAGES / "Joe_Alread.wiki",
        "Joe Alread",
        "* 3rd, [[1996 Decipher World Championship]]\n* final twelve, [[1997 Decipher World Championship]]\n* Ironman winner, missed the 1999 main event",
    )

    stub_person(
        "Bjørn Sørgjerd",
        "was the runner-up at the [[1996 Decipher World Championship]] in Vail, Colorado (Norway). Trandosite spells the name Bjorn Sorgjerd; Wikipedia uses Bjørn Sørgjerd.",
        "* 2nd, [[1996 Decipher World Championship]] (lost the final to [[Raphael Asselin]])",
    )
    write_page("Bjorn Sorgjerd", "#REDIRECT [[Bjørn Sørgjerd]]\n")
    write_page("Bjorn Sørgjerd", "#REDIRECT [[Bjørn Sørgjerd]]\n")
    write_page("Bjørn Sorgjerd", "#REDIRECT [[Bjørn Sørgjerd]]\n")

    # Kevin Reitzel already has a Squadron / anagram stub. Do not overwrite; merge by hand.
    stub_person(
        "Michael Riboulet",
        "was runner-up at the [[1997 Decipher World Championship]] and the [[1998 Decipher World Championship]] (United Kingdom). He was the first player in two Grand Finals. Gary Carman later named him as a Bristol playtest partner.",
        "* 2nd, [[1997 Decipher World Championship]]\n* 2nd, [[1998 Decipher World Championship]]",
    )
    stub_person(
        "Matt Potter",
        "is the 1998 SWCCG World Champion (United States), the first American winner. He defeated [[Michael Riboulet]] 2 (+9) in the Operatives final at the Cavalier Hotel.",
        "* 1st, [[1998 Decipher World Championship]]",
    )
    # Paul Todd Feldman already has a 2025 Retro GEMPC table. Do not overwrite; merge by hand.
    stub_person(
        "Kevin Shannon",
        "finished 4th at the [[2000 Decipher World Championship]] Day 3. His Game 2 modified win vs Steve Brentson is the cut-math example on [[Tournaments]].",
        "* 4th Day 3, [[2000 Decipher World Championship]] (5 / +29; Modified Win vs Steve Brentson)",
        extra_src="* [https://web.archive.org/web/20010303120030/http://decipher.com/deciphercon/2000/events/results/starwars3.html DecipherCon 2000 Day 3]",
    )
    stub_person(
        "Kyle Craft",
        "finished 3rd at the [[2000 Decipher World Championship]] Day 3 (6 / +2), one differential slot behind [[Matt Sokol]] for the Final Confrontation.",
        "* 2nd after Day 2 (14 / +65) and 3rd Day 3, [[2000 Decipher World Championship]]",
        extra_src="* [https://web.archive.org/web/20010303120030/http://decipher.com/deciphercon/2000/events/results/starwars3.html DecipherCon 2000 Day 3]",
    )
    stub_person(
        "Lucas Hernandez",
        "made the [[1998 Decipher World Championship]] final twelve. Trandosite says he dominated day 2 until [[Michael Riboulet]] beat him by a large margin in the last game and took the final slot.",
        "* final twelve, [[1998 Decipher World Championship]]",
    )
    stub_person(
        "Maarten Logghe",
        "was one of the twelve finalists at the [[1996 Decipher World Championship]] in Vail.",
        "* finalist, [[1996 Decipher World Championship]]",
    )
    stub_person(
        "Dominic Gaudreault",
        "took the 12th and last Day 3 slot at the [[2000 Decipher World Championship]] (Day 2: 10 / +70) and finished 5th on Day 3.",
        "* 12th Day 2 / 5th Day 3, [[2000 Decipher World Championship]]",
        extra_src="* [https://web.archive.org/web/20001026043505/http://www.decipher.com/deciphercon/2000/events/results/starwars.html DecipherCon 2000 Day 2]",
    )


def write_url_list() -> None:
    urls = [
        "https://web.archive.org/web/20050517110350/http://trandosite.mcmail.com/wf00p2.htm",
        "https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game",
        "https://blog.categoryonegames.com/wp-content/uploads/2013/07/1998-World-Championship.pdf",
        "https://web.archive.org/web/20001026043505/http://www.decipher.com/deciphercon/2000/events/results/starwars.html",
        "https://web.archive.org/web/20010303120030/http://decipher.com/deciphercon/2000/events/results/starwars3.html",
        "https://www.theonering.net/torwp/2001/10/03/27367-deicphercon-cancelled/",
        "https://www.theforce.net/ccg/story/DecipherCon_2001_72163.asp",
        "https://www.theforce.net/ccg/story/Special_message_from_Decipher_CEO_Warren_Holland_70685.asp",
        "https://www.theforce.net/ccg/story/The_Hyperspace_Lane_to_the_World_Championships_68998.asp",
        "https://www.starwarsccg.org/community/awards/",
        "https://web.archive.org/web/20050208232221/http://www.decipher.com/rfd/100501transcript.html",
        "https://web.archive.org/web/20030111000000/http://www.decipher.com/starwars/index.html",
        "https://arstechnica.com/gaming/2015/12/that-one-time-i-played-in-the-star-wars-card-game-world-championship/",
        "https://www.starwarsccg.org/jawa/",
        "https://www.starwarsccg.org/tournaments/",
        "https://www.facebook.com/kevin.reitzel/posts/its-been-30-years-my-star-wars-ccg-1996-championship-deck-lists-that-i-used-at-t/10241711434940142/",
        "https://swccgdb.com/decklist/view/1/1996-world-champion-light-1.0",
        "https://swccgdb.com/decklist/view/2/1996-world-champion-dark-1.0",
        "https://swccgdb.com/decklist/view/3/mains-toys-1997-world-champion-1.0",
        "https://swccgdb.com/decklist/view/4/dagobah-turtle-1997-world-champion-1.0",
        "https://swccgdb.com/decklist/view/5/operatives-1998-world-champion-1.0",
        "https://swccgdb.com/decklist/view/6/operatives-1998-world-champion-1.0",
        "https://swccgdb.com/decklist/view/7/isb-1999-world-champion-1.0",
        "https://swccgdb.com/decklist/view/8/hidden-base-1999-world-champion-1.0",
        "https://swccgdb.com/decklist/view/9/hidden-base-2000-world-champion-1.0",
        "https://swccgdb.com/decklist/view/10/isb-2000-world-champion-1.0",
        "https://swccgdb.com/decklist/view/12/dagobah-a-manipulator-2nd-at-worlds-1997-1.0",
        "https://swccgdb.com/decklist/view/13/dagobah-miner-s-guild-2nd-at-worlds-1997-1.0",
        "https://swccgdb.com/decklist/view/14/operatives-speeders-2nd-at-worlds-1999-1.0",
        "https://swccgdb.com/decklist/view/15/hunt-down-2nd-at-worlds-1999-1.0",
        "https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/",
    ]
    p = ROOT / "encyclopedia" / "decipher-worlds-urls.txt"
    p.write_text("\n".join(urls) + "\n", encoding="utf-8")
    print("urls", len(urls), p)


def main() -> None:
    write_format_stubs()
    write_indexes()
    patch_formats()
    patch_premiere_ds2()
    patch_jawa_cup()
    patch_charity()
    patch_tournaments_akesson()
    for meta in DECK_META:
        write_swccgdb_deck(meta)
    write_reitzel_decks()
    write_hubs()
    write_people()
    write_url_list()
    # de-dupe titles, last write wins
    seen: dict[str, str] = {}
    for t, r in TITLES:
        seen[t] = r
    tsv = ROOT / "decipher-worlds-titles.tsv"
    tsv.write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8")
    print("pages", len(seen), "tsv", tsv)


if __name__ == "__main__":
    main()

