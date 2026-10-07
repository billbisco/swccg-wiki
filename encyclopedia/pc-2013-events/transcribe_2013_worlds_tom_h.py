#!/usr/bin/env python3
"""2013 World Championship Day 2: Tom H Xerox WYS + ROPS (name as written)."""
from __future__ import annotations

PLAYER = "Tom H"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 46
DS_PAGE = 47
LS_SCAN = "2013 Worlds Day 2 p46 Tom H LS.png"
DS_SCAN = "2013 Worlds Day 2 p47 Tom H DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Tom H. Username blank. Event blank. "
    "LIGHT/DARK boxes empty; dest Light from Watch Your Step. "
    "Do not dest as Tom Haid (Haid is Profit / Wookiee Slaving on p40/p41). "
    "LSFK dested Luke Skywalker, Jedi Knight. "
    "Leia BP dested Leia With Blaster Rifle. "
    "Insurrection combo dested Insurrection & Aim High. "
    "All Wings combo dested All Wings Report In & Darklighter Spin. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements. "
    "See Threepio Ambassador dested See-Threepio. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "NDA dested No Questions Asked. "
    "Master Terric dested Mirax Terrik. "
    "Ronay with a Wanderer dested Romas 'Lock' Navander. "
    "Leia RD dested Leia, Rebel Princess. "
    "AFH dested A Few Maneuvers. "
    "IFTMF dested Heading For The Medical Frigate. "
    "Lando reprint dested Lando Calrissian. "
    "Spaceport Speeders Guild dested Spaceport Scoundrels Guild. "
    "Rescue About Anywhere dested I'm Here To Rescue You. "
    "Additional LKALOH moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Yoda, Great Warrior / Lando Calrissian. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Tom H. Username blank. Event blank. "
    "LIGHT/DARK boxes empty; dest Dark from Ralltiir Operations. "
    "ROPS dested Ralltiir Operations / In The Hands Of The Empire. "
    "Executor Shield dested Executor: Meditation Chamber. "
    "Hunt Down / I Have You Now dested I Have You Now. "
    "Clone Call dested Close Call. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "DVDL of TS dested Darth Vader, Dark Lord Of The Sith. "
    "Saber dested Saber 1. "
    "Emperor's Command dested Emperor's Power. "
    "Carrier dested Imperial-Class Star Destroyer. "
    "I Am A Jedi dested Join Me!. "
    "Out Flight dested Out Of Commission. "
    "Vader With Commander's Armor dested Darth Vader With Lightsaber. "
    "Ralltiir Spaceport Financial District dested Ralltiir: Spaceport Financial District. "
    "IHYN dested I Have You Now. "
    "We'll Let Fate Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Leave Them To Me / He's The Greatest dested Leave Them To Me. "
    "All Wrapped Up / Something dested All Wrapped Up. "
    "Additional There Is No Try / Battle Order moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Devastator / Imperial Domination. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Leia With Blaster Rifle"),
    n("Punch It!"),
    n("Insurrection & Aim High"),
    n("It's A Trap!"),
    n("No Questions Asked"),
    n("All Wings Report In & Darklighter Spin"),
    n("Corellian Retort", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Strikeforce", True),
    n("See-Threepio", True),
    n("Spaceport Street"),
    n("Corellian Engineer", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Dash Rendar", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Leia's Blaster Rifle"),
    n("Sense"),
    n("No Questions Asked", True),
    n("Lady Luck"),
    n("All Wings Report In & Darklighter Spin"),
    n("Imperial Atrocity", True),
    n("Mirax Terrik"),
    n("No Questions Asked", True),
    n("Corran Horn"),
    n("Romas 'Lock' Navander"),
    n("Evacuation Control", True),
    n("Leia, Rebel Princess"),
    n("Home One: Docking Bay"),
    n("Rebel Barrier"),
    n("Houjix & Out Of Nowhere"),
    n("A Few Maneuvers"),
    n("Millennium Falcon", True),
    n("Mace Windu, Master Of The Order"),
    n("Heading For The Medical Frigate"),
    n("Corellian Slip", True),
    n("Yoda, Great Warrior"),
    n("Lando Calrissian", True),
    n("Passport Search"),
    n("Captain Han Solo"),
    n("Corellia", True),
    n("Spaceport City"),
    n("Corellian Engineering Corporation", True),
    n("Wokling", True),
    n("Captured", True),
    n("Heading For The Medical Frigate", True),
    n("Rebel Barrier"),
    n("Palejo Reshad"),
    n("Spaceport Docking Bay"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Padme Naberrie", True),
    n("Spaceport Scoundrels Guild"),
    n("Chewie", True),
    n("General Crix Madine"),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Sergeant Bruckman"),
]
LS_SHIELDS = [
    n("I'm Here To Rescue You"),
    n("Battle Plan"),
    n("Chasm", True),
    n("The Professor", True),
    n("Jabba's Prize", True),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Do, Or Do Not", True),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = [
    n("Yoda, Great Warrior", True),
    n("Obi-Wan Kenobi", True),
]


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Executor: Meditation Chamber", True),
    n("Insignificant Rebellion", True),
    n("I Have You Now", True),
    n("Battle", True),
    n("Prepared Defenses", True),
    n("Imperial Domination", True),
    n("Arica"),
    n("Close Call", True),
    n("Victory"),
    n("The Emperor's Reach"),
    n("A Dark Time For The Rebellion", True),
    n("Something Special Planned For Them", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("He Hasn't Come Back Yet"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Lady Luck"),
    n("Blizzard 1", True),
    n("Force Pike"),
    n("Saber 1"),
    n("Control & Set For Stun"),
    n("Grand Moff Tarkin", True),
    n("Blizzard 4", True),
    n("Blizzard 2"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Tyrant"),
    n("Emperor's Power", True),
    n("Admiral Piett"),
    n("Weapon Levitation"),
    n("Imperial Command"),
    n("Imperial-Class Star Destroyer"),
    n("Colonel Davod Jon"),
    n("Join Me!", True),
    n("Emperor Palpatine"),
    n("Grand Admiral Thrawn", True),
    n("Close Call", True),
    n("Come Here You Big Coward", True),
    n("Devastator", True),
    n("Imperial Domination", True),
    n("Emperor Palpatine"),
    n("Why Didn't You Tell Me?", True),
    n("Empire's New Order", True),
    n("Frozen Assets", True),
    n("Out Of Commission"),
    n("Darth Vader With Lightsaber"),
    n("Spaceport Prefect's Office", True),
    n("A Dark Time For The Rebellion"),
    n("Spaceport Docking Bay"),
    n("Excellent", True),
    n("Operational As Planned", True),
    n("Ralltiir: Spaceport Financial District"),
    n("Cold Feet"),
    n("Spaceport Prefect"),
    n("Protocol Failure"),
    n("Imbalance & Kintan Strider", True),
    n("General Veers"),
    n("Imperial Barrier", True),
    n("I Have You Now", True),
    n("Lateral Damage"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Imperial Detention"),
    n("Resistance", True),
    n("A Useless Gesture"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Leave Them To Me", True),
    n("Firepower", True),
    n("Secret Plans", True),
    n("All Wrapped Up", True),
    n("There Is No Try", True),
    n("Battle Order", True),
]
DS_ADD = [
    n("Abyss"),
]
