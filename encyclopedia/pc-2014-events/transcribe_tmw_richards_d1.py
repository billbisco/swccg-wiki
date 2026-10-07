#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Mike Richards (mr007agent).

Source: 2014-TMW-Day-1.pdf pages 25–26 (2013 form).
"""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "mr007agent"
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2014 Texas Mini Worlds Day 1 p26 Mike Richards LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p25 Mike Richards DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Michael Richards dested Mike Richards. Username mr007agent. LIGHT checked. "
    "Deck Name Rebel Senate. Event TMW 2014. "
    "Plead My Case To The Senate empty dested Plead My Case To The Senate / Sanity And Compassion. "
    "Jedi Prescence dested Jedi Presence. "
    "Derek 'Hobbie' Klivian dested Derek 'Hobbie' Klivian. "
    "Senator Leia Organa dested Senator Leia Organa. "
    "Unique overcounts sheet-accurate (Rebel Leadership x4, Might Of The Republic x3, "
    "Artoo-Detoo In Red 5 x2, Bail Organa, Father Of Rebellion x2, "
    "Lando Calrissian, Scoundrel x2, Chewbacca, Protector x2). "
    "(V) from the checkbox; dittos inherit the first named line except where the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Michael Richards dested Mike Richards. Username mr007agent. DARK checked. "
    "Deck Name Slavers Tanks. Event TMW 2014. "
    "Wookiee Slaving Occupation dested Wookiee Slaving Operation / Indentured To The Empire. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Guri dested Guri. "
    "Unique overcounts sheet-accurate (Sonic Bombardment x4, Armored Attack Tank x3, "
    "Tank Commander x3, Vigo x3, Boba Fett, Prepared Hunter x2). "
    "(V) from the checkbox; dittos inherit the first named line except where the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Rogue Squadron Tactics"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Mace Windu, Master Of The Order"),
    n("Rebel Leadership", True, qty=4),
    n("Imperial Atrocity", True),
    n("Owen Lars & Beru Lars"),
    n("Jedi Presence"),
    n("Admiral Ackbar", True),
    n("Derek 'Hobbie' Klivian", True),
    n("IL-19"),
    n("Houjix"),
    n("So This Is How Liberty Dies"),
    n("Inconsequential Barriers"),
    n("Bail Organa"),
    n("Luke Skywalker", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Menace Fades"),
    n("Corran Horn"),
    n("Dressel"),
    n("Projection Of A Skywalker"),
    n("Sense", qty=2),
    n("Might Of The Republic", qty=3),
    n("Home One"),
    n("General Solo", True),
    n("Senate Hovercam"),
    n("Senator Padme Amidala"),
    n("Escape Pod", True, qty=2),
    n("Coruscant"),
    n("Field Dressing"),
    n("Alderaan Consular Ship"),
    n("Chewbacca, Protector", True, qty=2),
    n("Home One: War Room"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Yoda, Master Of The Force"),
    n("Commander Narra"),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Tantive IV"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Senator Leia Organa"),
    n("First Officer Thaneespi"),
    n("Coruscant: Night Club"),
    n("Obi-Wan Kenobi", True),
    n("Senator Mon Mothma"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("Chasm"),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Den Of Thieves & Special Delivery"),
    n("Mercenary Slavers"),
    n("Baktoid Armor Workshop"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Kashyyyk"),
    n("Cloud City: Security Tower", True),
    n("Kashyyyk: Forest Maze"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Deployment Orders"),
    n("Ni Chuba Na?", True),
    n("Tarkin's Bounty", True),
    n("Open Fire"),
    n("Scum And Villainy"),
    n("Wookiee Subjugation"),
    n("Defensive Fire", True),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Close Call", True),
    n("Control & Set For Stun"),
    n("A Dark Time For The Rebellion", True),
    n("Sonic Bombardment", True, qty=2),
    n("Sonic Bombardment", qty=2),
    n("Imperial Barrier", qty=2),
    n("Cease Fire!"),
    n("Heavy Fire Zone"),
    n("AAT Laser Cannon", qty=2),
    n("Armored Attack Tank", qty=3),
    n("AAT Assault Leader", qty=2),
    n("Stinger", True),
    n("Guri"),
    n("Slave I, Symbol Of Fear"),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Jango Fett, The Assassin"),
    n("Blockade Support Ship"),
    n("Tank Commander", qty=3),
    n("OOM Command Battle Droid", qty=2),
    n("U-3PO (Yoc-Threepio)"),
    n("Jabba The Hutt", True),
    n("Vigo", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Ephant Mon"),
    n("Prince Xizor"),
    n("Garindan", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("You've Never Won A Race?"),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Restricted Access", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
