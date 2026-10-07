#!/usr/bin/env python3
"""Day 2 Xerox transcription: Jake from State Farm.

Source scans: extract/day2/d2p1_p23.png (Light, This deck is your Dos mas)
and extract/day2/d2p1_p24.png (Dark, Senate \"Jake's Senate\"). 2013 form,
green-tinted. PLAYER as written; no legal surname on the sheet.
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Jake from State Farm"
USERNAME = ""

# --- Light: d2p1_p23.png. Light/Dark unchecked. Plead My Case / Senate. ---

LS_DECK_NAME = "This deck is your Dos mas"
LS_SIDE = "Light"
LS_FORM = "xerox_2013"
LS_SCAN = "extract/day2/d2p1_p23.png"
LS_PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 23
LS_STARTING = ("Plead My Case To The Senate / Sanity And Compassion", False)

LS_RESERVE = [
    n("Plead My Case To The Senate / Sanity And Compassion"),  # 1
    n("Coruscant: Jedi Council Chambers"),  # 2  Coruscant: Senate JCC
    n("Coruscant: Galactic Senate"),  # 3
    n("Strike Planning"),  # 4
    n("Wookiee", True),  # 5
    n("Rogue Squadron Tactics", True),  # 6
    n("Might Of The Republic"),  # 7
    n("Might Of The Republic"),  # 8
    n("Might Of The Republic"),  # 9
    n("Rebel Leadership", True),  # 10
    n("Rebel Leadership", True),  # 11
    n("Rebel Leadership", True),  # 12
    n("Let The Wookiee Win", True),  # 13
    n("Let The Wookiee Win", True),  # 14
    n("Rebel Barrier"),  # 15
    n("Rebel Barrier"),  # 16
    n("Sense"),  # 17
    n("Sense"),  # 18
    n("Gungan Warrior"),  # 19  Naboo kids
    n("Gungan Warrior"),  # 20
    n("It Could Be Worse"),  # 21
    n("It Could Be Worse"),  # 22
    n("NOOOOOOOOOOOO!", True),  # 23  NOOO!
    n("Narrow Escape"),  # 24
    n("Bail Organa", True),  # 25
    n("Bail Organa", True),  # 26
    n("Bail Organa, Elder Of Rebellion", True),  # 27
    n("Bail Organa, Elder Of Rebellion", True),  # 28
    n("Luke Skywalker, Rebel Scout", True),  # 29
    n("Admiral Ackbar", True),  # 30
    n("Wedge Antilles, Red Squadron Leader"),  # 31
    n("Jedi Survivor", True),  # 32
    n("Lando Calrissian, Scoundrel"),  # 33
    n("Senator Leia Organa", True),  # 34
    n("Jaina Solo", True),  # 35
    n("Owen Lars & Beru Lars"),  # 36
    n("Mas Amedda"),  # 37
    n("General Airen Cracken", True),  # 38
    n("Wyron Serper", True),  # 39
    n("Captain Yutani With Blaster Cannon", True),  # 40
    n("Chewbacca, Protector", True),  # 41
    n("General Solo", True),  # 42
    n("Obi-Wan Kenobi", True),  # 43
    n("Corran Horn"),  # 44
    n("Senator Padme Amidala", True),  # 45
    n("Senator Mon Mothma", True),  # 46
    n("Commander Vanden Willard"),  # 47
    n("Imperial Atrocity", True),  # 48
    n("So This Is How Liberty Dies", True),  # 49
    n("Field Dressing", True),  # 50
    n("Senate Hovercam"),  # 51
    n("Alderaan Consular Ship", True),  # 52  Alderaan Cruiser Ship
    n("Home One"),  # 53
    n("Kashyyyk: Forest Depths", True),  # 54
    n("Home One: War Room"),  # 55
    n("Dressel", True),  # 56
    n("Endor: Back Door"),  # 57
    n("Heading For The Medical Frigate"),  # 58
    n("Luke Skywalker, Rebel Scout", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

LS_SHIELDS = [
    n("Weapons Display"),  # 1
    n("Your Insight Serves You Well", True),  # 2
    n("Do, Or Do Not", True),  # 3
    n("Wise Advice", True),  # 4
    n("Ultimatum", True),  # 5
    n("Let's Keep A Little Optimism Here", True),  # 6
    n("Planetary Defenses", True),  # 7
    n("Don't Do That Again", True),  # 8
    n("Battle Plan", True),  # 9
    n("Simple Tricks And Nonsense", True),  # 10
    n("A Tragedy Has Occurred", True),  # 11
    n("Aim High", True),  # 12
    n("Chasm", True),  # 13
    n("The Professor", True),  # 14
    n("Your Ship?"),  # 15
]

LS_ADD: list[tuple[str | None, bool]] = []

LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []


# --- Dark: d2p1_p24.png. DARK checked. Senate "Jake's Senate". ---

DS_DECK_NAME = 'Senate "Jake\'s Senate"'
DS_SIDE = "Dark"
DS_FORM = "xerox_2013"
DS_SCAN = "extract/day2/d2p1_p24.png"
DS_PDF = "2014 Worlds Day 2 Part 1.pdf"
DS_PDF_PAGE = 24
DS_STARTING = ("My Lord, Is That Legal? / I Will Make It Legal", False)

DS_RESERVE = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),  # 1
    n("Ni Chuba Na??", True),  # 2  Ni Chuba Na
    n("Crush The Rebellion"),  # 3
    n("First Strike"),  # 4
    n("Combat Response", True),  # 5
    n("Black Sun Fleet"),  # 6
    n("Tatooine: Desert Landing Site"),  # 7
    n("Coruscant: Galactic Senate"),  # 8  Coruscant: Senate
    n("This Is Outrageous!"),  # 9
    n("Lott Dod"),  # 10
    n("Short Range Fighters & Watch Your Back"),  # 11
    n("Boba Fett, Prepared Hunter", True),  # 12
    n("Zuckuss", True),  # 13
    n("Toonbuck Toora"),  # 14
    n("Mobility", True),  # 15  Monnilist
    n("Short Range Fighters & Watch Your Back"),  # 16
    n("Passel Argente"),  # 17
    n("Lott Dod"),  # 18
    n("SFS L-s9.3 Laser Cannons"),  # 19  SFS G8 Laser Cannons
    n("Edcel Bar Gane"),  # 20
    n("Prepared Defenses"),  # 21
    n("Squabbling Delegates"),  # 22
    n("Sunsdown & Too Cold For Speeders"),  # 23
    n("Altering The Deal"),  # 24  Altering the deal control
    n("Coruscant Guard"),  # 25
    n("Darth Maul, Young Apprentice"),  # 26  Darth Maul w/ Sabers
    n("Tikkes"),  # 27
    n("Squabbling Delegates"),  # 28
    n("Jango Fett", True),  # 29  Mandalorian, Father Of Fett
    n("Ability, Ability, Ability"),  # 30  Ability x 3
    n("Naboo: Theed Palace Generator Core"),  # 31
    n("Darth Vader With Lightsaber"),  # 32
    n("Masterful Move"),  # 33  Master Supported
    n("Sense"),  # 34
    n("Vote Now!"),  # 35
    n("Punishing One", True),  # 36
    n("Open Fire!"),  # 37  I'm Free To / Open Fire scrawl
    n("Slave I, Symbol Of Fear", True),  # 38
    n("Squabbling Delegates"),  # 39
    n("Senate Hovercam"),  # 40
    n("The Phantom Menace"),  # 41
    n("You Are Beaten"),  # 42
    n("Baskol Yeelrm"),  # 43
    n("Our Blockade Is Perfectly Legal"),  # 44
    n("Lott Dod"),  # 45
    n("Maul's Double-Bladed Lightsaber"),  # 46  Darth Maul w/ Stick
    n("Sense"),  # 47
    n("Lott Dod"),  # 48
    n("Yeb Yeb Adem'thorn"),  # 49
    n("Open Fire!"),  # 50  same scrawl as 37
    n("Baron Soontir Fel"),  # 51
    n("Dengar", True),  # 52
    n("I Have You Now"),  # 53
    n("Saber 1"),  # 54
    n("Most Wanted", True),  # 55
    n("Limited Resources"),  # 56
    n("Evader & Monnok"),  # 57
    n("Darth Vader With Lightsaber"),  # 58
    n("Toonbuck Toora"),  # 59
    n("Knowledge And Defense", True),  # 60
]

DS_SHIELDS = [
    n("Do They Have A Code Clearance?"),  # 1  Code Clearance!
    n("Battle Order", True),  # 2
    n("Leave Them To Me", True),  # 3
    n("There Is No Try"),  # 4
    n("Oppressive Enforcement"),  # 5
    n("A Useless Gesture", True),  # 6
    n("Resistance"),  # 7
    n("Fanfare"),  # 8
    n("Death Star Sentry", True),  # 9
    n("Firepower", True),  # 10
    n("Abyss", True),  # 11
    n("Allegations Of Corruption"),  # 12
    n("Secret Plans"),  # 13
    n("Come Here You Big Coward"),  # 14
    n("You Cannot Hide Forever", True),  # 15
]

DS_ADD: list[tuple[str | None, bool]] = []

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []

NOTES = """
Jake from State Farm, 2014 Worlds Day 2, 2013 green form. No legal surname
on the sheet. Username blank.

