#!/usr/bin/env python3
"""Day 2 Xerox transcription: Matthew Harrison-Trainor (MHT).

Source scans: extract/day2_upright/d2p3_p11.png (Light, WYSv) and
extract/day2_upright/d2p3_p12.png (Dark, Slavers). 2013 form, typed.
Worlds Day 2. Light/Dark unchecked; side from cards.
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
FORM = "xerox_2013"
PDF = "2014 Worlds Day 2 Part 3.pdf"

MHT_D2_PLAYER = PLAYER
MHT_D2_LS_DECK_NAME = "WYSv"
MHT_D2_DS_DECK_NAME = "Slavers"


# --- Light: day2_upright/d2p3_p11.png. WYSv. Watch Your Step (V). ---

MHT_D2_LS_SCAN = "extract/day2_upright/d2p3_p11.png"
MHT_D2_LS_PDF_PAGE = 11
MHT_D2_LS_SIDE = "Light"
MHT_D2_LS_STARTING = n("Watch Your Step / This Place Can Be A Little Rough", True)

MHT_D2_LS_RESERVE = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),  # 1
    n("Corellia", True),  # 2
    n("Home One: Docking Bay"),  # 3  Home One: DB
    n("Spaceport City"),  # 4
    n("Spaceport Docking Bay"),  # 5
    n("Spaceport Street"),  # 6
    n("Spaceport Scoundrels Guild"),  # 7  Scoundrel's Guild
    n("Lando Calrissian, Unlikely Hero"),  # 8
    n("Leia, Rebel Princess"),  # 9
    n("Leia, Rebel Princess"),  # 10
    n("Wedge Antilles, Red Squadron Leader"),  # 11  Wedge, RSL
    n("Wedge Antilles, Red Squadron Leader"),  # 12
    n("Yoda, Great Warrior"),  # 13  Yoda, GW
    n("General Crix Madine"),  # 14  General Crix
    n("Romas 'Lock' Navander"),  # 15  Romas
    n("Dash Rendar", True),  # 16
    n("Corran Horn"),  # 17
    n("Sergeant Bruckman"),  # 18
    n("Laudica", True),  # 19
    n("Mirax Terrik"),  # 20  Mirax
    n("Palejo Rashad"),  # 21
    n("Luke Skywalker, Jedi Knight"),  # 22  Luke Skywalker, JK
    n("Luke Skywalker, Jedi Knight"),  # 23
    n("Chewbacca", True),  # 24  Chewie
    n("Captain Han Solo"),  # 25  Captain Han
    n("Jaina Solo"),  # 26
    n("Mace Windu, Master Of The Order"),  # 27  Mace Windu, MOTO
    n("Tarfful, Wookiee Insurgent"),  # 28
    n("Millennium Falcon", True),  # 29  Millenium Falcon
    n("Tantive IV", True),  # 30
    n("Obi-Wan In Radiant VII"),  # 31
    n("Lady Luck"),  # 32
    n("Padme Naberrie", True),  # 33
    n("No Questions Asked", True),  # 34  NOA
    n("No Questions Asked", True),  # 35
    n("No Questions Asked", True),  # 36
    n("You've Got A Lot Of Guts Coming Here"),  # 37
    n("Imperial Atrocity", True),  # 38
    n("Imperial Atrocity", True),  # 39
    n("Seeking An Audience", True),  # 40
    n("Corellian Engineering Corporation", True),  # 41  CEC
    n("Wokling", True),  # 42
    n("Insurrection & Aim High"),  # 43
    n("Let The Wookiee Win", True),  # 44
    n("Let The Wookiee Win", True),  # 45
    n("All Wings Report In & Darklighter Spin"),  # 46
    n("All Wings Report In & Darklighter Spin"),  # 47
    n("Fallen Portal"),  # 48
    n("Heading For The Medical Frigate"),  # 49
    n("Antilles Maneuver & Rebel Reinforcements"),  # 50
    n("It's A Trap!"),  # 51
    n("Houjix & Out Of Nowhere"),  # 52
    n("Corellian Retort", True),  # 53
    n("Antilles Maneuver", True),  # 54
    n("Antilles Maneuver", True),  # 55
    n("Rebel Barrier"),  # 56
    n("Desperate Reach", True),  # 57
    n("Punch It"),  # 58
    n("Corellian Slip", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60  Agression
]

MHT_D2_LS_SHIELDS = [
    n("Planetary Defenses", True),  # 1
    n("Jabba's Prize", True),  # 2
    n("Ultimatum"),  # 3
    n("Let's Keep A Little Optimism Here", True),  # 4
    n("The Professor", True),  # 5
    n("Yavin Sentry", True),  # 6
    n("Don't Do That Again", True),  # 7
    n("Weapons Display", True),  # 8  Weapon Display
    n("Simple Tricks And Nonsense"),  # 9
    n("Chasm", True),  # 10
    n("Battle Plan"),  # 11
    n("Do, Or Do Not"),  # 12
    n("A Tragedy Has Occurred"),  # 13  Occured
    n("Your Ship?"),  # 14
    n("Your Insight Serves You Well", True),  # 15
]

MHT_D2_LS_ADD: list[tuple[str | None, bool]] = []


# --- Dark: day2_upright/d2p3_p12.png. Slavers. ---

MHT_D2_DS_SCAN = "extract/day2_upright/d2p3_p12.png"
MHT_D2_DS_PDF_PAGE = 12
MHT_D2_DS_SIDE = "Dark"
MHT_D2_DS_STARTING = n("Wookiee Slaving Operation / Indentured To The Empire")

MHT_D2_DS_RESERVE = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),  # 1  Wookiee Slaving Operations
    n("Kashyyyk"),  # 2
    n("Kashyyyk: Skyhook Platform"),  # 3
    n("Jabba's Sail Barge: Passenger Deck"),  # 4
    n("Nal Hutta"),  # 5
    n("Kashyyyk: Wookiee Slaving Camp"),  # 6
    n("Kashyyyk: Slaving Camp Headquarters"),  # 7
    n("Arica"),  # 8
    n("Outer Rim Scout"),  # 9  ORS
    n("Outer Rim Scout"),  # 10
    n("Outer Rim Scout"),  # 11
    n("Outer Rim Scout"),  # 12
    n("Keder The Black"),  # 13
    n("Ponda Baba", True),  # 14
    n("Ket Maliss, Shadow Killer"),  # 15  Ket Malis
    n("Prince Xizor"),  # 16
    n("Bossk", True),  # 17
    n("Ephant Mon"),  # 18
    n("Jabba The Hutt", True),  # 19
    n("Jabba The Hutt", True),  # 20
    n("Jango Fett, The Assassin"),  # 21
    n("Boba Fett, Prepared Hunter"),  # 22
    n("P-59"),  # 23
    n("Velken Tezeri", True),  # 24
    n("Dengar With Blaster Carbine", True),  # 25  EPP Dengar
    n("Dengar With Blaster Carbine", True),  # 26
    n("OOM-9", True),  # 27
    n("Probot"),  # 28
    n("Mercenary Pilot", True),  # 29
    n("IG-88, Renegade Droid"),  # 30
    n("Jabba's Sail Barge", True),  # 31
    n("Maul's Sith Infiltrator"),  # 32
    n("Slave I, Symbol Of Fear"),  # 33  Slave 1
    n("Jabba's Space Cruiser", True),  # 34
    n("Scum And Villainy"),  # 35  Villany
    n("Scum And Villainy"),  # 36
    n("Mercenary Slavers"),  # 37
    n("Tarkin's Bounty", True),  # 38  Where Are You Taking This... Thing? crossed
    n("Something Special Planned For Them", True),  # 39
    n("Hutt Bounty", True),  # 40
    n("Jabba's Haven", True),  # 41
    n("Den Of Thieves & Special Delivery"),  # 42
    n("Power Of The Hutt"),  # 43
    n("Sonic Bombardment", True),  # 44
    n("Sonic Bombardment", True),  # 45
    n("Sonic Bombardment", True),  # 46
    n("Short Range Fighters & Watch Your Back!"),  # 47
    n("Short Range Fighters & Watch Your Back!"),  # 48
    n("Cold Feet", True),  # 49
    n("Lightsaber Deficiency", True),  # 50
    n("Cease Fire"),  # 51
    n("Cease Fire"),  # 52
    n("Wookiee Subjugation"),  # 53
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 54
    n("Abyssin Ornament"),  # 55
    n("Nevar Yalnal"),  # 56
    n("Nevar Yalnal"),  # 57
    n("Sneak Attack", True),  # 58
    n("Sneak Attack", True),  # 59
    n("Knowledge And Defense", True),  # 60
]

MHT_D2_DS_SHIELDS = [
    n("There Is No Try"),  # 1
    n("Death Star Sentry", True),  # 2
    n("A Useless Gesture", True),  # 3
    n("You Cannot Hide Forever"),  # 4
    n("Fanfare", True),  # 5
    n("Come Here You Big Coward"),  # 6
    n("Battle Order"),  # 7
    n("Imperial Detention", True),  # 8
    n("Allegations Of Corruption"),  # 9
    n("Abyss", True),  # 10
    n("I Find Your Lack Of Faith Disturbing", True),  # 11
    n("Do They Have A Code Clearance?", True),  # 12
    n("Secret Plans"),  # 13
    n("Firepower", True),  # 14
    n("Resistance"),  # 15
]

MHT_D2_DS_ADD: list[tuple[str | None, bool]] = []


MHT_D2_LS_UNREAD: list[int] = []
MHT_D2_DS_UNREAD: list[int] = []
MHT_D2_LS_NO_DEST: list[str] = []
MHT_D2_DS_NO_DEST: list[str] = []

NOTES = """
Matthew Harrison-Trainor / MHT, 2014 Worlds Day 2, 2013 form, typed.
Light/Dark unchecked; side from cards.

