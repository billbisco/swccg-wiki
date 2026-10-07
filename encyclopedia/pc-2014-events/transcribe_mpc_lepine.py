#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Cole Lepine.

Source: MPC-2014-Day-1-Main-Event.pdf pages 69–70 (2013 form, 15 shields).
Name C Lepine dested Cole Lepine. Username clepine / Clepines.
Dark Slavers. Light Quiet Mining Colony.
"""
from __future__ import annotations

PLAYER = "Cole Lepine"
USERNAME = "clepine"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 70
DS_PAGE = 69
LS_SCAN = "2014 Match Play Championship Day 1 Cole Lepine LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Cole Lepine DS.png"
LS_DECK_NAME = "QMC"
DS_DECK_NAME = "Slavers"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name C Lepine dested Cole Lepine. Username clepine. "
    "LIGHT checked. QMC dested Quiet Mining Colony / Independent Operation (V). "
    "We Need Luke dested We'll Handle This. Hiding In The Garbage dested Hiding In The Garbage (V). "
    "I'll Take The Leader crossed skipped. T. Utris M'Toc dested Trooper Utris M'Toc (V). "
    "S. Edian dested Sergeant Edian (V). Unique overcounts sheet-accurate "
    "(Path Of Least Resistance (V) x3, Let The Wookiee Win x2, Rebel Barrier x2, "
    "Choke x2, Imperial Atrocity (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name C Lepine dested Cole Lepine. Username Clepines. "
    "DARK checked. Slavers dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Virtual-only objective dested without (V) even with checkbox True. "
    "K: SCH dested Kashyyyk: Slaving Camp Headquarters (V). "
    "Jango Father Of Fett dested Jango Fett, The Assassin (V). "
    "Elom Mon dested Ephant Mon. Boba Fett Relentless Hunter dested "
    "Boba Fett, Relentless Bounty Hunter (V). Blast My Star Destroyer dested "
    "Alert My Star Destroyer!. Imbalance & Kessel Combo dested Imbalance & Kintan Strider. "
    "Line 57 Look Sir Droids crossed; Defensive Fire & Hutt Smooch replacement. "
    "Unique overcounts sheet-accurate (Greedo x3, Scum And Villainy x2, "
    "Short Range Fighters & Watch Your Back! x3, Sonic Bombardment (V) x3, "
    "Sneak Attack (V) x2, Oh, Switch Off x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation", True),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Hoth: Ice Plains", True),
    n("All My Urchins & Cloud City Celebration", True),
    n("Menace Fades"),
    n("We'll Handle This"),
    n("Path Of Least Resistance", True, qty=3),
    n("Cloud City: Nightclub"),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Hiding In The Garbage", True),
    n("Chewbacca, Walking Carpet", True),
    n("Luke With Lightsaber"),
    n("Melas", True),
    n("Jar Jar Binks"),
    n("Tanus Spijek", True),
    n("Foul Moudama", True),
    n("Han Solo, Innocent Scoundrel", True),
    n("Aayla Secura", True),
    n("Leesub Sirln", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Leslomy Tacema", True),
    n("Mirax Terrik"),
    n("Harc Seff", True),
    n("Dash Rendar", True),
    n("Leia, Rebel Princess"),
    n("Nien Nunb, Sullustan Smuggler", True),
    n("Wokling", True),
    n("Sergeant Edian", True),
    n("Trooper Utris M'Toc", True),
    n("Kal'Falnl C'ndros"),
    n("Desperate Reach", True),
    n("Battle Plan & Draw Their Fire"),
    n("Choke", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("All Wings Report In"),
    n("It Could Be Worse", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Don't Underestimate Our Chances", True),
    n("It's A Hit"),
    n("Rebel Barrier", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("It's A Trap!"),
    n("Alternatives To Fighting"),
    n("Booster In Pulsar Skate", True),
    n("Overseer", True),
    n("Lando's Luxury Yacht", True),
    n("Ellor's Madak", True),
    n("Imperial Atrocity", True, qty=2),
    n("Yoxgit"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Weapons Display"),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Your Ship", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters", True),
    n("Den Of Thieves & Special Delivery", True),
    n("Wookiee Subjugation", True),
    n("Mercenary Slavers", True),
    n("Jabba's Haven", True),
    n("Prisoner Of The Hutt"),
    n("Nal Hutta"),
    n("Kashyyyk: Skyhook Platform", True),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Velken Tezeri", True),
    n("Greedo", qty=3),
    n("Jabba's Space Cruiser", True),
    n("Scum And Villainy", qty=2),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Sonic Bombardment", True, qty=3),
    n("Jango Fett, The Assassin", True),
    n("Jabba's Sail Barge", True),
    n("Jabba The Hutt", True),
    n("Mercenary Pilot"),
    n("Reegesk", True),
    n("Hutt Bounty", True),
    n("Ephant Mon"),
    n("Prince Xizor"),
    n("Boba Fett, Relentless Bounty Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("Boba Fett"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Protocol Failure", True),
    n("Look Sir, Droids"),
    n("Garindan", True),
    n("Sneak Attack", True, qty=2),
    n("Maul's Sith Infiltrator"),
    n("Oh, Switch Off", qty=2),
    n("Weapon Levitation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Dengar With Blaster Carbine", True),
    n("Court Of The Vile Gangster", True),
    n("Alert My Star Destroyer!"),
    n("Imbalance & Kintan Strider"),
    n("Poteen Boska", True),
    n("Bossk", True),
    n("Tarkin's Orders"),
    n("4-LOM With Concussion Rifle"),
    n("OOM-9", True),
    n("Probot"),
    n("Lightsaber Deficiency", True),
    n("Defensive Fire & Hutt Smooch"),
    n("Mara Jade With Lightsaber", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
