#!/usr/bin/env python3
"""2015 European Championship: Wojtek Wisniewski Day 2 (place 9).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p20 Dark / p21 Light (handwritten caps).
"""
from __future__ import annotations

PLAYER = "Wojtek Wisniewski"
USERNAME = "HIPO"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 21
DS_PAGE = 20
LS_SCAN = "2015 European Championship Wojtek Wisniewski LS.png"
DS_SCAN = "2015 European Championship Wojtek Wisniewski DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 9 circled. p20 Dark / p21 Light handwritten. Name 'Wojtek Wisniewski', Username HIPO on both. "
    "Event Date 10/17/15. DS 3:1 / LS 2:2."
)
LS_NOTE = (
    "Posted Watch Your Step/... dested Watch Your Step / This Place Can Be A Little Rough. "
    "Posted Tatooine (Coruscant) kept (wiki title Tatooine (Coruscant)). Posted Tat: Podracing Bay dested Tatooine: Podracer Bay. "
    "Posted Tat: Podrace Arena dested Tatooine: Podrace Arena. Posted Anakin's Pod dested Anakin's Podracer. "
    "Posted Squadron Assigment dested Squadron Assignments. Posted Artoo in Red 5 (+ditto) dested Artoo-Detoo In Red 5 x2. "
    "Posted Luke Skywalker (+ditto, both V boxes checked) dested Luke Skywalker V x2. Posted EPP Han dested Han With Heavy Blaster Pistol. "
    "Posted All Wing Combo dested All Wings Report In & Darklighter Spin. Posted Ralltir Freighter Capt. dested Ralltiir Freighter Captain. "
    "Posted Obi-Wan Kenobi (V checked) dested Obi-Wan Kenobi V. Posted Chewie Enraged dested Chewie, Enraged. "
    "Posted Houjix Combo dested Houjix & Out Of Nowhere. Posted Shocking Inf Combo dested Shocking Information & Grimtaash. "
    "Civil Disorder box has a tick: read as V. "
    "Shields: Let's Keep A Little... dested Let's Keep A Little Optimism Here; The Republic No Longer.. dested The Republic No Longer Functions. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START Let Them Make The First Move / At Last We Will Have Revenge (sheet 'LET THEM MAKE.'). "
    "TITLE MISMATCH: wiki says Combat Readiness, sheet starts Let Them Make The First Move (Combat Readiness is not on the sheet). "
    "Posted Knowledge And Defences dested Knowledge And Defense. Posted Naboo: Generator / Core dested Naboo: Theed Palace Generator / Generator Core. "
    "Posted Wipe Them Out.. dested Wipe Them Out, All Of Them. Posted Crush The Reb. dested Crush The Rebellion. "
    "Posted Imp. Barrier dested Imperial Barrier. Posted 4-LOM EPP dested 4-LOM With Concussion Rifle. Posted Emp. Palpy dested Emperor Palpatine. "
    "Posted Image Of A Dark Lord dested Image Of The Dark Lord. Posted Dr Evazan Combo dested Dr. Evazan & Ponda Baba. Posted Ghhhk kept. "
    "Posted Darth Vader DLOTS dested Darth Vader, Dark Lord Of The Sith. Posted Omni Box Combo dested Ommni Box & It's Worse. "
    "Posted Ability x3 dested Ability, Ability, Ability. Posted We Must Acc.. dested We Must Accelerate Our Plans. "
    "Posted Maul's Double Light. dested Maul's Double-Bladed Lightsaber. Posted Turn It Off... dested Turn It Off! Turn It Off!. "
    "Line 41 Imperial Barrier crossed out, Masterfull written: dested Masterful Move (total 2). "
    "Ditto pairs with only the first V box checked (Force Field 10/11, Sith Fury 12/13, Image 22/23) recorded as V x2. "
    "Shields: I Find Your... dested I Find Your Lack Of Faith Disturbing; Death Star Sentra dested Death Star Sentry; Secret Plan dested Secret Plans; "
    "Oppresive Enf... dested Oppressive Enforcement; Come Here... dested Come Here You Big Coward; Vote Of No Conf. dested Vote Of No Confidence; "
    "Imp. Detention dested Imperial Detention (box faintly marked, left non-V). Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Boonta Eve Podrace"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Podracer Bay"),
    n("Tatooine: Podrace Arena"),
    n("Anakin's Podracer"),
    n("Squadron Assignments"),
    n("Podrace Prep"),
    n("Kashyyyk"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("On The Edge"),
    n("Luke Skywalker", True, qty=2),
    n("Mirax Terrik"),
    n("Life Debt"),
    n("Han With Heavy Blaster Pistol"),
    n("X-wing Laser Cannon"),
    n("Control & Tunnel Vision", qty=2),
    n("Starship Levitation", True),
    n("Pulsar Skate"),
    n("A New Secret Base", True),
    n("Organized Attack"),
    n("Theron Nett"),
    n("Red 10"),
    n("Red Squadron 1"),
    n("Dash Rendar"),
    n("Captain Han Solo"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Outrider"),
    n("Wedge Antilles", True),
    n("Ralltiir Freighter Captain", qty=2),
    n("I'll Take The Leader", qty=2),
    n("Sabotage", True),
    n("Civil Disorder", True),
    n("It's A Hit!"),
    n("Phylo Gandish"),
    n("Coruscant"),
    n("Obi-Wan Kenobi", True),
    n("Millennium Falcon"),
    n("Projection Of A Skywalker", qty=2),
    n("Chewie, Enraged", qty=2),
    n("It Could Be Worse"),
    n("A Few Maneuvers"),
    n("Kessel"),
    n("Rebel Barrier"),
    n("I Did It!"),
    n("We're Doomed"),
    n("Legendary Starfighter"),
    n("Houjix & Out Of Nowhere"),
    n("Melas", True),
    n("Shocking Information & Grimtaash"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("Wise Advice"),
    n("Planetary Defenses"),
    n("Let's Keep A Little Optimism Here"),
    n("The Republic No Longer Functions", True),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Ounee Ta"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "Let Them Make The First Move / At Last We Will Have Revenge"
DS_CARDS = [
    n("Knowledge And Defense"),
    n("Let Them Make The First Move / At Last We Will Have Revenge"),
    n("Deep Hatred"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Wipe Them Out, All Of Them"),
    n("Blaster Rack", True),
    n("Crush The Rebellion"),
    n("According To My Design"),
    n("Force Field", True, qty=2),
    n("Sith Fury", True, qty=2),
    n("Imperial Barrier"),
    n("4-LOM With Concussion Rifle"),
    n("Lord Maul", qty=2),
    n("Count Dooku", True, qty=2),
    n("Emperor Palpatine", qty=2),
    n("Image Of The Dark Lord", True, qty=2),
    n("Stunning Leader", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Ghhhk"),
    n("Sense", qty=2),
    n("Alter", True),
    n("A Day Long Remembered", True, qty=2),
    n("Masterful Move", qty=2),
    n("Monnok"),
    n("Dooku's Lightsaber", True),
    n("The Phantom Menace", qty=2),
    n("Force Lightning"),
    n("Blockade Flagship: Bridge"),
    n("Force Push", True),
    n("Zuckuss In Mist Hunter", qty=2),
    n("I Have You Now", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Maul"),
    n("Ommni Box & It's Worse"),
    n("Maul's Sith Infiltrator"),
    n("P-59"),
    n("Mara Jade With Lightsaber", True),
    n("Ability, Ability, Ability", True),
    n("Vader's Lightsaber"),
    n("Maul Strikes"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("Boba Fett In Slave I", True),
    n("Turn It Off! Turn It Off!", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Vote Of No Confidence", True),
    n("Imperial Detention"),
    n("Firepower"),
]
DS_ADD = []
