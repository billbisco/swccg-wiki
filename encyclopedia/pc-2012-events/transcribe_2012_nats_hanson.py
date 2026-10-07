#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Matt Hanson.

Source: 2012NationalsDay1.pdf pages 26–27 (handwritten 2010 Xerox, 12 shields).
Name Matt Hanson dested Matt Hanson as written. Username blank.
p26 Dark Endor Operations. p27 Light Yavin 4: Massassi Throne Room.
Do not dest as a new identified person until analog identifies.
"""
from __future__ import annotations

PLAYER = "Matt Hanson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 27
DS_PAGE = 26
LS_SCAN = "2012 US Nationals Day 1 Matt Hanson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Matt Hanson DS.png"
LS_DECK_NAME = "fuck it"
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox. Username blank. Event Date 6/9/12 Event Name Nats. Dark Deck Name crossed."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Hanson dested Matt Hanson as written. "
    "Username blank. LIGHT checked. Deck Name fuck it. Event Date 6/9/12 Event Name Nats. "
    "Analog leftover generate empty dest as written. "
    "Do not dest as a new identified person until analog identifies. "
    "Y4 MTR dested Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "Insurrection/Aim high dested Insurrection & Aim High analog leftover Wirfs. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "H1:DB dested Home One: Docking Bay analog leftover. "
    "Boss Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover. "
    "Tat. Mos Espa DB dested Tatooine: Mos Espa Docking Bay analog leftover. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel True analog leftover Skilton. "
    "Obi w/ Stick dested Obi-Wan With Lightsaber analog leftover Graham. "
    "LSTK dested Luke Skywalker, Jedi Knight analog leftover Wirfs. "
    "WYLCFM dested leftover_xerox as written analog empty. "
    "SWTJC dested Speak With The Jedi Council analog leftover Anderson. "
    "Wesa dested Wesa Gotta Grand Army analog leftover Frafjord. "
    "LTWW dested Let The Wookiee Win True analog leftover. "
    "Leia RP dested Leia, Rebel Princess analog leftover Pinto. "
    "AJR dested A Jedi's Resilience analog leftover Anderson. "
    "Padme dested Padme Naberrie True analog leftover Jourdan. "
    "HCF dested Han, Chewie, And The Falcon True analog leftover Booker. "
    "Antilles Maneuver & Rebel Rein dested Antilles Maneuver & Rebel Reinforcements True analog leftover Fernando. "
    "SATM dested Sorry About The Mess analog leftover. "
    "DTF dested Draw Their Fire analog leftover Anderson. "
    "Threepio w/ parts dested Threepio With His Parts Showing analog leftover Bollentino. "
    "Sai'torr dested Sai'torr Kal Fas True analog leftover. "
    "Armed dangerous & Krayt dested Armed And Dangerous & Krayt Dragon Howl True analog leftover Anderson. "
    "Obi JCC dested Obi-Wan Kenobi analog leftover. "
    "Line 60 blank skipped. Unique 59 sheet-accurate. "
    "Shield A Tragedy dested A Tragedy Has Occurred analog leftover George. "
    "Simple tricks dested Simple Tricks And Nonsense True analog leftover Frafjord. "
    "Your Insight dested Your Insight Serves You Well True analog leftover Skilton. "
    "Lets keep a little optimism dested Let's Keep A Little Optimism Here True analog leftover Harpster. "
    "Shield 12 We dested Wise Advice analog leftover Frafjord."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Hanson dested Matt Hanson as written. "
    "Username blank. DARK checked. Deck Name crossed. Event Date 6/9/12 Event Name Nats. "
    "Analog leftover generate empty dest as written. "
    "Do not dest as a new identified person until analog identifies. "
    "EOPS dested Endor Operations / Imperial Outpost analog leftover Kinsey. "
    "Endor bunker dested Endor: Bunker analog leftover Kinsey. "
    "Landing platform dested Endor: Landing Platform (Docking Bay) analog leftover Marty. "
    "Laser cannon battery dested Laser Cannon Battery analog leftover Kinsey leftover_xerox. "
    "Ni chuba dested Ni Chuba Na?? True analog leftover Anderson. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Tempest 1 dested Tempest Scout 1 analog leftover Marty. "
    "Imbalance & Kintan Strider dested analog leftover Jessica. "
    "Victory dested Victory True analog leftover Frafjord. "
    "I've lost artoo dested I've Lost Artoo! analog leftover. "
    "Lightsaber deficiency dested Lightsaber Deficiency True analog leftover Brentson. "
    "Chimera dested Chimaera analog leftover. "
    "Lieutenant Creevele dested Lieutenant Cabbel True analog leftover Koswicki. "
    "Ghhhk & those rebels dested Ghhhk & Those Rebels Won't Escape Us analog leftover Hilbun. "
    "Something special planned dested Something Special Planned For Them True analog leftover Wirfs. "
    "Commander Igar dested Commander Igar analog leftover Wirfs. "
    "CHYBC dested Come Here You Big Coward True analog leftover Anderson. "
    "Do You have Code dested Do They Have A Code Clearance? analog leftover Anderson. "
    "We'll let fate decide dested We'll Let Fate-a Decide, Huh? analog leftover Pistone. "
    "YCHF dested You Cannot Hide Forever True analog leftover Kinsey. "
    "Shield 12 Su dested Surface Defense analog leftover Dalton. "
    "True vs empty kept separate. Unique 60. Shields 12."
)

def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)

LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Insurrection & Aim High"),
    n("Heading For The Medical Frigate"),
    n("Home One: Docking Bay"),
    n("Naboo: Boss Nass' Chambers"),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Lando Calrissian, Scoundrel", True),
    n("Blaster Deflection", qty=2),
    n("Sense", qty=3),
    n("Home One: War Room"),
    n("Rebel Leadership", True, qty=3),
    n("Sorry About The Mess", qty=2),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("WYLCFM"),
    n("Speak With The Jedi Council", qty=2),
    n("Alter", True),
    n("Tantive IV", True),
    n("Luke's Bionic Hand", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Jedi Lightsaber", True),
    n("Let The Wookiee Win", True),
    n("Leia, Rebel Princess", qty=2),
    n("Desperate Reach", True),
    n("Strikeforce", True),
    n("A Jedi's Resilience", qty=2),
    n("Padme Naberrie", True),
    n("Han, Chewie, And The Falcon", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Kiffex"),
    n("Draw Their Fire"),
    n("Elegant Lightsaber", True),
    n("Admiral Ackbar"),
    n("Fallen Jedi", True, qty=2),
    n("Home One"),
    n("Corran Horn"),
    n("Luke's Lightsaber"),
    n("Threepio With His Parts Showing"),
    n("Sai'torr Kal Fas", True),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Obi-Wan Kenobi"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Laser Cannon Battery"),
    n("Imperial Stockpile", True),
    n("Kuat Drive Yards", True),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("Admiral Chiraneau"),
    n("Intensify The Forward Batteries", qty=3),
    n("Establish Secret Base", True),
    n("Darth Vader", True),
    n("Protocol Failure", True),
    n("Tempest Scout 1", qty=2),
    n("Admiral Piett"),
    n("Judicator"),
    n("Blizzard 4", True),
    n("Executor"),
    n("Avenger"),
    n("Admiral Motti", True),
    n("Imbalance & Kintan Strider", True),
    n("Kashyyyk"),
    n("Blizzard 2", True, qty=2),
    n("Imperial Command", qty=2),
    n("Imperial Decree"),
    n("Victory", True),
    n("Blizzard 1", True),
    n("Trample", qty=3),
    n("Ominous Rumors"),
    n("Overwhelmed", qty=2),
    n("Lateral Damage"),
    n("I've Lost Artoo!"),
    n("Sullust"),
    n("Fondor"),
    n("General Veers", True),
    n("Lightsaber Deficiency", True),
    n("Chimaera"),
    n("Grand Moff Tarkin", True),
    n("Admiral Ozzel", True),
    n("Imperial Barrier"),
    n("Lieutenant Cabbel", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Something Special Planned For Them", True),
    n("Cold Feet", True),
    n("Devastator", True),
    n("Commander Igar"),
    n("Grand Admiral Thrawn"),
    n("Thunderflare"),
    n("Conquest", True),
    n("Endor Shield", True),
]
DS_SHIELDS = [
    n("Resistance", True),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Allegations Of Corruption", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Surface Defense"),
]
DS_ADD = []
