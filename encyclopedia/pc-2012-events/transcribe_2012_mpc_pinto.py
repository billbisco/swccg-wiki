#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Joe Pinto.

Source: 2012mpcday1.pdf pages 119–120.
p119 typed GEMP dump Light Yavin 4 (V). p120 typed GEMP dump Dark Spice Mine Operations.
Name Joe Pinto dested Joe Pinto (existing stub). Username blank.
Pack player-stubs/Joe_Pinto.wiki.
Do not dest as a new person. Do not rewrite 2013 leftovers
(2013 PLAYER Joe Pinto LS Plead My Case To The Senate / DS Carbon Chamber Testing).
"""
from __future__ import annotations

PLAYER = "Joe Pinto"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 119
DS_PAGE = 120
LS_SCAN = "2012 Match Play Championship Day 1 Joe Pinto LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Joe Pinto DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "p119 typed GEMP dump Yavin 4; p120 typed GEMP dump Spice Mine Operations. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Name Joe Pinto dested Joe Pinto. "
    "Username blank. Deck Name blank (New Text Document is Notepad). "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "yavin 4 v dested Yavin 4 True starting location analog Herold. "
    "tatooine ep1 dested Tatooine (Coruscant) analog Cullen. "
    "AFA v dested Anger, Fear, Aggression True in the 60 analog Casey. "
    "luke trust me v dested Luke, Trust Me without True no (V) reprint. "
    "haven dested Haven. massassi base sentry v dested Massassi Base Sentry in the 60. "
    "Restore freedom v dested Restore Freedom To The Galaxy without True virtual-only. "
    "screaming lando dested Lando With Blaster Rifle x2. "
    "leia rp dested Leia, Rebel Princess. "
    "wedge in rs1 v dested Wedge In Red Squadron 1 without True analog Kelly. "
    "booster in pulsar skate v dested Booster In Pulsar Skate without True virtual-only. "
    "alter ep 1 v dested Alter (V). "
    "satm/blaster pro dested Sorry About The Mess & Blaster Proficiency. "
    "it's not my fault v dested It's Not My Fault! True x2 analog Herold. "
    "Aim High True dested Aim High without True analog Graham. Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump. Name Joe Pinto dested Joe Pinto. "
    "Username blank. Deck Name blank (New Text Document (2) is Notepad). "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "K&D v dested Knowledge And Defense True in the 60 analog Murray. "
    "spice mine operations v dested Spice Mine Operations without True virtual-only. "
    "he is not ready/imperial prop v dested He Is Not Ready & Imperial Propaganda analog Montgomery. "
    "grotto v dested Grotto Werribee True. "
    "admiral pellaeon v dested Admiral Pellaeon as written. "
    "spice mine admin v dested Spice Mine Administrator analog Harpster. "
    "punishing one v dested Punishing One True. "
    "kessel surv system v dested Kessel Surveillance System. "
    "short range/watch back dested Short Range Fighters & Watch Your Back! x2. "
    "imbalance/kintan strider v dested Imbalance & Kintan Strider. "
    "ghhhk/rebels wont escape dested Ghhhk & Those Rebels Won't Escape Us analog Hilbun. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Tatooine (Coruscant)"),
    n("Hoth"),
    n("Yavin 4: Docking Bay"),
    n("Yavin 4: Massassi Headquarters"),
    n("Yavin 4: Briefing Room"),
    n("Yavin 4: Massassi War Room"),
    n("Cloud City: Lower Corridor"),
    n("Anger, Fear, Aggression", True),
    n("Evacuation Control", True),
    n("Special Modifications", True),
    n("Luke, Trust Me"),
    n("Draw Their Fire"),
    n("Demotion"),
    n("Haven"),
    n("Wokling", True),
    n("Your Insight Serves You Well"),
    n("Honor Of The Jedi"),
    n("Hindsight", True),
    n("Massassi Base Sentry"),
    n("Restore Freedom To The Galaxy"),
    n("Lando With Blaster Rifle", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Corran Horn"),
    n("Mirax Terrik"),
    n("Leia, Rebel Princess"),
    n("Wedge In Red Squadron 1"),
    n("Booster In Pulsar Skate"),
    n("Tantive IV", True),
    n("Bravo Fighter", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Gold Leader In Gold 1", True),
    n("Spiral"),
    n("Artoo-Detoo In Red 5"),
    n("Dark Approach", True),
    n("Sense", qty=2),
    n("Smoke Screen", qty=3),
    n("Control & Tunnel Vision"),
    n("Alter (V)"),
    n("Careful Planning", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("It's Not My Fault!", True, qty=2),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Inconsequential Barriers"),
    n("Weapon Levitation"),
    n("A Jedi's Resilience"),
    n("X-wing Laser Cannon"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Another Pathetic Lifeform"),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Protocol Failure"),
    n("Lateral Damage"),
    n("Presence Of The Force"),
    n("Endor Shield", True),
    n("Combat Response", True),
    n("I'll Take Them Myself"),
    n("Wipe Them Out, All Of Them"),
    n("General Veers", True),
    n("General Nevar"),
    n("Mara Jade With Lightsaber"),
    n("Grotto Werribee", True),
    n("Darth Maul With Lightsaber"),
    n("Admiral Pellaeon"),
    n("Darth Vader", True),
    n("Dengar", True),
    n("Guri"),
    n("4-LOM With Concussion Rifle"),
    n("Garindan", True),
    n("Spice Mine Administrator"),
    n("Baron Soontir Fel"),
    n("Punishing One", True),
    n("Justifier"),
    n("Vader's Personal Shuttle", True),
    n("Stinger", True),
    n("Saber 1"),
    n("Spice Mine Operations"),
    n("Kashyyyk"),
    n("Blockade Flagship: Bridge"),
    n("Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Cold Feet", True),
    n("Trample"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Why Didn't You Tell Me?", True),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("We Must Accelerate Our Plans"),
    n("A Dark Time For The Rebellion", True),
    n("Crash Landing"),
    n("Imperial Command", qty=2),
    n("Operational As Planned", True),
    n("Imbalance & Kintan Strider"),
    n("Lightsaber Deficiency", True),
    n("They're Still Coming Through!"),
    n("Masterful Move & Endor Occupation"),
    n("Combat Readiness", True),
    n("Close Call", True),
    n("Imperial Barrier"),
    n("Gravity Shadow"),
    n("Kessel Surveillance System"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Blizzard Scout 1", True),
    n("Battle Deployment", qty=2),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption"),
    n("Fanfare"),
    n("Firepower", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Leave Them To Me", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
