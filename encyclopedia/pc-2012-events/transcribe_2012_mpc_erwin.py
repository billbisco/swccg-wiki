#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Erwin.

Source: 2012mpcday1.pdf pages 1–2 (2010 form, 12 shields).
Name C. Erwin / Chris Erwin dested Chris Erwin. Username blank.
Email [redacted] stays off the article.
Dark A Stunning Move (V). Light Yavin 4 (V).
"""
from __future__ import annotations

PLAYER = "Chris Erwin"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2012 Match Play Championship Day 1 Chris Erwin LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Erwin DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
DS_NOTE = (
    "Handwritten 2010 Xerox. Name C. Erwin dested Chris Erwin. Username blank. "
    "DARK checked. Event 2012 MPC 2/11/12. ASM dested A Stunning Move / A Valuable Hostage. "
    "Palp Quarters dested Coruscant: Palpatine's Quarters. Private Platform dested "
    "Coruscant: Private Platform. Gift of Meste dested Gift Of The Master. "
    "Ni Chuba Na dested Ni Chuba Na??. Know & Def dested Knowledge And Defense. "
    "1st Strike dested First Strike. Cyborg Com dested Grievous, Hunter Of Jedi. "
    "You Are Beaten dested You Are Beaten. Flagship hallway dested Blockade Flagship: Hallway. "
    "IG body guard dested IG-100 MagnaGuard. Sith Fury dested Sith Fury. Elis dested Elis Helrot. "
    "Cyborg Com LS dested Grievous' Lightsabers. B FS DB dested Blockade Flagship: Docking Bay. "
    "Enemies in Mist dested Zuckuss In Mist Hunter. 4-LOM w/ gun dested 4-LOM With Concussion Rifle. "
    "I am put it's worse dested It's Worse. Look sir two droids dested Look Sir, Droids. "
    "Oh Switch Off dested Oh, Switch Off. Droid Squad dested Battle Droid Squad. "
    "Pote Maul dested Jango Fett, The Assassin. Sniper / DS dested Sniper & Dark Strike. "
    "B FS Bridge dested Blockade Flagship: Bridge. Galen dested Galen Marek, Starkiller. "
    "Masterful Move / EO dested Masterful Move & Endor Occupation. Maul dual saber dested "
    "Maul's Double-Bladed Lightsaber. Maul YA dested Darth Maul, Young Apprentice. "
    "Dr. E + PB dested Dr. Evazan & Ponda Baba. Gavin dested Reegesk. Celchu LS dested "
    "Galen's Lightsaber, Vader's Gift. Imp Propaganda dested Imperial Propaganda. "
    "Imp Barrier dested Imperial Barrier. Imbalance + KS dested Imbalance. "
    "Boba + Slave I dested Boba Fett In Slave I. Ghhhk those rebels dested "
    "Ghhhk & Those Rebels Won't Escape Us. They're Still Coming Through dested "
    "They're Still Coming Through!. Shield I'm free dested Imperial Decree. "
    "Alleg. of Coruspt dested Allegations Of Corruption. Unique overcounts "
    "sheet-accurate (IG-100 MagnaGuard x4, Battle Droid Squad x3). (V) from checkbox."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Erwin dested Chris Erwin. Username blank. "
    "LIGHT checked. Yavin 4 (V) is the starting location (no Objective). "
    "Massassi HQ dested Yavin 4: Massassi Headquarters. Squadron Assign dested "
    "Squadron Assignments. All Wings + DL Spin dested All Wings Report In & Darklighter Spin. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1. Wedge A. Red Squadron Leader dested "
    "Wedge Antilles, Red Squadron Leader. Red Squad 7 dested Red 7. Chewie dested Chewie, Enraged. "
    "Imp Atrocity dested Imperial Atrocity. Hubbie dested Wookiee Roar. Ant. Man / Rebel Rein. dested "
    "Antilles Maneuver & Rebel Reinforcements. Honor of Jedi dested Honor Of The Jedi. "
    "Projection of Sky dested Projection Of A Skywalker. Captain Han dested Captain Han Solo. "
    "Obi Wan Kenobi dested Obi-Wan Kenobi. Corran Horn dested Corran Horn. "
    "Yavin 4 docking bay dested Yavin 4: Docking Bay. Massassi War Room dested "
    "Yavin 4: Massassi War Room. Tatooine EP 1 dested Tatooine. S-traps dested It's A Trap!. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. Kev Sentry dested Kier Santage. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Flush of Insight dested Flash Of Insight. "
    "Unique overcounts sheet-accurate (I'll Take The Leader x3, All Wings Report In & "
    "Darklighter Spin x2, Let The Wookiee Win (V) x2, Imperial Atrocity (V) x2, "
    "Projection Of A Skywalker x2, Red 7 x2, Organized Attack x2, Lando Calrissian, Scoundrel x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Yavin 4: Massassi Headquarters"),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("Luke, Trust Me", True),
    n("Anger, Fear, Aggression", True),
    n("Restore Freedom To The Galaxy", True),
    n("Red 5", True),
    n("Luke Skywalker", True),
    n("All Wings Report In & Darklighter Spin", True, qty=2),
    n("Escape Pod", True),
    n("Tunnel Vision"),
    n("I'll Take The Leader", qty=3),
    n("Jek Porkins", True),
    n("Gold Leader In Gold 1", True),
    n("Millennium Falcon", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Outrider"),
    n("Red 6"),
    n("Massassi Base Sentry"),
    n("Legendary Starfighter"),
    n("Let The Wookiee Win", True, qty=2),
    n("Red 7", qty=2),
    n("Chewie, Enraged", True),
    n("Imperial Atrocity", True, qty=2),
    n("Wookiee Roar", True),
    n("A Few Maneuvers"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Honor Of The Jedi"),
    n("Projection Of A Skywalker", qty=2),
    n("Captain Han Solo"),
    n("X-wing Laser Cannon"),
    n("Obi-Wan Kenobi", True),
    n("Corran Horn"),
    n("Yavin 4: Docking Bay"),
    n("Yavin 4: Massassi War Room"),
    n("Organized Attack", qty=2),
    n("Tatooine"),
    n("It's A Trap!", True),
    n("Rebel Barrier"),
    n("Yoda, Great Warrior", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Kier Santage"),
    n("Baragwin"),
    n("Artoo-Detoo In Red 5"),
    n("Dash Rendar"),
    n("Houjix"),
    n("Biggs Darklighter", True),
    n("Haven"),
    n("Careful Planning", True),
    n("Flash Of Insight", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Aim High", True),
    n("A Tragedy Has Occurred", True),
    n("Do, Or Do Not"),
    n("Traffic Control", True),
    n("Jabba's Prize", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan"),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Private Platform", True),
    n("Insidious Prisoner", True),
    n("Prepared Defenses"),
    n("Gift Of The Master", True),
    n("Jabba's Haven", True),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
    n("First Strike"),
    n("Force Push", True),
    n("Grievous, Hunter Of Jedi", True, qty=3),
    n("You Are Beaten"),
    n("The Phantom Menace"),
    n("Blockade Flagship: Hallway"),
    n("IG-100 MagnaGuard", True, qty=4),
    n("No Escape"),
    n("Sith Fury", True, qty=2),
    n("Elis Helrot"),
    n("Grievous' Lightsabers", True),
    n("Blockade Flagship: Docking Bay"),
    n("Nal Hutta"),
    n("Blaster Rack", True),
    n("He Is Not Ready", True),
    n("Force Field", True, qty=2),
    n("Zuckuss In Mist Hunter"),
    n("4-LOM With Concussion Rifle"),
    n("Control", qty=2),
    n("It's Worse"),
    n("Look Sir, Droids", True, qty=2),
    n("Oh, Switch Off"),
    n("Battle Droid Squad", True, qty=3),
    n("Jango Fett, The Assassin"),
    n("Sniper & Dark Strike"),
    n("Blockade Flagship: Bridge"),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Reegesk", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Imperial Propaganda", True),
    n("Imperial Barrier"),
    n("Imbalance", True),
    n("Boba Fett In Slave I", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("They're Still Coming Through!"),
]
DS_SHIELDS = [
    n("Imperial Decree", True),
    n("Allegations Of Corruption"),
    n("There Is No Try", True),
    n("Weapon Of A Sith"),
    n("Abyss", True),
    n("Battle Order"),
    n("A Useless Gesture"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Imperial Detention", True),
    n("Resistance", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
