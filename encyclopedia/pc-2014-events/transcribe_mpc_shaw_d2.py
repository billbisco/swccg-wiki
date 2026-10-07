#!/usr/bin/env python3
"""2014 Match Play Championship Day 2 Xerox: Greg Shaw.

Source: MPC-2014-Day-2-Main-Event.pdf pages 7–8 (2010 form).
Name Greg Shaw. Username blank.
Dark full 60 Set Your Course For Alderaan.
Light Same as Yesterday with In/Out from Day 1 Light.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Match Play Championship Day 2.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2014 Match Play Championship Day 2 Greg Shaw LS.png"
DS_SCAN = "2014 Match Play Championship Day 2 Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox. Light Same as Yesterday with In/Out."
LS_PUBLIC_NOTE = (
    "Same as Day 1 Light with In/Out substitutions listed on the scan."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Greg Shaw. Username blank. Same as Yesterday. "
    "IN Escape Pod (V), Houjix, Grimtaash. OUT Desperate Reach (V), "
    "Houjix & Out Of Nowhere, You've Got A Lot Of Guts Coming Here. "
    "Dest Day 1 Light minus those OUT plus those IN. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Greg Shaw. Username blank. DARK checked. "
    "Set Your Course For Alderaan dested Set Your Course For Alderaan / "
    "More Dangerous Than You Realize. Dual-title (V) empty. "
    "Death Star: Central Core (V) dested Death Star: Central Core (V). "
    "Commence Primary Ignition dested Commence Primary Ignition. "
    "TIE Sentry Ships dested TIE Sentry Ships. "
    "He Is Not Ready dested He Is Not Ready. "
    "Operational As Planned dested Operational As Planned. "
    "Darth Maul w/ Lightsaber dested Darth Maul With Lightsaber. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Abyss crossed in Additional, Death Star Sentry replacement. "
    "Unique overcounts sheet-accurate (Intensify The Forward Batteries x2, "
    "Lightsaber Deficiency (V) x2, Overwhelmed x2, Relentless Pursuit x2, "
    "Operational As Planned (V) x2, Force Pike (V) x2, Darth Sidious x3, "
    "Darth Maul With Lightsaber x2, Vigilance x2). "
    "NO_DEST Crush Them. (V) from checkbox."
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
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Heading For The Medical Frigate"),
    n("No Questions Asked", True, qty=3),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Corran Horn"),
    n("Jaina Solo"),
    n("Chewie", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Laudica", True),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Palejo Reshad"),
    n("Romas \"Lock\" Navander"),
    n("Mirax Terrik"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Obi-Wan In Radiant VII"),
    n("Tantive IV", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Rebel Barrier", qty=2),
    n("Corellian Retort", True, qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Let The Wookiee Win", True, qty=2),
    n("Sense"),
    n("Punch It!"),
    n("Home One: Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Anger, Fear, Aggression", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("Grimtaash"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Planetary Defenses", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("He Can Go About His Business"),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / More Dangerous Than You Realize"
DS_CARDS = [
    n("Set Your Course For Alderaan / More Dangerous Than You Realize"),
    n("Knowledge And Defense", True),
    n("Death Star"),
    n("Death Star: Docking Bay"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("Laser Cannon Battery"),
    n("Imperial Stockade"),
    n("Commence Primary Ignition", True),
    n("Superlaser"),
    n("Death Star: Central Core", True),
    n("Death Star: War Room", True),
    n("Nal Hutta"),
    n("Corulag"),
    n("Rendili"),
    n("Intensify The Forward Batteries", qty=2),
    n("Arica"),
    n("U-3PO"),
    n("A Million Voices Crying Out"),
    n("Your Destiny", True),
    n("Protocol Failure"),
    n("Lateral Damage"),
    n("The Phantom Menace"),
    n("Image Of The Dark Lord", True),
    n("Dreaded Imperial Starfleet", True),
    n("Tactical Doctrine"),
    n("Imperial Propaganda", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Force Push", True),
    n("Overwhelmed", qty=2),
    n("Relentless Pursuit", qty=2),
    n("Imperial Barrier"),
    n("He Is Not Ready", True),
    n("TIE Sentry Ships", True),
    n("Masterful Move"),
    n("Operational As Planned", True, qty=2),
    n("Crossfire"),
    n("Force Pike", True, qty=2),
    n("Crush Them"),
    n("Darth Sidious", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("Vigilance", qty=2),
    n("Thunderflare"),
    n("Conquest", True),
    n("Tyrant"),
    n("Victory"),
    n("Accuser"),
    n("Devastator", True),
    n("Vengeance"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("Battle Order"),
    n("Resistance"),
    n("Do They Have A Code Clearance", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = [
    n("Fanfare", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
]
