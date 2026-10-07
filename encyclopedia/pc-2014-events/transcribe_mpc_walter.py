#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Ryan Walter.

Source: MPC-2014-Day-1-Main-Event.pdf pages 116–117 (2013 form, 15 shields).
Name Ryan Walter. Username RyanNCWA.
"""
from __future__ import annotations

PLAYER = "Ryan Walter"
USERNAME = "RyanNCWA"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 116
DS_PAGE = 117
LS_SCAN = "2014 Match Play Championship Day 1 Ryan Walter LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Ryan Walter DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Ryan Walter. Username RyanNCWA. LIGHT checked. "
    "Hoth: Main Power Generators start. Tauntaun Skreej dested Tauntaun. "
    "Thrown Back dested Thrown Back. Yoda GW dested Yoda, Great Warrior. "
    "Princess Leia, Last Scion dested Princess Leia, Last Scion. "
    "AFA dested Anger, Fear, Aggression. HMTMF dested Han, Chewie, And The Falcon. "
    "Guardian's Lightsaber dested Guardian's Lightsaber. "
    "Tatooine (Premiere) dested Tatooine. Han's Heavy Blaster dested Han's Heavy Blaster Pistol. "
    "NO_DEST Republic Gunship (V). "
    "Shields 11–15 empty. Unique overcounts sheet-accurate (Jedi Lightsaber x3, Houjix x2, "
    "Republic Gunship (V) x2, Sense x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Ryan Walter. Username RyanNCWA. Email [redacted]. "
    "DARK checked. Fondor start. Galen Marek, Starkiller dested Galen Marek, Starkiller. "
    "Grievous, Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Dooku's Saber dested Dooku's Lightsaber. Knowledge & Defense dested Knowledge And Defense. "
    "Boba Fett, Relentless Bounty Hunter dested Boba Fett, Relentless Bounty Hunter. "
    "Jango Fett, The Assassin dested Jango Fett, The Assassin. "
    "SFS 9.3 Laser Cannons dested SFS L-s9.3 Laser Cannons. "
    "Grievous' Sabers dested Grievous' Lightsabers. "
    "NO_DEST Dr. Evazan's Blaster. "
    "Reactor Terminal listed in main and in shields, sheet-accurate. "
    "Shields 7–15 empty. Unique overcounts sheet-accurate (Victory-Class Star Destroyer x2, "
    "TIE Vanguard x6, Dark Jedi Lightsaber x3). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hoth: Main Power Generators"
LS_CARDS = [
    n("Hoth: Main Power Generators"),
    n("Hoth: North Ridge"),
    n("Rogue 3"),
    n("Rogue 2"),
    n("2-1B"),
    n("Zev Senesca"),
    n("Wes Janson"),
    n("Dual Laser Cannon"),
    n("Jedi Lightsaber", qty=3),
    n("Houjix", qty=2),
    n("A New Secret Base"),
    n("Echo Base Garrison"),
    n("Echo Base Operations"),
    n("Lightsaber Proficiency"),
    n("General Solo"),
    n("Independence"),
    n("Redemption"),
    n("Liberty"),
    n("Sense"),
    n("Tatooine"),
    n("Legendary Starfighter"),
    n("Millennium Falcon"),
    n("X-Wing Laser Cannon"),
    n("Artoo-Detoo In Red 5"),
    n("Bacta Tank"),
    n("Obi-Wan Kenobi"),
    n("Disarmed"),
    n("Han's Heavy Blaster Pistol"),
    n("Tantive IV"),
    n("Tauntaun"),
    n("Sense"),
    n("Undercover"),
    n("Out Of Nowhere"),
    n("Thrown Back"),
    n("Goo Nee Tay"),
    n("Projection Of A Skywalker"),
    n("Mantellian Savrip"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Hoth"),
    n("Control"),
    n("Yavin 4", True),
    n("Guardian's Lightsaber", True),
    n("Hoth: Echo Med Lab", True),
    n("Yoda, Great Warrior", True),
    n("Princess Leia, Last Scion", True),
    n("Luke Skywalker", True),
    n("Republic Gunship", True, qty=2),
    n("Chewbacca, Walking Carpet", True),
    n("Foul Moudama", True),
    n("Anger, Fear, Aggression", True),
    n("Han, Chewie, And The Falcon"),
    n("Squadron Assignments"),
    n("Battle Plan"),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Traffic Control", True),
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("There Is Another", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []


DS_START = "Fondor"
DS_CARDS = [
    n("Fondor"),
    n("Death Star"),
    n("Kashyyyk"),
    n("Rendili"),
    n("Ord Mantell"),
    n("Executor: Main Corridor"),
    n("Executor: Docking Bay"),
    n("Executor: Comm Station"),
    n("Executor: Meditation Chamber"),
    n("Executor: Control Station"),
    n("Lord Sidious", True),
    n("Darth Vader", True),
    n("Galen Marek, Starkiller", True),
    n("Count Dooku", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Zuckuss"),
    n("Dengar"),
    n("IG-88"),
    n("U-3PO"),
    n("Flagship Executor"),
    n("Thunderflare"),
    n("Tyrant"),
    n("Victory-Class Star Destroyer", qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Mist Hunter", True),
    n("Punishing One"),
    n("Dooku's Lightsaber", True),
    n("TIE Vanguard", qty=6),
    n("Ghhhk"),
    n("Disarmed"),
    n("Sense"),
    n("Control"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses", True),
    n("Combat Response", True),
    n("Flagship"),
    n("Flagship Operations"),
    n("Boba Fett, Relentless Bounty Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Battle Order"),
    n("Reactor Terminal"),
    n("Oppressive Enforcement"),
    n("Dreaded Imperial Starfleet"),
    n("All Power To Weapons"),
    n("Mobilization Points"),
    n("Dark Jedi Lightsaber", qty=3),
    n("SFS L-s9.3 Laser Cannons"),
    n("Dr. Evazan's Blaster"),
    n("Grievous' Lightsabers", True),
    n("Blizzard 2", True),
    n("IG-88's Pulse Cannon"),
    n("IG-88's Neural Inhibitor"),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("Reactor Terminal"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Leave Them To Me", True),
    n("You Cannot Hide Forever", True),
    n("Abyss", True),
]
DS_ADD = []
