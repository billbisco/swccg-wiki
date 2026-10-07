#!/usr/bin/env python3
"""2014 Match Play Championship Day 2 Xerox: Matthew Harrison-Trainor.

Source: MPC-2014-Day-2-Main-Event.pdf pages 3–4 (2013 form, 15 shields).
Name MHT dested Matthew Harrison-Trainor. Username blank.
Dark full 60 Ralltiir Operations. Light full 60 Watch Your Step.
"""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Match Play Championship Day 2.pdf"
LS_PAGE = 4
DS_PAGE = 3
LS_SCAN = "2014 Match Play Championship Day 2 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2014 Match Play Championship Day 2 Matthew Harrison-Trainor DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "ROPS"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name MHT dested Matthew Harrison-Trainor. Username blank. "
    "LIGHT checked. WYS dested Watch Your Step (V) / This Place Can Be A Little Rough (V). "
    "Romas Lock Navander dested Romas \"Lock\" Navander. Palejo Reshad dested Palejo Reshad. "
    "Maris Brood, Fallen Jedi crossed with no replacement skipped. "
    "Unique overcounts sheet-accurate (Wedge Antilles, Red Squadron Leader x2, "
    "Imperial Atrocity (V) x2, Let The Wookiee Win (V) x2, Antilles Maneuver (V) x2, "
    "Dash Rendar (V) x2, No Questions Asked (V) x3, Luke Skywalker, Jedi Knight x2, "
    "All Wings Report In & Darklighter Spin x2, Rebel Barrier x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name MHT dested Matthew Harrison-Trainor. Username blank. "
    "DARK checked. ROPS dested Ralltiir Operations / In The Hands Of The Empire. Dual-title "
    "(V) empty. Prep Def dested Prepared Defenses (V). Insig Rebellion dested Insurrection (V). "
    "Ender Shield dested Endor Shield (V). OVDLOTS dested Ominous Rumors & Dark Lord Of The Sith. "
    "OV BOTS dested I Have You Now (V). EPP Kir Kanos dested Kir Kanos. "
    "C Stesat dested Coruscant: Galactic Senate. C Director's Office dested Coruscant: Imperial City. "
    "C Docking Bay dested Coruscant: Docking Bay. Cargo Heart dested Cargo Ferry. "
    "Control + SFS dested Control & Set For Stun. WDYTM dested We're In Attack Position Now (V). "
    "ADTFR dested A Dark Time For The Rebellion (V). Temp Command dested Imperial Command. "
    "Imbalance Combo dested Imbalance & Kintan Strider. HHCBY dested He Hasn't Come Back Yet. "
    "Temp Justice dested Imperial Justice (V). Temp Doom dested Walker Garrison (V). "
    "GMT dested Grand Moff Tarkin (V). TIE-1A dested TIE Advanced x1. Grandin dested The Emperor (V). "
    "Shield Greedle dested We'll Let Fate-a Decide, Huh?. Shield See Them dested Leave Them To Me. "
    "Unique overcounts sheet-accurate (Emperor Palpatine x2, We're In Attack Position Now (V) x2, "
    "A Dark Time For The Rebellion (V) x2, Imperial Command x2, Stop Motion (V) x2, "
    "Walker Garrison (V) x2, Blizzard 4 x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Houjix & Out Of Nowhere"),
    n("Desperate Reach", True),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Sergeant Bruckman"),
    n("Mirax Terrik"),
    n("Corran Horn"),
    n("Romas \"Lock\" Navander"),
    n("Palejo Reshad"),
    n("Padme Naberrie", True),
    n("Leia, Rebel Princess", qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("Leia's Blaster Rifle"),
    n("Spaceport Street"),
    n("Imperial Atrocity", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Punch It"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Antilles Maneuver", True, qty=2),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Spaceport Docking Bay"),
    n("Spaceport City"),
    n("Spaceport Scoundrels Guild"),
    n("Home One: Docking Bay"),
    n("Corellia", True),
    n("Captain Han Solo"),
    n("Chewie", True),
    n("Millennium Falcon", True),
    n("Laudica", True),
    n("General Crix Madine"),
    n("No Questions Asked", True, qty=3),
    n("Mace Windu, Master Of The Order"),
    n("Yoda, Great Warrior"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Corellian Retort", True),
    n("Corellian Slip", True),
    n("Rebel Barrier", qty=2),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII"),
    n("Lady Luck"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Planetary Defenses", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Jabba's Prize", True),
    n("Your Ship"),
]
LS_ADD = []


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Prepared Defenses", True),
    n("Insurrection", True),
    n("Kuat Drive Yards", True),
    n("Endor Shield", True),
    n("Emperor Palpatine", qty=2),
    n("Ominous Rumors & Dark Lord Of The Sith"),
    n("I Have You Now", True),
    n("Admiral Motti", True),
    n("Admiral Ozzel"),
    n("General Veers", True),
    n("Kir Kanos"),
    n("Coruscant: Galactic Senate"),
    n("Ralltiir: Finance District"),
    n("Kashyyyk"),
    n("Coruscant: Imperial City"),
    n("Coruscant: Docking Bay"),
    n("Endor"),
    n("Lambda-Class Shuttle"),
    n("Cargo Ferry"),
    n("Devastator", True),
    n("Victory"),
    n("Blizzard 4", qty=2),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Control & Set For Stun"),
    n("Outflank", True),
    n("Come Here You Big Coward", True),
    n("We're In Attack Position Now", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Lightsaber Deficiency", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Command", qty=2),
    n("Imbalance & Kintan Strider"),
    n("Trample"),
    n("Close Call", True),
    n("Cold Feet", True),
    n("Stop Motion", True, qty=2),
    n("He Hasn't Come Back Yet"),
    n("Imperial Justice", True),
    n("Walker Garrison", True, qty=2),
    n("Grand Moff Tarkin", True),
    n("Mara Jade, The Emperor's Hand"),
    n("Arica"),
    n("Colonel Davod Jon"),
    n("Lt. Commander Arden Lynn"),
    n("TIE Advanced x1"),
    n("Grand Admiral Thrawn"),
    n("Janus Greejatus"),
    n("The Emperor", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("There Is No Try"),
    n("Abyss"),
    n("Resistance"),
    n("Leave Them To Me"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Do They Have A Code Clearance?", True),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
