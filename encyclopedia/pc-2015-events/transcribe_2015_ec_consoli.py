#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: Angelo Consoli Day 2 (place 6).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p14 Dark / p15 Light (typed category dumps).
"""
from __future__ import annotations

PLAYER = "Angelo Consoli"
USERNAME = "Gravityshadow"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 15
DS_PAGE = 14
LS_SCAN = "2015 European Championship Angelo Consoli LS.png"
DS_SCAN = "2015 European Championship Angelo Consoli DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 6 circled. p14 Dark / p15 Light typed category dumps, no PC form. "
    "Headers 'DS Angelo Consoli TTO' / 'LS Angelo Consoli Combat'; 'Angelo Consoli (Gravityshadow)' taken as username. "
    "DS 3:1 / LS 3:1. Handwritten joke note on p14 (printed lists) ignored."
)
LS_NOTE = (
    "START We'll Handle This / Duel Of The Fates. "
    "Anger, Fear, Aggression (V) (+Defensive Shields) listed under STARTING, counted in the 60. "
    "Posted Naboo: Theed Palace: Generator Core dested Naboo: Theed Palace Generator Core; likewise Generator. "
    "Heading for the Medical Frigate (+3 effects) dested Heading For The Medical Frigate; +3 effects are the listed Effects. "
    "Posted Luke Skywalker V x2 dested Luke Skywalker True qty 2. Posted Han, Chewie and the Falcon dested Han, Chewie, And The Falcon. "
    "Posted Qui-Gon's Lightsaber x2 kept (title exists). Antilles Maneuver listed once plain, once (v). "
    "Control & Tunnel Vision x2 (x2 handwritten). Effects: 'A Gift' crossed out, not in deck. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START Endor Operations / Imperial Outpost. "
    "Knowledge & Defense (v) (+Defensive Shields) listed under STARTING, counted in the 60; dested Knowledge And Defense. "
    "Operational As Planned (+1 effect) dested Operational As Planned. "
    "Posted Tatooine (EP I) dested Tatooine (Coruscant). "
    "Dr. Evazan & Ponda Baba crossed out, not in deck. "
    "Handwritten 'Control + Set for Stun' next to INTERRUPTS heading dested Control & Set For Stun (makes 60). "
    "Posted Nemoidian Advisor x2 dested Neimoidian Advisor. Posted Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Posted That Thing's Operational! dested That Thing's Operational. "
    "Sheet header says 'TTO' (That Thing's Operational) but objective is Endor Operations, matches wiki. "
    "Black Sun Fleet x3 sheet-accurate. Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("We'll Handle This / Duel Of The Fates"),
    n("Inner Strength"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Heading For The Medical Frigate"),
    n("Nar Shaddaa"),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker", True, qty=2),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("Threepio With His Parts Showing"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda, Master Of The Force", qty=2),
    n("Artoo-Detoo In Red 5", qty=4),
    n("Azure Angel"),
    n("Han, Chewie, And The Falcon"),
    n("Red Squadron 1"),
    n("Qui-Gon's Lightsaber", qty=2),
    n("X-wing Laser Cannon"),
    n("I'll Take The Leader"),
    n("A New Secret Base", True),
    n("Evacuation Control", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Alter", True),
    n("Antilles Maneuver"),
    n("Antilles Maneuver", True),
    n("Blast The Door, Kid!", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Dodge"),
    n("Escape Pod", True),
    n("Free Ride & Endor Celebration", qty=2),
    n("Houjix"),
    n("It Could Be Worse"),
    n("It's A Trap!"),
    n("Jedi Levitation", True),
    n("Sense", qty=2),
    n("The Bith Shuffle & Desperate Reach"),
    n("We're Doomed"),
    n("Weapon Levitation"),
    n("Were You Looking For Me?"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Goldenrod"),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Operational As Planned"),
    n("Death Star II"),
    n("Moff Jerjerrod"),
    n("Death Star II: Capacitors"),
    n("Death Star II: Coolant Shaft"),
    n("Death Star II: Reactor Core"),
    n("Tatooine (Dark) (Coruscant)"),
    n("Admiral Ozzel"),
    n("Arica"),
    n("Boba Fett, Bounty Hunter"),
    n("Count Dooku", qty=2),
    n("Darth Maul", qty=2),
    n("Darth Vader", True),
    n("Darth Vader With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Jango Fett"),
    n("P-59"),
    n("Stormtrooper Garrison"),
    n("Wooof", True),
    n("Elis In Hinthra"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Vader's Personal Shuttle", True),
    n("Zuckuss In Mist Hunter"),
    n("Black Sun Fleet", qty=3),
    n("Combat Response", True),
    n("Endor Shield", True),
    n("Image Of The Dark Lord", True),
    n("Imperial Decree", True),
    n("No Escape"),
    n("We Shall Double Our Efforts!"),
    n("Control & Set For Stun"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Close Call", True),
    n("Dark Maneuvers", qty=2),
    n("Elis Helrot"),
    n("Force Push", True),
    n("Ghhhk"),
    n("Imbalance & Kintan Strider"),
    n("Masterful Move"),
    n("Neimoidian Advisor", qty=2),
    n("Ommni Box & It's Worse"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Surface Defense", True),
    n("Turn It Off! Turn It Off!", True),
    n("We Must Accelerate Our Plans"),
    n("That Thing's Operational"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Vote Of No Confidence"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
