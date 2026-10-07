#!/usr/bin/env python3
"""2008 World Championship hub + transcribed lists (Virtual Sets 2002-2009).

Format note: 2008 is pre-Virtual-Block reorg (same pool as 2007). Use
[[Virtual Sets (2002-2009)]], not [[Legacy Open]] / Virtual Block dests.
Dates on sheets: Day 1 10/10/08, Day 2 10/11/08, Day 3 10/12/08.
Site Minneapolis MN. Winner Kevin Shannon def. Kyle Krueger (HoF).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
TSV = ROOT / "y2008-worlds-titles.tsv"
MEDIA = ROOT / "y2008-worlds-media"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"

EVENT = "2008 World Championship"
DATES = "10â€“12 October 2008"
FORMAT = "[[Virtual Sets (2002-2009)|Decipher + Virtual Sets (2002-2009)]]"
FORMAT_SHORT = "[[Virtual Sets (2002-2009)|Decipher + Virtual Sets (2002-2009)]]"
SITE = "Minneapolis, Minnesota"
WINNER = "[[Kevin Shannon]]"
CAT = "[[Category:2008]]"
PC_INDEX = "https://www.starwarsccg.org/2008-decklists/"
HOF = "https://www.starwarsccg.org/community/awards/"
PDF = {
    "Day 1": ("https://res.starwarsccg.org/Resources/tournaments/Decklists/2008/Worlds/2008+Worlds+D1.pdf", "2008 Worlds Day 1.pdf"),
    "Day 2": ("https://res.starwarsccg.org/Resources/tournaments/Decklists/2008/Worlds/2008+Worlds+D2.pdf", "2008 Worlds Day 2.pdf"),
    "Day 3": ("https://res.starwarsccg.org/Resources/tournaments/Decklists/2008/Worlds/2008+Worlds+D3.pdf", "2008 Worlds Day 3.pdf"),
    "Team": ("https://res.starwarsccg.org/Resources/tournaments/Decklists/2008/Worlds/2008+Worlds+Team.pdf", "2008 Worlds Team.pdf"),
}

titles_out: list[tuple[str, str]] = []


def write(title: str, text: str) -> str:
    fn = wiki_fname(title)
    if not fn.endswith(".wiki"):
        fn += ".wiki"
    path = PAGES / fn
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    titles_out.append((title, f"pages/{fn}"))
    return f"pages/{fn}"


def write_stub(player: str, text: str) -> str:
    fn = wiki_fname(player) + ".wiki"
    path = STUBS / fn
    path.parent.mkdir(parents=True, exist_ok=True)
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    titles_out.append((player, f"pages/player-stubs/{fn}"))
    return f"pages/player-stubs/{fn}"


def scan_table(scan_file: str, pdf_label: str, page: int) -> str:
    return (
        '{| style="margin:0 auto;border:0;border-collapse:collapse;background:transparent"\n'
        "|-\n"
        f'| style="vertical-align:top;border:0;padding:0" | [[File:{scan_file}|800px]]\n'
        f'| style="vertical-align:top;border:0;padding:0 0 0 0.2em;line-height:1" | '
        f"<ref>Page {page} of [[:File:{pdf_label}]].</ref>\n"
        "|}"
    )


def type_cut(groups: list[tuple[str, list[tuple[int, str]]]]) -> str:
    blocks = []
    for heading, cards in groups:
        bits = [f"'''{heading}'''"]
        for qty, link in cards:
            bits.append(f"* {qty}x {link}" if qty > 1 else f"* {link}")
        blocks.append("\n".join(bits))
    mid = (len(blocks) + 1) // 2
    left = "\n\n".join(blocks[:mid])
    right = "\n\n".join(blocks[mid:])
    return (
        '{| class="wikitable" style="width:100%;"\n'
        "|-\n"
        '| style="width:50%; vertical-align:top;" |\n'
        f"{left}\n"
        '| style="width:50%; vertical-align:top;" |\n'
        f"{right}\n"
        "|}\n"
    )


def deck_page(
    *,
    title: str,
    player: str,
    side: str,
    stage: str,
    starting: str,
    archetype_pipe: str,
    groups: list[tuple[str, list[tuple[int, str]]]],
    scan_file: str,
    page: int,
    public_note: str | None = None,
) -> str:
    pdf_url, pdf_label = PDF[stage if stage != "Team" else "Team"]
    if stage.startswith("Day"):
        pass
    side_cat = "Dark Side decks" if side == "Dark" else "Light Side decks"
    lead = (
        f"'''{title}''' was the {side} Side constructed list played by [[{player}]] "
        f"at [[{EVENT}]] ({stage})."
    )
    if public_note:
        lead += f" {public_note}"
    body = f"""{lead}


