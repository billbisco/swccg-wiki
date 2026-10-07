#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Brian Hollingworth.

Source: 2012mpcday1.pdf pages 85–86 (2010 form, 12 shields).
Name Brian Hollingworth dested Brian Hollingworth (not Tom Hollingworth).
Username Kinslayer. p85 DARK box / Light 60. p86 LIGHT box / Dark 60.
Dest sides from the 60s. Pack player-stubs/Brian_Hollingworth.wiki.
"""
from __future__ import annotations

PLAYER = "Brian Hollingworth"
USERNAME = "Kinslayer"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 85
DS_PAGE = 86
LS_SCAN = "2012 Match Play Championship Day 1 Brian Hollingworth LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Brian Hollingworth DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Hollingworth dested Brian Hollingworth. "
    "Username Kinslayer. DARK box checked; dest Light from the 60 (WYS). "
    "Deck Name blank. Event Date/Name blank. Analog Tom Hollingworth is a different person. "
    "TFT dested TFT True. WYS dested Watch Your Step / This Place Can Be A Little Rough True. "
    "Captain Han dested Captain Han Solo. CEC dested Corellian Engineering Corporation True. "
    "Insurrection Aim High dested Insurrection & Aim High. Heading dested Heading For The Medical Frigate. "
    "Chewie dested Chewie True. Fallen Jedi dested Maris Brood, Fallen Jedi True. "
    "Jedi Luke dested Luke Skywalker, Jedi Knight x2. Street dested Spaceport Street. "
    "HO:DB dested Home One: Docking Bay. Spaceport DB dested Spaceport Docking Bay. "
    "Leia, RP dested Leia, Rebel Princess. Atrocity dested Imperial Atrocity True x3. "
    "Boshek Brash Smuggler dested BoShek, Brash Smuggler True. Corran dested Corran Horn x2. "
    "Barrier dested Rebel Barrier. Wedge RSL dested Wedge Antilles, Red Squadron Leader x2. "
    "Palejo dested Palejo Reshad. Romas dested Romas \"Lock\" Navander. Mirax dested Mirax Terrik. "
    "Yoda GW dested Yoda, Great Warrior True x2. LTWW dested Let The Wookiee Win True x2. "
    "All Wings combo dested All Wings Report In & Darklighter Spin. ICBW dested It Could Be Worse. "
    "Seeking Audience dested Seeking An Audience True. Booster in Skate dested Booster In Pulsar Skate True. "
    "Boshek freighter dested BoShek's Modified Freighter True. Retort dested Corellian Retort True. "
    "Antilles Man dested Antilles Maneuver True. Antilles Man combo dested Antilles Maneuver & Rebel Reinforcements True x2. "
    "Scoundrels Guild dested Spaceport Scoundrels Guild True. Klor Slug dested K'lor'slug True. "
    "Jabba Prize dested Jabba's Prize True. Tragedy dested A Tragedy Has Occurred. "
    "DDTA dested Don't Do That Again True. Insight dested Your Insight Serves You Well True. "
    "Shield 12 cropped; dest shields 11. Unique 60."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Hollingworth dested Brian Hollingworth. "
    "Username Kinslayer. LIGHT box checked; dest Dark from the 60 (IO/IC). "
    "Deck Name blank. Event Date/Name blank. Analog Tom Hollingworth is a different person. "
    "KYC dested KYC True. IO/IC dested Imperial Occupation / Imperial Control True. "
    "Ice Plains dested Hoth: Ice Plains True. Ni Chuba Na dested Ni Chuba Na?? True. "
    "Darth Vader dested Darth Vader, Dark Lord Of The Sith True. "
    "Black Leader dested Juno Eclipse, Black Leader True. "
    "Emperor's Reach dested Maarek Stele, The Emperor's Reach True. "
    "Dark Time Rebellion dested A Dark Time For The Rebellion True x2. "
    "Marquand bliz 6 dested Marquand In Blizzard 6 True. Image Dark Lord dested Image Of The Dark Lord True. "
    "Igar dested Commander Igar True. Target Generator dested Target The Main Generator. "
    "Main Power Gens dested Hoth: Main Power Generators. Prep Def dested Prepared Defenses True. "
    "YMSYL dested You May Start Your Landing. Decree empty then Decree True kept separate. "
    "3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "6th Marker dested Hoth: Mountains (6th Marker). Code Clearance dested Do They Have A Code Clearance?. "
    "Nevar dested General Nevar True. Ommni Box + It's Worse dested Ommni Box & It's Worse True. "
    "Thrawn dested Grand Admiral Thrawn. OP as Planned dested Operational As Planned True. "
    "We're Attack Position Now dested We're In Attack Position Now x2. "
    "Command dested Imperial Command x2. Coward dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever True. TINT dested There Is No Try. "
    "Shield 12 cropped; dest shields 11. Unique 60."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("TFT", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Corellian Engineering Corporation", True),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Heading For The Medical Frigate"),
    n("Chewie", True),
    n("Dash Rendar", True, qty=2),
    n("Laudica", True),
    n("Antilles Maneuver", True),
    n("Yoda, Great Warrior", True, qty=2),
    n("Spaceport Scoundrels Guild", True),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Maris Brood, Fallen Jedi", True),
    n("K'lor'slug", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Spaceport Street"),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Imperial Atrocity", True, qty=3),
    n("BoShek, Brash Smuggler", True),
    n("Corran Horn", qty=2),
    n("Rebel Barrier"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Palejo Reshad"),
    n("Romas \"Lock\" Navander"),
    n("Mirax Terrik"),
    n("Let The Wookiee Win", True, qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("It Could Be Worse"),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("Spiral"),
    n("Enhanced Proton Torpedoes", True),
    n("Tantive IV", True),
    n("Booster In Pulsar Skate", True),
    n("BoShek's Modified Freighter", True),
    n("Corellian Retort", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("Grimtaash"),
    n("Desperate Reach", True),
    n("No Questions Asked", True, qty=3),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("KYC", True),
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Ice Plains", True),
    n("Ni Chuba Na??", True),
    n("Veers", True),
    n("Admiral Motti", True),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Juno Eclipse, Black Leader", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Hoth Blockade", True),
    n("AT-AT Cannon", True),
    n("Protocol Failure", True),
    n("Marquand In Blizzard 6", True),
    n("Image Of The Dark Lord", True),
    n("Commander Igar", True),
    n("Conquest", True),
    n("Target The Main Generator"),
    n("Walker Garrison"),
    n("Endor Shield", True),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Prepared Defenses", True),
    n("You May Start Your Landing"),
    n("Imperial Decree"),
    n("Imperial Decree", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Do They Have A Code Clearance?"),
    n("Hoth: Mountains (6th Marker)"),
    n("General Nevar", True),
    n("Grand Moff Tarkin", True, qty=2),
    n("Why Didn't You Tell Me?", True),
    n("Ommni Box & It's Worse", True),
    n("Grand Admiral Thrawn"),
    n("Operational As Planned", True),
    n("Blizzard 4", qty=2),
    n("Blizzard 2", True, qty=2),
    n("Tempest 1"),
    n("Victory", True, qty=2),
    n("Katana", True),
    n("Devastator", True),
    n("Blockade Support Ship", True),
    n("We're In Attack Position Now", qty=2),
    n("Force Push", True),
    n("Cold Feet", True),
    n("Trample", qty=2),
    n("Imperial Command", qty=2),
    n("No Escape"),
    n("General Veers", True),
    n("Control", qty=2),
    n("Garindan", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Imperial Detention", True),
    n("Death Star Sentry", True),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Secret Plans"),
]
DS_ADD = []
