#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Nick Rambo.

Source: 2012NationalsDay1.pdf pages 62–63 (handwritten 2010 Xerox, 12 shields).
p62 Dark / p63 Light Name Nick Rambo Username RamboIrish dested Nick Rambo analog leftover empty.
Pack player-stubs/Nick_Rambo.wiki.
"""
from __future__ import annotations

PLAYER = "Nick Rambo"
USERNAME = "RamboIrish"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 63
DS_PAGE = 62
LS_SCAN = "2012 US Nationals Day 1 Nick Rambo LS.png"
DS_SCAN = "2012 US Nationals Day 1 Nick Rambo DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Nick Rambo dested Nick Rambo analog leftover empty. "
    "Username RamboIrish. Event Name Nationals 2012. Do not dest as Nick Olson."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Nick Rambo dested Nick Rambo analog leftover empty. "
    "Username RamboIrish. LIGHT checked. Event Name Nationals 2012. "
    "Deck Name TRM stays off the article. "
    "LS_START You Can Either Profit By This... / Or Be Destroyed analog leftover Olson. "
    "Han dested Han Solo True analog leftover Olson. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "Luke Skywalker, SITF dested Luke Skywalker, Strong In The Force analog leftover Olson x3. "
    "Chewie Protector dested Chewbacca, Protector analog leftover Olson. "
    "Naked 3PO dested Threepio With His Parts Showing analog leftover Olson. "
    "Artoo BLD dested Artoo, Brave Little Droid True analog leftover Olson. "
    "LTWW dested Let The Wookiee Win True analog leftover Brady x2. "
    "OOC&TT dested Out Of Commission & Transmission Terminated analog leftover Olson. "
    "SATM&BP dested Sorry About The Mess & Blaster Proficiency analog leftover. "
    "IMBATS dested I Must Be Allowed To Speak True analog leftover Olson. "
    "Sai'torr dested Sai'torr Kal Fas True analog leftover Olson Virtual Block. "
    "Eject combo dested Eject! Eject! Eject! & Imperial Atrocity analog leftover Olson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Shield 8 Let's Keep A Little Optimism Here crossed no replacement skip. Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Nick Rambo dested Nick Rambo analog leftover empty. "
    "Username RamboIrish. DARK checked. Event Name Nationals 2012. "
    "Deck Name This day Aria stays off the article. "
    "Imperial Occupation / Imperial Control dested Imperial Occupation / Imperial Control True analog leftover Olson. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover George. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover. "
    "Line 20 crossed dest We're In Attack Position Now analog leftover Olson replacement. "
    "Executor dested Executor analog leftover Olson x2. "
    "Imperial Command dested Imperial Command analog leftover Brady x3 unique overcount. "
    "Control dested Control leftover_xerox x3 unique overcount. "
    "MM&EO dested Masterful Move & Endor Occupation analog leftover x2. "
    "Line 45 crossed dest Cold Feet True analog leftover replacement. "
    "Line 46 crossed dest We're In Attack Position Now True analog leftover replacement unique overcount mixed V. "
    "Imbalance & Kintan Strider dested Imbalance & Kintan Strider analog leftover 2014 Worlds. "
    "YMSYL dested You May Start Your Landing analog leftover. "
    "DTHACC dested Do They Have A Code Clearance? analog leftover. "
    "TTMG dested Target The Main Generator analog leftover. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Shield 12 Oppressive Enforcement crossed dest A Useless Gesture True analog leftover replacement. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han Solo", True),
    n("Heading For The Medical Frigate"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Home One: War Room"),
    n("Yavin 4: Massassi War Room", True),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Padmé Naberrie", True, qty=2),
    n("Princess Leia", True),
    n("Boushh"),
    n("Chewbacca, Protector"),
    n("Corran Horn"),
    n("Lando With Vibro-Ax"),
    n("Admiral Ackbar", True),
    n("Yoda, Great Warrior"),
    n("Threepio With His Parts Showing"),
    n("IL-19"),
    n("Artoo, Brave Little Droid", True),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Tatooine Utility Belt", True),
    n("Rebel Leadership", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Don't Forget The Droids", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Skywalkers"),
    n("Gift Of The Mentor"),
    n("Jedi Levitation", True),
    n("Nabrun Leids"),
    n("Run Luke, Run!"),
    n("Clash Of Sabers"),
    n("Blaster Deflection"),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("I Must Be Allowed To Speak", True),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Imperial Atrocity", True),
    n("Eject! Eject! Eject! & Imperial Atrocity"),
    n("Lightsaber Proficiency"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("The Professor", True),
    n("Do, Or Do Not", True),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum", True),
    n("Your Insight Serves You Well", True),
    n("Aim High", True),
    n("Affect Mind"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Prepared Defenses"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
    n("Darth Vader", True),
    n("Juno Eclipse, Black Leader"),
    n("General Nevar"),
    n("Admiral Piett"),
    n("Grand Admiral Thrawn"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Grand Moff Tarkin", True),
    n("Commander Igar"),
    n("Admiral Motti", True),
    n("Veers", True),
    n("Darth Maul"),
    n("Bossk", True),
    n("We're In Attack Position Now"),
    n("Victory"),
    n("Conquest", True),
    n("Devastator", True),
    n("Executor", qty=2),
    n("AT-AT Cannon", True),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("Imperial Command", qty=3),
    n("Control", qty=3),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Trample", qty=2),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Cold Feet", True, qty=2),
    n("We're In Attack Position Now", True),
    n("Imbalance & Kintan Strider"),
    n("Walker Garrison"),
    n("Imperial Decree"),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Prepare For A Surface Attack"),
    n("Ni Chuba Na??", True),
    n("Hoth Blockade"),
    n("Image Of The Dark Lord", True),
    n("Do They Have A Code Clearance?"),
    n("Protocol Failure"),
    n("Something Special Planned For Them", True),
    n("Target The Main Generator"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try", True),
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("Allegations Of Corruption", True),
    n("Secret Plans", True),
    n("Abyss", True),
    n("Imperial Detention"),
    n("Come Here You Big Coward", True),
    n("Resistance"),
    n("A Useless Gesture", True),
]
DS_ADD = []
