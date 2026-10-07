#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Mike Richards Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "m007agent"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 77
DS_PAGE = 78
LS_SCAN = "2013 Match Play Championship p77 Mike Richards LS.png"
DS_SCAN = "2013 Match Play Championship p78 Mike Richards DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Sheet name Michael Richards; canon Mike Richards. "
    "Username m007agent. Event MPC 2013, dated 1/26/13. Light. Deck title Thomas Whaley Love. "
    "MWYHL dested Mind What You Have Learned (V) / Save You It Can (V). "
    "IITFYS (V) in the 60 is the Epic Event; Additional Cards IITFYS is the Jedi Test. "
    "Strong is Under dested Strong Is Vader. "
    "Do or do Not & Wise Advice dested Do, Or Do Not & Wise Advice. "
    "Battle Plan & DTF dested Battle Plan & Draw Their Fire. "
    "Found Someone You Have & Huges Goal dested Found Someone You Have & Higher Ground. "
    "Alternatives to Fightly dested Alternatives To Fighting. Collision dested Collision!. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "If I could & worse dested It Could Be Worse. "
    "Armed And Dangerous & Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "Luke Skywalker, JK / Luke Jedi Knight dested Luke Skywalker, Jedi Knight. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "It's A trap dested It's A Trap!. "
    "Antilles Maneuver & Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Mace Windu, Master of the Force dested Mace Windu, Master Of The Order. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Sorry About The Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Jedi Tests listed under Additional Cards (prefer_sh False). "
    "Form left column reprints 37–38 on lines 39–40 are Luke's Bionic Hand and Clash Of Sabers. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Sheet name Michael Richards; canon Mike Richards. "
    "Username m007agent. Event MPC 2013, dated 1/26/13. Dark. Deck title Emil Whaley Love. "
    "Starting Kessel: Spice Mines - Administrator's Office; Combat Response. "
    "Combat Response as written (not Combat Readiness). "
    "Obsidian 10 kept as Obsidian 10 (OS-72-10 is the next line). "
    "I'll Take Them Myself dested I'll Take Them Myself. "
    "Darth Maul w/ Saber dested Darth Maul With Lightsaber. "
    "Mara Jade w/ Saber dested Mara Jade With Lightsaber. "
    "Tibanna Floating Refinery dested Tibanna Floating Refinery. "
    "U-3PO dested U-3PO (Yoo-Threepio). "
    "Black Leader dested DS-61-4. "
    "Darth Vader, Betrayer of the Jedi dested Darth Vader, Betrayer Of The Jedi. "
    "Dark Maneuvers & Tallon Roll dested Dark Maneuvers & Tallon Roll. "
    "Masterful Move & Endor Celebration dested Masterful Move & Endor Occupation. "
    "Image of the Dark Lord dested Image Of The Dark Lord. "
    "Short Range Fighters & WYB dested Short Range Fighters & Watch Your Back!. "
    "Kessel: Spice Mines Extraction dested Kessel: Spice Mines - Extraction Facility. "
    "Darth Vader w/ Saber dested Darth Vader With Lightsaber. "
    "Where Are You Taking This Thing dested Where Are You Taking This ... Thing?. "
    "Come Here You are Big Coward dested Come Here You Big Coward. "
    "We'll Let Fate Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Shield line 9 I Find Your Lack Of Faith Disturbing is fully crossed; omitted. "
    "Form left column reprints 37–38 on lines 39–40 are Clouds and Masterful Move & Endor Occupation. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned (V) / Save You It Can (V)"
LS_CARDS = [
    n("Mind What You Have Learned (V) / Save You It Can (V)", True),
    n("It Is The Future You See", True),
    n("Strong Is Vader", True),
    n("Thrown Back", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Dagobah"),
    n("Battle Plan & Draw Their Fire"),
    n("Under Attack"),
    n("Luke's Bionic Hand", True),
    n("Found Someone You Have & Higher Ground"),
    n("Home One: War Room"),
    n("Dagobah: Bog Clearing"),
    n("Alternatives To Fighting"),
    n("Collision!"),
    n("Yoda", True),
    n("Elegant Lightsaber"),
    n("Dodge"),
    n("Daughter Of Skywalker", True),
    n("Han, Chewie, And The Falcon", True),
    n("Coruscant"),
    n("Courage Of A Skywalker", True),
    n("It Could Be Worse"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Backpack"),
    n("Rebel Leadership", True),
    n("Imperial Atrocity", True),
    n("Corran Horn"),
    n("Master Qui-Gon"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Artoo-Detoo In Red 5"),
    n("Weapon Levitation"),
    n("Anger, Fear, Aggression", True),
    n("Lady Luck"),
    n("Admiral Ackbar", True),
    n("Elegant Lightsaber"),
    n("Luke's Bionic Hand"),
    n("Clash Of Sabers"),
    n("Luke Skywalker, Jedi Knight"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Houjix"),
    n("Escape Pod", True),
    n("Projection Of A Skywalker"),
    n("Dagobah: Yoda's Hut"),
    n("The Way Of Things"),
    n("On The Edge"),
    n("It's A Trap!"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Home One"),
    n("Yoda's Hope"),
    n("Mace Windu, Master Of The Order"),
    n("Maris Brood, Fallen Jedi"),
    n("Quick Draw", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Reflection", True),
    n("Obi-Wan Kenobi", True),
    n("Artoo-Detoo In Red 5"),
    n("Dagobah: Jungle"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]

DS_START = "Kessel: Spice Mines - Administrator's Office"
DS_CARDS = [
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Combat Response"),
    n("I'm Sorry", True),
    n("Obsidian 10", True),
    n("OS-72-10"),
    n("I'll Take Them Myself", True),
    n("According To My Design", True),
    n("Spice Mine Operations"),
    n("DS-61-3"),
    n("Something Special Planned For Them", True),
    n("Black 2", True),
    n("Darth Maul With Lightsaber"),
    n("Force Field", True),
    n("All Power To Weapons"),
    n("Mara Jade With Lightsaber", True),
    n("Atmospheric Assault", True),
    n("Tibanna Floating Refinery", True),
    n("U-3PO (Yoo-Threepio)"),
    n("All Power To Weapons", qty=3),
    n("Atmospheric Assault", True),
    n("Baron Soontir Fel"),
    n("You Are Beaten"),
    n("Knowledge And Defense", True),
    n("Where Are You Taking This ... Thing?"),
    n("Storm Clouds"),
    n("DS-61-5"),
    n("Imperial Propaganda", True),
    n("Black 5", True),
    n("Force Lightning"),
    n("DS-61-4"),
    n("Lightsaber Deficiency", True),
    n("Black 1", True),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Dark Maneuvers & Tallon Roll", qty=3),
    n("Clouds"),
    n("Masterful Move & Endor Occupation"),
    n("Emperor Palpatine"),
    n("Moruth Doole, Kessel Administrator", True),
    n("Image Of The Dark Lord", True),
    n("Protocol Failure"),
    n("A Dark Time For The Rebellion", True),
    n("Kessel Surveillance System", True),
    n("Darth Maul With Lightsaber"),
    n("Arica"),
    n("Saber 1"),
    n("Ghhhk"),
    n("Black 3", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Kessel"),
    n("Protocol Failure", True),
    n("Lightsaber Deficiency", True),
    n("DS-61-2"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("A Dark Time For The Rebellion", True),
    n("Darth Vader With Lightsaber"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Resistance"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = [
    n("A Useless Gesture", True),
]
