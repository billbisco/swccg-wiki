#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Anthony Massung.

Source: 2014-Alderaan-Regionals.pdf pages 3–4 (2010 form).
"""
from __future__ import annotations

PLAYER = "Anthony Massung"
USERNAME = ""
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2014 Alderaan Regionals p03 Anthony Massung LS.png"
DS_SCAN = "2014 Alderaan Regionals p04 Anthony Massung DS.png"
NOTE = "Handwritten Xerox form."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / Aggressive Negotiations"
LS_CARDS = [
    n("Republic At War / Aggressive Negotiations"),
    n("Geonosis: Forward Command Center"),
    n("Begun, The Clone War Has"),
    n("Heading For The Medical Frigate", True),
    n("Wokling", True),
    n("Nick Of Time", True),
    n("Rogue Squadron Tactics"),
    n("Han Solo, Innocent Scoundrel"),
    n("Slight Weapons Malfunction"),
    n("AT-RT", qty=9),
    n("Dual Laser Cannon", True, qty=5),
    n("Muunilinst: Republic Landing Site"),
    n("Acclamator-Class Assault Ship", qty=2),
    n("Alderaan Consular Ship"),
    n("Sensor Panel"),
    n("Jaina Solo"),
    n("Muunilinst: Docking Bay"),
    n("Lady Luck"),
    n("Sorry About The Mess"),
    n("Phylo Gandish", True),
    n("Sabotage", True, qty=2),
    n("Rebel Artillery"),
    n("Imperial Atrocity", True),
    n("Grimtaash"),
    n("Desperate Tactics"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Muunilinst: Harnaidan Plains"),
    n("Plo Koon", True),
    n("Muunilinst: City Of Harnaidan"),
    n("Lucky Shot", True),
    n("Dressel"),
    n("Dark Approach", True),
    n("Artoo, Brave Little Droid"),
    n("Away Put Your Weapon", True),
    n("Projection Of A Skywalker"),
    n("Assault On Muunilinst"),
    n("Escape Pod", True),
    n("Radar Scanner", qty=2),
    n("Houjix"),
    n("Seeking An Audience", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Anakin Skywalker"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Rebel Barrier"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Chasm"),
    n("Weapons Display"),
    n("Your Insight Serves You Well"),
    n("Don't Do That Again"),
    n("Yavin Sentry"),
    n("The Professor"),
]
LS_ADD = [
    n("Let's Keep A Little Optimism Here"),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
]


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself"),
    n("Geonosis: Separatist Council Room"),
    n("War Has Begun"),
    n("Everything Is Going As Planned"),
    n("Droid Racks"),
    n("3,720 To 1", True),
    n("Baktoid Armor Workshop"),
    n("Armored Attack Tank", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("AAT Assault Leader"),
    n("Daultay Dofine", True),
    n("Cold Feet", True),
    n("Muunilinst: City Of Harnaidan"),
    n("We're In Attack Position Now", qty=2),
    n("AAT Laser Cannon", qty=3),
    n("Defensive Fire", True),
    n("Tank Commander", qty=2),
    n("OOM Command Battle Droid", qty=2),
    n("Imperial Artillery"),
    n("Imperial Barrier", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Muunilinst: Separatist Command Center"),
    n("Deployment Orders"),
    n("Something Special Planned For Them", True),
    n("Maul's Sith Infiltrator"),
    n("P-59"),
    n("Forced Servitude"),
    n("Guri"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Probot"),
    n("Protocol Failure"),
    n("4-LOM With Concussion Rifle", True),
    n("Defense Of Muunilinst"),
    n("Stop Motion", True),
    n("Inconsequential Losses", True),
    n("Muunilinst"),
    n("Open Fire!"),
    n("Blockade Flagship", True),
    n("Slave I, Symbol Of Fear"),
    n("Force Push", True),
    n("Muunilinst: Banking Clan Headquarters"),
    n("OOM-9", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Cloud City: Security Tower", True),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Battle Order"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Firepower"),
    n("You Cannot Hide Forever"),
    n("Fanfare"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?"),
]
DS_ADD = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Oppressive Enforcement"),
]