== Deck info ==

* '''Player:''' [[{player}]]
* '''Event:''' [[{EVENT}]]
* '''Format:''' {FORMAT_SHORT}
* '''Side:''' [[{side}]]
* '''Starting Card:''' {starting}
* '''Stage:''' {stage}

== Decklist ==

{type_cut(groups)}

== Scan ==

{scan_table(scan_file, pdf_label, page)}

== See also ==

* [[{EVENT}]]
* [[{player}]]
* [[List of SWCCG tournaments]]

== Sources ==

* [{pdf_url} {pdf_label}], res.starwarsccg.org
* [{PC_INDEX} 2008 Decklists], starwarsccg.org
* [{HOF} Awards and Hall of Fame], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:{side_cat}]]
[[Category:2008]]
"""
    return write(title, body)


# --- Tom Frafjord Day 3 DS TTO / Endor Operations (p07) ---
FRAFJORD_DS_GROUPS = [
    ("Objective", [(1, "[[Endor Operations / Imperial Outpost|Endor Operations]]")]),
    ("Location", [
        (1, "[[Endor]]"),
        (1, "[[Endor: Landing Platform]]"),
        (1, "[[Endor: Bunker]]"),
        (1, "[[Death Star II]]"),
        (1, "[[Death Star II: Capacitors]]"),
        (1, "[[Death Star II: Coolant Shaft]]"),
        (1, "[[Death Star II: Docking Bay]]"),
        (1, "[[Death Star II: Reactor Core]]"),
        (1, "[[Tatooine]]"),
    ]),
    ("Character", [
        (1, "[[Moff Jerjerrod]]"),
        (1, "[[Admiral Chiraneau]]"),
        (1, "[[Admiral Ozzel]]"),
        (1, "[[Commander Igar (V)]]"),
        (1, "[[Commander Merrejk]]"),
        (1, "[[Darth Maul With Lightsaber]]"),
        (1, "[[General Veers (V)]]"),
        (1, "[[Grand Admiral Thrawn]]"),
    ]),
    ("Starship", [
        (1, "[[Conquest (V)]]"),
        (1, "[[Devastator (V)]]"),
        (3, "[[Imperial-Class Star Destroyer (V)]]"),
        (1, "[[Thunderflare]]"),
        (1, "[[Tyrant]]"),
    ]),
    ("Vehicle", [
        (1, "[[Blizzard 1 (V)]]"),
        (1, "[[Blizzard 2]]"),
        (2, "[[Blizzard 4]]"),
    ]),
    ("Effect", [
        (1, "[[Operational As Planned]]"),
        (1, "[[Imperial Arrest Order & The Secret Plans|Imperial Arrest Order and Secret Plans]]"),
        (1, "[[Breached Defenses (V)]]"),
        (1, "[[Endor Shield (V)]]"),
        (1, "[[Image Of The Dark Lord (V)]]"),
        (1, "[[Imperial Decree (V)]]"),
        (1, "[[No Escape]]"),
        (1, "[[That Thing's Operational]]"),
        (1, "[[Knowledge And Defense (V)]]"),
    ]),
    ("Interrupt", [
        (3, "[[Cold Feet (V)]]"),
        (1, "[[Come With Me]]"),
        (3, "[[Control]]"),
        (1, "[[Control & Set For Stun]]"),
        (2, "[[Imperial Command]]"),
        (1, "[[Lateral Damage]]"),
        (1, "[[Limited Resources]]"),
        (1, "[[Masterful Move]]"),
        (1, "[[Omni Box & It's Worse]]"),
        (1, "[[Projective Telepathy]]"),
        (1, "[[Twi'lek Advisor]]"),
        (2, "[[We Must Accelerate Our Plans]]"),
        (1, "[[We Shall Double Our Efforts!]]"),
        (3, "[[We're In Attack Position Now]]"),
    ]),
    ("Defensive Shield", [
        (1, "[[Abyss (V)]]"),
        (1, "[[Allegations Of Corruption]]"),
        (1, "[[Battle Order]]"),
        (1, "[[Come Here You Big Coward]]"),
        (1, "[[Fanfare]]"),
        (1, "[[Firepower (V)]]"),
        (1, "[[Oppressive Enforcement]]"),
        (1, "[[Reactor Terminal (V)]]"),
        (1, "[[Resistance]]"),
        (1, "[[Something Special Planned For Them (V)]]"),
        (1, "[[There'll Be Hell To Pay]]"),
        (1, "[[Do They Have A Code Clearance?]]"),
    ]),
]


def ensure_player(player: str, rows_html: str) -> None:
    stub_path = STUBS / (wiki_fname(player) + ".wiki")
    if stub_path.exists():
        text = stub_path.read_text(encoding="utf-8")
        if EVENT in text and "Day 3" in text and player.split()[0] in text:
            # still rewrite with tidy if needed
            pass
        # inject / replace tournament results conservatively via rewrite
    body = f"""'''{player}''' is a ''Star Wars'' CCG player.

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{rows_html}
|}}

