#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Steve Skilton Xerox TIGIH. Dark unpublished."""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 24
DS_PAGE = 24
LS_SCAN = "2013 Texas Mini Worlds Day 1 p24 Steve Skilton LS.png"
DS_SCAN = ""
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Steve Skilton. Username blank. "
    "Deck Name Baroni's TIGIH. LIGHT checked. Event Date and Event Name blank. "
    "No Dark sheet. Hub Dark stays empty. "
    "Do not rewrite the 2013 MPC Steve S., Worlds, or SoCal Steve Skilton leftovers. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "He Can Go crossed, Insight dested Your Insight Serves You Well. "
    "Scrambled dested Scrambled Transmission. "
    "Honor of the Jedi dested Honor Of The Jedi "
    "(LTWW and Uncanny Foresight on that line are crossed aborted writes). "
    "SATM dested Sorry About The Mess & Blaster Proficiency. "
    "Speak w/ Council dested Speak With The Jedi Council. "
    "Heading for the Med dested Heading For The Medical Frigate. "
    "Atrocity dested Imperial Atrocity. "
    "Projection dested Projection Of A Skywalker. "
    "Sai Torr dested Sai'torr Kal Fas. "
    "Mace MOTO dested Mace Windu, Master Of The Order. "
    "Yoda MOTF dested Yoda, Master Of The Force. "
    "Wesa dested Wesa Gotta Grand Army. "
    "Princess Leia RP dested Leia, Rebel Princess. "
    "Ackbar dested Admiral Ackbar. "
    "Screaming Lando dested Lando Calrissian, Scoundrel. "
    "JSJK dested Luke Skywalker, Jedi Knight. "
    "Qui Gons saber dested Qui-Gon Jinn's Lightsaber. "
    "Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "H1:WR dested Home One: War Room. "
    "JCC dested Coruscant: Jedi Council Chamber. "
    "Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "H,C,F dested Han, Chewie, And The Falcon. "
    "EPP Obi dested Obi-Wan With Lightsaber. "
    "Seeking dested Seeking An Audience. "
    "Carry weapon dested Only Jedi Carry That Weapon. "
    "Business dested He Can Go About His Business. "
    "Sentry dested Yavin Sentry. "
    "Tragedy dested A Tragedy Has Occurred. "
    "Weapons Disp dested Weapons Display. "
    "Professor dested The Professor. "
    "Tricks + Nonsense dested Simple Tricks And Nonsense. "
    "Do or Do Not dested Do, Or Do Not. "
    "Insight Shield dested Your Insight Serves You Well. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "Form left column reprints 37-38 on extra 37-38 are Wesa Gotta Grand Army "
    "and Leia, Rebel Princess. "
    "Unique overcounts sheet-accurate: Sense x3, Let The Wookiee Win x2, "
    "Escape Pod x2, Mace Windu x2, Rebel Leadership x2, "
    "Wesa Gotta Grand Army x3, Han, Chewie, And The Falcon x2, "
    "Lando Calrissian, Scoundrel x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "No Dark sheet in the Day 1 PDF for Steve Skilton. Hub Dark stays empty. "
    "Do not rewrite the 2013 MPC Steve S., Worlds, or SoCal Steve Skilton leftovers."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Sense", qty=3),
    n("Weapon Levitation"),
    n("Anger, Fear, Aggression"),
    n("I Feel The Conflict"),
    n("Quick Draw", True),
    n("Wokling"),
    n("Your Insight Serves You Well"),
    n("Projection Of A Skywalker"),
    n("Imperial Atrocity"),
    n("Houjix"),
    n("Heading For The Medical Frigate"),
    n("Speak With The Jedi Council"),
    n("Impressive, Most Impressive"),
    n("A Jedi's Resilience"),
    n("Scrambled Transmission"),
    n("Blaster Deflection"),
    n("Naboo: Battle Plains"),
    n("Rebel Leadership"),
    n("Sai'torr Kal Fas"),
    n("Draw Their Fire"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Let The Wookiee Win", qty=2),
    n("Honor Of The Jedi"),
    n("Escape Pod", qty=2),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon"),
    n("Master Qui-Gon", True),
    n("Yoda, Master Of The Force"),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Leia, Rebel Princess", True),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Seeking An Audience", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("He Can Go About His Business"),
    n("Yavin Sentry"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Weapons Display"),
    n("The Professor"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
]
LS_ADD = [
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here"),
    n("Chasm"),
]

DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
