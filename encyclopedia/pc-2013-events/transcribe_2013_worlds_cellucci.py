#!/usr/bin/env python3
"""2013 World Championship Day 1: Stephen Cellucci LS typed printout + DS Xerox."""
from __future__ import annotations

PLAYER = "Stephen Cellucci"
LS_USERNAME = "Nolimit"
DS_USERNAME = "NoLimit"
USERNAME = "Nolimit"
STAGE = "Day 1"
PDF = "2013 Worlds Day 1.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2013 Worlds Day 1 p01 Stephen Cellucci LS.png"
DS_SCAN = "2013 Worlds Day 1 p02 Stephen Cellucci DS.png"
LS_NOTE = (
    "Typed numbered printout (not a handwritten Xerox form). Username Nolimit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username NoLimit. Event Day 1 Worlds. "
    "Endor ops / Imperial Outpost dested Endor Operations / Imperial Outpost. "
    "Short Range Fighters & WYB dested Short Range Fighters & Watch Your Back!. "
    "Corporal Mista dested Corporal Midge. Lieutenant Penz dested Lieutenant Renz. "
    "Sergeant Barrich dested Sergeant Barich. "
    "Form left column reprints 37–38 on lines 39–40. "
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
    n("Wokling", True),
    n("Strike Planning", True),
    n("Commando Training & K'lor'slug"),
    n("Coruscant"),
    n("Sense", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Houjix"),
    n("Luke Skywalker, Rebel Scout", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Mechanical Failure"),
    n("Seeking An Audience", True),
    n("Chewbacca, Protector", True),
    n("Senate Hovercam"),
    n("Senator Mon Mothma"),
    n("General Solo"),
    n("Might Of The Republic", qty=3),
    n("Senator Leia Organa"),
    n("Mas Amedda"),
    n("Jedi Presence"),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Coruscant: Night Club"),
    n("Redeemed Apprentice"),
    n("So This Is How Liberty Dies"),
    n("Menace Fades"),
    n("Draw Their Fire"),
    n("Grimtaash"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Rebel Barrier", qty=2),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Imperial Atrocity", qty=2),
    n("Bail Organa", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Escape Pod", True, qty=2),
    n("Let The Wookiee Win", True),
    n("Owen Lars & Beru Lars"),
    n("Republic Gunship Wing"),
    n("Alderaan Consular Ship"),
    n("Senator Padmé Amidala"),
    n("Corran Horn"),
    n("Mantellian Savrip"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Battle Plan"),
    n("Aim High"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Planetary Defenses", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Prepared Defenses"),
    n("Endor Shield", True),
    n("Establish Control", True),
    n("Scout Blaster"),
    n("Endor"),
    n("Dark Maneuvers"),
    n("Sergeant Elsek"),
    n("Sonic Bombardment", True),
    n("Aratech Corporation", True),
    n("Breached Defenses & Molator"),
    n("Imperial Academy Training", True),
    n("Imperial Stockpile", True),
    n("Perimeter Patrol"),
    n("Ominous Rumors", True),
    n("Establish Secret Base", True),
    n("Endor: Bunker"),
    n("Admiral Ozzel"),
    n("General Tagge", True),
    n("Slave I, Symbol Of Fear"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Sonic Bombardment", True),
    n("Blast Points"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Corporal Drelosyn"),
    n("Sonic Bombardment", True),
    n("Stormtrooper Garrison"),
    n("Compact Firepower", qty=2),
    n("Cold Feet", True),
    n("Why Didn't You Tell Me?", True),
    n("Imperial Barrier"),
    n("Lightsaber Deficiency", True, qty=3),
    n("Security Precautions", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin"),
    n("Blast Points"),
    n("Grand Moff Tarkin", True),
    n("Protocol Failure"),
    n("Speeder Bike", qty=3),
    n("Endor: Landing Platform"),
    n("Corporal Midge"),
    n("Sergeant Elsek"),
    n("Sergeant Barich"),
    n("Lieutenant Renz", True),
    n("Sergeant Irol", True),
    n("Grand Moff Tarkin", True),
    n("Cloud City: Security Tower", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Darth Vader With Lightsaber"),
    n("Navy Trooper Fenson"),
    n("Endor: Forest Clearing"),
    n("Endor"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Imperial Detention"),
    n("Fanfare", True),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("A Useless Gesture"),
]
