#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Scott Morgan.

Source: 2012BespinRegionals.pdf pages 5–6 (typed 2010 Xerox).
p05 Light / p06 Dark Name Scott Morgan dested Scott Morgan analog leftover
2012 Nats / player-stubs/Scott_Morgan.wiki. Username boshek1.
Do not dest as a new person. Do not dest 2012 Nats Scott Morgan 60s again.
"""
from __future__ import annotations

PLAYER = "Scott Morgan"
USERNAME = "boshek1"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2012 Bespin Regionals Scott Morgan LS.png"
DS_SCAN = "2012 Bespin Regionals Scott Morgan DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed 2010 Xerox p05 Light / p06 Dark. "
    "Name Scott Morgan dested Scott Morgan analog leftover 2012 Nats / "
    "player-stubs/Scott_Morgan.wiki. Username boshek1. Date blank Event 2012 Bespin Regional. "
    "Do not dest as a new person. Do not dest 2012 Nats Scott Morgan 60s again."
)
LS_NOTE = (
    "Typed 2010 Xerox p05 Light. Name Scott Morgan dested Scott Morgan. Username boshek1. "
    "LIGHT checked. Deck Name Why Am I Playing TRM???? dested off article. "
    "Yavin 4: Massassi Throne Room dested Yavin 4: Massassi Throne Room analog leftover Hanson. "
    "Insurrection & *Aim High dested Insurrection & Aim High analog leftover 2012 Nats. "
    "Padme Naberrie dested Padmé Naberrie True analog leftover Brady. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas True analog leftover Lingrell. "
    "Seeking An Audience dested Seeking An Audience True analog leftover Brady. "
    "Sorry About The Mess & Blaster Proficiency dested analog leftover Ziagos qty=2. "
    "Hear Me Baby, Hold Together dested Hear Me Baby, Hold Together True analog leftover Frafjord. "
    "Let The Wookiee Win dested Let The Wookiee Win True analog leftover Brady qty=2. "
    "Shield 12 Ounee Ta dested analog leftover 2012 Nats same typed dump. Unique 60 shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox p06 Dark. Name Scott Morgan dested Scott Morgan. Username boshek1. "
    "DARK checked. Deck Name A Stupid Move On My Part dested off article. "
    "A Stunning Move/A Valuable Hostage dested A Stunning Move / A Valuable Hostage analog leftover virtual-only. "
    "Ni Chuba Na?? dested Ni Chuba Na? True analog leftover TYPE_OVERRIDE. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi analog leftover Consoli qty=2. "
    "IG Bodyguard droid dested IG-100 MagnaGuard analog leftover Consoli. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Consoli. "
    "Control dested Control & Set For Stun analog leftover Burgt qty=2. "
    "Knowledge And Defense True IN THE 60. Darth Maul, Young Apprentice x3 unique overcount. "
    "Shield 12 Allegations Of Corruption dested analog leftover 2012 Nats same typed dump. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Insurrection & Aim High"),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Mace Windu", True, qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Padmé Naberrie", True),
    n("Leia, Rebel Princess", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("IL-19"),
    n("Leia's Blaster Rifle"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True, qty=2),
    n("Artoo-Detoo In Red 5"),
    n("Han, Chewie, And The Falcon"),
    n("Home One"),
    n("Spiral"),
    n("Tantive IV", True),
    n("Sai'torr Kal Fas", True),
    n("A Jedi's Plans"),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Houjix & Out Of Nowhere"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Sense", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Desperate Reach", True),
    n("Hear Me Baby, Hold Together", True),
    n("Let The Wookiee Win", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Night Club"),
    n("Home One: Docking Bay"),
    n("Home One: War Room"),
    n("Kiffex"),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("The Professor", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Ounee Ta"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Insidious Prisoner"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Coruscant: Palpatine's Quarters"),
    n("Ni Chuba Na?", True),
    n("Gift Of The Master"),
    n("Establish Control", True),
    n("Prepared Defenses"),
    n("Knowledge And Defense", True),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("P-59"),
    n("IG-100 MagnaGuard"),
    n("Probot"),
    n("OOM-9", True),
    n("Battle Droid Squad", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Boba Fett In Slave I", True),
    n("Victory"),
    n("Zuckuss In Mist Hunter"),
    n("Blaster Rack", True),
    n("Ability, Ability, Ability", True),
    n("Search And Destroy"),
    n("A Sith's Weapon"),
    n("Protocol Failure"),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("Tarkin's Bounty", True),
    n("The Phantom Menace", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sniper & Dark Strike", qty=2),
    n("Control & Set For Stun", qty=2),
    n("Force Field", True, qty=2),
    n("Force Push", True),
    n("Cold Feet", True),
    n("Maul Strikes"),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True, qty=2),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Fondor"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Imperial Detention"),
    n("Wipe Them Out, All Of Them", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Abyss"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
