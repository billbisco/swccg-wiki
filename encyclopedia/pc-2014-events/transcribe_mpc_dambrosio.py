#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Mike D'Ambrosio.

Source: MPC-2014-Day-1-Main-Event.pdf pages 37–38 (2013 form, 15 shields).
Username blank. Sheet Mike d'Amario.
"""
from __future__ import annotations

PLAYER = "Mike D'Ambrosio"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 38
DS_PAGE = 37
LS_SCAN = "2014 Match Play Championship Day 1 Mike D'Ambrosio LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Mike D'Ambrosio DS.png"
NOTE = "Handwritten 2013 Xerox form. Sheet Mike d'Amario dested Mike D'Ambrosio."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Mike d'Amario dested Mike D'Ambrosio. Username blank. "
    "LIGHT/DARK empty. IITFYS (V) dested It Is The Future You See (V) (starting Epic "
    "Event). Lando's Luxury Yacht dested Lady Luck. SATM & BP dested Sorry About The Mess "
    "& Blaster Proficiency. Artoo in Red 5 dested Artoo-Detoo In Red 5. Unique overcounts "
    "sheet-accurate (Master Qui-Gon (V) x2, Luke Skywalker, Strong In The Force x2, Mace "
    "Windu (V) x2, Let The Wookiee Win (V) x3, A Jedi's Resilience x2, Speak With The Jedi "
    "Council x2, Wesa Gotta Grand Army x3, Rebel Leadership (V) x3, Imperial Atrocity (V) "
    "x2, Clash Of Sabers x2, Escape Pod (V) x2, Luke Skywalker, Jedi Knight x2). What Are "
    "You Trying To Push On Us dested What're You Tryin' To Push On Us?. "
    "(V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Mike d'Amario dested Mike D'Ambrosio. Username blank. "
    "Imperial Occupation / Imperial Control (V) dested Imperial Occupation (V) / Imperial "
    "Control (V). Jango FOF dested Jango Fett, The Assassin. Control + Set For Stun dested "
    "Control & Set For Stun. Maarek Stele dested Maarek Stele, The Emperor's Reach. Size "
    "Passage dested Hoth: Ice Cave as written (NO_DEST). 509th Super Commandos dested "
    "501st Legion as written (NO_DEST). Unique overcounts sheet-accurate (Cyclone Walker "
    "x3, We're In "
    "Attack Position Now x2, A Dark Time For The Rebellion (V) x2, AT-AT Deployment "
    "Platform x2, Blizzard 4 x2, Trample x2, Conquest (V) x2, Imperial Command x3). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("It Is The Future You See", True),
    n("Home One: War Room"),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("Hear Me Baby, Hold Together", True),
    n("Yavin 4: Massassi War Room", True),
    n("Han, Chewie, And The Falcon", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Master Qui-Gon", True, qty=2),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Leia, Rebel Princess"),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Lady Luck", True),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon's Lightsaber"),
    n("Houjix"),
    n("Let The Wookiee Win", True, qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Jedi Levitation", True),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection"),
    n("Clash Of Sabers", qty=2),
    n("Corran Horn"),
    n("Artoo-Detoo In Red 5"),
    n("Escape Pod", True, qty=2),
    n("Weapon Levitation"),
    n("What're You Tryin' To Push On Us?"),
    n("Grimtassh"),
    n("Naboo: Battle Plains"),
    n("Hoth: Echo Command Center"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("There Is Another", True),
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Chasm"),
    n("Weapons Display"),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Ice Cave"),
    n("Imperial Decree", True),
    n("Cold Feet", True),
    n("Hoth: Ice Plains", True),
    n("Hoth"),
    n("Walker Garrison", True),
    n("Imperial Decree"),
    n("You May Start Your Landing", True),
    n("All Power To Weapons", True),
    n("Endor Shield", True),
    n("Prepared Defenses", True),
    n("General Veers", True),
    n("Executor"),
    n("Cyclone Walker", qty=3),
    n("We're In Attack Position Now", qty=2),
    n("Image Of The Dark Lord", True),
    n("U-3PO"),
    n("Admiral Motti", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("AT-AT Cannon", True),
    n("AT-AT Deployment Platform", qty=2),
    n("Blizzard 4", qty=2),
    n("Trample", qty=2),
    n("Garindan", True),
    n("Conquest", True, qty=2),
    n("Maarek Stele, The Emperor's Reach"),
    n("General Tagge"),
    n("Do They Have A Code Clearance?", True),
    n("Admiral Piett"),
    n("Close Call", True),
    n("Grand Moff Tarkin", True),
    n("Imperial Command", qty=3),
    n("Tempest 1"),
    n("Commander Igar"),
    n("Target The Main Generator", True),
    n("Hoth Blockade"),
    n("No Escape"),
    n("Hoth: Defensive Perimeter"),
    n("Victory"),
    n("Blizzard 2", True),
    n("501st Legion"),
    n("Darth Vader", True),
    n("Jango Fett, The Assassin"),
    n("Hoth: Mountains"),
    n("Grand Admiral Thrawn"),
    n("Control & Set For Stun"),
    n("Crash Landing"),
    n("Alert My Star Destroyer"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("After Her!", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Firepower"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("Leave Them To Me"),
]
DS_ADD = []
