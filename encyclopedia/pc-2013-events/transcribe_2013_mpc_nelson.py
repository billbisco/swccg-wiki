#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Aaron Nelson Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "hrdog2003"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 63
DS_PAGE = 64
LS_SCAN = "2013 Match Play Championship p63 Aaron Nelson LS.png"
DS_SCAN = "2013 Match Play Championship p64 Aaron Nelson DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Aaron Nelson. Username hrdog2003. Light. Deck title SoCal Blowout. "
    "Plead My Case To The Senate / Senators In Laager. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber. "
    "Senator Bail Organa dested Bail Organa. Bail Organa, Father of Rebellion dested Bail Organa, Father Of Rebellion. "
    "Lando, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Frozen Assets aka Blowout / WTF?! dested Frozen Assets. "
    "Klor'slug dested K'lor'slug. Coruscant (EP1) dested Coruscant. "
    "Yoda Jedi Councilor dested Yoda, Senior Council Member. "
    "Senator Garm Bel Iblis dested General Bel Iblis. "
    "Alderaan Consular Ship dested Radiant VII. "
    "Yoda, Grand Warrior dested Yoda, Great Warrior. "
    "Wesa Gotta Grand Army as written. Naboo: BNC dested Naboo: Boss Nass' Chambers. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Senator Padme Amidala dested Senator Padme Amidala. "
    "Obi w/ Saber dested Obi-Wan With Lightsaber. "
    "AFA dested Anger, Fear, Aggression (Effect). "
    "Battle Plan Cruiser as written. "
    "YISYW dested Your Insight Serves You Well. DDTA dested Don't Do That Again. "
    "Form left column reprints 37–38 on lines 39–40 are Houjix and Menace Fades. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Aaron Nelson. Username hrdog2003. Dark. Deck title SoCal Walkers. "
    "Imperial Occupation / Imperial Control (V) both faces. "
    "Hoth: Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth: MPG (DS) dested Hoth: Main Power Generators (1st Marker). "
    "Boba Fett, Prepared Hunter as written. Tiny/Trample Bounty dested Tarkin's Bounty. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "The Mandalorian, FoF dested Jango Fett, The Assassin. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth: Mountains dested Hoth: Mountains (6th Marker). "
    "Alert My Star Destroyer! as written. General Nevar as written. "
    "Short Range Fighters & WYB dested Short Range Fighters & Watch Your Back. "
    "Blade Fury dested Sith Fury. DTHACC dested Do They Have A Code Clearance?. "
    "Marquand In Blizzard 6 as written. I Have You Now in the line-47 gutter. "
    "Maul w/ Saber dested Darth Maul With Lightsaber. "
    "Maul's Sith Infiltrator as written. Trample (new-v) dested Trample. "
    "Prepared Defenses dested Prepared Defenses. K+D dested Knowledge And Defense. "
    "Ni Chuba Na dested Ni Chuba Na??. You May Start Your Landing as written. "
    "Form left column reprints 37–38 on lines 39–40 are Force Push and Grand Moff Tarkin. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Senators In Laager"
LS_CARDS = [
    n("Plead My Case To The Senate / Senators In Laager"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Bail Organa", qty=3),
    n("So This Is How Liberty Dies"),
    n("Jedi Presence", qty=3),
    n("Imperial Atrocity", True),
    n("Mechanical Failure"),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Naboo: Battle Plains"),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Senate Hovercam"),
    n("Chewbacca, Protector", True),
    n("General Solo", True),
    n("Escape Pod", True),
    n("Frozen Assets", qty=2),
    n("Sense", qty=2),
    n("K'lor'slug", True),
    n("Coruscant"),
    n("Yoda, Senior Council Member", qty=2),
    n("Radiant VII", qty=2),
    n("General Bel Iblis"),
    n("Coruscant: Night Club"),
    n("Yoda, Great Warrior", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Houjix"),
    n("Menace Fades"),
    n("Might Of The Republic", qty=3),
    n("Senator Mon Mothma"),
    n("Naboo: Boss Nass' Chambers"),
    n("Corran Horn"),
    n("Commander Narra"),
    n("Owen Lars & Beru Lars"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Senator Padme Amidala"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Field Dressing"),
    n("Clash Of Sabers"),
    n("Anger, Fear, Aggression", True),
    n("Wokling", True),
    n("Heading For The Medical Frigate"),
    n("Battle Plan Cruiser"),
    n("Strike Planning"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("A Tragedy Has Occurred", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth"),
    n("Boba Fett, Prepared Hunter"),
    n("Stop Motion", True),
    n("Garindan", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Tarkin's Bounty", True),
    n("Masterful Move & Endor Occupation"),
    n("Jango Fett, The Assassin"),
    n("Walker Garrison"),
    n("We're In Attack Position Now"),
    n("Target The Main Generator"),
    n("Admiral Piett"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth Blockade"),
    n("Victory"),
    n("Cold Feet", True),
    n("Imperial Command", qty=2),
    n("Alert My Star Destroyer!"),
    n("Commander Igar", True),
    n("Slave I, Symbol Of Fear"),
    n("General Nevar"),
    n("Admiral Motti", True),
    n("Grand Admiral Thrawn"),
    n("Tempest 1"),
    n("Veers", True),
    n("Ghhhk"),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Trample", True, qty=2),
    n("Trample"),
    n("Control"),
    n("Sith Fury"),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Imperial Decree", True),
    n("Force Push", True),
    n("Grand Moff Tarkin", True),
    n("Blizzard 1", True),
    n("AT-AT Cannon", True),
    n("Do They Have A Code Clearance?"),
    n("Conquest", True),
    n("A Dark Time For The Rebellion", True),
    n("Marquand In Blizzard 6"),
    n("I Have You Now", True),
    n("No Escape"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Maul's Sith Infiltrator"),
    n("Prepared Defenses", True),
    n("Knowledge And Defense", True),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Battle Order", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Fanfare", True),
]
DS_ADD = []
