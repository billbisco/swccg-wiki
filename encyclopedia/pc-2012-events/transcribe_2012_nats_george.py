#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: George.

Source: 2012NationalsDay1.pdf pages 23–24 (typed 2010 Xerox, 12 shields).
Name George dested George (2012 US Nationals) analog leftover last-name collision
([[George]] is #REDIRECT [[Eric George]]; Username blank). Username blank.
p23 Light Restore Freedom / Restore Freedom To The Galaxy.
p24 Dark HDv / Hunt Down And Destroy The Jedi.
Do not dest as Eric George. Do not overwrite the existing [[George]] redirect.
Do not dest as a new identified person until analog identifies.
"""
from __future__ import annotations

PLAYER = "George"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2012 US Nationals Day 1 George LS.png"
DS_SCAN = "2012 US Nationals Day 1 George DS.png"
LS_DECK_NAME = "Restore Freedom"
DS_DECK_NAME = "HDv"
NOTE = "Typed 2010 Xerox form. Username blank. Event Name Nationals. Dark Event Date 6/9/12."
LS_NOTE = (
    "Typed 2010 Xerox. Name George dested George (2012 US Nationals) analog leftover collision. "
    "Username blank. LIGHT checked. Deck Name Restore Freedom. Event Name Nationals. "
    "Do not dest as Eric George. Do not overwrite [[George]] redirect. "
    "Do not dest as a new identified person until analog identifies. "
    "Restore Freedom to the Galaxy dested Restore Freedom To The Galaxy True analog leftover Grant. "
    "Luke, Trust Me dested analog leftover Pinto. "
    "X-Wing Laser Cannon dested X-wing Laser Cannon analog leftover Jessica. "
    "All Wings dested All Wings Report In & Darklighter Spin analog leftover Veasey. "
    "Sense & Recoil dested Sense & Recoil In Fear analog leftover Frafjord. "
    "Anger, Fear, Agression dested Anger, Fear, Aggression True analog leftover Fernando. "
    "Shield The Proffessor dested The Professor analog leftover Frafjord. "
    "Shield Wise Advise dested Wise Advice analog leftover Frafjord. "
    "True vs empty kept separate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name George dested George (2012 US Nationals) analog leftover collision. "
    "Username blank. DARK checked. Deck Name HDv. Event Date 6/9/12 Event Name Nationals. "
    "Do not dest as Eric George. Do not overwrite [[George]] redirect. "
    "Do not dest as a new identified person until analog identifies. "
    "Hunt Down dested Hunt Down And Destroy The Jedi True analog leftover. "
    "Coruscant dested Coruscant True analog leftover 2012 MPC Hunt Down. "
    "Ni Chuba Na dested Ni Chuba Na?? True analog leftover Frafjord. "
    "Darth Vader DLOTS dested Darth Vader, Dark Lord Of The Sith analog leftover. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi True analog leftover walker. "
    "Black Leader dested Juno Eclipse, Black Leader True analog leftover walker. "
    "Galen's Fighter dested Rogue Shadow True analog leftover walker. "
    "Galen's Saber dested Galen's Lightsaber, Vader's Gift True analog leftover Frafjord. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers True analog leftover walker. "
    "4-Lom dested 4-LOM With Concussion Rifle True analog leftover Frafjord. "
    "Victory True dest without extra (V) analog leftover Frafjord. "
    "Knowledge, And Defense dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Galen True vs empty kept separate. "
    "Shield Fire Power dested Firepower analog leftover Fernando. "
    "True vs empty kept separate. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Restore Freedom To The Galaxy", True),
    n("Squadron Assignments"),
    n("Luke, Trust Me", True),
    n("Rycar Ryjerd", True),
    n("Yavin 4", True),
    n("Yavin 4: Massassi Headquarters"),
    n("Careful Planning", True),
    n("Kessel"),
    n("Ralltiir"),
    n("Yavin 4: Massassi War Room", True),
    n("Yavin 4: Docking Bay"),
    n("Yavin 4: Massassi Throne Room"),
    n("Yavin 4: Briefing Room"),
    n("Luke Skywalker", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Elyhek Rue"),
    n("Yoda, Great Warrior", True),
    n("Fallen Jedi", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Jek Porkins", True),
    n("Portable Scanner"),
    n("Enhanced Proton Torpedoes", qty=2),
    n("X-wing Laser Cannon"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Red 7"),
    n("Red 6"),
    n("Red Squadron 7", True),
    n("Red Squadron 1"),
    n("Tantive IV", True),
    n("Projection Of A Skywalker", qty=2),
    n("Scrambled Transmission", True),
    n("Demotion", True),
    n("I'm With You Too", True),
    n("Imperial Atrocity", True, qty=2),
    n("Massassi Base Sentry", True),
    n("Legendary Starfighter"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("It Could Be Worse", qty=2),
    n("Rebel Artillery", qty=3),
    n("Power Pivot", qty=2),
    n("Organized Attack", qty=2),
    n("Sense & Recoil In Fear"),
    n("Control & Tunnel Vision"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("I'll Take The Leader"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Aim High"),
    n("The Professor"),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here"),
    n("Weapons Display"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant", True),
    n("Coruscant: Imperial City"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Gift Of The Master", True),
    n("A Sith's Plans", True),
    n("Blockade Flagship: Hallway", True),
    n("Blockade Flagship: Bridge"),
    n("Naboo: Theed Palace Generator Core"),
    n("Endor"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Galen, Secret Apprentice", True),
    n("Galen, Secret Apprentice", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Grand Moff Tarkin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Juno Eclipse, Black Leader", True),
    n("Mara Jade With Lightsaber", True),
    n("Myn Kyneugh", True),
    n("General Nevar", True),
    n("Battle Droid Squad", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Victory", True, qty=2),
    n("Rogue Shadow", True),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Grievous' Lightsabers", True),
    n("Trophy Of A Kill", True, qty=2),
    n("Blaster Rack", True),
    n("Search And Destroy"),
    n("Disarmed"),
    n("Imperial Justice", True),
    n("Revenge Of The Sith", True),
    n("A Sith's Weapon", True),
    n("No Escape"),
    n("Sniper & Dark Strike", qty=2),
    n("Vader's Obsession"),
    n("Force Lightning"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Alter & Collateral Damage"),
    n("Force Push", True),
    n("Force Field", True, qty=2),
    n("Sense"),
    n("Elis Helrot"),
    n("According To My Design", True),
    n("Prepared Defenses", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Fanfare"),
    n("Imperial Detention"),
    n("You Cannot Hide Forever"),
    n("Oppressive Enforcement"),
    n("Death Star Sentry"),
    n("Firepower"),
]
DS_ADD = []
