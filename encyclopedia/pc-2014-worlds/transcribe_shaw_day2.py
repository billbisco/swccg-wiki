#!/usr/bin/env python3
"""Day 2 Xerox transcription: Greg Shaw (Stealtheblind).

Source scans: extract/day2/d2p1_p21.png (Dark, Bonne Nuit / Hunt Down)
and extract/day2/d2p1_p22.png (Light, Bonne Chance / Y4 Jedi Council).
2010 form, Worlds 2014 Day 2. (V) follows the sheet checkbox. Dittos expanded.
Day 2 60 is not the Day 3 Bonne Nuit / Bonne Chance list.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Greg Shaw"
USERNAME = "Stealtheblind"
FORM = "xerox_2010"
PDF = "2014 Worlds Day 2 Part 1.pdf"

SHAW_D2_PLAYER = PLAYER
SHAW_D2_USERNAME = USERNAME
SHAW_D2_DS_DECK_NAME = "Bonne Nuit"
SHAW_D2_LS_DECK_NAME = "Bonne Chance"


# --- Dark: d2p1_p21.png. DARK checked. Hunt Down. ---

SHAW_D2_DS_SCAN = "extract/day2/d2p1_p21.png"
SHAW_D2_DS_PDF_PAGE = 21
SHAW_D2_DS_SIDE = "Dark"
SHAW_D2_DS_STARTING = n(
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True
)

SHAW_D2_DS_RESERVE = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),  # 1
    n("Coruscant"),  # 2  written Coruscant (SE)
    n("Coruscant: Imperial City"),  # 3
    n("A Sith's Plans"),  # 4
    n("Prepared Defenses", True),  # 5
    n("Ni Chuba Na??", True),  # 6  Ni Chuba Na
    n("Gift Of The Master"),  # 7
    n("Endor Shield", True),  # 8
    n("Blockade Flagship: Bridge"),  # 9
    n("Endor"),  # 10
    n("Naboo: Theed Palace Generator Core"),  # 11
    n("Darth Vader, Dark Lord Of The Sith"),  # 12
    n("Darth Vader, Dark Lord Of The Sith"),  # 13
    n("Darth Vader, Dark Lord Of The Sith"),  # 14
    n("Galen Marek, Starkiller"),  # 15
    n("Galen Marek, Starkiller"),  # 16
    n("Galen Marek, Starkiller"),  # 17
    n("Boba Fett, Bounty Hunter"),  # 18
    n("Emperor Palpatine"),  # 19
    n("Emperor Palpatine"),  # 20
    n("Emperor Palpatine"),  # 21
    n("Juno Eclipse, Black Leader"),  # 22
    n("Juno Eclipse, Black Leader"),  # 23
    n("Admiral Ozzel"),  # 24
    n("Garindan", True),  # 25
    n("Mara Jade With Lightsaber"),  # 26
    n("P-59"),  # 27
    n("Dengar With Blaster Carbine", True),  # 28
    n("Dr. Evazan & Ponda Baba"),  # 29
    n("General Nevar"),  # 30
    n("Grand Moff Tarkin", True),  # 31
    n("Vader's Lightsaber"),  # 32
    n("Galen's Lightsaber, Vader's Gift"),  # 33
    n("Blizzard 4"),  # 34
    n("Rogue Shadow"),  # 35
    n("Victory"),  # 36
    n("Blast Door Controls"),  # 37
    n("Blaster Rack", True),  # 38
    n("Combat Response", True),  # 39
    n("Emperor's Power", True),  # 40
    n("No Escape"),  # 41
    n("Revenge Of The Sith"),  # 42
    n("Imperial Propaganda", True),  # 43
    n("Close Call", True),  # 44
    n("Force Field", True),  # 45
    n("Force Push", True),  # 46
    n("Force Lightning"),  # 47
    n("Force Lightning"),  # 48
    n("We Must Accelerate Our Plans"),  # 49
    n("We Must Accelerate Our Plans"),  # 50
    n("We Must Accelerate Our Plans"),  # 51
    n("Stop Motion", True),  # 52
    n("Cold Feet", True),  # 53
    n("Masterful Move"),  # 54
    n("Masterful Move"),  # 55
    n("Ghhhk"),  # 56
    n("One Beautiful Thing"),  # 57
    n("One Beautiful Thing"),  # 58
    n("Weapon Levitation & The Empire's Back"),  # 59
    n("Knowledge And Defense", True),  # 60
]

SHAW_D2_DS_SHIELDS = [
    n("Fanfare", True),  # 1
    n("A Useless Gesture", True),  # 2
    n("Weapon Of A Sith"),  # 3
    n("Battle Order"),  # 4
    n("Resistance"),  # 5
    n("Do They Have A Code Clearance?", True),  # 6
    n("I Find Your Lack Of Faith Disturbing", True),  # 7
    n("You Cannot Hide Forever", True),  # 8
    n("Firepower", True),  # 9
    n("There Is No Try"),  # 10
    n("Come Here You Big Coward"),  # 11
    n("Secret Plans"),  # 12
]

SHAW_D2_DS_ADD = [
    n("Abyss", True),  # 1
    n("Allegations Of Corruption"),  # 2
    n("Death Star Sentry", True),  # 3
]


# --- Light: d2p1_p22.png. LIGHT checked. Y4 / Jedi Council. ---

SHAW_D2_LS_SCAN = "extract/day2/d2p1_p22.png"
SHAW_D2_LS_PDF_PAGE = 22
SHAW_D2_LS_SIDE = "Light"
SHAW_D2_LS_STARTING = n("Yavin 4: Massassi Throne Room")

SHAW_D2_LS_RESERVE = [
    n("Yavin 4: Massassi Throne Room"),  # 1
    n("Coruscant: Jedi Council Chamber", True),  # 2
    n("Home One: War Room"),  # 3
    n("Naboo: Boss Nass' Chambers"),  # 4
    n("Naboo: Battle Plains"),  # 5
    n("Yavin 4: Massassi War Room", True),  # 6
    n("Anakin Skywalker, Padawan Learner"),  # 7
    n("Admiral Ackbar", True),  # 8
    n("Home One"),  # 9
    n("Houjix"),  # 10
    n("Luke Skywalker, Strong In The Force"),  # 11
    n("Luke Skywalker, Strong In The Force"),  # 12
    n("Luke's Lightsaber"),  # 13
    n("Mace Windu", True),  # 14
    n("Mace Windu", True),  # 15
    n("Master Qui-Gon", True),  # 16
    n("Master Qui-Gon", True),  # 17
    n("Han, Chewie, And The Falcon"),  # 18
    n("Han, Chewie, And The Falcon", True),  # 19  ditto; (V) checked
    n("Jedi Lightsaber", True),  # 20
    n("Sorry About The Mess & Blaster Proficiency"),  # 21
    n("Wokling", True),  # 22
    n("Heading For The Medical Frigate"),  # 23
    n("Jaina Solo"),  # 24
    n("Jaina Solo"),  # 25
    n("Lady Luck"),  # 26
    n("Lando Calrissian, Unlikely Hero"),  # 27
    n("Leia, Rebel Princess"),  # 28
    n("Quick Draw", True),  # 29
    n("Corran Horn"),  # 30
    n("Blaster Deflection"),  # 31
    n("Rebel Leadership", True),  # 32
    n("Rebel Leadership", True),  # 33
    n("Rebel Leadership", True),  # 34
    n("Sai'torr Kal Fas", True),  # 35
    n("Scrambled Transmission", True),  # 36
    n("Seeking An Audience", True),  # 37
    n("Speak With The Jedi Council"),  # 38
    n("Weapon Levitation"),  # 39  as written; Light has Jedi Levitation
    n("Anger, Fear, Aggression", True),  # 40
    n("Lando Calrissian, Scoundrel"),  # 41
    n("Let The Wookiee Win", True),  # 42
    n("Let The Wookiee Win", True),  # 43
    n("Let The Wookiee Win", True),  # 44
    n("Qui-Gon's Lightsaber"),  # 45
    n("Strikeforce", True),  # 46
    n("Wesa Gotta Grand Army"),  # 47
    n("Wesa Gotta Grand Army"),  # 48
    n("Wesa Gotta Grand Army"),  # 49
    n("A Jedi's Resilience"),  # 50
    n("A Jedi's Resilience"),  # 51
    n("Escape Pod", True),  # 52
    n("Escape Pod", True),  # 53
    n("Imperial Atrocity", True),  # 54
    n("Imperial Atrocity", True),  # 55
    n("Imperial Atrocity", True),  # 56
    n("Luke Skywalker, Jedi Knight"),  # 57
    n("Luke Skywalker, Jedi Knight"),  # 58  Mace Windu crossed; ditto of 57 kept
    n("Artoo-Detoo In Red 5"),  # 59
    n("Artoo-Detoo In Red 5"),  # 60
]

SHAW_D2_LS_SHIELDS = [
    n("A Tragedy Has Occurred"),  # 1
    n("Affect Mind", True),  # 2
    n("Aim High"),  # 3
    n("Another Pathetic Lifeform"),  # 4
    n("Battle Plan"),  # 5
    n("Do, Or Do Not"),  # 6
    n("Don't Do That Again", True),  # 7
    n("Let's Keep A Little Optimism Here", True),  # 8
    n("Only Jedi Carry That Weapon"),  # 9
    n("Simple Tricks And Nonsense"),  # 10
    n("The Professor", True),  # 11
    n("Ultimatum"),  # 12
]

SHAW_D2_LS_ADD = [
    n("Weapons Display", True),  # 1
    n("Yavin Sentry", True),  # 2
    n("Your Insight Serves You Well", True),  # 3
]


SHAW_D2_DS_UNREAD: list[int] = []
SHAW_D2_LS_UNREAD: list[int] = []
SHAW_D2_DS_NO_DEST: list[str] = []
SHAW_D2_LS_NO_DEST: list[str] = []  # Weapon Levitation dests Dark JP; kept as written

NOTES = """
Greg Shaw / Stealtheblind, 2014 Worlds Day 2, 2010 form.
Dark d2p1_p21 Bonne Nuit (DARK checked). Hunt Down (V).
Light d2p1_p22 Bonne Chance (LIGHT checked). Y4 / Jedi Council.
No objective title on LS line 1 — Yavin 4: Massassi Throne Room as written.

