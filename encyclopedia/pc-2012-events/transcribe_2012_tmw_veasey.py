#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: John Veasey.

Source: 2012TMWDay1.pdf pages 21–23 (typed GEMP dump, not a handwritten Xerox
form). Handwritten Veez dested John Veasey analog leftover 2012 Nats/MPC /
generate CANON / pages/John_Veasey.wiki. Username veez analog leftover 2012
Nats. p21 Light Wooks. p22–p23 Dark Droids. Do not dest as a new person.
Do not dest as Veez as a new person. Do not dest 2012 Nats / 2012 MPC Veasey
60s again.
"""
from __future__ import annotations

PLAYER = "John Veasey"
USERNAME = "veez"
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 21
DS_PAGE = 23
LS_SCAN = "2012 Texas Mini Worlds Day 1 John Veasey LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 John Veasey DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed GEMP dump p21 Light / p22–p23 Dark. "
    "Handwritten Veez dested John Veasey analog leftover 2012 Nats. "
    "Username veez analog leftover 2012 Nats. Do not dest as a new person. "
    "Do not dest 2012 Nats / 2012 MPC Veasey 60s again."
)
LS_NOTE = (
    "Typed GEMP dump p21 Light Wooks. Handwritten Veez dested John Veasey analog leftover 2012 Nats. "
    "Username veez analog leftover 2012 Nats. Do not dest as a new person. Do not dest as Veez as a new person. "
    "(1 starting) dested LS_SHIELDS 12 analog leftover Nats Veasey. "
    "The Professor True crossed dest replacement Your Insight Serves You Well True analog leftover. "
    "Nabrun Leids in the shield block dest unique 60 analog leftover extra written line. "
    "Wookiee True x8 dest Wookiee analog leftover. "
    "Kashyyyk: Wookiee Haven (Forest) dested Kashyyyk: Wookiee Haven analog leftover. "
    "Commando Training & K'lor'slug dested analog leftover Hendon. "
    "Anger, Fear, Aggression True dested analog leftover Kirkpatrick start. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump p22–p23 Dark Droids. Handwritten Veez dested John Veasey analog leftover 2012 Nats. "
    "Username veez analog leftover 2012 Nats. Do not dest as a new person. "
    "A Stunning Move/A Valuable Hostage dested A Stunning Move analog leftover Anderson virtual-only. "
    "Knowledge And Defense True dested analog leftover Anderson True IN THE 60. "
    "Coruscant: Private Platform (Docking Bay) dested Coruscant: Private Platform analog leftover Kirkpatrick. "
    "IG Bodyguard droid dested IG-Bodyguard Droid analog leftover Kirkpatrick qty=2. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi analog leftover Hendon qty=2. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Hendon. "
    "The Phantom Menace (AI) dested The Phantom Menace analog leftover Kirkpatrick. "
    "U-3PO (Yoo-Threepio) dested U-3PO analog leftover Lush. "
    "Force Push True handwritten dested analog leftover Hendon True. "
    "Something Special Planned For Them handwritten dested analog leftover Kirkpatrick True. "
    "Imbalance & Kintan Strider dested analog leftover Kirkpatrick. "
    "Masterful Move & Endor Occupation dested analog leftover Kirkpatrick. "
    "Unique 61 sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Kashyyyk", True),
    n("Protector", True),
    n("Kashyyyk: Forest Depths"),
    n("Grrrghrrrgh!"),
    n("Declaration Of Rebellion"),
    n("Launching The Assault"),
    n("Kashyyyk: Sacred Forest"),
    n("Kashyyyk: Wookiee Haven"),
    n("Home One: War Room"),
    n("Home One"),
    n("Chewbacca", True),
    n("Chewbacca Of Kashyyyk", True, qty=2),
    n("Yarua", True, qty=2),
    n("Kashyyyk Insurgent Leader", qty=2),
    n("Blind Jedi", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Princess Leia", True),
    n("Luke Skywalker", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("Padme Naberrie", True),
    n("Wookiee", True, qty=8),
    n("Commando Training & K'lor'slug"),
    n("Menace Fades"),
    n("Bargaining Table", qty=2),
    n("I Hope She's All Right"),
    n("Imperial Atrocity", True),
    n("Let's Go Left", True),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Might Of The Republic", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Nar Shaddaa Wind Chimes"),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("Wookiee Strangle", True),
    n("Wookiee Guide", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("We Wish To Board At Once"),
    n("Nabrun Leids"),
    n("Hindsight", True),
    n("Admiral Ackbar", True),
    n("Honor Of The Jedi"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("A Stunning Move"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Insidious Prisoner"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("3,720 To 1", True),
    n("Jabba's Haven"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Nal Hutta"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Grievous' Lightsabers"),
    n("Galen, Secret Apprentice", qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Aurra Sing", True),
    n("Dengar With Blaster Carbine", True),
    n("4-LOM With Concussion Rifle", True),
    n("P-59"),
    n("P-60"),
    n("Battle Droid Squad", qty=2),
    n("IG-Bodyguard Droid", qty=2),
    n("Force Push", True),
    n("Something Special Planned For Them", True),
    n("U-3PO"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Dark Jedi Lightsaber", True),
    n("Blaster Rack", True),
    n("The Phantom Menace"),
    n("No Escape"),
    n("Imperial Propaganda", True),
    n("Victory"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Tarkin's Bounty", True),
    n("Force Field", True),
    n("Oh, Switch Off", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk"),
    n("Stunning Leader"),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control & Set For Stun"),
    n("Sniper & Dark Strike"),
    n("Imbalance & Kintan Strider"),
    n("Sith Fury", True),
    n("Forced Servitude"),
    n("Brangus Glee", True),
    n("Garindan", True),
    n("Self-Destruct Mechanism"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Abyss", True),
]
DS_ADD = []
