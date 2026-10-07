#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Steve.

Source: 2014-Alderaan-Regionals.pdf pages 9–10 (2013 Print Form).
Name box is a Steve-like signature dested Steve as written. Username blank.
"""
from __future__ import annotations

PLAYER = "Steve"
USERNAME = ""
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2014 Alderaan Regionals p09 Steve LS.png"
DS_SCAN = "2014 Alderaan Regionals p10 Steve DS.png"
NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name box Steve-like signature dested Steve as written. Username blank. "
    "LS There Is Good In Him (Deck Name TIGIH) / DS Endor Operations "
    "(Deck Name EOPS Thanks From Batmouse). Dark LIGHT/DARK boxes empty; dested Dark. "
    "There Is Good In Him dested There Is Good In Him / I Can Save Him. "
    "Endor Operations dested Endor Operations / Imperial Outpost. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Slave 1, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Mandalorian Father dested Jango Fett, The Assassin. "
    "Baktoid Armor Workshop dested Baktoid Armor Workshop. "
    "Ominous Rumors Open Fire dested Ominous Rumors & Open Fire as written. "
    "AT-AT Laser Cannon dested AT-AT Cannon. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Maleun Seel dested Malvern Seel. "
    "Tarfful, Wookiee Insurgent dested Tarfful, Wookiee Insurgent. "
    "He Can Go About His Business dested He Can Go About His Business. "
    "Secret shield dested Secret Plans. "
    "Dittos inherit the first named line except where the (V) checkbox differs. "
    "NO_DEST as written: Malvern Seel; Ominous Rumors & Open Fire; Dark Commander. "
    "(V) from the checkbox. Unique overcounts sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Leia, Rebel Princess"),
    n("Houjix"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Clash Of Sabers"),
    n("Blaster Deflection", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Rebel Barrier", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Grimtaash"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Speak With The Jedi Council", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Escape Pod", True),
    n("Seeking An Audience", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Dark Approach", True),
    n("Dark Approach"),
    n("Malvern Seel"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Tarfful, Wookiee Insurgent"),
    n("Corran Horn"),
    n("Home One: War Room"),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Han With Heavy Blaster Pistol", True),
    n("Han With Heavy Blaster Pistol"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Naboo: Battle Plains"),
    n("Home One"),
    n("Sense", qty=2),
    n("Imperial Atrocity", True),
    n("Mechanical Failure"),
    n("A Jedi's Resilience", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Affect Mind", True),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Landing Platform"),
    n("Endor: Bunker"),
    n("The Emperor", True),
    n("Endor Shield", True),
    n("Inconsequential Losses", True),
    n("Baktoid Armor Workshop", True),
    n("According To My Design", True),
    n("Image Of The Dark Lord", True),
    n("Perimeter Patrol"),
    n("Establish Secret Base", True),
    n("Ominous Rumors"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Sneak Attack", qty=2),
    n("Arica"),
    n("AT-AT Cannon", qty=2),
    n("Chimaera"),
    n("Cloud City: Security Tower", True),
    n("Deployment Orders"),
    n("Dengar"),
    n("Ominous Rumors & Open Fire"),
    n("General Nevar"),
    n("Endor: Forest Clearing"),
    n("Grand Admiral Thrawn"),
    n("Armored Attack Tank", qty=3),
    n("Close Call", True),
    n("Close Call"),
    n("Sonic Bombardment", True, qty=3),
    n("We're In Attack Position Now", qty=3),
    n("U-3PO"),
    n("Imperial Artillery", True),
    n("Imperial Artillery"),
    n("Imperial Barrier"),
    n("OOM-9"),
    n("Ghhhk & Those Rebels Won't Escape Us", True, qty=3),
    n("Defensive Fire", True),
    n("Masterful Move & Endor Occupation", True),
    n("Sense", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Imbalance & Kintan Strider"),
    n("Ghhhk"),
    n("Dark Commander"),
    n("OOM Command Battle Droid"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
