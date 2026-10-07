#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Justin Carulli.

Source: 2012mpcday1.pdf pages 59–60 (2010 form, 12 shields).
Name Justin Carulli dested Justin Carulli. Username blank.
p59 Light Center Of Tyranny. p60 Dark A Stunning Move.
Do not dest as a new person. Do not rewrite 2013 leftovers.
2013 leftover PLAYER="Justin Carulli" USERNAME blank; pack player-stubs/Justin_Carulli.wiki.
"""
from __future__ import annotations

PLAYER = "Justin Carulli"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 59
DS_PAGE = 60
LS_SCAN = "2012 Match Play Championship Day 1 Justin Carulli LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Justin Carulli DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Justin Carulli. Username blank. LIGHT checked. "
    "Event MPC 2012. Deck Name blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "A Center of Tyranny / A Liberated Shield dested Center Of Tyranny / A Liberated World. "
    "Gacta Infiltrator dested Bacta Infirmary. "
    "Wes Janson, Rogue Veteran dested Wes Janson, Rogue Veteran. "
    "Pycho Belbu dested Tycho Celchu True. "
    "Strike Force dested Strikeforce True. "
    "Kub Kubs Commander dested Yub Yub, Commander x4. "
    "Derek Hobbie Klivian dested Derek 'Hobbie' Klivian True. "
    "Commando Training & Klor'slug dested Commando Training & K'lor'slug. "
    "Leia True dested Leia (V). "
    "Veteran Rogue True and empty kept separate. "
    "Luke Skywalker, Rebel Hero True and empty dittos kept separate. "
    "Unique 60. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Justin Carulli. Username blank. DARK checked. "
    "Event MPC 2012. Deck Name blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "A Stunning Move / A Valuable Hostage dested A Stunning Move / A Valuable Hostage. "
    "Knowledge + Defense dested Knowledge And Defense True. "
    "I've Lost Artoo dested I've Lost Artoo! True. "
    "Giant Strikes dested Maul Strikes. "
    "Dr Evazan Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Boba Fett, Relentless BH dested Boba Fett, Relentless Bounty Hunter x2. "
    "Darth Maul, YA dested Darth Maul, Young Apprentice x3. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi x2. "
    "Out Flank dested Outflank True. "
    "Blockade Flagship: DB dested Blockade Flagship: Docking Bay. "
    "Galen, Secret Apprentice dested as written x3. "
    "Sniper + Dark Strike dested Sniper & Dark Strike x2. "
    "Maul's Double Blade Saber dested Maul's Double-Bladed Lightsaber. "
    "Unique 60. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Center Of Tyranny / A Liberated World"),
    n("Anger, Fear, Aggression", True),
    n("Coruscant", True),
    n("Planetary Shield"),
    n("Coruscant: Main Power Plant"),
    n("Coruscant: Lower Levels"),
    n("Rogue Insertion"),
    n("Heading For The Medical Frigate"),
    n("Declaration Of Rebellion"),
    n("Bacta Infirmary"),
    n("Rogue Squadron Tactics"),
    n("Wes Janson, Rogue Veteran"),
    n("Tycho Celchu", True),
    n("Luke's Blaster Pistol", True),
    n("Han, Chewie, And The Falcon"),
    n("Spiral"),
    n("Strikeforce", True),
    n("Projection Of A Skywalker"),
    n("Derek 'Hobbie' Klivian", True),
    n("Yub Yub, Commander", qty=4),
    n("We Wish To Board At Once", qty=2),
    n("Coruscant Celebration", qty=2),
    n("Dack Ralter", True),
    n("Luke Skywalker, Rebel Hero", True),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Civil Disorder", True),
    n("Kier Santage"),
    n("Honor Of The Jedi"),
    n("Leia, Rebel Princess"),
    n("Desperate Reach", True),
    n("Too Close For Comfort"),
    n("Escape Pod", True),
    n("Dash Rendar", True),
    n("Menace Fades"),
    n("Obi-Wan In Radiant VII"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Commando Training & K'lor'slug"),
    n("It Could Be Worse"),
    n("Dressel"),
    n("Imperial Atrocity", True),
    n("Hear Me Baby, Hold Together", True),
    n("Han, Chewie, And The Falcon"),
    n("Leia", True),
    n("Veteran Rogue", True),
    n("Houjix"),
    n("Corran Horn"),
    n("Veteran Rogue"),
    n("Odin Nesloor & First Aid"),
    n("Commander Narra"),
    n("Biggs, Rogue Legend"),
    n("Ten Numb", True),
    n("Tantive IV", True),
    n("Field Dressing"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Knowledge And Defense", True),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Trained In The Jedi Arts"),
    n("I've Lost Artoo!", True),
    n("Imperial Propaganda", True, qty=4),
    n("Force Field", True, qty=2),
    n("The Phantom Menace", qty=2),
    n("Maul Strikes"),
    n("A Dark Time For The Rebellion", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Sith Fury", True, qty=2),
    n("Ability, Ability, Ability", True),
    n("Why Didn't You Tell Me?", True),
    n("Victory", qty=2),
    n("Boba Fett, Relentless Bounty Hunter", qty=2),
    n("Boba Fett's Blaster Rifle", True),
    n("Battle Droid Squad", qty=3),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Stop Motion", True),
    n("Ket Maliss", qty=2),
    n("Trophy Of A Kill", qty=2),
    n("The Circle Is Now Complete"),
    n("Masterful Move & Endor Occupation"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blockade Flagship: Bridge"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Outflank", True),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Cold Feet", True),
    n("Galen, Secret Apprentice", qty=3),
    n("Blaster Rack", True),
    n("Dark Jedi Lightsaber", True),
    n("Sniper & Dark Strike", qty=2),
    n("A Sith's Weapon"),
    n("Zuckuss In Mist Hunter"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
