#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Tom Frafjord.

Source: 2012NationalsDay1.pdf pages 19–20 (handwritten 2010 Xerox, 12 shields).
Name Tom Frafjord dested Tom Frafjord analog leftover 2008 Worlds. Username citizenSwanky.
p19 Dark Save Me Greebus! / A Stunning Move.
p20 Light Don't order 66 Me Bro! / We'll Handle This.
Do not dest as a new person. Do not dest as Peter Grouty.
"""
from __future__ import annotations

PLAYER = "Tom Frafjord"
USERNAME = "citizenSwanky"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 20
DS_PAGE = 19
LS_SCAN = "2012 US Nationals Day 1 Tom Frafjord LS.png"
DS_SCAN = "2012 US Nationals Day 1 Tom Frafjord DS.png"
LS_DECK_NAME = "Don't order 66 Me Bro!"
DS_DECK_NAME = "Save Me Greebus!"
NOTE = "Handwritten 2010 Xerox form. Username citizenSwanky. Event Date 06/09/12 Event Name Nationals."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Tom Frafjord dested Tom Frafjord analog leftover 2008 Worlds. "
    "Username citizenSwanky. LIGHT checked. Deck Name Don't order 66 Me Bro!. "
    "Event Date 06/09/12 Event Name Nationals. Do not dest as a new person. Do not dest as Peter Grouty. "
    "We'll Handle This dested We'll Handle This / Duel Of The Fates True analog leftover Consoli. "
    "Yoda dested Yoda, Senior Council Member analog leftover. "
    "Qui-Gon dested Qui-Gon Jinn With Lightsaber analog leftover. "
    "I Hope She's Alright dested I Hope She's All Right analog leftover Murray. "
    "Sense's Recoil In Fear dested Sense & Recoil In Fear analog leftover combo. "
    "Woooo dested Wookiee Roar True analog leftover Gemme. "
    "Are You Brain Dead dested Are You Brain Dead? analog leftover Marlow. "
    "Hear Me Baby dested Hear Me Baby, Hold Together analog leftover Dubreuil. "
    "Out Of Commission dested leftover_xerox. "
    "We Gotta Grand Army dested Wesa Gotta Grand Army analog leftover. "
    "A Jedi's Resilience dested analog leftover Anderson. "
    "Anger Fear dested Anger, Fear, Aggression analog leftover Bali. "
    "Shield Another Pathetic dested Another Pathetic Lifeform analog leftover Amato. "
    "Shield Only Jedi dested Only Jedi Carry That Weapon analog leftover. "
    "True vs empty kept separate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Tom Frafjord dested Tom Frafjord analog leftover 2008 Worlds. "
    "Username citizenSwanky. DARK checked. Deck Name Save Me Greebus!. "
    "Event Date 06/09/12 Event Name Nationals. Do not dest as a new person. Do not dest as Peter Grouty. "
    "A Stunning Move dested A Stunning Move / A Valuable Hostage empty analog leftover Consoli. "
    "Ni Chuba-Na dested Ni Chuba Na?? True analog leftover Anderson. "
    "Cyborg Commander HoJ dested Grievous, Hunter Of Jedi analog leftover walker. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard analog leftover walker. "
    "Mandalorian Father dested Jango Fett, The Assassin analog leftover. "
    "Boba Fett in Slave I dested Boba Fett In Slave I analog leftover Bordier. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover Hilbun. "
    "Imbalance dested Imbalance & Kintan Strider analog leftover Consoli. "
    "Oh Switch Off dested Oh, Switch Off analog leftover Erwin. "
    "Something Special dested Something Special Planned For Them analog leftover Wirfs. "
    "Masterful Move dested Masterful Move & Endor Occupation analog leftover Marlow. "
    "Lightsaber Deficiency dested analog leftover Jan. "
    "Operational As Planned dested analog leftover Ziagos. "
    "Galen's Lightsaber dested Galen's Lightsaber, Vader's Gift analog leftover Ziagos. "
    "Knowledge dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "D-59 dested P-59 analog leftover Skilton. "
    "Establish Control dested analog leftover Kessling. "
    "True vs empty kept separate. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("The Signal", True),
    n("A Jedi's Plans"),
    n("Your Insight Serves You Well"),
    n("Honor Of The Jedi"),
    n("Coruscant: Jedi Archives"),
    n("Coruscant: Night Club"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yoda, Senior Council Member", True),
    n("Plo Koon"),
    n("Depa Billaba"),
    n("Jedi Advisor", qty=3),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Fallen Jedi", qty=2),
    n("Ki-Adi-Mundi", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Elegant Lightsaber", qty=2),
    n("Jedi Lightsaber", True),
    n("I Hope She's All Right"),
    n("Quick Draw", True),
    n("Menace Fades"),
    n("Scrambled Transmission", True),
    n("Projection Of A Skywalker"),
    n("Strike Force", True),
    n("Imperial Atrocity", True, qty=3),
    n("Sense & Recoil In Fear"),
    n("Sense", qty=2),
    n("Alter", True),
    n("Smoke Screen", qty=3),
    n("Blaster Deflection", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Speak With The Jedi Council", qty=3),
    n("Are You Brain Dead?", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Wookiee Roar", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Wesa Gotta Grand Army"),
    n("A Jedi's Resilience", qty=2),
    n("Escape Pod", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Another Pathetic Lifeform", True),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Establish Control", True),
    n("Ni Chuba Na??", True),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Death Star: War Room"),
    n("Corulag", True),
    n("Victory"),
    n("Blockade Support Ship"),
    n("Boba Fett In Slave I", True),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Darth Maul"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Jango Fett, The Assassin"),
    n("4-LOM With Concussion Rifle", True),
    n("IG-100 MagnaGuard", True),
    n("P-59"),
    n("Probot"),
    n("Dark Jedi Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Search And Destroy"),
    n("Imperial Decree", True),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("The Phantom Menace", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("You Are Beaten"),
    n("Imbalance & Kintan Strider"),
    n("Coruscant Detention", True),
    n("Force Field", True, qty=2),
    n("Sith Fury", True),
    n("Weapon Levitation"),
    n("Operational As Planned", True),
    n("Force Push", True),
    n("Cold Feet", True),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Oh, Switch Off"),
    n("Stop Motion", True, qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("A Useless Gesture"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
