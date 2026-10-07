#!/usr/bin/env python3
"""2013 World Championship Day 2: Aaron Kinser Xerox Walkers + Hyperdrive."""
from __future__ import annotations

PLAYER = "Aaron Kinser"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 53
DS_PAGE = 52
LS_SCAN = "2013 Worlds Day 2 p53 Aaron Kinser LS.png"
DS_SCAN = "2013 Worlds Day 2 p52 Aaron Kinser DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Aaron Kinser. Username blank. "
    "Event Worlds Day 2. Deck title Hyper Active. LIGHT. "
    "Do not rewrite the 2013 MPC Aaron Kinser leftover. "
    "The Hyperdrive Generator's Gone dested The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Tatooine City Outskirts dested Tatooine: City Outskirts. "
    "Tatooine Watto's Junkyard dested Tatooine: Watto's Junkyard. "
    "Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Jabba's Palace Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Threepio with Parts Showing dested Threepio With His Parts Showing. "
    "Obi-Wan Kenobi Padawan Learner dested Obi-Wan Kenobi, Padawan Learner. "
    "Master Qui-Gon dested Master Qui-Gon. "
    "Mace Windu, Master of the Order dested Mace Windu, Master Of The Order. "
    "Senator Mon Mothma dested Senator Mon Mothma. "
    "Senator Jar Jar Binks dested Senator Jar Jar Binks. "
    "Maris Brood, Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "R3PO dested R-3PO (Ar-Threepio). "
    "Republic Gunship Wing dested Republic Gunship Wing. "
    "Much To Learn dested Much To Learn, You Still Have. "
    "Yoda Stew combo dested Yoda Stew & You Do Have Your Moments. "
    "Sorry About The Mess + Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Into The Garbage Chute Flyboy dested Into The Garbage Chute, Flyboy. "
    "Were You Looking For Me dested Were You Looking For Me?. "
    "Crush of the Saber as written. "
    "Form left column reprints 37-38 on lines 39-40 are Crush Of The Saber x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Aaron Kinser. Username blank. "
    "Event Day 2. Deck title Is it still Good!?. DARK. "
    "Do not rewrite the 2013 MPC Aaron Kinser leftover. "
    "Imperial Occupation dested Imperial Occupation (V) / Imperial Control (V). "
    "Hoth sites dested Hoth: Mountains / Ice Plains / Defensive Perimeter / Main Power Generators. "
    "The Mandalorian dested The Mandalorian. "
    "Black Leader dested Black Leader. "
    "U3PO dested U-3PO (Yoo-Threepio). "
    "Ozzel dested Admiral Ozzel. "
    "Masterful Move + Endor Occup dested Masterful Move & Endor Occupation. "
    "Control Set For Stun dested Control & Set For Stun. "
    "Alert My Star Destroyer dested Alert My Star Destroyer!. "
    "The Emperor's Reach dested The Emperor's Reach. "
    "Anger Fear Aggression Struggle of the Throne dested Anger, Fear, Aggression & Struggle Of The Throne. "
    "Additional Leave Them To Me / Imperial Detention moved to Dark shields. "
    "Additional Wipe Them Out, All Of Them kept as extra Effect. "
    "Form left column reprints 37-38 on lines 39-40 are Grand Moff Tarkin / Grand Admiral Thrawn. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Watto's Junkyard"),
    n("Naboo: Boss Nass' Chambers"),
    n("Jabba's Palace: Audience Chamber"),
    n("Threepio With His Parts Showing"),
    n("Obi-Wan Kenobi, Padawan Learner", True),
    n("Master Qui-Gon", True, qty=3),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Senator Mon Mothma"),
    n("Senator Jar Jar Binks", True),
    n("Maris Brood, Fallen Jedi"),
    n("R-3PO (Ar-Threepio)", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Guardian's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Obi-Wan's Lightsaber"),
    n("Republic Gunship Wing", qty=3),
    n("Seeking An Audience", True),
    n("Temporary Foothold"),
    n("Crash Site Memorial"),
    n("Imperial Atrocity", True, qty=2),
    n("Meditation", True),
    n("Much To Learn, You Still Have"),
    n("Disarmed"),
    n("Lightsaber Proficiency"),
    n("Sai'torr Kal Fas", True),
    n("A Gift"),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Credits Will Do Fine"),
    n("A Remote Planet", True),
    n("Crush Of The Saber", qty=2),
    n("Blaster Deflection", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Sense", qty=3),
    n("Were You Looking For Me?"),
    n("Nabrun Leids"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Barrier"),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Might Of The Republic"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Let The Wookiee Win", True),
    n("Heading For The Medical Frigate", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Aim High", True),
]
LS_ADD = []


DS_START = "Imperial Occupation (V) / Imperial Control (V)"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Mountains"),
    n("AT-AT Deployment Platform"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Main Power Generators", True),
    n("Hoth"),
    n("AT-AT Cannon", True),
    n("Imperial Command", qty=3),
    n("Close Call", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Artillery"),
    n("Cold Feet"),
    n("Masterful Move & Endor Occupation"),
    n("Control & Set For Stun"),
    n("Prepared Defenses", True),
    n("No Escape"),
    n("Alert My Star Destroyer!"),
    n("Hoth Blockade", True),
    n("Image Of The Dark Lord", True),
    n("Do They Have A Code Clearance?"),
    n("You May Start Your Landing", True),
    n("Fleet Security Protocols"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("We're In Attack Position Now"),
    n("Conquest", True, qty=2),
    n("Victory"),
    n("Flagship Executor"),
    n("Admiral Ozzel", True),
    n("Probot"),
    n("Ghhhk"),
    n("The Emperor's Reach"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("Veers", True),
    n("Commander Igar"),
    n("Black Leader", True),
    n("The Mandalorian", True),
    n("Admiral Motti", True),
    n("Darth Vader", True),
    n("Admiral Piett"),
    n("U-3PO (Yoo-Threepio)"),
    n("Target The Main Generator"),
    n("Blizzard 4"),
    n("Cyclone Walker", qty=3),
    n("AT-AT Deployment Platform"),
    n("Blizzard 2", True),
    n("Tempest 1"),
    n("We're In Attack Position Now"),
    n("Trample"),
    n("Crash Landing"),
    n("Anger, Fear, Aggression & Struggle Of The Throne"),
]
DS_SHIELDS = [
    n("Battle Plan"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Resistance", True),
    n("Come Here You Big Coward"),
    n("Reactor Terminal"),
    n("A Useless Gesture"),
    n("Fanfare"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Leave Them To Me", True),
    n("Imperial Detention"),
]
DS_ADD = [
    n("Wipe Them Out, All Of Them", True),
]
