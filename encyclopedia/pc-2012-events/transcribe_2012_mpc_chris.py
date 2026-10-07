#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Terwilliger.

Source: 2012mpcday1.pdf pages 137–138 (2010 form, 12 shields).
Name Chris Twigs / Chris Twigg dested Chris Terwilliger (2013 Worlds analog).
Username blank (do not copy 2014 Nats Username Vader322).
p137 Light Center Of Tyranny. p138 Dark Imperial Occupation.
Pack player-stubs/Chris_Terwilliger.wiki.
Do not dest as Brian Terwilliger. Do not dest as Marty Terwilliger.
Do not dest as a new person.
Do not rewrite 2013 Worlds leftover Hyperdrive / Walkers.
"""
from __future__ import annotations

PLAYER = "Chris Terwilliger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 137
DS_PAGE = 138
LS_SCAN = "2012 Match Play Championship Day 1 Chris Terwilliger LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Terwilliger DS.png"
LS_DECK_NAME = "What..."
DS_DECK_NAME = "...What!"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Twigs dested Chris Terwilliger. "
    "Username blank. LIGHT checked. Deck Name What... Event Name MPC 12. "
    "Do not dest as Brian Terwilliger. Do not dest as Marty Terwilliger. "
    "Do not copy 2014 Nats Username Vader322. "
    "Do not rewrite 2013 Worlds leftover Hyperdrive. "
    "Center of Tyranny True dested Center Of Tyranny / A Liberated World True analog Hodur. "
    "Gold Leader in Gold 1 True dested Gold Leader In Gold 1 True analog leftover. "
    "Planetary Shield True dested analog Hodur. "
    "Coruscant Lower levels True dested Coruscant: Lower Levels True analog Hodur. "
    "Commando Training & K'lor'slug True dested analog leftover. "
    "Declaration of Rebellion True dested Declaration Of Rebellion True analog leftover. "
    "Honor of the Jedi empty dested Honor Of The Jedi analog leftover. "
    "It's not my Fault! True dested It's Not My Fault! True analog leftover. "
    "Obi-Wan in Radiant VII True dested Obi-Wan In Radiant VII True analog Hodur. "
    "Wedge Antilles Red Squadron Leader dested Wedge Antilles, Red Squadron Leader analog leftover. "
    "Phylo Gandish True dested as written analog Herold. "
    "Odin Nesloor & First Aid True dested analog leftover. "
    "Luke Skywalker, Rebel Hero True x3 sheet-accurate. "
    "Yub Yub Commander True dested Yub Yub, Commander True analog Hodur. "
    "Coruscant Senate landing Platform True dested Coruscant: Senate Landing Platform True analog leftover. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon analog leftover. "
    "Return of a Jedi True dested Return Of A Jedi True analog leftover. "
    "Heading to the Medical Frigate True dested Heading For The Medical Frigate True analog leftover. "
    "Derek Hobbie True dested Derek 'Hobbie' Klivian True analog Hodur. "
    "Tycho Celchu True dested analog leftover. "
    "Biggs, Rogue Legend True dested analog Hodur. "
    "Antilles Maneuver & Rebel Reinforcements True dested analog leftover. "
    "Pain-Rendar dested Dash Rendar True analog Hodur. "
    "Leia True dested Leia True analog Carulli. "
    "Padme Naberrie True dested analog leftover. "
    "It could be worse dested It Could Be Worse analog leftover. "
    "Booster in Pulsar Skate True dested analog leftover. "
    "Anger, Fear, Aggression True dested in the 60 analog Casey. Unique 60. Shields 12. "
    "Shield Wise Advice crossed Battle Plan dest replacement empty analog leftover. "
    "Simple Tricks and Nonsense True dested analog leftover. "
    "Weapons Display True dested analog leftover."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Twigg dested Chris Terwilliger. "
    "Username blank. DARK checked. Deck Name ...What! Event Name MPC '12. "
    "Do not dest as Brian Terwilliger. Do not dest as Marty Terwilliger. "
    "Do not copy 2014 Nats Username Vader322. "
    "Do not rewrite 2013 Worlds leftover Walkers. "
    "Imperial Occupation True dested Imperial Occupation / Imperial Control True analog leftover. "
    "marker 3 dested Hoth: Defensive Perimeter (3rd Marker) analog Eier. "
    "marker 6 dested Hoth: Mountains (6th Marker) analog Eier. "
    "marker 5 True dested Hoth: Ice Plains True analog leftover Dark 5th Marker. "
    "marker 1 dested Hoth: Ice Plains empty analog Foth True AND empty kept separate. "
    "We're In Attack Position Now empty x2 analog leftover. "
    "Operational As Planned empty x2 analog leftover. "
    "Imperial Command empty x3 analog leftover. "
    "Masterful Move & Endor Occupation dested analog leftover. "
    "Ni Chuba Na?? True dested analog leftover. "
    "A Dark Time For The Rebellion True x3 sheet-accurate. "
    "Prepared Defenses True dested in the 60 analog Pistone. "
    "Do they have a code clearance dested Do They Have A Code Clearance? analog leftover. "
    "Image of a Dark Lord True dested Image Of The Dark Lord True analog leftover. "
    "Endor Shield True dested analog leftover. "
    "Omni Box & It's worse dested Ommni Box & It's Worse analog Hollingworth. "
    "Boba Fett, Bounty Hunter True dested analog leftover. "
    "The Emperor's Reach True dested Maarek Stele, The Emperor's Reach analog Eier. "
    "Veers True dested analog Brian leftover. "
    "Marquand in Blizzard 6 True dested Marquand In Blizzard 6 True analog leftover. "
    "General Nevar True dested analog leftover. "
    "Victory True dested analog leftover. "
    "U-3PO dested U-3PO analog leftover. "
    "Black Leader True dested Juno Eclipse, Black Leader analog Eier. "
    "Admiral Piett True AND empty kept separate analog Foth. "
    "Tempest 1 dested analog Brian leftover. "
    "Executor dested analog leftover. "
    "K&D True dested in the 60 analog Murray. Unique 60. Shields 12. "
    "You Can't Hide Forever True dested You Cannot Hide Forever True analog leftover. "
    "Leave them to me True dested Leave Them To Me True analog leftover."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Center Of Tyranny / A Liberated World", True),
    n("Dressel", True),
    n("Gold Leader In Gold 1", True),
    n("Planetary Shield", True),
    n("Coruscant: Lower Levels", True),
    n("Coruscant", True),
    n("Coruscant: Main Power Plant", True),
    n("Commando Training & K'lor'slug", True),
    n("Rogue Insertion", True),
    n("Declaration Of Rebellion", True),
    n("Honor Of The Jedi"),
    n("Rogue Squadron Tactics", True),
    n("Bacta Infirmary", True),
    n("Dack Ralter", True),
    n("Commander Narra", True),
    n("Coruscant Celebration", qty=2),
    n("It's Not My Fault!", True, qty=2),
    n("Obi-Wan In Radiant VII", True),
    n("Luke's Blaster Pistol", True),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Phylo Gandish", True),
    n("Odin Nesloor & First Aid", True, qty=2),
    n("Luke Skywalker, Rebel Hero", True, qty=3),
    n("Wes Janson, Rogue Veteran", True),
    n("Yub Yub, Commander", True, qty=3),
    n("Field Dressing", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Coruscant: Senate Landing Platform", True),
    n("Imperial Atrocity", True),
    n("Corran Horn"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Return Of A Jedi", True),
    n("Heading For The Medical Frigate", True),
    n("Spiral"),
    n("Derek 'Hobbie' Klivian", True),
    n("Menace Fades"),
    n("Tycho Celchu", True),
    n("Biggs, Rogue Legend", True),
    n("Civil Disorder", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Dash Rendar", True),
    n("Leia", True),
    n("Padme Naberrie", True),
    n("It Could Be Worse"),
    n("Booster In Pulsar Skate", True),
    n("Ten Numb", True),
    n("Captive Pursuit"),
    n("Tantive IV", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here"),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Ice Plains"),
    n("AT-AT Cannon", True),
    n("Target The Main Generator", True),
    n("We're In Attack Position Now", qty=2),
    n("Hoth Blockade", True),
    n("Operational As Planned", qty=2),
    n("Imperial Command", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Trample", qty=2),
    n("Ni Chuba Na??", True),
    n("A Dark Time For The Rebellion", True, qty=3),
    n("Control", qty=2),
    n("Prepared Defenses", True),
    n("No Escape"),
    n("You May Start Your Landing"),
    n("Do They Have A Code Clearance?"),
    n("Imperial Decree"),
    n("Image Of The Dark Lord", True),
    n("Endor Shield", True),
    n("Walker Garrison"),
    n("Ommni Box & It's Worse"),
    n("Commander Igar", True),
    n("Admiral Piett", True),
    n("Garindan", True, qty=2),
    n("Boba Fett, Bounty Hunter", True),
    n("Grand Moff Tarkin", True),
    n("Darth Vader", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Veers", True),
    n("Marquand In Blizzard 6", True),
    n("General Nevar", True),
    n("Grand Admiral Thrawn"),
    n("Bossk", True),
    n("Blizzard 1", True),
    n("Victory", True),
    n("U-3PO"),
    n("Juno Eclipse, Black Leader", True),
    n("Admiral Piett"),
    n("Conquest", True),
    n("Blizzard 2", True),
    n("Tempest 1"),
    n("Executor", qty=2),
    n("Blizzard 4", True),
    n("Devastator", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Leave Them To Me", True),
    n("Resistance"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
