#!/usr/bin/env python3
"""Rebuild Outrider Cup hubs as team events: winner = team, rosters, matches, player rows."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from generate_2019_2021 import is_bio, tidy_player_page, wiki_fname  # noqa: E402
from generate_2026_remaining import upsert_stub  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
TSV = ROOT / "outrider-teams-titles.tsv"


def refs() -> str:
    return """{{#if:1|<nowiki />
<h2>References</h2>
<references />}}"""


def L(page: str, label: str) -> str:
    return f"[[{page}|{label}]]"


def cell(page: str | None, label: str | None) -> str:
    if not page or not label:
        return "—"
    return L(page, label)


def table(headers: list[str], rows: list[list[str]], sortable: bool = False) -> str:
    klass = "wikitable sortable" if sortable else "wikitable"
    bits = [f'{{| class="{klass}"', "! " + " !! ".join(headers)]
    for row in rows:
        bits += ["|-", "| " + " || ".join(row)]
    bits.append("|}")
    return "\n".join(bits)


def roster_table(
    players: list[tuple[str, str | None, str | None, str | None, str | None]],
    captains: set[str],
    picks: set[str] | None = None,
) -> str:
    picks = picks or set()
    rows = []
    for name, ds_p, ds_l, ls_p, ls_l in players:
        cap = " <small>(captain)</small>" if name in captains else ""
        pick = " <small>(captain's pick)</small>" if name in picks else ""
        rows.append([f"[[{name}]]{cap}{pick}", cell(ds_p, ds_l), cell(ls_p, ls_l)])
    return table(["Player", "Dark", "Light"], rows, sortable=True)


# --- 2019 deck pages (existing hub titles) ---
def d19(stage: str, player: str, side: str, slug: str, label: str) -> tuple[str, str]:
    return (f"2019 Outrider Cup {stage} {player} {side} {slug}", label)


R1 = "Round 1"
R2 = "Round 2"

C19_R1 = {
    "Justin Branch": (d19(R1, "Justin Branch", "DS", "I Want That Map", "I Want That Map"), d19(R1, "Justin Branch", "LS", "Old Allies", "Old Allies")),
    "Tom Damen": (d19(R1, "Tom Damen", "DS", "My Lord, Is That Legal", "My Lord, Is That Legal?"), d19(R1, "Tom Damen", "LS", "They Have No Idea We're Coming", "They Have No Idea We're Coming")),
    "Stephan de Vos": (d19(R1, "Stephan de Vos", "DS", "Hunt Down And Destroy The Jedi (V)", "Hunt Down And Destroy The Jedi (V)"), d19(R1, "Stephan de Vos", "LS", "Careful Planning (V)", "Careful Planning (V)")),
    "Quirin Fürgut": (d19(R1, "Quirin Fürgut", "DS", "A Stunning Move", "A Stunning Move"), d19(R1, "Quirin Fürgut", "LS", "The Galaxy May Need A Legend", "The Galaxy May Need A Legend")),
    "Emil Wallin": (d19(R1, "Emil Wallin", "DS", "No Money, No Parts, No Deal!", "No Money, No Parts, No Deal!"), d19(R1, "Emil Wallin", "LS", "Diplomatic Mission To Alderaan", "Diplomatic Mission To Alderaan")),
    "Bastian Winkelhaus": (d19(R1, "Bastian Winkelhaus", "DS", "Ralltiir Operations (V)", "Ralltiir Operations (V)"), d19(R1, "Bastian Winkelhaus", "LS", "Yavin 4: Massassi Throne Room", "Yavin 4: Massassi Throne Room")),
    "Justin Desai": (d19(R1, "Justin Desai", "DS", "Ralltiir Operations (V)", "Ralltiir Operations (V)"), d19(R1, "Justin Desai", "LS", "Rendezvous Point On Tatooine (V)", "Rendezvous Point On Tatooine (V)")),
    "Chris Kelly": (d19(R1, "Chris Kelly", "DS", "Hunt Down And Destroy The Jedi (V)", "Hunt Down And Destroy The Jedi (V)"), d19(R1, "Chris Kelly", "LS", "He Is The Chosen One", "He Is The Chosen One")),
    "Bryan Mischke": (d19(R1, "Bryan Mischke", "DS", "Endor Operations", "Endor Operations"), d19(R1, "Bryan Mischke", "LS", "Yavin 4: Massassi Throne Room", "Yavin 4: Massassi Throne Room")),
    "Joe Olson": (d19(R1, "Joe Olson", "DS", "I Want That Map", "I Want That Map"), d19(R1, "Joe Olson", "LS", "Diplomatic Mission To Alderaan", "Diplomatic Mission To Alderaan")),
    "Greg Shaw": (d19(R1, "Greg Shaw", "DS", "Agents Of Black Sun", "Agents Of Black Sun"), d19(R1, "Greg Shaw", "LS", "Old Allies", "Old Allies")),
    "Chris Wirfs": (d19(R1, "Chris Wirfs", "DS", "Court Of The Vile Gangster", "Court Of The Vile Gangster"), d19(R1, "Chris Wirfs", "LS", "There Is Good In Him", "There Is Good In Him")),
}
C19_R2 = {
    "Justin Branch": (d19(R2, "Justin Branch", "DS", "Court Of The Vile Gangster", "Court Of The Vile Gangster"), d19(R2, "Justin Branch", "LS", "They Have No Idea We're Coming", "They Have No Idea We're Coming")),
    "Tom Damen": (d19(R2, "Tom Damen", "DS", "A Stunning Move", "A Stunning Move"), d19(R2, "Tom Damen", "LS", "He Is The Chosen One", "He Is The Chosen One")),
    "Stephan de Vos": (d19(R2, "Stephan de Vos", "DS", "Agents Of Black Sun", "Agents Of Black Sun"), d19(R2, "Stephan de Vos", "LS", "Careful Planning (V)", "Careful Planning (V)")),
    "Quirin Fürgut": (d19(R2, "Quirin Fürgut", "DS", "ISB Operations", "ISB Operations"), d19(R2, "Quirin Fürgut", "LS", "Careful Planning (V)", "Careful Planning (V)")),
    "Emil Wallin": (d19(R2, "Emil Wallin", "DS", "Endor Operations", "Endor Operations"), d19(R2, "Emil Wallin", "LS", "Old Allies", "Old Allies")),
    "Bastian Winkelhaus": (d19(R2, "Bastian Winkelhaus", "DS", "I Want That Map", "I Want That Map"), d19(R2, "Bastian Winkelhaus", "LS", "Diplomatic Mission To Alderaan", "Diplomatic Mission To Alderaan")),
    "Justin Desai": (d19(R2, "Justin Desai", "DS", "Endor Operations", "Endor Operations"), d19(R2, "Justin Desai", "LS", "The Galaxy May Need A Legend", "The Galaxy May Need A Legend")),
    "Chris Kelly": (d19(R2, "Chris Kelly", "DS", "Court Of The Vile Gangster", "Court Of The Vile Gangster"), d19(R2, "Chris Kelly", "LS", "We Have A Plan", "We Have A Plan")),
    "Bryan Mischke": (d19(R2, "Bryan Mischke", "DS", "Agents Of Black Sun", "Agents Of Black Sun"), d19(R2, "Bryan Mischke", "LS", "Rendezvous Point On Tatooine (V)", "Rendezvous Point On Tatooine (V)")),
    "Joe Olson": (d19(R2, "Joe Olson", "DS", "Ralltiir Operations (V)", "Ralltiir Operations (V)"), d19(R2, "Joe Olson", "LS", "Yavin 4: Massassi Throne Room", "Yavin 4: Massassi Throne Room")),
    "Greg Shaw": (d19(R2, "Greg Shaw", "DS", "Imperial Entanglements", "Imperial Entanglements"), d19(R2, "Greg Shaw", "LS", "He Is The Chosen One", "He Is The Chosen One")),
    "Chris Wirfs": (d19(R2, "Chris Wirfs", "DS", "I Want That Map", "I Want That Map"), d19(R2, "Chris Wirfs", "LS", "Old Allies", "Old Allies")),
}

USA19 = ["Joe Olson", "Bryan Mischke", "Justin Desai", "Chris Kelly", "Greg Shaw", "Chris Wirfs"]
EUR19 = ["Bastian Winkelhaus", "Emil Wallin", "Justin Branch", "Tom Damen", "Stephan de Vos", "Quirin Fürgut"]


def pack(cmap, names):
    out = []
    for n in names:
        (ds_p, ds_l), (ls_p, ls_l) = cmap[n]
        out.append((n, ds_p, ds_l, ls_p, ls_l))
    return out


def yt(vid: str, lab: str) -> str:
    return f"[https://youtu.be/{vid} {lab}]"


def write_2019() -> str:
    r1_matches = table(
        ["Team USA", "Team Europe", "Games", "Match"],
        [
            ["[[Chris Wirfs]]", "[[Bastian Winkelhaus]]", f"{yt('7-8DF6xesa0', 'G1')} Bastian +8; {yt('0TCp2WPWk3E', 'G2')}", "—"],
            ["[[Justin Desai]]", "[[Emil Wallin]]", yt("10KvpymOZSk", "G1 & G2"), "—"],
            ["[[Joe Olson]]", "[[Justin Branch]]", yt("-SyXiG9vGZw", "G1 & G2") + " (split, per Olson)", "split"],
            ["[[Greg Shaw]]", "[[Quirin Fürgut]]", f"{yt('_O8vkVayEVw', 'G1')} Quirin +5; {yt('6ZXLDRxBuRQ', 'G2')}", "—"],
            ["[[Chris Kelly]]", "[[Stephan de Vos]]", yt("E1YQBFl0fes", "G1 & G2"), "Stephan de Vos"],
            ["[[Bryan Mischke]]", "[[Tom Damen]]", "played 15 December 2019", "—"],
        ],
    )
    r2_matches = table(
        ["Team USA", "Team Europe", "Games", "Match"],
        [
            ["[[Joe Olson]]", "[[Bastian Winkelhaus]]", f"{yt('ZAC_Wn9Bw_A', 'G1 & G2')} Bastian +24; Olson concedes G2", "Bastian Winkelhaus"],
            ["[[Chris Kelly]]", "[[Emil Wallin]]", f"{yt('LZs-vw3F3vU', 'G1')} Emil +12; {yt('cGcsgysrnws', 'G2')} Kelly by over 12", "split"],
            ["[[Greg Shaw]]", "[[Justin Branch]]", f"{yt('UDJccVBYhpE', 'G1')} Branch +16", "—"],
            ["[[Chris Wirfs]]", "[[Quirin Fürgut]]", f"{yt('UfQjnOogic0', 'G1')} Wirfs LS +23; Quirin concedes G2", "Chris Wirfs"],
            ["[[Bryan Mischke]]", "[[Stephan de Vos]]", yt("UglxdllFzLI", "stream"), "—"],
            ["[[Justin Desai]]", "[[Tom Damen]]", f"{yt('wdT3-tS-So8', 'G1')} Desai +29; Damen concedes G2", "Justin Desai"],
        ],
    )
    body = f"""'''2019 Outrider Cup''' was the inaugural Players Committee biennial Europe versus United States team event on GEMP, 3 December 2019 – 20 January 2020. '''[[Team USA]]''' defeated [[Team Europe]] 7–4.<ref name="score">https://forum.starwarsccg.org/viewtopic.php?t=74099</ref><ref name="congrats">https://forum.starwarsccg.org/viewtopic.php?t=74436</ref>

