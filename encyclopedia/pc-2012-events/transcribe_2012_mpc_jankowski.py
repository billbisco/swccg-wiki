#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Wojciech Jankowski.

Source: 2012mpcday1.pdf pages 95–96 (2010 form).
Name Wojciech Jankowski dested Wojciech Jankowski (analog empty; pack player-stubs).
p95 Light. p96 Dark. Username box blank.
"""
from __future__ import annotations

PLAYER = "Wojciech Jankowski"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 95
DS_PAGE = 96
LS_SCAN = "2012 Match Play Championship Day 1 Wojciech Jankowski LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Wojciech Jankowski DS.png"
LS_DECK_NAME = "Speeder Celebration"
DS_DECK_NAME = "Rambo Trooper"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Wojciech Jankowski dested Wojciech Jankowski. "
    "Analog empty. Username box blank. LIGHT checked. "
    "Deck Name Speeder Celebration. Event Date/Name blank. "
    "Email [redacted] dest notes only. "
    "Line 1 remnant Massassi Thr dested Yavin 4: Massassi Throne Room. "
    "Sandspeeder x8. Rebel Snowspeeder x2. "
    "Dash in Rogue 10 dested Dash In Rogue 10 without True (no (V) reprint). General Crix Madine dested without True. "
    "Tat: Celebration dested Tatooine: Celebration x2. "
    "Golden Laser Battery dested Laser Cannon Battery. "
    "Planet Defender Ion Cannon dested Planet Defender Ion Cannon True. "
    "General Crix Madine dested General Crix Madine True. "
    "Rebel Cell sites dested Rebel Cell - Situation Room / Monitoring Station / Perimeter / Hidden Landing Site. "
    "Wedge of Time dested as written True. "
    "Uncivilized Settlements dested as written True. "
    "Strike Force dested Strikeforce True. "
    "Tatooine (EP1) dested Tatooine (Coruscant). "
    "Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Wojciech Jankowski dested Wojciech Jankowski. "
    "Analog empty. Username box blank. DARK checked. "
    "Deck Name Rambo Trooper. Event Date/Name blank. "
    "Line 1 remnant Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "Coruscant: Emp. City dested Coruscant: Imperial City. "
    "Imp Academy Training dested Imperial Academy Training. "
    "Imperial Stormtrooper True then empty x8 kept separate. "
    "Ghhhk & Those Rebels dested Ghhhk & Those Rebels Won't Escape Us True. "
    "Darth Vader, Clone Machine dested Darth Vader, Dark Lord Of The Sith x5. "
    "Galen's Fighter dested Rogue Shadow True. "
    "Galen dested Galen Marek, Starkiller. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Lightsaber Passages dested Lightsaber Proficiency. "
    "Coruscant dested Coruscant (Dark). "
    "Darklure Fire dested as written. "
    "Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Sandspeeder", qty=8),
    n("Rebel Snowspeeder", qty=2),
    n("Dash In Rogue 10"),
    n("Desperate Tactics", qty=2),
    n("Tatooine: Celebration", qty=2),
    n("Slight Weapons Malfunction", qty=3),
    n("Dual Laser Cannon", True, qty=2),
    n("Heavy Turbolaser Battery"),
    n("Kin Kian"),
    n("Captain Verrack"),
    n("Rebel Leadership", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Home One"),
    n("Laser Cannon Battery"),
    n("Planet Defender Ion Cannon", True),
    n("Advantage", True),
    n("General Crix Madine"),
    n("On Target"),
    n("Rebel Cell - Situation Room", True),
    n("Hoth: Echo Command Center"),
    n("Rebel Cell - Monitoring Station"),
    n("Medium Repeating Blaster Cannon"),
    n("Artillery Remote"),
    n("Wes Janson"),
    n("Rapid Fire"),
    n("Admiral Ackbar", True),
    n("Rebel Cell - Perimeter", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Combined Fleet Action"),
    n("Dual Laser Cannon"),
    n("Spiral"),
    n("Commander Luke Skywalker", True),
    n("Dack Ralter", True),
    n("Wokling", True),
    n("Superficial Damage"),
    n("Wedge Of Time", True),
    n("Uncivilized Settlements", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Strikeforce", True),
    n("Hidden Base", True),
    n("Tatooine (Coruscant)"),
    n("Rebel Cell - Hidden Landing Site"),
    n("Anger, Fear, Aggression", True),
    n("Home One: War Room"),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("The Professor"),
    n("Aim High"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Traffic Control"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses"),
    n("Endor"),
    n("General Veers"),
    n("Imperial Stockpile", True),
    n("Blaster Rifle", True),
    n("Imperial Academy Training"),
    n("Drop!", True),
    n("Endor Shield"),
    n("Strategic Reserves", True),
    n("Jabba's Palace: Audience Chamber"),
    n("I Want That Ship"),
    n("Tatooine: Jabba's Palace", qty=2),
    n("Imperial Domination"),
    n("You Cannot Hide Forever"),
    n("Signal", qty=4),
    n("Blast Points", qty=2),
    n("Sneak Attack"),
    n("Imperial Stormtrooper", True),
    n("Imperial Stormtrooper", qty=8),
    n("Executor"),
    n("Elis Helrot"),
    n("Darklure Fire"),
    n("Ghhhk & Those Rebels Won't Escape Us", True),
    n("Operational As Planned", True),
    n("Operational As Planned"),
    n("Darth Vader's Lightsaber"),
    n("Search And Destroy", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=5),
    n("Imperial Dominator"),
    n("There'll Be Hell To Pay"),
    n("Grand Moff Tarkin", True),
    n("Juno Eclipse, Black Leader"),
    n("Lightsaber Proficiency"),
    n("Grand Admiral Thrawn"),
    n("Rogue Shadow", True),
    n("Galen Marek, Starkiller"),
    n("A Sith's Plans", True),
    n("Coruscant (Dark)"),
    n("Knowledge And Defense"),
    n("Allegations Of Corruption"),
    n("Surface Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("On The Hunt"),
    n("Reactor Terminal"),
    n("Oppressive Enforcement"),
    n("Fanfare"),
    n("Resistance"),
    n("Battle Order"),
    n("Firepower"),
    n("Abyss"),
    n("Secret Plans"),
    n("Imperial Detention"),
]
DS_ADD = []
