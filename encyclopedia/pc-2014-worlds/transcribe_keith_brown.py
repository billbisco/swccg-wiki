#!/usr/bin/env python3
"""Day 2 Xerox transcription: Keith Brown (DJK1).

Source scans: extract/day2/d2p1_p05.png (Dark, unnamed Wookiee Slaving
Operations) and extract/day2/d2p1_p06.png (Light, DJK1, Republic At War /
Muunilinst). 2010 form. p05 name/deck/side boxes blank; paired with p06
on handwriting (X-in-box (V) ticks, slant) and adjacent pages.
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Keith Brown"
USERNAME = "DJK1"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p1_p06.png"
DS_SCAN = "extract/day2/d2p1_p05.png"
PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 6
DS_PDF_PAGE = 5
LS_STARTING = ("Republic At War / Aggressive Negotiations", True)
DS_STARTING = ("Wookiee Slaving Operation / Indentured To The Empire", True)


# --- Light: d2p1_p06.png. LIGHT/DARK unchecked. RAW / Muunilinst. ---

LS_RESERVE = [
    n("Republic At War / Aggressive Negotiations", True),  # 1
    n("Geonosis: Forward Command Center", True),  # 2
    n("Begun, The Clone War Has", True),  # 3
    n("Heading For The Medical Frigate"),  # 4  HFTMF
    n("Rogue Squadron Tactics", True),  # 5
    n("Nick Of Time", True),  # 6
    n("Wokling", True),  # 7
    n("Assault On Muunilinst", True),  # 8
    n("Muunilinst: City Of Harnaidan", True),  # 9
    n("Muunilinst: Harnaidan Plains", True),  # 10
    n("Muunilinst: Republic Landing Site", True),  # 11
    n("Rebel Cell - Hidden Landing Site", True),  # 12
    n("Dressel", True),  # 13
    n("Lady Luck", True),  # 14
    n("Alderaan Consular Ship", True),  # 15  Alderaan Consular Ship
    n("Acclamator-Class Assault Ship", True),  # 16
    n("Republic Gunship Wing", True),  # 17
    n("Low-Altitude Assault Transport", True),  # 18
    n("AT-RT", True),  # 19
    n("AT-RT", True),  # 20
    n("AT-RT", True),  # 21
    n("AT-RT", True),  # 22
    n("AT-RT", True),  # 23
    n("AT-RT", True),  # 24
    n("AT-RT", True),  # 25
    n("AT-RT", True),  # 26
    n("Dual Laser Cannon", True),  # 27
    n("Dual Laser Cannon", True),  # 28
    n("Dual Laser Cannon", True),  # 29
    n("Dual Laser Cannon", True),  # 30
    n("Dual Laser Cannon", True),  # 31
    n("Lando Calrissian, Unlikely Hero", True),  # 32
    n("Lando Calrissian, Unlikely Hero", True),  # 33
    n("Dash Rendar", True),  # 34
    n("Jaina Solo", True),  # 35  written Jaina Solo
    n("Anakin Skywalker, Padawan Learner", True),  # 36  Anakin Skywalker, PL
    n("Obi-Wan Kenobi, Jedi Knight", True),  # 37  Obi-Wan Kenobi, JK
    n("Plo Koon", True),  # 38
    n("Qui-Gon Jinn With Lightsaber"),  # 39
    n("Mace Windu, Master Of The Order", True),  # 40
    n("Menace Fades"),  # 41
    n("Strikeforce", True),  # 42  Strikeforce
    n("Imperial Atrocity", True),  # 43
    n("Imperial Atrocity", True),  # 44
    n("Sorry About The Mess"),  # 45
    n("Sabotage", True),  # 46
    n("Slight Weapons Malfunction", True),  # 47
    n("Slight Weapons Malfunction"),  # 48
    n("Hear Me Baby, Hold Together", True),  # 49
    n("Desperate Reach", True),  # 50
    n("Desperate Reach", True),  # 51
    n("Rebel Barrier"),  # 52
    n("Houjix & Out Of Nowhere"),  # 53  Houjix & OON
    n("Houjix & Out Of Nowhere"),  # 54
    n("Out Of Commission & Transmission Terminated"),  # 55  OOC & TT
    n("Sorry About The Mess & Blaster Proficiency"),  # 56  SATM & BP
    n("All Wings Report In & Darklighter Spin"),  # 57  AWRI & DS
    n("Away Put Your Weapon", True),  # 58
    n("Desperate Tactics"),  # 59
    n("Anger, Fear, Aggression", True),  # 60  AFA
]

LS_SHIELDS = [
    n("Affect Mind", True),  # 1
    n("He Can Go About His Business", True),  # 2  He Can Go About his Biz
    n("Wise Advice"),  # 3
    n("Aim High"),  # 4
    n("The Professor", True),  # 5
    n("Battle Plan"),  # 6
    n("Don't Do That Again", True),  # 7  DDTA
    n("Do, Or Do Not"),  # 8  DODN
    n("Your Insight Serves You Well", True),  # 9  YISYW
    n("Weapons Display", True),  # 10
    n("Ultimatum"),  # 11
    n("Simple Tricks And Nonsense"),  # 12
]

LS_ADD = [
    n("Yavin Sentry", True),  # 1
    n("Chasm", True),  # 2
    n("A Tragedy Has Occurred"),  # 3
]


# --- Dark: d2p1_p05.png. LIGHT/DARK unchecked. Wookiee Slaving Ops. ---

DS_RESERVE = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),  # 1
    n("Kashyyyk"),  # 2
    n("Mercenary Slavers", True),  # 3
    n("Kashyyyk: Slaving Camp Headquarters", True),  # 4  Slaving Camp HQ
    n("Wookiee Subjugation", True),  # 5
    n("Power Of The Hutt"),  # 6
    n("Jabba's Haven", True),  # 7
    n("Den Of Thieves & Special Delivery", True),  # 8  Den of Thieves & S.D.
    n("Kashyyyk: Skyhook Platform", True),  # 9
    n("Kashyyyk: Wookiee Slaving Camp", True),  # 10
    n("Nal Hutta"),  # 11
    n("Jabba's Sail Barge: Passenger Deck"),  # 12  Jabba's Sail Barge: PD
    n("Jabba's Space Cruiser", True),  # 13
    n("Slave I, Symbol Of Fear", True),  # 14
    n("Maul's Sith Infiltrator"),  # 15
    n("Jabba's Sail Barge", True),  # 16
    n("OOM-9", True),  # 17
    n("4-LOM With Concussion Rifle"),  # 18
    n("IG-88 With Riot Gun"),  # 19
    n("P-59"),  # 20
    n("Garindan", True),  # 21
    n("Garindan", True),  # 22
    n("Mercenary Pilot", True),  # 23
    n("Outer Rim Scout"),  # 24
    n("Outer Rim Scout"),  # 25
    n("Outer Rim Scout"),  # 26
    n("Outer Rim Scout"),  # 27
    n("Velken Tezeri", True),  # 28
    n("Ponda Baba", True),  # 29
    n("Dengar With Blaster Carbine", True),  # 30
    n("Bossk", True),  # 31
    n("Lady Valarian", True),  # 32
    n("Ephant Mon"),  # 33
    n("Jabba The Hutt", True),  # 34
    n("Jabba The Hutt", True),  # 35
    n("Prince Xizor", True),  # 36  (V) box filled/scribble
    n("Mara Jade With Lightsaber", True),  # 37
    n("Boba Fett, Prepared Hunter", True),  # 38
    n("Jango Fett, The Assassin", True),  # 39
    n("Dengar In Punishing One", True),  # 40  Protocol Droid crossed
    n("Ability, Ability, Ability", True),  # 41
    n("Something Special Planned For Them", True),  # 42
    n("Hutt Bounty", True),  # 43
    n("Scum And Villainy"),  # 44
    n("Scum And Villainy"),  # 45
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 46  Ghhhk & TRWEU
    n("Tarkin's Orders"),  # 47
    n("Elis Helrot"),  # 48
    n("Cold Feet", True),  # 49
    n("Lightsaber Deficiency", True),  # 50
    n("Defensive Fire & Hutt Smooch"),  # 51  written Hutt Smash
    n("Defensive Fire & Hutt Smooch"),  # 52
    n("Sneak Attack", True),  # 53
    n("Sneak Attack", True),  # 54
    n("Short Range Fighters & Watch Your Back!"),  # 55  SRF & WYB
    n("Short Range Fighters & Watch Your Back!"),  # 56
    n("Sonic Bombardment", True),  # 57
    n("Sonic Bombardment", True),  # 58
    n("Sonic Bombardment", True),  # 59
    n("Knowledge And Defense", True),  # 60  K & D
]

DS_SHIELDS = [
    n("Firepower", True),  # 1
    n("Secret Plans"),  # 2
    n("Resistance"),  # 3
    n("I Find Your Lack Of Faith Disturbing", True),  # 4
    n("Fanfare", True),  # 5
    n("A Useless Gesture", True),  # 6  AUG
    n("You Cannot Hide Forever", True),  # 7  YCHF
    n("Come Here You Big Coward"),  # 8  CHYBC
    n("Oppressive Enforcement"),  # 9
    n("There Is No Try"),  # 10  TINT
    n("Allegations Of Corruption"),  # 11  Allegations
    n("Abyss", True),  # 12
]

DS_ADD = [
    n("Battle Order"),  # 1
    n("Death Star Sentry"),  # 2
    n("We'll Let Fate-a Decide, Huh?"),  # 3  We'll Let Fate Decide
]


LS_UNREAD: list[int] = []
DS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []
DS_NO_DEST: list[str] = []

NOTES = """
Keith Brown / DJK1, 2014 Worlds Day 2, 2010 form.
Paired p05 Dark (name/deck/side blank) with p06 Light (Name DJK1).
Light/Dark unchecked on both; side from cards. Same X-in-box (V) ticks.

LS d2p1_p06 Republic At War (V). Deck name blank.
15 Alderaan Consular Ship. 17 Republic Gunship Wing. 35 Jaina Solo.
53-54 Houjix & OON. 55 OOC & TT. 56 SATM & BP. 57 AWRI & DS.

DS d2p1_p05 Wookiee Slaving Ops (V). 12 Sail Barge: PD = Passenger Deck.
40 Protocol Droid crossed; Dengar In Punishing One kept.
36 Prince Xizor (V) box filled. 51-52 written Hutt Smash -> Hutt Smooch combo.
""".strip()


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 12, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 12, len(DS_SHIELDS)
    print("file", __file__)
    print("LS", PLAYER, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
    print("DS", PLAYER, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
