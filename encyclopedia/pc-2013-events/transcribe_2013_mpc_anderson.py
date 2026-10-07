#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: John Anderson Xerox LS+DS."""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "puck71"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2013 Match Play Championship p06 John Anderson LS.png"
DS_SCAN = "2013 Match Play Championship p05 John Anderson DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username puck71. Event MPC Day 1, dated 1/26/13. "
    "Deck title Revolution 2. Light. MWYHL → Mind What You Have Learned / Save You It Can "
    "(7-side Save You It Can). "
    "IITFYS (V) in the 60 is the Epic Event; Additional Cards IITFYS is the Jedi Test. "
    "Battle Plan + Draw Their Fire as written. "
    "Do, Or Do Not + Wise Advice as written. Strong Is Vader as written. "
    "Line 14 struck, Bravo Fighter (V). Line 22 struck, Under Attack. "
    "Found Someone You Have + Higher Ground as written. "
    "Antilles Maneuver + Rebel Reinforcements as written. "
    "Jedi Tests listed under Additional Cards. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username puck71. Event MPC Day 1, dated 1/26/13. "
    "Deck title Revolution 1. Dark. Starting location Kessel: Spice Mines Administrator's Office. "
    "Combat Response as written. Line 29 Baron Soontir Fel. "
    "Black Leader dested DS-61-4. Obsidian 10 dested OS-72-10. "
    "Line 11 struck rewrite dested Maul's Double-Bladed Lightsaber. "
    "Line 55 Phantom Menace struck no (V). Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Dagobah"),
    n("It Is The Future You See", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Thrown Back", True),
    n("Strong Is Vader"),
    n("Artoo-Detoo In Red 5"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke's Bionic Hand", qty=2),
    n("Yoda", True),
    n("Bravo 2", True),
    n("Quick Draw", True),
    n("Imperial Atrocity", True),
    n("Home One: War Room"),
    n("Rebel Leadership", True, qty=3),
    n("Dagobah: Bog Clearing"),
    n("Under Attack"),
    n("Han, Chewie, And The Falcon", True),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Admiral Ackbar", True),
    n("Projection Of A Skywalker"),
    n("Home One"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers"),
    n("Daughter Of Skywalker", True),
    n("Yoda's Hope"),
    n("Luke's Backpack"),
    n("Reflection", True),
    n("Armed And Dangerous & Krayt Dragon Howl", qty=2),
    n("Alternatives To Fighting"),
    n("Corran Horn"),
    n("Elegant Lightsaber", qty=2),
    n("Escape Pod", True),
    n("It Could Be Worse"),
    n("Houjix"),
    n("Dodge"),
    n("The Way Of Things"),
    n("It's A Trap!"),
    n("Mace Windu, Master Of The Order"),
    n("On The Edge"),
    n("Courage Of A Skywalker", True),
    n("Weapon Levitation"),
    n("Hear Me Baby, Hold Together", True),
    n("Collision!"),
    n("Kiffex"),
    n("Inconsequential Barriers"),
    n("Found Someone You Have & Higher Ground"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Obi-Wan Kenobi", True),
    n("Master Qui-Gon", True),
    n("Fallen Jedi"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Planetary Defenses", True),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel: Spice Mines - Administrator's Office"),
    n("According To My Design"),
    n("Emperor Palpatine"),
    n("I'll Take Them Myself"),
    n("I'm Sorry", True),
    n("Combat Response"),
    n("You Are Beaten"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Force Field", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Image Of The Dark Lord", True),
    n("Protocol Failure", qty=2),
    n("Force Lightning"),
    n("Atmospheric Assault", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Darth Vader With Lightsaber"),
    n("Spice Mine Operations"),
    n("Saber 1"),
    n("DS-61-3"),
    n("Dark Maneuvers & Tallon Roll", qty=2),
    n("Black 3", True),
    n("DS-61-4"),
    n("Imperial Barrier"),
    n("Baron Soontir Fel"),
    n("Ghhhk"),
    n("A Dark Time For The Rebellion", True),
    n("Desperate Counter", True),
    n("Black 1"),
    n("DS-61-5"),
    n("Kessel"),
    n("All Power To Weapons", qty=3),
    n("Black 5"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Limited Resources"),
    n("Black 2", True),
    n("DS-61-2"),
    n("Clouds"),
    n("Arica"),
    n("Kessel Surveillance System"),
    n("Where Are You Taking This Thing?"),
    n("Storm Clouds"),
    n("Spice Mine Administrator"),
    n("Something Special Planned For Them", True),
    n("Imperial Propaganda", True),
    n("The Phantom Menace"),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("OS-72-10"),
    n("OS-72-10", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Resistance"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Abyss", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
]
DS_ADD = []
