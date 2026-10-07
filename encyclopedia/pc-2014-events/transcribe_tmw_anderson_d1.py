#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: John Anderson.

Source: 2014-TMW-Day-1.pdf pages 21–22 (2013 form).
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2014 Texas Mini Worlds Day 1 p21 John Anderson LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p22 John Anderson DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name John Anderson. Username blank. LIGHT checked. Event TMW 2014. "
    "Republic At War empty dested Republic At War / A Precarious Predicament. "
    "Do not dest as a new person. Do not rewrite 2013 Worlds Anderson leftover "
    "or 2013 TMW Anderson leftover. "
    "Your Ship dested Your Ship?. "
    "Unique overcounts sheet-accurate (It's Not My Fault! x3, Dual Laser Cannon x4, AT-RT x9). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name John Anderson. Username blank. DARK checked. Event TMW 2014. "
    "Wookiee Slaving Operation empty dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Imbalance & Kintan Stricer dested Imbalance & Kintan Strider. "
    "P-59 dested P-59. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Unique overcounts sheet-accurate (Sonic Bombardment x3, Outer Rim Scout x4). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / A Precarious Predicament"
LS_CARDS = [
    n("Republic At War / A Precarious Predicament"),
    n("Geonosis: Forward Command Center"),
    n("Begun, The Clone War Has"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Nick Of Time", True),
    n("Rogue Squadron Tactics"),
    n("Desperate Tactics", qty=2),
    n("Rebel Artillery"),
    n("Let The Wookiee Win", True, qty=2),
    n("It's Not My Fault!", True, qty=3),
    n("Lucky Shot", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Rebel Barrier"),
    n("Lucky Shot"),
    n("Dark Approach", True),
    n("Houjix"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Fixer"),
    n("Chewbacca, Walking Carpet"),
    n("Plo Koon", True),
    n("Clone Pilot"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Han Solo, Innocent Scoundrel"),
    n("Jaina Solo"),
    n("Anakin Solo"),
    n("Seeking An Audience", True),
    n("Crash Site Memorial"),
    n("Imperial Atrocity", True),
    n("Lady Luck"),
    n("Acclamator-Class Assault Ship", qty=2),
    n("Alderaan Consular Ship"),
    n("Rebel Cell - Hidden Landing Site"),
    n("Muunilinst: Republic Landing Site"),
    n("Muunilinst: City Of Harnaidan"),
    n("Muunilinst: Harnaidan Plains"),
    n("Dressel"),
    n("Dual Laser Cannon", True, qty=4),
    n("AT-RT", qty=9),
    n("Assault On Muunilinst"),
    n("Hear Me Baby, Hold Together", True),
    n("Escape Pod", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("He Can Go About His Business"),
    n("Your Ship?"),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Jabba's Haven"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Velken Tezeri", True),
    n("Nal Hutta"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Mercenary Pilot", True),
    n("Imbalance & Kintan Strider"),
    n("Jabba The Hutt", True),
    n("Stop Motion", True),
    n("Jabba's Space Cruiser", True),
    n("P-59"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("4-LOM With Concussion Rifle"),
    n("He Hasn't Come Back Yet"),
    n("Probot"),
    n("Garindan", True),
    n("Ephant Mon"),
    n("Mara Jade With Lightsaber"),
    n("Dengar With Blaster Carbine", True),
    n("Scum And Villainy"),
    n("Hutt Bounty", True),
    n("Tarkin's Orders"),
    n("Slave I, Symbol Of Fear"),
    n("IG-88, Renegade Droid"),
    n("Outer Rim Scout"),
    n("Jabba's Sail Barge", True),
    n("Ponda Baba", True),
    n("Cold Feet", True),
    n("Outer Rim Scout"),
    n("Scum And Villainy"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Boba Fett, Prepared Hunter"),
    n("Defensive Fire & Hutt Smooch"),
    n("Outer Rim Scout"),
    n("Sneak Attack", True),
    n("Sonic Bombardment", True),
    n("Maul's Sith Infiltrator"),
    n("Outer Rim Scout"),
    n("Jango Fett, The Assassin"),
    n("Prince Xizor"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Kashyyyk: Skyhook Platform"),
    n("Sonic Bombardment", True),
    n("Something Special Planned For Them", True),
    n("Bossk", True),
    n("Sonic Bombardment", True),
    n("Close Call", True),
    n("Ability, Ability, Ability", True),
    n("Protocol Failure"),
    n("Lightsaber Deficiency", True, qty=2),
    n("OOM-9", True),
    n("Cease Fire"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("Abyss", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Death Star Sentry", True),
]
DS_ADD = []
