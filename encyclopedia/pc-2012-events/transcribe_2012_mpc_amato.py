#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Nicholas Amato.

Source: 2012mpcday1.pdf pages 39–40 (2010 form, 12 shields).
Name Nick Amato dested Nicholas Amato (2013 leftover analog).
Username nicholas.amato. Event MPC Date 02/11/12.
p39 Light Rescue The Princess. p40 Dark Set Your Course For Alderaan.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Nicholas Amato"
USERNAME = "nicholas.amato"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 39
DS_PAGE = 40
LS_SCAN = "2012 Match Play Championship Day 1 Nicholas Amato LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Nicholas Amato DS.png"
LS_DECK_NAME = "Thank You Artoo! But Our Princess Is In Another Death Star!"
DS_DECK_NAME = "Great Ball of Fire!"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Nick Amato dested Nicholas Amato. "
    "Username nicholas.amato. Event MPC Date 02/11/12. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Rescue The Princess/Sometimes I Amaze Even Myself dested Rescue The Princess "
    "/ Sometimes I Amaze Even Myself empty. "
    "Artoo & *Threepio dested Artoo & Threepio True. "
    "Odin Nesloor & *First Aid dested Odin Nesloor & First Aid x3. "
    "SATM dested Sorry About The Mess & Blaster Proficiency. "
    "Antilles Maneuver & *Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1. "
    "Unique 60. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Nick Amato dested Nicholas Amato. "
    "Username nicholas.amato. Event MPC Date 02/11/12. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "SYCFA dested Set Your Course For Alderaan / The Ultimate Power In The Universe empty. "
    "Super Laser dested Superlaser. "
    "Furry Fury dested Sith Fury x2. "
    "He is Not Ready & Imperial Propaganda dested He Is Not Ready & Imperial Propaganda. "
    "Wipe them out dested Wipe Them Out, All Of Them True. "
    "We'll let fate-a decide dested We'll Let Fate-a Decide, Huh? True. "
    "Hyper Route Navigation Chart dested Hyperroute Navigation Chart in Additional. "
    "Unique 60. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rescue The Princess / Sometimes I Amaze Even Myself"
LS_CARDS = [
    n("Rescue The Princess / Sometimes I Amaze Even Myself"),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Docking Bay"),
    n("Death Star: Docking Bay 327"),
    n("Death Star: Detention Block Corridor"),
    n("Senator Leia Organa"),
    n("Prisoner 2187"),
    n("Scomp Link Access", True),
    n("Cell 2187", True),
    n("Rycar Ryjerd", True),
    n("Artoo & Threepio", True),
    n("IL-19"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Captain Verrack", True),
    n("Luke With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Home One"),
    n("Tantive IV", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Home One: War Room"),
    n("Kiffex"),
    n("Thank The Maker"),
    n("A Jedi's Resilience", qty=3),
    n("Houjix"),
    n("Sense", qty=2),
    n("Escape Pod", True),
    n("Desperate Reach", True),
    n("Inconsequential Barriers"),
    n("Odin Nesloor & First Aid", qty=3),
    n("We're Doomed"),
    n("How Did We Get Into This Mess?", qty=2),
    n("Rebel Leadership", True),
    n("Houjix & Out Of Nowhere"),
    n("Grimtaash"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Hopping Mad", True),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("K'lor'slug", True),
    n("Wedge In Red Squadron 1"),
    n("Our Most Desperate Hour", True),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("The Professor", True),
    n("Another Pathetic Lifeform", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Kiffex"),
    n("Rendili"),
    n("Nal Hutta"),
    n("Death Star: Central Core", True),
    n("Death Star: War Room", True),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Lord Sidious", qty=2),
    n("U-3PO"),
    n("Cease Fire!"),
    n("Intensify The Forward Batteries", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sith Fury", qty=2),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Force Push", True),
    n("Relentless Pursuit", qty=2),
    n("TIE Sentry Ships", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Overwhelmed", qty=2),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True),
    n("Image Of The Dark Lord", True),
    n("Imperial Decree", True),
    n("Lateral Damage"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("A Bright Center To The Universe"),
    n("Tarkin Doctrine"),
    n("Devastator", True),
    n("Conquest", True),
    n("Victory"),
    n("Tyrant"),
    n("Visage"),
    n("Judicator", qty=2),
    n("Accuser"),
    n("Thunderflare"),
    n("Imperial Barrier", qty=3),
    n("Control & Set For Stun", qty=2),
    n("Laser Cannon Battery"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Battle Order"),
    n("Fanfare"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Wipe Them Out, All Of Them", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
]
DS_ADD = [
    n("Hyperroute Navigation Chart"),
]
