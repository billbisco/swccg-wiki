#!/usr/bin/env python3
"""2013 World Championship Day 2: Chris Twigg Xerox Hyperdrive + Walkers."""
from __future__ import annotations

PLAYER = "Chris Terwilliger"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 97
DS_PAGE = 98
LS_SCAN = "2013 Worlds Day 2 p97 Chris Twigg LS.png"
DS_SCAN = "2013 Worlds Day 2 p98 Chris Twigg DS.png"
PUBLIC_NOTE = "Name box on the Day 2 sheet is Chris Twigg."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Chris Twigg. Username blank. Email [redacted]. LIGHT. "
    "Deck title Dark Rules. Dest as Chris Terwilliger (2014 generate maps Chris Twigg). "
    "Do not dest as BTwigg or Brian Terwilliger. Do not rewrite the 2013 MPC BTwigg leftover. "
    "Hyperdrive dested The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Tat: City outskirts dested Tatooine: City Outskirts. "
    "Tat: Watto's Junkyard dested Tatooine: Watto's Junkyard. "
    "Heading to the medical Frigate dested Heading For The Medical Frigate. "
    "Republic Gunship Wing dested Republic Gunship Wing. "
    "Guardian's Lightsaber dested Guardian's Lightsaber. "
    "Yoda stew / You'd have your moments dested Yoda Stew & You Do Have Your Moments. "
    "Sorry about the mess / Blaster Proficiency dested "
    "Sorry About The Mess & Blaster Proficiency. "
    "R-3PO dested R-3PO (Ar-Threepio). "
    "Naboo: Boss nass chamber dested Naboo: Boss Nass' Chambers. "
    "Jabba's Palace: Audience chamber dested Jabba's Palace: Audience Chamber. "
    "Maris Brood, Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Mace Windu, master of the Order dested Mace Windu, Master Of The Order. "
    "Were you looking for me? dested Were You Looking For Me?. "
    "A Remote Planet dested A Remote Planet. "
    "Lucky shot dested Lucky Shot. "
    "Form left column reprints 37-38 on lines 39-40 are Disarmed and Seeking An Audience. "
    "Additional Affect Mind / Ultimatum / He Can Go About His Business moved to Light shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Chris Twigg. Username blank. Email [redacted]. DARK. "
    "Deck title Twigg Hoth. Dest as Chris Terwilliger. "
    "Do not dest as BTwigg or Brian Terwilliger. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control. "
    "Hoth: Marker 1 dested Hoth: Main Power Generators (1st Marker). "
    "Hoth: Marker 3 dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth: Marker 5 dested Hoth: Ice Plains (5th Marker). "
    "Hoth: Marker 6 dested Hoth: Mountains (6th Marker). "
    "You may start your landing dested You May Start Your Landing. "
    "We're in Attack Position Now dested We're In Attack Position Now. "
    "Alert my star Destroyer dested Alert My Star Destroyer!. "
    "Magarek Stele dested Maarek Stele, The Emperor's Reach. "
    "ISB sector commander dested ISB Sector Commander. "
    "Juno Eclipse, Black leader dested Juno Eclipse, Black Leader. "
    "Admiral Mott dested Admiral Motti. "
    "U-3PO dested U-3PO (Yoo-Threepio). "
    "Cyclone Walker dested Cyclone Walker. "
    "Victory dested Victory. "
    "We'll Let Fate-a Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37-38 on lines 39-40 are Darth Vader and Juno Eclipse, Black Leader. "
    "Additional Battle Order / Secret Plans / Abyss moved to Dark shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Watto's Junkyard"),
    n("Credits Will Do Fine"),
    n("Heading For The Medical Frigate", True),
    n("Meditation"),
    n("Obi-Wan's Journal"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Senator Jar Jar Binks", True),
    n("Crash Site Memorial"),
    n("Sense", qty=3),
    n("Sai'torr Kal Fas", True),
    n("Guardian's Lightsaber", True),
    n("Imperial Atrocity", True, qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Sorry About The Mess", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("A Gift"),
    n("Republic Gunship Wing", True, qty=3),
    n("Master Qui-Gon", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Might Of The Republic"),
    n("Temporary Foothold", True),
    n("Disarmed"),
    n("Seeking An Audience", True),
    n("Much To Learn, You Still Have", True),
    n("Senator Mon Mothma", True),
    n("Blaster Deflection"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Were You Looking For Me?"),
    n("A Remote Planet", True),
    n("R-3PO (Ar-Threepio)", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Jabba's Palace: Audience Chamber"),
    n("Obi-Wan's Lightsaber"),
    n("Lucky Shot", True),
    n("Maris Brood, Fallen Jedi", True),
    n("Clash Of Sabers", qty=2),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Lightsaber Proficiency"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Nabrun Leids"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Aim High", True),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
    n("Battle Plan"),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Wise Advice", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("Affect Mind", True),
    n("Ultimatum"),
    n("He Can Go About His Business", True),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Mountains (6th Marker)", True),
    n("Hoth"),
    n("AT-AT Deployment Platform", True, qty=2),
    n("Prepared Defenses", True),
    n("Fleet Security Protocols", True),
    n("You May Start Your Landing", True),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Imperial Decree", True),
    n("Crash Landing"),
    n("Alert My Star Destroyer!"),
    n("Image Of The Dark Lord", True),
    n("Do They Have A Code Clearance?"),
    n("Hoth Blockade", True),
    n("No Escape"),
    n("A Dark Time For The Rebellion", qty=2),
    n("Close Call", True),
    n("Imperial Command", qty=3),
    n("Protocol Failure", True),
    n("Lightsaber Deficiency", True),
    n("Trample"),
    n("We're In Attack Position Now", qty=2),
    n("Garindan", True),
    n("Probot", True),
    n("Grand Admiral Thrawn"),
    n("Jango Fett, The Assassin", True),
    n("Veers", True),
    n("Admiral Motti", True),
    n("Grand Moff Tarkin", True),
    n("Darth Vader", True),
    n("Juno Eclipse, Black Leader", True),
    n("Commander Igar"),
    n("Admiral Piett"),
    n("Maarek Stele, The Emperor's Reach", True),
    n("ISB Sector Commander", True),
    n("Control & Set For Stun"),
    n("AT-AT Cannon", True),
    n("Flagship Executor"),
    n("Victory", True),
    n("Conquest", True, qty=2),
    n("Blizzard 2", True),
    n("Blizzard 4", qty=2),
    n("Tempest 1"),
    n("Cyclone Walker", True, qty=3),
    n("U-3PO (Yoo-Threepio)"),
    n("Target The Main Generator"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Leave Them To Me", True),
    n("Firepower", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Oppressive Enforcement", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Abyss", True),
]
DS_ADD = []
