#!/usr/bin/env python3
"""2013 Alderaan Regionals: Nathan typed 2010 Xerox LS+DS.

Name field Nathan. Username SolaGratia. Dest Nathan as written (same SoCal Nathan).
Do not dest as Nathan Russell / Nathan Wall / Nathan Way.
Do not rewrite 2013 SoCal Nathan leftover.
"""
from __future__ import annotations

PLAYER = "Nathan"
USERNAME = "SolaGratia"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2013 Alderaan Regionals p26 Nathan LS.png"
DS_SCAN = "2013 Alderaan Regionals p25 Nathan DS.png"
LS_NOTE = (
    "Typed 2010 Xerox Print Form (12 shields + Additional). Name Nathan dested as written "
    "(same SoCal Nathan). Username SolaGratia. Event Alderaan Regionals 2013. LIGHT checked. "
    "Deck Name TRM - Toy Box. No objective on the sheet; line 1 Yavin IV: Throne Room dested "
    "as START. HFTMF dested Heading For The Medical Frigate. Naboo: Boss Nass Chamber dested "
    "Naboo: Boss Nass' Chambers. Mace Windu MOTO dested Mace Windu, Master Of The Order. "
    "Luke Skywalker, Jedi Knight crossed SITF dested Luke Skywalker, Strong In The Force. "
    "EPP Qui-Gon dested Qui-Gon Jinn With Lightsaber. Threepio with Parts Showing dested "
    "Threepio With His Parts Showing. Jedi's Lightsaber dested Jedi Lightsaber True. "
    "HCF dested Home One: Conference Room. Crossed line 33 dested Artoo-Detoo In Red 5. "
    "Evacuation Control crossed R2 in Red 5 dested Artoo-Detoo In Red 5 True. "
    "WGAGA dested WGAGA as written. Control Combo dested Control & Tunnel Vision. "
    "LTWW dested Let The Wookiee Win True. LTWW crossed Scrambled Transmission dested "
    "Scrambled Transmission True. OOC dested Out Of Commission. Hear Me Baby dested "
    "Hear Me Baby, Hold Together True. Houjix Combo dested Houjix & Out Of Nowhere. "
    "SATM Combo dested Sorry About The Mess & Blaster Proficiency. AFA dested "
    "Anger, Fear, Aggression True. Unique overcounts sheet-accurate (Obi-Wan Kenobi x2, "
    "Luke SITF x2, EPP Qui-Gon x2, Lando Scoundrel x2, Blaster Deflection x2, WGAGA x2, "
    "LTWW True x2, OOC x2, Rebel Leadership x3, A Jedi's Resilience x2, Artoo-Detoo In Red 5 x2). "
    "(V) from the checkbox; crossed cards dest the replacement."
)
DS_NOTE = (
    "Typed 2010 Xerox Print Form (12 shields + Additional). Name Nathan dested as written "
    "(same SoCal Nathan). Username SolaGratia. Event Alderaan Regionals 2013. DARK checked. "
    "Deck Name ROps is TOps - MHT Dom 1.5. Raltir Ops empty dested Ralltiir Operations / "
    "In The Hands Of The Empire without True. Prepared Def dested Prepared Defenses True. "
    "Ral: Fin District dested Ralltiir: Financial District. SP: Street / Docking Bay / "
    "Prefects Office dested Spaceport Street / Spaceport Docking Bay / Spaceport Prefect's Office. "
    "Emp Palpatine dested Emperor Palpatine. Darth Vader, DLOTS dested "
    "Darth Vader, Dark Lord Of The Sith. Darth Vader, Betrayer dested Darth Vader, Betrayer as written. "
    "EPP Mara Jade dested Mara Jade With Lightsaber. EPP Kir Kanos dested Kir Kanos. "
    "Lt. Com Ardan dested Commander Ardan. Col David Jon dested Colonel Davod Jon. "
    "Maarek Steele dested Maarek Stele, The Emperor's Reach. Victory dested Victory as written. "
    "Sneak Attack dested Sneak Attack True. Why Didn't You Tell Me? dested Why Didn't You Tell Me? True. "
    "Imbalance Combo dested Armed And Dangerous & Krayt Dragon Howl. Control Combo dested "
    "Control & Set For Stun. ADTFTR dested A Dark Time For The Rebellion True. "
    "WAYTTT? dested WAYTTT? as written. Barrier dested Imperial Barrier. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. K+D dested "
    "Knowledge And Defense True. Wipe Them Out All of Them crossed YCHF dested "
    "You Cannot Hide Forever True. Unique overcounts sheet-accurate (Emperor Palpatine x2, "
    "Imperial Domination x2, Close Call x2, Imperial Command x2). (V) from the checkbox; "
    "crossed cards dest the replacement."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Throne Room"
LS_CARDS = [
    n("Yavin 4: Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Home One: War Room"),
    n("Yavin 4: War Room", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order"),
    n("Obi-Wan Kenobi", True),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force"),
    n("Luke Skywalker, Strong In The Force"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Threepio With His Parts Showing"),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Home One"),
    n("Home One: Conference Room"),
    n("Artoo-Detoo In Red 5"),
    n("Sai'torr Kal Fas", True),
    n("Artoo-Detoo In Red 5", True),
    n("Blaster Deflection"),
    n("Blaster Deflection"),
    n("WGAGA"),
    n("WGAGA"),
    n("Speak With The Jedi Council"),
    n("Control & Tunnel Vision"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", True),
    n("Scrambled Transmission", True),
    n("Either Way, You Win", True),
    n("Out Of Commission"),
    n("Out Of Commission"),
    n("Rebel Leadership", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership", True),
    n("Hear Me Baby, Hold Together", True),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("A Jedi's Resilience"),
    n("A Jedi's Resilience"),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("Sense"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Don't Do That Again"),
    n("He Can Go About His Business", True),
    n("Ultimatum", True),
]
LS_ADD = [
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Affect Mind", True),
]


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Prepared Defenses", True),
    n("Insignificant Rebellion", True),
    n("Endor Shield", True),
    n("Kuat Drive Yards", True),
    n("Ralltiir: Financial District"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport Prefect's Office"),
    n("Endor"),
    n("Kashyyyk"),
    n("Emperor Palpatine"),
    n("Emperor Palpatine"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer"),
    n("Mara Jade With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Kir Kanos"),
    n("Admiral Ozzel"),
    n("Grand Admiral Thrawn"),
    n("Veers", True),
    n("Commander Ardan"),
    n("Colonel Davod Jon"),
    n("Janus Greejatus"),
    n("Ysanne Isard"),
    n("Admiral Motti", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Garindan", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Tempest 1"),
    n("Tyrant"),
    n("Conquest", True),
    n("Devastator", True),
    n("Victory"),
    n("Imperial Domination", True),
    n("Imperial Domination", True),
    n("Imperial Justice", True),
    n("Sneak Attack", True),
    n("Why Didn't You Tell Me?", True),
    n("Imperial Propaganda", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Close Call", True),
    n("Close Call", True),
    n("Outflank", True),
    n("Control & Set For Stun"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("He Hasn't Come Back Yet"),
    n("A Dark Time For The Rebellion", True),
    n("WAYTTT?"),
    n("Trample"),
    n("Imperial Barrier"),
    n("Ghhhk"),
    n("Imperial Command"),
    n("Imperial Command"),
    n("Masterful Move & Endor Occupation"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
]
DS_ADD = [
    n("Abyss", True),
    n("Imperial Detention", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
