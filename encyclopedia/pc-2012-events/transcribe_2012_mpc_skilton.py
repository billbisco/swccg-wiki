#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Steve Skilton.

Source: 2012mpcday1.pdf pages 91–92 (2010 form).
Name Steve to the izz0 dested Steve Skilton (2013 leftover analog).
p91 Light. p92 Dark. Username box blank.
Do not dest as Steve Izzo. Do not dest as a new person.
Do not rewrite 2013 leftovers. Pack player-stubs/Steve_Skilton.wiki.
"""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 91
DS_PAGE = 92
LS_SCAN = "2012 Match Play Championship Day 1 Steve Skilton LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Steve Skilton DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Steve to the izz0 dested Steve Skilton. "
    "Username box blank. LIGHT checked. Deck Name blank. Event Date/Name blank. "
    "Do not dest as Steve Izzo. Do not rewrite 2013 leftovers. "
    "Line 1 remnant Throne Room dested Yavin 4: Massassi Throne Room. "
    "Rebel cell landing site dested Rebel Cell - Hidden Landing Site. "
    "Luke SITF dested Luke Skywalker, Strong In The Force x2. "
    "HCE dested Hoth: Echo Command Center. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel x2. "
    "EPP Obi-wan dested Obi-Wan With Lightsaber x2. "
    "Speak w/ Jedi Council dested Speak With The Jedi Council. "
    "SATB/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Master Qui Gon dested Master Qui-Gon True x2. "
    "AJR dested A Jedi's Resilience x2. "
    "Clash dested Clash Of Sabers. "
    "Blast Deflection dested Blaster Deflection x2. "
    "Wesa dested Wesa Gotta Grand Army x2. "
    "Qui's Lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "Sai'torr dested Sai'torr Kal Fas True. "
    "Rebel Leadership True then ditto empty kept separate. "
    "Kittos dested Kit Fisto. "
    "NOOOOOOOOOOOO dested NOOOOOOOOOOOO! True. "
    "Were you looking for me dested Were You Looking For Me?. "
    "Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Steve to the izz0 dested Steve Skilton. "
    "Username box blank. DARK checked. Deck Name blank. Event Date/Name blank. "
    "Do not dest as Steve Izzo. Do not rewrite 2013 leftovers. "
    "HD dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "K+D dested Knowledge And Defense True. "
    "DVD LoTS dested Darth Vader, Dark Lord Of The Sith x3. "
    "Galen dested Galen, Secret Apprentice x3. "
    "Cyborg Comm dested Grievous, Hunter Of Jedi x2. "
    "Weapon Lev Combo dested Weapon Levitation & The Empire's Back True then empty. "
    "Fury of the Sith dested Fury Of The Sith x2. "
    "Galen's Saber, V's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Vader's Saber dested Darth Vader's Lightsaber. "
    "P-59 dested P-59. Flagship Bridge dested Blockade Flagship: Bridge. "
    "4-Lom w gun dested 4-LOM With Concussion Rifle True. "
    "Dr. E + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Comscan dested Comscan Detection True. "
    "Where are you taking this thing dested Where Are You Taking This ... Thing? True. "
    "Line 40 cropped; dest unique 59. "
    "The Emp's Prize dested The Emperor's Prize True. "
    "Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "Kir Kanos w/ Force Pike dested Kir Kanos With Force Pike True. "
    "EPP Mara dested Mara Jade With Lightsaber True. "
    "DS: War Room dested Death Star: War Room True. "
    "Cyborg's Sabers dested Grievous' Lightsabers. "
    "Sith's plans dested Sith Fury. "
    "Lost Moooo dested NOOOOOOOOOOOO! True. "
    "Coruscant dested Coruscant (Dark). "
    "Ni Chuba dested Ni Chuba Na?? True. "
    "Unique 59. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Rebel Cell - Hidden Landing Site"),
    n("Quick Draw"),
    n("Luke Skywalker, Strong In The Force"),
    n("Draw Their Fire"),
    n("Tantive IV", True),
    n("Corran Horn"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hoth: Echo Command Center"),
    n("Lando Calrissian, Scoundrel"),
    n("Revolution"),
    n("Luke Skywalker, Jedi Knight"),
    n("Artoo-Detoo In Red 5"),
    n("Obi-Wan With Lightsaber"),
    n("Luke Skywalker, Strong In The Force"),
    n("Lando Calrissian, Scoundrel"),
    n("Speak With The Jedi Council"),
    n("Rebel Leadership", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Let The Wookiee Win", True),
    n("Mace Windu", True),
    n("Jedi Lightsaber", True),
    n("Master Qui-Gon", True),
    n("Home One: War Room"),
    n("Weapon Levitation"),
    n("Mechanical Failure"),
    n("Luke's Lightsaber"),
    n("A Jedi's Resilience"),
    n("Gift Of The Mentor"),
    n("Obi-Wan With Lightsaber"),
    n("Clash Of Sabers"),
    n("Blaster Deflection"),
    n("Artoo-Detoo In Red 5"),
    n("Mechanical Failure"),
    n("The Force Is Strong With This One"),
    n("A Jedi's Resilience"),
    n("Sense"),
    n("Wesa Gotta Grand Army"),
    n("Blaster Deflection"),
    n("Let The Wookiee Win", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Sai'torr Kal Fas", True),
    n("Master Qui-Gon", True),
    n("Threepio With His Parts Showing"),
    n("Hear Me Baby, Hold Together", True),
    n("Leia, Rebel Princess"),
    n("Home One"),
    n("Mace Windu", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Wesa Gotta Grand Army"),
    n("Kit Fisto"),
    n("Admiral Ackbar", True),
    n("NOOOOOOOOOOOO!", True),
    n("Let The Wookiee Win", True),
    n("Imperial Atrocity", True),
    n("Were You Looking For Me?"),
    n("Anger, Fear, Aggression", True),
    n("Hindsight", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Another Pathetic Lifeform", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Yavin Sentry"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Knowledge And Defense", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("We Must Accelerate Our Plans", qty=3),
    n("Emperor Palpatine", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Force Field", True, qty=2),
    n("Weapon Levitation & The Empire's Back", True),
    n("Weapon Levitation & The Empire's Back"),
    n("Fury Of The Sith", qty=2),
    n("Trophy Of A Kill", qty=2),
    n("Presence Of The Force"),
    n("Restraining Bolt"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Darth Vader's Lightsaber"),
    n("Cold Feet", True),
    n("P-59"),
    n("Elis Helrot"),
    n("Blockade Flagship: Bridge"),
    n("A Sith's Weapon"),
    n("4-LOM With Concussion Rifle", True),
    n("Emperor's Power", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Comscan Detection", True),
    n("Force Push"),
    n("Where Are You Taking This ... Thing?", True),
    n("The Emperor's Prize", True),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Masterful Move & Endor Occupation"),
    n("No Escape"),
    n("Program Trap", True),
    n("Blast Door Controls"),
    n("Kir Kanos With Force Pike", True),
    n("First Strike"),
    n("Mara Jade With Lightsaber", True),
    n("Death Star: War Room", True),
    n("Grievous' Lightsabers"),
    n("Gift Of The Master"),
    n("Blaster Rack", True),
    n("Sith Fury"),
    n("NOOOOOOOOOOOO!", True),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Force Lightning"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Do They Have A Code Clearance?", True),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
