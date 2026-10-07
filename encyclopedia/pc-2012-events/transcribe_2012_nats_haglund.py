#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Chris Haglund.

Source: 2012NationalsDay1.pdf page 25 (handwritten notebook dump, both sides).
Name Chris Haglund dested Chris Haglund as written (circled at bottom). Username blank.
p25 Light Anger, Fear, Aggression / Dark Knowledge And Defense.
Do not dest as a new identified person until analog identifies.
"""
from __future__ import annotations

PLAYER = "Chris Haglund"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 25
DS_PAGE = 25
LS_SCAN = "2012 US Nationals Day 1 Chris Haglund LS.png"
DS_SCAN = "2012 US Nationals Day 1 Chris Haglund DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten notebook dump both sides on p25. Username blank. Name Chris Haglund circled."
LS_NOTE = (
    "Handwritten notebook. Name Chris Haglund dested Chris Haglund as written. "
    "Username blank. Light circled. Analog leftover generate empty dest as written. "
    "Do not dest as a new identified person until analog identifies. "
    "Anger, Fear, Aggression x1d 05 dested Anger, Fear, Aggression True analog leftover Casey. "
    "Hoth: MPG dested Hoth: Main Power Generators analog leftover Wirfs. "
    "Hoth dested Hoth analog leftover. "
    "Haven dested Haven analog leftover Erwin. "
    "Hoth: Echo Command Center dested Hoth: Echo Command Center (War Room) analog leftover Booker. "
    "3 clouds dested Clouds analog leftover Finley. "
    "Echo Base OPS dested Echo Base Operations analog leftover. "
    "Civil disorder dested Civil Disorder analog leftover Consoli. "
    "All Wings Report In dested All Wings Report In & Darklighter Spin analog leftover Veasey. "
    "Shocking Info + Grimtaash dested Shocking Information & Grimtaash analog leftover combo. "
    "It could be worse dested It Could Be Worse analog leftover George. "
    "Owen Lars + Beru Lars dested Owen Lars & Beru Lars analog leftover. "
    "T. Bana Gas Miner dested Tibanna Gas Miner analog leftover. "
    "war shelter wind chimes dested Nar Shaddaa Wind Chimes analog leftover Cooleo. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon analog leftover Booker. "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1 analog leftover Howland. "
    "X-wings dested X-wing analog leftover. "
    "True vs empty kept separate. Unique 60. No shields listed."
)
DS_NOTE = (
    "Handwritten notebook. Name Chris Haglund dested Chris Haglund as written. "
    "Username blank. Dark circled. Analog leftover generate empty dest as written. "
    "Do not dest as a new identified person until analog identifies. "
    "Knowledge And Defense x1d 05 dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Crossfire dested Crossfire analog leftover. "
    "Ni Chuba Na dested Ni Chuba Na?? True analog leftover Anderson. "
    "Ability, Ability, Ability dested analog leftover Booker. "
    "Kashyyyk: Slaving Camp Headquarters dested analog leftover. "
    "Combat Readiness dested Combat Readiness analog leftover. "
    "Presence of the Force dested Presence Of The Force analog leftover. "
    "Dread Imperial Star (Dest x2) dested Imperial-Class Star Destroyer analog leftover Jessica. "
    "It's worse dested It's Worse analog leftover Fernando. "
    "Short-range Fighters dested Short Range Fighters analog leftover Burgt. "
    "Dark Maneuvers + Tallon Roll dested Dark Maneuvers & Tallon Roll analog leftover SAN. "
    "OS-72-1 dested OS-72-1 In Obsidian 1 analog leftover Thornton. "
    "U-3PO dested U-3PO analog leftover Shaw. "
    "Dreadnaught-Class Heavy Cruiser dested analog leftover. "
    "True vs empty kept separate. Unique 62 sheet-accurate. No shields listed."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Hoth: North Ridge"),
    n("Hoth: Main Power Generators"),
    n("Hoth"),
    n("Careful Planning"),
    n("Wokling"),
    n("A New Secret Base"),
    n("Haven", qty=2),
    n("Corulag"),
    n("Hoth: Echo Corridor"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Clouds", qty=3),
    n("Incom Corporation"),
    n("Echo Base Operations"),
    n("Civil Disorder"),
    n("Rebel Fleet", qty=2),
    n("Organized Attack", qty=4),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Shocking Information & Grimtaash"),
    n("It Could Be Worse", qty=2),
    n("Mirax Terrik"),
    n("Luke Skywalker"),
    n("Commander Evram Lajaie"),
    n("Owen Lars & Beru Lars"),
    n("Lieutenant Blount"),
    n("Melas"),
    n("Tibanna Gas Miner", qty=5),
    n("Nar Shaddaa Wind Chimes"),
    n("Han, Chewie, And The Falcon"),
    n("Wedge In Red Squadron 1"),
    n("X-wing", qty=15),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Knowledge And Defense"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Crossfire"),
    n("Ni Chuba Na??", True),
    n("Ability, Ability, Ability"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Combat Readiness"),
    n("Kashyyyk"),
    n("Presence Of The Force"),
    n("Imperial-Class Star Destroyer", qty=2),
    n("Lateral Damage", qty=2),
    n("Gravity Shadow", qty=2),
    n("It's Worse"),
    n("Counter Assault", qty=6),
    n("Short Range Fighters", qty=3),
    n("Tallon Roll"),
    n("Dark Maneuvers", qty=3),
    n("Dark Maneuvers & Tallon Roll"),
    n("All Power To Weapons", qty=4),
    n("OS-72-1 In Obsidian 1", qty=4),
    n("U-3PO"),
    n("TIE Scout", qty=16),
    n("Obsidian Squadron TIE"),
    n("Scythe Squadron TIE", qty=2),
    n("Dreadnaught-Class Heavy Cruiser", qty=3),
    n("Kessel"),
    n("Kiffex"),
]
DS_SHIELDS = []
DS_ADD = []