== See also ==

* [[{EVENT}]]
* [[List of SWCCG tournaments]]

== Sources ==

* [{PDF['Day 3'][0]} 2008 Worlds Day 3 PDF], res.starwarsccg.org
* [{HOF} Awards and Hall of Fame], starwarsccg.org

[[Category:Players]]
[[Category:2008]]
"""
    write_stub(player, body)


def hub() -> None:
    # Day 3 transcribed cells
    d3 = [
        ("Steve Baroni", "Hunt Down And Destroy The Jedi", None, True, False),  # DS transcribed later
        ("Jonny Chu", None, None, False, False),
        ("Garrett Larson", "Ralltiir Operations", None, False, False),
        ("Tom Frafjord", "Endor Operations", "I-podracer", True, False),
        ("Kyle Krueger", "You Can Stop Screaming Now", "Still a Kyle Deck", False, False),
        ("Brian Hunter", "mistryl Headaches", "No Virtual Emperors, Por Favor", False, False),
        ("Kevin Shannon", "Ralltiir Operations", "D-B-Oh No!", False, False),
        ("Michael Raveling", None, None, False, False),
    ]
    # For now only Frafjord DS has a deck page title
    frafjord_ds_title = "2008 Worlds Day 3 Tom Frafjord DS Endor Operations"

    def cell(player, side, label, linked_title):
        if linked_title:
            return f"[[{linked_title}|{label}]]"
        if label:
            return "â€”"  # listed on sheet but not yet transcribed as wiki page
        return "â€”"

    bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    # Tom Frafjord row with DS link
    rows = {
        "Steve Baroni": ("â€”", "â€”"),
        "Jonny Chu": ("â€”", "â€”"),
        "Garrett Larson": ("â€”", "â€”"),
        "Tom Frafjord": (f"[[{frafjord_ds_title}|Endor Operations]]", "â€”"),
        "Kyle Krueger": ("â€”", "â€”"),
        "Brian Hunter": ("â€”", "â€”"),
        "Kevin Shannon": ("â€”", "â€”"),
        "Michael Raveling": ("â€”", "â€”"),
    }
    for p, (ds, ls) in rows.items():
        bits.append("|-")
        bits.append(f"| [[{p}]] || {ds} || {ls}")
    bits.append("|}")
    tbl3 = "\n".join(bits)

    # Day 1 inventory (all sheet pairs; empty until transcribed)
    d1_players = [
        "Warren Maruschak", "Jason Jenkins", "Jim Radloff", "Thomas Whaley",
        "David McCune", "John Anderson", "Matt Sherrington", "Robert J Johnson",
        "Brady Moore", "Justin Kaufman", "Mark Peterson", "Shawn Banwell",
        "Sean Miller", "Brandon Brist", "Peter Davis", "Alden Peterson",
        "Markey", "Walseth",
    ]
    # Markey DS + Walseth LS are separate incomplete names
    d1_bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    pairs = [
        ("Warren Maruschak", "Agents Of Black Sun", "DBO"),
        ("Jason Jenkins", "Hunt Down And Destroy The Jedi", "Mind What You Have Learned"),
        ("Jim Radloff", "Boom ball '08", "Your Wife"),
        ("Thomas Whaley", "I AM A TOOL", "Some old BS"),
        ("David McCune", "Loses to wts.", "Cloners"),
        ("John Anderson", "Greedo's Scum", "Watch Your Step"),
        ("Matt Sherrington", "My Lord, Is That Legal?", "Fallon Rolls"),
        ("Robert J Johnson", "Bring Him Before Me", "Agents In The Court"),
        ("Brady Moore", "Hunt Down And Destroy The Jedi", "LSC"),
        ("Justin Kaufman", "Endor Operations", "BBO"),
        ("Mark Peterson", "Hunt Down And Destroy The Jedi", "Anger, Fear, Aggression (V)"),
        ("Shawn Banwell", "Hunt Down And Destroy The Jedi", "Careful Planning (V)"),
        ("Sean Miller", "Imperial Arrest Order", "Hidden Base"),
        ("Brandon Brist", "Hunt Down And Destroy The Jedi", "Quiet Mining Colony"),
        ("Peter Davis", "â€”", "â€”"),
        ("Alden Peterson", "Strand", "â€”"),
        ("Markey", "â€”", None),  # DS only incomplete
        ("Walseth", None, "â€”"),  # LS only incomplete
    ]
    for player, ds_lab, ls_lab in pairs:
        ds = "â€”" if ds_lab else ""
        ls = "â€”" if ls_lab else ""
        if ds_lab is None:
            ds = ""
        if ls_lab is None:
            ls = ""
        # show â€” for pending transcription
        ds_cell = "â€”" if ds_lab not in (None, "") else ""
        ls_cell = "â€”" if ls_lab not in (None, "") else ""
        if ds_lab is None:
            ds_cell = ""
        if ls_lab is None:
            ls_cell = ""
        # Always show emdash for sides that have a sheet
        if ds_lab is not None:
            ds_cell = "â€”"
        else:
            ds_cell = ""
        if ls_lab is not None:
            ls_cell = "â€”"
        else:
            ls_cell = ""
        d1_bits.append("|-")
        d1_bits.append(f"| [[{player}]] || {ds_cell or 'â€”'} || {ls_cell or 'â€”'}")
    # Fix Markey / Walseth rows properly
    d1_bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    for player, ds_lab, ls_lab in [
        ("Warren Maruschak", True, True),
        ("Jason Jenkins", True, True),
        ("Jim Radloff", True, True),
        ("Thomas Whaley", True, True),
        ("David McCune", True, True),
        ("John Anderson", True, True),
        ("Matt Sherrington", True, True),
        ("Robert J Johnson", True, True),
        ("Brady Moore", True, True),
        ("Justin Kaufman", True, True),
        ("Mark Peterson", True, True),
        ("Shawn Banwell", True, True),
        ("Sean Miller", True, True),
        ("Brandon Brist", True, True),
        ("Peter Davis", True, True),
        ("Alden Peterson", True, True),
        ("Markey", True, False),
        ("Walseth", False, True),
    ]:
        ds = "â€”" if ds_lab else ""
        ls = "â€”" if ls_lab else ""
        d1_bits.append("|-")
        d1_bits.append(f"| [[{player}]] || {ds or ''} || {ls or ''}")
    d1_bits.append("|}")
    tbl1 = "\n".join(d1_bits)

    body = f"""'''{EVENT}''' was a Players Committee constructed World Championship, {DATES}, in {SITE}. The constructed pool was Decipher-printed cards plus the [[Virtual Sets (2002-2009)|pre-reorg Virtual Sets]] legal in 2008 (not [[Legacy Open]] / Virtual Block). {WINNER} defeated [[Kyle Krueger]] in the final.<ref name="hof">{HOF}</ref> Published lists are the Day 1â€“3 and Team PDFs on the Players Committee decklist desk.<ref name="tdl">{PC_INDEX}</ref> Dates on the sheets are 10 October 2008 (Day 1), 11 October 2008 (Day 2), and 12 October 2008 (Day 3).