DS: line 2 Coruscant (SE). Line 6 Ni Chuba Na → Ni Chuba Na??.
Line 11 Naboo: Theed Palace Generator Core (last word Core).
Line 35 Rogue Shadow (not Galen's Fighter as on Day 3).
Line 59 Weapon Levitation & The Empire's Back; (V) empty.

LS: line 18 Han, Chewie, And The Falcon (V) empty; line 19 ditto (V) checked.
Line 39 Weapon Levitation as written (Day 3 had Jedi Levitation / other cards).
Line 41 Lando Calrissian, Scoundrel (separate from Unlikely Hero on 27).
Line 58 Mace Windu crossed; ditto of 57 Luke Skywalker, Jedi Knight kept.
""".strip()


if __name__ == "__main__":
    assert len(SHAW_D2_DS_RESERVE) == 60, len(SHAW_D2_DS_RESERVE)
    assert len(SHAW_D2_DS_SHIELDS) == 12, len(SHAW_D2_DS_SHIELDS)
    assert len(SHAW_D2_LS_RESERVE) == 60, len(SHAW_D2_LS_RESERVE)
    assert len(SHAW_D2_LS_SHIELDS) == 12, len(SHAW_D2_LS_SHIELDS)
    print("transcribe_shaw_day2.py", PLAYER)
    print("  Dark Bonne Nuit reserve", len(SHAW_D2_DS_RESERVE), "shields", len(SHAW_D2_DS_SHIELDS), "add", len(SHAW_D2_DS_ADD), "unread", SHAW_D2_DS_UNREAD, "no_dest", SHAW_D2_DS_NO_DEST)
    print("  Light Bonne Chance reserve", len(SHAW_D2_LS_RESERVE), "shields", len(SHAW_D2_LS_SHIELDS), "add", len(SHAW_D2_LS_ADD), "unread", SHAW_D2_LS_UNREAD, "no_dest", SHAW_D2_LS_NO_DEST)
