#!/usr/bin/env python3
"""2013 World Championship Day 2: Justin Carulli 2012 Print Form LS+DS."""
from __future__ import annotations

PLAYER = "Justin Carulli"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 24
DS_PAGE = 23
LS_SCAN = "2013 Worlds Day 2 p24 Justin Carulli LS.png"
DS_SCAN = "2013 Worlds Day 2 p23 Justin Carulli DS.png"
LS_NOTE = (
    "Handwritten 2012 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Justin Carulli. Username blank. Event Worlds 13. Deck title Kessel. LIGHT. "
    "There Is Good In Him / I Can Save Him dested There Is Good In Him / I Can Save Him. "
    "Endor: Chief's Hut dested Endor: Chief Chirpa's Hut. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Sorry About The Mess / Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Mace Windu, Master Of The Order dested Mace Windu, Master Of The Order. "
    "Lines 36–37 struck Set For Stun dested omitted. "
    "Line 58 struck dested omitted. "
    "Don't Tread On Me dested Don't Tread On Me. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army. "
    "Qui-Gon Jinn w/ Lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "Obi-Wan w/ Lightsaber dested Obi-Wan With Lightsaber. "
    "Han w/ Heavy Blaster Pistol dested Han With Heavy Blaster Pistol. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2012 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Justin Carulli. Username blank. Event Worlds 13. Deck title Endor. DARK. "
    "Kessel: Admin Office dested Kessel: Spice Mines - Administrator's Office. "
    "I'll Take Them Myself dested I'll Take Them Myself. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Kessel: Spice Mines Prison dested Kessel: Spice Mines - Prison. "
    "Short Range Fighters / Watch Your Back dested "
    "Short Range Fighters & Watch Your Back!. "
    "The Mandalorian, Father of Fett dested The Mandalorian. "
    "Moff Disra, Kessel Admin dested as written. "
    "Black Sun Fleet dested Black Sun Fleet. "
    "Spice Mine Ops dested Spice Mine Operations. "
    "Galen, Secret Apprentice dested Galen, Secret Apprentice. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Dr. Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Death Star Sentry dested Death Star Sentry. "
    "We'll Let Fate-A Decide Huh dested We'll Let Fate-A Decide, Huh?. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him", True),
    n("Anger, Fear, Aggression"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)", True),
    n("Luke Skywalker, Rebel Scout"),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("A Jedi's Resilience"),
    n("A Jedi's Resilience", True),
    n("Escape Pod", True),
    n("Blaster Deflection", qty=2),
    n("Yavin 4: Massassi War Room", True),
    n("Speak With The Jedi Council"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Chewie, Enraged"),
    n("Chewie, Enraged", True),
    n("Seeking An Audience"),
    n("Mace Windu, Master Of The Order"),
    n("Rebel Barrier", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Draw Their Fire"),
    n("Grimtaash"),
    n("Nabrun Leids"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Houjix", True),
    n("Smoke Screen", qty=2),
    n("Naboo: Battle Plains"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Corran Horn", True),
    n("Admiral Ackbar"),
    n("Clash Of Sabers", qty=2),
    n("Sense"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Wesa Gotta Grand Army"),
    n("Wesa Gotta Grand Army", True),
    n("Rebel Leadership", True, qty=2),
    n("Imperial Atrocity"),
    n("Luke Skywalker, Jedi Knight", True),
    n("Home One: War Room", True),
    n("Dark Approach", True),
    n("Don't Tread On Me", True),
    n("Padme Naberrie"),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("Jabba's Prize", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Wise Advice"),
    n("Aim High"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Knowledge And Defense", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Combat Readiness"),
    n("I'll Take Them Myself", True),
    n("Ni Chuba Na??"),
    n("Gift Of The Master"),
    n("Boba Fett, Prepared Hunter", True),
    n("Garindan"),
    n("Kessel: Spice Mines - Prison"),
    n("Sidious' Lightsaber"),
    n("Force Lightning"),
    n("Lord Sidious", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Victory"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Dark Maneuvers", qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Sonic Bombardment"),
    n("Sonic Bombardment", True, qty=2),
    n("Why Didn't You Tell Me?", True),
    n("Force Push", True),
    n("Imperial Justice"),
    n("Galen, Secret Apprentice", qty=3),
    n("Alter", True),
    n("Lightsaber Deficiency"),
    n("Sense"),
    n("Sense", True),
    n("Cold Feet", True),
    n("Close Call"),
    n("Kessel Surveillance System"),
    n("Blizzard 4"),
    n("Maul's Sith Infiltrator"),
    n("Emperor Palpatine", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("The Mandalorian", True),
    n("Force Field"),
    n("Force Field", True),
    n("Sniper & Dark Strike"),
    n("Moff Disra, Kessel Admin"),
    n("Arica"),
    n("Imperial Barrier", True),
    n("Cloud City: Security Tower"),
    n("Black Sun Fleet"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Protocol Failure", True),
    n("Darth Maul"),
    n("Spice Mine Operations", True),
    n("Blaster Rack"),
    n("Galen's Lightsaber, Vader's Gift"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-A Decide, Huh?"),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement", True),
    n("Firepower"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Death Star Sentry"),
    n("Come Here You Big Coward"),
    n("Battle Order", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption", True),
    n("Abyss", True),
]
DS_ADD = []
