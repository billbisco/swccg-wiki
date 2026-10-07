#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Tim Murray.

Source: 2012mpcday1.pdf pages 115–116 (2010 form, 12 shields).
Name Tim Murray dested Tim Murray (analog generate / player-stubs empty).
p115 Light Explosive Ewoks. p116 Dark ASM from da Hood.
Username Timbed2003 (Light) / Timbod2003 (Dark spelling variant).
Pack player-stubs/Tim_Murray.wiki.
Do not dest as a new invented person. Dest Name box as written.
"""
from __future__ import annotations

PLAYER = "Tim Murray"
USERNAME = "Timbed2003"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 115
DS_PAGE = 116
LS_SCAN = "2012 Match Play Championship Day 1 Tim Murray LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Tim Murray DS.png"
LS_DECK_NAME = "Explosive Ewoks"
DS_DECK_NAME = "ASM from da Hood"
NOTE = "Handwritten 2010 Xerox form. Username Timbed2003."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Tim Murray dested Tim Murray. "
    "Username Timbed2003. LIGHT checked. Deck Name Explosive Ewoks. "
    "Event Date 2/11/12 Event Name MPC. Analog generate empty dest as written. "
    "Rebel Strike Team / Garrison Destroyed True dested Rebel Strike Team / Garrison Destroyed True. "
    "Wesa Ready To Do Our-sa Part dested Wesa Ready To Do Our-Sa Part True. "
    "I Hope She's Alright dested I Hope She's All Right True. "
    "Yub Yub! dested Yub Yub!. Graak dested Graak. Kazak dested Kazak. "
    "Your Ships? dested Your Ship?. Do or Do Not True dested Do, Or Do Not. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Tim Murray dested Tim Murray. "
    "Username Timbod2003 dested Timbed2003. DARK checked. Deck Name ASM from da Hood. "
    "Event Date 2/11/12 Event Name MPC. "
    "ASM dested dual A Stunning Move / A Valuable Hostage empty. "
    "Knowledge And Defense True dested in the 60 analog starting interrupt. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x3 analog Casey. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog Anis. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard analog Jourdan. "
    "Ni Chuba Na dested Ni Chuba Na?? empty. "
    "Private Platform dested Coruscant: Private Platform (Docking Bay). "
    "A Dark Time The Rebellion dested A Dark Time For The Rebellion. "
    "Always Thinking With Yar Stomach dested Always Thinking With Your Stomach. "
    "Resistance True dested Resistance without extra (V) analog Mack. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rebel Strike Team / Garrison Destroyed"
LS_CARDS = [
    n("Rebel Strike Team / Garrison Destroyed", True),
    n("Rebel Gunrunner"),
    n("The Shield Is Down!", True),
    n("Ewok Celebration"),
    n("Strike Planning"),
    n("Endor: Back Door"),
    n("Endor"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Explosive Charge", qty=2),
    n("Ewok Rescue"),
    n("Throw Me Another Charge", qty=2),
    n("Flash Of Insight", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Ewok Spearman"),
    n("Ewok Sentry", qty=2),
    n("Ewok Tribesman", qty=3),
    n("Sound The Attack", qty=2),
    n("Ewok Spear"),
    n("Daughter Of Skywalker"),
    n("Houjix"),
    n("Tantive IV", True),
    n("Admiral Ackbar", True),
    n("Slight Weapons Malfunction"),
    n("Home One"),
    n("Bright Hope", True),
    n("Yub Yub!"),
    n("Mindful Of The Future"),
    n("Liberty"),
    n("Rebel Artillery"),
    n("Demotion"),
    n("Wesa Ready To Do Our-Sa Part", True),
    n("I Hope She's All Right", True),
    n("Endor Celebration", True),
    n("Home One: War Room"),
    n("Imperial Atrocity", True),
    n("Chief Chirpa", True),
    n("Wicket", True),
    n("Graak"),
    n("General Crix Madine"),
    n("Ewok Catapult"),
    n("General Solo", True),
    n("Lumat"),
    n("Wuta"),
    n("Chewbacca Of Kashyyyk"),
    n("Romba"),
    n("Endor: Bunker"),
    n("Deactivate The Shield Generator"),
    n("Endor: Dense Forest"),
    n("Endor: Ewok Village", True),
    n("Kazak"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Traffic Control", True),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Your Ship?"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Knowledge And Defense", True),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Insidious Prisoner"),
    n("Oh, Switch Off"),
    n("Prepared Defenses"),
    n("Force Field", True, qty=2),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Galen, Secret Apprentice", qty=2),
    n("Sniper & Dark Strike", qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Control", qty=2),
    n("Battle Droid Squad", qty=3),
    n("Nal Hutta"),
    n("Bossk In Hound's Tooth", True),
    n("Dengar In Punishing One"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Blaster Rack", True),
    n("A Sith's Weapon"),
    n("No Escape"),
    n("Imperial Propaganda"),
    n("Weapon Levitation"),
    n("Force Push", True),
    n("Always Thinking With Your Stomach"),
    n("Ghhhk"),
    n("Dr. Evazan & Ponda Baba"),
    n("Victory"),
    n("The Phantom Menace"),
    n("Boba Fett In Slave I", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Zuckuss In Mist Hunter"),
    n("Maul Strikes"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Masterful Move & Endor Occupation"),
    n("Release Your Anger"),
    n("Ability, Ability, Ability", True),
    n("Podracer Collision"),
    n("P-59"),
    n("A Dark Time For The Rebellion"),
    n("IG-100 MagnaGuard"),
    n("We Must Accelerate Our Plans"),
    n("Lateral Damage"),
    n("I Have You Now"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Imperial Detention"),
    n("Resistance"),
    n("Wipe Them Out, All Of Them", True),
    n("Death Star Sentry", True),
    n("Battle Order"),
    n("Fanfare", True),
]
DS_ADD = []
