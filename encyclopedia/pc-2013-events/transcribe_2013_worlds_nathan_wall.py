#!/usr/bin/env python3
"""2013 World Championship Day 2: Nathan Wall Xerox Hyperdrive."""
from __future__ import annotations

PLAYER = "Nathan Wall"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 103
LS_SCAN = "2013 Worlds Day 2 p103 Nathan Wall LS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Nathan Wall. Username blank. Email blank. LIGHT. "
    "Deck title Hyperdrive. Event worlds day 2, dated 08/10/13. "
    "Dest as Nathan Wall as written. Do not dest as Nathan Way. "
    "Hyperdrive dested The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Shoot Shoot dested Shoo! Shoo!. "
    "Jayla Seena dested Aayla Secura. "
    "Sen. Padme Amidala dested Senator Padme Amidala. "
    "Obi-Wan Kenobi, Padawan dested Obi-Wan Kenobi, Padawan Learner. "
    "Tatooine City outskirts dested Tatooine: City Outskirts. "
    "Tatooine Watto's junkyard dested Tatooine: Watto's Junkyard. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas. "
    "A Jedi Res. dested A Jedi's Resilience. "
    "Sen. Leia dested Senator Leia Organa. "
    "Guardian's Light dested Guardian's Lightsaber. "
    "Mace Windu Mast dested Mace Windu, Master Of The Order. "
    "Mast. Qui-Gon dested Master Qui-Gon. "
    "Out of Commiss dested Out Of Commission. "
    "The B Shuffle dested The Bith Shuffle. "
    "Naboo Boss Nass dested Naboo: Boss Nass' Chambers. "
    "Obi-Wan Jour dested Obi-Wan's Journal. "
    "Into The Garbage Ch. Flyboy dested Into The Garbage Chute, Flyboy. "
    "Sorry About The Mess & Blaster Prof dested "
    "Sorry About The Mess & Blaster Proficiency. "
    "Qui-Gon Jinn Rel. Mast dested Qui-Gon Jinn, Jedi Master. "
    "Qui-Gon Light dested Qui-Gon Jinn's Lightsaber. "
    "Med dested Meditation. "
    "Clash of Sab dested Clash Of Sabers. "
    "Advantage dested Advantage. "
    "Wesa Got Grand Army dested Wesa Gotta Grand Army. "
    "Dark App dested Dark Approach. "
    "At me and Dang. & Blaster Prof dested "
    "Sorry About The Mess & Blaster Proficiency. "
    "Your Ship dested Your Ship?. "
    "Battle Control dested Traffic Control. "
    "Form left column reprints 37-38 on lines 39-40 are Advantage and "
    "Wesa Gotta Grand Army. "
    "Additional Chasm / Simple Tricks And Nonsense / Aim High moved to Light shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One", True),
    n("Rycar Ryjerd"),
    n("Heading For The Medical Frigate", True),
    n("Control"),
    n("Shoo! Shoo!", True),
    n("Elegant Lightsaber", True),
    n("Maris Brood, Fallen Jedi", True),
    n("Aayla Secura", True),
    n("Senator Padme Amidala", True),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Senator Mon Mothma", True),
    n("Tatooine: City Outskirts"),
    n("Credits Will Do Fine"),
    n("Tatooine: Watto's Junkyard"),
    n("Sai'torr Kal Fas", True),
    n("A Jedi's Resilience", qty=2),
    n("Senator Leia Organa", True),
    n("Guardian's Lightsaber", True),
    n("Yoda Stew"),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Master Qui-Gon", True),
    n("Lucky Shot", True),
    n("Lightsaber Proficiency"),
    n("Out Of Commission"),
    n("The Bith Shuffle"),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan's Journal"),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Qui-Gon Jinn, Jedi Master", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Houjix", qty=2),
    n("Meditation"),
    n("Clash Of Sabers", qty=2),
    n("Advantage"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Dark Approach"),
    n("Rebel Barrier", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", True),
    n("Escape Pod", True, qty=2),
    n("Seeking An Audience", True),
    n("Disarmed", qty=2),
    n("Quick Draw"),
    n("A Remote Planet"),
    n("Blaster Deflection", qty=2),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Your Ship?"),
    n("The Professor", True),
    n("Wise Advice", True),
    n("Ounee Ta"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry"),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Traffic Control", True),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
]
LS_ADD = []
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
