#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Nick Rambo.

Source: 2012BespinRegionals.pdf pages 21–22 notebook dump.
p21 Light / p22 Dark Name Nick Rambo dested Nick Rambo analog leftover 2012 Nats /
player-stubs/Nick_Rambo.wiki. Username blank (no username box).
Do not dest as Nick Olson. Do not dest as a new person.
Do not dest 2012 Nats Nick Rambo 60s again.
"""
from __future__ import annotations

PLAYER = "Nick Rambo"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2012 Bespin Regionals Nick Rambo LS.png"
DS_SCAN = "2012 Bespin Regionals Nick Rambo DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p21 Light / p22 Dark notebook dump. "
    "Name Nick Rambo dested Nick Rambo analog leftover 2012 Nats / "
    "player-stubs/Nick_Rambo.wiki. Username blank. "
    "Do not dest as Nick Olson. Do not dest as a new person. "
    "Do not dest 2012 Nats Nick Rambo 60s again."
)
LS_NOTE = (
    "Notebook dump p21 Light. Name Nick Rambo dested Nick Rambo. Username blank. "
    "Deck Name LOL Nalbandian dested off article. "
    "You Can Either Profit By This dested You Can Either Profit By This... / Or Be Destroyed analog leftover Nats. "
    "TAT: Jabba's Palace dested Tatooine: Jabba's Palace. JP:AC dested Jabba's Palace: Audience Chamber. "
    "Han dested Han Solo True. HFTMF dested Heading For The Medical Frigate. "
    "TAT: Lars' Farm dested Tatooine: Lars' Moisture Farm True. "
    "Y4: Massassi War Room dested Yavin 4: Massassi War Room True. "
    "Luke SITF dested Luke Skywalker, Strong In The Force qty=3. "
    "Padmé dested Padmé Naberrie True qty=2. Chewie Protector dested Chewbacca, Protector analog leftover Nats. "
    "Naked 3PO dested Threepio With His Parts Showing. Artoo BLD dested Artoo, Brave Little Droid True. "
    "Lando w/ Ax dested Lando With Vibro-Ax. Yoda GW dested Yoda, Great Warrior. "
    "LTWW True qty=1 sheet-accurate. Disarmed dest as written. "
    "OOC&TT dested Out Of Commission & Transmission Terminated. SATM&BP dested Sorry About The Mess & Blaster Proficiency. "
    "Eject combo crossed dest Imperial Atrocity True analog leftover + Atrocity True qty=2 at first. "
    "Recar dested Rycar Ryjerd True. IMBATS dested I Must Be Allowed To Speak True. "
    "AFA True IN THE 60. Unique 60 shields 10 sheet-accurate."
)
DS_NOTE = (
    "Notebook dump p22 Dark. Name Nick Rambo dested Nick Rambo. Username blank. "
    "Deck Name I feel bad for Andy Murray dested off article. "
    "Imperial Occupation / Imperial Control dested Imperial Occupation / Imperial Control True analog leftover Nats. "
    "The Hero's Reach dested Maarek Stele, The Emperor's Reach analog leftover. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover. "
    "Darsh Maul dested Darth Maul. Executor dested Executor qty=2 analog leftover Nats. "
    "Control qty=3 unique overcount. Imperial Command qty=3 unique overcount. "
    "MM&EO dested Masterful Move & Endor Occupation qty=2. "
    "Ni Chuba Na?? dested Ni Chuba Na? True analog leftover. "
    "DTHACC dested Do They Have A Code Clearance?. YMSYL dested You May Start Your Landing. "
    "K&D dested Knowledge And Defense True IN THE 60. "
    "Death Star Sentry True joke SUCK IT dested off article. "
    "Oppressive Enforcement crossed dest Battle Order True analog leftover replacement. Unique 60 shields 11."
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
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Padmé Naberrie", True, qty=2),
    n("Princess Leia", True),
    n("Boushh"),
    n("Admiral Ackbar", True),
    n("Chewbacca, Protector"),
    n("Corran Horn"),
    n("IL-19"),
    n("Threepio With His Parts Showing"),
    n("Artoo, Brave Little Droid", True),
    n("Lando With Vibro-Ax"),
    n("Yoda, Great Warrior"),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Tatooine Utility Belt", True),
    n("Let The Wookiee Win", True),
    n("Rebel Leadership", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Don't Forget The Droids", True, qty=2),
    n("Disarmed"),
    n("Blaster Deflection"),
    n("Skywalkers"),
    n("Jedi Levitation", True),
    n("Nabrun Leids"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Run Luke, Run!"),
    n("Gift Of The Mentor"),
    n("Clash Of Sabers"),
    n("Out Of Commission & Transmission Terminated"),
    n("Lightsaber Proficiency"),
    n("Scrambled Transmission", True),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True, qty=2),
    n("Rycar Ryjerd", True),
    n("I Must Be Allowed To Speak", True),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not", True),
    n("Ultimatum", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Battle Plan", True),
    n("Aim High"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Prepared Defenses"),
    n("Hoth: Mountains"),
    n("Hoth: Defensive Perimeter"),
    n("Veers", True),
    n("General Nevar"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Admiral Piett"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Commander Igar", True),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader", True),
    n("Bossk", True),
    n("Darth Maul"),
    n("Victory"),
    n("Conquest", True),
    n("Devastator", True),
    n("Executor", qty=2),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("AT-AT Cannon", True),
    n("Target The Main Generator"),
    n("Control", qty=3),
    n("Imperial Command", qty=3),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Trample", qty=2),
    n("Cold Feet", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Walker Garrison"),
    n("Imbalance & Kintan Strider"),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Prepare For A Surface Attack"),
    n("Ni Chuba Na?", True),
    n("Something Special Planned For Them", True),
    n("Protocol Failure"),
    n("Hoth Blockade"),
    n("Do They Have A Code Clearance?"),
    n("Image Of The Dark Lord"),
    n("We're In Attack Position Now", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("Imperial Detention"),
    n("Come Here You Big Coward", True),
    n("Resistance"),
    n("There Is No Try", True),
    n("Battle Order", True),
]
DS_ADD = []
