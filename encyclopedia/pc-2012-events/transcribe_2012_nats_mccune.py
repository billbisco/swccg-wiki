#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Bryan McCune.

Source: 2012NationalsDay1.pdf pages 36–37 (handwritten 2010 Xerox, 12 shields).
p36 Dark Name Bryan McCune Username Bryan-Ic3b dested Bryan McCune as written.
p37 Light Name B Gunmaster Event Name Nationals Bryan dested Bryan McCune analog leftover facing pair.
Analog leftover generate empty dest as written. Do not dest as David McCune.
Pack player-stubs/Bryan_McCune.wiki.
"""
from __future__ import annotations

PLAYER = "Bryan McCune"
USERNAME = "Bryan-Ic3b"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 37
DS_PAGE = 36
LS_SCAN = "2012 US Nationals Day 1 Bryan McCune LS.png"
DS_SCAN = "2012 US Nationals Day 1 Bryan McCune DS.png"
LS_DECK_NAME = "Cot"
DS_DECK_NAME = "Let's blow stuff UP"
NOTE = "Handwritten 2010 Xerox. Name Bryan McCune / B Gunmaster dested Bryan McCune as written. Username Bryan-Ic3b."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name B Gunmaster dested Bryan McCune analog leftover facing p36 Event Name Nationals Bryan. "
    "Username blank. LIGHT/DARK empty dest Light from the 60. Deck Name Cot. "
    "Analog leftover generate empty dest as written. Do not dest as David McCune. "
    "Center Of Tyranny True dested Center Of Tyranny / A Liberated World True analog leftover Hodur. "
    "Bacta Infirmary dested analog leftover Carulli True. "
    "Rogue Squadron + tactics dested Rogue Squadron Tactics True analog leftover Chris. "
    "Declaration Of Rebellion dested analog leftover Chris True. "
    "Rogue Insertion dested analog leftover Chris True. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber analog leftover Thornton. "
    "Deren Hobble Kilvian dested as written leftover_xerox True. "
    "Dash Rulter dested Dash Rendar True analog leftover Chris Terwilliger x2. "
    "Luke Skywalker, Rebel Hero dested analog leftover Gemme True x3 unique overcount. "
    "Veteran Rogue dested analog leftover Carulli True x2. "
    "Biggs, Rogue Legend dested analog leftover Finley True. "
    "Leia dested Princess Leia True analog leftover Jeeps. "
    "Wedge Antilles Legendary Pilot dested Wedge Antilles, Legendary Rogue True analog leftover Hodur. "
    "Leia, Rebel Princess dested analog leftover Pinto. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader analog leftover Jeeps. "
    "Tycho Celchu dested analog leftover Carulli True. "
    "Wes Janson, Rogue Veteran dested Wes Janson True analog leftover Jankowski. "
    "Commander Wedge dested Commander Wedge Antilles True analog leftover Gogolen. "
    "Yub Yub, Commander dested analog leftover Carulli True x4 unique overcount. "
    "Odin Nesloor and First Aid dested Odin Nesloor & First Aid True analog leftover Booker. "
    "Honor of a Jedi dested Honor Of The Jedi analog leftover Foth. "
    "Commando Training combo dested Commando Training & K'lor'slug True analog leftover Grouty. "
    "Projection of a Skywalker dested Projection Of A Skywalker analog leftover 2013 MPC Herold x2. "
    "Mind What dested Mind What You Have Learned / Save You It Can True analog leftover 2013 Anderson. "
    "Han, Chewie, & the Falcon dested Han, Chewie, And The Falcon analog leftover Booker x2. "
    "Obiwan in Red 7 dested Obi-Wan In Radiant VII True analog leftover 2013 Worlds Herold. "
    "AFA dested Anger, Fear, Aggression analog leftover Casey IN THE 60. "
    "Simple Tricks dested Simple Tricks And Nonsense True analog leftover Herold. "
    "Let them a little optimism dested Let's Keep A Little Optimism Here True analog leftover Hanson. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Bryan McCune dested Bryan McCune as written. "
    "Username Bryan-Ic3b. DARK checked. Deck Name Let's blow stuff UP. Event Name Nationals. "
    "Analog leftover generate empty dest as written. Do not dest as David McCune. "
    "SYCFA / TUPITU empty dested Set Your Course For Alderaan / The Ultimate Power In The Universe analog leftover Brodsky. "
    "Imperial Stockpile dested analog leftover Cullen True. "
    "Prepared Defenses dested analog leftover IN THE 60 True. "
    "Visage dested analog leftover Brummett. "
    "Intensify The Forward Batteries dested analog leftover Brummett x2. "
    "Commence Primary Ignition dested analog leftover Brummett True. "
    "Vegence dested Vengeance analog leftover. "
    "Victory dested analog leftover Hanson True x2. "
    "He is not ready combo dested He Is Not Ready & Imperial Propaganda True analog leftover Bordier. "
    "Death Star Gunner True and empty kept separate analog leftover. "
    "Imperial Trooper Guard Garrison dested Imperial Trooper Guard analog leftover Marc Hanson. "
    "U-3PO dested analog leftover Shaw. "
    "Operational As Planned dested analog leftover TMW Herold True x2. "
    "TIE Sentry Ships dested analog leftover Brummett True x2. "
    "A Dark Time For The Rebellion dested analog leftover SAN True x2. "
    "Flawless Marksmanship dested analog leftover x5 unique overcount. "
    "Lightsaber Deficiency dested analog leftover TMW Herold True. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Come Here You Big Coward dested analog leftover Anderson. "
    "Wipe Them Out dested Wipe Them Out, All Of Them analog leftover. "
    "Imperial Decree dested analog leftover Erwin True. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Center Of Tyranny / A Liberated World", True),
    n("Bacta Infirmary", True),
    n("Rogue Squadron Tactics", True),
    n("Declaration Of Rebellion", True),
    n("Rogue Insertion", True),
    n("Coruscant", True),
    n("Coruscant: Main Power Plant", True),
    n("Coruscant: Lower Levels", True),
    n("Heading For The Medical Frigate"),
    n("Dressel", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Deren Hobble Kilvian", True),
    n("Dash Rendar", True, qty=2),
    n("Ten Numb", True),
    n("Luke Skywalker, Rebel Hero", True, qty=3),
    n("Veteran Rogue", True, qty=2),
    n("Biggs, Rogue Legend", True),
    n("Princess Leia", True),
    n("Wedge Antilles, Legendary Rogue", True),
    n("Leia, Rebel Princess"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Tycho Celchu", True),
    n("Corran Horn"),
    n("Wes Janson", True),
    n("Commander Wedge Antilles", True),
    n("Luke's Blaster Pistol", True),
    n("Escape Pod", True, qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Houjix"),
    n("Too Close For Comfort"),
    n("Hear Me Baby, Hold Together", True),
    n("Yub Yub, Commander", True, qty=4),
    n("Odin Nesloor & First Aid", True),
    n("Menace Fades"),
    n("Field Dressing", True),
    n("Flash Of Insight", True),
    n("Imperial Atrocity", True),
    n("Honor Of The Jedi"),
    n("Commando Training & K'lor'slug", True),
    n("Civil Disorder", True),
    n("Coruscant Celebration"),
    n("Projection Of A Skywalker", qty=2),
    n("Mind What You Have Learned / Save You It Can", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Spiral"),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII", True),
    n("Planetary Shield", True),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("The Professor", True),
    n("Battle Plan", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again", True),
    n("Traffic Control", True),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("Do, Or Do Not", True),
    n("Aim High"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Imperial Stockpile", True),
    n("Laser Cannon Battery"),
    n("Kuat Drive Yards", True),
    n("A Million Voices Crying Out"),
    n("Alderaan"),
    n("Death Star"),
    n("Death Star: Docking Bay"),
    n("Prepared Defenses", True),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Carida"),
    n("Kiffex"),
    n("Nal Hutta"),
    n("Superlaser"),
    n("Intensify The Forward Batteries", qty=2),
    n("Commence Primary Ignition", True),
    n("Vengeance"),
    n("Accuser"),
    n("Visage"),
    n("Victory", True, qty=2),
    n("Devastator"),
    n("Thunderflare"),
    n("Chimaera"),
    n("Judicator", qty=2),
    n("Stalker"),
    n("Conquest", True),
    n("Tyrant"),
    n("Image Of The Dark Lord", True),
    n("Protocol Failure", True, qty=2),
    n("Dreaded Imperial Starfleet", True),
    n("Lateral Damage"),
    n("Tarkin's Doctrine", True),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Death Star Gunner", True),
    n("Death Star Gunner"),
    n("Imperial Trooper Guard"),
    n("U-3PO"),
    n("Operational As Planned", True, qty=2),
    n("Relentless Pursuit", qty=4),
    n("TIE Sentry Ships", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Flawless Marksmanship", qty=5),
    n("Lightsaber Deficiency", True),
    n("Limited Resources"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Crossfire"),
    n("A Useless Gesture"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Wipe Them Out, All Of Them"),
    n("Abyss"),
    n("Imperial Decree", True),
]
DS_ADD = []
