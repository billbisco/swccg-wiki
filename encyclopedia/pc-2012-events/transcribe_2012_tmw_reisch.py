#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Nick Reisch.

Source: 2012TMWDay1.pdf pages 17–18 (typed slang printout, not a handwritten
Xerox form). Name Nick Reisch dested Nick Reisch analog leftover 2013 TMW /
2013 Worlds / 2013 MPC / player-stubs/Nick_Reisch.wiki. Username blank
(typed dump has no Username field). p17 Dark. p18 Light. Do not dest as a
new person. Do not dest 2013 TMW Reisch 60s again.
"""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 18
DS_PAGE = 17
LS_SCAN = "2012 Texas Mini Worlds Day 1 Nick Reisch LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Nick Reisch DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Nick Reisch dested Nick Reisch analog leftover player-stubs/Nick_Reisch.wiki. "
    "Username blank. Do not dest as a new person. Do not dest 2013 TMW Reisch 60s again."
)
LS_NOTE = (
    "Typed slang printout. Name Nick Reisch dested Nick Reisch. Username blank. "
    "Anger, Fear, Aggression True dested Anger, Fear, Aggression analog leftover Hendon IN THE 60. "
    "Tatooine: Slave Quarters dested analog leftover Hendon. "
    "Communing dested Communing analog leftover Hendon start. "
    "Master Kenobi dested analog leftover Hendon. "
    "Wokling True dested analog leftover Hendon. "
    "Maneuvering Flaps combo dested Maneuvering Flaps & Nick Of Time analog leftover Eier. "
    "Tatooine (Ep1) dested Tatooine analog leftover Hendon. "
    "Tatooine: Obi's Hut True dested Tatooine: Obi-Wan's Hut analog leftover Hendon True. "
    "Commander Luke True x2 dested Commander Luke Skywalker analog leftover True qty=2. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader analog leftover Brandon. "
    "Commander Wedge True dested Commander Wedge Antilles analog leftover True. "
    "Hobbie dested Derek \"Hobbie\" Klivian analog leftover Richards. "
    "Zev dested Zev Senesca analog leftover Eier. "
    "Scoundrel Lando True dested Lando Calrissian, Scoundrel analog leftover True. "
    "Ackbar True dested Admiral Ackbar analog leftover Hendon True. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover Hendon. "
    "Yoda great warrior dested Yoda, Great Warrior analog leftover Hendon. "
    "Padme True dested Padme Naberrie analog leftover Hendon True. "
    "Shmi dested Shmi Skywalker analog leftover Hendon. "
    "Threepio whps dested Threepio With His Parts Showing analog leftover Hendon. "
    "HCF True dested Han, Chewie, And The Falcon analog leftover True. "
    "Tantive True dested Tantive IV analog leftover True. "
    "Let's Go Left True x3 crossed handwritten x2 dest qty=2 analog leftover Lush. "
    "Strikeforce True dested Strike Force analog leftover Hendon True. "
    "Scrambled Transmission True crossed dest replacement Obi-Wan's Apparition True analog leftover. "
    "houjix dested Houjix analog leftover Hendon. "
    "It's Not My fault True dested It's Not My Fault! analog leftover True. "
    "Hear me baby True dested Hear Me Baby, Hold Together analog leftover Hendon True. "
    "Yub Yub commander dested Yub Yub, Commander analog leftover Hodur. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements analog leftover Hendon. "
    "Shield Simple Tricks & Nonsense dested Simple Tricks And Nonsense analog leftover Hendon. "
    "Shield Don't do That Again True dested Don't Do That Again analog leftover Lush True. "
    "Shield Do Or Do Not dested Do, Or Do Not analog leftover Hendon. "
    "Shield Yavin Sentry True dested Yavin Sentry analog leftover Lush True. "
    "Unique 59 sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Typed slang printout. Name Nick Reisch dested Nick Reisch. Username blank. "
    "Knowledge & Defense True dested Knowledge And Defense analog leftover Hendon True IN THE 60. "
    "Hunt Down True dested Hunt Down And Destroy The Jedi analog leftover Hendon True. "
    "Coruscant (SE) dested Coruscant analog leftover Hendon. "
    "A Sith's Plans dested analog leftover Hendon. "
    "Ni Chuba Na True dested Ni Chuba Na?? analog leftover Hendon True. "
    "Gift of the Master dested Gift Of The Master analog leftover Hendon. "
    "Naboo: 3/2 dested Naboo: Theed Palace Generator Core analog leftover Hendon. "
    "Dungeon (Prison) dested Jabba's Palace: Dungeon analog leftover Krueger. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith analog leftover Hendon qty=3. "
    "Galen dested Galen, Secret Apprentice analog leftover Hendon qty=3. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover Hendon qty=2. "
    "EPP Mara dested Mara Jade With Lightsaber analog leftover. "
    "Boba Fett, BH dested Boba Fett, Bounty Hunter analog leftover Lush. "
    "EPP 4LOM True dested 4-LOM With Concussion Rifle analog leftover Hendon True. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Hendon. "
    "Galen's Fighter dested Rogue Shadow analog leftover Hendon. "
    "Vader's Ligthsaber dested Darth Vader's Lightsaber analog leftover Hendon. "
    "Galen's Ligthsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift analog leftover Hendon. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Hendon. "
    "Ability Ability Ability True dested Ability, Ability, Ability analog leftover True. "
    "Search & Destroy dested Search And Destroy analog leftover Bordier. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover Hendon qty=3. "
    "MM&EO dested Masterful Move & Endor Occupation analog leftover Hendon. "
    "Imbalance combo dested Imbalance & Kintan Strider analog leftover Brandon. "
    "Sniper & DS dested Sniper & Dark Strike analog leftover Richards. "
    "Weapon Levitation combo dested Weapon Levitation & The Empire's Back analog leftover Nathan. "
    "Shield Weapon of a Sith dested Weapon Of A Sith analog leftover Lush. "
    "Shield Do They Have a Code Clearance True dested Do They Have A Code Clearance? analog leftover Chu True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Maneuvering Flaps & Nick Of Time"),
    n("Home One: War Room"),
    n("Tatooine"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Jundland Wastes"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Commander Luke Skywalker", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Commander Wedge Antilles", True),
    n("Derek \"Hobbie\" Klivian"),
    n("Zev Senesca"),
    n("Dash Rendar", True),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel", True),
    n("Admiral Ackbar", True),
    n("Major Haash'n"),
    n("Leia, Rebel Princess"),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", True),
    n("Tantive IV", True),
    n("Bright Hope", True),
    n("Spiral"),
    n("Rogue 1", qty=2),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Dual Laser Cannons", True),
    n("Let's Go Left", True, qty=2),
    n("Launching The Assault"),
    n("Flash Of Insight", True, qty=3),
    n("Echo Base Garrison"),
    n("Strike Force", True),
    n("Hindsight", True),
    n("Rebel Gunrunner"),
    n("Menace Fades"),
    n("Obi-Wan's Apparition", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("It's Not My Fault!", True),
    n("Hear Me Baby, Hold Together", True),
    n("Yub Yub, Commander"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Rebel Leadership", True, qty=3),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
    n("Yavin Sentry", True),
    n("Another Pathetic Lifeform", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Endor Shield", True),
    n("Endor"),
    n("Naboo: Theed Palace Generator Core"),
    n("Jabba's Palace: Dungeon"),
    n("Blockade Flagship: Bridge"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Mara Jade With Lightsaber"),
    n("P-59"),
    n("Boba Fett, Bounty Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("General Nevar"),
    n("Juno Eclipse, Black Leader"),
    n("Rogue Shadow"),
    n("Victory", qty=2),
    n("Darth Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Something Special Planned For Them", True),
    n("Revenge Of The Sith"),
    n("Ability, Ability, Ability", True),
    n("No Escape"),
    n("Protocol Failure"),
    n("Blaster Rack", True),
    n("Special Delivery", True),
    n("Search And Destroy"),
    n("Force Field", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Cold Feet", True),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk"),
    n("Imbalance & Kintan Strider"),
    n("Sense"),
    n("Force Lightning"),
    n("Sniper & Dark Strike"),
    n("Weapon Levitation & The Empire's Back"),
    n("Sith Fury", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Resistance", True),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
