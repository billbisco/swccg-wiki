#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Schoenthal.

Source: 2012mpcday1.pdf pages 125–126 (2010 form, 12 shields).
Name Chris Schoenthal dested Chris Schoenthal. Username imrhil327.
p125 Light Watch Your Step. p126 Dark Hunt Down And Destroy The Jedi (V).
Pack pages/Chris_Schoenthal.wiki (is_bio True Tournament Advocate).
Do not dest as a new person. Do not rewrite 2013 Alderaan / 2014 TMW leftovers.
"""
from __future__ import annotations

PLAYER = "Chris Schoenthal"
USERNAME = "imrhil327"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 125
DS_PAGE = 126
LS_SCAN = "2012 Match Play Championship Day 1 Chris Schoenthal LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Schoenthal DS.png"
LS_DECK_NAME = "I Must Edit: Female"
DS_DECK_NAME = "Does Wayne Brady..."
NOTE = "Handwritten 2010 Xerox form. Username imrhil327."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Schoenthal dested Chris Schoenthal. "
    "Username imrhil327. LIGHT checked. Deck Name I have to Choose A Bitch? crossed, "
    "I Must Edit: Female dest replacement. Event Date 2/11/12 Event Name 2012 MPC. "
    "Line 1 remnant WYS dested Watch Your Step / This Place Can Be A Little Rough empty. "
    "Tatooine (E1) dested Tatooine analog TMW. Ditto Docking Bay 94 dested Tatooine: Docking Bay 94. "
    "Ant Man & The Power Converters dested Antilles Maneuver & Rebel Reinforcements analog HT. "
    "Cliegg dested Cliegg Lars. BoShek's Mad Freighter dested as written analog 2013 Alderaan. "
    "Line 38 blank skipped. Line 40 remnant Han w/ Heavy Pistol dested Han With Heavy Blaster Pistol. "
    "Morex Tarik dested Mirax Terrik. Rayce Ryioda dested Rayce analog 2013 Alderaan. "
    "AFA True dested in the 60 analog Casey. HFTMF empty dested in the 60 analog Casey. "
    "Houjix True AND empty kept separate analog Foth. Sabotage True x2. "
    "Escape Pod True AND empty kept separate. Chewbacca True AND empty kept separate. "
    "Luke Skywalker True AND empty kept separate. Melas True x2. "
    "Do not copy 2013 Alderaan WYS / 2014 TMW Communing dests. Unique 59. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Schoenthal dested Chris Schoenthal. "
    "Username imrhil327. DARK checked. Deck Name Does Wayne Brady... "
    "Event Date 2/11/12 Event Name 2012 MPC. "
    "Hunt Down True dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "Coruscant (SE) dested Coruscant analog Howland. Energy Shield dested Endor Shield True analog Richards. "
    "Gift Of The Magi dested as written. Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog Anis. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber analog Harpster. "
    "Trophy of A Kill dested Trophy Of A Kill as written. Guri's Fighter dested Stinger. "
    "Line 40 remnant ditto dested Galen, Secret Apprentice x3 with line 52. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x3 analog Casey. "
    "Black Leader dested Juno Eclipse, Black Leader analog Eier. "
    "4-LOM True AND empty kept separate analog Foth. Force Field True AND empty kept separate. "
    "Coruscant empty AND True kept separate. Prepared Defenses True dested in the 60 analog Pistone. "
    "K&D True dested in the 60 analog Murray. Shield The Power dested Firepower True analog Richards. "
    "Do not copy 2013 Alderaan ROPS / 2014 TMW ASM dests. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Get To Your Ships!"),
    n("I Must Be Allowed To Speak"),
    n("Houjix", True),
    n("Heading For The Medical Frigate"),
    n("Hindsight", True),
    n("Sabotage", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Imperial Atrocity", True),
    n("Menace Fades"),
    n("Scrambled Transmission", True),
    n("Seeking An Audience", True),
    n("K'lor'slug", True),
    n("Moving To Attack Position", qty=2),
    n("Blast The Door, Kid!"),
    n("It's A Hit!"),
    n("Control & Tunnel Vision"),
    n("Wookiee Strangle", True),
    n("Inconsequential Barriers"),
    n("Cliegg Lars", qty=2),
    n("Houjix"),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Pulsar Skate"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("BoShek's Mad Freighter"),
    n("Outrider"),
    n("Millennium Falcon"),
    n("Han With Heavy Blaster Pistol"),
    n("Sergeant Dolleyn", True),
    n("BoShek, Brash Smuggler"),
    n("Mirax Terrik"),
    n("Wedge Antilles", True),
    n("Talon Karrde", qty=2),
    n("Chewbacca", True),
    n("Chewbacca"),
    n("Melas", True, qty=2),
    n("Han Solo, Courageous Smuggler", qty=2),
    n("Luke Skywalker", True),
    n("Luke Skywalker"),
    n("Bespin"),
    n("Corellia", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Dash Rendar"),
    n("Rayce", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Aim High"),
    n("A Tragedy Has Occurred", True),
    n("Your Insight Serves You Well", True),
    n("Battle Plan", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("A Sith's Plans"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Gift Of The Magi"),
    n("Blockade Flagship: Hallway"),
    n("Grand Admiral Thrawn"),
    n("Emperor Palpatine", qty=2),
    n("Force Push", True),
    n("Sniper & Dark Strike"),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Lightning"),
    n("Elis Helrot"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Force Field", True),
    n("Force Field"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ghhhk"),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("Revenge Of The Sith"),
    n("No Escape"),
    n("Blast Door Controls"),
    n("Grievous' Lightsabers"),
    n("Galen's Lightsaber"),
    n("Vader's Lightsaber"),
    n("Trophy Of A Kill", qty=2),
    n("Victory", qty=2),
    n("Stinger"),
    n("Naboo: Theed Palace Throne Room"),
    n("Blockade Flagship: Bridge"),
    n("Endor"),
    n("Galen, Secret Apprentice", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Battle Droid Squad", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Mara Jade With Lightsaber"),
    n("4-LOM With Concussion Rifle"),
    n("Coruscant", True),
    n("Juno Eclipse, Black Leader"),
    n("General Veers"),
    n("Dengar With Blaster Carbine", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
