#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Nathan typed 2013 Print Form LS+DS.

Name field Nathan. Username SolaGratia. Dest Nathan as written (first name only).
Do not dest as Nathan Russell / Nathan Wall / Nathan Way.
"""
from __future__ import annotations

PLAYER = "Nathan"
USERNAME = "SolaGratia"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 41
DS_PAGE = 42
LS_SCAN = "2013 SoCal Grand Prix Day 1 p41 Nathan LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p42 Nathan DS.png"
LS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Nathan dested as written. Username SolaGratia. "
    "Deck Name ...but will it work?!?!? Event SD Grand Prix. LIGHT checked. "
    "We Have a Plan / TWBLAC empty dested We Have A Plan / They Will Be Lost And Confused. "
    "Naboo: Throne Room / Hallway / Courtyard dested Naboo: Theed Palace Throne Room / "
    "Hallway / Courtyard. "
    "HFTMF dested Heading For The Medical Frigate. "
    "K' Lor Slug COMBO dested Commando Training & K'lor'slug. "
    "Naboo: BNC dested Naboo: Boss Nass' Chambers. "
    "Senator Leia dested Senator Leia Organa. "
    "Obi-Wan Jedi Knight dested Obi-Wan Kenobi, Jedi Knight. "
    "Master Qui-Gon Jinn dested Master Qui-Gon. "
    "Houjix COMBO dested Houjix & Out Of Nowhere. "
    "Control / Tunnel Vision dested Control & Tunnel Vision. "
    "Wesa Got a Grand Army dested Wesa Gotta Grand Army. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "AFA dested Anger, Fear, Aggression. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred. "
    "Weapon Display dested Weapons Display. "
    "You're Insights Serve You Well dested Your Insight Serves You Well. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Do or Do Not dested Do, Or Do Not. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Nathan dested as written. Username SolaGratia. "
    "Deck Name ...something go boom. Event SD Grand Prix. DARK checked. "
    "SYCFA empty dested Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Laser Canon Battery dested Laser Cannon Battery. "
    "EPP Maul dested Darth Maul With Lightsaber. "
    "Devestator dested Devastator. "
    "Victory dested Victory as written. "
    "He is Not Ready / Imp Prop crossed, There is No Try dested There Is No Try. "
    "Intensify Forward Batteries dested as written. "
    "Tarkin's Doctrine dested as written. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Cease Fire dested Cease Fire!. "
    "Tie Sentry Ships dested TIE Sentry Ships. "
    "K&D dested Knowledge And Defense. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Courtyard"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug"),
    n("A Good Blaster At Your Side"),
    n("Quick Draw", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Queen Amidala", qty=3),
    n("Panaka, Protector Of The Queen", qty=3),
    n("Senator Leia Organa", qty=2),
    n("Jerus Jannick", qty=2),
    n("Maris Brood, Fallen Jedi", qty=2),
    n("Ki-Adi-Mundi", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Master Qui-Gon", True),
    n("Artoo, Brave Little Droid"),
    n("Bravo Fighter", True),
    n("Landing Claw"),
    n("Panaka's Blaster"),
    n("Amidala's Blaster"),
    n("Leia's Blaster Rifle"),
    n("Guardian's Lightsaber"),
    n("Sai'torr Kal Fas", True),
    n("We'll Take The Long Way", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Imperial Atrocity", True, qty=2),
    n("Jedi Levitation", True),
    n("Found Someone You Have", True),
    n("Slight Weapons Malfunction", qty=2),
    n("Seeking An Audience", True),
    n("Control & Tunnel Vision"),
    n("Either Way, You Win", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("I've Decided To Go Back", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Ascension Guns", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("The Professor"),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Don't Do That Again"),
    n("He Can Go About His Business", True),
    n("Ultimatum", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Death Star: Central Core", True),
    n("Death Star: War Room", True),
    n("Nal Hutta"),
    n("Rendili"),
    n("Kiffex"),
    n("Darth Sidious", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("U-3PO"),
    n("Intensify Forward Batteries"),
    n("Commence Primary Ignition", True),
    n("Superlaser"),
    n("Judicator", qty=2),
    n("Conquest", True, qty=2),
    n("Accuser"),
    n("Devastator", True),
    n("Tyrant"),
    n("Stalker", True),
    n("Thunderflare"),
    n("Victory"),
    n("Dreaded Imperial Starfleet", True),
    n("Tarkin's Doctrine"),
    n("Presence Of The Force"),
    n("Imperial Propaganda", True),
    n("There Is No Try", True),
    n("Protocol Failure"),
    n("Force Push", True),
    n("Relentless Pursuit", qty=2),
    n("Stunning Leader", qty=2),
    n("Sense", qty=2),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True, qty=2),
    n("Imperial Barrier"),
    n("Cease Fire!", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("TIE Sentry Ships", True),
    n("Force Field", True, qty=2),
    n("Weapon Levitation"),
    n("Flawless Marksmanship", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Abyss", True),
    n("Imperial Detention", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
