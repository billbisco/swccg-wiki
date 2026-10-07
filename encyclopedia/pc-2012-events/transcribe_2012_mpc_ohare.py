#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris O'Hare.

Source: 2012mpcday1.pdf pages 117–118 (2010 form, 12 shields).
Name Chris O'Hare / Chris Ohr dested Chris O'Hare (analog generate empty;
facing pair Light Name box complete).
p117 Light Watch Your Step. p118 Dark A Stunning Move.
Username Fuller Sith. Pack player-stubs/Chris_O'Hare.wiki.
Do not dest as a new invented person. Dest Name box as written.
"""
from __future__ import annotations

PLAYER = "Chris O'Hare"
USERNAME = "Fuller Sith"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 117
DS_PAGE = 118
LS_SCAN = "2012 Match Play Championship Day 1 Chris O'Hare LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris O'Hare DS.png"
LS_DECK_NAME = "Hunter told me a secret"
DS_DECK_NAME = "Ash Du Rifter"
NOTE = "Handwritten 2010 Xerox form. Username Fuller Sith."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris O'Hare dested Chris O'Hare. "
    "Username Fuller Sith. LIGHT checked. Deck Name Hunter told me a secret. "
    "Analog generate empty dest as written. Dark Name Chris Ohr dested Chris O'Hare facing pair. "
    "AFA True dested Anger, Fear, Aggression True in the 60. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough empty. "
    "Tatooine (Coruscant) dested Tatooine (Coruscant) analog Cullen. "
    "Insurrection / Aim High dested Insurrection & Aim High analog Atkin. "
    "Squad Assembly dested Squadron Assignments analog Atkin. "
    "Antilles Maneuver / Rebel Artillery dested Antilles Maneuver & Rebel Reinforcements analog Atkin. "
    "Fallen Portal dested Falcon Parts analog Atkin. "
    "Houjix + Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Boshek, BS dested BoShek, Brash Smuggler True analog Lepine. "
    "H. Solo, CS dested Han Solo, Courageous Smuggler analog Atkin. "
    "Traffic Control True dested in the 60. Melas crossed skipped. "
    "I'll Take The Odds dested as written. Unique 59 sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Ohr dested Chris O'Hare. "
    "Username Fuller Sith. DARK checked. Deck Name Ash Du Rifter. Event Name MPC. "
    "Line 1 K&D dested Knowledge And Defense True in the 60 analog Murray. "
    "ASM / AVH True dested dual A Stunning Move / A Valuable Hostage virtual-only. "
    "TP dested Trophy Of A Kill analog Anderson. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog Casey. "
    "IG Body Guard Droid dested IG-100 MagnaGuard analog Jourdan. "
    "Ghhhk + TRWEU dested Ghhhk & Those Rebels Won't Escape Us analog Hilbun. "
    "C + SFS dested Control & Set For Stun analog Lepine. "
    "MM + EO dested Masterful Move & Endor Occupation analog PMT. "
    "AUG dested A Useless Gesture True. DTHCC dested Do They Have A Code Clearance? True. "
    "CHYBC dested Come Here You Big Coward. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Heading For The Medical Frigate"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Squadron Assignments"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Outrider"),
    n("Dash Rendar"),
    n("Imperial Atrocity", True),
    n("Artoo-Detoo In Red 5"),
    n("Daughter Of Skywalker"),
    n("Kessel"),
    n("Palace Raiders", qty=4),
    n("Falcon Parts"),
    n("Houjix & Out Of Nowhere"),
    n("Wedge Antilles", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Corellian Slip", True),
    n("Luke Skywalker", qty=2),
    n("Patrol Craft", qty=5),
    n("I'll Take The Odds", qty=2),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Han, Chewie, And The Falcon"),
    n("Tatooine Celebration", qty=2),
    n("Spaceport Docking Bay"),
    n("Control & Tunnel Vision", qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Sabotage", True),
    n("Pulsar Skate"),
    n("Han Solo, Courageous Smuggler"),
    n("Millennium Falcon"),
    n("BoShek, Brash Smuggler", True, qty=2),
    n("Traffic Control", True),
    n("Tycho Celchu"),
    n("Menace Fades"),
    n("On The Edge"),
    n("X-wing Laser Cannon"),
    n("It's A Hit!"),
    n("All Wings Report In"),
    n("Rebel Barrier"),
    n("Luke With Lightsaber"),
    n("Rel Sentry"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display"),
    n("Ounee Ta", True),
    n("Jabba's Prize"),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("A Stunning Move / A Valuable Hostage"),
    n("Trophy Of A Kill"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Coruscant: Palpatine's Quarters"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Darth Maul"),
    n("Sniper & Dark Strike"),
    n("Coruscant: Galactic Senate"),
    n("No Escape"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Nal Hutta"),
    n("Victory"),
    n("Coruscant: Security Office"),
    n("Masterful Move & Endor Occupation"),
    n("Dr. Evazan"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice"),
    n("Blockade Flagship: Bridge"),
    n("Aurra Sing", True),
    n("4-LOM With Concussion Rifle", True),
    n("Force Field"),
    n("Control & Set For Stun"),
    n("Battle Droid Squad", True, qty=3),
    n("Dengar With Blaster Carbine"),
    n("The Phantom Menace", qty=2),
    n("IG-100 MagnaGuard"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Blockade Flagship: Hallway", True),
    n("Blockade Flagship: Docking Bay", True),
    n("Blaster Rack"),
    n("Stop Motion", True),
    n("Battle Droid Squad"),
    n("Zuckuss In Mist Hunter"),
    n("P-59"),
    n("Alter"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Propaganda", True),
    n("Sith Fury", True, qty=2),
    n("Force Field", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blockade Flagship: Hallway"),
    n("Dark Jedi Lightsaber", True),
    n("Stunning Leader"),
    n("Imperial Decree", True),
    n("Blockade Flagship: Docking Bay"),
    n("Ability, Ability, Ability"),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Weapon Of A Sith"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Battle Order", qty=2),
]
DS_ADD = []
