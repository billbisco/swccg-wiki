#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Cole Lepine Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Cole Lepine"
USERNAME = "clepine"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 56
DS_PAGE = 55
LS_SCAN = "2013 Match Play Championship p56 Cole Lepine LS.png"
DS_SCAN = "2013 Match Play Championship p55 Cole Lepine DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username clepine. Event MPC '13, 26 January 2013. "
    "Deck title They came from…. Light. "
    "Watch Your Step / This Place Can Be A Little Rough. "
    "L. RP dested Leia, Rebel Princess. Boshek, BS dested BoShek, Brash Smuggler. "
    "Lando, UH dested Lando Calrissian, Unlikely Hero. Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Yoda, GW dested Yoda, Great Warrior. LSJK dested Luke Skywalker, Jedi Knight. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. Crix dested General Crix Madine. "
    "Bruckman dested Sergeant Bruckman. Bo's Ship dested Pulsar Skate. "
    "All Wings combo dested All Wings Report In & Darklighter Spin. "
    "Antman combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Retort dested Corellian Retort. Guild dested Spaceport Scoundrels Guild. "
    "NQA dested No Questions Asked. Fallen Portal dested Fallen Portal. "
    "AFA dested Anger, Fear, Aggression. CEC dested Corellian Engineering Corporation. "
    "I & AH dested Insurrection & Aim High. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username clepine. Event MPC '13, 26 January 2013. "
    "Deck title Behind!. Dark. "
    "Ralltiir Operations / In The Hands Of The Empire. "
    "IAO dested Imperial Arrest Order. SSPET dested Something Special Planned For Them. "
    "ADTFTR dested A Dark Time For The Rebellion. Line 13 Weapon Lev was crossed out; ditto of ADTFTR. "
    "WDYTM dested Why Didn't You Tell Me. Lightsaber Def dested Lightsaber Deficiency. "
    "WTAPN dested We're In Attack Position Now. HLCBY dested He Hasn't Come Back Yet. "
    "Iceheart dested Ysanne Isard. DV DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "DV BOTJ dested Darth Vader, Betrayer Of The Jedi. Kir Kanos w/ FF dested Kir Kanos With Force Pike. "
    "GMT dested Grand Moff Tarkin. GAT dested Grand Admiral Thrawn. "
    "F3B Sectoid Commander dested ISB Sector Commander. Evax dested Officer Evax. "
    "K+D dested Knowledge And Defense. Financial District dested Ralltiir: Spaceport Financial District. "
    "We'll Let Fate-a Decide, Huh? in the shield box. CHYBC dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. DSS dested Death Star Sentry. AUG dested A Useless Gesture. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Chewie", True),
    n("Leia, Rebel Princess"),
    n("Padme Naberrie", True),
    n("BoShek, Brash Smuggler", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Obi-Wan Kenobi", True),
    n("Obi-Wan Kenobi"),
    n("Maris Brood, Fallen Jedi"),
    n("Yoda, Great Warrior", True),
    n("Yoda, Great Warrior"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Mirax Terrik"),
    n("Dash Rendar", True),
    n("Dash Rendar"),
    n("Pulsar Skate", True),
    n("Lady Luck", True),
    n("Imperial Atrocity", True),
    n("Imperial Atrocity"),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("Rebel Barrier", qty=2),
    n("Antilles Maneuver", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Corellian Retort", True),
    n("Houjix"),
    n("Grimtaash"),
    n("Spaceport Scoundrels Guild", True),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Home One: Docking Bay"),
    n("No Questions Asked", True),
    n("No Questions Asked"),
    n("Tantive IV", True),
    n("K'lor'slug", True),
    n("Fallen Portal"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("Weapons Display", True),
    n("Jabba's Prize"),
]
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Imperial Arrest Order"),
    n("Imperial Decree", True),
    n("Something Special Planned For Them", True),
    n("Imperial Justice", True),
    n("Imperial Domination", True),
    n("Imperial Domination"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Command", qty=2),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("He Hasn't Come Back Yet"),
    n("Outflank", True),
    n("Sneak Attack", True),
    n("Trample"),
    n("Control & Set For Stun"),
    n("Close Call", True),
    n("Ghhhk"),
    n("Why Didn't You Tell Me", True),
    n("Lightsaber Deficiency", True),
    n("We're In Attack Position Now"),
    n("Blizzard 1", True),
    n("Blizzard 4"),
    n("Tempest 1"),
    n("Blizzard 2", True),
    n("Blizzard Scout 1", True),
    n("Vader's Personal Shuttle"),
    n("Victory", True),
    n("Emperor's Personal Shuttle"),
    n("Conquest", True),
    n("Endor"),
    n("Kashyyyk"),
    n("Ralltiir: Spaceport Financial District", True),
    n("Spaceport Street"),
    n("Spaceport Prefect's Office"),
    n("Spaceport Docking Bay"),
    n("Ysanne Isard", True),
    n("Colonel Davod Jon"),
    n("Emperor Palpatine", qty=2),
    n("Janus Greejatus"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("General Veers", True),
    n("Arica"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Admiral Ozzel"),
    n("Kir Kanos With Force Pike", True),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("ISB Sector Commander", True),
    n("Officer Evax"),
    n("Garindan", True),
    n("Commander Merrejk"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
]
DS_ADD = []