LS d2p3_p11 WYSv. Watch Your Step (V).
Line 13 Yoda, GW → Yoda, Great Warrior.
Line 15 Romas → Romas 'Lock' Navander.
Line 34–36 NOA (V) → No Questions Asked (V).
Line 41 CEC (V) → Corellian Engineering Corporation (V).
Spaceport sites written without Corellia: prefix.
Line 7 Spaceport Scoundrel's Guild → Spaceport Scoundrels Guild.

DS d2p3_p12 Slavers.
Line 15 Ket Malis, Shadow Killer → Ket Maliss, Shadow Killer.
Line 25 EPP Dengar → Dengar With Blaster Carbine (V).
Line 38 Where Are You Taking This... Thing? crossed; Tarkin's Bounty (V) kept.
""".strip()


if __name__ == "__main__":
    assert len(MHT_D2_LS_RESERVE) == 60, len(MHT_D2_LS_RESERVE)
    assert len(MHT_D2_LS_SHIELDS) == 15, len(MHT_D2_LS_SHIELDS)
    assert len(MHT_D2_DS_RESERVE) == 60, len(MHT_D2_DS_RESERVE)
    assert len(MHT_D2_DS_SHIELDS) == 15, len(MHT_D2_DS_SHIELDS)
    print("transcribe_mht_day2.py", PLAYER)
    print("  Light WYSv reserve", len(MHT_D2_LS_RESERVE), "shields", len(MHT_D2_LS_SHIELDS), "unread", MHT_D2_LS_UNREAD, "no_dest", MHT_D2_LS_NO_DEST)
    print("  Dark Slavers reserve", len(MHT_D2_DS_RESERVE), "shields", len(MHT_D2_DS_SHIELDS), "unread", MHT_D2_DS_UNREAD, "no_dest", MHT_D2_DS_NO_DEST)
