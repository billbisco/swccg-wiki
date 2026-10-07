#!/usr/bin/env python3
"""Day 2 Xerox transcription: Sean Miller.

Source scans: extract/day2/d2p2_p03.png (Light, SCC) and
extract/day2/d2p2_p04.png (Dark, Walking). 2013 form, Day 2.
We'll Handle This / Coruscant and Imperial Occupation / Hoth walkers.
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Sean Miller"
USERNAME = ""
PDF = "2014 Worlds Day 2 Part 2.pdf"


# --- Light: d2p2_p03.png, 2013 form. LIGHT checked. ---

LS_DECK_NAME = "SCC"
LS_SIDE = "Light"
LS_FORM = "xerox_2013"
LS_SCAN = "extract/day2/d2p2_p03.png"
LS_PDF_PAGE = 3
LS_STARTING = ("We'll Handle This / Duel Of The Fates", True)

LS_RESERVE = [
    n("We'll Handle This / Duel Of The Fates", True),  # 1  We'll handle this / Duel of Fates
    n("Coruscant: Senate Landing Platform", True),  # 2  Coruscant: SLP
    n("Coruscant: Night Club", True),  # 3
    n("Coruscant: Jedi Archives", True),  # 4
    n("Coruscant: Jedi Council Chamber", True),  # 5  Coruscant: JCC
    n("A Jedi's Plans", True),  # 6
    n("Projection Of A Skywalker"),  # 7
    n("Out Of Commission & Transmission Terminated"),  # 8  OCC & TT
    n("Plo Koon"),  # 9
    n("Jedi Advisor", True),  # 10
    n("Yoda, Senior Council Member", True),  # 11
    n("Ki-Adi-Mundi", True),  # 12
    n("Threepio With His Parts Showing"),  # 13  Threepio w/ parts
    n("Depa Billaba"),  # 14
    n("Blaster Deflection"),  # 15
    n("Clash Of Sabers"),  # 16
    n("Jedi Lightsaber", True),  # 17
    n("Speak With The Jedi Council"),  # 18
    n("Sorry About The Mess & Blaster Proficiency"),  # 19  SATM & BP
    n("Nabrun Leids"),  # 20
    n("Sorry About The Mess & Blaster Proficiency"),  # 21  SATM & BP
    n("Qui-Gon Jinn With Lightsaber"),  # 22  Qui-Gon with stick
    n("Impressive, Most Impressive"),  # 23
    n("Blaster Deflection"),  # 24
    n("Let The Wookiee Win", True),  # 25  LTWW
    n("Speak With The Jedi Council", True),  # 26
    n("Are You Brain Dead?!"),  # 27  Are you brain dead
    n("Maris Brood, Fallen Jedi", True),  # 28  Fallen Jedi (V)
    n("Let The Wookiee Win", True),  # 29  LTWW
    n("A Jedi's Concentration"),  # 30
    n("The Signal", True),  # 31
    n("Sense"),  # 32
    n("Honor Of The Jedi"),  # 33  Honor of Jedi
    n("Qui-Gon Jinn With Lightsaber"),  # 34  Qui-Gon w/ stick
    n("Obi-Wan Kenobi, Jedi Knight", True),  # 35
    n("Obi-Wan's Lightsaber"),  # 36  Obi-Wan's lightsaber; (V) empty
    n("Smoke Screen"),  # 37  Small Screen
    n(None),  # 38  We-On Jedi; unread, see NOTES
    n("Imperial Atrocity", True),  # 39
    n("A Jedi's Resilience"),  # 40
    n("Sense"),  # 41
    n("Jedi Advisor", True),  # 42
    n("A Jedi's Resilience"),  # 43
    n("Quick Draw", True),  # 44
    n("Mace Windu, Master Of The Order", True),  # 45  Mace Windu MOTS (V)
    n("Alter", True),  # 46
    n("Mace Windu", True),  # 47
    n("Obi-Wan Kenobi, Jedi Knight", True),  # 48
    n("Imperial Atrocity", True),  # 49
    n("It Could Be Worse"),  # 50
    n("A Jedi's Resilience"),  # 51
    n("We're Doomed"),  # 52
    n("Mandalorian Mishap", True),  # 53
    n("I Hope She's All Right"),  # 54
    n("Nabrun Leids"),  # 55
    n("Sense"),  # 56
    n("Menace Fades"),  # 57
    n("Your Insight Serves You Well"),  # 58
    n("Jedi Lightsaber", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60  AFA
]

LS_SHIELDS = [
    n("Your Insight Serves You Well", True),  # 1
    n("Battle Plan"),  # 2
    n("Simple Tricks And Nonsense"),  # 3  Simple Tricks + nonsense
    n("Let's Keep A Little Optimism Here", True),  # 4
    n("Ultimatum"),  # 5
    n("Planetary Defenses", True),  # 6
    n("Your Ship?", True),  # 7
    n("Don't Do That Again"),  # 8
    n("He Can Go About His Business", True),  # 9
    n("The Professor", True),  # 10
    n("Only Jedi Carry That Weapon"),  # 11  Only Jedi Can Use That Weapon
    n("Aim High"),  # 12
    n("Weapons Display", True),  # 13
    n("Chasm", True),  # 14
    n("A Tragedy Has Occurred"),  # 15
]

LS_ADD = []

LS_UNREAD = [38]
LS_NO_DEST: list[str] = []


# --- Dark: d2p2_p04.png, 2013 form. DARK checked. ---

DS_DECK_NAME = "Walking"
DS_SIDE = "Dark"
DS_FORM = "xerox_2013"
DS_SCAN = "extract/day2/d2p2_p04.png"
DS_PDF_PAGE = 4
DS_STARTING = ("Imperial Occupation / Imperial Control", True)

DS_RESERVE = [
    n("Imperial Occupation / Imperial Control", True),  # 1  Imperial Occupation / Imp Ctrl
    n("Prepared Defenses"),  # 2
    n("Endor Shield", True),  # 3
    n("Ni Chuba Na??"),  # 4
    n("You May Start Your Landing", True),  # 5  YMSYL
    n("Hoth"),  # 6
    n("Hoth: 5th Marker", True),  # 7
    n("Hoth: 6th Marker"),  # 8
    n("Hoth: 3rd Marker"),  # 9
    n("Hoth: 1st Marker"),  # 10
    n("Flagship Executor"),  # 11
    n("Victory", True),  # 12
    n("Victory", True),  # 13
    n("Conquest", True),  # 14
    n("AT-AT Cannon", True),  # 15
    n("Target The Main Generator"),  # 16
    n("AT-AT Cannon"),  # 17  AT-AT ACC
    n("Imperial Decree"),  # 18
    n("Hoth Blockade", True),  # 19
    n("No Escape", True),  # 20
    n("Alert My Star Destroyer"),  # 21
    n("Imperial Propaganda", True),  # 22
    n("Imbalance & Kintan Strider", True),  # 23
    n("Imperial Barrier"),  # 24
    n("Imperial Artillery"),  # 25
    n("Imperial Command"),  # 26
    n("Imperial Command"),  # 27
    n("Imperial Command"),  # 28
    n("Trample", True),  # 29
    n("Trample"),  # 30
    n("Stop Motion", True),  # 31
    n("Stop Motion", True),  # 32
    n("Force Push", True),  # 33
    n("Cold Feet", True),  # 34
    n("AT-AT Driver", True),  # 35  ADT FTR
    n("AT-AT Driver", True),  # 36  ADT FTR
    n("Control & Set For Stun", True),  # 37  Control / SFS
    n("We're In Attack Position Now"),  # 38
    n("We're In Attack Position Now"),  # 39
    n("Juno Eclipse, Black Leader", True),  # 40  Black Leader
    n("ISB Sector Commander", True),  # 41
    n("Grand Moff Tarkin", True),  # 42
    n("Darth Vader, Dark Lord Of The Sith"),  # 43  DV DL o TS
    n("Grand Moff Tarkin", True),  # 44
    n("Garindan", True),  # 45
    n("Grand Admiral Thrawn"),  # 46
    n("Garindan", True),  # 47
    n("General Veers", True),  # 48
    n("Commander Igar"),  # 49
    n("General Veers", True),  # 50  Veers
    n("The Emperor's Reach", True),  # 51
    n("Jango Fett, The Assassin", True),  # 52
    n("U-3PO (Yoo-Threepio)"),  # 53  U3PO
    n("Blizzard 1", True),  # 54
    n("Blizzard 2", True),  # 55
    n("Marquand In Blizzard 6", True),  # 56
    n("Blizzard 4"),  # 57
    n("Blizzard 4"),  # 58
    n("Tempest 1"),  # 59
    n("Knowledge And Defense", True),  # 60  K + D
]

DS_SHIELDS = [
    n("Firepower", True),  # 1
    n("Resistance", True),  # 2
    n("Leave Them To Me", True),  # 3
    n("A Useless Gesture", True),  # 4
    n("Imperial Detention", True),  # 5
    n("Fanfare", True),  # 6
    n("There Is No Try"),  # 7
    n("Come Here You Big Coward"),  # 8
    n("Battle Order"),  # 9
    n("Secret Plans"),  # 10
    n("Death Star Sentry"),  # 11
    n("Allegations Of Corruption", True),  # 12
    n("Abyss", True),  # 13
]

DS_ADD = []

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []


NOTES = """
Sean Miller, 2014 Worlds Day 2, 2013 form. Username blank.
Light d2p2_p03.png deck SCC (LIGHT checked). We'll Handle This / Coruscant.
Dark d2p2_p04.png deck Walking (DARK checked). Imperial Occupation / Hoth walkers.

