#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Matt Gombos.

Source: 2012mpcday1.pdf pages 77–78 (2010 form, 12 shields).
Name Matt Gombos dested Matt Gombos (analog encyclopedia / player-stubs / generate empty).
p77 Light Yavin 4: Massassi Throne Room. p78 Dark Hunt Down And Destroy The Jedi (V).
Username Mr. G. Pack player-stubs/Matt_Gombos.wiki.
"""
from __future__ import annotations

PLAYER = "Matt Gombos"
USERNAME = "Mr. G"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 77
DS_PAGE = 78
LS_SCAN = "2012 Match Play Championship Day 1 Matt Gombos LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Matt Gombos DS.png"
LS_DECK_NAME = "I'm such a bad player..."
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Gombos dested Matt Gombos. "
    "Username Mr. G. LIGHT checked. Deck Name I'm such a bad player... "
    "Event Date/Name blank. Analog encyclopedia / player-stubs / generate empty. "
    "Yavin 4 Throne Room dested Yavin 4: Massassi Throne Room. "
    "Hoth Echo WR dested Hoth: Echo Command Center. "
    "Master Qui-Gon dested Master Qui-Gon True x2. "
    "EPP Obi-Wan dested Obi-Wan With Lightsaber x2. "
    "Coruscant JCC dested Coruscant: Jedi Council Chamber. "
    "Luke SITF dested Luke Skywalker, Strong In The Force x3. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army x2. "
    "LTWW dested Let The Wookiee Win True x3. "
    "Threepio WHPS dested Threepio With His Parts Showing. "
    "AJR dested A Jedi's Resilience x2. "
    "R2 in Red 5 dested Artoo-Detoo In Red 5 x2. "
    "Don't Tread On Me dested Don't Tread On Me True. "
    "Speak w/ the Council dested Speak With The Jedi Council. "
    "Qui-Gon's Lightsaber (R3) dested Qui-Gon Jinn's Lightsaber. "
    "Line 40 cropped; dest unique 59. Shield 12 cropped; dest shields 11. "
    "Only Jedi Curry dested Only Jedi Carry That Weapon."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Gombos dested Matt Gombos. "
    "Username Mr. G. DARK checked. Deck Name blank. Event Date/Name blank. "
    "HDADTJ / TFHGOOTU dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "Imperial City dested Coruscant: Imperial City. "
    "Coruscant (sys) dested Coruscant. "
    "Galen SA dested Galen, Secret Apprentice x3. "
    "I've Lost Artoo dested I've Lost Artoo! True. "
    "Weapon Lev + TEB dested Weapon Levitation & The Empire's Back x2. "
    "Cyborg Commander's Saber dested Grievous' Lightsabers. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x2. "
    "MM + EO dested Masterful Move & Endor Occupation. "
    "Darth Vader BLotS dested Darth Vader, Betrayer Of The Jedi x3. "
    "Kir Kanos w/ Force Pike dested Kir Kanos With Force Pike. "
    "Death Star WR dested Death Star: War Room True. "
    "POTF dested Presence Of The Force. "
    "YCHF dested You Cannot Hide Forever. "
    "Line 40 cropped. Line 60 remnant dested You Have Failed Me For The Last Time True. "
    "Shield 12 remnant dested Allegations Of Corruption. Unique 59. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Hoth: Echo Command Center"),
    n("Imperial Atrocity", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Home One"),
    n("Mechanical Failure"),
    n("Tawss Khaa", True),
    n("Revolution"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("The Force Is Strong With This One"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=3),
    n("Were You Looking For Me?"),
    n("Sense"),
    n("Naboo: Boss Nass' Chambers"),
    n("Han, Chewie, And The Falcon"),
    n("Threepio With His Parts Showing"),
    n("Jedi Lightsaber", True),
    n("A Jedi's Resilience", qty=2),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess"),
    n("Honor Of The Jedi"),
    n("Corran Horn"),
    n("Draw Their Fire"),
    n("Naboo: Battle Plains"),
    n("Major Haash'n"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Don't Tread On Me", True),
    n("Speak With The Jedi Council"),
    n("Goo Nee Tay"),
    n("Sai'torr Kal Fas", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Kiffex"),
    n("Clash Of Sabers"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Tantive IV", True),
    n("Mace Windu", True, qty=2),
    n("Luke's Lightsaber"),
    n("Blaster Deflection"),
    n("Quick Draw", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum", True),
    n("Aim High"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("A Sith's Plans"),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Emperor's Power", True),
    n("Galen, Secret Apprentice", qty=3),
    n("I've Lost Artoo!", True),
    n("Force Push", True),
    n("Weapon Levitation & The Empire's Back", qty=2),
    n("Gift Of The Master"),
    n("A Sith's Weapon"),
    n("Blaster Rack", True),
    n("Elis Helrot"),
    n("Coruscant Detention", True),
    n("First Strike"),
    n("Blast Door Controls"),
    n("Search And Destroy"),
    n("Grievous' Lightsabers"),
    n("Program Trap", True),
    n("Force Lightning"),
    n("Revenge Of The Sith", qty=2),
    n("The Circle Is Now Complete"),
    n("Force Field", True),
    n("Masterful Move & Endor Occupation"),
    n("Emperor Palpatine", qty=3),
    n("Blockade Flagship: Bridge"),
    n("Mara Jade With Lightsaber"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", qty=3),
    n("Kir Kanos With Force Pike"),
    n("Dr. Evazan & Ponda Baba"),
    n("Cold Feet", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Death Star: War Room", True),
    n("Trophy Of A Kill", qty=2),
    n("Restraining Bolt"),
    n("Presence Of The Force"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("I Have You Now", qty=2),
    n("You Cannot Hide Forever"),
    n("Naboo: Theed Palace Generator"),
    n("Sniper & Dark Strike"),
    n("You Have Failed Me For The Last Time", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Secret Plans", True),
    n("Resistance"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