[[Chris Gogolen]] designed the event as six-a-side match play on GEMP: five players from Player of the Year points plus one captain's pick per side, unique objectives per team each round, and a race to seven match points (12 matches across two rounds). [[Joe Olson]] captained Team USA and assigned the Round 1 pairings; [[Bastian Winkelhaus]] captained Team Europe. Round 1 (3–15 December 2019) used the pre-December 2019 errata; Round 2 (7–20 January 2020) used the post-December 2019 errata.<ref name="info">https://forum.starwarsccg.org/viewtopic.php?t=73616</ref>

The forum scoreboard is titled "TEAM USA WINS THE CUP!" The congratulations thread is '''Congratulations Team USA'''; Tom Damen's first post opened "Well done Murica!"<ref name="congrats" /> Team USA later received Outrider Cup hoodies after the win.<ref name="wrap21">https://www.starwarsccg.org/team-europe-wins-the-2021-outrider-cup/</ref>

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' GEMP (teams)
* '''Dates:''' 3 December 2019 – 20 January 2020
* '''Winner:''' [[Team USA]] (7–4)
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1168 2019 Outrider Cup]

== Rosters ==

=== Team USA ===

Captain [[Joe Olson]]. Captain's pick: [[Chris Wirfs]].<ref name="info" />

{roster_table(pack(C19_R1, USA19), {"Joe Olson"}, {"Chris Wirfs"})}

Round 2 lists (post-December 2019 errata):

{roster_table(pack(C19_R2, USA19), {"Joe Olson"}, {"Chris Wirfs"})}

=== Team Europe ===

Captain [[Bastian Winkelhaus]]. Captain's pick: [[Quirin Fürgut]].<ref name="info" />

{roster_table(pack(C19_R1, EUR19), {"Bastian Winkelhaus"}, {"Quirin Fürgut"})}

Round 2 lists:

{roster_table(pack(C19_R2, EUR19), {"Bastian Winkelhaus"}, {"Quirin Fürgut"})}

== Matches ==

Each pairing was a two-game match (one game each side of the Force). The team that won the pairing earned one point. The first-post scoreboard on 20 January 2020 is Europe 4, USA 7.<ref name="score" /> Game-level notes below are from that post; match winners are listed only when the post names them (or records a concession of game 2). Splits are listed as splits.

=== Round 1 ===

Pairings as posted 26 November 2019.<ref name="r1">https://forum.starwarsccg.org/viewtopic.php?t=74065</ref> Window 3–15 December 2019.

{r1_matches}

=== Round 2 ===

Pairings as posted 1 January 2020.<ref name="r2">https://forum.starwarsccg.org/viewtopic.php?t=74291</ref> Window 7–20 January 2020.

{r2_matches}

== See also ==

