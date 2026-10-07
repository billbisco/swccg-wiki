#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Brandon Burgt.

Source: 2012NationalsDay1.pdf pages 9–10 (handwritten 2010 Xerox, 12 shields).
Name Brandon Burgt dested Brandon Burgt as written. Username blank.
p09 Dark Starburst of Spice / Fondor.
p10 Light we don't have a plan / We Have A Plan.
Do not dest as Brandon Baity. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Brandon Burgt"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2012 US Nationals Day 1 Brandon Burgt LS.png"
DS_SCAN = "2012 US Nationals Day 1 Brandon Burgt DS.png"
LS_DECK_NAME = "we don't have a plan"
DS_DECK_NAME = "Starburst of Spice"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brandon Burgt dested Brandon Burgt as written. Username blank. "
    "LIGHT checked. Deck Name we don't have a plan. Event Date blank Event Name blank. "
    "Do not dest as Brandon Baity. Do not dest as a new person. "
    "we have a plan / they will be lost dested We Have A Plan / They Will Be Lost And Confused analog leftover. "
    "Naboo: Theed Courtyard dested Naboo: Theed Palace Courtyard analog leftover Yanaga. "
    "Naboo: Theed Throne Room dested Naboo: Theed Palace Throne Room analog leftover Yanaga. "
    "insurrection + aim high dested Insurrection & Aim High analog leftover Field. "
    "Sai'torr kal Fas dested Sai'torr Kal Fas True analog leftover Anderson. "
    "Queens royal ship dested Queen's Royal Starship leftover_xerox. "
    "Panaka's blaster dested Captain Panaka's Blaster leftover_xerox. "
    "Naboo blaster dested Naboo Blaster leftover_xerox. "
    "Obi-Wan's saber dested Obi-Wan's Lightsaber analog leftover. "
    "Amidala's blaster dested Queen Amidala's Blaster leftover_xerox. "
    "Qui-Gon Jinn's saber dested Qui-Gon Jinn's Lightsaber analog leftover. "
    "Obi Wan Kenobi Jedi Knight dested Obi-Wan Kenobi, Jedi Knight True analog leftover. "
    "Fallen Jedi dested Fallen Jedi True analog leftover Jan. "
    "Master Qui-Gon dested Master Qui-Gon True analog leftover. "
    "Panaka, Protector of a Queen dested Panaka, Protector Of A Queen leftover_xerox. "
    "Lieutenant Chamberlain dested leftover_xerox. "
    "Padme Amidala dested Padmé Amidala leftover_xerox. "
    "Padme Naberrie dested Padmé Naberrie analog leftover Kelly. "
    "Ric Olie dested Ric Olie leftover_xerox. "
    "Threepio w/ parts showing dested Threepio With His Parts Showing analog leftover Jan. "
    "Control + tunnel vision dested Control & Tunnel Vision analog leftover Field. "
    "Discussion group dested Discussion Group leftover_xerox. "
    "Heading for med frigate dested Heading For The Medical Frigate analog leftover Anderson. "
    "Brisky morning munchen dested Brisky Morning Munchen leftover_xerox. "
    "we don't have a plan dested We Don't Have A Plan leftover_xerox. "
    "Lost his dested Lost His leftover_xerox. "
    "Are you brain dead dested Are You Brain Dead?! analog leftover light_frank. "
    "Odin Ith dested analog leftover Field. "
    "I've won this round dested I've Won This Round leftover_xerox. "
    "Thrown back dested Thrown Back True analog leftover. "
    "Shield only Jedi carry that weapon dested Only Jedi Carry That Weapon analog leftover Bordier. "
    "Shields 8–12 blank skip. Unique overcounts sheet-accurate "
    "(Fallen Jedi True x2, Obi-Wan Kenobi, Jedi Knight True x2, Flash Of Insight True x2, "
    "Control & Tunnel Vision x2, Sense x3, Rebel Barrier x3). "
    "Panaka, Protector Of A Queen True vs empty kept separate. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brandon Burgt dested Brandon Burgt as written. Username blank. "
    "DARK checked. Deck Name Starburst of Spice. Event Date blank Event Name blank. "
    "Do not dest as Brandon Baity. Do not dest as a new person. "
    "Fondor dested Fondor (starting location, no Objective). "
    "You can not hide Forever combo dested You Cannot Hide Forever analog leftover Fred. "
    "Imperial stockpile dested Imperial Stockpile analog leftover. "
    "I'll take them myself dested I'll Take Them Myself analog leftover Fred. "
    "Prepared Defenses dested in the 60 analog leftover Jan. "
    "Knowledge + defense dested Knowledge And Defense True analog leftover Jan. "
    "U3PO dested U-3PO analog leftover. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover Fred. "
    "TIE Assault Squadron dested leftover_xerox. "
    "Short range Fighters dested Short Range Fighters analog leftover Fred. "
    "ImBalance combo dested Imbalance & Kintan Strider analog leftover. "
    "Death Squadron star destroyer dested Death Squadron Star Destroyer leftover_xerox. "
    "Flagship Executor dested Flagship Executor analog leftover Fred. "
    "Protocol Failure dested analog leftover Fred. "
    "Executor control Station dested Executor: Control Station analog leftover Fred. "
    "Lightsaber deficiency dested Lightsaber Deficiency True analog leftover Jan. "
    "Flagship operations dested Flagship Operations analog leftover Fred. "
    "Fozec dested analog leftover. "
    "Labria dested analog leftover Fred. "
    "Early warning network dested Early Warning Network leftover_xerox. "
    "Operational as Planned dested Operational As Planned True analog leftover Grant. "
    "Death star assault Squadron dested Death Star Assault Squadron leftover_xerox. "
    "exec holotheatre dested Executor: Holotheatre analog leftover Fred. "
    "exec med chamber dested Executor: Meditation Chamber analog leftover Fred. "
    "exec main corridor dested Executor: Main Corridor analog leftover Fred. "
    "Control combo dested Control & Set For Stun analog leftover Fred. "
    "Captain goldhardt dested Captain Goldhardt leftover_xerox. "
    "Commander Grandee dested leftover_xerox. "
    "exec Command Staff dested Executor: Comm Station analog leftover Fred. "
    "exec docking bay dested Executor: Docking Bay analog leftover. "
    "Imp decree dested Imperial Decree analog leftover Fred. "
    "Caldon dested Caldon leftover_xerox. "
    "Shields 8–12 blank skip. Unique overcounts sheet-accurate "
    "(Ghhhk & Those Rebels Won't Escape Us x2, Black Squadron TIE x3, TIE Interceptor x3, "
    "Fozec True x2, Flawless Marksmanship x2, Operational As Planned True x2, Relentless Pursuit x2, "
    "Nevar Yalnal x3, Undercover x3, Control & Set For Stun x2, Lightsaber Deficiency True x2, "
    "Flagship Executor x2, Flagship Operations x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Throne Room"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Sai'torr Kal Fas", True),
    n("Queen's Royal Starship"),
    n("Outrider"),
    n("Captain Panaka's Blaster"),
    n("Naboo Blaster"),
    n("Obi-Wan's Lightsaber"),
    n("Queen Amidala's Blaster"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jar Jar Binks"),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("Queen Amidala"),
    n("Fallen Jedi", True, qty=2),
    n("Master Qui-Gon", True),
    n("Let The Wookiee Win"),
    n("Flash Of Insight", True, qty=2),
    n("Panaka, Protector Of A Queen", True),
    n("Lieutenant Chamberlain", True),
    n("Panaka, Protector Of A Queen"),
    n("Padmé Amidala"),
    n("Padmé Naberrie"),
    n("Ric Olie"),
    n("Threepio With His Parts Showing"),
    n("Dash Rendar"),
    n("Lightsaber Proficiency"),
    n("Control & Tunnel Vision", qty=2),
    n("Too Close For Comfort"),
    n("Out Of Commission"),
    n("The Signal"),
    n("Clash Of Sabers"),
    n("Discussion Group"),
    n("Heading For The Medical Frigate"),
    n("Brisky Morning Munchen"),
    n("Another Pathetic Lifeform"),
    n("Honor Of The Jedi"),
    n("We Don't Have A Plan"),
    n("Lost His"),
    n("Sense", qty=3),
    n("Alter"),
    n("Are You Brain Dead?!"),
    n("Odin Ith"),
    n("Projection Of A Skywalker"),
    n("I've Won This Round"),
    n("Rebel Barrier", qty=3),
    n("Inconsequential Barriers"),
    n("Hindsight", True),
    n("Thrown Back", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Simple Tricks And Nonsense", True),
    n("Traffic Control", True),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon", True),
    n("Battle Plan"),
    n("The Professor"),
]
LS_ADD = []

DS_START = "Fondor"
DS_CARDS = [
    n("Fondor"),
    n("You Cannot Hide Forever"),
    n("Imperial Stockpile"),
    n("Concussion Missiles", True),
    n("I'll Take Them Myself"),
    n("Prepared Defenses"),
    n("Knowledge And Defense", True),
    n("U-3PO"),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("TIE Assault Squadron"),
    n("Short Range Fighters"),
    n("Black Squadron TIE", qty=3),
    n("Imbalance & Kintan Strider"),
    n("TIE Interceptor", qty=3),
    n("Hoth"),
    n("Death Squadron Star Destroyer"),
    n("Flagship Executor", qty=2),
    n("Protocol Failure"),
    n("Executor: Control Station"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Flagship Operations", qty=2),
    n("Fozec", True, qty=2),
    n("Labria", True),
    n("Flawless Marksmanship", qty=2),
    n("Early Warning Network"),
    n("Arica"),
    n("Operational As Planned", True, qty=2),
    n("Relentless Pursuit", qty=2),
    n("Limited Resources"),
    n("Death Star Assault Squadron"),
    n("Nevar Yalnal", qty=3),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Executor: Main Corridor"),
    n("Undercover", qty=3),
    n("Control & Set For Stun", qty=2),
    n("Captain Goldhardt"),
    n("Commander Grandee"),
    n("Executor: Comm Station"),
    n("Executor: Docking Bay"),
    n("Imperial Decree"),
    n("Yavin 4"),
    n("Caldon"),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Fanfare"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
