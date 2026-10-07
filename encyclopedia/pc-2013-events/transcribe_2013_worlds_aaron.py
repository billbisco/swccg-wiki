#!/usr/bin/env python3
"""2013 World Championship Day 1: Aaron Kia Xerox LS+DS (name as written)."""
from __future__ import annotations

PLAYER = "Aaron Kia"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Worlds Day 1.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2013 Worlds Day 1 p08 Aaron Kia LS.png"
DS_SCAN = "2013 Worlds Day 1 p07 Aaron Kia DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Aaron Kia. Username blank. "
    "Event Day 1. Deck title Chris's Best 1. LIGHT. Dated 8/10/13. "
    "Saitor Kal Fas dested Sai'torr Kal Fas. Hyper Drive dested Hyper Escape. "
    "Maris Brood dested Maris Brood, Fallen Jedi. "
    "Mace Windu Master of the order dested Mace Windu, Master Of The Order. "
    "Wesa Got a Grand Army dested Wesa Gotta Grand Army. "
    "Qui-Gon Jinn Lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "Much To Learn You Still Have dested Much To Learn, You Still Have. "
    "Were You Looking for me dested Were You Looking For Me?. "
    "Into the Garbage Chute Flyboy dested Into The Garbage Chute, Flyboy. "
    "Obi Wan Padawan Learner dested Obi-Wan Kenobi, Padawan Learner. "
    "Seeking An Audience dested Seeking An Audience. "
    "Heading For the Medical Frigate dested Heading For The Medical Frigate. "
    "Threepio With His Parts Showing dested Threepio With His Parts Showing. "
    "Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Tatooine Watto Junkyard dested Tatooine: Watto's Junkyard. "
    "Tatooine City Outskirts dested Tatooine: City Outskirts. "
    "Anger Fear aggression dested Anger, Fear, Aggression. "
    "Sorry About the Mess dested Sorry About The Mess. "
    "Scramble New Meaning dested as written. "
    "Yoda Stew and You do the Wookiee dested Yoda, You Seek Yoda. "
    "Republic Gunship Close dested Republic Gunship. "
    "R2PO dested Artoo-Detoo. Scramble Say The Bits dested as written. "
    "Shield line 1 reads 15 shields with no titles listed. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field first-name Aaron only. Username blank. "
    "LIGHT/DARK boxes empty; walker package is Dark. "
    "A Hoth My Destroyer dested Walker Garrison. "
    "Cyclone Walker dested AT-AT. Vanguard in Blizzard 1 dested AT-AT Commander. "
    "Control Set For Stun dested Set For Stun. "
    "We're in Attack Position dested We're In Attack Position Now. "
    "Target the main Generator dested Target The Main Generator. "
    "Masterful Move Endor Occupation dested Masterful Move & Endor Occupation. "
    "Jango Fett The Assassin dested Jango Fett, The Assassin. "
    "AT-AT Deployment Platform dested as written. "
    "You'll Be Stunt Your luck dested You'll Be Dead!. "
    "WIAPPN dested We're In Attack Position Now. For FP dested Force Push. "
    "IOTDL dested as written. DTHACC dested as written. "
    "ADTFTR dested A Dark Time For The Rebellion. Cold Beet dested Cold Feet. "
    "Hoth MPG dested Hoth: Main Power Generators. "
    "3rd Marker dested Hoth: 3rd Marker. 5th Marker dested Hoth: 5th Marker. "
    "6th Marker dested Hoth: 6th Marker. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Shields mostly blank. Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Sai'torr Kal Fas"
LS_CARDS = [
    n("Sai'torr Kal Fas", True),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Hyper Escape"),
    n("A Remote Planet", True),
    n("Credits Will Do Fine"),
    n("Maris Brood, Fallen Jedi"),
    n("Scramble New Meaning"),
    n("Might Of The Republic"),
    n("Temporary Truce"),
    n("Mace Windu, Master Of The Order"),
    n("Lightsaber Proficiency"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Master Qui-Gon", True),
    n("Blaster Proficiency"),
    n("Much To Learn, You Still Have"),
    n("Republic Gunship Wing"),
    n("Rebel Barrier"),
    n("Crash Site Memorial"),
    n("Sai'torr Kal Fas"),
    n("Republic Gunship Wing"),
    n("Nabrun Leids"),
    n("Were You Looking For Me?"),
    n("Let The Wookiee Win", True),
    n("Sense"),
    n("Blaster Proficiency"),
    n("Yoda, You Seek Yoda"),
    n("Guardian's Lightsaber"),
    n("Mace Windu, Master Of The Order"),
    n("Obi-Wan's Journal"),
    n("Meditation"),
    n("Obi-Wan's Lightsaber"),
    n("Obi-Wan Kenobi, Padawan Learner", True),
    n("Into The Garbage Chute, Flyboy", True),
    n("Sorry About The Mess"),
    n("Sense"),
    n("R2-D2 (Artoo-Detoo)"),
    n("Scramble Say The Bits", True),
    n("A Gift"),
    n("Into The Garbage Chute, Flyboy", True),
    n("Master Qui-Gon", True),
    n("Republic Gunship Wing"),
    n("Disarmed"),
    n("Sense"),
    n("Clash Of Sabers"),
    n("Seeking An Audience", True),
    n("Obi-Wan Kenobi, Padawan Learner"),
    n("Clash Of Sabers"),
    n("Heading For The Medical Frigate"),
    n("Imperial Atrocity", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Naboo: Boss Nass' Chambers"),
    n("Sorry About The Mess"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Sorry About The Mess"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Walker Garrison"
DS_CARDS = [
    n("Walker Garrison"),
    n("Close Call", True),
    n("No Escape"),
    n("AT-AT"),
    n("AT-AT Commander"),
    n("Tempest 1"),
    n("Set For Stun"),
    n("Victory", True),
    n("We're In Attack Position Now"),
    n("Admiral Piett"),
    n("Target The Main Generator"),
    n("Close Call", True),
    n("Masterful Move & Endor Occupation"),
    n("Prepared Defenses", True),
    n("Imperial Commander", qty=2),
    n("Blizzard 1"),
    n("U-3PO (Yoo-Threepio)"),
    n("AT-AT Deployment Platform", True),
    n("Jango Fett, The Assassin"),
    n("AT-AT", True),
    n("AT-AT Deployment Platform", True),
    n("Garindan", True),
    n("AT-AT Cannon", True),
    n("General Veers", True),
    n("AT-AT", True),
    n("Darth Vader", True),
    n("General Nevar", True),
    n("Admiral Motti", True),
    n("Executor"),
    n("Fleet Security Protocols"),
    n("You'll Be Dead!", True),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Dark Waters"),
    n("Hoth: Ice Plains (5th Marker)"),
    n("Hoth"),
    n("We're In Attack Position Now"),
    n("Force Push", True),
    n("Target The Main Generator"),
    n("IOTDL"),
    n("Imperial Command"),
    n("DTHACC"),
    n("A Dark Time For The Rebellion", True),
    n("Blizzard 2", True),
    n("Victory"),
    n("Conquest"),
    n("Blizzard 4"),
    n("Grand Moff Tarkin"),
    n("Walker Garrison"),
    n("Cold Feet", True),
    n("Trample"),
    n("Hoth: Main Power Generators (1st Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Grand Admiral Thrawn"),
    n("Black 11"),
    n("Conquest"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = []
DS_ADD = []
