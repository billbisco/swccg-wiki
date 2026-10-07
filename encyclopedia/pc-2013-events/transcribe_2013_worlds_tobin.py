#!/usr/bin/env python3
"""2013 World Championship Day 2: Nicholas Tobin Xerox Senate + Contract Killers."""
from __future__ import annotations

PLAYER = "Nicholas Tobin"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 96
DS_PAGE = 95
LS_SCAN = "2013 Worlds Day 2 p96 Nicholas Tobin LS.png"
DS_SCAN = "2013 Worlds Day 2 p95 Nicholas Tobin DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name Nicholas Tobin. Username blank. LIGHT. Deck title Rebel Senate. "
    "Dest as Nicholas Tobin. Do not rewrite 2014 Worlds Tobin leftovers. "
    "Plead My Case dested Plead My Case To The Senate / Sanity And Compassion. "
    "Sai'torr Kai Fas dested Sai'torr Kal Fas. "
    "Bail Organa, Father Of The Rebellion dested Bail Organa, Father Of Rebellion. "
    "NOOOOOOOOOOOOO! dested NOOOOOOOOOOOO!. "
    "Coruscant (Cor) dested Coruscant. "
    "Gold Leader In Gold 1 dested Gold Leader In Gold 1. "
    "Booster In Pulsar Skate dested Booster In Pulsar Skate. "
    "Armed And Dangerous & Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "Sorry About The Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Out Of Commission & Transmission Terminate dested "
    "Out Of Commission & Transmission Terminated. "
    "Heading For The Medical Frigate dested Heading For The Medical Frigate. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name Nicholas Tobin. Username blank. DARK. Deck title Assassin!. "
    "Dest as Nicholas Tobin. Do not rewrite 2014 Worlds Tobin leftovers. "
    "Contract Killers/Feared Throughout The Galaxy dested "
    "Contract Killers / Feared Throughout The Galaxy. "
    "Coruscant (SE) dested Coruscant. "
    "Gift Of The Mester dested Gift Of The Master. "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Luuke dested Luuke. "
    "I Find You Lack Of Faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Sith Fury & End This Destructive Conflict dested "
    "Sith Fury & End This Destructive Conflict. "
    "Weapon Levitation & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Imbalance & Kintan Strider dested Imbalance & Kintan Strider. "
    "Ghhhk & Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "(V) from the checkbox; dittos inherit the first named line."
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
    n("Strike Planning"),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Bail Organa"),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Senator Mon Mothma"),
    n("Senator Leia Organa"),
    n("Senator Padme Amidala"),
    n("Mas Amedda"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Han With Heavy Blaster Pistol"),
    n("Chewbacca, Protector"),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda, Great Warrior"),
    n("Luke's Lightsaber"),
    n("Luke's Bionic Hand"),
    n("Landing Claw"),
    n("Alderaan Consular Ship"),
    n("Gold Leader In Gold 1", True),
    n("Booster In Pulsar Skate"),
    n("Senate Hovercam"),
    n("Seeking An Audience", True),
    n("So This Is How Liberty Dies"),
    n("Menace Fades"),
    n("Imperial Atrocity", True, qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Blaster Deflection", qty=2),
    n("Jedi Presence"),
    n("Hear Me Baby, Hold Together", True),
    n("Might Of The Republic", qty=2),
    n("Control & Tunnel Vision"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Jedi Levitation", True),
    n("Swing-And-A-Miss"),
    n("Clash Of Sabers"),
    n("Dark Approach", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("NOOOOOOOOOOOO!"),
    n("Let The Wookiee Win", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Coruscant"),
    n("Coruscant: Nightclub"),
    n("Naboo: Boss Nass' Chambers"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Coruscant"),
    n("Coruscant: Sub City Lair"),
    n("On The Hunt"),
    n("Prepared Defenses"),
    n("Jabba's Haven"),
    n("Guild Of Assassins"),
    n("Gift Of The Master"),
    n("Galen Marek, Starkiller", qty=2),
    n("IG-88 With Riot Gun"),
    n("Arica", True, qty=2),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Ket Maliss, Shadow Killer"),
    n("Jango Fett, The Assassin"),
    n("Guri"),
    n("Probot"),
    n("J'Quille", True),
    n("Luuke"),
    n("P-59"),
    n("Aurra Sing's Blaster Rifle"),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Trophy Of A Kill", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Dengar In Punishing One"),
    n("Protocol Failure"),
    n("Death Mark & Hutt Bounty"),
    n("Blaster Rack", True),
    n("Disarmed"),
    n("Lightsaber Deficiency", True),
    n("Abyssin Ornament", True, qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("A Dark Time For The Rebellion", True),
    n("One Beautiful Thing", qty=2),
    n("Levitation Attack", True),
    n("Sith Fury & End This Destructive Conflict"),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Barrier"),
    n("Nevar Yalnal"),
    n("Force Field", True),
    n("Imbalance & Kintan Strider"),
    n("You Are Beaten"),
    n("Weapon Levitation & The Empire's Back"),
    n("Nal Hutta"),
    n("Coruscant: Casino"),
    n("Coruscant: Palpatine's Quarters"),
    n("Cloud City: Security Tower", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Imperial Detention"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Resistance"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
