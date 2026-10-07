#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Steve Harpster.

Source: 2012mpcday1.pdf pages 31–32 (2010 form, 12 shields).
Name HARPSTER dested Steve Harpster. Username blank.
p31 Dark Spice / Kessel.
p32 Light STEP (V) / Watch Your Step (V).
Do not dest as a new person. Do not rewrite 2013 MPC HARPSTER leftover.
"""
from __future__ import annotations

PLAYER = "Steve Harpster"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 32
DS_PAGE = 31
LS_SCAN = "2012 Match Play Championship Day 1 Steve Harpster LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Steve Harpster DS.png"
LS_DECK_NAME = "STEP (V)"
DS_DECK_NAME = "Spice"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name HARPSTER dested Steve Harpster. "
    "Username blank. Event MPC. Deck Name STEP (V). LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC HARPSTER leftover. "
    "WYS OBJ dested Watch Your Step / This Place Can Be A Little Rough True. "
    "CEC dested Corellian Engineering Corporation. "
    "NQA dested No Questions Asked. "
    "Palejo Reshad dested Palejo Reshad. "
    "Obi-Wan In Radiant 7 dested as written. "
    "Mirax dested Mirax Terrik. "
    "LTWW dested Let The Wookiee Win. "
    "Tantive 4 dested Tantive IV. "
    "Yoda GW dested Yoda, Great Warrior. "
    "HMBHT dested Hear Me Baby, Hold Together. "
    "Romas Lock dested Romas \"Lock\" Navander. "
    "LSSZ dested Luke Skywalker, Jedi Knight. "
    "Antilles Maneuver Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Boshek Brash Smuggler dested BoShek, Brash Smuggler. "
    "Sergeant Bruckman dested as written. "
    "Boshek's Modified Ship dested BoShek's Modified Freighter. "
    "Falcon dested Han, Chewie, And The Falcon. "
    "Leia RP dested Leia, Rebel Princess. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Insurrection / Combo dested Insurrection & Aim High. "
    "Blind Jedi dested as written. Fallen Jedi dested as written. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name HARPSTER dested Steve Harpster. "
    "Username blank. Event MPC. Deck Name Spice. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC HARPSTER leftover. "
    "Kessel dested Kessel empty. "
    "Kessel Admin Office dested Kessel: Spice Mines - Administrator's Office True. "
    "The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Darth Maul w/ Stick dested Darth Maul With Lightsaber. "
    "GMT dested Grand Moff Tarkin. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Spice Mine Admin dested Spice Mine Administrator. "
    "Darth Sidious form 21 True and form 22 Non-V dested empty kept separate. "
    "GHKR dested Ghhhk. "
    "Where Are You Taking This dested Where Are You Taking This ... Thing?. "
    "Vader's Lightsaber dested Darth Vader's Lightsaber. "
    "Maul's Ship dested Maul's Sith Infiltrator. "
    "PLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "ARKA dested Arica. "
    "Galen's Stick dested Galen's Lightsaber, Vader's Gift. "
    "Galen dested Galen Marek, Starkiller. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "Blockade FS Bridge dested Blockade Flagship: Bridge. "
    "Spice Mine Ops dested Spice Mine Operations. "
    "NA CHUBY NA dested Ni Chuba Na??. "
    "Something Special PFT dested Something Special Planned For Them. "
    "K+D dested Knowledge And Defense. "
    "Shield 9 Death Star Sentry crossed, Resistance Non-V dest replacement without (V). "
    "CHYBC dested Come Here You Big Coward. YCHF dested You Cannot Hide Forever. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Senator Leia Organa", True),
    n("Civil Disorder", True),
    n("Hindsight", True),
    n("Palejo Reshad"),
    n("Menace Fades"),
    n("Spaceport Scoundrels Guild", True),
    n("No Questions Asked", True, qty=3),
    n("Obi-Wan In Radiant 7", True),
    n("Escape Pod", True),
    n("Evacuation Control", True),
    n("Captain Han Solo"),
    n("Mirax Terrik"),
    n("Dash Rendar", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Tantive IV", True),
    n("Yoda, Great Warrior", True, qty=2),
    n("Imperial Atrocity", True),
    n("Sense"),
    n("Blind Jedi", True),
    n("Hear Me Baby, Hold Together", True),
    n("Romas \"Lock\" Navander"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Antilles Maneuver", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Alderaan Consular Ship", True),
    n("BoShek, Brash Smuggler", True),
    n("Spaceport Street"),
    n("Houjix"),
    n("Corran Horn", qty=2),
    n("Spaceport Docking Bay"),
    n("Sergeant Bruckman"),
    n("Fallen Jedi", True),
    n("BoShek's Modified Freighter", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Home One: Docking Bay"),
    n("Han, Chewie, And The Falcon", True),
    n("Leia, Rebel Princess"),
    n("Chewie", True),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience"),
    n("Booster In Pulsar Skate", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Insurrection & Aim High"),
    n("Laudica", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("The Professor", True),
    n("Chasm", True),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Jabba's Prize", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office", True),
    n("Imperial Command"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Force Field", True, qty=2),
    n("Victory", True, qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Tarkin's Bounty", True),
    n("Grand Moff Tarkin", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Spice Mine Administrator", True, qty=2),
    n("Garindan", True),
    n("Darth Sidious", True),
    n("Darth Sidious"),
    n("Ghhhk"),
    n("P-59"),
    n("Force Push", True),
    n("Blast Door Controls"),
    n("Where Are You Taking This ... Thing?", True),
    n("Darth Vader's Lightsaber"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Sidious' Lightsaber", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("The Emperor", True),
    n("Kessel: Spice Mines - Prison", True),
    n("Kessel: Spice Mines - Docking Bay", True),
    n("Kessel Surveillance System", True),
    n("Protocol Failure", True),
    n("Arica"),
    n("Cold Feet", True),
    n("Much Anger In Him"),
    n("Conquest", True),
    n("The Phantom Menace"),
    n("Alert My Star Destroyer"),
    n("I'll Take Them Myself", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Blockade Flagship: Bridge"),
    n("You Are Beaten"),
    n("Imperial Justice", True),
    n("Grand Admiral Thrawn"),
    n("Spice Mine Operations", True),
    n("Blaster Rack", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Lightsaber Deficiency", True),
    n("Something Special Planned For Them", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Firepower", True),
    n("Battle Order"),
    n("Fanfare", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
