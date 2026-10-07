#!/usr/bin/env python3
"""2014 US Nationals Day 1 typed printouts: Brad Eier.

Source: Nationals-2014-day-1.pdf pages 30–31 (Holotable-style printouts
with handwritten shield lists and a few OUT/IN notes).
Strike-throughs are omitted; handwritten IN cards are included.
(V) follows a trailing (V) on the printout or a V mark beside the title.
"""
from __future__ import annotations

PLAYER = "Brad Eier"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 30
DS_PAGE = 31
LS_SCAN = "2014 US Nationals Day 1 p30 Brad Eier LS.png"
DS_SCAN = "2014 US Nationals Day 1 p31 Brad Eier DS.png"


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tanus Spijek", True),
    n("Chewbacca, Protector"),
    n("Sai'torr Kal Fas", True),
    n("Anakin's Lightsaber", True),
    n("Tatooine Utility Belt", True),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand"),
    n("Padme Naberrie", True),
    n("Boushh"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Tawss Khaa", True),
    n("Grimtaash"),
    n("Houjix"),
    n("A Gift"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("R2-D2 (Artoo-Detoo)", True),
    n("Obi-Wan's Lightsaber"),
    n("Corran Horn"),
    n("Yoda, Great Warrior"),
    n("Lando Calrissian, Scoundrel"),
    n("Blaster Deflection"),
    n("Leia, Rebel Princess"),
    n("Clash Of Sabers"),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Nabrun Leids"),
    n("Visored Vision", qty=2),
    n("Speak With The Jedi Council"),
    n("Rebel Leadership", True, qty=2),
    n("See-Threepio", True, qty=2),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Wesa Gotta Grand Army"),
    n("Yavin 4: Massassi War Room", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Rycar Ryjerd", True, qty=2),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("Heading For The Medical Frigate"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han", True),
    n("I Must Be Allowed To Speak", True),
    n("Harvest", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Battle Plan"),
    n("Your Ship?", True),
    n("He Can Go About His Business", True),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Weapon Levitation"),
    n("You Are Beaten"),
    n("Force Field", True),
    n("P-59"),
    n("Blockade Flagship: Hallway"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Sith Fury", True),
    n("Imperial Barrier"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Force Lightning", qty=2),
    n("Sniper & Dark Strike"),
    n("Force Push", True),
    n("Sonic Bombardment", True, qty=3),
    n("Sense"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("A Sith's Weapon"),
    n("Disarmed", qty=2),
    n("Garindan", True),
    n("Battle Droid Squad", qty=2),
    n("Imperial Justice", True),
    n("Maul's Sith Infiltrator"),
    n("The Phantom Menace"),
    n("Jango Fett, The Assassin"),
    n("Masterful Move"),
    n("IG-100 MagnaGuard"),
    n("Dengar With Blaster Carbine", True),
    n("Ghhhk"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Trophy Of A Kill", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Dooku's Lightsaber"),
    n("Count Dooku", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Galen Marek, Starkiller", qty=2),
    n("Cloud City: Security Tower", True),
    n("I've Lost Artoo!", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Boba Fett, Prepared Hunter"),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
]
DS_ADD = []
