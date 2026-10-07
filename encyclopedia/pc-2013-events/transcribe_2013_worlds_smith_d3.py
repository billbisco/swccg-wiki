#!/usr/bin/env python3
"""2013 World Championship Day 3: Reid Smith Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = ""
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 13
DS_PAGE = 14
LS_SCAN = "2013 Worlds Day 3 p13 Reid Smith LS.png"
DS_SCAN = "2013 Worlds Day 3 p14 Reid Smith DS.png"
LS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name RSmith. Username blank. LIGHT. Deck title itch. Dest Reid Smith. "
    "Do not dest as Day 2 RSmith (Conway East / Buck Faston). "
    "Do not inject Username 3MW0J8; the Day 3 Username box is blank. "
    "There Is Good In Him / I Can Save dested There Is Good In Him / I Can Save Him. "
    "Endor: Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Don't Tread On Me dested Don't Tread On Me. "
    "Boon Bous dested Boushh. "
    "Republic Gunship Wing dested Republic Gunship Wing as written. "
    "Sense (Prem) dested Sense. "
    "Sorry About The Mess + Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Mace Windu, Master Of The Order checkbox empty dested without (V). "
    "Jabba's Prize written in shields dested as a shield. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name RSmith. Username blank. DARK. Deck title scratch (almost). Dest Reid Smith. "
    "Do not dest as Day 2 RSmith (Conway East / Buck Faston). "
    "Wookiee Slaving Operation / Indentured dested "
    "Wookiee Slaving Operation / Indentured To The Empire. "
    "Kashyyyk Slaving Camp HQ dested Kashyyyk: Slaving Camp Headquarters. "
    "Den of Thieves and Special Delivery dested Den Of Thieves & Special Delivery. "
    "Begin Landing Your Troops and we don't path dested Begin Landing Your Troops "
    "(checkbox empty; not Begin Landing Your Troops & The Dark Path). "
    "Evader and Monnok dested Evader & Monnok. "
    "Kashyyyk Wookiee Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Jabba's Sail Barge dested Jabba's Sail Barge. "
    "Jabba's Space Cruiser dested Jabba's Space Cruiser. "
    "Jabba Sail Barge Passenger Deck dested Jabba's Sail Barge: Passenger Deck. "
    "Scum and Vilary dested Scum And Villainy. "
    "Ket Maliss Shadow Killer dested Ket Maliss, Shadow Killer. "
    "4Lom with Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Breached Defenses and Molator dested Breached Defenses & Molator. "
    "IG-88 With Riot Gun dested IG-88 With Riot Gun. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Ghhhk and Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "The Mandalorian Father of Fett dested The Mandalorian. "
    "Shield 1 Battle struck then Firepower dested Firepower. "
    "Death Star Sentry written in shields dested as a shield. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Clash Of Sabers", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Coruscant: Jedi Council Chamber", True),
    n("Padme Naberrie", True),
    n("Dark Approach", True, qty=2),
    n("Draw Their Fire"),
    n("Home One"),
    n("Boushh", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Naboo: Battle Plains"),
    n("Republic Gunship Wing"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sense", qty=2),
    n("Seeking An Audience", True),
    n("A Jedi's Resilience", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection", qty=2),
    n("Rebel Barrier", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Nabrun Leids"),
    n("Rebel Leadership", True, qty=2),
    n("Imperial Atrocity", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Mace Windu, Master Of The Order"),
    n("Escape Pod", True),
    n("Corran Horn"),
    n("Grimtaash"),
    n("Houjix"),
    n("Home One: War Room"),
    n("Leia, Rebel Princess"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Crush The Rebellion"),
    n("Begin Landing Your Troops"),
    n("Kashyyyk: Skyhook Platform"),
    n("Outer Rim Scout", qty=5),
    n("Sonic Bombardment", True, qty=3),
    n("Prince Xizor"),
    n("Zuckuss In Mist Hunter"),
    n("Imperial Barrier", qty=3),
    n("Jabba The Hutt", True),
    n("Dengar With Blaster Carbine", True),
    n("Lightsaber Deficiency", True, qty=3),
    n("Dr. Evazan"),
    n("Gardulla The Hutt", True),
    n("P-59"),
    n("Evader & Monnok"),
    n("Hutt Bounty", True),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Jabba's Sail Barge", True),
    n("Lady Valarian"),
    n("Jabba's Space Cruiser", True),
    n("Look Sir, Droids"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Mercenary Pilot", True),
    n("Ponda Baba", True),
    n("Scum And Villainy"),
    n("Bossk With Mortar Gun", True),
    n("Ket Maliss, Shadow Killer"),
    n("4-LOM With Concussion Rifle"),
    n("Breached Defenses & Molator"),
    n("Ephant Mon"),
    n("IG-88 With Riot Gun"),
    n("Garindan", True),
    n("Boba Fett, Prepared Hunter"),
    n("Probot"),
    n("Reegesk", True),
    n("Slave I, Symbol Of Fear"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("The Mandalorian"),
    n("Abyssin Ornament"),
    n("Protocol Failure"),
    n("Velken Tezeri", True),
    n("Bane Malar", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Battle Order", True),
    n("Secret Plans", True),
    n("Allegations Of Corruption", True),
    n("Abyss", True),
    n("Fanfare", True),
    n("Come Here You Big Coward", True),
    n("A Useless Gesture", True),
    n("There Is No Try", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