* [[Team USA]] · [[Team Europe]]
* [[2021 Outrider Cup]] · [[2023 Outrider Cup III]] · [[2026 Outrider Cup IV]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2019-outrider-cup/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2019-outrider-cup/ 2019 Outrider Cup], starwarsccg.org
* [https://forum.starwarsccg.org/viewforum.php?f=1168 Forum], f=1168
* [https://forum.starwarsccg.org/viewtopic.php?t=73616 Information thread], t=73616
* [https://forum.starwarsccg.org/viewtopic.php?t=74099 Matches and Results], t=74099
* [https://forum.starwarsccg.org/viewtopic.php?t=74436 Congratulations Team USA], t=74436
* [https://forum.starwarsccg.org/viewtopic.php?t=73620 Team USA roster thread], t=73620
* [https://forum.starwarsccg.org/viewtopic.php?t=73630 Team Europe roster thread], t=73630

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2019]]
"""
    path = PAGES / "2019_Outrider_Cup.wiki"
    path.write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return "2019 Outrider Cup"


def d21(stage: str, player: str, side: str, slug: str, label: str) -> tuple[str, str]:
    return (f"2021 Outrider Cup {stage} {player} {side} {slug}", label)


C21_USA = {
    "Joe Olson": (d21("Team USA", "Joe Olson", "DS", "Ralltiir Operations (V)", "Ralltiir Operations (V)"), d21("Team USA", "Joe Olson", "LS", "Communing", "Communing")),
    "Matthew Harrison-Trainor": (d21("Team USA", "Matthew Harrison-Trainor", "DS", "Carbon Chamber Testing", "Carbon Chamber Testing"), d21("Team USA", "Matthew Harrison-Trainor", "LS", "Old Allies", "Old Allies")),
    "Hayes Hunter": (d21("Team USA", "Hayes Hunter", "DS", "Hunt Down And Destroy The Jedi (V)", "Hunt Down And Destroy The Jedi (V)"), d21("Team USA", "Hayes Hunter", "LS", "Let The Wookiee Win (V)", "Let The Wookiee Win (V)")),
    "Paul Myers": (d21("Team USA", "Paul Myers", "DS", "This Deal Is Getting Worse All The Time", "This Deal Is Getting Worse All The Time"), d21("Team USA", "Paul Myers", "LS", "Diplomatic Mission To Alderaan", "Diplomatic Mission To Alderaan")),
    "Justin Desai": (d21("Team USA", "Justin Desai", "DS", "Bring Him Before Me", "Bring Him Before Me"), d21("Team USA", "Justin Desai", "LS", "The Galaxy May Need A Legend", "The Galaxy May Need A Legend")),
    "Jared Napolitano": (d21("Team USA", "Jared Napolitano", "DS", "Agents Of Black Sun", "Agents Of Black Sun"), d21("Team USA", "Jared Napolitano", "LS", "Rendezvous Point On Tatooine (V)", "Rendezvous Point On Tatooine (V)")),
}
C21_EUR = {
    "Bastian Winkelhaus": (d21("Team Europe", "Bastian Winkelhaus", "DS", "Shadow Collective", "Shadow Collective"), d21("Team Europe", "Bastian Winkelhaus", "LS", "The Galaxy May Need A Legend", "The Galaxy May Need A Legend")),
    "Justin Branch": (d21("Team Europe", "Justin Branch", "DS", "ISB Operations", "ISB Operations"), d21("Team Europe", "Justin Branch", "LS", "He Is The Chosen One", "He Is The Chosen One")),
    "Quirin Fürgut": (d21("Team Europe", "Quirin Fürgut", "DS", "Agents Of Black Sun", "Agents Of Black Sun"), d21("Team Europe", "Quirin Fürgut", "LS", "Communing", "Communing")),
    "Timo Dusel": (d21("Team Europe", "Timo Dusel", "DS", "Endor Operations", "Endor Operations"), d21("Team Europe", "Timo Dusel", "LS", "Old Allies", "Old Allies")),
    "Ziemowit Skwara": (d21("Team Europe", "Ziemowit Skwara", "DS", "Ralltiir Operations (V)", "Ralltiir Operations (V)"), d21("Team Europe", "Ziemowit Skwara", "LS", "Quiet Mining Colony", "Quiet Mining Colony")),
    "Miguel Tarin": (d21("Team Europe", "Miguel Tarin", "DS", "I Want That Map", "I Want That Map"), d21("Team Europe", "Miguel Tarin", "LS", "Let The Wookiee Win (V)", "Let The Wookiee Win (V)")),
}
C21_TB = {
    "Bastian Winkelhaus": (d21("Tiebreaker", "Bastian Winkelhaus", "DS", "ISB Operations", "ISB Operations"), d21("Tiebreaker", "Bastian Winkelhaus", "LS", "Quiet Mining Colony", "Quiet Mining Colony")),
    "Joe Olson": (d21("Tiebreaker", "Joe Olson", "DS", "Carbon Chamber Testing", "Carbon Chamber Testing"), d21("Tiebreaker", "Joe Olson", "LS", "Let The Wookiee Win (V)", "Let The Wookiee Win (V)")),
}
USA21 = ["Joe Olson", "Justin Desai", "Matthew Harrison-Trainor", "Hayes Hunter", "Paul Myers", "Jared Napolitano"]
EUR21 = ["Bastian Winkelhaus", "Justin Branch", "Timo Dusel", "Quirin Fürgut", "Ziemowit Skwara", "Miguel Tarin"]


def write_2021() -> str:
    known = table(
        ["Game", "Dark", "Light", "Result", "Video"],
        [
            [
                "8 (Europe 5–2 entering)",
                "[[Matthew Harrison-Trainor]] ([[Carbon Chamber Testing]])",
                "[[Quirin Fürgut]] ([[Communing]])",
                "streamed; wrap does not name this game's winner",
                yt("G_RCjcBxt-0", "stream"),
            ],
            [
                "Tiebreaker (26 January 2022)",
                "[[Joe Olson]] ([[Carbon Chamber Testing]] / Let The Wookiee Win (V) Dwell)",
                "[[Bastian Winkelhaus]] ([[Quiet Mining Colony]] / [[ISB Operations]])",
                "Winkelhaus defeated Olson",
                yt("K7PIzyidp7A", "tiebreaker"),
            ],
        ],
    )
    body = f"""'''2021 Outrider Cup''' (Outrider Cup II) was the Players Committee biennial Europe versus United States team event on GEMP, November 2021 – 26 January 2022. '''[[Team Europe]]''' defeated [[Team USA]] in a captains' tiebreaker after the 12 regulation games finished 6–6.<ref name="wrap">https://www.starwarsccg.org/team-europe-wins-the-2021-outrider-cup/</ref>

On 26 January 2022 Europe's captain [[Bastian Winkelhaus]] ([[Quiet Mining Colony]] / [[ISB Operations]]) defeated USA's captain [[Joe Olson]] ([[Carbon Chamber Testing]] / [[Let The Wookiee Win (V)]]) in that tiebreaker. Team USA had stormed back from a 4–1 deficit to force the extra match. Olson and [[Justin Desai]] went 2–0 in their two match-ups; Winkelhaus was the lone 2–0 for Team Europe. Dark Side finished 8–4 across the 12 regulation games.<ref name="wrap" />

[[Jared Napolitano]] was tournament director, with [[Bill Kafer]] and [[Dan Tartaglione]] assisting where there was a conflict of interest. Gogolen's 2019 format carried over: six players a side from 2020–2021 Player of the Year points plus captain's picks, and no two teammates on the same objective.

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' GEMP (teams)
* '''Dates:''' November 2021 – 26 January 2022
* '''Winner:''' [[Team Europe]] (6–6, then tiebreaker)
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YR1HOXIuvwOCtxCnDopFC9T YouTube playlist]

== Rosters ==

=== Team Europe ===

Captain [[Bastian Winkelhaus]].

{roster_table(pack(C21_EUR, EUR21), {"Bastian Winkelhaus"})}

=== Team USA ===

Captain [[Joe Olson]].

{roster_table(pack(C21_USA, USA21), {"Joe Olson"})}

=== Tiebreaker ===

{roster_table(pack(C21_TB, ["Bastian Winkelhaus", "Joe Olson"]), {"Bastian Winkelhaus", "Joe Olson"})}

== Matches ==

The wrap names the 6–6 regulation score, the 4–1 Europe lead USA came back from, Olson and Desai at 2–0, Winkelhaus as Europe's only 2–0, and the 26 January 2022 tiebreaker. It does not publish a 12-row pairing table. Individual games are on the PC YouTube playlist; sourced pairings below are those named in the wrap or in a stream title.

{known}

The stream of game 8 (Europe 5–2 at the start) also scheduled Winkelhaus on [[The Galaxy May Need A Legend]] against [[Paul Myers]] as the next match; that pairing is not repeated in the wrap.

== See also ==

* [[Team USA]] · [[Team Europe]]
* [[2019 Outrider Cup]] · [[2023 Outrider Cup III]] · [[2026 Outrider Cup IV]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/outrider-cup-ii/ PC results]
* [https://www.starwarsccg.org/team-europe-wins-the-2021-outrider-cup/ Wrap]

== Sources ==

* [https://www.starwarsccg.org/outrider-cup-ii/ 2021 Outrider Cup], starwarsccg.org
* [https://www.starwarsccg.org/team-europe-wins-the-2021-outrider-cup/ Team Europe Wins the 2021 Outrider Cup]
* [https://www.youtube.com/playlist?list=PLQSFYZX0M9YR1HOXIuvwOCtxCnDopFC9T YouTube playlist]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2021]]
"""
    (PAGES / "2021_Outrider_Cup.wiki").write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return "2021 Outrider Cup"


def d23(player: str, side: str, slug: str, label: str) -> tuple[str, str]:
    return (f"2023 Outrider Cup III {player} {side} {slug}", label)


C23 = {
    "Justin Desai": (d23("Justin Desai", "DS", "ROTS Maul", "Revenge Of The Sith"), d23("Justin Desai", "LS", "HITCO", "He Is The Chosen One")),
    "Brian Fred": (d23("Brian Fred", "DS", "Endor Operations", "Endor Operations"), d23("Brian Fred", "LS", "Diplomatic Mission To Alderaan", "Diplomatic Mission To Alderaan")),
    "Greg Shaw": (d23("Greg Shaw", "DS", "CCT", "Carbon Chamber Testing"), d23("Greg Shaw", "LS", "No Idea", "They Have No Idea We're Coming")),
    "Hayes Hunter": (d23("Hayes", "DS", "SC", "Shadow Collective"), d23("Hayes", "LS", "Clones", "Hunt For The Droid General")),
    "Joe Olson": (d23("Joe Olson", "DS", "AOBS", "Agents Of Black Sun"), d23("Joe Olson", "LS", "QMC", "Quiet Mining Colony")),
    "Mike Kessling": (d23("Mike Kessling", "DS", "ISB", "ISB Operations"), d23("Mike Kessling", "LS", "Yoda Comm", "Communing")),
    "Emil Wallin": (d23("Emil Wallin", "DS", "AOBS", "Agents Of Black Sun"), d23("Emil Wallin", "LS", "Old Allies", "Old Allies")),
    "Cedrik Vanderhaegen": (d23("Cedrik Vanderhaegen", "DS", "HD", "Hunt Down And Destroy The Jedi"), d23("Cedrik Vanderhaegen", "LS", "WHAP", "We Have A Plan")),
    "Justin Branch": (d23("Justin Branch", "DS", "ISB", "ISB Operations"), d23("Justin Branch", "LS", "Anakin", "The Force Is Strong In My Family")),
    "Koen Meijssen": (d23("Koen Meijssen", "DS", "Map", "I Want That Map"), d23("Koen Meijssen", "LS", "Zero Hour", "Zero Hour")),
    "Quirin Fürgut": (d23("Quirin Fürgut", "DS", "EOps", "Endor Operations"), d23("Quirin Fürgut", "LS", "Hitco", "He Is The Chosen One")),
    "Timo Dusel": (d23("Timo Dusel", "DS", "Thrawn", "A Great Tactician Creates Plans"), d23("Timo Dusel", "LS", "Y4O", "Yavin 4 Base Operations")),
}
USA23 = ["Justin Desai", "Hayes Hunter", "Joe Olson", "Mike Kessling", "Brian Fred", "Greg Shaw"]
EUR23 = ["Emil Wallin", "Koen Meijssen", "Timo Dusel", "Quirin Fürgut", "Cedrik Vanderhaegen", "Justin Branch"]


def write_fred_2023_decks() -> list[str]:
    """PC wrap lists; GEMP zip omitted Fred."""
    titles = []
    ds = """== Deck info ==
* '''Player:''' [[Brian Fred]]
* '''Event:''' [[2023 Outrider Cup III]]
* '''Stage:''' Team USA
* '''Format:''' [[Open]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' [[Endor Operations / Imperial Occupation|Endor Operations]]
* '''Source:''' [https://www.starwarsccg.org/2023-outrider-cup-brian-fred-ds-tto/ PC list]

== Decklist ==

{| class="wikitable" style="width:100%;"
|-
| style="width:50%; vertical-align:top;" |
'''Admiral's Order'''
* 2x [[Black Sun Fleet]]

'''Character'''
* 1x [[4-LOM With Concussion Rifle (V)]]
* 1x [[Admiral Motti]]
* 1x [[Admiral Ozzel]]
* 1x [[Ap'lek]]
* 1x [[Baron Soontir Fel]]
* 1x [[Boba Fett (V)]]
* 1x [[Darth Vader (V)]]
* 1x [[Grand Admiral Thrawn (AI) (V)]]
* 2x [[Grand Moff Tarkin (V)]]
* 1x [[Lord Maul With Lightsaber]]
* 1x [[Lord Sidious]]
* 1x [[Moff Jerjerrod]]

'''Effect'''
* 1x [[Combat Response (V)]]
* 1x [[Endor Shield (V)]]
* 1x [[Image Of The Dark Lord (V)]]
* 1x [[Imperial Decree (V)]]
* 1x [[Knowledge And Defense (V)]]
* 1x [[Much Anger In Him]]
* 1x [[No Escape]]
* 2x [[Tarkin's Bounty (V)]]
* 1x [[Tentacle (V)]]
* 1x [[We Shall Double Our Efforts!]]

'''Epic Event'''
* 1x [[That Thing's Operational]]

| style="width:50%; vertical-align:top;" |
'''Interrupt'''
* 2x [[A Dark Time For The Rebellion (V)]]
* 1x [[Always Two There Are]]
* 1x [[Dark Maneuvers]]
* 2x [[Force Push (V)]]
* 2x [[Imperial Command]]
* 1x [[Masterful Move]]
* 1x [[Operational As Planned]]
* 4x [[Short Range Fighters & Watch Your Back!]]
* 1x [[Surface Defense (V)]]
* 1x [[Tarkin's Orders]]
* 1x [[Voyeur]]

'''Location'''
* 1x [[Death Star II]]
* 1x [[Death Star II: Capacitors]]
* 1x [[Death Star II: Coolant Shaft]]
* 1x [[Death Star II: Reactor Core]]
* 1x [[Endor]]
* 1x [[Endor: Bunker]]
* 1x [[Endor: Landing Platform (Docking Bay)]]
* 1x [[Kashyyyk]]
* 1x [[Naboo]]

'''Objective'''
* 1x [[Endor Operations / Imperial Occupation|Endor Operations]]

'''Starship'''
* 1x [[Mara Jade In VT-49 Decimator]]
* 1x [[Maul's Sith Infiltrator]]
* 1x [[Saber 1]]
* 1x [[Slave I, Symbol Of Fear]]
* 1x [[Vader's Personal Shuttle (V)]]
* 1x [[Zuckuss In Mist Hunter]]

|}

== See also ==
* [[2023 Outrider Cup III]]
* [[2023 Outrider Cup III Brian Fred LS Diplomatic Mission To Alderaan]]
* [[List of SWCCG tournaments]]

{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:Dark Side decks]]
[[Category:2023]]
"""
    ls = """== Deck info ==
* '''Player:''' [[Brian Fred]]
* '''Event:''' [[2023 Outrider Cup III]]
* '''Stage:''' Team USA
* '''Format:''' [[Open]]
* '''Side:''' [[Light]]
* '''Starting Card:''' [[Diplomatic Mission To Alderaan / A Weakness Can Be Found|Diplomatic Mission To Alderaan]]
* '''Starting Interrupt:''' [[Heading For The Medical Frigate]]
* '''Source:''' [https://www.starwarsccg.org/2023-outrider-cup-brian-fred-ls-diplo/ PC list]

== Decklist ==

{| class="wikitable" style="width:100%;"
|-
| style="width:50%; vertical-align:top;" |
'''Character'''
* 1x [[Admiral Raddus]]
* 1x [[Ahsoka Tano]]
* 1x [[Bail Organa]]
* 1x [[Captain Hera Syndulla]]
* 1x [[Captain Raymus Antilles]]
* 1x [[Chewbacca, Protector]]
* 1x [[Chirrut Îmwe]]
* 1x [[Commander Narra]]
* 1x [[Commander Vanden Willard (V)]]
* 1x [[General Airen Cracken]]
* 1x [[Han Solo, Optimistic General]]
* 1x [[Jyn Erso]]
* 1x [[Lando Calrissian, Scoundrel]]
* 1x [[Leia Organa (V)]]
* 2x [[Luke Skywalker, Rebel Scout (V)]]
* 1x [[Obi-Wan Kenobi (V)]]
* 2x [[Owen Lars & Beru Lars]]
* 1x [[R2-D2 & C-3PO]]
* 1x [[Rey]]
* 1x [[Senator Mon Mothma]]

'''Effect'''
* 1x [[Anger, Fear, Aggression (V)]]
* 1x [[I Must Be Allowed To Speak (V)]]
* 1x [[Stolen Data Tapes]]
* 1x [[Strike Planning (V)]]
* 1x [[Wokling (V)]]

| style="width:50%; vertical-align:top;" |
'''Interrupt'''
* 2x [[Antilles Maneuver (V)]]
* 2x [[Careful Planning]]
* 2x [[Escape Pod & We're Doomed]]
* 1x [[Fly Casual]]
* 1x [[Heading For The Medical Frigate]]
* 2x [[Houjix]]
* 1x [[It's A Hit!]]
* 2x [[Might Of The Republic]]
* 2x [[Narrow Escape]]
* 3x [[Old Ben]]
* 1x [[Quite A Mercenary (V)]]
* 3x [[Rebel Leadership (V)]]

'''Location'''
* 1x [[Alderaan]]
* 1x [[Chandrila]]
* 1x [[Jabba's Palace: Antechamber]]
* 1x [[Jabba's Palace: Entrance Cavern]]
* 1x [[Tatooine]]
* 1x [[Tatooine: Dune Sea]]
* 1x [[Tatooine: Lars' Moisture Farm (V)]]

'''Objective'''
* 1x [[Diplomatic Mission To Alderaan / A Weakness Can Be Found|Diplomatic Mission To Alderaan]]

'''Starship'''
* 1x [[Corellian Corvette]]
* 1x [[Tantive IV (V)]]
* 1x [[Tydirium (V)]]

|}

== See also ==
* [[2023 Outrider Cup III]]
* [[2023 Outrider Cup III Brian Fred DS Endor Operations]]
* [[List of SWCCG tournaments]]

{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:Light Side decks]]
[[Category:2023]]
"""
    mapping = [
        ("2023 Outrider Cup III Brian Fred DS Endor Operations", "2023_Outrider_Cup_III_Brian_Fred_DS_Endor_Operations.wiki", ds),
        ("2023 Outrider Cup III Brian Fred LS Diplomatic Mission To Alderaan", "2023_Outrider_Cup_III_Brian_Fred_LS_Diplomatic_Mission_To_Alderaan.wiki", ls),
    ]
    for title, fname, body in mapping:
        (PAGES / fname).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return [title for title, _fname, _body in mapping]


def write_2023() -> str:
    matches = table(
        ["#", "Winner", "Defeated", "Score after", "Video"],
        [
            ["1", "[[Joe Olson]] (Agents Of Black Sun)", "[[Timo Dusel]] (Yavin 4 Base Operations)", "USA 1–0", yt("Kp74Cpcis8M", "Match 1")],
            ["2", "[[Koen Meijssen]] (Zero Hour)", "[[Hayes Hunter]] (Shadow Collective)", "USA 1–1", yt("afj2nAdrNYw", "Match 2")],
            ["3", "[[Justin Desai]] (He Is The Chosen One)", "[[Cedrik Vanderhaegen]] (Hunt Down And Destroy The Jedi)", "USA 2–1", yt("hEudc6ZXJmg", "Match 3")],
            ["4", "[[Greg Shaw]] (They Have No Idea We're Coming)", "[[Timo Dusel]] (A Great Tactician Creates Plans)", "USA 3–1", yt("CZHCcUAtvNk", "Match 4")],
            ["5", "[[Quirin Fürgut]] (He Is The Chosen One)", "[[Mike Kessling]] (ISB Operations)", "USA 3–2", yt("DZXrXrbDqFA", "Match 5")],
            ["6", "[[Brian Fred]] (Diplomatic Mission To Alderaan)", "[[Quirin Fürgut]] (Endor Operations)", "USA 4–2", yt("PCSZ23SYVFU", "Match 6")],
            ["7", "[[Joe Olson]] (Quiet Mining Colony)", "[[Justin Branch]] (ISB Operations)", "USA 5–2", yt("bkjv8uImTcQ", "Match 7")],
            ["8", "[[Koen Meijssen]] (I Want That Map)", "[[Mike Kessling]] (Communing)", "USA 5–3", yt("D-CqjIC7Wq4", "Match 8")],
            ["9", "[[Cedrik Vanderhaegen]] (We Have A Plan)", "[[Greg Shaw]] (Carbon Chamber Testing)", "USA 5–4", "—"],
            ["10", "[[Emil Wallin]] (Old Allies)", "[[Justin Desai]] (Revenge Of The Sith)", "5–5", yt("R7Wks5qqua4", "Match 10")],
            ["11", "[[Brian Fred]] (Endor Operations)", "[[Justin Branch]] (The Force Is Strong In My Family)", "USA 6–5", yt("xR72a7lhST8", "Match 11")],
            ["12", "[[Hayes Hunter]] (Hunt For The Droid General)", "[[Emil Wallin]] (Agents Of Black Sun)", "USA 7–5", yt("JIElEdC5hvE", "Match 12")],
        ],
    )
    body = f"""'''2023 Outrider Cup III''' was the Players Committee biennial Europe versus United States team event on GEMP, 16–28 January 2024. '''[[Team USA]]''' defeated [[Team Europe]] 7–5.<ref name="wrap">https://www.starwarsccg.org/outrider-cup-iii-wrap-up-victory-for-team-usa/</ref><ref name="pc">https://www.starwarsccg.org/2023-11-outrider-cup-iii/</ref>

The wrap is titled ''Outrider Cup III Wrap-up: Victory for Team USA''. The PC results page publishes the same squad as '''Team North America'''. USA jumped to 5–2; Europe tied the series at 5–5; [[Brian Fred]] (Endor Operations) then defeated [[Justin Branch]], and [[Hayes Hunter]] (Hunt For The Droid General) defeated Europe's captain [[Emil Wallin]] (Agents Of Black Sun) in the twelfth game to take the cup 7–5. Light Side won 9 of the 12 games. [[Chris Schoenthal]] was tournament director; [[Dan Tartaglione]] led streaming.<ref name="wrap" />

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' GEMP (teams)
* '''Dates:''' 16–28 January 2024
* '''Winner:''' [[Team USA]] (7–5)
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?p=1420092 forum]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YSrrTqd4wsG-XI5bjt0TnLO YouTube playlist]

== Rosters ==

=== Team USA ===

Published as Team North America on the PC results page. Captain [[Justin Desai]]. Captain's pick: [[Greg Shaw]].

{roster_table(pack(C23, USA23), {"Justin Desai"}, {"Greg Shaw"})}

=== Team Europe ===

Captain [[Emil Wallin]]. Captain's pick: [[Justin Branch]].

{roster_table(pack(C23, EUR23), {"Emil Wallin"}, {"Justin Branch"})}

== Matches ==

Twelve single games (each player one Dark and one Light against different opponents), race to seven. Results as published on the wrap; videos from the PC playlist.<ref name="wrap" />

{matches}

== See also ==

* [[Team USA]] · [[Team Europe]]
* [[2019 Outrider Cup]] · [[2021 Outrider Cup]] · [[2026 Outrider Cup IV]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2023-11-outrider-cup-iii/ PC results]
* [https://www.starwarsccg.org/outrider-cup-iii-wrap-up-victory-for-team-usa/ Wrap]

== Sources ==

* [https://www.starwarsccg.org/2023-11-outrider-cup-iii/ 2023-11 Outrider Cup III], starwarsccg.org
* [https://www.starwarsccg.org/outrider-cup-iii-wrap-up-victory-for-team-usa/ Outrider Cup III Wrap-up: Victory for Team USA]
* [https://www.starwarsccg.org/2023-outrider-cup-brian-fred-ds-tto/ Brian Fred Dark], starwarsccg.org
* [https://www.starwarsccg.org/2023-outrider-cup-brian-fred-ls-diplo/ Brian Fred Light], starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?p=1420092 GEMP Importable Decklists]
* [https://www.youtube.com/playlist?list=PLQSFYZX0M9YSrrTqd4wsG-XI5bjt0TnLO YouTube playlist]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2023]]
"""
    (PAGES / "2023_Outrider_Cup_III.wiki").write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return "2023 Outrider Cup III"


def d26(player: str, side: str, slug: str, label: str) -> tuple[str, str]:
    return (f"2026 Outrider Cup IV {player} {side} {slug}", label)


C26 = {
    "Emil Wallin": (d26("Emil Wallin", "DS", "EOps", "Endor Operations"), d26("Emil Wallin", "LS", "Old Allies", "Old Allies")),
    "Casper Jørgensen": (d26("Casper Jørgensen", "DS", "SC", "Shadow Collective"), d26("Casper Jørgensen", "LS", "No Idea", "They Have No Idea We're Coming")),
    "Cedrik Vanderhaegen": (d26("Cedrik Vanderhaegen", "DS", "HDv", "Hunt Down And Destroy The Jedi (V)"), d26("Cedrik Vanderhaegen", "LS", "Rey Saga", "The Force Is Strong In My Family")),
    "Jonas Hagen Nørregaard": (d26("Jonas Hagen Nørregaard", "DS", "Hoth CPv", "Combat Readiness (V)"), d26("Jonas Hagen Nørregaard", "LS", "WHAP", "We Have A Plan")),
    "Patrik Csapi": (d26("Patrik Csapi", "DS", "Walkers", "The Shield Will Be Down in Moments"), d26("Patrik Csapi", "LS", "Diplo", "Diplomatic Mission To Alderaan")),
    "Timo Dusel": (d26("Timo Dusel", "DS", "Thrawn", "A Great Tactician Creates Plans"), d26("Timo Dusel", "LS", "RST", "Rebel Strike Team")),
    "Joe Olson": (d26("Joe Olson", "DS", "EOps", "Endor Operations"), d26("Joe Olson", "LS", "WYS", "Watch Your Step")),
    "Brian Fred": (d26("Brian Fred", "DS", "Invasion", "Invasion"), d26("Brian Fred", "LS", "WHAP", "We Have A Plan")),
    "Chris Gogolen": (d26("Chris Gogolen", "DS", "Walkers", "The Shield Will Be Down in Moments"), d26("Chris Gogolen", "LS", "Luke Saga", "The Force Is Strong In My Family")),
    "Greg Shaw": (d26("Greg Shaw", "DS", "Senate", "My Lord, Is That Legal?"), d26("Greg Shaw", "LS", "RTPv", "Rescue The Princess (V)")),
    "Hayes Hunter": (d26("Hayes Hunter", "DS", "HDv", "Hunt Down And Destroy The Jedi (V)"), d26("Hayes Hunter", "LS", "Hidden Path", "The Hidden Path")),
    "Sam Tashima": (d26("Sam Tashima", "DS", "SC", "Shadow Collective"), d26("Sam Tashima", "LS", "QMC", "Quiet Mining Colony")),
}
USA26 = ["Joe Olson", "Brian Fred", "Chris Gogolen", "Greg Shaw", "Hayes Hunter", "Sam Tashima"]
EUR26 = ["Emil Wallin", "Casper Jørgensen", "Cedrik Vanderhaegen", "Jonas Hagen Nørregaard", "Patrik Csapi", "Timo Dusel"]


def write_2026() -> str:
    matches = table(
        ["#", "Winner", "Defeated", "Score after", "Video"],
        [
            ["1", "[[Brian Fred]] (We Have A Plan)", "[[Timo Dusel]] (A Great Tactician Creates Plans)", "USA 1–0", yt("AQv7nwrrMfk", "stream")],
            ["2", "[[Chris Gogolen]] (The Shield Will Be Down in Moments)", "[[Timo Dusel]] (Rebel Strike Team)", "USA 2–0", "—"],
            ["3", "[[Sam Tashima]] (Shadow Collective)", "[[Cedrik Vanderhaegen]] (The Force Is Strong In My Family)", "USA 3–0", yt("khgMi_K01tw", "stream")],
            ["4", "[[Joe Olson]] (Endor Operations)", "[[Patrik Csapi]] (Diplomatic Mission To Alderaan)", "USA 4–0", yt("peWq9HiAdbM", "stream")],
            ["5", "[[Jonas Hagen Nørregaard]] (We Have A Plan)", "[[Brian Fred]] (Invasion)", "USA 4–1", yt("eHxXe52lIck", "stream")],
            ["6", "[[Joe Olson]] (Watch Your Step)", "[[Casper Jørgensen]] (Shadow Collective)", "USA 5–1", yt("APwkBSbux6o", "stream")],
            ["7", "[[Patrik Csapi]] (The Shield Will Be Down in Moments)", "[[Chris Gogolen]] (The Force Is Strong In My Family)", "USA 5–2", yt("TLE1pihXt5Y", "stream")],
            ["8", "[[Sam Tashima]] (Quiet Mining Colony)", "[[Emil Wallin]] (Endor Operations)", "USA 6–2", yt("8KR2B4Nq7T4", "stream")],
            ["9", "[[Cedrik Vanderhaegen]] (Hunt Down And Destroy The Jedi (V))", "[[Greg Shaw]] (Rescue The Princess (V))", "USA 6–3", yt("z6UspCGLxGw", "stream")],
            ["10", "[[Hayes Hunter]] (Hunt Down And Destroy The Jedi (V))", "[[Emil Wallin]] (Old Allies)", "USA 7–3", yt("CdDxhOMm08g", "stream")],
            ["—", "[[Jonas Hagen Nørregaard]] (Combat Readiness (V)) vs [[Hayes Hunter]] (The Hidden Path)", "pairing posted; winner not on the first-post scoreboard", "—", yt("fAovLhw4U5g", "stream")],
            ["—", "[[Greg Shaw]] (My Lord, Is That Legal?) vs [[Casper Jørgensen]] (They Have No Idea We're Coming)", "pairing posted; winner not on the first-post scoreboard", "—", yt("f393hAQVtaE", "stream")],
        ],
    )
    body = f"""'''2026 Outrider Cup IV''' was the Players Committee biennial Europe versus United States team event on GEMP, 13 January – 4 February 2026. '''[[Team USA]]''' defeated [[Team Europe]] 7–3 on the first-post scoreboard.<ref name="board">https://forum.starwarsccg.org/viewtopic.php?t=86388</ref><ref name="pc">https://www.starwarsccg.org/2026-02-outrider-cup-iv/</ref>

The information thread frames the sides as North America and Europe; the pairings post lists '''United States''' and Europe; the PC results page lists '''Team USA''' and Team Europe; the live scoreboard counts Team North America versus Team Europe. This wiki uses '''Team USA''' as the winner label (same as 2019 and the 2023 wrap title) and the published six-player rosters.<ref name="info">https://forum.starwarsccg.org/viewtopic.php?t=86302</ref><ref name="pair">https://forum.starwarsccg.org/viewtopic.php?t=86377</ref>

[[Joe Olson]] captained Team USA; [[Emil Wallin]] captained Team Europe. Each player submitted one Dark and one Light list. Pairings were drawn so nobody played the same opponent twice. [[Hayes Hunter]] (Hunt Down And Destroy The Jedi (V)) defeated Wallin (Old Allies) to make the posted score 7–3. Two remaining posted pairings have YouTube streams; the first-post scoreboard does not name those winners.

== Format ==

* '''Environment:''' [[Open]]
* '''Platform:''' GEMP (teams)
* '''Dates:''' 13 January – 4 February 2026
* '''Winner:''' [[Team USA]] (7–3 on the posted scoreboard)
* '''Forum:''' [https://forum.starwarsccg.org/viewforum.php?f=1588 Outrider Cup IV Forum]
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?t=86478 forum t=86478]
* '''Video:''' [https://www.youtube.com/playlist?list=PLQSFYZX0M9YTcnh-wm5_BUu8YGPYwH-Ut YouTube playlist]

== Rosters ==

=== Team USA ===

Captain [[Joe Olson]].

{roster_table(pack(C26, USA26), {"Joe Olson"})}

=== Team Europe ===

Captain [[Emil Wallin]].

{roster_table(pack(C26, EUR26), {"Emil Wallin"})}

== Matches ==

First player in each pairing played Dark Side.<ref name="pair" /> Results 1–10 are the first-post scoreboard; the last two rows are posted pairings with streams whose winners that post does not name.<ref name="board" />

{matches}

== See also ==

* [[Team USA]] · [[Team Europe]]
* [[2019 Outrider Cup]] · [[2021 Outrider Cup]] · [[2023 Outrider Cup III]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2026-02-outrider-cup-iv/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2026-02-outrider-cup-iv/ 2026-02 Outrider Cup IV], starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?t=86302 Information thread], t=86302
* [https://forum.starwarsccg.org/viewtopic.php?t=86377 Pairings], t=86377
* [https://forum.starwarsccg.org/viewtopic.php?t=86388 Schedule and Scoreboard], t=86388
* [https://forum.starwarsccg.org/viewtopic.php?t=86478 Decklist files], t=86478
* [https://forum.starwarsccg.org/viewforum.php?f=1588 Forum], f=1588
* [https://www.youtube.com/playlist?list=PLQSFYZX0M9YTcnh-wm5_BUu8YGPYwH-Ut YouTube playlist]

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""
    (PAGES / "2026_Outrider_Cup_IV.wiki").write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return "2026 Outrider Cup IV"


def prow(date: str, event: str, note: str, finish: str, ds: tuple[str, str], ls: tuple[str, str]) -> str:
    return (
        f"|- \n| {date} || [[{event}]] ({note}) || [[Open]] || {finish} || "
        f"{cell(ds[0], ds[1])} || {cell(ls[0], ls[1])}"
    )


def player_rows() -> dict[str, list[str]]:
    rows: dict[str, list[str]] = defaultdict(list)
    # 2026
    for n in USA26:
        ds, ls = C26[n]
        rows[n].append(prow("13 January – 4 February 2026", "2026 Outrider Cup IV", "Team USA", "1", ds, ls))
    for n in EUR26:
        ds, ls = C26[n]
        rows[n].append(prow("13 January – 4 February 2026", "2026 Outrider Cup IV", "Team Europe", "2", ds, ls))
    # 2023
    for n in USA23:
        ds, ls = C23[n]
        rows[n].append(prow("16–28 January 2024", "2023 Outrider Cup III", "Team USA", "1", ds, ls))
    for n in EUR23:
        ds, ls = C23[n]
        rows[n].append(prow("16–28 January 2024", "2023 Outrider Cup III", "Team Europe", "2", ds, ls))
    # 2021 TB then team
    ds, ls = C21_TB["Bastian Winkelhaus"]
    rows["Bastian Winkelhaus"].append(prow("26 January 2022", "2021 Outrider Cup", "Tiebreaker", "1", ds, ls))
    ds, ls = C21_TB["Joe Olson"]
    rows["Joe Olson"].append(prow("26 January 2022", "2021 Outrider Cup", "Tiebreaker", "2", ds, ls))
    for n in EUR21:
        ds, ls = C21_EUR[n]
        rows[n].append(prow("November 2021 – January 2022", "2021 Outrider Cup", "Team Europe", "1", ds, ls))
    for n in USA21:
        ds, ls = C21_USA[n]
        rows[n].append(prow("November 2021 – January 2022", "2021 Outrider Cup", "Team USA", "2", ds, ls))
    # 2019 R2 then R1
    for n in USA19:
        ds, ls = C19_R2[n]
        rows[n].append(prow("7–20 January 2020", "2019 Outrider Cup", "Team USA, Round 2", "1", ds, ls))
        ds, ls = C19_R1[n]
        rows[n].append(prow("3–15 December 2019", "2019 Outrider Cup", "Team USA, Round 1", "1", ds, ls))
    for n in EUR19:
        ds, ls = C19_R2[n]
        rows[n].append(prow("7–20 January 2020", "2019 Outrider Cup", "Team Europe, Round 2", "2", ds, ls))
        ds, ls = C19_R1[n]
        rows[n].append(prow("3–15 December 2019", "2019 Outrider Cup", "Team Europe, Round 1", "2", ds, ls))
    return rows


EVENTS_RE = (
    r"\[\[(?:2019 Outrider Cup|2021 Outrider Cup|2023 Outrider Cup III|2026 Outrider Cup IV)\]\]"
)

SRC = {
    "2019 Outrider Cup": "https://www.starwarsccg.org/2019-outrider-cup/",
    "2021 Outrider Cup": "https://www.starwarsccg.org/team-europe-wins-the-2021-outrider-cup/",
    "2023 Outrider Cup III": "https://www.starwarsccg.org/outrider-cup-iii-wrap-up-victory-for-team-usa/",
    "2026 Outrider Cup IV": "https://www.starwarsccg.org/2026-02-outrider-cup-iv/",
}


def resolve_player(player: str) -> Path | None:
    stub = STUBS / (player.replace(" ", "_") + ".wiki")
    bio = PAGES / (player.replace(" ", "_") + ".wiki")
    if bio.exists() and is_bio(bio.read_text(encoding="utf-8", errors="replace")):
        return bio
    if stub.exists():
        return stub
    if bio.exists():
        return bio
    return None


def strip_outrider_rows(text: str) -> str:
    return re.sub(rf"\|-\s*\n\| [^\n]*{EVENTS_RE}[^\n]*\n", "", text)


def played_events(rows: list[str]) -> list[str]:
    out = []
    for et in SRC:
        if any(f"[[{et}]]" in row for row in rows) and et not in out:
            out.append(et)
    return out


def patch_player(player: str, new_rows: list[str]) -> tuple[str, str]:
    path = resolve_player(player)
    if path is None:
        upsert_stub(player, new_rows, "2026 Outrider Cup IV", SRC["2026 Outrider Cup IV"])
        dest = STUBS / (player.replace(" ", "_") + ".wiki")
        tidy_player_page(dest)
        return player, f"pages/player-stubs/{dest.name}"
    text = strip_outrider_rows(path.read_text(encoding="utf-8"))
    if "|}" in text and "Tournament Results" in text:
        text = text.replace("|}\n", "\n".join(new_rows) + "\n|}\n", 1)
    events = played_events(new_rows)
    for et in events:
        src = SRC[et]
        if f"[[{et}]]" not in text.split("== Tournament Results ==")[0] and "* [[Championships]]" in text:
            text = text.replace("* [[Championships]]", f"* [[{et}]]\n* [[Championships]]", 1)
        extra = f"* [{src} {et}], starwarsccg.org\n"
        if "== Sources ==" in text and src not in text:
            text = text.replace("== Sources ==\n", "== Sources ==\n" + extra, 1)
    path.write_text(text, encoding="utf-8", newline="\n")
    tidy_player_page(path)
    stub = STUBS / (player.replace(" ", "_") + ".wiki")
    if "player-stubs" not in str(path) and stub.exists():
        st = strip_outrider_rows(stub.read_text(encoding="utf-8"))
        stub.write_text(st, encoding="utf-8", newline="\n")
        tidy_player_page(stub)
    if "player-stubs" in str(path):
        rel = f"pages/player-stubs/{path.name}"
    else:
        rel = f"pages/{path.name}"
    return player, rel


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    repls = [
        (
            "| 2026-02 || [[2026 Outrider Cup IV|Outrider Cup IV]] || January–February 2026 || GEMP (teams) || [[Open]] || Team Europe",
            "| 2026-02 || [[2026 Outrider Cup IV|Outrider Cup IV]] || 13 January – 4 February 2026 || GEMP (teams) || [[Open]] || [[Team USA]]",
        ),
        (
            "| 2023-11 || [[2023 Outrider Cup III|Outrider Cup III]] || 16–26 January 2024 || GEMP (teams) || [[Open]] || Team North America",
            "| 2023-11 || [[2023 Outrider Cup III|Outrider Cup III]] || 16–28 January 2024 || GEMP (teams) || [[Open]] || [[Team USA]]",
        ),
        (
            "| 2021-12 || [[2021 Outrider Cup|Outrider Cup]] || November–December 2021 || GEMP (teams) || [[Open]] || —",
            "| 2021-12 || [[2021 Outrider Cup|Outrider Cup]] || November 2021 – 26 January 2022 || GEMP (teams) || [[Open]] || [[Team Europe]]",
        ),
        (
            "| 2019-12 || [[2019 Outrider Cup|Outrider Cup]] || November–December 2019 || GEMP (teams) || [[Open]] || —",
            "| 2019-12 || [[2019 Outrider Cup|Outrider Cup]] || 3 December 2019 – 20 January 2020 || GEMP (teams) || [[Open]] || [[Team USA]]",
        ),
    ]
    for old, new in repls:
        if old not in text:
            print("LISTMISS", old[:80])
        text = text.replace(old, new)
    LIST.write_text(text, encoding="utf-8", newline="\n")


def write_redirects() -> list[tuple[str, str]]:
    mapping = {
        "2019 Outrider Cup I": "2019 Outrider Cup",
        "Outrider Cup II": "2021 Outrider Cup",
        "2021 Outrider Cup II": "2021 Outrider Cup",
        "Outrider Cup III": "2023 Outrider Cup III",
        "Outrider Cup IV": "2026 Outrider Cup IV",
        "Team North America": "Team USA",
    }
    out = []
    for src, dest in mapping.items():
        p = PAGES / wiki_fname(src)
        p.write_text(f"#REDIRECT [[{dest}]]\n", encoding="utf-8", newline="\n")
        out.append((src, f"pages/{p.name}"))
    return out


def main() -> None:
    titles: list[tuple[str, str]] = []
    for fn in (write_2019, write_2021, write_2023, write_2026):
        t = fn()
        titles.append((t, f"pages/{wiki_fname(t)}"))
    for t in write_fred_2023_decks():
        titles.append((t, f"pages/{wiki_fname(t)}"))
    patch_list()
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.extend(write_redirects())
    for player, rows in player_rows().items():
        name, rel = patch_player(player, rows)
        titles.append((name, rel))
    seen = {}
    for t, r in titles:
        seen[t] = r
    TSV.write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8", newline="\n")
    print("titles", len(seen), "->", TSV)


if __name__ == "__main__":
    main()
