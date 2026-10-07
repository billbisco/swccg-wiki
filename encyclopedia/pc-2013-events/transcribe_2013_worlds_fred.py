#!/usr/bin/env python3
"""2013 World Championship Day 2: Brian Fred informal overlay LS+DS."""
from __future__ import annotations

PLAYER = "Brian Fred"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 33
DS_PAGE = 32
LS_SCAN = "2013 Worlds Day 2 p33 Brian Fred LS.png"
DS_SCAN = "2013 Worlds Day 2 p32 Brian Fred DS.png"
LS_NOTE = (
    "Informal handwritten overlay, not a 2010 Xerox Print Form. "
    "Name B Fred dested Brian Fred. Username blank. "
    "WYS/Duh! dested Watch Your Step / This Place Can Be A Little Rough. "
    "Pulsar Skate dested Pulsar Skate. Artoo in red 5 dested Artoo-Detoo In Red 5. "
    "BoShek's Mod Light Freighter dested Boshek's Modified Light Freighter. "
    "Phylo dested Phylo Gandish. Palace raider dested Palace Raider. "
    "BoShek Brash Smuggler dested BoShek, Brash Smuggler. "
    "Mos Eisley DB dested Tatooine: Mos Eisley. Spaceport DB dested Spaceport Docking Bay. "
    "Cantina dested Tatooine: Cantina. Tat DB dested Tatooine: Docking Bay 94. "
    "Tatooine ep1 dested Tatooine (Coruscant). "
    "Control/Tunnel dested Control & Tunnel Vision. "
    "All Wings/Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Nar Shaddaa/Out of Somewhere dested Nar Shaddaa Wind Chimes & Out Of Somewhere. "
    "Out of Commission/TT struck omitted. "
    "Ins/Aim High dested Insurrection. "
    "Lando Cal Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Houjix/Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Jabba's fire dested Jabba's Prize. "
    "15 defensive-shield slots on this overlay."
)
DS_NOTE = (
    "Informal handwritten overlay, not a 2010 Xerox Print Form. "
    "Name B Fred dested Brian Fred. Username blank. Endor ops. "
    "Endor ops dested Endor Operations / Imperial Outpost. "
    "DS-61-2 dested DS-61-2. "
    "High Speed Tactics struck omitted. "
    "Right-column Corporal Drelosyn (V) struck omitted. "
    "Baron Fel and Saber 1 kept (x marks read as include). "
    "Sneak Attack margin x3 dested qty 3. "
    "Juno Eclipse Black Leader dested Juno Eclipse, Black Leader. "
    "Ghhhk/These rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Endor Dark Forest dested Endor: Dark Forest. "
    "Vader's Shuttle dested Vader's Personal Shuttle. "
    "3 Short range/WYB dested Short Range Fighters & Watch Your Back!. "
    "We'll let fate dested We'll Let Fate-a Decide, Huh?. "
    "YCHFF dested You Cannot Hide Forever. "
    "15 defensive-shield slots on this overlay."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Pulsar Skate"),
    n("Artoo-Detoo In Red 5"),
    n("Outrider"),
    n("Boshek's Modified Light Freighter", True, qty=5),
    n("Patrol Craft"),
    n("Melas", True, qty=2),
    n("Phylo Gandish"),
    n("Talon Karrde"),
    n("Palace Raider", qty=6),
    n("BoShek, Brash Smuggler"),
    n("Wedge Antilles", True),
    n("Dash Rendar"),
    n("Mirax Terrik"),
    n("Luke Skywalker", True),
    n("Tatooine: Mos Eisley"),
    n("Spaceport Docking Bay"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine (Coruscant)", True),
    n("Corellia", True),
    n("Fallen Portal", qty=2),
    n("I'll Take The Leader", qty=2),
    n("It's A Hit!"),
    n("It Could Be Worse"),
    n("We're Doomed"),
    n("Control & Tunnel Vision", qty=2),
    n("Imperial Atrocity", True),
    n("Rebel Barrier"),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Menace Fades"),
    n("Tatooine Celebration", qty=2),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("Moving To Attack Position"),
    n("Insurrection"),
    n("Heading For The Medical Frigate"),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("Millennium Falcon"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Desperate Reach", True),
    n("Han Solo, Courageous Smuggler"),
    n("Houjix & Out Of Nowhere"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Ship?"),
    n("He Can Go About His Business", True),
    n("The Professor"),
    n("Yavin Sentry"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Planetary Defenses", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Jabba's Prize", True),
]

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Speeder Bike", qty=5),
    n("DS-61-2"),
    n("Navy Trooper Fenson"),
    n("Darth Vader", True),
    n("Baron Soontir Fel"),
    n("Juno Eclipse, Black Leader"),
    n("Admiral Ozzel"),
    n("Major Turr Phennir"),
    n("General Tagge", True),
    n("Sergeant Irol", True, qty=2),
    n("Sergeant Barich", qty=2),
    n("Corporal Drelosyn"),
    n("Sergeant Elsek", qty=2),
    n("Garindan", True, qty=3),
    n("Lightsaber Deficiency", True, qty=2),
    n("Sneak Attack", True, qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Prepared Defenses"),
    n("Force Push", True),
    n("Aratech Corporation", True),
    n("Ni Chuba Na??", True),
    n("Establish Control", True),
    n("Combat Response", True),
    n("Establish Secret Base", True),
    n("Endor Shield", True),
    n("Ominous Rumors", True),
    n("Protocol Failure"),
    n("Imperial Barrier", qty=2),
    n("Perimeter Patrol"),
    n("Imperial Domination", True),
    n("Fighters Coming In"),
    n("Endor: Bunker"),
    n("Endor: Forest Clearing"),
    n("Endor: Dark Forest"),
    n("Fondor"),
    n("Endor: Landing Platform"),
    n("Endor"),
    n("Black 1"),
    n("Black 2", True),
    n("Saber 1"),
    n("Saber 2"),
    n("Vader's Personal Shuttle", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Imperial Detention"),
]
DS_ADD = []
