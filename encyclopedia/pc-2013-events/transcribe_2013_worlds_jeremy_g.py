#!/usr/bin/env python3
"""2013 World Championship Day 2: Jeremy G Xerox LS TIGIH; DS Same as Day 1 unpublished."""
from __future__ import annotations

PLAYER = "Jeremy G"
USERNAME = "Jedi Jer"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 34
DS_PAGE = 35
LS_SCAN = "2013 Worlds Day 2 p34 Jeremy G LS.png"
DS_SCAN = "2013 Worlds Day 2 p35 Jeremy G DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name JediJer. Username blank on Light. "
    "Deck title I'm just a copy cat. LIGHT. Worlds Day 2. "
    "TIGIH / ICSH dested There Is Good In Him / I Can Save Him. "
    "Endor: Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Luke, Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Qui-Gon w saber dested Qui-Gon Jinn With Lightsaber. "
    "Lando, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Luke, Jedi Knight dested Luke Skywalker, Jedi Knight. "
    "Speak w/ the Council dested Speak With The Jedi Council. "
    "Jedi Lev dested Jedi Levitation. "
    "Odin Neslor combo dested Odin Nesloor & First Aid. "
    "Sorry About The Mess combo dested Sorry About The Mess & Blaster Proficiency. "
    "Mace MOTO dested Mace Windu, Master Of The Order. "
    "Maris Brood dested Maris Brood, Fallen Jedi. "
    "Obi Wan w Lightsaber dested Obi-Wan With Lightsaber. "
    "Leia EP dested Princess Leia Organa. "
    "Han w/ Blaster dested Han With Heavy Blaster Pistol. "
    "Chewie Enraged dested Chewie, Enraged. "
    "AFA dested Anger, Fear, Aggression. "
    "Only Jedi Carry dested Only Jedi Carry That Weapon. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Do or Do Not dested Do, Or Do Not. "
    "Form left column reprints 37–38 on lines 39–40 are I Hope She's All Right "
    "and Mace Windu, Master Of The Order. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jeremy G. Username Jedi Jer. "
    "DARK. Sheet headed Same as Day 1. Worlds Day 1 Dark is not in the published "
    "Day 1 PDF leftover, so the 60 is not copied this leftover."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Corran Horn"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Imperial Atrocity", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("A Jedi's Resilience", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Blaster Deflection", qty=2),
    n("Dark Approach", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Smoke Screen", qty=2),
    n("Sense", qty=2),
    n("Escape Pod", True),
    n("Jedi Levitation", True),
    n("Odin Nesloor & First Aid"),
    n("Clash Of Sabers"),
    n("Swing-And-A-Miss"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Houjix"),
    n("Seeking An Audience", True),
    n("I Hope She's All Right"),
    n("Mace Windu, Master Of The Order"),
    n("Maris Brood, Fallen Jedi"),
    n("Ki-Adi-Mundi", True),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Princess Leia Organa"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Admiral Ackbar", True),
    n("Elegant Lightsaber"),
    n("Home One"),
    n("Coruscant: Jedi Council Chamber"),
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("Wise Advice"),
    n("The Professor", True),
    n("Ultimatum", True),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("Chasm"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
]
LS_ADD = []

DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
