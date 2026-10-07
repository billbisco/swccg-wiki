#!/usr/bin/env python3
"""Day 2 Xerox transcription: Matt Sokol.

Source scans: extract/day2/d2p1_p17.png (Light, Yavin 4 Massassi / Restore Freedom)
and extract/day2/d2p1_p18.png (Dark, HD / Cloud City). 2010 form.
(V) follows the sheet checkbox. Dittos expanded.
Day 2 60 is not the Day 3 QMC / Hunt Down Executor list.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Matt Sokol"
USERNAME = ""
FORM = "xerox_2010"
PDF = "2014 Worlds Day 2 Part 1.pdf"

SOKOL_D2_PLAYER = PLAYER
SOKOL_D2_LS_DECK_NAME = "Light"
SOKOL_D2_DS_DECK_NAME = "Dark"


# --- Light: d2p1_p17.png. LIGHT checked. Restore Freedom / Y4. ---

SOKOL_D2_LS_SCAN = "extract/day2/d2p1_p17.png"
SOKOL_D2_LS_PDF_PAGE = 17
SOKOL_D2_LS_SIDE = "Light"
SOKOL_D2_LS_STARTING = n("Restore Freedom To The Galaxy")

SOKOL_D2_LS_RESERVE = [
    n("Yavin 4", True),  # 1
    n("Nar Shaddaa"),  # 2
    n("Tatooine"),  # 3
    n("Yavin 4: Massassi War Room"),  # 4  Yavin 4: War Room
    n("Yavin 4: Massassi Headquarters"),  # 5  HQ
    n("Restore Freedom To The Galaxy"),  # 6
    n("Corran Horn"),  # 7
    n("Wedge Antilles, Red Squadron Leader"),  # 8  Wedge, RSL
    n("Biggs Darklighter", True),  # 9  Biggs
    n("Captain Han Solo"),  # 10
    n("Tycho Celchu"),  # 11
    n("Lieutenant Blount"),  # 12  Lt. Blount
    n("Jek Porkins", True),  # 13  Jek
    n("Keir Santage"),  # 14
    n("Luke Skywalker", True),  # 15
    n("Dash Rendar", True),  # 16
    n("Boushh"),  # 17
    n("Captain Han Solo"),  # 18  Cap Han Solo
    n("Chewbacca", True),  # 19  Chewie
    n("Derek 'Hobbie' Klivian", True),  # 20  Hobbie
    n("Gold Leader In Gold 1", True),  # 21  GL in G1
    n("Red 3", True),  # 22
    n("Red Squadron 4"),  # 23
    n("Outrider"),  # 24
    n("Rogue Squadron X-wing"),  # 25
    n("Red Squadron 7", True),  # 26
    n("Red 6", True),  # 27
    n("Artoo-Detoo In Red 5"),  # 28
    n("Red Squadron 4"),  # 29
    n("Millennium Falcon", True),  # 30  Falcon
    n("Enhanced Proton Torpedoes", True),  # 31
    n("X-wing Laser Cannon"),  # 32
    n("Legendary Starfighter"),  # 33
    n("Haven"),  # 34
    n("S-foils", True),  # 35
    n("Massassi Base Sentry"),  # 36
    n("Imperial Atrocity", True),  # 37
    n("Imperial Atrocity"),  # 38  ditto; (V) empty
    n("Projection Of A Skywalker"),  # 39  POS
    n("Projection Of A Skywalker"),  # 40
    n("Undercover", True),  # 41
    n("Undercover"),  # 42  ditto; (V) empty
    n("Luke, Trust Me"),  # 43
    n("Wokling", True),  # 44
    n("Squadron Assignments"),  # 45  Squad Assignment
    n("All Wings Report In & Darklighter Spin"),  # 46  AWRT & DS
    n("All Wings Report In & Darklighter Spin"),  # 47
    n("All Wings Report In & Darklighter Spin"),  # 48
    n("Let The Wookiee Win", True),  # 49  LTWW
    n("Out Of Commission & Transmission Terminated"),  # 50  OOC & TT
    n("Houjix"),  # 51
    n("Control & Tunnel Vision"),  # 52  Control & TV
    n("Escape Pod", True),  # 53
    n("Antilles Maneuver & Rebel Reinforcements"),  # 54  AM & RR
    n("Rebel Barrier"),  # 55  Barrier
    n("Rebel Barrier"),  # 56
    n("Organized Attack"),  # 57  Org Attack
    n("Organized Attack"),  # 58
    n("Careful Planning", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60  AFA
]

SOKOL_D2_LS_SHIELDS: list[tuple[str | None, bool]] = []
# sheet writes "15 Shields" on line 1; 2–12 blank
SOKOL_D2_LS_ADD: list[tuple[str | None, bool]] = []


# --- Dark: d2p1_p18.png. DARK checked. Hunt Down / Cloud City. ---

SOKOL_D2_DS_SCAN = "extract/day2/d2p1_p18.png"
SOKOL_D2_DS_PDF_PAGE = 18
SOKOL_D2_DS_SIDE = "Dark"
SOKOL_D2_DS_STARTING = n(
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True
)

SOKOL_D2_DS_RESERVE = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),  # 1  HD
    n("Coruscant"),  # 2
    n("Coruscant: Imperial City"),  # 3
    n("Cloud City: Security Tower", True),  # 4  CC: Security Tower
    n("Bespin: Cloud City"),  # 5
    n("Clouds"),  # 6  Bespin Cloud
    n("Bespin"),  # 7
    n("Tibanna Floating Refinery"),  # 8
    n("SFS L-s9.3 Laser Cannons"),  # 9
    n("Saber Squadron TIE"),  # 10
    n("Saber Squadron TIE"),  # 11
    n("Saber Squadron TIE"),  # 12
    n("Saber 1"),  # 13
    n("Obsidian 10", True),  # 14
    n("Saber 4"),  # 15
    n("Rogue Shadow"),  # 16
    n("Darth Vader, Dark Lord Of The Sith"),  # 17  DV, DLOTS
    n("OS-72-10"),  # 18
    n("Jango Fett"),  # 19  Jundo Fett
    n("Juno Eclipse, Black Leader"),  # 20  written Juno Eclipse
    n("Baron Soontir Fel"),  # 21
    n("Saber Squadron Pilot"),  # 22
    n("Saber Squadron Pilot"),  # 23
    n("Saber Squadron Pilot"),  # 24
    n("Arica"),  # 25
    n("Keder The Black"),  # 26
    n("Keder The Black"),  # 27
    n("U-3PO"),  # 28
    n("U-3PO"),  # 29
    n("Imperial Propaganda", True),  # 30
    n("Imperial Propaganda"),  # 31  ditto; (V) empty
    n("Protocol Failure"),  # 32
    n("Lateral Damage"),  # 33
    n("Lateral Damage"),  # 34
    n("Sonic Bombardment", True),  # 35
    n("Sonic Bombardment"),  # 36
    n("Sonic Bombardment"),  # 37
    n("Sonic Bombardment"),  # 38
    n("One Beautiful Thing"),  # 39
    n("One Beautiful Thing"),  # 40
    n("Short Range Fighters & Watch Your Back!"),  # 41  SRF & WYB
    n("Short Range Fighters & Watch Your Back!"),  # 42
    n("Short Range Fighters & Watch Your Back!"),  # 43
    n("All Power To Weapons"),  # 44  APTW
    n("All Power To Weapons"),  # 45
    n("All Power To Weapons"),  # 46
    n("All Power To Weapons"),  # 47
    n("Nevar Yalnal"),  # 48
    n("Nevar Yalnal"),  # 49
    n("Force Push", True),  # 50
    n("Ghhhk"),  # 51
    n("Masterful Move"),  # 52
    n("Abyssin Ornament", True),  # 53
    n("Abyssin Ornament"),  # 54  ditto; (V) empty
    n("A Sith's Plans"),  # 55
    n("I'm Sorry", True),  # 56
    n("Combat Response", True),  # 57
    n("Ni Chuba Na??", True),  # 58
    n("Prepared Defenses"),  # 59
    n("Knowledge And Defense", True),  # 60  K+D
]

SOKOL_D2_DS_SHIELDS: list[tuple[str | None, bool]] = []
# sheet writes "15 Shield" on line 1; 2–12 blank
SOKOL_D2_DS_ADD: list[tuple[str | None, bool]] = []


SOKOL_D2_LS_UNREAD: list[int] = []
SOKOL_D2_DS_UNREAD: list[int] = []
SOKOL_D2_LS_NO_DEST: list[str] = []
SOKOL_D2_DS_NO_DEST: list[str] = []

NOTES = """
Matt Sokol, 2014 Worlds Day 2, 2010 form. Name Sokol.
Light d2p1_p17 (LIGHT checked). Yavin 4 Massassi / Restore Freedom.
Dark d2p1_p18 (DARK checked). HD / Cloud City TIEs.

