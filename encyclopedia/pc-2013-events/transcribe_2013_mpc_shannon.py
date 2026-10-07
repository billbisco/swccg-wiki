#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Shannon Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Shannon"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 82
DS_PAGE = 81
LS_SCAN = "2013 Match Play Championship p82 Shannon LS.png"
DS_SCAN = "2013 Match Play Championship p81 Shannon DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Shannon. Light. "
    "Plead My Case To Senate dested Plead My Case To The Senate / Senators In Laager. "
    "Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Battle Plan + Draw Their Fire dested Battle Plan & Draw Their Fire. "
    "Heading for The Medical Frigate dested Heading For The Medical Frigate. "
    "Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Coruscant (Episode I) dested Coruscant. "
    "Bail Organa, Father of Rebellion dested Bail Organa, Father Of Rebellion. "
    "Senator JarJar Binks dested Senator Jar Jar Binks. "
    "Luke Skywalker Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Obi Wan with Lightsaber dested Obi-Wan With Lightsaber. "
    "Wedge Antilles, Red Squad Leader dested Wedge Antilles, Red Squadron Leader. "
    "Chewbacca Protector dested Chewbacca, Protector. "
    "Owen + Beru Lars dested Owen Lars & Beru Lars. "
    "Commander Nara dested Commander Narra. "
    "Yoda Stew + You Do Have Your Moments dested Yoda Stew & You Do Have Your Moments. "
    "Houjix + Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Sense (premiere) dested Sense. "
    "Simple tricks + Nonsense dested Simple Tricks And Nonsense. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred. "
    "Lets Keep A Little Optimism Here dested Let's Keep A Little Optimism Here. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Form left column reprints 37–38 on lines 39–40 are Wesa Gotta Grand Army and Houjix & Out Of Nowhere. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Shannon. Dark. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control. "
    "NiChuba Na dested Ni Chuba Na??. "
    "You May Start Your Landing dested You May Start Your Landing. "
    "Hoth: Main Power Generators dested Hoth: Main Power Generators (1st Marker). "
    "Hoth: Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth: Mountains dested Hoth: Mountains (6th Marker). "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "The Emperors Reach dested Maarek Stele, The Emperor's Reach. "
    "The Mandalorian Father of Fett dested Jango Fett, The Assassin. "
    "Boba Fett Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Garindan dested Garindan. "
    "Darth Maul with Lightsaber dested Darth Maul With Lightsaber. "
    "Marquand in Blz 6 dested Marquand In Blizzard 6. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Maul's Sith Infiltrator as written. "
    "Dark Time For Rebellion dested A Dark Time For The Rebellion. "
    "Masterful Move + Endor Occ dested Masterful Move & Endor Occupation. "
    "Short Range Fighters + Watch Your Back dested Short Range Fighters & Watch Your Back. "
    "Alert My Star Destroyer dested Alert My Star Destroyer!. "
    "Image of The Dark Lord dested Image Of The Dark Lord. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "Hoth Blockade as written. "
    "We're In Attack Position Now as written. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "Form left column reprints 37–38 on lines 39–40 are A Dark Time For The Rebellion and Ghhhk. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Senators In Laager"
LS_CARDS = [
    n("Plead My Case To The Senate / Senators In Laager"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Battle Plan & Draw Their Fire"),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Night Club"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Coruscant"),
    n("Bail Organa", qty=2),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Senator Mon Mothma"),
    n("Senator Leia Organa"),
    n("Senator Padme Amidala"),
    n("Senator Jar Jar Binks"),
    n("General Solo", True),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Chewbacca, Protector", True),
    n("Owen Lars & Beru Lars"),
    n("Corran Horn"),
    n("Commander Narra"),
    n("Alderaan Consular Ship", qty=2),
    n("Yoda Stew & You Do Have Your Moments", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Desperate Reach", True),
    n("Clash Of Sabers"),
    n("Jedi Presence", qty=3),
    n("Menace Fades"),
    n("Sense", qty=2),
    n("Might Of The Republic", qty=3),
    n("Frozen Assets", qty=2),
    n("Mechanical Failure", qty=2),
    n("Senate Hovercam"),
    n("Field Dressing"),
    n("Imperial Atrocity", True),
    n("So This Is How Liberty Dies"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("You May Start Your Landing", True),
    n("Prepared Defenses", True),
    n("Hoth"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Target The Main Generator"),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Admiral Piett"),
    n("Commander Igar", True),
    n("Juno Eclipse, Black Leader"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("General Nevar"),
    n("Veers", True),
    n("Garindan", True),
    n("Admiral Motti", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Blizzard 4"),
    n("Tempest 1"),
    n("Marquand In Blizzard 6"),
    n("Blizzard 2", True),
    n("Blizzard 1", True),
    n("Conquest", True, qty=2),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Force Push", True),
    n("Control"),
    n("A Dark Time For The Rebellion", True),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Imperial Command", qty=2),
    n("Walker Garrison"),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Trample", qty=2),
    n("Tarkin's Bounty", True),
    n("Alert My Star Destroyer!"),
    n("Image Of The Dark Lord", True),
    n("Do They Have A Code Clearance?"),
    n("Hoth Blockade"),
    n("No Escape"),
    n("Imperial Decree", True),
    n("We're In Attack Position Now"),
    n("AT-AT Cannon", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
