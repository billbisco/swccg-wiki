#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Andrew Bollentino.

Source: 2012mpcday1.pdf pages 49–50 (2010 form, 12 shields).
Name Andrew Bollemo / Andrew Bolletino dested Andrew Bollentino.
Username Lord Bane (Dark; Light Username blank).
p49 Light Plead My Case. p50 Dark Moonwalking / Imperial Occupation (V).
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Andrew Bollentino"
USERNAME = "Lord Bane"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 49
DS_PAGE = 50
LS_SCAN = "2012 Match Play Championship Day 1 Andrew Bollentino LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Andrew Bollentino DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "Moonwalking"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Andrew Bollemo dested Andrew Bollentino. "
    "Username blank on Light; Lord Bane on Dark. LIGHT checked. Event Date 2/11/12. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Plead My Case / Sanity dested Plead My Case To The Senate / Sanity And Compassion. "
    "Cor: JCC dested Coruscant: Jedi Council Chamber. Cor: Senate + Senate Throne Room "
    "dested Coruscant: Galactic Senate x2. HFTMF dested Heading For The Medical Frigate. "
    "Cor: Night Club dested Coruscant: Night Club True. Sei Taria dested Sei Taria. "
    "Sen. Leia Organa dested Senator Leia Organa True. "
    "Bail Organa, Father of R dested Bail Organa, Father Of Rebellion True x2. "
    "LS JK dested Luke Skywalker, Jedi Knight. Yoda, MOFO dested Yoda, Master Of The Force. "
    "TWHPS dested Threepio With His Parts Showing. SATM / BP dested "
    "Sorry About The Mess & Blaster Proficiency x2. Sense / Recoil dested Sense & Recoil In Fear. "
    "GL in G1 dested Gold Leader In Gold 1 True. AJR dested A Jedi's Resilience x2. "
    "NOOOOO dested NOOOOOOOOOOOO! True. Senator Padme Amidala dested Senator Padmé Amidala. "
    "Han, Chewie, Falcon dested Han, Chewie, And The Falcon True. "
    "Wedge in RS1 dested Wedge In Red Squadron 1 True. "
    "Alderaan Cons. Ship dested Radiant VII True. Taking them w/ us dested Taking Them With Us. "
    "General Cal. dested General Calrissian. Control / TV dested Control & Tunnel Vision. "
    "LS, Rebel Scout dested Luke Skywalker, Rebel Scout. AFA dested Anger, Fear, Aggression. "
    "Shield Proficiency dested The Professor. Unique 60. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Andrew Bolletino dested Andrew Bollentino. "
    "Username Lord Bane. DARK checked. Deck Name Moonwalking. Event Date 2/11/12. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "IO/IC True dested Imperial Occupation / Imperial Control True. "
    "YMSYL dested You May Start Your Landing. Ni Chuba Na dested Ni Chuba Na?? True. "
    "Hoth: Main P.G. dested Hoth: Main Power Generators. "
    "4-LOM w/ Conc. Ri. dested 4-LOM With Concussion Rifle True. "
    "ISB Sec. Comm dested ISB Sector Commander True. "
    "The Emp. Reach dested Maarek Stele, The Emperor's Reach True. "
    "Black Leader dested Juno Eclipse, Black Leader True. GMT dested Grand Moff Tarkin True. "
    "Veers dested Veers True. Boba Fett, BH dested Boba Fett, Bounty Hunter True. "
    "G.A. Thrawn dested Grand Admiral Thrawn. DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Maul w/ L.S. dested Darth Maul With Lightsaber. Hoth: Mountains dested "
    "Hoth: Mountains (6th Marker). Hoth. Def. Per. dested Hoth: Defensive Perimeter (3rd Marker). "
    "Marquand in Bliz. 6 dested Marquand In Blizzard 6 True. Temp. Scout 6 dested Tempest Scout 6. "
    "Flagship Ex. + two dittos dested Flagship Executor x3. Alert My S.D. dested Alert My Star Destroyer. "
    "Prepare for a Surf. Attack dested Prepare For A Surface Attack. "
    "Do they Have A.C.C. dested Do They Have A Code Clearance? in the main 60. "
    "We're in Att. Pos. Now dested We're In Attack Position Now. "
    "Battle Deployment + ditto dested Battle Deployment x2. "
    "A Dark Time For The Reb True + ditto dested A Dark Time For The Rebellion True x2. "
    "Imperial Command + ditto dested Imperial Command x2. Trample + ditto dested Trample x2. "
    "Outflank True + ditto dested Outflank True x2. Imperial Artillery + ditto dested Imperial Artillery x2. "
    "K+D dested Knowledge And Defense True. YCHF dested You Cannot Hide Forever. "
    "Coward dested Come Here You Big Coward. Fire Power dested Firepower. "
    "Dittos inherit (V). Unique 60. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Wokling", True),
    n("Strike Planning", True),
    n("Quick Draw", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate", qty=2),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Night Club", True),
    n("Sei Taria"),
    n("So This Is How Liberty Dies", True),
    n("Senator Leia Organa", True),
    n("Bail Organa, Father Of Rebellion", True, qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Lightsaber"),
    n("Coruscant"),
    n("K'lor'slug", True),
    n("Sai'torr Kal Fas", True),
    n("Menace Fades"),
    n("Yoda, Master Of The Force"),
    n("Might Of The Republic", qty=2),
    n("Yavin 4", True),
    n("It's A Trap!"),
    n("Threepio With His Parts Showing"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Mas Amedda"),
    n("Sense & Recoil In Fear"),
    n("Blaster Deflection", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Gold Leader In Gold 1", True),
    n("A Jedi's Resilience", qty=2),
    n("NOOOOOOOOOOOO!", True),
    n("Obi-Wan Kenobi", True),
    n("Mace Windu", True, qty=2),
    n("Senator Padmé Amidala"),
    n("Bail Organa", True),
    n("Jedi Lightsaber", True, qty=3),
    n("Han, Chewie, And The Falcon", True),
    n("Wedge In Red Squadron 1", True),
    n("Imperial Atrocity", True, qty=2),
    n("Escape Pod", True),
    n("Radiant VII", True),
    n("Senator Mon Mothma", True),
    n("Obi-Wan's Lightsaber"),
    n("Taking Them With Us"),
    n("General Calrissian"),
    n("Control & Tunnel Vision"),
    n("Luke Skywalker, Rebel Scout"),
    n("Spiral"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("The Professor"),
    n("Weapons Display"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well"),
    n("Don't Do That Again"),
    n("Another Pathetic Lifeform"),
    n("Aim High"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("You May Start Your Landing"),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("Prepared Defenses"),
    n("4-LOM With Concussion Rifle", True),
    n("General Nevar", True),
    n("ISB Sector Commander", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Juno Eclipse, Black Leader", True),
    n("Grand Moff Tarkin", True),
    n("Veers", True),
    n("Commander Igar"),
    n("Admiral Piett"),
    n("Boba Fett, Bounty Hunter", True),
    n("Grand Admiral Thrawn"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Maul With Lightsaber"),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6", True),
    n("Tempest 1"),
    n("Blizzard 4"),
    n("Tempest Scout 6"),
    n("Victory", True),
    n("Flagship Executor", qty=3),
    n("Hoth Blockade", True),
    n("Alert My Star Destroyer"),
    n("Prepare For A Surface Attack"),
    n("Do They Have A Code Clearance?"),
    n("Imperial Propaganda", True),
    n("Image Of The Dark Lord", True),
    n("We're In Attack Position Now"),
    n("Battle Deployment", qty=2),
    n("Close Call", True),
    n("Walker Garrison", True),
    n("Why Didn't You Tell Me?", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Command", qty=2),
    n("Trample", qty=2),
    n("Force Push", True),
    n("Outflank", True, qty=2),
    n("Imperial Artillery", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Detention", True),
    n("Wipe Them Out, All Of Them", True),
    n("Allegations Of Corruption", True),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Abyss"),
    n("Fanfare"),
    n("Battle Order"),
    n("Firepower"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
