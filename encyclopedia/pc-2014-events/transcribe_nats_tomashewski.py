#!/usr/bin/env python3
"""2014 US Nationals Day 1 typed printouts: Mike Tomashewski.

Source: Nationals-2014-day-1.pdf pages 1–2 (typed, slang-heavy).
(V) follows a trailing v / (V) on the printout.
"""
from __future__ import annotations

PLAYER = "Mike Tomashewski"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2014 US Nationals Day 1 p01 Mike Tomashewski LS.png"
DS_SCAN = "2014 US Nationals Day 1 p02 Mike Tomashewski DS.png"


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("I Feel The Conflict"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Don't Tread On Me", True),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("Mechanical Failure"),
    n("Home One"),
    n("Yavin 4: Massassi War Room", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Home One: War Room"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=2),
    n("Dark Approach", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Sense", qty=2),
    n("Blaster Deflection", qty=2),
    n("Escape Pod", True),
    n("Nabrun Leids"),
    n("Clash Of Sabers"),
    n("Rebel Barrier", qty=2),
    n("Houjix"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council", qty=2),
    n("Let The Wookiee Win", qty=3),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Anakin Skywalker, Padawan Learner"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Corran Horn"),
    n("IL-19"),
    n("Mace Windu, Master Of The Order"),
    n("Tarfful, Wookiee Insurgent"),
]
LS_SHIELDS = [
    n("Anger, Fear, Aggression", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = [
    n("Affect Mind", True),
]


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself"),
    n("War Has Begun"),
    n("Geonosis: Separatist Council Room"),
    n("Any Methods Necessary"),
    n("Gift Of The Master", True),
    n("Lateral Damage"),
    n("First Strike"),
    n("Where Are You Taking This ... Thing?"),
    n("Rally To Our Cause"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Trophy Of A Kill", qty=2),
    n("Dark Jedi Lightsaber", True, qty=2),
    n("Geonosis"),
    n("Naboo: Theed Palace Generator"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Count Dooku", qty=2),
    n("Darth Sidious", qty=2),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Aurra Sing, Deadly Assassin"),
    n("Lott Dod", qty=2),
    n("Orn Free Taa"),
    n("Nute Gunray", True),
    n("Jango Fett, The Assassin"),
    n("Aks Moe"),
    n("Boba Fett, Prepared Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Baskol Yeesrim"),
    n("Passel Argente"),
    n("Edcel Bar Gane"),
    n("Dr. Evazan & Ponda Baba"),
    n("Yeb Yeb Ademthorn"),
    n("Force Field", True, qty=2),
    n("Force Push", True),
    n("Force Lightning"),
    n("Sense"),
    n("Alter", True),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Sonic Bombardment", True),
    n("Squabbling Delegates", qty=3),
    n("We Must Accelerate Our Plans"),
    n("Sniper & Dark Strike"),
    n("Weapon Levitation"),
    n("You Are Beaten"),
    n("Levitation Attack", qty=2),
]
DS_SHIELDS = [
    n("Knowledge And Defense", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = [
    n("Firepower", True),
]
