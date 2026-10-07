#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Marc Hanson.

Source: 2012NationalsDay1.pdf pages 28–29 (handwritten notebook dump).
Name Marc Hanson dested Marc Hanson as written. Username blank.
p28 Light Rescue The Princess. p29 Dark Vader's Lightsaber.
Do not dest as Matt Hanson. Do not dest as a new identified person until analog identifies.
"""
from __future__ import annotations

PLAYER = "Marc Hanson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 28
DS_PAGE = 29
LS_SCAN = "2012 US Nationals Day 1 Marc Hanson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Marc Hanson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten notebook dump. Username blank. Name Marc Hanson."
LS_NOTE = (
    "Handwritten notebook. Name Marc Hanson dested Marc Hanson as written. "
    "Username blank. Light Side heading. Analog leftover generate empty dest as written. "
    "Do not dest as Matt Hanson. Do not dest as a new identified person until analog identifies. "
    "Rescue The Princess/Sometimes I Amaze Even Myself dested Rescue The Princess / Sometimes I Amaze Even Myself analog leftover Cullen. "
    "Command Vanden Willard dested Commander Vanden Willard analog leftover. "
    "Princess Organa dested Princess Organa analog leftover. "
    "Path of Least Resistance + Revealed dested Path Of Least Resistance & Revealed analog leftover combo. "
    "Sorry About The Mess + Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency analog leftover Ziagos. "
    "Rebel crossed Reinforcements dested Rebel Reinforcements analog leftover. "
    "Alter + Friendly Fire dested Alter & Friendly Fire analog leftover combo. "
    "Bothanui dested Bothawui analog leftover. "
    "Leia of Alderaan dested Leia Of Alderaan analog leftover. "
    "Unique 60. No shields listed."
)
DS_NOTE = (
    "Handwritten notebook. Name Marc Hanson dested Marc Hanson as written. "
    "Username blank. Dark Side heading. Analog leftover generate empty dest as written. "
    "Do not dest as Matt Hanson. Do not dest as a new identified person until analog identifies. "
    "Start dested Vader's Lightsaber first listed analog leftover notebook. "
    "It's worse dested It's Worse analog leftover Fernando. "
    "Lt. Pol Treidum dested Lt. Pol Treidum analog leftover. "
    "IM4-099 (Eyeeminfour) dested IM4-099 analog leftover. "
    "Sergeant Torrent dested leftover_xerox as written. "
    "Darth Vader, Dark Lord of the Sith dested Darth Vader, Dark Lord Of The Sith analog leftover George. "
    "A Day Long Remembered dested analog leftover. "
    "Weapon Of An Ungrateful Son dested analog leftover Jan. "
    "Bad Feeling Have I dested analog leftover. "
    "Unique 60. No shields listed."
)

def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)

LS_START = "Rescue The Princess / Sometimes I Amaze Even Myself"
LS_CARDS = [
    n("Rescue The Princess / Sometimes I Amaze Even Myself"),
    n("It Could Be Worse", qty=3),
    n("Crack Shot"),
    n("Mercenary Armor"),
    n("Rebel Trooper", qty=3),
    n("Commander Vanden Willard"),
    n("Princess Organa"),
    n("Death Star: Detention Block Corridor"),
    n("Death Star: Docking Bay 327"),
    n("Yavin 4"),
    n("Yavin 4: Massassi Ruins"),
    n("Yavin 4: Jungle"),
    n("Rebel Guard", qty=2),
    n("Yavin 4: Docking Bay", qty=2),
    n("Rebel Squad Leader"),
    n("Yavin 4: Briefing Room"),
    n("Yavin 4: Massassi War Room"),
    n("Surprise Assault", qty=3),
    n("Narrow Escape", qty=2),
    n("Yavin 4: Massassi Headquarters"),
    n("I'm Here To Rescue You"),
    n("Rebel Trooper Recruit"),
    n("Chewbacca, Protector"),
    n("Blaster Rifle"),
    n("Yavin 4 Trooper"),
    n("Undercover"),
    n("Mon Mothma"),
    n("Path Of Least Resistance & Revealed"),
    n("Bacta Tank"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("General Dodonna"),
    n("Rebel Commander", qty=2),
    n("Cell 2187"),
    n("Rebel Reinforcements"),
    n("Han's Heavy Blaster Pistol"),
    n("Medium Repeating Blaster Cannon"),
    n("Y-wing", qty=2),
    n("Gold Leader In Gold 1"),
    n("Effective Repairs"),
    n("Alter & Friendly Fire", qty=2),
    n("FX-7"),
    n("Disruptor Pistol", qty=2),
    n("Forest"),
    n("TK-422"),
    n("Bothawui"),
    n("Leia Of Alderaan"),
    n("Reflection"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Vader's Lightsaber"
DS_CARDS = [
    n("Vader's Lightsaber"),
    n("Stormtrooper Utility Belt", qty=4),
    n("Grand Moff Tarkin"),
    n("The Empire's Back", qty=2),
    n("Imperial Squad Leader"),
    n("Put All Sections On Alert"),
    n("Navy Trooper"),
    n("Stormtrooper", qty=3),
    n("Imperial Trooper Guard", qty=3),
    n("Imperial Commander", qty=2),
    n("Death Star Trooper", qty=3),
    n("Death Star: Docking Bay 327"),
    n("It's Worse"),
    n("Commence Primary Ignition"),
    n("Hoth"),
    n("Lt. Pol Treidum"),
    n("Death Star Sentry"),
    n("Alderaan"),
    n("Collateral Damage", qty=2),
    n("Death Star: Detention Block Corridor"),
    n("Dagobah"),
    n("Superlaser"),
    n("We Have A Prisoner"),
    n("IM4-099"),
    n("Death Star Gunner", qty=2),
    n("Imperial Blaster", qty=2),
    n("Sergeant Torrent"),
    n("Death Star: Detention Block Control Room"),
    n("Death Star: War Room"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("A Day Long Remembered"),
    n("Death Star: Conference Room"),
    n("Death Star: Central Core"),
    n("Trooper Charge"),
    n("Lieutenant Suba"),
    n("Weapon Levitation"),
    n("Yavin 4"),
    n("Chief Bast"),
    n("Tatooine"),
    n("Blaster Rifle"),
    n("Elite Squadron Stormtrooper", qty=2),
    n("Weapon Of An Ungrateful Son"),
    n("Death Star"),
    n("Reactor Terminal"),
    n("Bad Feeling Have I"),
]
DS_SHIELDS = []
DS_ADD = []
