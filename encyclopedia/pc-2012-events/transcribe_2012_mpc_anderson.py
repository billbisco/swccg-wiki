#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: John Anderson.

Source: 2012mpcday1.pdf pages 35–36 (2002 DECK LIST print form).
Name John Anderson dested John Anderson. Username blank (no Username box).
p35 Light Pussy Sweet / Communing. p36 Dark Pussy Good / A Stunning Move.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 35
DS_PAGE = 36
LS_SCAN = "2012 Match Play Championship Day 1 John Anderson LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 John Anderson DS.png"
LS_DECK_NAME = "Pussy Sweet"
DS_DECK_NAME = "Pussy Good"
NOTE = "Handwritten 2002 DECK LIST print form."
LS_NOTE = (
    "Handwritten 2002 DECK LIST print form. Name John Anderson dested John Anderson. "
    "Username blank (no Username box). Event MPC Day 1 Date 2/11/12. LIGHT SIDE checked. "
    "Deck Title Pussy Sweet. Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Yavin 4 (v) dested Yavin 4 True (location). "
    "Communing dested Communing (objective). "
    "Master Kenobi dested Master Kenobi. "
    "The Camp dested The Camp True. "
    "Power Pivot line 6 plus line 7 under the saber dested Power Pivot x2. "
    "It's Not My Fault dested It's Not My Fault! True. "
    "Mag. Flaps dested Maneuvering Flaps True. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Lieut. Tarn Mison crossed, Kin Kian dest replacement. "
    "Dark Ralter dested Dack Ralter True. "
    "Biggs Rogue Legend dested Biggs, Rogue Legend. "
    "Derek Hobbie Klivian dested Derek \"Hobbie\" Klivian True. "
    "Y4: War Room dested Yavin 4: Massassi War Room. "
    "Tat: City Outskirts dested Tatooine: City Outskirts. "
    "Tat: Obi's Hut dested Tatooine: Obi-Wan's Hut True. "
    "Y4: Briefing Room dested Yavin 4: Briefing Room. "
    "Coruscant EP1 dested Coruscant. "
    "Tatooine EP1 dested Tatooine (Coruscant). "
    "WOOOOOOOOO! dested Wookiee Roar True. "
    "AFA dested Anger, Fear, Aggression True. "
    "Insight dested Your Insight Serves You Well True. "
    "Tragedy dested A Tragedy Has Occurred. "
    "Out Of That Assin dested Don't Do That Again True. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Light unique 59 sheet-accurate (form 40 Tarn Mison crossed). "
    "(V) from written (v); dittos inherit."
)
DS_NOTE = (
    "Handwritten 2002 DECK LIST print form. Name John Anderson dested John Anderson. "
    "Username blank. Event MPC Day 1 Date 2/11/12. DARK SIDE checked. "
    "Deck Title Pussy Good. Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "A Stunning Move dested A Stunning Move / A Valuable Hostage empty. "
    "Ni Chuba Na?? dested Ni Chuba Na?? True. "
    "Gift of the Master dested Gift Of The Master. "
    "Maul's Double Bladed Saber dested Maul's Double-Bladed Lightsaber. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Cyborg Commander Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "Galen Secret Apprentice dested Galen, Secret Apprentice as written. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "A Dark Time For The Rebellion dested A Dark Time For The Rebellion True. "
    "Masterful Move + End. Occupation dested Masterful Move & Endor Occupation. "
    "Victory dested Victory as written. "
    "Elis in Hinthra dested Elis In Hinthra. "
    "ZTMH dested Zuckuss In Mist Hunter. "
    "Dr. Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "4-LOM w/ Concussion Rifle dested 4-LOM With Concussion Rifle True. "
    "Boba Fett in Slave I dested Boba Fett In Slave I True. "
    "Search + Destroy dested Search And Destroy. "
    "Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine True. "
    "Form 52 crossed, Poggle dest replacement True. "
    "Blockade Flagship Docking Bay crossed on form 53, Hallway dest. "
    "Why Didn't You Tell Me dested Why Didn't You Tell Me? True. "
    "Control (Dagobah) dested Control. "
    "K+D dested Knowledge And Defense True. "
    "Useless Gesture dested A Useless Gesture True. "
    "Oppressive Enforcement crossed, Fanfare dest replacement True. "
    "Allegiance of Corruption dested Allegations Of Corruption. "
    "(V) from written (v); dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Yavin 4", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Squadron Assignments"),
    n("The Camp", True),
    n("Power Pivot", qty=2),
    n("Organized Attack", qty=3),
    n("It's Not My Fault!", True, qty=3),
    n("Maneuvering Flaps", True),
    n("Echo Base Garrison"),
    n("Obi-Wan's Apparition", True),
    n("Rebel Fleet"),
    n("Massassi Base Sentry"),
    n("Rebel Gunrunner"),
    n("Imperial Atrocity", True, qty=3),
    n("Hindsight", True),
    n("Dual Laser Cannon", True),
    n("Restore Freedom To The Galaxy"),
    n("Rebel Aces"),
    n("Enhanced Proton Torpedoes", True),
    n("Rogue 1", qty=2),
    n("Red Squadron 7", True),
    n("Rogue Squadron X-wing", qty=6),
    n("Red 6"),
    n("Yoda, Great Warrior"),
    n("Jek Porkins", True),
    n("Kin Kian"),
    n("Dack Ralter", True),
    n("Keir Santage"),
    n("Corran Horn"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Biggs, Rogue Legend"),
    n("Dash Rendar", True),
    n("Derek \"Hobbie\" Klivian", True),
    n("Commander Wedge Antilles", True),
    n("Yavin 4: Massassi War Room"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Yavin 4: Briefing Room"),
    n("Coruscant"),
    n("Tatooine (Coruscant)"),
    n("Use The Force"),
    n("Hear Me Baby, Hold Together", True),
    n("Wookiee Roar", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("Battle Plan", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice", True),
    n("Do, Or Do Not", True),
    n("Aim High"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Insidious Prisoner"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Trophy Of A Kill"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Nal Hutta"),
    n("Force Field", True, qty=2),
    n("IG-100 MagnaGuard", qty=2),
    n("Battle Droid Squad", qty=2),
    n("The Phantom Menace"),
    n("A Sith's Weapon"),
    n("Sniper & Dark Strike"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ghhhk"),
    n("Victory"),
    n("P-59"),
    n("Elis In Hinthra"),
    n("Darth Maul", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Image Of The Dark Lord", True),
    n("Blockade Flagship: Docking Bay"),
    n("Boba Fett In Slave I", True, qty=2),
    n("No Escape"),
    n("Maul's Sith Infiltrator"),
    n("Search And Destroy"),
    n("Dengar With Blaster Carbine", True),
    n("Poggle", True),
    n("Blockade Flagship: Hallway"),
    n("Blaster Rack", True),
    n("Blockade Flagship: Bridge"),
    n("Probot"),
    n("Why Didn't You Tell Me?", True),
    n("Control", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Resistance"),
    n("Fanfare", True),
    n("There Is No Try"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
]
DS_ADD = []
