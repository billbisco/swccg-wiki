#!/usr/bin/env python3
"""2013 World Championship Day 3 typed Print Form: Vikram Bali Light."""
from __future__ import annotations

PLAYER = "Vikram Bali"
USERNAME = "DVD ROTS"
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 4
DS_PAGE = 0
LS_SCAN = "2013 Worlds Day 3 p04 Vikram Bali LS.png"
DS_SCAN = ""
NOTE = "Typed 2013 Xerox Print Form. Username DVD ROTS. Line 43 Sense & Recoil In Fear struck, handwritten Sense. Line 59 Sorry About The Mess & Blaster Proficiency struck, handwritten Clash Of Sabers."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Coruscant: Jedi Council Chamber"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Insurrection & Aim High"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Your Insight Serves You Well"),
    n("Scrambled Transmission", True),
    n("Sai'torr Kal Fas", True),
    n("Honor Of The Jedi"),
    n("Home One: War Room"),
    n("Yavin 4: Massassi War Room", True),
    n("Home One: Docking Bay"),
    n("Hoth: Echo Docking Bay"),
    n("Coruscant: Docking Bay"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Yoda, Master Of The Force"),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan Kenobi", True),
    n("Leia", True),
    n("Padmé Naberrie", True),
    n("Threepio With His Parts Showing"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Tantive IV", True),
    n("Jedi Lightsaber", True, qty=2),
    n("Luke's Lightsaber"),
    n("Mantellian Savrip"),
    n("Seeking An Audience", True),
    n("Strikeforce", True),
    n("Much To Learn, You Still Have"),
    n("Let The Wookiee Win", True),
    n("Sense"),
    n("Control & Tunnel Vision"),
    n("Rebel Leadership", True, qty=3),
    n("Blaster Deflection"),
    n("Fallen Portal"),
    n("Under Attack"),
    n("Impressive, Most Impressive", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Are You Brain Dead?!"),
    n("Clash Of Sabers"),
    n("Hear Me Baby, Hold Together", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
]
LS_ADD = []

DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
