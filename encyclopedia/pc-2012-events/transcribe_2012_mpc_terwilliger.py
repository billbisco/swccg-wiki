#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Brian Terwilliger.

Source: 2012mpcday1.pdf pages 27–28 (2010 form, 12 shields).
Name Brian Terwilliger dested Brian Terwilliger. Username blank.
p27 Dark Know Your Role & Shut Your Mouth / Imperial Occupation (V).
p28 Light Use Me / Hidden Base.
Do not dest as Chris Terwilliger. Do not rewrite 2013 BTwigg leftover.
"""
from __future__ import annotations

PLAYER = "Brian Terwilliger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 28
DS_PAGE = 27
LS_SCAN = "2012 Match Play Championship Day 1 Brian Terwilliger LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Brian Terwilliger DS.png"
LS_DECK_NAME = "Use Me"
DS_DECK_NAME = "Know Your Role & Shut Your Mouth"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Terwilliger dested Brian Terwilliger. "
    "Username blank. Event MPC. Deck Name Use Me. LIGHT checked. "
    "Do not dest as Chris Terwilliger. Do not rewrite 2013 BTwigg leftover. "
    "Hidden Base dested Hidden Base / Systems Will Slip Through Your Fingers empty. "
    "Rendezvous Point dested Rendezvous Point. "
    "Republic Logistics dested Republic Logistics. "
    "Mon Cal Dockyards dested Mon Calamari: Dockyards. "
    "Kin Kian dested Kin Kian. Dack Ralter dested Dack Ralter. "
    "Han Chewie & Falcon dested Han, Chewie, And The Falcon. "
    "Mon Cal Star Cruiser dested Mon Calamari Star Cruiser. "
    "Kiffex dested Kiffex. Mon Calamari dested Mon Calamari. "
    "Dagobah: Yoda's Hut dested Dagobah: Yoda's Hut. "
    "A Jedi's Plans dested as written. "
    "Heavy Turbolaser Battery dested Heavy Turbolaser Battery. "
    "Projection Of A Skywalker dested Projection Of A Skywalker. "
    "3PO w his parts showing dested Threepio With His Parts Showing. "
    "Were you looking for me dested Were You Looking For Me?. "
    "Stay Sharp dested Stay Sharp. "
    "Antilles Maneuver / Rebel Reinforcements dested "
    "Antilles Maneuver & Rebel Reinforcements. "
    "Power Pivot dested Power Pivot. Cutarget dested as written. "
    "OOC / Trans Terminated dested Out Of Commission & Transmission Terminated. "
    "ICBW dested as written. Merc Sunlet dested Merc Sunlet. "
    "Handy for Medical Frigate dested Heading For The Medical Frigate. "
    "AF Aggression dested Anger, Fear, Aggression. "
    "Tragedy (not v) checkbox True dested without (V). "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Terwilliger dested Brian Terwilliger. "
    "Username blank. Event Date 2/11/12. Deck Name Know Your Role & Shut Your Mouth. "
    "DARK checked. Do not dest as Chris Terwilliger. Do not rewrite 2013 BTwigg leftover. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control True. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Ghhhk form 2 True and form 3 empty kept separate. "
    "Hoth Main Power Generators (1st) dested Hoth: Main Power Generators. "
    "Hoth Ice Plains (V) dested Hoth: Ice Plains True. "
    "You May Start Your Landing dested You May Start Your Landing. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Target the Main Generator dested Target The Main Generator. "
    "Do they have a code clearance dested Do They Have A Code Clearance?. "
    "General Nevar dested General Nevar. AT-AT Cannon dested AT-AT Cannon. "
    "Hoth 3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Operational as Planned dested Operational As Planned. "
    "Omni Box / It's Worse dested Ommni Box & It's Worse. "
    "Executor dested Flagship Executor. U3PO dested U-3PO. "
    "We're in Attack Position Now dested We're In Attack Position Now. "
    "Boba Fett, Bounty Hunter dested Boba Fett, Bounty Hunter. "
    "Darth Vader dested Darth Vader. Laser Cannon Battery dested Laser Cannon Battery. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Dark Time for Rebellion dested A Dark Time For The Rebellion. "
    "Walker Garrison dested Walker Garrison. Commander Igar dested Commander Igar. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Hoth Mountains dested Hoth: Mountains (6th Marker). "
    "Masterful Move / Endor Occupation dested Masterful Move & Endor Occupation. "
    "Marquand in Blizz 6 dested Marquand In Blizzard 6. "
    "Image of the Dark Lord dested Image Of The Dark Lord. "
    "Hoth Blockade dested Hoth Blockade. "
    "Leave them to me dested Leave Them To Me. "
    "There is no try dested There Is No Try. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Rendezvous Point"),
    n("Republic Logistics", True),
    n("Superficial Damage", True),
    n("Mon Calamari: Dockyards", True),
    n("Boushh"),
    n("Admiral Ackbar", True),
    n("Kin Kian"),
    n("Captain Verrack", True),
    n("Dack Ralter"),
    n("Luke Skywalker", True),
    n("Han, Chewie, And The Falcon"),
    n("Mon Calamari Star Cruiser", True, qty=5),
    n("Liberty"),
    n("Defiance", qty=2),
    n("Dagobah"),
    n("Tatooine"),
    n("Kessel"),
    n("Kiffex"),
    n("Naboo"),
    n("Kashyyyk"),
    n("Mon Calamari"),
    n("Dagobah: Yoda's Hut"),
    n("A Jedi's Plans", True),
    n("Heavy Turbolaser Battery", qty=3),
    n("Grimtaash"),
    n("Projection Of A Skywalker", qty=2),
    n("Threepio With His Parts Showing"),
    n("Were You Looking For Me?"),
    n("Alter"),
    n("Stay Sharp"),
    n("Hear Me Baby, Hold Together", True),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Power Pivot", qty=2),
    n("Escape Pod", True),
    n("Cutarget", qty=3),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("ICBW", qty=2),
    n("Merc Sunlet", True),
    n("Rebel Barrier"),
    n("Heading For The Medical Frigate", True),
    n("Imperial Atrocity", True, qty=4),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("He Can Go About His Business", True),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Ghhhk", True),
    n("Ghhhk"),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("Target The Main Generator"),
    n("Prepared Defenses", True),
    n("Do They Have A Code Clearance?"),
    n("General Nevar", True),
    n("Tempest 1"),
    n("AT-AT Cannon", True),
    n("Veers", True),
    n("Imperial Occupation / Imperial Control", True),
    n("Victory", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Operational As Planned", True),
    n("Blizzard 2", True),
    n("Ommni Box & It's Worse", qty=2),
    n("Flagship Executor", qty=2),
    n("Control", qty=2),
    n("U-3PO"),
    n("Conquest", True),
    n("We're In Attack Position Now", qty=2),
    n("Bossk", True),
    n("Devastator", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Darth Vader", True),
    n("No Escape"),
    n("Laser Cannon Battery"),
    n("Maarek Stele, The Emperor's Reach", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Command", qty=3),
    n("Walker Garrison"),
    n("Commander Igar", True),
    n("Trample", qty=2),
    n("Admiral Piett"),
    n("Juno Eclipse, Black Leader", True),
    n("Blizzard 4", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Masterful Move & Endor Occupation"),
    n("Marquand In Blizzard 6", True),
    n("Image Of The Dark Lord", True),
    n("Blizzard 1", True),
    n("Hoth Blockade", True),
    n("Admiral Motti", True),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
]
DS_SHIELDS = [
    n("Resistance", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("Leave Them To Me", True),
    n("Abyss", True),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("There Is No Try", True),
]
DS_ADD = []
