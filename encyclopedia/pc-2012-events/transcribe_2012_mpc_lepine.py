#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Cole Lepine.

Source: 2012mpcday1.pdf pages 15–16 (handwritten notebook 60s).
Name Cole Lepine dested Cole Lepine. Username clepine.
p15 Dark IO/IC (V). p16 Light WYS(V).
"""
from __future__ import annotations

PLAYER = "Cole Lepine"
USERNAME = "clepine"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2012 Match Play Championship Day 1 Cole Lepine LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Cole Lepine DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten notebook 60 bound into 2012mpcday1.pdf."
LS_NOTE = (
    "Handwritten notebook. Name Cole Lepine dested Cole Lepine. Username clepine. "
    "LS Decklist. Event MPC 2012. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Cap'n Han Solo dested Captain Han Solo. HFTMF dested Heading For The Medical Frigate. "
    "CEC dested Corellian Engineering Corporation. I & AH dested Insurrection & Aim High. "
    "Merc Sunset dested Merc Sunlet. Evac Control dested Evacuation Control. "
    "Atrocity dested Imperial Atrocity. Seeking dested Seeking An Audience. "
    "NQA dested No Questions Asked. Spiral dested Spiral. "
    "BoShek's Ship dested Pulsar Skate. B:PS dested Booster In Pulsar Skate. "
    "LSJK dested Luke Skywalker, Jedi Knight. Yoda the Great dested Yoda, Great Warrior. "
    "Fallen Jeedai dested Maris Brood, Fallen Jedi. Chewie dested Chewie. "
    "Leia dested Princess Leia. Leia, RP dested Leia, Rebel Princess. "
    "Padmé dested Padmé Naberrie. Lando C, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Boshek, BS dested BoShek, Brash Smuggler. Wedge, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Romas \"Lock\" Navander dested Romas \"Lock\" Navander. "
    "Antman Combo dested Antilles Maneuver & Rebel Reinforcements. Antman dested Antilles Maneuver. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "Yub Yub, Commander dested Yub Yub, Commander. AFA dested Anger, Fear, Aggression. "
    "H1:DB dested Home One: Docking Bay. Spaceport S. Guild dested Spaceport Scoundrels Guild. "
    "D,O DN dested Do, Or Do Not. DDTA dested Don't Do That Again. "
    "J. Prize dested Jabba's Prize. LKALOH dested Let's Keep A Little Optimism Here. "
    "STAN dested Simple Tricks And Nonsense. Y. Sentry dested Yavin Sentry. "
    "Unique overcounts sheet-accurate (No Questions Asked x2, Luke Skywalker, Jedi Knight x2, "
    "Yoda, Great Warrior x2, Maris Brood, Fallen Jedi x2, Corran Horn x2, "
    "Wedge Antilles, Red Squadron Leader x2, Let The Wookiee Win x3, "
    "Antilles Maneuver & Rebel Reinforcements x2, All Wings Report In & Darklighter Spin x2). "
    "(V) as written on the notebook."
)
DS_NOTE = (
    "Handwritten notebook. Name Cole Lepine dested Cole Lepine. Username clepine. "
    "DS Decklist. Event MPC 2012. "
    "IO/IC dested Imperial Occupation / Imperial Control. "
    "Hoth: MPG dested Hoth: Main Power Generators. Prep Def dested Prepared Defenses. "
    "NCN?? dested Ni Chuba Na??. YMSYL dested You May Start Your Landing. "
    "Hoth: DP (3rd Marker) dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth: Mountains (6th Marker) dested Hoth: Mountains (6th Marker). "
    "TTMG dested Target The Main Generator. WIAPN crossed, WIAPN dested We're In Attack Position Now. "
    "B. Leader dested Juno Eclipse, Black Leader. Darth Vader dested Darth Vader, Dark Lord Of The Sith. "
    "The Reach dested Maarek Stele, The Emperor's Reach. "
    "I. Justice (V) crossed, Tarkin's Bounty dested as replacement. "
    "I. Propaganda dested Imperial Propaganda. "
    "Control crossed, Control & Set For Stun dested as replacement. "
    "ADTFTR dested A Dark Time For The Rebellion. I. Command dested Imperial Command. "
    "WDYTM? dested Why Didn't You Tell Me?. MM & EO dested Masterful Move & Endor Occupation. "
    "Omni Box & It's Worse dested Ommni Box & It's Worse. K & D dested Knowledge And Defense. "
    "DTHACC? dested Do They Have A Code Clearance? in the main 60. "
    "AUG dested A Useless Gesture. CHYBC dested Come Here You Big Coward. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing. TINT dested There Is No Try. "
    "YCHF dested You Cannot Hide Forever. "
    "Unique overcounts sheet-accurate (Garindan x2, Victory x2, "
    "A Dark Time For The Rebellion x2, Imperial Command x2, Trample x2). "
    "Main unique 58 sheet-accurate. (V) as written on the notebook."
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
    n("Merc Sunlet", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True),
    n("K'lor'slug", True),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("No Questions Asked", True, qty=2),
    n("Spiral"),
    n("Tantive IV", True),
    n("Pulsar Skate", True),
    n("Booster In Pulsar Skate", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Yoda, Great Warrior", True, qty=2),
    n("Maris Brood, Fallen Jedi", True, qty=2),
    n("Chewie", True),
    n("Princess Leia", True),
    n("Leia, Rebel Princess"),
    n("Padmé Naberrie", True),
    n("Lando Calrissian, Scoundrel"),
    n("BoShek, Brash Smuggler", True),
    n("Corran Horn", qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Dash Rendar", True),
    n("Romas \"Lock\" Navander"),
    n("Palejo Reshad"),
    n("Mirax Terrik"),
    n("Let The Wookiee Win", True, qty=3),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Antilles Maneuver", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Yub Yub, Commander", True),
    n("Corellian Retort", True),
    n("Escape Pod", True),
    n("Sense"),
    n("Houjix"),
    n("Anger, Fear, Aggression", True),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again"),
    n("Jabba's Prize", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Imperial Decree"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Hoth Blockade", True),
    n("We're In Attack Position Now"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Admiral Piett"),
    n("Juno Eclipse, Black Leader", True),
    n("Commander Igar", True),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Darth Maul"),
    n("Garindan", True, qty=2),
    n("Gela Yeens", True),
    n("General Nevar", True),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Veers", True),
    n("Maul's Sith Infiltrator"),
    n("Flagship Executor"),
    n("Victory", True, qty=2),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6", True),
    n("Tempest 1"),
    n("Do They Have A Code Clearance?"),
    n("Image Of The Dark Lord", True),
    n("Tarkin's Bounty", True),
    n("Imperial Propaganda", True),
    n("No Escape"),
    n("Control & Set For Stun"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Crash Landing"),
    n("Imperial Command", qty=2),
    n("Trample", qty=2),
    n("Walker Garrison"),
    n("Why Didn't You Tell Me?", True),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("Ommni Box & It's Worse"),
    n("Operational As Planned", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