== Format ==

* '''Environment:''' {FORMAT_SHORT}
* '''Site:''' {SITE}
* '''Dates:''' {DATES}
* '''Winner:''' {WINNER}

== Day 3 ==

{tbl3}

Day 3 Top 8 Xerox and typed sheets are in [[:File:2008 Worlds Day 3.pdf]].

== Day 2 ==

Day 2 lists (119 pages) are being transcribed from [[:File:2008 Worlds Day 2.pdf]].

== Day 1 ==

{tbl1}

Remaining Day 1 Xerox and typed sheets are in [[:File:2008 Worlds Day 1.pdf]].

== Team Tournament ==

Team Tournament lists are being transcribed from [[:File:2008 Worlds Team.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Championships]]
* [[Virtual Sets (2002-2009)]]
* [[Formats]]

== Sources ==

* [{PC_INDEX} 2008 Decklists], starwarsccg.org
* [{HOF} Awards and Hall of Fame], starwarsccg.org
* [{PDF['Day 1'][0]} 2008 Worlds Day 1 PDF], res.starwarsccg.org
* [{PDF['Day 2'][0]} 2008 Worlds Day 2 PDF], res.starwarsccg.org
* [{PDF['Day 3'][0]} 2008 Worlds Day 3 PDF], res.starwarsccg.org
* [{PDF['Team'][0]} 2008 Worlds Team PDF], res.starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Championships]]
[[Category:2008]]
[[Category:Tournaments]]
"""
    write(EVENT, body)


def patch_list() -> None:
    if not LIST.exists():
        print("WARN no List_of_SWCCG_tournaments.wiki")
        return
    text = LIST.read_text(encoding="utf-8")
    if "2008 World Championship" in text:
        print("List already has 2008 World Championship")
        return
    section = (
        "\n== 2008 ==\n\n"
        '{| class="wikitable sortable"\n'
        "|-\n"
        "! Tag !! Event !! Dates !! Site !! Format !! Winner\n"
        "|-\n"
        f"| 2008-10-10 || [[{EVENT}|World Championship]] "
        f"|| {DATES} || Minneapolis, Minnesota || {FORMAT_SHORT} || {WINNER}\n"
        "|}\n"
    )
    for needle in ("== 2007 ==", "== Decipher World Championships =="):
        if needle in text:
            LIST.write_text(
                text.replace(needle, section + "\n" + needle, 1),
                encoding="utf-8",
                newline="\n",
            )
            titles_out.append(
                ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki")
            )
            print("patched List")
            return
    print("WARN could not patch List automatically")


def main() -> None:
    MEDIA.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)
    STUBS.mkdir(parents=True, exist_ok=True)

    # Category stub
    write("Category:2008", "{{category}}\n\nWorld Championship and related pages for 2008.\n")

    title = "2008 Worlds Day 3 Tom Frafjord DS Endor Operations"
    deck_page(
        title=title,
        player="Tom Frafjord",
        side="Dark",
        stage="Day 3",
        starting="[[Endor Operations / Imperial Outpost|Endor Operations]]",
        archetype_pipe="Endor Operations",
        groups=FRAFJORD_DS_GROUPS,
        scan_file="2008 Worlds Day 3 p07 Tom Frafjord DS.png",
        page=7,
        public_note="Sheet event field reads Worlds Day 3; deck title TTO (That Thing's Operational / Endor Operations).",
    )

    ensure_player(
        "Tom Frafjord",
        "|-\n| '''10â€“12 October 2008''' || [[2008 World Championship]] (Day 3) || "
        f"{FORMAT_SHORT} || â€” || [[2008 Worlds Day 3 Tom Frafjord DS Endor Operations|Endor Operations]] || â€”\n",
    )

    hub()
    patch_list()

    # TSV
    lines = [f"{t}\t{p}" for t, p in titles_out]
    TSV.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("Wrote", len(titles_out), "titles ->", TSV)
    for t, p in titles_out:
        print(" ", t, "->", p)


if __name__ == "__main__":
    main()