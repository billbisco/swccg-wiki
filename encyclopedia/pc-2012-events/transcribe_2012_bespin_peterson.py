#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Mark Peterson.

Source: 2012BespinRegionals.pdf pages 19–20.
p19 Light typed 2010 Xerox / p20 Dark typed 2010 Xerox.
Name Mark Peterson dested Mark Peterson analog leftover 2012 Nats /
player-stubs/Mark_Peterson.wiki. Username Lukes Bionic Hand.
Do not dest as Alden Peterson. Do not dest as a new person.
Do not dest 2012 Nats Mark Peterson 60s again.
"""
from __future__ import annotations

PLAYER = "Mark Peterson"
USERNAME = "Lukes Bionic Hand"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 19
DS_PAGE = 20
LS_SCAN = "2012 Bespin Regionals Mark Peterson LS.png"
DS_SCAN = "2012 Bespin Regionals Mark Peterson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p19 Light typed 2010 Xerox / p20 Dark typed 2010 Xerox. "
    "Name Mark Peterson dested Mark Peterson analog leftover 2012 Nats / "
    "player-stubs/Mark_Peterson.wiki. Username Lukes Bionic Hand. "
    "Date 7/14/12 Event Bespin Regionals. "
    "Do not dest as Alden Peterson. Do not dest as a new person. "
    "Do not dest 2012 Nats Mark Peterson 60s again."
)
LS_NOTE = (
    "Typed 2010 Xerox p19 Light. Name Mark Peterson dested Mark Peterson. "
    "Username Lukes Bionic Hand. LIGHT checked. Deck Name JEEDAI dested off article. "
    "We'll Handle This dested We'll Handle This / Duel Of The Fates True analog leftover Consoli. "
    "Anger, Fear, Aggression True IN THE 60. "
    "Your Insight Serves You Well empty IN THE 60 and True shield 9 kept separate. "
    "Fallen Jedi dest as written qty=2. Jedi Advisor dest as written qty=2. "
    "Noooooooooooo! dested Noooooooooooo True analog leftover Arlandson. "
    "Imperial Atrocity True analog leftover clip L40. "
    "Speak With The Jedi Council dest as written qty=3. "
    "Shield 12 empty skip unique 11 sheet-accurate analog leftover clip. Unique 60 shields 11."
)
DS_NOTE = (
    "Typed 2010 Xerox p20 Dark. Name Mark Peterson dested Mark Peterson. "
    "Username Lukes Bionic Hand. DARK checked. Deck Name Wakuhz dested off article. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control True analog leftover Nats. "
    "Knowledge And Defense True IN THE 60. "
    "Imperial Decree empty line 6 and True line 22 kept separate. "
    "Ni Chuba Na dested Ni Chuba Na? True analog leftover. "
    "Garindian dested Garindan True analog leftover Nats. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Nats. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Nats. "
    "Marqarid dested Marquand In Blizzard 6 analog leftover Nats. "
    "Tempest 1 dested analog leftover Nats clip L40. "
    "We'll Let Fate A Decide Huh dested We'll Let Fate-a Decide, Huh? analog leftover. "
    "Shield 12 empty skip unique 11 sheet-accurate analog leftover Nats. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates", True),
    n("Anger, Fear, Aggression", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Heading For The Medical Frigate"),
    n("A Jedi's Plans"),
    n("Your Insight Serves You Well"),
    n("Projection Of A Skywalker"),
    n("Honor Of The Jedi"),
    n("Coruscant: Jedi Archives"),
    n("Coruscant: Night Club"),
    n("Naboo: Theed Palace Generator"),
    n("Temporary Foothold"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Fallen Jedi", qty=2),
    n("Yoda, Senior Council Member", True),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("Jedi Advisor", qty=2),
    n("Mace Windu", True, qty=2),
    n("Depa Billaba"),
    n("Plo Koon"),
    n("Ki-Adi-Mundi", True),
    n("IL-19"),
    n("Elegant Lightsaber"),
    n("Let The Wookiee Win", True),
    n("Jedi Lightsaber", True, qty=2),
    n("Wokling", True),
    n("I Hope She's All Right"),
    n("Obi-Wan's Lightsaber"),
    n("Evacuation Control", True),
    n("Menace Fades"),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Hindsight", True),
    n("Imperial Atrocity", True),
    n("Smoke Screen", qty=2),
    n("Noooooooooooo", True),
    n("Seeking An Audience", True),
    n("Jedi Levitation", True),
    n("Are You Brain Dead?!", qty=2),
    n("Alter"),
    n("Blaster Deflection", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Clash Of Sabers"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Speak With The Jedi Council", qty=3),
    n("Sense", qty=2),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Knowledge And Defense", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Imperial Decree"),
    n("You May Start Your Landing"),
    n("Ni Chuba Na?", True),
    n("Endor Shield", True),
    n("Hoth: Mountains"),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Masterful Move & Endor Occupation"),
    n("Cease Fire!", qty=2),
    n("Where Are You Taking This ... Thing?"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Garindan", True),
    n("Commander Igar", True),
    n("Blockade Support Ship"),
    n("Imperial Decree", True),
    n("Conquest", True),
    n("Victory"),
    n("Cold Feet", True, qty=2),
    n("Image Of The Dark Lord", True),
    n("Hoth Blockade"),
    n("Grand Moff Tarkin", True),
    n("Admiral Motti", True),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader", True),
    n("General Nevar"),
    n("Veers", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Hoth: Defensive Perimeter"),
    n("U-3PO"),
    n("Grand Admiral Thrawn"),
    n("Admiral Piett"),
    n("We're In Attack Position Now", qty=2),
    n("No Escape"),
    n("Do They Have A Code Clearance?"),
    n("Control", qty=2),
    n("Walker Garrison"),
    n("Prepared Defenses"),
    n("Trample", qty=2),
    n("Flagship Executor", qty=2),
    n("Alert My Star Destroyer"),
    n("Tarkin's Bounty", True),
    n("Imperial Command", qty=2),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Secret Plans"),
]
DS_ADD = []
