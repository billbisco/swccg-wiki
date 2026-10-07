#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Jess Ojala.

Source: 2012NationalsDay1.pdf pages 52–53 (handwritten 2010 Xerox).
p52 Dark Name Jessica O. / p53 Light Name Jess Ojala dested Jess Ojala analog leftover
empty last-initial merge. Username blank. Analog leftover generate empty dest as written.
Do not dest as Jessica Echeverria.
Pack player-stubs/Jess_Ojala.wiki.
"""
from __future__ import annotations

PLAYER = "Jess Ojala"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 53
DS_PAGE = 52
LS_SCAN = "2012 US Nationals Day 1 Jess Ojala LS.png"
DS_SCAN = "2012 US Nationals Day 1 Jess Ojala DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Jessica O. / Jess Ojala dested Jess Ojala analog leftover "
    "empty last-initial merge. Username blank. Do not dest as Jessica Echeverria."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jess Ojala dested Jess Ojala analog leftover empty. "
    "Username blank. LIGHT checked. Event Date 6/9/12 Event Name Nationals. "
    "Do not dest as Jessica Echeverria. Line 1 Heading For The Medical Frigate. "
    "LS_START Yavin 4: Massassi Throne Room analog leftover Anderson line 32. "
    "Insurrection dested Insurrection analog leftover not combo. "
    "Quick Draw dested Quick Draw True analog leftover Brady. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas True analog leftover Virtual Block. "
    "Eject combo dested Eject! Eject! Eject! & Imperial Atrocity True analog leftover Grant. "
    "Naboo: Theed Palace Generator dested Naboo: Theed Palace Generator analog leftover Molitor. "
    "Home One: Docking Bay dested Home One: Docking Bay analog leftover Morgan. "
    "Obi-Wan, Crazy Wizard dested Obi-Wan, Crazy Old Wizard True analog leftover x2. "
    "Luke Skywalker, Strong In The dested Luke Skywalker, Strong In The Force True analog leftover x3. "
    "Yoda, Great Warrior dested Yoda, Great Warrior True analog leftover x2. "
    "Senator Mon Mothma dested Senator Mon Mothma True analog leftover. "
    "Taiz dested leftover_xerox. "
    "Chewie dested Chewbacca, Protector True analog leftover Echeverria. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi True analog leftover Sean Miller. "
    "Anger, Fear, Aggression dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Shield Only Jedi Carry That Weapon dested Only Jedi Carry That Weapon analog leftover. "
    "Let's Keep A Little Optimism Here dested Let's Keep A Little Optimism Here True analog leftover. "
    "Shield 12 blank skip. Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Jessica O. dested Jess Ojala analog leftover empty last-initial. "
    "Username blank. DARK checked. Event Date 6/9/12 Event Name Nationals. "
    "Do not dest as Jessica Echeverria. Line 1 HD True dested Hunt Down And Destroy The Jedi True analog leftover George. "
    "If The Trace Was Correct dested If The Trace Was Correct True analog leftover. "
    "Ni Chuba Na dested Ni Chuba Na?? True analog leftover Frafjord. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover George. "
    "Gela Yeons dested Gela Yeens True analog leftover alex_w. "
    "Boba Fett, RBH dested Boba Fett, Renowned Bounty Hunter analog leftover leftover_xerox. "
    "Ice-Heart dested Ysanne Isard analog leftover Echeverria. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover George. "
    "Darth Vader w/ Lightsaber dested Darth Vader With Lightsaber analog leftover Brady. "
    "Blak 4 dested DS-61-4 analog leftover Nieland. "
    "Galen's Fighter dested Rogue Shadow analog leftover George. "
    "Galen's Lightsaber dested Galen's Lightsaber, Vader's Gift analog leftover George. "
    "Vader's Saber dested Vader's Lightsaber analog leftover Sokol. "
    "Darth Vader, Betrayer / Boty / Vader's BOTY dested Darth Vader, Betrayer Of The Jedi analog leftover Sokol x3 unique overcount. "
    "Lat Dam dested Lateral Damage analog leftover Banger. "
    "Executor Med Chamber dested Executor: Meditation Chamber analog leftover Sokol. "
    "Tat: Mos Eisley dested Tatooine: Mos Eisley analog leftover. "
    "Knowledge And Defense dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Shield Come Here dested Come Here You Big Coward analog leftover. "
    "Shields 8–12 blank skip. Unique 60. Shields 7."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("Insurrection"),
    n("Quick Draw", True),
    n("Draw Their Fire"),
    n("Projection Of A Skywalker", qty=2),
    n("Flash Of Insight", True),
    n("Flash Of Insight"),
    n("Sai'torr Kal Fas", True),
    n("Eject! Eject! Eject! & Imperial Atrocity", True),
    n("Bacta Tank"),
    n("Mantellian Savrip"),
    n("Blast The Door, Kid!"),
    n("Rebel Barrier", qty=2),
    n("Sense", qty=3),
    n("It Could Be Worse", qty=2),
    n("First Aid"),
    n("The Force Is Strong With This One"),
    n("Gift Of The Mentor"),
    n("Slight Weapons Malfunction"),
    n("Alter"),
    n("Naboo: Theed Palace Generator"),
    n("Hoth"),
    n("Home One: Docking Bay"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: Echo Command Center"),
    n("Yavin 4: Massassi Throne Room"),
    n("Obi-Wan's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Journal"),
    n("Lando In Millennium Falcon"),
    n("Gold Leader In Gold 1", True),
    n("Corellian Corvette"),
    n("Spiral"),
    n("Wedge In Red Squadron 1"),
    n("Red Leader In Red 1"),
    n("Obi-Wan, Crazy Old Wizard", True, qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Corran Horn"),
    n("Yoda, Great Warrior", True, qty=2),
    n("Senator Mon Mothma", True),
    n("Taiz"),
    n("Chewbacca, Protector", True),
    n("Kal'Falnl C'ndros"),
    n("General Carlist Rieekan", True),
    n("Owen Lars & Beru Lars"),
    n("Leia With Blaster Rifle"),
    n("Maris Brood, Fallen Jedi", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Chasm", True),
    n("Do, Or Do Not", True),
    n("Only Jedi Carry That Weapon"),
    n("Weapons Display", True),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("If The Trace Was Correct", True),
    n("Imperial City"),
    n("Coruscant"),
    n("A Sith's Plans"),
    n("Something Special Planned For Them", True),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
    n("Galen", qty=2),
    n("Imperial Stormtrooper"),
    n("Lord Sidious", qty=2),
    n("Mod Terrik"),
    n("Grievous, Hunter Of Jedi"),
    n("D-l9 And Pulu"),
    n("Gela Yeens", True),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("Mott-T'uk"),
    n("Bossk", True),
    n("Darth Vader, Betrayer Of The Jedi", qty=3),
    n("Tumbris"),
    n("Lt. Cabbel"),
    n("Ponda Baba", True),
    n("Ysanne Isard"),
    n("Juno Eclipse, Black Leader"),
    n("Salacious Crumb"),
    n("Darth Vader With Lightsaber"),
    n("Di-Ciro"),
    n("Commander Lennox", True),
    n("ISB Commander"),
    n("Limited Resources"),
    n("Scanning Crew", qty=2),
    n("Dark Maneuvers"),
    n("Takeel"),
    n("Elis Helrot", qty=2),
    n("Gravity Shadow"),
    n("DS-61-4"),
    n("Sentinel-Class Landing Craft"),
    n("TIE Scout", qty=2),
    n("Combat Cloud Car"),
    n("TIE Advanced x1"),
    n("Rogue Shadow"),
    n("Freyanag's Rifle", True),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Insight From Rebellion"),
    n("Lateral Damage"),
    n("Search And Destroy"),
    n("Hoth"),
    n("Hoth: Defensive Perimeter"),
    n("Executor: Meditation Chamber"),
    n("Tatooine: Mos Eisley"),
    n("Imperial Pilot", True),
    n("Prepared Defenses"),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Firepower"),
    n("Reactor Terminal"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
