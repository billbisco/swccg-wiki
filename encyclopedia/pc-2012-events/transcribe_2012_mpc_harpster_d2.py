#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Steve Harpster.

Source: 2012mpcday2.pdf pages 5–6 (2010 form, 12 shields).
Name HARPSTER dested Steve Harpster. Username blank.
p05 Light STEPC(V). p06 Dark HD (V).
Do not dest as a new person. Do not rewrite 2013 leftovers.
Do not rewrite Day 1 leftover Watch Your Step (V) / Kessel.
Pack player-stubs/Steve_Harpster.wiki.
"""
from __future__ import annotations

PLAYER = "Steve Harpster"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2012 Match Play Championship Day 2 Steve Harpster LS.png"
DS_SCAN = "2012 Match Play Championship Day 2 Steve Harpster DS.png"
LS_DECK_NAME = "STEPC(V)"
DS_DECK_NAME = "HD (V)"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name HARPSTER dested Steve Harpster. Username blank. "
    "Event MPC Day 2. Deck Name STEPC(V). LIGHT. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Do not rewrite Day 1 leftover Watch Your Step (V). "
    "WYS True dested Watch Your Step / This Place Can Be A Little Rough True analog leftover Harpster IN THE 60 AND START. "
    "HFTMF dested Heading For The Medical Frigate analog leftover Harpster IN THE 60. "
    "Booster in Pulsar Skate True dested Booster In Pulsar Skate True analog leftover Harpster. "
    "Boshek Brash Smuggler True dested BoShek, Brash Smuggler True analog leftover Harpster. "
    "Boshek's Ship Freighter True dested BoShek's Modified Freighter True analog leftover Harpster. "
    "Alderaan's Consular Ship True dested Alderaan Consular Ship True analog leftover Harpster. "
    "Obi in Radiant 7 dested Obi-Wan In Radiant 7 analog leftover Harpster. "
    "Tantive 4 True dested Tantive IV True analog leftover Harpster. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Harpster. "
    "Blind Jedi True dested as written analog leftover Harpster. "
    "Fallen Jedi True dested as written analog leftover Harpster. "
    "Yoda Great Warrior True dested analog leftover Harpster. "
    "Antilles Maneuver Combo True dested Antilles Maneuver & Rebel Reinforcements True analog leftover Harpster. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin analog leftover Harpster. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover Harpster. "
    "Mirax dested Mirax Terrik analog leftover Harpster. "
    "Palejo Reshad dested analog leftover Harpster. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader analog leftover Harpster. "
    "Romas Lock dested Romas \"Lock\" Navander analog leftover Harpster. "
    "Let The Wookie True dested Let The Wookiee Win True analog leftover Harpster. "
    "Home 1 Docking Bay dested Home One: Docking Bay analog leftover Harpster. "
    "Spaceport Scoundrels Guild True dested analog leftover Harpster. "
    "LSSK dested Luke Skywalker, Jedi Knight analog leftover Harpster. "
    "NQA True dested No Questions Asked True analog leftover Harpster. "
    "Insurrection / Aim High dested Insurrection & Aim High analog leftover Harpster. "
    "Corellian Eng Corp True dested Corellian Engineering Corporation True analog leftover Harpster. "
    "Falcon True dested Han, Chewie, And The Falcon True analog leftover Harpster. "
    "Captain Han dested Captain Han Solo analog leftover Harpster. "
    "Chewie True dested analog leftover Harpster. "
    "AFA True dested Anger, Fear, Aggression True analog leftover Harpster IN THE 60. "
    "Shield Abyss True dested Abyss True analog leftover. "
    "Shield DDTA True dested Don't Do That Again True analog leftover Harpster. "
    "Shield Let's Keep Optimism True dested Let's Keep A Little Optimism Here True analog leftover Harpster. "
    "Shield Wise Advice / Do, Or Do Not dested Do, Or Do Not & Wise Advice analog leftover Marlow. "
    "Shield Simple Tricks True dested Simple Tricks And Nonsense True analog leftover Harpster. "
    "Unique overcounts sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name HARPSTER dested Steve Harpster. Username blank. "
    "Event MPC Day 2. Deck Name HD (V). DARK. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Do not rewrite Day 1 leftover Kessel. "
    "Hunt Down And Destroy The Jedi True dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True analog leftover HD IN THE 60 AND START. "
    "Cyborg Commander True dested Grievous, Hunter Of Jedi True analog leftover Shaw. "
    "Cyborg Commander's Lightsabers True dested Grievous' Lightsabers True analog leftover Shaw. "
    "PILOTS dested Darth Vader, Dark Lord Of The Sith analog leftover Harpster. "
    "Vader's Lightsaber dested Darth Vader's Lightsaber analog leftover Harpster. "
    "Galen Secret Apprentice True dested Galen, Secret Apprentice True analog leftover Shaw. "
    "Galen's Lightsaber, Vader's Gift True dested analog leftover Harpster. "
    "General Nevar True dested analog leftover Wirfs. "
    "4-LOM w/ Concussion Rifle True dested 4-LOM With Concussion Rifle True analog leftover Foth. "
    "Grand Moff Tarkin True dested analog leftover Harpster. "
    "Dr Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover Shaw. "
    "Galen's Fighter True dested Rogue Shadow True analog leftover TMW Shaw. "
    "Victory True dested Victory analog leftover Harpster. "
    "Sniper & Dark Strike dested analog leftover Shaw. "
    "Naboo Theed Palace Courtyard dested Naboo: Theed Palace Courtyard analog leftover Graham. "
    "Coruscant dested Coruscant analog leftover Foth. "
    "A Sith's Plans True dested analog leftover Alperstein. "
    "Ability x3 True dested Ability, Ability, Ability True analog leftover Shaw. "
    "Prepared Defenses True dested analog leftover Foth IN THE 60. "
    "The Emperor True dested analog leftover Nelson. "
    "Search And Destroy dested analog leftover. "
    "Garindan True dested analog leftover Wirfs. "
    "Lightsaber Deficiency True dested analog leftover Harpster. "
    "Protocol Failure True dested analog leftover Harpster. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation analog leftover Harpster. "
    "Where Are You Taking This Thing True dested Where Are You Taking This ... Thing? True analog leftover Harpster. "
    "According To My Design True dested analog leftover. "
    "We Must Accelerate Our Plans dested analog leftover Harpster. "
    "Something Special Planned For Them True dested analog leftover Wirfs. "
    "Endor Shield True dested analog leftover Schoenthal. "
    "Gift of the Master True dested Gift Of The Master True analog leftover Harpster. "
    "Ni Chuba Na?? True dested analog leftover Harpster. "
    "A Sith's Weapon True dested analog leftover Shaw. "
    "Knowledge And Defense True dested analog leftover Murray IN THE 60. "
    "Shield Code Clearance True dested Do They Have A Code Clearance? True analog leftover Shaw. "
    "Shield Come Here You Big Coward dested analog leftover Harpster. "
    "Unique overcounts sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Alter", True),
    n("Heading For The Medical Frigate"),
    n("Booster In Pulsar Skate", True),
    n("BoShek, Brash Smuggler", True),
    n("BoShek's Modified Freighter", True),
    n("Senator Leia Organa", True),
    n("Alderaan Consular Ship", True),
    n("Obi-Wan In Radiant 7"),
    n("Tantive IV", True),
    n("Lando Calrissian, Scoundrel"),
    n("Blind Jedi", True),
    n("Fallen Jedi", True),
    n("Yoda, Great Warrior", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Antilles Maneuver", True),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Imperial Atrocity", True, qty=4),
    n("Grimtaash"),
    n("Houjix"),
    n("Escape Pod", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Mirax Terrik"),
    n("Sergeant Bruckman"),
    n("Palejo Reshad"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Laudica", True),
    n("Romas \"Lock\" Navander"),
    n("Dash Rendar", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild", True),
    n("Spaceport Street"),
    n("Spaceport City"),
    n("Corellia", True),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("No Questions Asked", True, qty=3),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Han, Chewie, And The Falcon", True),
    n("Captain Han Solo"),
    n("Chewie", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Abyss", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Yavin Sentry", True),
    n("Jabba's Prize", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Battle Droid Squad", True, qty=2),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Grievous' Lightsabers", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Darth Vader's Lightsaber"),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("General Nevar", True),
    n("Grand Admiral Thrawn"),
    n("Mara Jade With Lightsaber", True),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Moff Tarkin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Rogue Shadow", True),
    n("Victory", True, qty=2),
    n("Imperial Justice", True),
    n("Sniper & Dark Strike"),
    n("Blaster Rack", True),
    n("Endor"),
    n("Naboo: Theed Palace Courtyard"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("A Sith's Plans", True),
    n("Ability, Ability, Ability", True),
    n("Prepared Defenses", True),
    n("Blockade Flagship: Hallway"),
    n("The Emperor", True),
    n("Ghhhk"),
    n("Search And Destroy"),
    n("Garindan", True),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure", True),
    n("Force Field", True, qty=2),
    n("No Escape"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Blast Door Controls"),
    n("Revenge Of The Sith", True),
    n("Where Are You Taking This ... Thing?", True),
    n("According To My Design", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Cold Feet", True),
    n("Something Special Planned For Them", True),
    n("Endor Shield", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("A Sith's Weapon", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
]
DS_ADD = []
