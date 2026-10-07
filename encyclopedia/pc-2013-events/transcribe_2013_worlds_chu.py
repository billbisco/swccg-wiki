#!/usr/bin/env python3
"""2013 World Championship Day 2: Jonny Chu Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Jonny Chu"
USERNAME = "mryellow"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 26
DS_PAGE = 27
LS_SCAN = "2013 Worlds Day 2 p26 Jonny Chu LS.png"
DS_SCAN = "2013 Worlds Day 2 p27 Jonny Chu DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jonny Chu. Username mryellow. "
    "Event Worlds Day 2. Deck title Stevi / LS. LIGHT. Communing. "
    "Tatooine (EP1) dested Tatooine (Coruscant). "
    "Nick Of Time dested Nick Of Time. "
    "Alderaan Consular Ship dested Alderaan Consular Ship. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Chewbacca's Bowcaster dested Chewbacca's Bowcaster. "
    "Projection Of A Skywalker dested Projection Of A Skywalker. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Sectors Leave a mark dested Set For Stun. "
    "Inconsequential Barriers dested Inconsequential Barriers. "
    "Either Way You Win dested Either Way, You Win. "
    "The Bith Shuffle / Desp. Reach dested The Bith Shuffle & Desperate Reach. "
    "Yoda Stew dested Yoda Stew. "
    "Out Of Commission / Transmission Terminated dested "
    "Out Of Commission & Transmission Terminated. "
    "Control / Tunnel Vision dested Control & Tunnel Vision. "
    "Run Luke Run dested Run Luke, Run!. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jonny Chu. Username mryellow. "
    "Event Worlds Day 2. Deck title Kessel / Spice. DARK. "
    "Kessel: Spice Mines - Admin Office dested "
    "Kessel: Spice Mines - Administrator's Office. "
    "I'll Take Them Myself dested I'll Take Them Myself. "
    "I'm Sorry dested I'm Sorry. "
    "Short Range Fighters / Watch Your Back dested "
    "Short Range Fighters & Watch Your Back!. "
    "Mennek dested as written. "
    "Masterful Move / Endor Occupation dested Masterful Move & Endor Occupation. "
    "He Is Not Ready / Imp. Propaganda dested He Is Not Ready. "
    "Wipe Them Out, All Of Them dested Wipe Them Out, All Of Them. "
    "Image Of The Dark Lord dested Image Of The Dark Lord. "
    "Kader The Black dested Keder The Black. "
    "U-3PO dested U-3PO (Yoo-Threepio). "
    "Obsidian 16 dested as written. "
    "Tibanna Harvesting Refinery dested Tibanna Floating Refinery. "
    "After Her dested After Her!. "
    "We'll Let Fate-A Decide Huh dested We'll Let Fate-A Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Nick Of Time", True),
    n("Alderaan Consular Ship"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Chewbacca's Bowcaster"),
    n("Flash Of Insight", True),
    n("Draw Their Fire"),
    n("Rebel Gunrunner", True),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Projection Of A Skywalker"),
    n("Luke With Lightsaber", qty=2),
    n("Chewie, Enraged", True, qty=2),
    n("Chewbacca, Protector", qty=2),
    n("Luke Skywalker", True),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior"),
    n("Lando Calrissian, Scoundrel", True),
    n("Corran Horn"),
    n("Padme Naberrie", True),
    n("Leia, Rebel Princess"),
    n("Set For Stun"),
    n("Han With Heavy Blaster Pistol"),
    n("Admiral Ackbar", True),
    n("Houjix"),
    n("Inconsequential Barriers"),
    n("Grimtaash"),
    n("Either Way, You Win", True),
    n("Hear Me Baby, Hold Together", True),
    n("Lucky Shot", True),
    n("Escape Pod", True, qty=3),
    n("The Bith Shuffle & Desperate Reach"),
    n("Let The Wookiee Win", True, qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("Yoda Stew", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Out Of Commission & Transmission Terminated", True),
    n("Control & Tunnel Vision"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
]
LS_ADD = [
    n("Your Insight Serves You Well", True),
    n("Yoda Stew"),
    n("Affect Mind", True),
]


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("I'm Sorry", True),
    n("Combat Response", True),
    n("Combat Readiness", True),
    n("Short Range Fighters & Watch Your Back!", True),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Mennek"),
    n("Limited Resources"),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Masterful Move & Endor Occupation", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Ghhhk", qty=2),
    n("Abyssin Ornament", True),
    n("Abyssin Ornament"),
    n("He Is Not Ready"),
    n("Imperial Propaganda", True),
    n("Wipe Them Out, All Of Them", True),
    n("Protocol Failure", qty=2),
    n("Image Of The Dark Lord", True),
    n("All Power To Weapons", qty=5),
    n("Saber Squadron Pilot", qty=3),
    n("Baron Soontir Fel", qty=2),
    n("Keder The Black"),
    n("Keder The Black"),
    n("OS-72-10"),
    n("U-3PO (Yoo-Threepio)"),
    n("Arica"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Jango Fett, The Assassin"),
    n("Obsidian 16", True),
    n("Saber Squadron TIE", qty=3),
    n("Saber 1", qty=2),
    n("Saber 4"),
    n("Spice Mine Operations"),
    n("Clouds"),
    n("Storm Clouds"),
    n("Kessel Surveillance System"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Tibanna Floating Refinery"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("After Her!", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("Secret Plans", True),
]
DS_ADD = [
    n("There Is No Try"),
    n("We'll Let Fate-A Decide, Huh?", True),
    n("You Cannot Hide Forever"),
]
