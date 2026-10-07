#!/usr/bin/env python3
"""2013 World Championship Day 1 typed Print Form: Drew Powers LS+DS."""
from __future__ import annotations

PLAYER = "Drew Powers"
USERNAME = "Rebort"
STAGE = "Day 1"
PDF = "2013 Worlds Day 1.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2013 Worlds Day 1 p09 Drew Powers LS.png"
DS_SCAN = "2013 Worlds Day 1 p10 Drew Powers DS.png"
NOTE = "Typed 2013 Xerox Print Form."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rescue The Princess / Sometimes I Amaze Even Myself"
LS_CARDS = [
    n("Rescue The Princess / Sometimes I Amaze Even Myself"),
    n("Scomp Link Access", True),
    n("Cell 2187", True),
    n("Rycar Ryjerd", True),
    n("Senator Leia Organa", True),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Docking Bay"),
    n("Death Star: Docking Bay"),
    n("Death Star: Detention Block Corridor"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Maris Brood, Fallen Jedi", True, qty=2),
    n("Qui-Gon With Lightsaber", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Artoo & Threepio", True),
    n("Corran Horn"),
    n("Odin Nesloor & First Aid", True, qty=4),
    n("Blaster Deflection", qty=3),
    n("Smoke Screen", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("How Did We Get Into This Mess", qty=2),
    n("Rebel Barrier", qty=2),
    n("We're Doomed"),
    n("Wesa Gotta Grand Army"),
    n("Speak With The Jedi Council"),
    n("Strangle"),
    n("Houjix"),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience"),
    n("Fallen Portal"),
    n("Sense"),
    n("Let The Wookiee Win", True),
    n("Our Most Desperate Hour", True),
    n("Hopping Mad", True),
    n("Imperial Atrocity", True),
    n("Scrambled Transmission"),
    n("Much To Learn, You Still Have", True),
    n("Projection Of A Skywalker"),
    n("Death Star Plans"),
    n("Guardian's Lightsaber", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Ultimatum", True),
    n("Wise Advice"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan"),
    n("Chasm", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("He Can Go About His Business", True),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Start Your Engines"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Sebulba's Podracer"),
    n("Presence Of The Force", qty=2),
    n("No Bargain", True),
    n("Shada", qty=2),
    n("Death Star: War Room", True),
    n("Hoth: Wampa Cave"),
    n("Blockade Flagship: Bridge"),
    n("Boba Fett In Slave I", True),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Aurra Sing"),
    n("Gardulla The Hutt"),
    n("Prophetess", True),
    n("Kitik Keed'kak", True),
    n("P-59"),
    n("P-60"),
    n("Probot", True),
    n("IG-88 With Riot Gun"),
    n("4-LOM With Concussion Rifle"),
    n("Trophy Of A Kill", True, qty=4),
    n("A Dark Time For The Rebellion", True, qty=3),
    n("I'd Just As Soon Kiss A Wookiee", qty=3),
    n("Projective Telepathy", qty=2),
    n("Control", qty=2),
    n("Vader's Obsession", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Imperial Barrier", qty=2),
    n("Stunning Leader", True, qty=3),
    n("Ghhhk"),
    n("Surprise"),
    n("Comscan Detection", True),
    n("Elis Helrot"),
    n("Jabba's Haven", True),
    n("No Escape"),
    n("Dark Reconnaissance", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order", True),
    n("Secret Plans", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Resistance", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Oppressive Enforcement", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Wipe Them Out, All Of Them", True),
    n("Imperial Detention", True),
    n("Death Star Sentry", True),
]
DS_ADD = []
