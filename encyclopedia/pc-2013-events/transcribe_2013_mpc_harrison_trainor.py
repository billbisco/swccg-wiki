#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Matthew Harrison-Trainor Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 40
DS_PAGE = 39
LS_SCAN = "2013 Match Play Championship p40 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2013 Match Play Championship p39 Matthew Harrison-Trainor DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title WYS V. Light. "
    "Watch Your Step / This Place Can Be A Little Rough. "
    "Scoundrels Guild dested Spaceport Scoundrels Guild. "
    "Bruckman dested Sergeant Bruckman. Boshhk, Brash Smuggler dested BoShek, Brash Smuggler. "
    "Boshek's Freighter dested Pulsar Skate. Lando's Yacht dested Lady Luck. "
    "Corellian Return dested Corellian Slip. All Wings combo dested All Wings Report In & Darklighter Spin. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements. "
    "AFA dested Anger, Fear, Aggression. Student's Insight dested Your Insight Serves You Well. "
    "Jabba's Prize in the shield box dested the character. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title Rops. Dark. "
    "Ralltiir Operations / In The Hands Of The Empire. "
    "Spaceport Financial District dested Ralltiir: Spaceport Financial District. "
    "Ardan dested Lieutenant Commander Ardan. Davad Jan dested Colonel Davod Jon. "
    "Janus dested Janus Greejatus. Iceheart dested Ysanne Isard. "
    "The Reach dested Maarek Stele, The Emperor's Reach. Kir Kanos EPP dested Kir Kanos. "
    "Imbalance combo dested Imbalance & Kintan Strider. "
    "Control + SFS dested Control & Set For Stun. "
    "Masterful Move combo dested Masterful Move & Endor Occupation. "
    "WDYTM dested Why Didn't You Tell Me?. ADTFTR dested A Dark Time For The Rebellion. "
    "K+D dested Knowledge And Defense. YCHF dested You Cannot Hide Forever. "
    "Coward dested Come Here You Big Coward. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Spaceport Scoundrels Guild"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Home One: Docking Bay"),
    n("Heading For The Medical Frigate"),
    n("Corellian Engineering Corporation", True),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Captain Han Solo"),
    n("General Crix Madine"),
    n("Corran Horn"),
    n("Mirax Terrik"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Dash Rendar", True, qty=2),
    n("Sergeant Bruckman"),
    n("Leia, Rebel Princess", qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("BoShek, Brash Smuggler"),
    n("Padme Naberrie", True),
    n("Chewie", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Spiral"),
    n("Pulsar Skate"),
    n("Millennium Falcon", True),
    n("Lady Luck"),
    n("No Questions Asked", True, qty=3),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("Rebel Leadership", True, qty=2),
    n("Houjix"),
    n("Corellian Slip", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Rebel Barrier", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Antilles Maneuver", True),
    n("Escape Pod", True, qty=2),
    n("K'lor'slug", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Jabba's Prize", True),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir: Spaceport Financial District"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport Prefect's Office"),
    n("Endor"),
    n("Kashyyyk"),
    n("Kuat Drive Yards", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Imperial Domination", True, qty=2),
    n("Imperial Justice", True),
    n("Tyrant"),
    n("Conquest", True),
    n("Devastator", True),
    n("Victory"),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Grand Moff Tarkin", True),
    n("Kir Kanos"),
    n("Admiral Ozzel"),
    n("General Veers", True),
    n("Lieutenant Commander Ardan"),
    n("Colonel Davod Jon"),
    n("Arica"),
    n("Janus Greejatus"),
    n("Ysanne Isard"),
    n("Admiral Motti", True),
    n("Grand Admiral Thrawn"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Garindan", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Tempest 1"),
    n("Blizzard 4"),
    n("Sneak Attack", True),
    n("Prepared Defenses", True),
    n("Why Didn't You Tell Me", True, qty=3),
    n("Imbalance & Kintan Strider"),
    n("Close Call", True, qty=2),
    n("Outflank", True, qty=2),
    n("Control & Set For Stun", True),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("A Dark Time For The Rebellion"),
    n("A Dark Time For The Rebellion", True),
    n("Trample"),
    n("Imperial Barrier", True),
    n("Ghhhk"),
    n("Imperial Command", qty=2),
    n("Ralltiir"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Death Star Sentry", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
]
DS_ADD = []
