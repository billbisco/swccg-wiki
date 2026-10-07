#!/usr/bin/env python3
"""Day 2 Xerox transcription: Mike Stirling Dark (p25) + Light (p26).

Source scans: extract/day2/d2p1_p25.png (Dark, My Lord Is That Legal / Senate)
and extract/day2/d2p1_p26.png (Light, Hoth Echo Base / Main Power Generators).
2013 form. Facing-page dest: p26 Name blank Light between Jake from State
Farm (p23–p24) and Mitch Nieland (Part 2 p01); p25 named Mike Stirling.
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


# --- Dark: d2p1_p25.png. Light/Dark unchecked. Mike Stirling. ---

DS_PLAYER = "Mike Stirling"
DS_USERNAME = ""
DS_DECK_NAME = ""
DS_SIDE = "Dark"
DS_FORM = "xerox_2013"
DS_SCAN = "extract/day2/d2p1_p25.png"
DS_PDF = "2014 Worlds Day 2 Part 1.pdf"
DS_PDF_PAGE = 25
DS_STARTING = ("My Lord, Is That Legal? / I Will Make It Legal", False)

DS_RESERVE = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),  # 1
    n("Prepared Defenses"),  # 2
    n("Coruscant"),  # 3
    n("Coruscant: Galactic Senate"),  # 4  ditto Senate
    n("Begin Landing Your Troops"),  # 5
    n("The Phantom Menace"),  # 6
    n("You Cannot Hide Forever & Mobilization Points"),  # 7  can't hide / Mobilization Points
    n("Rune Haako"),  # 8  Run of Hasko
    n("Darth Vader"),  # 9
    n("Darth Vader, Dark Lord Of The Sith"),  # 10  Vader The Black / Dark Lord
    n("Grand Moff Tarkin"),  # 11
    n("I Have You Now"),  # 12
    n("Mara Jade, The Emperor's Hand"),  # 13  Mara Jade - Emp's Hand
    n("Squabbling Delegates"),  # 14
    n("Squabbling Delegates"),  # 15
    n("Edcel Bar Gane"),  # 16
    n("Edcel Bar Gane"),  # 17
    n("Naboo"),  # 18
    n("Naboo: Theed Palace Docking Bay"),  # 19  ditto Docking Bay
    n("Naboo: Theed Palace Throne Room"),  # 20  ditto Throne Room
    n("Maul's Double-Bladed Lightsaber"),  # 21
    n("Darth Maul, Young Apprentice"),  # 22
    n("Darth Maul, Young Apprentice"),  # 23
    n("Mara Jade's Lightsaber"),  # 24  MJ's Lightsaber
    n("Lord Vader"),  # 25
    n("Prince Xizor"),  # 26
    n("Rendili"),  # 27
    n("Guri"),  # 28
    n("Vader's Lightsaber"),  # 29
    n("Executor: Docking Bay"),  # 30
    n("P-60"),  # 31
    n("P-59"),  # 32
    n("Baskol Yeelrm"),  # 33
    n("Aks Moe"),  # 34
    n("Neimoidian Pilot"),  # 35
    n("Neimoidian Pilot"),  # 36
    n("Orn Free Taa"),  # 37
    n("Tikkes"),  # 38
    n("Coruscant: Docking Bay"),  # 39  Coruscant: DB
    n("Yeb Yeb Adem'thorn"),  # 40
    n("The Point Is Conceded"),  # 41
    n("The Point Is Conceded"),  # 42
    n("Maul's Double-Bladed Lightsaber"),  # 43  Maul's Lightsaber
    n("Sly Moore"),  # 44  SY Lunch
    n("Toonbuck Toora"),  # 45
    n("Trade Federation Droid Control Ship"),  # 46
    n("Trade Federation Droid Control Ship"),  # 47
    n("Droid Starfighter"),  # 48
    n("Droid Starfighter"),  # 49
    n("Lott Dod"),  # 50
    n("Nute Gunray"),  # 51
    n("Daultay Dofine"),  # 52
    n("Vader's Lightsaber"),  # 53
    n("We Only Want To Arrest Them"),  # 54  We only want to arrest
    n("Passel Argente"),  # 55
    n("Our Blockade Is Perfectly Legal"),  # 56
    n("Surprise"),  # 57  We Have A Surprise
    n("Accept This Trade Federation"),  # 58
    n("This Is Outrageous!"),  # 59
    n("Knowledge And Defense"),  # 60
]

DS_SHIELDS = [
    n("Firepower", True),  # 1
    n("Weapon Of A Sith"),  # 2
    n("Secret Plans"),  # 3
    n("Fanfare", True),  # 4
    # 5 Come Here You Big Coward crossed; no replacement
    # 6 We'll Let Fate-a Decide, Huh? crossed; no replacement
    n("Abyss", True),  # 7
    n("I Find Your Lack Of Faith Disturbing"),  # 8
    n("Battle Order"),  # 9
    n("Oppressive Enforcement"),  # 10
    n("A Useless Gesture"),  # 11
    n("Come Here You Big Coward"),  # 12
    n("Allegations Of Corruption"),  # 13
    n("There Is No Try"),  # 14
    # 15 blank
]

DS_ADD: list[tuple[str | None, bool]] = []

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []


# --- Light: d2p1_p26.png. Name/side blank. Hoth Echo Base. ---

LS_PLAYER = "Mike Stirling"
LS_USERNAME = ""
LS_DECK_NAME = ""
LS_SIDE = "Light"
LS_FORM = "xerox_2013"
LS_SCAN = "extract/day2/d2p1_p26.png"
LS_PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 26
LS_STARTING = ("Hoth: Main Power Generators (1st Marker)", False)

LS_RESERVE = [
    n("Hoth"),  # 1  system
    n("Hoth: Main Power Generators (1st Marker)"),  # 2  1st Marker
    n("Hoth: North Ridge (4th Marker)"),  # 3  North Ridge
    n("Careful Planning", True),  # 4
    n("A New Secret Base"),  # 5
    n("Mon Calamari Dockyards", True),  # 6  Mon Calamari Shipyards
    n("Launching The Assault"),  # 7
    n("Hoth: Echo Docking Bay"),  # 8  Hoth: DB
    n("Hoth: Echo Med Lab", True),  # 9
    n("Hoth: Echo Command Center (War Room)"),  # 10  War Room
    n("Hoth: Defensive Perimeter (3rd Marker)"),  # 11  3rd Marker
    n("Hoth: Echo Corridor"),  # 12
    n(None),  # 13  Garrison crossed; Detention remaining — unread
    n("Kashyyyk"),  # 14
    n("Mon Calamari"),  # 15
    n("Anoat"),  # 16
    n("Ralltiir"),  # 17
    n("All Wings Report In & Darklighter Spin"),  # 18
    n("Incom Corporation"),  # 19  Incom Corp.
    n("X-wing Laser Cannon"),  # 20
    n("Docking And Repair Facilities"),  # 21
    n("Bacta Tank"),  # 22
    n("Rebel Fleet"),  # 23
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 24
    n("Houjix & Out Of Nowhere", True),  # 25
    n("Hyper Escape"),  # 26
    n("Hyper Escape"),  # 27
    n("Full Throttle"),  # 28
    n("Organized Attack"),  # 29
    n("All Wings Report In"),  # 30
    n("Han Solo"),  # 31  Hall Okend
    n("Bren Quersey"),  # 32
    n("Lieutenant Lepira"),  # 33
    n("Admiral Ackbar"),  # 34  ADM Ackbar
    n("Commander Luke Skywalker"),  # 35  Cmdr Luke
    n("Commander Wedge Antilles"),  # 36  Cmdr Wedge
    n("Mon Calamari Star Cruiser"),  # 37
    n("Mon Calamari Star Cruiser"),  # 38
    n("Mon Calamari Star Cruiser"),  # 39
    n("Masanya"),  # 40
    n("Spiral"),  # 41
    n("Home One"),  # 42
    n("Han, Chewie, And The Falcon"),  # 43  Han Crosses Falcon; prior name crossed
    n("Liberty"),  # 44
    n("Echo Base Operations"),  # 45
    n("Echo Base Garrison"),  # 46  Echo Base Condition / Garrison
    n("Echo Base Sensors"),  # 47
    n("Zev Senesca"),  # 48
    n("Derek 'Hobbie' Klivian"),  # 49  Hobbie
    n("Corran Horn", True),  # 50
    n("X-wing"),  # 51
    n("X-wing"),  # 52
    n("X-wing"),  # 53
    n("X-wing"),  # 54
    n("X-wing"),  # 55
    n("X-wing"),  # 56
    n("X-wing"),  # 57
    n("Boushh"),  # 58
    n("Combined Fleet Action"),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

LS_SHIELDS = [
    n("Your Insight Serves You Well", True),  # 1
    n("Weapons Display", True),  # 2
    n("Chasm", True),  # 3
    n("Battle Order"),  # 4  as written
    n("Affect Mind", True),  # 5
    n("Wise Advice"),  # 6
    n("A Tragedy Has Occurred"),  # 7
    n("Battle Plan"),  # 8
    n("Planetary Defenses", True),  # 9
    n("Aim High"),  # 10
    n("Ultimatum"),  # 11
    n("He Can Go About His Business", True),  # 12
]

LS_ADD: list[tuple[str | None, bool]] = []

LS_UNREAD = [13]
LS_NO_DEST: list[str] = []

NOTES = """
Mike Stirling Dark d2p1_p25.png (2013 form). Light/Dark unchecked; side from
My Lord, Is That Legal / Senate. Name Mike Stirling. Deck name blank.

