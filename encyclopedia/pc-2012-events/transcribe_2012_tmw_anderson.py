#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: John Anderson.

Source: 2012TMWDay1.pdf pages 13–14 (2010 Xerox, 12 shields).
Name John Anderson dested John Anderson analog leftover 2012 Nats/MPC /
2013 TMW / player-stubs/John_Anderson.wiki. Username Puck 71 / Puck71 dested
Puck71 analog leftover 2012 Nats. p13 Dark Ass Stunning Move. p14 Light
Happy Fun Time. Do not dest as a new person. Do not dest 2012 Nats / 2012 MPC
/ 2013 TMW Anderson 60s again.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "Puck71"
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2012 Texas Mini Worlds Day 1 John Anderson LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 John Anderson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox form. "
    "Name John Anderson dested John Anderson analog leftover 2012 Nats. "
    "Username Puck71. Do not dest as a new person. "
    "Do not dest 2012 Nats / 2012 MPC / 2013 TMW Anderson 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name John Anderson dested John Anderson. Username Puck71. "
    "LIGHT checked. Event Date 4/28/12 Event Name TMW. Deck Name Happy Fun Time skip. "
    "Yavin 4: Throne Room dested Yavin 4: Massassi Throne Room analog leftover Nats "
    "(starting location, no Objective). "
    "HFTMF dested Heading For The Medical Frigate analog leftover Nats. "
    "Were You Lookin For Me? dested Were You Looking For Me? analog leftover. "
    "3P0 w/ Parts dested Threepio With His Parts Showing analog leftover. "
    "AJR dested A Jedi's Resilience analog leftover. "
    "Armed + Dangerous + Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl analog leftover Nats. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Nats qty=2. "
    "HCF dested Han, Chewie, And The Falcon analog leftover Nats qty=2. "
    "Hoth: War Room dested Hoth: Echo War Room analog leftover Barnes. "
    "Smoke Screen qty=4 unique overcount sheet-accurate. "
    "LSJK dested Luke Skywalker, Jedi Knight analog leftover Nats. "
    "Speak w/ Jedi Council dested Speak With The Jedi Council analog leftover Nats qty=2. "
    "Imp. Atrocity dested Imperial Atrocity analog leftover True. "
    "Sai'torr dested Sai'torr Kal Fas analog leftover Nats True. "
    "Gaffer dested Alter analog leftover Nats (handwritten capital A). "
    "Leia RP dested Leia, Rebel Princess analog leftover Nats. "
    "Ackbar dested Admiral Ackbar analog leftover Nats True. "
    "LTWW dested Let The Wookiee Win analog leftover True. "
    "Naboo: Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover Nats. "
    "LS, SITF dested Luke Skywalker, Strong In The Force analog leftover Nats qty=2. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency analog leftover Nats. "
    "Line 48 Clash of Sabers crossed dest replacement Scrambled dested Scrambled Transmission analog leftover Nats True. "
    "Qui Gon w/ Saber dested Qui-Gon Jinn With Lightsaber analog leftover Nats qty=2. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army analog leftover qty=2. "
    "Obi w/ Saber dested Obi-Wan With Lightsaber analog leftover Nats. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber analog leftover Nats True. "
    "AFA dested Anger, Fear, Aggression True analog leftover Nats IN THE 60. "
    "Shield DDTA dested Don't Do That Again analog leftover True. "
    "Shield Tragedy dested A Tragedy Has Occurred analog leftover. "
    "Shield Insight dested Your Insight Serves You Well analog leftover True. "
    "Unique 60. Shields 12. Unique overcounts sheet-accurate (Smoke Screen x4, Rebel Leadership True x3)."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name John Anderson dested John Anderson. Username Puck71. "
    "DARK checked. Event Date 04/28/12 Event Name TMW. Deck Name Ass Stunning Move skip. "
    "ASM empty dested A Stunning Move / A Valuable Hostage analog leftover Nats. "
    "Cor: Priv. Platform dested Coruscant: Private Platform analog leftover Nats. "
    "Cor: Palp's Quarters dested Coruscant: Palpatine's Quarters analog leftover Nats. "
    "Prep Defenses dested Prepared Defenses analog leftover True. "
    "Ni Chuba Na? dested Ni Chuba Na?? analog leftover Nats True. "
    "Galen dested Galen, Secret Apprentice analog leftover Nats qty=3. "
    "MM+EO dested Masterful Move & Endor Occupation analog leftover Nats qty=2. "
    "B.F.: Bridge dested Blockade Flagship: Bridge analog leftover. "
    "B.F.: DB dested Blockade Flagship: Docking Bay analog leftover Nats. "
    "B.F.: Hallway dested Blockade Flagship: Hallway analog leftover Nats. "
    "YAB dested You Are Beaten analog leftover 2013 MPC Anderson. "
    "Darth Maul, YA dested Darth Maul, Young Apprentice analog leftover Nats qty=2. "
    "Fett in Slave I dested Boba Fett In Slave I analog leftover MPC Anderson True qty=2. "
    "Image of the Dark Lord dested Image Of The Dark Lord analog leftover True. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover Nats qty=2. "
    "Cyborg's Sabers dested Grievous' Lightsabers analog leftover Nats. "
    "ZIMH dested Zuckuss In Mist Hunter analog leftover MPC Anderson. "
    "Maul's Ship dested Maul's Sith Infiltrator analog leftover Nats. "
    "Dark Time dested A Dark Time For The Rebellion analog leftover Nats True qty=2. "
    "4-LOM w/ Gun dested 4-LOM With Concussion Rifle analog leftover Erwin True. "
    "IG-Bodyguard Droid dested IG-100 MagnaGuard analog leftover Nats qty=2. "
    "Imp. Propaganda dested Imperial Propaganda analog leftover True. "
    "Dengar w/ blaster dested Dengar With Blaster Carbine analog leftover Alperstein True. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift analog leftover Nats. "
    "Sniper + DS dested Sniper & Dark Strike analog leftover Nats. "
    "Maul's Double Bladed Saber dested Maul's Double-Bladed Lightsaber analog leftover Nats. "
    "Elis in Hinthra dested Elis In Hinthra analog leftover MPC Anderson. "
    "Dr. E + Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover Nats. "
    "K+D dested Knowledge And Defense analog leftover Nats True IN THE 60. "
    "Shield Coward dested Come Here You Big Coward analog leftover Nats. "
    "Shield Weapon of a Sith dested Weapon Of A Sith analog leftover. "
    "Shield Allegations dested Allegations Of Corruption analog leftover. "
    "Shield YCHF dested You Cannot Hide Forever analog leftover Nats True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Were You Looking For Me?"),
    n("Threepio With His Parts Showing"),
    n("A Jedi's Resilience"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Hoth: Echo War Room"),
    n("Smoke Screen", qty=4),
    n("Luke Skywalker, Jedi Knight"),
    n("Speak With The Jedi Council", qty=2),
    n("Imperial Atrocity", True),
    n("Clash Of Sabers"),
    n("Seeking An Audience", True),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Mace Windu", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Sense", qty=2),
    n("Alter"),
    n("Naboo: Battle Plains"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Let The Wookiee Win", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Jedi Lightsaber", True),
    n("Tantive IV", True),
    n("Home One: War Room"),
    n("Rebel Leadership", True, qty=3),
    n("Draw Their Fire"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Scrambled Transmission", True),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Corran Horn"),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum", True),
    n("Battle Plan", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Jabba's Haven"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Galen, Secret Apprentice", qty=3),
    n("Masterful Move & Endor Occupation", qty=2),
    n("A Sith's Weapon"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("You Are Beaten"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Darth Maul", qty=2),
    n("Boba Fett In Slave I", True, qty=2),
    n("Image Of The Dark Lord", True),
    n("Control", qty=2),
    n("Why Didn't You Tell Me?", True),
    n("Ghhhk"),
    n("Force Field", True, qty=2),
    n("Victory"),
    n("Battle Droid Squad", qty=2),
    n("Trophy Of A Kill"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Grievous' Lightsabers"),
    n("Zuckuss In Mist Hunter"),
    n("Maul's Sith Infiltrator"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("IG-100 MagnaGuard", qty=2),
    n("Imperial Propaganda", True),
    n("Search And Destroy"),
    n("Dengar With Blaster Carbine", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blaster Rack", True),
    n("Sniper & Dark Strike"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Nal Hutta"),
    n("No Escape"),
    n("The Phantom Menace"),
    n("Elis In Hinthra"),
    n("P-59"),
    n("Probot"),
    n("Dr. Evazan & Ponda Baba"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
]
DS_ADD = []
