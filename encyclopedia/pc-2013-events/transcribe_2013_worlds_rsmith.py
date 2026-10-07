#!/usr/bin/env python3
"""2013 World Championship Day 2: RSmith Xerox Senate + Kessel."""
from __future__ import annotations

PLAYER = "RSmith"
LS_USERNAME = "Conway East"
DS_USERNAME = "Buck Faston"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 89
DS_PAGE = 90
LS_SCAN = "2013 Worlds Day 2 p89 RSmith LS.png"
DS_SCAN = "2013 Worlds Day 2 p90 RSmith DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name RSmith. Username Conway East. Email [redacted]. LIGHT. "
    "Deck title Yo dizzle. Dest as RSmith. Do not dest as Reid Smith "
    "(Reid Smith Username is 3MW0J8). "
    "Plead My Case dested Plead My Case To The Senate / Sanity And Compassion. "
    "Coruscant (EP1) dested Coruscant. "
    "Command Training & K'lor'slug dested Commando Training & K'lor'slug. "
    "Out Of Commission & Transmission Term dested Out Of Commission & Transmission Terminated. "
    "Do Or Do Not dested Do, Or Do Not. "
    "Planetery Defenses dested Planetary Defenses. "
    "Jabba's Prize written on shield 1 dested as Character in the 60. "
    "Lando ditto on line 31 has a (V) check; dittos inherit the first named line "
    "(Lando Calrissian, Scoundrel without (V)). "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name RSmith. Username Buck Faston. Email AHfan81@yah. DARK. "
    "Deck title Pittsburgh Fuckin' Pennsylvania. Dest as RSmith. Do not dest as Reid Smith "
    "(Reid Smith Username is 3MW0J8). "
    "Kessel dested Kessel. "
    "Kessel: Spice Mines - Administrator's Office dested Kessel: Spice Mines - Administrator's Office. "
    "Kessel: Spice Mines - Extraction Facility dested Kessel: Spice Mines - Extraction Facility. "
    "Kessel: Spice Mines - Prison dested Kessel: Spice Mines - Prison. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Dr. Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "The Mandalorian, Father Of Fett dested The Mandalorian. "
    "Blade Sun Fleet dested Black Sun Fleet. "
    "Spice Mine Administrator dested as written. "
    "Victory dested Victory. "
    "We'll Let Fate-a Decide Huh? dested We'll Let Fate-a Decide, Huh?. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Rebel Barrier", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("A280 Sharpshooter Rifle", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Might Of The Republic", qty=3),
    n("Senator Mon Mothma"),
    n("Mas Amedda"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Escape Pod", True),
    n("Commander Narra"),
    n("Coruscant: Senate Landing Platform"),
    n("Bail Organa, Father Of Rebellion", qty=3),
    n("Let The Wookiee Win", True, qty=3),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Menace Fades"),
    n("Alderaan Consular Ship", qty=2),
    n("Houjix"),
    n("General Solo", True),
    n("On The Edge"),
    n("Jedi Presence", qty=2),
    n("Senate Hovercam"),
    n("Senator Padme Amidala"),
    n("Imperial Atrocity", True, qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Coruscant"),
    n("Wesa Gotta Grand Army"),
    n("Commando Training & K'lor'slug"),
    n("Chewbacca, Protector", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Owen Lars & Beru Lars"),
    n("Coruscant Guard"),
    n("So This Is How Liberty Dies"),
    n("Draw Their Fire"),
    n("Bail Organa"),
    n("Grimtaash"),
    n("Senator Leia Organa"),
    n("Anger, Fear, Aggression", True),
    n("Jabba's Prize"),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Aim High", True),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Planetary Defenses", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Spice Mine Operations"),
    n("Imperial Justice", True),
    n("Cloud City: Security Tower", True),
    n("Blaster Rack", True),
    n("Lord Sidious", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Slave I, Symbol Of Fear"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Why Didn't You Tell Me?", True),
    n("Emperor Palpatine", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Lightning"),
    n("Darth Vader", True),
    n("The Mandalorian"),
    n("Black Sun Fleet"),
    n("Sidious' Lightsaber"),
    n("Sonic Bombardment", True, qty=3),
    n("Dark Maneuvers", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Blizzard 4"),
    n("Where Are You Taking This ... Thing?"),
    n("Kessel: Spice Mines - Prison"),
    n("Cold Feet", True),
    n("Imperial Barrier", qty=2),
    n("Force Field", True, qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Kessel Surveillance System"),
    n("Arica"),
    n("Sniper & Dark Strike"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Alter", True),
    n("Lightsaber Deficiency", True),
    n("Spice Mine Administrator"),
    n("Maul's Sith Infiltrator"),
    n("Force Push", True),
    n("Victory"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Protocol Failure"),
    n("Close Call", True),
    n("Garindan", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward", True),
    n("There Is No Try", True),
    n("Secret Plans"),
    n("Death Star Sentry", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("Battle Order", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
