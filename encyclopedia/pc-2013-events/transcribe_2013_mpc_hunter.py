#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Brian Hunter Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Brian Hunter"
USERNAME = "Hunter"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 45
DS_PAGE = 46
LS_SCAN = "2013 Match Play Championship p45 Brian Hunter LS.png"
DS_SCAN = "2013 Match Play Championship p46 Brian Hunter DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username Hunter. Event The Match Play Championship, 26 January 2013. "
    "Deck title This Deck Was Good Ten Years Ago. Light. "
    "Plead My Case To The Senate / Sanity And Compassion. "
    "Threepio w/ His Parts Showing dested Threepio With His Parts Showing. "
    "Han, Chewie + the Falcon dested Han, Chewie, And The Falcon. "
    "Luke / Qui-Gon / Obi-Wan w/ Lightsaber dested the Enhanced Premiere printings. "
    "SATM + B.P. dested Sorry About The Mess & Blaster Proficiency. "
    "Lando's Luxury Yacht dested Lady Luck. AFA dested Anger, Fear, Aggression. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username Hunter. Event The Match Play Championship, 26 January 2013. "
    "Deck title This Deck Was Good Two Years Ago. Dark. "
    "A Stunning Move / A Valuable Hostage. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Short Range Fighters + W.Y.B. dested Short Range Fighters & Watch Your Back. "
    "He Is Not Ready + Imp. Propaganda dested He Is Not Ready. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Dr. Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Ghhhk + Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "K+D dested Knowledge And Defense. YCHF dested You Cannot Hide Forever. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Ascertaining The Truth"),
    n("The Gravest Of Circumstances"),
    n("Plea To The Court"),
    n("Senate Hovercam"),
    n("Imperial Atrocity", True),
    n("Queen Amidala, Ruler Of Naboo", qty=2),
    n("Senator Palpatine", qty=2),
    n("Horox Ryyder"),
    n("Liana Merian"),
    n("Yarua"),
    n("Mas Amedda"),
    n("Senator Mon Mothma", qty=2),
    n("Were You Looking For Me?"),
    n("Threepio With His Parts Showing"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Life Debt"),
    n("Draw Their Fire"),
    n("Nar Shaddaa"),
    n("Naboo: Theed Palace Generator Core"),
    n("Corran Horn"),
    n("Princess Leia", True),
    n("Scrambled Transmission", True),
    n("Luke With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Horox Ryyder"),
    n("Might Of The Republic", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Civil Disorder"),
    n("Senator Palpatine"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Jedi Levitation", True),
    n("Sense"),
    n("Obi-Wan With Lightsaber"),
    n("Inconsequential Barriers"),
    n("Princess Leia", True),
    n("Leia's Blaster Rifle"),
    n("Legendary Starfighter"),
    n("I Will Not Defer"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience"),
    n("Jedi Levitation", True),
    n("Sense"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Chasm", True),
    n("Battle Plan"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Insidious Prisoner"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen Marek, Starkiller", qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blockade Support Ship"),
    n("Dengar With Blaster Carbine", True),
    n("Battle Droid Squad", qty=2),
    n("IG-100 MagnaGuard"),
    n("The Phantom Menace"),
    n("No Escape"),
    n("Dr. Evazan & Ponda Baba"),
    n("Sith Fury", True),
    n("Sonic Bombardment", True, qty=2),
    n("A Sith's Weapon"),
    n("Force Field", True),
    n("Something Special Planned For Them", True),
    n("Imperial Barrier"),
    n("Control & Set For Stun"),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Cloud City: Security Tower", True),
    n("The Phantom Menace"),
    n("Short Range Fighters & Watch Your Back"),
    n("Force Field", True),
    n("He Is Not Ready"),
    n("Sniper & Dark Strike"),
    n("Dr. Evazan & Ponda Baba"),
    n("A Dark Time For The Rebellion", True),
    n("IG-100 MagnaGuard"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Maul Strikes"),
    n("Darth Maul, Young Apprentice"),
    n("Boba Fett, Prepared Hunter"),
    n("Weapon Levitation"),
    n("Sonic Bombardment", True),
    n("Sith Fury", True),
    n("Imperial Justice", True),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Imperial Barrier"),
    n("Nal Hutta"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Abyss", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