Unnamed Light d2p1_p26.png (2013 form). Name/side blank. Hoth Echo Base /
Main Power Generators. Likely pair with p25 Stirling; not Chris Twigg
(his Day 2 LS is Y4 on d2p3_p17).

DS: 7 You Cannot Hide Forever / Mobilization Points combo. 8 Rune Haako.
10 Vader The Black → Darth Vader, Dark Lord Of The Sith (line 9 Premiere
Darth Vader; 25 Lord Vader). 19-20 Naboo: Theed Palace Docking Bay and
Throne Room. 44 SY Lunch → Sly Moore. 54 We only want to arrest as
written. 57 We Have A Surprise → Surprise. 58 Accept This Trade Federation
as written. Shields 5-6 Come Here You Big Coward and We'll Let Fate-a
Decide Huh? crossed with no replacement; omitted. 15 blank omitted.

LS: 2 1st Marker → Hoth: Main Power Generators (1st Marker). 6 Shipyards
→ Mon Calamari Dockyards (V). 13 Garrison crossed, Detention remaining —
unread, not expanded. 31 Hall Okend → Han Solo. 45-47 Echo Base
Operations, Garrison, Sensors. 49 Hobbie → Derek 'Hobbie' Klivian.
""".strip()


def _dump(side: str, reserve, shields, add) -> None:
    rows = []
    for name, v in reserve:
        if name:
            rows.append(f"{side}\t{name}\t{int(v)}")
    for name, v in shields:
        if name:
            rows.append(f"{side}\t{name}\t{int(v)}\tsh")
    for name, v in add:
        if name:
            rows.append(f"{side}\t{name}\t{int(v)}")
    print("\n".join(rows))


if __name__ == "__main__":
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    print(
        "transcribe_mike_stirling.py",
        "DS",
        DS_PLAYER,
        DS_SIDE,
        "reserve",
        len(DS_RESERVE),
        "shields",
        len(DS_SHIELDS),
        "unread",
        DS_UNREAD,
        "no_dest",
        DS_NO_DEST,
    )
    print(
        "transcribe_mike_stirling.py",
        "LS",
        LS_PLAYER,
        LS_SIDE,
        "reserve",
        len(LS_RESERVE),
        "shields",
        len(LS_SHIELDS),
        "unread",
        LS_UNREAD,
        "no_dest",
        LS_NO_DEST,
    )
    _dump("Dark", DS_RESERVE, DS_SHIELDS, DS_ADD)
    _dump("Light", LS_RESERVE, LS_SHIELDS, LS_ADD)
