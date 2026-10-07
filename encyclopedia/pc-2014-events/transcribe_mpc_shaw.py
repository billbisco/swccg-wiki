#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Greg Shaw.

Source: MPC-2014-Day-1-Main-Event.pdf pages 96–97 (2013 form, 15 shields).
Name Gregory Shaw dested Greg Shaw. Username blank.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 96
DS_PAGE = 97
LS_SCAN = "2014 Match Play Championship Day 1 Greg Shaw LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Gregory Shaw dested Greg Shaw. Username blank. "
    "LIGHT checked. Watch Your Step (V) dested Watch Your Step (V) / This Place Can Be A Little Rough (V). "
    "Corellian Engineering Corp dested Corellian Engineering Corporation. "
    "Wedge Antilles, Red Squad Leader dested Wedge Antilles, Red Squadron Leader. "
    "Romas 'Lock' Navander dested Romas \"Lock\" Navander. All Wings Report In & DS dested "
    "All Wings Report In & Darklighter Spin. Antilles Maneuver & Rebel Rampage dested "
    "Antilles Maneuver & Rebel Reinforcements. Sense (Premiere) dested Sense. "
    "You've Got A Lot of Guts dested You've Got A Lot Of Guts Coming Here. "
    "Unique overcounts sheet-accurate (No Questions Asked (V) x3, Dash Rendar (V) x2, "
    "Wedge Antilles, Red Squadron Leader x2, Luke Skywalker, Jedi Knight x2, "
    "Leia, Rebel Princess x2, Rebel Barrier x2, Corellian Retort (V) x2, "
    "All Wings Report In & Darklighter Spin x2, Antilles Maneuver (V) x2, "
    "Let The Wookiee Win (V) x2). NO_DEST Romas 'Lock' Navander. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Gregory Shaw dested Greg Shaw. Username blank. "
    "DARK checked. Imperial Occupation (V) dested Imperial Occupation (V) / Imperial Control (V). "
    "Ni Chuba Na?? dested Ni Chuba Na??. Marquand in Blizzard 6 dested Marquand In Blizzard 6. "
    "GMT dested Grand Moff Tarkin. Juno Eclipse, Black Leader dested Juno Eclipse, Black Leader. "
    "Maarek Stele, The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Jango Fett, the Assassin dested Jango Fett, The Assassin. Ommni Box & It's Worse dested "
    "Ommni Box & It's Worse. Unique overcounts sheet-accurate (Blizzard 4 x2, "
    "Grand Moff Tarkin (V) x2, Victory x2, A Dark Time For The Rebellion (V) x2, "
    "Trample x2, Force Push (V) x2, Imperial Command x3, We're In Attack Position Now x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Spaceport City"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Heading For The Medical Frigate"),
    n("No Questions Asked", True, qty=3),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Corran Horn"),
    n("Jaina Solo"),
    n("Chewie", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Laudica", True),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Palejo Reshad"),
    n("Romas \"Lock\" Navander"),
    n("Mirax Terrik"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Obi-Wan In Radiant VII"),
    n("Tantive IV", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Rebel Barrier", qty=2),
    n("Corellian Retort", True, qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere"),
    n("Let The Wookiee Win", True, qty=2),
    n("Sense"),
    n("Punch It!"),
    n("Home One: Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Planetary Defenses", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("He Can Go About His Business"),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Ice Plains", True),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("You May Start Your Landing", True),
    n("Prepared Defenses", True),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Blizzard 4", qty=2),
    n("Veers", True),
    n("General Nevar"),
    n("Emperor Palpatine"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Juno Eclipse, Black Leader"),
    n("ISB Sector Commander"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Maul With Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("U-3PO (Yoo-Threepio)"),
    n("Jango Fett, The Assassin"),
    n("Hoth Blockade"),
    n("Image Of The Dark Lord", True),
    n("Wipe Them Out, All Of Them", True),
    n("No Escape"),
    n("Alert My Star Destroyer!"),
    n("Imperial Propaganda"),
    n("Ommni Box & It's Worse"),
    n("Victory", qty=2),
    n("Conquest", True),
    n("Flagship Executor"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Trample", qty=2),
    n("Force Push", True, qty=2),
    n("Imperial Command", qty=3),
    n("We're In Attack Position Now", qty=2),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("After Her!", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance", True),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
