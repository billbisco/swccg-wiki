#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Mike Tomashewski Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Mike Tomashewski"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 99
DS_PAGE = 100
LS_SCAN = "2013 Match Play Championship p99 Mike Tomashewski LS.png"
DS_SCAN = "2013 Match Play Championship p100 Mike Tomashewski DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Mike Tomashewski. Light. Deck title MHT is my Hero. "
    "Y4 Throne Room dested Yavin 4: Massassi Throne Room. Prepared Defenses crossed; HFTMF dested "
    "Heading For The Medical Frigate. N Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "C Jedi Council Chamber dested Coruscant: Jedi Council Chamber. Y4 War Room dested "
    "Yavin 4: Massassi War Room. Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "R2 in Red 5 dested Artoo-Detoo In Red 5. LSJK dested Luke Skywalker, Jedi Knight. "
    "Luke Strong in the Force dested Luke Skywalker, Strong In The Force. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "Mace Windu Master of the Order dested Mace Windu, Master Of The Order. "
    "EL-19 dested Incom T-16 Skyhopper. Qui-Gon Jinn w/ Lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "Leia Rebel Princess dested Leia, Rebel Princess. Wesa Gotta Grand Army as written. "
    "Sorry About the Mess + BP dested Sorry About The Mess & Blaster Proficiency. "
    "AOR dested All Wings Report In. Let the Wookiee Win dested Let The Wookiee Win. "
    "Were You Looking For Me as written. Speak w/ the Jedi Council dested Speak With The Jedi Council. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Only Jedi Carry That Weapon as written. Your Insight Serves You Well as written. "
    "Do or Do Not dested Do Or Do Not. Let's Keep A Little Optimism Here as written. "
    "Simple Tricks + Nonsense dested Simple Tricks And Nonsense. "
    "Form left column reprints 37–38 on lines 39–40 (Qui-Gon ditto + Leia). "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Mike Tomashewski. Dark. Deck title No One expects the Spanish Inquisition! "
    "Occupied crossed; Invasion / In Complete Control as written. "
    "Where Are Those Droidekas as written. 3720 to 1 dested 3,720 To 1. "
    "He is Not Ready + Imp. Propaganda dested He Is Not Ready (combo title is not in the 2013 pool). "
    "Blockade Support Ship as written. Maul's Sith Infiltrator as written. "
    "Naboo TP Throne Room dested Naboo: Theed Palace Throne Room. "
    "Naboo TP Courtyard dested Naboo: Theed Palace Courtyard. "
    "Naboo TP Generator dested Naboo: Theed Palace Generator. "
    "P13 + P14 dested P-13 & P-14. Mandalorian Father of Fett dested Jango Fett, The Assassin. "
    "Nute Gunray Neimoidian Viceroy dested Nute Gunray, Neimoidian Viceroy. "
    "Daultay Dofine dested Daultay Dofine. Master Destroyers dested Master, Destroyers!. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Ghhhk + Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "Elis Helrot as written. Oh Switch Off dested Oh, Switch Off. "
    "Lullaby x3 dested Twi'lek Advisor. Wounded Warrior as written. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Death Star Sentry crossed; Resistance dested Resistance. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "Form left column reprints 37–38 on lines 39–40 (Destroyer Droid dittos). "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Imperial Atrocity", True, qty=2),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Battle Plains"),
    n("Yavin 4: Massassi War Room", True),
    n("Nar Shaddaa"),
    n("Qui-Gon's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Threepio With His Parts Showing"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Corran Horn"),
    n("Mace Windu", True),
    n("Lando Calrissian, Scoundrel"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Admiral Ackbar", True),
    n("Mace Windu, Master Of The Order"),
    n("Incom T-16 Skyhopper"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Leia, Rebel Princess"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Escape Pod", True),
    n("Rebel Barrier"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("All Wings Report In", qty=2),
    n("Blaster Deflection", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Houjix"),
    n("Rebel Leadership", True, qty=3),
    n("Nabrun Leids"),
    n("Life Debt"),
    n("Were You Looking For Me?"),
    n("Speak With The Jedi Council"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well", True),
    n("Do Or Do Not"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Droid Racks", True),
    n("Naboo"),
    n("Blockade Flagship"),
    n("Naboo: Swamp"),
    n("Prepared Defenses"),
    n("At Last We Are Getting Results", True),
    n("Where Are Those Droidekas?!", True),
    n("3,720 To 1", True),
    n("Tarkin's Bounty", True),
    n("Crossfire"),
    n("You Cannot Hide Forever"),
    n("Forced Servitude"),
    n("He Is Not Ready"),
    n("Blockade Support Ship"),
    n("Maul's Sith Infiltrator"),
    n("Naboo: Theed Palace Throne Room"),
    n("Blockade Flagship: Bridge"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Generator"),
    n("P-60", qty=2),
    n("P-59", qty=2),
    n("P-13 & P-14"),
    n("Jango Fett, The Assassin"),
    n("Guri", qty=2),
    n("Darth Maul"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Daultay Dofine", True),
    n("Destroyer Droid", qty=9),
    n("Master, Destroyers!", qty=3),
    n("Lightsaber Deficiency", True),
    n("Sniper & Dark Strike"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Elis Helrot"),
    n("Oh, Switch Off", qty=2),
    n("Twi'lek Advisor", qty=3),
    n("Wounded Warrior", qty=2),
    n("Outflank", True),
    n("Abyssin Ornament"),
    n("Self-Destruct Mechanism"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Resistance", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Fanfare", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