LS: line 1 Yavin 4 (V) system; objective is line 6 Restore Freedom To The Galaxy.
Line 8 Wedge, RSL. Line 9 Biggs. Line 13 Jek → Jek Porkins (V).
Line 20 Hobbie. Line 21 GL in G1 → Gold Leader In Gold 1 (V).
Line 26 Red Squad 7. Line 30 Falcon → Millennium Falcon (V).
Line 39 POS → Projection Of A Skywalker. Line 45 Squad Assignment → Squadron Assignments.
Line 52 Control & TV → Control & Tunnel Vision.
Shields: "15 Shields" note only; no names.

DS: line 5 Bespin Cloud City → Bespin: Cloud City. Line 6 Bespin Cloud → Clouds.
Line 8 Tibanna Floating Refinery. Line 9 SFS L-s9.3 Laser Cannons.
Lines 10–12 Saber Squadron TIE. Line 13 Saber 1. Line 19 Jango Fett (Jundo).
Line 20 Juno Eclipse → Juno Eclipse, Black Leader.
Line 56 I'm Sorry (V). Line 58 Ni Chuba Na???.
Shields: "15 Shield" note only; no names.
""".strip()


if __name__ == "__main__":
    assert len(SOKOL_D2_LS_RESERVE) == 60, len(SOKOL_D2_LS_RESERVE)
    assert len(SOKOL_D2_DS_RESERVE) == 60, len(SOKOL_D2_DS_RESERVE)
    print("transcribe_sokol_day2.py", PLAYER)
    print("  Light reserve", len(SOKOL_D2_LS_RESERVE), "shields", len(SOKOL_D2_LS_SHIELDS), "unread", SOKOL_D2_LS_UNREAD, "no_dest", SOKOL_D2_LS_NO_DEST)
    print("  Dark reserve", len(SOKOL_D2_DS_RESERVE), "shields", len(SOKOL_D2_DS_SHIELDS), "unread", SOKOL_D2_DS_UNREAD, "no_dest", SOKOL_D2_DS_NO_DEST)
