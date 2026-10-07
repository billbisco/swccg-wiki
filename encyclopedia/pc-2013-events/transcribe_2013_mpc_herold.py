#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Brian Herold informal LS+DS."""
from __future__ import annotations

PLAYER = "Brian Herold"
LS_USERNAME = "Rimmie Gergalibbler"
DS_USERNAME = "Jizzwailer's Wangzapper"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 43
DS_PAGE = 44
LS_SCAN = "2013 Match Play Championship p43 Brian Herold LS.png"
DS_SCAN = "2013 Match Play Championship p44 Brian Herold DS.png"
LS_NOTE = (
    "Informal handwritten list on a custom Obi-Wan overlay form (not a 2010 Xerox Print Form). "
    "Username Rimmie Gergalibbler. Event MPC, 26 January 2013. "
    "Deck title Maati Teu Was A Victim Of Inception. Light. "
    "Mind What You Have Learned / Save You It Can. "
    "Coruscant (SE) dested Coruscant. Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Major Hassh'n dested Major Haash'n. LSJK dested Luke Skywalker, Jedi Knight. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Control & TV dested Control & Tunnel Vision. Ant Man combo dested Antilles Maneuver & Rebel Reinforcements. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. "
    "YISYW dested Your Insight Serves You Well. He Can Go About His Business as written. "
    "Jedi Tests listed under Additional Cards. (V) from a written v / checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Informal handwritten list on a custom Obi-Wan overlay form (not a 2010 Xerox Print Form). "
    "Username Jizzwailer's Wangzapper. Event MPC, 26 January 2013. "
    "Deck title Ghostbusters captured the Zeitgeist. Dark. "
    "Starting location Kessel: Spice Mines - Administrator's Office. Combat Response. "
    "Tibanna Floating Platform dested Tibanna Floating Refinery. "
    "Obsidian 10 dested OS-72-10. Black Leader dested DS-61-4. "
    "Where Are U Taking This Thing dested Where Are You Taking This ... Thing?. "
    "Spice Mine Administrator dested Moruth Doole, Kessel Administrator. "
    "Maul / Vader / Mara w Saber dested the Enhanced Premiere printings. "
    "MM & EO dested Masterful Move & Endor Occupation. "
    "Short Range Fighters & WYB dested Short Range Fighters & Watch Your Back. "
    "Gesture dested A Useless Gesture. YCHF dested You Cannot Hide Forever. "
    "CHYBC dested Come Here You Big Coward. (V) from a written v / checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Dagobah"),
    n("Strong Is Vader"),
    n("It Is The Future You See", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Thrown Back", True),
    n("Dagobah: Bog Clearing"),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Home One: War Room"),
    n("Coruscant"),
    n("Yoda", True),
    n("Daughter Of Skywalker"),
    n("Maris Brood, Fallen Jedi"),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Admiral Ackbar"),
    n("Major Haash'n"),
    n("Corran Horn"),
    n("Mace Windu, Master Of The Order"),
    n("Luke's Bionic Hand", qty=2),
    n("Luke's Backpack"),
    n("Elegant Lightsaber", qty=2),
    n("Home One"),
    n("Artoo-Detoo In Red 5", True),
    n("Bravo Fighter"),
    n("Han, Chewie, And The Falcon", True),
    n("The Way Of Things"),
    n("Projection Of A Skywalker"),
    n("Quick Draw", True),
    n("Reflection", True),
    n("Imperial Atrocity"),
    n("Yoda's Hope"),
    n("Armed And Dangerous & Krayt Dragon Howl", qty=2),
    n("Courage Of A Skywalker", True),
    n("Control & Tunnel Vision"),
    n("It Could Be Worse"),
    n("Alternatives To Fighting"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Escape Pod", True),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Leadership", True, qty=3),
    n("Under Attack"),
    n("It's A Trap!"),
    n("Collision!"),
    n("Clash Of Sabers"),
    n("Jedi Levitation"),
    n("Houjix"),
    n("On The Edge"),
    n("Dodge"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Found Someone You Have & Higher Ground"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Aim High"),
    n("Ultimatum"),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
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
    n("According To My Design"),
    n("Emperor Palpatine"),
    n("I'll Take Them Myself"),
    n("Combat Response"),
    n("I'm Sorry", True),
    n("Kessel"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Storm Clouds"),
    n("Clouds"),
    n("Kessel Surveillance System"),
    n("Tibanna Floating Refinery"),
    n("Black 1"),
    n("Black 2", True),
    n("Black 3", True),
    n("Black 5"),
    n("OS-72-10", True),
    n("Saber 1"),
    n("Tarkin's Bounty"),
    n("Imperial Propaganda", True),
    n("Protocol Failure", qty=2),
    n("Image Of The Dark Lord", True),
    n("Where Are You Taking This ... Thing?"),
    n("Something Special Planned For Them", True),
    n("Spice Mine Operations"),
    n("Atmospheric Assault", True, qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("You Are Beaten"),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("All Power To Weapons", qty=4),
    n("Dark Maneuvers & Tallon Roll", qty=2),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("A Dark Time For The Rebellion", True),
    n("Limited Resources"),
    n("DS-61-4"),
    n("DS-61-2"),
    n("DS-61-3"),
    n("DS-61-5"),
    n("OS-72-10"),
    n("Baron Soontir Fel"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader With Lightsaber"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Mara Jade With Lightsaber"),
    n("Arica"),
    n("U-3PO"),
    n("Moruth Doole, Kessel Administrator"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