LS uncertain:
- 2 Coruscant: SLP (V) -> Coruscant: Senate Landing Platform (vb5).
- 8 OCC & TT -> Out Of Commission & Transmission Terminated.
- 19/21 SATM & BP -> Sorry About The Mess & Blaster Proficiency.
- 22/34 Qui-Gon with stick -> Qui-Gon Jinn With Lightsaber.
- 27 Are you brain dead -> Are You Brain Dead?!
- 28 Fallen Jedi (V) -> Maris Brood, Fallen Jedi (vb4).
- 36 Obi-Wan's Lightsaber, (V) empty (line is not crossed out; a stray mark).
- 37 Small Screen -> Smoke Screen.
- 38 We-On Jedi, (V) empty. Not Fallen Jedi (that's 28). Not a unique title
  match. Left unread rather than guess (Jedi Presence / Fall Of A Jedi / I Am
  A Jedi all fail the letters).
- 45 Mace Windu MOTS (V) -> Mace Windu, Master Of The Order (vb7). 47 is
  Mace Windu with (V) checked on the Coruscant character.
- Shield 11 Only Jedi Can Use That Weapon -> Only Jedi Carry That Weapon.

DS uncertain:
- 5 YMSYL (V) -> You May Start Your Landing (Dark Hoth, vb8 (V)).
- 17 AT-AT ACC, (V) empty -> second AT-AT Cannon (line 15 is the (V) copy).
- 19 Hoth Blockade (V) -> Hoth Blockade (vb2).
- 35-36 ADT FTR (V) -> AT-AT Driver (V).
- 40 Black Leader (V) -> Juno Eclipse, Black Leader (vb4).
- 43 DV DLoTS -> Darth Vader, Dark Lord Of The Sith.
- 52 Jango Fett, The Assassin (V) (vb8).
- 12-13 two Victory (V); unique Star Destroyer listed twice as written.
- Shields 14-15 blank.
""".strip()


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 15, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert 12 <= len(DS_SHIELDS) <= 15, len(DS_SHIELDS)
    print("file", __file__)
    print("player", PLAYER, "username", USERNAME or "-")
    print("LS", LS_DECK_NAME, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
    print("DS", DS_DECK_NAME, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
