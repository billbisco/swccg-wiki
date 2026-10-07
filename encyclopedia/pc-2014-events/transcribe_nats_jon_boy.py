#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Jon Boy.

Source: Nationals-2014-day-1.pdf pages 23–24 (2010 form).
Name Jon Boy dest as written.
"""
from __future__ import annotations

PLAYER = "Jon Boy"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2014 US Nationals Day 1 p23 Jon Boy LS.png"
DS_SCAN = "2014 US Nationals Day 1 p24 Jon Boy DS.png"
NOTE = "Handwritten 2010 Xerox. Name Jon Boy dested as written."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jon Boy. Username blank. "
    "Deck name Make no Sense, this does. IITFYS dested It Is The Future You See / A Tremor In The Force. "
    "Do or do not & Wise Advice dested Do, Or Do Not & Wise Advice. "
    "Battle Plan & Draw Their Fire dested Battle Plan & Draw Their Fire. "
    "Lando's Luxury Yacht dested Lady Luck. SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Han, Chewie, & The Falcon dested Han, Chewie, And The Falcon. "
    "AFA dested Anger, Fear, Aggression. Unique overcounts sheet-accurate "
    "(Imperial Atrocity x2, Luke Skywalker, Strong In The Force x2, Mace Windu x3, "
    "Let The Wookiee Win x3, Rebel Leadership x3, Artoo-Detoo In Red 5 x2, "
    "Wesa Gotta Grand Army x3, A Jedi's Resilience x2, Luke Skywalker, Jedi Knight x2, "
    "Master Qui-Gon x2, Escape Pod x2, Speak With The Jedi Council x2). (V) from checkbox. "
    "NO_DEST (2014 index): What Are You Tryin' To Push On Us?."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Jon Boy. Username blank. "
    "Deck name Eating wookies are chewle. Wookiee Slaving Operation dested "
    "Wookiee Slaving Operation / Indentured To The Empire. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Ghhhk & Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "P-59 dested P-59. K+D dested Knowledge And Defense. Unique overcounts sheet-accurate "
    "(Imperial Barrier x2, Sonic Bombardment x3, Lightsaber Deflection x2, "
    "Outer Rim Scout x5, Scum & Villainy x2, Ponda Baba x2). (V) from checkbox. "
    "Jabba's Palace dested Tatooine: Jabba's Palace. "
    "NO_DEST (2014 index): Rane Kantoo (V); Lightsaber Deflection (V); Evading The Hutt; Daut Nund (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Home One: War Room"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True, qty=2),
    n("What Are You Tryin' To Push On Us?"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Mace Windu", True, qty=3),
    n("Blaster Deflection", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Clash Of Sabers"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Rebel Leadership", True, qty=3),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Luke's Lightsaber"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Jedi Levitation", True),
    n("Hear Me Baby, Hold Together", True),
    n("A Jedi's Resilience", qty=2),
    n("Jedi Lightsaber", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Speak With The Jedi Council"),
    n("Master Qui-Gon", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Lady Luck", True),
    n("Seeking An Audience", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Home One"),
    n("Escape Pod", True, qty=2),
    n("Speak With The Jedi Council"),
    n("Naboo: Battle Plains"),
    n("Admiral Ackbar"),
    n("Weapon Levitation", True),
    n("Houjix"),
    n("Han, Chewie, And The Falcon", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Aim High", True),
    n("A Tragedy Has Occurred", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Ultimatum", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Planetary Defenses", True),
]
LS_ADD = [
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind"),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Kashyyyk"),
    n("Wookiee Slaving Operation / Indentured To The Empire", True),
    n("Kashyyyk: Slaving Camp Headquarters", True),
    n("Den Of Thieves & Special Delivery", True),
    n("Wookiee Subjugation", True),
    n("Jabba's Haven", True),
    n("Power Of The Hutt"),
    n("Mercenary Slavers", True),
    n("Rane Kantoo", True),
    n("Sneak Attack", True),
    n("Jabba The Hutt"),
    n("Imperial Barrier", qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("Sonic Bombardment", True, qty=3),
    n("Cease Fire!"),
    n("Kashyyyk: Forest Maze", True),
    n("Wounded Warrior"),
    n("Lightsaber Deflection", True, qty=2),
    n("4-LOM With Concussion Rifle"),
    n("Jabba's Space Cruiser", True),
    n("Evading The Hutt"),
    n("Bossk", True),
    n("Outer Rim Scout", qty=5),
    n("Abyssin Ornament"),
    n("Nal Hutta"),
    n("IG-88 With Riot Gun"),
    n("Ket Maliss, Shadow Killer", True),
    n("Ree-Yees", True),
    n("Scum And Villainy", True, qty=2),
    n("Garindan", True),
    n("Kashyyyk: Skyhook Platform", True),
    n("Jabba's Sail Barge", True),
    n("Ephant Mon"),
    n("Slave I, Symbol Of Fear", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Hutt Bounty", True),
    n("Jango Fett, The Assassin"),
    n("Mercenary Pilot", True),
    n("Prince Xizor"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Tatooine: Jabba's Palace"),
    n("Probe Droid"),
    n("Dengar With Blaster Carbine", True),
    n("Lady Valarian"),
    n("Daut Nund", True),
    n("Ponda Baba", True, qty=2),
    n("Velken Tezeri", True),
    n("P-59"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Come Here You Big Coward", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Secret Plans"),
]
DS_ADD = [
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Battle Order", True),
]
