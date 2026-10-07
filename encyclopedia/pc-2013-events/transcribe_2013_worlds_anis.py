#!/usr/bin/env python3
"""2013 World Championship Day 2 typed slang printout: Casey Anis LS+DS."""
from __future__ import annotations

PLAYER = "Casey Anis"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2013 Worlds Day 2 p07 Casey Anis LS.png"
DS_SCAN = "2013 Worlds Day 2 p08 Casey Anis DS.png"
NOTE = "Typed slang printout (not a handwritten Xerox form)."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Wes Janson"),
    n("Control & Tunnel Vision"),
    n("Seeking An Audience", True),
    n("Strikeforce", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Lucky Shot", True),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Let's Go Left", True, qty=3),
    n("Echo Base Garrison"),
    n("Launching The Assault"),
    n("Obi-Wan's Apparition", True),
    n("Menace Fades"),
    n("Rebel Gunrunner"),
    n("Imperial Atrocity", True),
    n("Flash Of Insight", True),
    n("Yub Yub, Commander"),
    n("Hear Me Baby, Hold Together", True),
    n("It's Not My Fault!", True),
    n("Rebel Leadership", True, qty=3),
    n("Houjix"),
    n("Escape Pod", True),
    n("Dual Laser Cannon", True),
    n("Rogue 4"),
    n("Rogue 3"),
    n("Rogue 2"),
    n("Rogue 1", qty=2),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Home One"),
    n("Shmi Skywalker"),
    n("Padmé Naberrie", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Dash Rendar", True),
    n("Threepio With His Parts Showing"),
    n("Derek 'Hobbie' Klivian"),
    n("Commander Wedge Antilles", True),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess"),
    n("Zev Senesca"),
    n("Tatooine: Jundland Wastes"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine"),
    n("Home One: War Room"),
    n("Tatooine: City Outskirts"),
    n("Maneuvering Flaps & Nick Of Time"),
    n("Wokling", True),
    n("Master Kenobi"),
    n("Communing"),
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Always Thinking With Your Stomach"),
    n("Protocol Failure"),
    n("They're Still Coming Through!"),
    n("Turn It Off! Turn It Off!"),
    n("Ephant Mon"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Mercenary Pilot"),
    n("Outer Rim Scout", qty=4),
    n("Jabba The Hutt", True),
    n("Velken Tezeri", True),
    n("Dr. Evazan"),
    n("Ponda Baba", True),
    n("Reegesk", True),
    n("Dengar With Blaster Carbine", True),
    n("P-59"),
    n("Bossk With Mortar Gun", True, qty=2),
    n("Ket Maliss, Shadow Killer"),
    n("Prince Xizor"),
    n("Probot"),
    n("4-LOM With Concussion Rifle"),
    n("Gela Yeens", True),
    n("Garindan", True),
    n("Hutt Bounty", True),
    n("Scum And Villainy"),
    n("Breached Defenses & Molator"),
    n("Zuckuss In Mist Hunter"),
    n("Jabba's Space Cruiser", True),
    n("Slave One, Symbol Of Fear"),
    n("Jabba's Sail Barge", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Skyhook Platform"),
    n("Nal Hutta"),
    n("Lightsaber Deficiency", True, qty=3),
    n("Imperial Barrier", qty=3),
    n("Abyssin Ornament", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Imbalance & Kintan Strider"),
    n("Jabba's Haven"),
    n("Power Of The Hutt"),
    n("Mercenary Slavers"),
    n("Wookiee Subjugation"),
    n("Den Of Thieves & Special Delivery"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Kashyyyk"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
