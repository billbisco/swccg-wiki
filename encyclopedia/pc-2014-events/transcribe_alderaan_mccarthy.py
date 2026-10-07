#!/usr/bin/env python3
"""2014 Alderaan Regionals typed printouts: Roy McCarthy.

Source: 2014-Alderaan-Regionals.pdf pages 13–14 (typed 2013 form).
"""
from __future__ import annotations

PLAYER = "Roy McCarthy"
USERNAME = "RybackStun"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 13
DS_PAGE = 14
LS_SCAN = "2014 Alderaan Regionals p13 Roy McCarthy LS.png"
DS_SCAN = "2014 Alderaan Regionals p14 Roy McCarthy DS.png"
NOTE = "Typed printout (not a handwritten Xerox form)."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("All My Urchins & Cloud City Celebration", True),
    n("Keeping The Empire Out Forever"),
    n("Anger, Fear, Aggression", True),
    n("Harc Seff", True),
    n("Cloud City: West Gallery"),
    n("Rebel Barrier", qty=2),
    n("Booster In Pulsar Skate", True),
    n("Luke With Lightsaber"),
    n("Overseer", True),
    n("Uutik", True),
    n("BoShek", True),
    n("Nien Nunb, Sullustan Smuggler", True),
    n("Chewbacca, Walking Carpet", True),
    n("Path Of Least Resistance", qty=2),
    n("Houjix & Out Of Nowhere", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Dash Rendar", True),
    n("Alter", True),
    n("Aayla Secura", True),
    n("Menace Fades"),
    n("Sergeant Edian", True),
    n("Lobot", True),
    n("Projection Of A Skywalker"),
    n("Cloud City: North Corridor"),
    n("Trooper Utris M'Toc", True),
    n("It's A Trap!"),
    n("Kebyc", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("Ellors Madak", True),
    n("Foul Moudama", True),
    n("Lady Luck", True),
    n("Desperate Reach", True),
    n("Princess Leia", True),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Houjix & Out Of Nowhere"),
    n("It Could Be Worse", qty=2),
    n("Errant Venture", True),
    n("Han Solo, Innocent Scoundrel", True),
    n("Yoxgit"),
    n("Blast The Door, Kid!"),
    n("Hindsight", True),
    n("Outrider"),
    n("Tanus Spijek", True),
    n("Leslomy Tecema", True),
    n("Melas", True),
    n("Leesub Sirln", True),
    n("Dark Approach", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Choke"),
    n("Let The Wookiee Win", qty=2),
    n("Alternatives To Fighting"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan", True),
    n("Aim High", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("Don't Do That Again", True),
    n("Traffic Control", True),
    n("Do, Or Do Not", True),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Insidious Prisoner", True),
    n("Coruscant: Private Platform", True),
    n("Prepared Defenses"),
    n("Jabba's Haven", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
    n("Count Dooku", True, qty=2),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("IG-100 MagnaGuard", True, qty=2),
    n("Battle Droid Squad", True, qty=2),
    n("P-60"),
    n("P-59"),
    n("4-LOM With Concussion Rifle", True),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Aurra Sing, Deadly Assassin", True, qty=2),
    n("Operational As Planned", True),
    n("Imbalance & Kintan Strider", True),
    n("Oh, Switch Off", qty=2),
    n("Lana Dobreed & Sacrifice", True),
    n("Cold Feet", True),
    n("Sniper & Dark Strike", True),
    n("Ghhhk"),
    n("Sonic Bombardment", True, qty=2),
    n("Control & Set For Stun"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Force Field", True, qty=2),
    n("Blaster Rack", True),
    n("Protocol Failure", True),
    n("Breached Defenses & Molator", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Dark Jedi Lightsaber", True, qty=2),
    n("Dooku's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Trophy Of A Kill", True, qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Nal Hutta"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward", True),
    n("Secret Plans", True),
    n("Resistance", True),
    n("Battle Order", True),
    n("There Is No Try", True),
    n("You Cannot Hide Forever", True),
    n("Reactor Terminal", True),
    n("Imperial Detention", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
