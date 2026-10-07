#!/usr/bin/env python3
"""2012 US Nationals Day 2 leftover Xerox: Angelo Consoli.

Source: 2012NationalsDay2.pdf pages 1–2 (typed Light 2010 Xerox / handwritten Dark Same as Yesterday).
Name Angelo Consoli dested Angelo Consoli analog leftover Day 1 / 2013 Worlds CANON.
Username GravityShadow.
p01 Light Mind What You Have Learned. Worlds 2011 form reused dest 2012 Nats Day 2.
p02 Dark Same as Yesterday with In/Out from Day 1 A Stunning Move.
Do not dest as a new person. Do not dest Day 1 Consoli 60s again.
"""
from __future__ import annotations

PLAYER = "Angelo Consoli"
USERNAME = "GravityShadow"
STAGE = "Day 2"
PDF = "2012 US Nationals Day 2.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2012 US Nationals Day 2 Angelo Consoli LS.png"
DS_SCAN = "2012 US Nationals Day 2 Angelo Consoli DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p01 typed 2010 Xerox Light MWYHL. Worlds 2011 form reused dest 2012 Nats Day 2. "
    "p02 handwritten Dark Same as Yesterday with In/Out from Day 1 A Stunning Move. "
    "Username GravityShadow. LIGHT/DARK empty on p02 dest from filled 60s / Deck Name ASM. "
    "Do not dest as a new person."
)
PUBLIC_NOTE = ""
LS_NOTE = (
    "Typed 2010 Xerox. Name Angelo Consoli dested Angelo Consoli analog leftover Day 1. "
    "Username GravityShadow. LIGHT checked. Event Name Worlds 2011 crossed dest 2012 Nats Day 2. "
    "Mind What You Have Learned True dested Mind What You Have Learned / Save You It Can True analog leftover McCune. "
    "Anger, Fear, Aggression True dested analog leftover McCune IN THE 60. "
    "Strong Is Vader True dested dest-as-written leftover_xerox. "
    "It Is The Future You See True dested analog leftover pistone IN THE 60. "
    "Battle Plan & Draw Their Fire dested analog leftover. "
    "Do, Or Do Not & Wise Advice dested analog leftover. "
    "Thrown Back True dested analog leftover. "
    "Coruscant (Special Edition) dested Coruscant analog leftover. "
    "Mace Windu, Master of the Order True dested Mace Windu, Master Of The Order True analog leftover Consoli Day 1. "
    "Luke Skywalker, Jedi Knight dested analog leftover Jake Nelson x2. "
    "Fallen Jedi True dested analog leftover Consoli Day 1. "
    "Admiral Ackbar True dested analog leftover Fernando. "
    "Captain Hanack crossed dested Major Haash'n analog leftover Cooleo. "
    "Han, Chewie And The Falcon True dested analog leftover. "
    "Artoo Detoo In Red 5 dested Artoo-Detoo In Red 5 analog leftover McCune. "
    "Civil Disorder True / Quick Draw True dested analog leftover Consoli Day 1. "
    "Projection Of A Skywalker True dested analog leftover McCune. "
    "Hear Me Baby, Hold Together True dested analog leftover Frafjord. "
    "Sorry About The Mess & Blaster Proficiency dested analog leftover Consoli Day 1. "
    "Impressive, Most Impressive crossed dested Hindsight True analog leftover Consoli Day 1. "
    "Out Of Commission & Transmission Terminated crossed dested Rebel Leadership True analog leftover. "
    "Antilles Maneuver & Rebel Reinforcements True dested analog leftover McCune. "
    "Jabba's Prize crossed dested Weapons Display True analog leftover. "
    "Another Pathetic Lifeform crossed dested Battle Plan True analog leftover. "
    "He Can Go About His Business crossed dested Yavin Sentry True analog leftover. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred analog leftover. "
    "Margin Jabba's Prize True dested extra shield unique 13 sheet-accurate analog leftover Consoli Day 1 shields 13. "
    "Unique 60. Shields 13."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Angelo Consoli dested Angelo Consoli analog leftover Day 1. "
    "Username GravityShadow. LIGHT/DARK empty dest from filled 60s / Deck Name ASM. "
    "Same as Yesterday dested Day 1 A Stunning Move / A Valuable Hostage analog leftover pistone In/Out. "
    "OUT Disarmed, They're Still Coming Through, There Is No Try shield analog leftover Day 1 lines. "
    "IN Search And Destroy dested analog leftover Anderson. "
    "IN Operational As Planned True already in Day 1 keep. "
    "IN Oppressive Enforcement dested analog leftover Finley shield. "
    "Virtual-only objective dest without extra (V). Unique sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Anger, Fear, Aggression", True),
    n("Dagobah"),
    n("Strong Is Vader", True),
    n("It Is The Future You See", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Thrown Back", True),
    n("Dagobah: Bog Clearing"),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Home One: War Room"),
    n("Coruscant"),
    n("Yoda", True),
    n("Daughter Of Skywalker", True),
    n("Mace Windu, Master Of The Order", True),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Fallen Jedi", True),
    n("Admiral Ackbar", True),
    n("Major Haash'n"),
    n("Home One"),
    n("Han, Chewie And The Falcon", True),
    n("Bravo Fighter", True),
    n("Artoo-Detoo In Red 5"),
    n("Elegant Lightsaber", True, qty=2),
    n("Luke's Bionic Hand", True, qty=2),
    n("Luke's Backpack"),
    n("Civil Disorder", True),
    n("Quick Draw", True),
    n("The Way Of Things"),
    n("Imperial Atrocity", True),
    n("Reflection", True),
    n("Yoda's Hope"),
    n("Projection Of A Skywalker", True),
    n("Krayt Dragon Howl & Armed And Dangerous", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers"),
    n("Control & Tunnel Vision"),
    n("Hindsight", True),
    n("Jedi Levitation"),
    n("Alternatives To Fighting"),
    n("Courage Of A Skywalker", True),
    n("It's A Trap!"),
    n("Grimtaash"),
    n("Under Attack"),
    n("Escape Pod", True),
    n("Collision"),
    n("It Could Be Worse"),
    n("On The Edge"),
    n("Dodge"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Battle Plan", True),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("Yavin Sentry", True),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Jabba's Prize", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Coruscant: Palpatine's Quarters"),
    n("Knowledge And Defense", True),
    n("Oh, Switch Off"),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Operational As Planned", True),
    n("Force Push", True),
    n("Elis Helrot"),
    n("Force Field", True, qty=2),
    n("Weapon Levitation & The Empire's Back"),
    n("Imperial Barrier"),
    n("Imbalance & Kintan Strider"),
    n("A Dark Time For The Rebellion", True),
    n("You Are Beaten"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Control"),
    n("Sniper & Dark Strike"),
    n("The Phantom Menace"),
    n("Protocol Failure"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("First Strike"),
    n("Nal Hutta"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship"),
    n("Victory"),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Battle Droid Squad", qty=2),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Darth Maul"),
    n("Galen, Secret Apprentice", qty=2),
    n("AP-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("OOM-9", True),
    n("IG-100 MagnaGuard"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("Jabba's Haven"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Prepared Defenses", True),
    n("Insidious Prisoner"),
    n("Imperial Justice", True),
    n("Search And Destroy"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
