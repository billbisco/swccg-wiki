#!/usr/bin/env python3
"""2013 World Championship Day 2: Josh Mack Xerox WYS + Kessel TIT MOPS."""
from __future__ import annotations

PLAYER = "Josh Mack"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 62
DS_PAGE = 63
LS_SCAN = "2013 Worlds Day 2 p62 Josh Mack LS.png"
DS_SCAN = "2013 Worlds Day 2 p63 Josh Mack DS.png"
LS_PUBLIC_NOTE = "Day 2 name box is Mack."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Mack. Username blank. "
    "Email blank. Event Worlds, dated 08/10/13. Deck title Hope I Don't Play Sithies. LIGHT. "
    "Dested Josh Mack from the same-year 2013 MPC leftover (Username Remaker). "
    "Do not rewrite the 2013 MPC Josh Mack leftover. "
    "Watch Your Step unchecked (V) dested Watch Your Step / This Place Can Be A Little Rough. "
    "Tatooine (Cor) dested Tatooine. Tatooine: DB 94 dested Tatooine: Docking Bay 94. "
    "HFTMF dested Heading For The Medical Frigate. "
    "OOC & TT dested Out Of Commission & Transmission Terminated. "
    "All Wings report in combo dested All Wings Report In & Darklighter Spin. "
    "Control & TV dested Control & Tunnel Vision. "
    "Rebel Agent dested Leia, Rebel Princess. "
    "Japanese line 41 ウェッジ・アンティリーズ dested Wedge Antilles (V). "
    "Boshhk, Brash Smuggler dested BoShek, Brash Smuggler. "
    "Artoo in R5 dested Artoo-Detoo In Red 5. "
    "Han's toolkit dested Han's Toolkit. "
    "Tatooine: Lars moisture farm dested Tatooine: Lars' Moisture Farm. "
    "AFA dested Anger, Fear, Aggression. "
    "Shield 8 There Is Another box struck not v dested There Is Another. "
    "Jabba's Prize kept as extra Character. "
    "Form left column reprints 37-38 on lines 39-40 overwritten with Mirax Terrik and Sergeant Doallyn. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name MACK. Username blank. "
    "Deck title TIT MOPS. DARK. "
    "Do not rewrite the 2013 MPC Josh Mack leftover. "
    "Starting Kessel + Combat Readiness. "
    "Kessel: Admin's Office dested Kessel: Spice Mines - Administrator's Office. "
    "I'll Take The Leader dested as written (Admiral's Order). "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Galen SA dested Galen, Secret Apprentice. "
    "Darth Maul w/ Lightsaber dested Darth Maul With Lightsaber. "
    "Jango, the Assassin dested Jango Fett, The Assassin. "
    "Dr. E & Ponda B dested Dr. Evazan & Ponda Baba. "
    "4-lom w/ concussion rifle dested 4-LOM With Concussion Rifle. "
    "Ghhhk & Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Short Range combo dested Short Range Fighters & Watch Your Back!. "
    "Sniper & Dark Strike dested Sniper & Dark Strike. "
    "Slave I SoF dested Slave I, Symbol Of Fear. "
    "He Is Not Ready Combo struck omitted; Alter dested Alter. "
    "Kessel: Extraction Facility dested Kessel: Spice Mines - Extraction Facility. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Sidious' Saber dested Sidious' Lightsaber. "
    "Kessel: Cave dested as written. "
    "Spice Mine Administrator dested as written. "
    "We'll Let Fate decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Death Star Sentry dested Death Star Sentry. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("I Must Be Allowed To Speak", True),
    n("Let The Wookiee Win", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Houjix & Out Of Nowhere"),
    n("Either Way, You Win", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Old Ben"),
    n("Rebel Barrier"),
    n("A Few Maneuvers"),
    n("Desperate Reach", True),
    n("Dodge"),
    n("Control & Tunnel Vision", qty=2),
    n("Moving To Attack Position"),
    n("Imperial Atrocity", True),
    n("Tatooine Celebration", qty=2),
    n("Seeking An Audience", True),
    n("Rycar Ryjerd", True),
    n("Corellian Slip", True, qty=2),
    n("Much To Learn, You Still Have"),
    n("Menace Fades"),
    n("Leia, Rebel Princess", qty=2),
    n("Han Solo, Courageous Smuggler"),
    n("Luke Skywalker", True),
    n("Dash Rendar"),
    n("Talon Karrde", qty=2),
    n("Mirax Terrik"),
    n("Sergeant Doallyn"),
    n("Wedge Antilles", True),
    n("Melas", True, qty=2),
    n("Chewbacca, Walking Carpet", qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("BoShek, Brash Smuggler"),
    n("I'll Take The Leader"),
    n("Pulsar Skate"),
    n("Millennium Falcon"),
    n("Infinity"),
    n("Lando's Luxury Yacht"),
    n("Outrider"),
    n("Artoo-Detoo In Red 5"),
    n("Mercenary Armor", True),
    n("Han's Toolkit", True),
    n("Corellia", True),
    n("Tatooine: Mos Eisley"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Planetary Defenses", True),
    n("The Professor", True),
    n("There Is Another"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
]
LS_ADD = [
    n("Jabba's Prize"),
]


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take The Leader"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Emperor Palpatine", qty=2),
    n("Lord Sidious", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Arica"),
    n("Spice Mine Administrator"),
    n("4-LOM With Concussion Rifle", True),
    n("Force Field", True, qty=2),
    n("Force Push", True),
    n("Force Lightning"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Sniper & Dark Strike"),
    n("Imperial Barrier"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Blizzard 4"),
    n("Darth Vader", True),
    n("Imperial Justice", True),
    n("Dark Maneuvers", qty=2),
    n("Black Sun Fleet"),
    n("Protocol Failure"),
    n("Alter", True),
    n("Kessel Surveillance System"),
    n("Kessel: Cave"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Cloud City: Security Tower", True),
    n("Spice Mine Operations"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Sidious' Lightsaber"),
    n("Cold Feet", True),
    n("Blaster Rack", True),
    n("Sense", qty=2),
    n("Close Call", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Firepower", True),
    n("There Is No Try", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Death Star Sentry", True),
]
DS_ADD = []
