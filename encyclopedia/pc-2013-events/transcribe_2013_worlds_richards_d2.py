#!/usr/bin/env python3
"""2013 World Championship Day 2: Mike Richards Xerox Hunt Down + Quiet Mining Colony."""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "m007agent"
LS_USERNAME = "m007agent"
DS_USERNAME = "m007agent"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 81
DS_PAGE = 80
LS_SCAN = "2013 Worlds Day 2 p81 Mike Richards LS.png"
DS_SCAN = "2013 Worlds Day 2 p80 Mike Richards DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Sheet name Michael Richards; canon Mike Richards. "
    "Username m007agent (sheet mroo7agent). Deck title Go Caleb. LIGHT. "
    "Do not rewrite the 2013 MPC Mike Richards leftover (MWYHL / Hunt Down). "
    "Quiet Mining Colony dested Quiet Mining Colony / Independent Operation. "
    "Besgin dested Bespin. Baldan's Eye dested Beldon's Eye. "
    "Keeping the Empire Forever dested Keeping The Empire Out Forever. "
    "The Birth Shuttle & Desperate Launch dested The Bith Shuffle & Desperate Reach. "
    "Fit to the Vast / Tato Cantina dested Tatooine: Cantina. "
    "Punch It dested Punch It!. Hare Seff dested Harc Seff. "
    "Blast the Door Kid dested Blast The Door, Kid!. "
    "Qui-Gon Jinn with Saber dested Qui-Gon Jinn With Lightsaber. "
    "Luke with Skywalker dested Luke Skywalker. "
    "Cloud City: Chasm hallway dested Cloud City: Chasm Walkway. "
    "Pacumir Thryss dested Pucumir Thryss. "
    "Artoo Brave Little Droid dested Artoo, Brave Little Droid. "
    "Lando's Luxury Yacht dested Lando's Luxury Yacht. "
    "Obi-Wan with Saber dested Obi-Wan With Lightsaber. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "Additional A Tragedy Has Occurred / Weapons Display moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Imperial Atrocity and Kebyc. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Sheet name Michael Richards; canon Mike Richards. "
    "Username m007agent (sheet mroo7agent). Deck title Go James. DARK. "
    "Do not rewrite the 2013 MPC Mike Richards leftover. "
    "Hunt Down dested Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V). "
    "Ni Chu Ba Na dested Ni Chuba Na??. "
    "Drop! (V) checkbox dested Drop! Effect; Drop! (V) is a Defensive Shield. "
    "Trophy of a Kill (V) checkbox dested without (V). "
    "One Beautiful High dested One Beautiful Thing. "
    "Weapon Levitation & The Emperor's Back dested Weapon Levitation & The Empire's Back. "
    "Ability x3 dested Ability, Ability, Ability. "
    "Galen, Secret Apprentice dested Galen, Secret Apprentice. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Galen's Fighter dested Galen's Fighter. "
    "Sith Fury & End This Destructive Conflict dested Sith Fury & End This Destructive Conflict. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Asoca dested as written. "
    "Fear Will Keep Them In Line struck omitted; Weapon Of A Sith written, margin not V. "
    "Additional Oppressive Enforcement / There Is No Try / Battle Order moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Restraining Bolt x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Wokling", True),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True),
    n("Fall Of The Legend"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Tatooine: Cantina"),
    n("Punch It!"),
    n("Clutch"),
    n("Rebel Barrier"),
    n("Fall Of The Legend"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Clutch"),
    n("Cloud City Celebration"),
    n("All Wings Report In & Darklighter Spin"),
    n("Path Of Least Resistance"),
    n("Into The Ventilation Shaft, Lefty"),
    n("Obi-Wan With Lightsaber"),
    n("Harc Seff", True),
    n("Path Of Least Resistance"),
    n("Blast The Door, Kid!"),
    n("Spiral"),
    n("Cloud City Celebration"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Outrider"),
    n("Dash Rendar", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Luke Skywalker"),
    n("Let The Wookiee Win", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Cloud City: Chasm Walkway"),
    n("Overseer"),
    n("Imperial Atrocity", True),
    n("Kebyc", True),
    n("Pucumir Thryss"),
    n("Weather Vane", True),
    n("Let The Wookiee Win", True),
    n("Fall Of The Legend"),
    n("Spiral"),
    n("Lando's Luxury Yacht"),
    n("Leia, Rebel Princess"),
    n("Artoo, Brave Little Droid"),
    n("Cloud City: North Corridor"),
    n("Clutch"),
    n("Dash Rendar", True),
    n("Pucumir Thryss"),
    n("Luke With Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Into The Ventilation Shaft, Lefty"),
    n("Punch It!"),
    n("Escape Pod", True),
    n("Houjix"),
    n("Han, Chewie, And The Falcon"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Cloud City: Security Tower", True),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("Prepared Defenses"),
    n("Gift Of The Master", True),
    n("A Sith's Plans", True),
    n("Ni Chuba Na??", True),
    n("Drop!"),
    n("Force Field", True),
    n("Trophy Of A Kill", qty=4),
    n("Vader's Lightsaber"),
    n("Aurra Sing's Blaster Rifle"),
    n("Naboo: Theed Palace Generator Core"),
    n("We Must Accelerate Our Plans", qty=3),
    n("One Beautiful Thing", qty=2),
    n("Weapon Levitation & The Empire's Back", True, qty=4),
    n("Levitation Attack", qty=4),
    n("Sonic Bombardment", True, qty=3),
    n("Alter", True, qty=2),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Restraining Bolt", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Blockade Flagship: Bridge"),
    n("Asoca", True),
    n("Jango Fett, The Assassin"),
    n("Galen's Fighter", True),
    n("Slave I, Symbol Of Fear"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Ysanne Isard"),
    n("Boba Fett, Prepared Hunter"),
    n("Grand Moff Tarkin", True),
    n("Juno Eclipse, Black Leader"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Weapon Of A Sith"),
    n("Abyss"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Battle Order"),
]
DS_ADD = []
