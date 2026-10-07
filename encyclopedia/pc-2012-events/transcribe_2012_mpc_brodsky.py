#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Brian Brodsky.

Source: 2012mpcday1.pdf pages 53–54 (2010 form, 12 shields).
Name Brian Brodsky dested Brian Brodsky. Username bbrodsky50.
p53 Light Finley's Filabusters. p54 Dark I said ACROSS her nose not UP IT!!.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Brian Brodsky"
USERNAME = "bbrodsky50"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 53
DS_PAGE = 54
LS_SCAN = "2012 Match Play Championship Day 1 Brian Brodsky LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Brian Brodsky DS.png"
LS_DECK_NAME = "Finley's Filabusters"
DS_DECK_NAME = '"I said ACROSS her nose not UP IT!!"'
NOTE = "Typed 2010 Xerox form."
LS_NOTE = (
    "Typed 2010 Xerox. Name Brian Brodsky. Username bbrodsky50. LIGHT checked. "
    "Deck Name Finley's Filabusters. Event MPC 2012 Date 02/11/12. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Plead My Case To The Senate/Sanity dested Plead My Case To The Senate / Sanity And Compassion. "
    "Senator Jar Jar dested Senator Jar Jar Binks True. "
    "Senator Padme Amidala dested Senator Padmé Amidala True x2. "
    "Alderaan Consular Ship dested Radiant VII True. "
    "Antillies Manuever dested Antilles Maneuver True. "
    "Obi-Wan With Lightsaber dested Obi-Wan With Lightsaber x2. "
    "Hyper Escape (Japanese edition) + HyperEscape dested Hyper Escape x2. "
    "Wedge, Red Squadron Leader dested Wedge Antilles, Red Squadron Leader. "
    "Antillies Manuever/Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements True. "
    "Unique 60. (V) from checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Brian Brodsky. Username bbrodsky50. DARK checked. "
    "Deck Name I said ACROSS her nose not UP IT!!. Event MPC 2012 Date 02/11/12. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Set Your Course For Alderaan/The Ultimate dested Set Your Course For Alderaan / "
    "The Ultimate Power In The Universe. Death Star: Docking Bay 327 (Japanese) dested "
    "Death Star: Docking Bay 327. Alderaan (Japanese) dested Alderaan. "
    "He Is Not Ready/Imperial Propaganda dested He Is Not Ready & Imperial Propaganda. "
    "Ghhhk/Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "Omni Box/It's Worse dested Ommni Box & It's Worse. "
    "Masterful Move/Endor Occupation dested Masterful Move & Endor Occupation. "
    "Hyperroute Navigation Chart dested Hyperroute Navigation Chart in Additional. "
    "Unique 60. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("Rogue Squadron Tactics", True),
    n("Wokling", True),
    n("Senator Jar Jar Binks", True),
    n("Spiral"),
    n("Senator Padmé Amidala", True, qty=2),
    n("Home One"),
    n("Rebel Leadership", True),
    n("Capital Support", qty=2),
    n("Radiant VII", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Menace Fades"),
    n("Star Destroyer!"),
    n("Biggs, Rogue Legend", True),
    n("Might Of The Republic", qty=2),
    n("Bail Organa", True, qty=2),
    n("Captain Verrack", True),
    n("Tycho Celchu", True),
    n("Antilles Maneuver", True),
    n("Luke's Lightsaber"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Hyper Escape", qty=2),
    n("Naboo"),
    n("Projection Of A Skywalker"),
    n("Tantive IV", True),
    n("Kashyyyk: Forest Depths", True),
    n("Admiral Ackbar", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Changing The Odds"),
    n("Corellian Retort", True),
    n("Senator Leia Organa", True),
    n("Imperial Atrocity", True, qty=2),
    n("Senator Mon Mothma", True),
    n("A Jedi's Resilience"),
    n("Starship Levitation", True, qty=2),
    n("Senate Hovercam"),
    n("Dressel", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Mas Amedda"),
    n("Bail Organa, Father Of Rebellion", True),
    n("So This Is How Liberty Dies", True),
    n("Bright Hope", True),
    n("Corran Horn"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Mon Calamari Star Cruiser", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Death Star"),
    n("Prepared Defenses", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile", True),
    n("Laser Cannon Battery"),
    n("Kuat Drive Yards", True),
    n("Conquest", True),
    n("Intensify The Forward Batteries", qty=2),
    n("Control", qty=2),
    n("Stop Motion", True),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Tarkin Doctrine", True),
    n("U-3PO"),
    n("TIE Sentry Ships", True, qty=2),
    n("Operational As Planned", True, qty=2),
    n("Rendili"),
    n("They've Shut Down The Main Reactor", qty=2),
    n("Lightsaber Deficiency", True),
    n("Devastator", True),
    n("Imperial Barrier"),
    n("Vengeance"),
    n("Darth Sidious"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Kiffex"),
    n("Victory"),
    n("Death Star: War Room", True),
    n("Something Special Planned For Them", True),
    n("Judicator"),
    n("Ommni Box & It's Worse"),
    n("Stalker", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Imperial Propaganda", True),
    n("Moff Tarkin, Death Star Commandant", True),
    n("Nal Hutta"),
    n("Accuser", True),
    n("Masterful Move & Endor Occupation"),
    n("Death Star: Central Core", True),
    n("Lord Sidious", True, qty=2),
    n("Commence Primary Ignition", True),
    n("Cold Feet", True),
    n("The Phantom Menace"),
    n("A Dark Time For The Rebellion", True),
    n("Grand Admiral Thrawn"),
    n("Dreaded Imperial Starfleet", True),
    n("Superlaser"),
    n("Visage"),
    n("Presence Of The Force"),
    n("Force Push", True),
    n("Tyrant"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("There Is No Try"),
    n("Resistance", True),
    n("Secret Plans", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("Hyperroute Navigation Chart"),
]
