#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Matt Sokol.

Source: 2012mpcday1.pdf pages 11–12 (2010 form, 12 shields).
Name Sokol Dark / Sokol Light dested Matt Sokol. Username blank.
p11 DARK checked. Event MPC. Deck Name empty.
p12 LIGHT checked. Event MPC. Deck Name empty.
"""
from __future__ import annotations

PLAYER = "Matt Sokol"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 12
DS_PAGE = 11
LS_SCAN = "2012 Match Play Championship Day 1 Matt Sokol LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Matt Sokol DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Sokol Light dested Matt Sokol. Username blank. "
    "LIGHT checked. Event MPC. Deck Name empty. No objective; start dested Yavin 4: Massassi Throne Room. "
    "Krayt Dragon Howl & Arm dested Armed And Dangerous & Krayt Dragon Howl. "
    "Haven dested as written. Tanker IU dested Tantive IV. "
    "HC + F dested Han, Chewie, And The Falcon. LTWW dested Let The Wookiee Win. "
    "Speak with the Jedi dested Speak With The Jedi Council. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. "
    "Hands off dested Hands Off. Sai'torr Kal Fas dested Sai'torr Kal Fas. "
    "Leia, Rebel Princess dested Leia, Rebel Princess. Padme Naberrie dested Padmé Naberrie. "
    "Lando Calrissian, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Obi-Wan With Stick dested Obi-Wan With Lightsaber. "
    "Qui-Gon Jinn with dested Qui-Gon Jinn With Lightsaber. "
    "Luke Skywalker, Jedi dested Luke Skywalker, Jedi Knight. "
    "Luke Skywalker, SITF dested Luke Skywalker, Strong In The Force "
    "(form 44 True and form 45 empty kept separate). "
    "Luke's Bionic Hand dested as written. "
    "Home One Room dested Home One: War Room. Hoth: War Room dested Hoth: Echo Command Center (War Room). "
    "Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Coruscant: Jedi Chamber dested Coruscant: Jedi Council Chamber. "
    "Yavin 4: Throne Room dested Yavin 4: Massassi Throne Room. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Unique overcounts sheet-accurate (Han, Chewie, And The Falcon x2, Rebel Leadership x3, "
    "Let The Wookiee Win x2, Smoke Screen x4, Wesa Gotta Grand Army x2, Blaster Deflection x2, "
    "Sense x2, Speak With The Jedi Council x2, Clash Of Sabers x2, Lando Calrissian, Scoundrel x2, "
    "Qui-Gon Jinn With Lightsaber x2, Mace Windu x2). "
    "(V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Sokol Dark dested Matt Sokol. Username blank. "
    "DARK checked. Event MPC. Deck Name empty. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Naboo TP Generator Core dested Naboo: Theed Palace Generator Core. "
    "Vader's Saber dested Vader's Lightsaber. Galen's Saber dested Galen's Lightsaber, Vader's Gift. "
    "Cyborg's Saber dested Grievous' Lightsabers. Boba Fett in Slave 1 dested Boba Fett In Slave I. "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter. Galen's Fighter dested Rogue Shadow. "
    "Mara Jade dested Mara Jade. DV DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Galen dested Galen, Secret Apprentice. Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "The Emperor dested The Emperor. Black Leader dested Juno Eclipse, Black Leader. "
    "4-LOM with Gun dested 4-LOM With Concussion Rifle. Search & Destroy dested Search And Destroy. "
    "Ni Chuba Na?? dested Ni Chuba Na??. Gift of the Master dested Gift Of The Master. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Ghhhk & Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "MM & EO dested Masterful Move & Endor Occupation. "
    "Sniper & Dark Strike dested Sniper & Dark Strike. Weapon Lev dested Weapon Levitation. "
    "Knowledge and Defense dested Knowledge And Defense. "
    "We'll Let Fate-a Decide dested We'll Let Fate-a Decide, Huh?. "
    "Come Here You Big dested Come Here You Big Coward. After Her dested After Her!. "
    "Unique overcounts sheet-accurate (Darth Vader, Dark Lord Of The Sith x3, "
    "Galen, Secret Apprentice x3, Grievous, Hunter Of Jedi x2, Garindan x2, Discord x2, "
    "We Must Accelerate Our Plans x3, Stunning Leader x2, Force Field x2). "
    "(V) from checkbox; dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Scrambled Transmission", True),
    n("Draw Their Fire"),
    n("Civil Disorder", True),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Haven"),
    n("Tantive IV", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Smoke Screen", qty=4),
    n("Wesa Gotta Grand Army", qty=2),
    n("Blaster Deflection", qty=2),
    n("Sense", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Hands Off", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Padmé Naberrie", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand", True),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Kiffex"),
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Let's Keep A Little Optimism Here"),
    n("Only Jedi Carry That Weapon"),
    n("Chasm", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Endor"),
    n("Coruscant: Imperial City"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Hallway"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Boba Fett In Slave I", True),
    n("Zuckuss In Mist Hunter"),
    n("Rogue Shadow"),
    n("Victory"),
    n("Battle Droid Squad"),
    n("Mara Jade", True),
    n("Grand Admiral Thrawn"),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("The Emperor", True),
    n("Emperor Palpatine"),
    n("Juno Eclipse, Black Leader"),
    n("Garindan", True, qty=2),
    n("General Nevar"),
    n("4-LOM With Concussion Rifle", True),
    n("No Escape"),
    n("Search And Destroy"),
    n("Protocol Failure"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("A Sith's Plans"),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Revenge Of The Sith"),
    n("Discord", qty=2),
    n("Lightsaber Deficiency", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Lightning"),
    n("Stunning Leader", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Masterful Move & Endor Occupation"),
    n("You Are Beaten"),
    n("Sniper & Dark Strike"),
    n("Force Field", True, qty=2),
    n("Force Push", True),
    n("Weapon Levitation"),
    n("Prepared Defenses", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Battle Order"),
    n("After Her!", True),
    n("Secret Plans", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
]
DS_ADD = []
