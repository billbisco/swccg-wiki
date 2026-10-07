#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Brian Herold Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 19
DS_PAGE = 20
LS_SCAN = "2013 SoCal Grand Prix Day 1 p19 Brian Herold LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p20 Brian Herold DS.png"
LS_NOTE = (
    "Handwritten Xerox form. Event SoCal Grand Prix, 26 October 2013. "
    "YISYW → Your Insight Serves You Well. ankling → Wokling. "
    "Honor (OTJ) → Honor Of The Jedi. Sorry About The Mess & BP → "
    "Sorry About The Mess & Blaster Proficiency. Let's Keep A Lil Optimism Here → "
    "Let's Keep A Little Optimism Here. Simple Trix & Nonsense → Simple Tricks And Nonsense. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Xerox form. Wookiee Slaving Operations → Wookiee Slaving Operation / "
    "Indentured To The Empire. Kashyyyk: Slaving Camp HQ → Kashyyyk: Slaving Camp Headquarters. "
    "Bossk w Mortar Gun → Bossk With Mortar Gun. Ket Maliss, Shadow Killer as written. "
    "ReegesK → Ree-Yees. Dengar w Blaster Carbine → Dengar With Blaster Carbine. "
    "Mandalorian Father of Fett → Jango Fett, The Assassin. Slave 1 Symbol of Fear → "
    "Slave I, Symbol Of Fear. Branched Defenses & Malater → Breached Defenses & Molator. "
    "Scum & Villainy → Scum And Villainy. Dr. E → Dr. Evazan. "
    "Knowledge & Defense → Knowledge And Defense. YCHF → You Cannot Hide Forever. "
    "We'll Let Fate-a Decide, Huh? as written. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Heading For The Medical Frigate"),
    n("Your Insight Serves You Well"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Home One: War Room"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: War Room", True),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Corran Horn"),
    n("Luke Skywalker, Jedi Knight"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Maris Brood, Fallen Jedi"),
    n("Lando Calrissian, Scoundrel"),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Republic Gunship Wing", qty=2),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Guardian's Lightsaber"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Honor Of The Jedi"),
    n("Projection Of A Skywalker"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("A Jedi's Resilience"),
    n("Clash Of Sabers"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Grimtaash"),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Sense", qty=3),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Battle Plan", True),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("The Professor", True),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation", True),
    n("Power Of The Hutt"),
    n("Jabba's Haven"),
    n("Mercenary Slavers"),
    n("Nal Hutta"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Skyhook Platform"),
    n("Jabba The Hutt", True),
    n("Ephant Mon"),
    n("Prince Xizor"),
    n("Bossk With Mortar Gun", True),
    n("Lady Valarian"),
    n("Ket Maliss, Shadow Killer"),
    n("Garindan", True),
    n("Ponda Baba", True),
    n("Velken Tezeri", True),
    n("Ree-Yees", True),
    n("Dengar With Blaster Carbine", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Mercenary Pilot"),
    n("Outer Rim Scout", qty=5),
    n("4-LOM With Concussion Rifle"),
    n("Probot"),
    n("P-59"),
    n("Slave I, Symbol Of Fear"),
    n("Jabba's Space Cruiser", True),
    n("Zuckuss In Mist Hunter"),
    n("Jabba's Sail Barge", True),
    n("Laser Cannon Battery"),
    n("Hutt Bounty", True),
    n("Ability, Ability, Ability"),
    n("Protocol Failure"),
    n("Scum And Villainy"),
    n("Breached Defenses & Molator"),
    n("Imperial Barrier", qty=3),
    n("Lightsaber Deficiency", True, qty=3),
    n("Sonic Bombardment", True, qty=4),
    n("Abyssin Ornament", True, qty=2),
    n("Imbalance & Kintan Strider"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Dr. Evazan"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Oppressive Enforcement"),
]
DS_ADD = [
    n("Secret Plans"),
    n("Battle Order", True),
    n("Fanfare", True),
]
