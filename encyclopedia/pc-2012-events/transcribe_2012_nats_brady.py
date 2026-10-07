#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Brady.

Source: 2012NationalsDay1.pdf pages 42–43 (handwritten Light / handwritten Dark 2010 Xerox, 12 shields).
p42 Light / p43 Dark Name Brady dested Brady as written first-name-only.
Username blank. Analog leftover generate empty dest as written.
Do not dest as Brady Moore.
Pack player-stubs/Brady.wiki.
"""
from __future__ import annotations

PLAYER = "Brady"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 42
DS_PAGE = 43
LS_SCAN = "2012 US Nationals Day 1 Brady LS.png"
DS_SCAN = "2012 US Nationals Day 1 Brady DS.png"
LS_DECK_NAME = "Brady"
DS_DECK_NAME = "Brady"
NOTE = "Handwritten 2010 Xerox. Name Brady dested Brady as written first-name-only. Username blank."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brady dested Brady as written first-name-only. "
    "Username blank. LIGHT checked. Deck Name Brady. Event Date blank Event Name blank. "
    "Analog leftover generate empty dest as written. Do not dest as Brady Moore. "
    "PROFIT empty dested You Can Either Profit By This... / Or Be Destroyed analog leftover Bordier. "
    "UCTMF dested You Can Thank Me For... leftover_xerox. "
    "SEEKING dested Seeking An Audience True analog leftover. "
    "IHSA dested leftover_xerox True. "
    "QUICK DRAW dested Quick Draw True analog leftover leftover_xerox. "
    "JP:AC dested Jabba's Palace: Audience Chamber analog leftover. "
    "TAT:SP dested Tatooine: Slave Quarters analog leftover leftover_xerox. "
    "HAN dested Han Solo True analog leftover Martin. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency analog leftover Ziagos x3 unique overcount. "
    "3PO W/ PARTS dested C-3PO With His Parts Hanging Out analog leftover leftover_xerox. "
    "LEIA OC dested Leia Organa leftover_xerox. "
    "NICE OF THE dested Nice Of You To Drop By True leftover_xerox. "
    "LS, JK dested Luke Skywalker, Jedi Knight x4 unique overcount analog leftover leftover_xerox. "
    "HI:WR dested Hoth: Wampa Cave (7th Marker) analog leftover Grant. "
    "WESA dested Wesa Gotta Grand Army analog leftover Frafjord x2. "
    "OODGT dested leftover_xerox x2. "
    "TERSUTO dested leftover_xerox. "
    "LEIA, RP dested Leia, Rebel Princess analog leftover Pinto x2. "
    "EPP QUI-GON crossed dest Qui-Gon Jinn With Lightsaber analog leftover Graham skip original. "
    "Lucky Shot empty x2 plus extra misnumbered Lucky Shot True kept separate analog leftover McCune. "
    "extra 38 NABOO: BNC dested Naboo: Boss Nass' Chambers analog leftover leftover_xerox. "
    "EPP YUDANI dested leftover_xerox. "
    "SKYWALKER LS dested leftover_xerox. "
    "LEIA, BR dested leftover_xerox. "
    "WOOKIE (v) dested leftover_xerox True analog leftover notebook dest True when (v) written. "
    "SAITOR dested Sai'torr Kal Fas True analog leftover Lingrell. "
    "PADME dested Padmé Naberrie True leftover_xerox. "
    "COK dested leftover_xerox True. "
    "A F, A dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brady dested Brady as written first-name-only. "
    "Username blank. DARK checked. Deck Name Brady. Event Date blank Event Name blank. "
    "Analog leftover generate empty dest as written. Do not dest as Brady Moore. "
    "OBJECTIVE/STARTING LOCATION True dested Kessel analog leftover Kessel-deck starting. "
    "KESSEL: AO dested Kessel: Spice Mines - Administrator's Office analog leftover Cullen. "
    "SITH'S PLANS dested A Sith's Plans analog leftover Baroni. "
    "EPP VADER dested Darth Vader With Lightsaber analog leftover leftover_xerox x2. "
    "DIPO dested Dengar In Punishing One analog leftover Aasen. "
    "CONTROL & SFS dested Control & Set For Stun analog leftover SAN. "
    "SLAVE 1, SYMBOL OF FEAR dested Slave I, Symbol Of Fear analog leftover leftover_xerox. "
    "SNIPER COMBO dested leftover_xerox. "
    "EPP MAUL dested Darth Maul With Lightsaber analog leftover leftover_xerox x3 unique overcount. "
    "BAIRE DEPLOYMENT dested leftover_xerox. "
    "KESSEL: PRISON dested Kessel: Spice Mines - Prison analog leftover Cullen. "
    "BLP 4-LOM dested 4-LOM analog leftover leftover_xerox. "
    "WUMAP dested leftover_xerox x2. "
    "MEANW dested leftover_xerox. "
    "ADMIRAL PELLAEON dested leftover_xerox. "
    "MANDALORIAN FOF dested Jango Fett, The Assassin analog leftover Grouty. "
    "MAUL'S SHIP dested Maul's Sith Infiltrator analog leftover leftover_xerox. "
    "extra 37 SPICE MINE ADMIN dested leftover_xerox. extra 38 SPICE MINE OPS dested Spice Mine Operations analog leftover leftover_xerox. "
    "KESSEL: EF dested Kessel: Spice Mines - Extraction Facility analog leftover leftover_xerox. "
    "TAG dested leftover_xerox. BF: BRIDGE dested leftover_xerox. "
    "LS DEFICIENCY dested Lightsaber Deficiency True analog leftover TMW Herold. "
    "ORO & ROSETA dested leftover_xerox. WHY DON'T YOU ROLL ME dested leftover_xerox True. "
    "SSLFT dested leftover_xerox True. KHNYK dested leftover_xerox. "
    "DF BH dested leftover_xerox. ZIMM dested leftover_xerox. CAT OAM dested leftover_xerox. "
    "JUSTIFIER dested leftover_xerox. GARICA dested leftover_xerox. "
    "BF PREP HUNTER dested Boba Fett, Bounty Hunter analog leftover leftover_xerox. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("You Can Thank Me For..."),
    n("Seeking An Audience", True),
    n("IHSA", True),
    n("Quick Draw", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Slave Quarters"),
    n("Han Solo", True),
    n("Corran Horn"),
    n("Disarmed"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("C-3PO With His Parts Hanging Out"),
    n("Leia Organa"),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Nice Of You To Drop By", True),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Obi-Wan Kenobi", True),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Wesa Gotta Grand Army", qty=2),
    n("OODGT", qty=2),
    n("Tersuto"),
    n("Leia, Rebel Princess", qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Weapon Levitation"),
    n("Princess Leia", True),
    n("Qui-Gon Jinn With Lightsaber", True),
    n("Lucky Shot", qty=2),
    n("Lucky Shot", True),
    n("Naboo: Boss Nass' Chambers"),
    n("EPP Yoda"),
    n("A-280 Sharpshooter Rifle", True, qty=2),
    n("Skywalker Lightsaber"),
    n("Luke's Lightsaber"),
    n("Scrambled Transmission", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Leia With Blaster Rifle"),
    n("Grimtaash", True),
    n("Disarmed"),
    n("Wookiee", True),
    n("Sai'torr Kal Fas", True),
    n("Padmé Naberrie", True),
    n("Control Of Kessel", True),
    n("Hindsight", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Battle Plan"),
    n("Aim High"),
    n("OTTA"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well"),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel"),
    n("I'll Take Them Myself"),
    n("A Sith's Plans"),
    n("Endor Shield", True),
    n("Force Field", True),
    n("Darth Vader With Lightsaber", qty=2),
    n("Force Lash", True),
    n("Dengar In Punishing One"),
    n("Control & Set For Stun"),
    n("Imperial Barrier", qty=2),
    n("General Veers", True),
    n("Slave I, Symbol Of Fear"),
    n("Disarmed"),
    n("Sniper & Dark Strike"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Kessel Surveillance System"),
    n("Blizzard 2", True),
    n("Imperial Command", qty=2),
    n("BAIRE Deployment"),
    n("Kessel: Spice Mines - Prison"),
    n("4-LOM"),
    n("WUMAP", qty=2),
    n("Blizzard 4"),
    n("Meanwhile"),
    n("Admiral Pellaeon"),
    n("Grand Moff Tarkin", True),
    n("Imperial Decree", True),
    n("Imperial Decree"),
    n("Jango Fett, The Assassin"),
    n("Maul's Sith Infiltrator"),
    n("Sith Fury", True),
    n("Spice Mine Administrator"),
    n("Spice Mine Operations"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("TAG"),
    n("BF: Bridge"),
    n("Lightsaber Deficiency", True),
    n("Sith Fury", True),
    n("Jabba's Bounty", True),
    n("ORO & ROSETA"),
    n("Why Don't You Roll Me", True),
    n("SSLFT", True),
    n("KHNYK"),
    n("Ghhhk"),
    n("DF BH"),
    n("ZIMM"),
    n("CAT OAM"),
    n("Darth Maul With Lightsaber"),
    n("Trample"),
    n("JUSTIFIER"),
    n("GARICA"),
    n("Boba Fett, Bounty Hunter"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Leave Them To Me", True),
    n("Wipe Them Out, All Of Them", True),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Resonance"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
