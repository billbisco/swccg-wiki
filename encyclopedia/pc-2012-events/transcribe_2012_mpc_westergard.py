#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Westergard.

Source: 2012mpcday1.pdf pages 143–144 (2010 form, 12 shields).
Name Chris West# dested Chris Westergard analog 2013 leftover PLAYER="Chris Westergard".
Username blank.
p143 Light Plead My Case To The Senate. p144 Dark A Stunning Move.
Pack player-stubs/Chris_Westergard.wiki (is_bio False).
Do not dest as Jan Westergard.
Do not dest as a new person.
Do not rewrite 2013 leftover Watch Your Step / Wookiee Slaving Operation.
Do not rewrite 2014 leftover The Hyperdrive Generator's Gone / Death Star: Conference Room (V).
"""
from __future__ import annotations

PLAYER = "Chris Westergard"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 143
DS_PAGE = 144
LS_SCAN = "2012 Match Play Championship Day 1 Chris Westergard LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Westergard DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris West# dested Chris Westergard analog 2013 leftover. "
    "Username blank. LIGHT/DARK empty dest Light from the 60s. "
    "Do not dest as Jan Westergard. Do not dest as a new person. "
    "Do not rewrite 2013 leftover Watch Your Step. "
    "Plead My Case / Sanity & Comp dested Plead My Case To The Senate / Sanity And Compassion empty analog leftover. "
    "CC: Jedi Council Chamber dested Coruscant: Jedi Council Chamber analog leftover. "
    "Coruscant Senate dested Coruscant: Galactic Senate analog leftover. "
    "Bail Organa, Father dested Bail Organa, Father Of Rebellion analog leftover. "
    "Senator Padme True dested Senator Padmé Amidala True analog leftover. "
    "Yoda MFT dested Yoda, Master Of The Force analog leftover. "
    "Luke Skywalker JK dested Luke Skywalker, Jedi Knight analog leftover. "
    "HC & F dested Houjix & Out Of Nowhere analog leftover. "
    "Wedge in Red Squad 1 True dested Wedge In Red Squadron 1 True analog leftover. "
    "Strike Force dested Strikeforce analog leftover. "
    "So This How Liberty Dies dested So This Is How Liberty Dies analog leftover. "
    "Seeking an Audience dested Seeking An Audience analog leftover. "
    "Sorry about the mess / BP dested Sorry About The Mess & Blaster Proficiency analog leftover. "
    "Jedi Lev True dested Jedi Levitation True analog leftover. "
    "NOOOOO True dested NOOOOOOOOOOOO! True analog leftover. "
    "Unwanted U True dested as written. "
    "Control & TV dested Control & Tunnel Vision analog leftover. "
    "Swing & a Miss dested Swing-And-A-Miss analog leftover. "
    "Line 60 Knowledge & Defense Anger Fear True dested Knowledge And Defense True and Anger, Fear, Aggression True sheet-accurate unique 61. "
    "Dark shields crossed dest Light replacements analog leftover. Unique 61. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Westergard dested analog 2013 leftover. "
    "Username blank. LIGHT/DARK empty dest Dark from the 60s. "
    "Do not dest as Jan Westergard. Do not dest as a new person. "
    "Do not rewrite 2013 leftover Wookiee Slaving Operation. "
    "A Stunning Move True dested A Stunning Move / A Valuable Hostage True analog leftover. "
    "Palp's pad True dested Coruscant: Palpatine's Quarters True analog leftover. "
    "Ditto OD True dested Coruscant: Private Platform True analog Erwin. "
    "Gift of the Mentor True dested Gift Of The Master True analog leftover. "
    "Ni Chuba Na True dested Ni Chuba Na?? True analog leftover. "
    "Prepared Defenses empty dested in the 60 analog leftover. "
    "Dengar with Blaster True dested Dengar With Blaster Carbine True analog leftover. "
    "Maul's DB Lightsaber dested Maul's Double-Bladed Lightsaber analog leftover. "
    "Why didn't you tell me True dested Why Didn't You Tell Me? True analog leftover. "
    "Dre E & PB True dested Dr. Evazan & Ponda Baba True analog leftover. "
    "Phantom Menace dested The Phantom Menace analog leftover. "
    "Galen App True dested Galen, Secret Apprentice True analog leftover. "
    "IG Bodyguard Droid True dested IG-100 MagnaGuard True analog leftover. "
    "Cyborg Commander, Hunter True dested Grievous, Hunter Of Jedi True analog leftover. "
    "Cyborg Commander's Lightsaber True dested Grievous' Lightsabers True analog leftover. "
    "MM & EO dested Masterful Move & Endor Occupation analog leftover. "
    "Where are you taking this ... thing True dested Where Are You Taking This ... Thing? True analog leftover. "
    "4-Lom True dested 4-LOM With Concussion Rifle True analog leftover. "
    "Galen, Secret Apprentice True x2 AND empty kept separate analog Foth. Unique 60. Shields 12. "
    "Knowledge And Defense empty dested in the 60 analog leftover."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Strike Planning"),
    n("Wokling", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Mace Windu"),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Bail Organa"),
    n("Senator Padmé Amidala", True),
    n("Obi-Wan Kenobi", True),
    n("General Calrissian"),
    n("Yoda, Master Of The Force"),
    n("Corran Horn"),
    n("Senator Mon Mothma"),
    n("Mas Amedda"),
    n("Senator Leia Organa"),
    n("Luke Skywalker, Jedi Knight"),
    n("Coruscant: Night Club"),
    n("Coruscant"),
    n("Taking Them With Us"),
    n("Jedi Lightsaber", qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Booster In Pulsar Skate", True),
    n("Wedge In Red Squadron 1", True),
    n("Alderaan Consular Ship", True),
    n("Gold Leader In Gold 1"),
    n("Menace Fades"),
    n("Imperial Atrocity"),
    n("Strikeforce"),
    n("So This Is How Liberty Dies"),
    n("Seeking An Audience"),
    n("Grimtaash"),
    n("Sai'torr Kal Fas"),
    n("Senate Hovercam"),
    n("Sorry About The Mess & Blaster Proficiency", qty=3),
    n("Jedi Levitation", True, qty=2),
    n("Might Of The Republic", True),
    n("Life Debt", True),
    n("Blaster Deflection", qty=2),
    n("Alter", True),
    n("NOOOOOOOOOOOO!", True),
    n("Sense", qty=2),
    n("Unwanted U", True),
    n("A Jedi's Resilience", qty=2),
    n("Control & Tunnel Vision"),
    n("Swing-And-A-Miss"),
    n("Knowledge And Defense", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here"),
    n("Aim High"),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well"),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Insidious Prisoner", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Private Platform", True),
    n("Jabba's Palace", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses"),
    n("Blaster Deflection", True),
    n("A Dark Time For The Rebellion", True),
    n("Force Field", True, qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Control", qty=2),
    n("Sniper & Dark Strike", qty=2),
    n("Why Didn't You Tell Me?", True),
    n("Ghhhk"),
    n("Elis Helrot"),
    n("Battle Droid Squad", True, qty=2),
    n("Probot", True),
    n("Dr. Evazan & Ponda Baba", True),
    n("Nal Hutta"),
    n("Boba Fett In Slave I"),
    n("Restraining Bolt"),
    n("The Phantom Menace", qty=2),
    n("Garindan", True),
    n("Galen, Secret Apprentice", True, qty=2),
    n("Blockade Flagship: Hallway"),
    n("IG-100 MagnaGuard", True),
    n("Oh, Switch Off"),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Your Powers Are Weak, Old Man", True),
    n("Blockade Flagship: Bridge"),
    n("Grievous' Lightsabers", True),
    n("P-59"),
    n("Masterful Move & Endor Occupation"),
    n("Victory"),
    n("Something Special Planned", True),
    n("Ability, Ability, Ability", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("No Escape"),
    n("Galen, Secret Apprentice"),
    n("Zuckuss In Mist Hunter"),
    n("Where Are You Taking This ... Thing?", True),
    n("Blockade Flagship: Docking Bay"),
    n("4-LOM With Concussion Rifle", True),
    n("Maul Strikes"),
    n("Weapon Levitation"),
    n("Bossk In Hound's Tooth"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture"),
    n("There Is No Try"),
]
DS_ADD = []
