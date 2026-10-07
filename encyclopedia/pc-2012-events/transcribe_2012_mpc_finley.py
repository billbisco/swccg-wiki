#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chuck Finley.

Source: 2012mpcday1.pdf pages 69–70 (2010 form, 12 shields).
Name Chuck Finley dested Chuck Finley as written (analog empty).
Username blank. Pack player-stubs/Chuck_Finley.wiki.
p69 Light Finley's Filibusters. p70 Dark Chuck Finley *IS* the Kwisatz Haderach.
"""
from __future__ import annotations

PLAYER = "Chuck Finley"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 69
DS_PAGE = 70
LS_SCAN = "2012 Match Play Championship Day 1 Chuck Finley LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chuck Finley DS.png"
LS_DECK_NAME = "Finley's Filibusters"
DS_DECK_NAME = "Chuck Finley *IS* the Kwisatz Haderach"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chuck Finley dested Chuck Finley. "
    "Username blank. LIGHT checked. Deck Name Finley's Filibusters. "
    "Event 2012 MPC Date 02/11/12. Email [redacted]. "
    "Analog encyclopedia / player-stubs / generate empty; dest as written. "
    "Plead My Case / Sanity & Compassion dested Plead My Case To The Senate / "
    "Sanity And Compassion empty. "
    "Coruscant: Senate dested Coruscant: Galactic Senate. "
    "Alderaan Consular Ship dested Radiant VII True. "
    "Antilles Maneuver / Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements True. "
    "Corellian Retro dested Corellian Retort True. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Senator Padme Amidala dested Senator Padmé Amidala True x2. "
    "Unique 60. Shields 12. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chuck Finley dested Chuck Finley. "
    "Username blank. DARK checked. Deck Name Chuck Finley *IS* the Kwisatz Haderach. "
    "Event 2012 MPC Date 02/11/12. Email [redacted]. "
    "Kessel dested Kessel / Spice Mines Of Kessel empty. "
    "Kessel: Admin. Office dested Kessel: Spice Mines - Administrator's Office True. "
    "Kessel: Extraction Facility dested Kessel: Spice Mines - Extraction Facility True. "
    "Kessel: Prison dested Kessel: Spice Mines - Prison True. "
    "Baktold Armor Workshop dested Baktoid Armor Workshop True. "
    "I'm Sorry (That you suck) dested I'm Sorry True. "
    "Furry Fury dested Sith Fury. "
    "Ghhhk / Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Ommni Box / It's Worse dested Ommni Box & It's Worse. "
    "Masterful Move / Endor Occ dested Masterful Move & Endor Occupation. "
    "Dark Maneuvers / Tallon Roll dested Dark Maneuvers & Tallon Roll. "
    "Spice Mine Administrator dested as written True. "
    "Unique 60. Shields 12. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Rogue Squadron Tactics", True),
    n("Strike Planning"),
    n("Wokling", True),
    n("Spiral"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Capital Support", qty=2),
    n("Bail Organa, Father Of Rebellion", True),
    n("Senator Jar Jar Binks", True),
    n("Imperial Atrocity", True, qty=2),
    n("Star Destroyer!"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Dressel", True),
    n("Tantive IV", True),
    n("Hyper Escape", qty=2),
    n("Lando Calrissian, Scoundrel", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Luke's Lightsaber"),
    n("Home One"),
    n("Projection Of A Skywalker"),
    n("Starship Levitation", True, qty=2),
    n("Menace Fades"),
    n("Might Of The Republic", qty=2),
    n("So This Is How Liberty Dies", True),
    n("It Could Be Worse"),
    n("Admiral Ackbar", True),
    n("Kashyyyk: Forest Depths", True),
    n("A Jedi's Resilience"),
    n("Radiant VII", True),
    n("Corran Horn"),
    n("Haven"),
    n("Senator Mon Mothma", True),
    n("Senate Hovercam"),
    n("Bail Organa", True, qty=2),
    n("Senator Padmé Amidala", True, qty=2),
    n("Bright Hope", True),
    n("Biggs, Rogue Legend", True),
    n("Mon Calamari Star Cruiser", True),
    n("Captain Verrack", True),
    n("Corellian Retort", True),
    n("Mas Amedda"),
    n("Senator Leia Organa", True),
    n("Tycho Celchu", True),
    n("Rebel Leadership", True),
    n("Changing The Odds"),
    n("Wedge Antilles, Red Squadron Leader"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Another Pathetic Lifeform", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Kessel / Spice Mines Of Kessel"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Kessel / Spice Mines Of Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office", True),
    n("Baktoid Armor Workshop", True),
    n("I'll Take Them Myself", True),
    n("I'm Sorry", True),
    n("Deployment Orders", True),
    n("Lightsaber Deficiency", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Ommni Box & It's Worse"),
    n("Justifier", True, qty=2),
    n("Tank Commander", qty=2),
    n("Kessel Surveillance System", True),
    n("Emperor Palpatine"),
    n("Armored Attack Tank", qty=4),
    n("Zuckuss In Mist Hunter"),
    n("There'll Be Hell To Pay", qty=3),
    n("Stop Motion", True),
    n("Dark Maneuvers & Tallon Roll"),
    n("Masterful Move & Endor Occupation"),
    n("Kessel: Spice Mines - Extraction Facility", True),
    n("We're In Attack Position Now"),
    n("OS-72-1 In Obsidian 1"),
    n("Darth Maul With Lightsaber"),
    n("Sith Fury"),
    n("U-3PO"),
    n("Storm Clouds", True),
    n("All Power To Weapons", qty=2),
    n("Imperial Command", qty=2),
    n("Spice Mine Operations", True),
    n("Darth Sidious"),
    n("Cold Feet", True),
    n("OOM Command Battle Droid", True, qty=2),
    n("Force Push", True),
    n("Kessel: Spice Mines - Prison", True),
    n("Cease Fire!"),
    n("Lateral Damage"),
    n("Admiral Piett", True),
    n("Boba Fett In Slave I", True),
    n("Imperial Barrier", qty=2),
    n("Clouds"),
    n("Special Delivery", True),
    n("Spice Mine Administrator", True),
    n("Darth Vader With Lightsaber"),
    n("Floating Refinery", True),
    n("Limited Resources"),
    n("Grand Admiral Thrawn"),
    n("OS-72-2 In Obsidian 2"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
