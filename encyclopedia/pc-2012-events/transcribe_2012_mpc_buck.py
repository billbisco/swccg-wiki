#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Carl Buck.

Source: 2012mpcday1.pdf pages 57–58 (2010 form, 12 shields).
Name Carl Buck dested Carl Buck. Username blank.
p57 Light AFA. p58 Dark Invasion.
Do not dest as a new person. Do not rewrite 2013 leftovers.
2013 leftover PLAYER="Carl Buck" USERNAME blank; pack player-stubs/Carl_Buck.wiki.
"""
from __future__ import annotations

PLAYER = "Carl Buck"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 57
DS_PAGE = 58
LS_SCAN = "2012 Match Play Championship Day 1 Carl Buck LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Carl Buck DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form. LIGHT/DARK header boxes blank; dest from the 60s."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Carl Buck. Username blank. LIGHT/DARK boxes blank. "
    "Event Date blank. Event Name blank. Deck Name blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Anger Fear Aggression dested Anger, Fear, Aggression True. "
    "Scrombel Transmission dested Scrambled Transmission True. "
    "Eject eject & Imperial Atrocity dested Eject! Eject! Eject! & Imperial Atrocity "
    "(no True; combo has no (V) reprint). "
    "Strike Force dested Strikeforce True. "
    "Mandellian Scrubjay dested as written x2 (line 7 crossed start then dittos). "
    "Control / Tunnel Vision dested Control & Tunnel Vision. "
    "Sorry Bout Mess / Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Rycar Ryjerd dested Rycar Ryjerd True. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon True x2. "
    "Obi-Wan in Radiant VII dested Obi-Wan In Radiant VII True. "
    "Obi-Wan's Journal dested Obi-Wan's Journal. "
    "Qui Gon Jinn w/ stick dested Qui-Gon Jinn With Lightsaber x2. "
    "FL-14 dested as written (no True; no (V) reprint). "
    "3PO w/ Parts Showing dested Threepio With His Parts Showing. "
    "Unique 60. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Carl Buck. Username blank. LIGHT/DARK boxes blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Knowledge and Defense dested Knowledge And Defense True. "
    "AA + Laser Cannon dested AAT Laser Cannon x2. "
    "Droid Starfighter Laser Cannon dested Droid Starfighter Laser Cannons x2. "
    "Droid Blaster Rifle dested as written. "
    "There St'll Coming thru dested They're Still Coming Through!. "
    "Daulay Dofine dested Daultay Dofine True. "
    "Oh Switch Off dested Oh, Switch Off x2. "
    "Invasion / En Complete Control dested Invasion / In Complete Control. "
    "OOM-1 w/ Backup dested OOM-1 With Backup as written. "
    "Droid Rack dested Droid Racks. "
    "Insignificant Losses dested Insignificant Losses (no True; no (V) reprint). "
    "Theed Palace Throne Room dested Naboo: Theed Palace Throne Room. "
    "Ghhhk / Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Protocol dested Protocol Failure. "
    "OOM Commander Battle Droid dested as written x2 (no True; no (V) reprint). "
    "Nothing Can Get Through Our Shield dested Nothing Can Get Through Our Shield x2. "
    "Masterful Move / Endor Occupation dested Masterful Move & Endor Occupation. "
    "Form 60 Battle Droid Blaster Rifle crossed with no replacement skipped. "
    "Unique 59 sheet-accurate. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Scrambled Transmission", True),
    n("Eject! Eject! Eject! & Imperial Atrocity"),
    n("Draw Their Fire"),
    n("Strikeforce", True),
    n("Mandellian Scrubjay", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Hindsight", True),
    n("Lightsaber Proficiency"),
    n("Speak With The Jedi Council", qty=2),
    n("Clash Of Sabers"),
    n("We Wish To Board At Once"),
    n("Control & Tunnel Vision"),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("A Jedi's Resilience", qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Nabrun Leids"),
    n("Let The Wookiee Win", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Under Attack"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber"),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Spiral", qty=2),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII", True),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand", True),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("FL-14"),
    n("Threepio With His Parts Showing"),
    n("Sense"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("The Professor", True),
    n("Only Jedi Carry That Weapon", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("AAT Laser Cannon", qty=2),
    n("Droid Starfighter Laser Cannons", qty=2),
    n("Droid Blaster Rifle"),
    n("OOM-9"),
    n("They're Still Coming Through!"),
    n("Droid Starfighter", qty=2),
    n("Armored Attack Tank", qty=3),
    n("Daultay Dofine", True),
    n("Oh, Switch Off", qty=2),
    n("Blockade Support Ship", True),
    n("Defensive Fire", True),
    n("SSA-306"),
    n("3B3-10", True),
    n("DFS-327", qty=2),
    n("Trade Federation Tactics", True, qty=2),
    n("Imperial Artillery", qty=2),
    n("OOM-1 With Backup"),
    n("Sil Unch"),
    n("Invasion / In Complete Control"),
    n("Droid Racks"),
    n("At Last We Are Getting Results", True),
    n("Insignificant Losses"),
    n("Blockade Flagship", True),
    n("Naboo"),
    n("Naboo: Swamp"),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Battle Plains"),
    n("Baktoid Armor Workshop", True),
    n("Prepared Defenses"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Push", True),
    n("Collateral Damage"),
    n("Rune Haako, Legal Counsel"),
    n("3B3-21"),
    n("Protocol Failure"),
    n("Cease Fire!"),
    n("OOM Commander Battle Droid", qty=2),
    n("Imperial Propaganda", True),
    n("Nothing Can Get Through Our Shield", qty=2),
    n("DFS-1015"),
    n("Tey How"),
    n("Guri"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("SSA-1015"),
    n("Deployment Orders", True),
    n("SSA-719"),
    n("Masterful Move & Endor Occupation"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("There Is No Try"),
    n("After Her!", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
