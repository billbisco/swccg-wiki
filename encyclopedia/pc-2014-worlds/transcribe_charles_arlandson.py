#!/usr/bin/env python3
"""Day 2 Xerox transcription: Charles Arlandson (DaBrazen).

Source scans: extract/day2/d2p1_p13.png (Dark, Kessel CR) and
extract/day2/d2p1_p14.png (Light, A Wookie Mistake!). 2013 form,
Worlds 08/23/14, green-tinted. (V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Charles Arlandson"
USERNAME = "DaBrazen"
LS_DECK_NAME = "A Wookie Mistake!"
DS_DECK_NAME = ""
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2013"
LS_SCAN = "extract/day2/d2p1_p14.png"
DS_SCAN = "extract/day2/d2p1_p13.png"
PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 14
DS_PDF_PAGE = 13
LS_STARTING = ("Plead My Case To The Senate / Sanity And Compassion", True)
DS_STARTING = ("Kessel", False)


# --- Dark: d2p1_p13.png. DARK checked. Kessel CR. ---

DS_RESERVE = [
    n("Kessel"),  # 1
    n("Kessel: Spice Mines - Administrator's Office"),  # 2
    n("Ni Chuba Na??", True),  # 3  written Ni Chuba Na
    n("Gift Of The Master"),  # 4
    n("Combat Readiness", True),  # 5
    n("I'll Take Them Myself"),  # 6
    n("Moruth Doole, Kessel Administrator"),  # 7  Spice Mine Administrator
    n("Darth Vader, Dark Lord Of The Sith"),  # 8
    n("Dr. Evazan & Ponda Baba"),  # 9
    n("Galen Marek, Starkiller"),  # 10
    n("Galen Marek, Starkiller"),  # 11
    n("Galen Marek, Starkiller"),  # 12
    n("Count Dooku"),  # 13
    n("Count Dooku"),  # 14
    n("Emperor Palpatine"),  # 15
    n("Emperor Palpatine"),  # 16
    n("Darth Maul With Lightsaber"),  # 17
    n("Darth Maul With Lightsaber"),  # 18
    n("Arica"),  # 19
    n("Garindan", True),  # 20
    n("Darth Vader, Betrayer Of The Jedi"),  # 21
    n("Jango Fett, The Assassin"),  # 22
    n("Boba Fett, Prepared Hunter"),  # 23
    n("Slave I, Symbol Of Fear"),  # 24  Slave One
    n("Maul's Sith Infiltrator"),  # 25
    n("Blizzard 4"),  # 26
    n("Blizzard 4"),  # 27
    n("Kessel Surveillance System"),  # 28
    n("Galen's Lightsaber, Vader's Gift"),  # 29
    n("Vader's Lightsaber"),  # 30
    n("Dooku's Lightsaber"),  # 31
    n("Kessel: Spice Mines - Prison"),  # 32
    n("Kessel: Spice Mines - Extraction Facility"),  # 33
    n("Cloud City: Security Tower", True),  # 34
    n("Blaster Rack", True),  # 35
    n("Jabba's Haven"),  # 36
    n("The Phantom Menace"),  # 37
    n("Imperial Justice", True),  # 38
    n("Sense"),  # 39
    n("You Are Beaten", True),  # 40  After crossed; You Are Beaten kept
    n("Sonic Bombardment", True),  # 41
    n("Sonic Bombardment", True),  # 42
    n("Sonic Bombardment", True),  # 43
    n("Short Range Fighters & Watch Your Back!"),  # 44  Short Range Fighters Combo
    n("Short Range Fighters & Watch Your Back!"),  # 45
    n("Short Range Fighters & Watch Your Back!"),  # 46
    n("Dark Maneuvers"),  # 47
    n("Dark Maneuvers"),  # 48
    n("Force Field", True),  # 49
    n("Force Field", True),  # 50
    n("Cold Feet", True),  # 51
    n("Why Didn't You Tell Me?", True),  # 52
    n("Force Push", True),  # 53
    n("Sniper & Dark Strike"),  # 54
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 55  Ghhhk & Those Rebels
    n("Masterful Move & Endor Occupation"),  # 56  Masterful Move Combo
    n("Force Lightning"),  # 57
    n("Spice Mine Operations"),  # 58
    n("Black Sun Fleet"),  # 59
    n("Knowledge And Defense"),  # 60
]

DS_SHIELDS = [
    n("Do They Have A Code Clearance?"),  # 1
    n("Firepower", True),  # 2
    n("Imperial Detention", True),  # 3
    n("Resistance"),  # 4
    n("You Cannot Hide Forever", True),  # 5
    n("Death Star Sentry", True),  # 6
    n("Battle Order"),  # 7
    n("Fanfare"),  # 8
    n("A Useless Gesture"),  # 9
    n("Oppressive Enforcement", True),  # 10
    n("Come Here You Big Coward"),  # 11
    n("Allegations Of Corruption"),  # 12
    n("Abyss", True),  # 13
    n("Secret Plans"),  # 14
    n("After Her!"),  # 15
]

DS_ADD: list[tuple[str | None, bool]] = []


# --- Light: d2p1_p14.png. LIGHT checked. A Wookie Mistake! ---

LS_RESERVE = [
    n("Plead My Case To The Senate / Sanity And Compassion", True),  # 1
    n("Coruscant: Galactic Senate"),  # 2
    n("Coruscant: Jedi Council Chamber"),  # 3
    n("Rogue Squadron Tactics"),  # 4
    n("Wokling", True),  # 5
    n("Strike Planning"),  # 6
    n("Heading For The Medical Frigate"),  # 7
    n("Chewbacca, Protector", True),  # 8
    n("Corran Horn"),  # 9
    n("Senator Padme Amidala"),  # 10
    n("General Airen Cracken"),  # 11
    n("Bail Organa, Father Of Rebellion"),  # 12
    n("Bail Organa, Father Of Rebellion"),  # 13
    n("Bail Organa"),  # 14
    n("Bail Organa"),  # 15
    n("Commander Vanden Willard"),  # 16
    n("Captain Yutani With Blaster Cannon"),  # 17
    n("General Solo", True),  # 18
    n("Luke Skywalker, Rebel Scout", True),  # 19
    n("Luke Skywalker, Rebel Scout"),  # 20
    n("Owen Lars & Beru Lars"),  # 21
    n("Lando Calrissian, Scoundrel"),  # 22
    n("Wyron Serper", True),  # 23
    n("Jedi Survivor", True),  # 24
    n("Wedge Antilles, Red Squadron Leader"),  # 25
    n("Jaina Solo"),  # 26
    n("Senator Mon Mothma"),  # 27
    n("Senator Leia Organa"),  # 28
    n("Admiral Ackbar", True),  # 29
    n("Obi-Wan Kenobi", True),  # 30
    n("Mas Amedda"),  # 31
    n("Home One"),  # 32
    n("Alderaan Consular Ship"),  # 33
    n("Dressel"),  # 34
    n("Home One: War Room"),  # 35
    n("Endor: Back Door"),  # 36
    n("Kashyyyk: Forest Depths"),  # 37
    n("Field Promotion"),  # 38
    n("So This Is How Liberty Dies"),  # 39
    n("Senate Hovercam"),  # 40
    n("Imperial Atrocity", True),  # 41
    n("Menace Fades"),  # 42
    n("Narrow Escape"),  # 43
    n("Might Of The Republic"),  # 44
    n("Might Of The Republic"),  # 45
    n("Might Of The Republic"),  # 46
    n("Rebel Leadership", True),  # 47
    n("Rebel Leadership", True),  # 48
    n("Rebel Leadership", True),  # 49
    n("Let The Wookiee Win", True),  # 50
    n("Let The Wookiee Win", True),  # 51
    n("Rebel Barrier"),  # 52  Rebel Leadership crossed
    n("Rebel Barrier"),  # 53
    n("Nabrun Leids"),  # 54
    n("Nabrun Leids"),  # 55
    n("Sense"),  # 56
    n("Sense"),  # 57
    n("It Could Be Worse"),  # 58
    n("NOOOOOOOOOOOO!", True),  # 59
    n("Anger, Fear, Aggression"),  # 60
]

LS_SHIELDS = [
    n("Aim High"),  # 1
    n("Planetary Defenses"),  # 2
    n("Chasm"),  # 3
    n("A Tragedy Has Occurred"),  # 4
    n("Simple Tricks And Nonsense"),  # 5
    n("Battle Plan"),  # 6
    n("Don't Do That Again", True),  # 7
    n("Do, Or Do Not"),  # 8
    n("Wise Advice"),  # 9
    n("Your Insight Serves You Well", True),  # 10
    n("Weapons Display", True),  # 11
    n("Ultimatum"),  # 12
    n("Let's Keep A Little Optimism Here", True),  # 13
    n("The Professor", True),  # 14
    n("There Is Another"),  # 15
]

LS_ADD: list[tuple[str | None, bool]] = []


LS_UNREAD: list[int] = []
DS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []
DS_NO_DEST: list[str] = []

NOTES = """
Charles Arlandson / DaBrazen, 2014 Worlds 08/23/14, 2013 form (green).
Email [redacted] on the sheet (not stored as a field).
DS d2p1_p13 DARK checked. Deck name blank; Kessel CR from sites.
Line 1 written Kessel (system), not the objective title. Kessel CR /
Spice Mines Of Kessel inferred from Administrator's Office and spice sites.
7 Spice Mine Administrator -> Moruth Doole, Kessel Administrator.
24 Slave One -> Slave I, Symbol Of Fear.
40 After crossed; You Are Beaten kept (V box filled).
44-46 Short Range Fighters Combo -> SRF & Watch Your Back!
56 Masterful Move Combo -> Masterful Move & Endor Occupation.

LS d2p1_p14 LIGHT checked. Deck A Wookie Mistake! (prior name crossed).
12-13 Bail Organa, Father Of Rebellion; 14-15 Bail Organa.
23 Wyron Serper (written Wyrn Serper).
52 Rebel Leadership crossed; Rebel Barrier kept.
Hidden Fortress and Jedi Tests empty both sides.
""".strip()


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 15, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 15, len(DS_SHIELDS)
    print("file", __file__)
    print("LS", PLAYER, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
    print("DS", PLAYER, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
