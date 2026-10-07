#!/usr/bin/env python3
"""2013 World Championship Day 1: Nathan Way Xerox LS+DS.

Name field on both sheets reads Nathan Wall; dested Nathan Way to match the
Day 1 hub / LS pair.
"""
from __future__ import annotations

PLAYER = "Nathan Way"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Worlds Day 1.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2013 Worlds Day 1 p11 Nathan Way LS.png"
DS_SCAN = "2013 Worlds Day 1 p12 Nathan Way DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Nathan Wall dested Nathan Way. "
    "Username blank. Deck title Jedi Test. LIGHT. Dated 8/9/13. "
    "MWYHL dested Mind What You Have Learned / Save You It Can. "
    "IITFYS (V) in the 60 is the Epic Event; Additional Cards IITFYS is the Jedi Test. "
    "Onya Secure dested Obi-Wan Kenobi. "
    "Antilles Man & Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "Jedi Tests listed under Additional Cards. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Nathan Wall dested Nathan Way. "
    "Username blank. Deck title Assassins. DARK. Event Day 1 Worlds. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "Never Valnal dested Nevar Yalnal. "
    "Fett Maliss, Shadowkiller dested Ket Maliss, Shadow Killer. "
    "Masterful Move & Endoropa dested Masterful Move & Endor Occupation. "
    "Imbalance & Gintan Shider dested Imbalance & Kintan Strider. "
    "Greedo With Blaster dested Greedo with Blaster Pistol. "
    "Death Mark & Huff Bounty dested Death Mark & Hutt Bounty. "
    "The Mandalorian, Faithful Warrior dested Jango Fett, The Assassin. "
    "M Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Luvkk dested as written. Roltan dested as written. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("It Is The Future You See", True),
    n("Strong Is Vader", True),
    n("Yavin 4: Massassi War Room"),
    n("Coruscant"),
    n("Dagobah"),
    n("Dagobah: Bog Clearing"),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Rebel Leadership", True, qty=3),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke's Bionic Hand", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Elegant Lightsaber", True, qty=2),
    n("Yoda", True),
    n("Luke's Backpack"),
    n("Reflection", True),
    n("Daughter Of Skywalker", True),
    n("On The Edge"),
    n("Projection Of A Skywalker"),
    n("Yoda's Hope"),
    n("Lando's Luxury Yacht"),
    n("Escape Pod", True),
    n("It's A Trap!", True),
    n("Admiral Ackbar", True),
    n("Imperial Atrocity", True),
    n("Under Attack"),
    n("Collision!"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Fallen Jedi", True),
    n("Obi-Wan Kenobi", True),
    n("Qui-Gon Jinn, Jedi Master"),
    n("Weapon Levitation"),
    n("Found Someone You Have"),
    n("Dodge"),
    n("Uncontrollable Fury"),
    n("Quick Draw"),
    n("Corran Horn"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mace Windu, Master Of The Order", True),
    n("Han, Chewie, And The Falcon", True),
    n("Houjix & Out Of Nowhere"),
    n("Clash Of Sabers"),
    n("Courage Of A Skywalker"),
    n("Alternatives To Fighting"),
    n("Home One"),
    n("It Could Be Worse"),
    n("Thrown Back", True),
    n("The Way Of Things"),
    n("Battle Plan & Draw Their Fire"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Traffic Control", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum", True),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Do, Or Do Not", True),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy", True),
    n("Nal Hutta"),
    n("Cloud City: Security Tower", True),
    n("Coruscant: Casino", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Sub City Lair"),
    n("Coruscant"),
    n("Arica", True, qty=3),
    n("Aurra Sing, Deadly Assassin", True, qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Luvkk", True, qty=2),
    n("Abyssin Ornament", True, qty=3),
    n("Disarmed", qty=2),
    n("One Beautiful Thing", True, qty=2),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Trophy Of A Kill", True, qty=2),
    n("Stunning Leader", qty=2),
    n("Guild Of Assassins", True),
    n("Gift Of The Master", True),
    n("Knowledge And Defense", True),
    n("Aurra Sing's Blaster Rifle"),
    n("Prepared Defenses"),
    n("Jabba's Haven", True),
    n("Assassin's Blaster Rifle", True),
    n("On The Hunt", True),
    n("Ket Maliss, Shadow Killer", True),
    n("Roltan", True),
    n("Imbalance & Kintan Strider", True),
    n("Force Field"),
    n("Death Mark & Hutt Bounty"),
    n("Blaster Rack", True),
    n("Mara Jade's Lightsaber"),
    n("Imperial Artillery"),
    n("Jango Fett, The Assassin", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Ghhhk"),
    n("Boba Fett, Prepared Hunter", True),
    n("Masterful Move & Endor Occupation"),
    n("Nevar Yalnal"),
    n("I've Lost Artoo", True),
    n("Imperial Barrier"),
    n("Slave I, Symbol Of Fear"),
    n("Greedo with Blaster Pistol", True),
    n("They're Still Coming Through!", True),
    n("Presence Of The Force"),
    n("Ghhhk"),
    n("You Are Beaten"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("Battle Order", True),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("No Escape", True),
    n("Reactor Terminal", True),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("A Useless Gesture"),
]
DS_ADD = []