Light d2p1_p23 This deck is your Dos mas. Light/Dark unchecked; side from
Plead My Case / Senate cards. Same archetype as Mitch Nieland Dos mas!
(d2p2_p01): Wookiee (V) start, JCC, Gungan Warrior (Naboo kids), Dressel.

Dark d2p1_p24 Senate \"Jake's Senate\". DARK checked. My Lord, Is That Legal.

LS: 2 Coruscant: Senate JCC → Jedi Council Chambers (line 3 is Galactic
Senate). 5 Wookiee (V) character. 19-20 Naboo kids → Gungan Warrior.
23 NOOO! → NOOOOOOOOOOOO! (V). 52 Alderaan Cruiser Ship → Alderaan
Consular Ship (V). 56 Dressel (V) system.

DS: 2 Ni Chuba Na → Ni Chuba Na?? (V). 15 Monnilist (V) taken as Mobility.
19 SFS G8 Laser Cannons → SFS L-s9.3 Laser Cannons. 24 Altering the deal
→ Altering The Deal. 26 Maul w/ Sabers → Darth Maul, Young Apprentice.
29 Mandalorian, Father Of Fett (V) → Jango Fett. 30 Ability x 3 →
Ability, Ability, Ability. 33 Master Supported → Masterful Move.
37/50 Open Fire! (scrawl). 46 Maul w/ Stick → Maul's Double-Bladed
Lightsaber.
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
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 15, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 15, len(DS_SHIELDS)
    print(
        "transcribe_jake.py",
        "LS",
        PLAYER,
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
    print(
        "transcribe_jake.py",
        "DS",
        PLAYER,
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
    _dump("Light", LS_RESERVE, LS_SHIELDS, LS_ADD)
    _dump("Dark", DS_RESERVE, DS_SHIELDS, DS_ADD)
