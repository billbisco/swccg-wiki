#!/usr/bin/env python3
"""2013 World Championship Day 2: Conrad Simmering Xerox Communing + Spice."""
from __future__ import annotations

PLAYER = "Conrad Simmering"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 93
DS_PAGE = 94
LS_SCAN = "2013 Worlds Day 2 p93 Conrad Simmering LS.png"
DS_SCAN = "2013 Worlds Day 2 p94 Conrad Simmering DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Typed 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name Conrad Simmering. Username blank. LIGHT. Deck title Communing. "
    "Dest as Conrad Simmering. "
    "Communing dested Communing. "
    "Inconsequential Berriers dested Inconsequential Barriers. "
    "Out Of Commission & Transmission Termina dested "
    "Out Of Commission & Transmission Terminated. "
    "K'lor'slug dested K'lor'slug. "
    "Run Luke, Run! dested Run Luke, Run!. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Typed 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name Conrad Simmering. Username blank. DARK. Deck title Spice. "
    "Dest as Conrad Simmering. "
    "According to My Desing dested According To My Design. "
    "Kessel: Spice Mines-Administrator's Office dested "
    "Kessel: Spice Mines - Administrator's Office. "
    "Kessel: Spice Mines-Extraction Facility dested "
    "Kessel: Spice Mines - Extraction Facility. "
    "Spice Mine Operation dested Spice Mine Operations. "
    "DS-72-10 dested OS-72-10. "
    "Black Leader dested Black Leader. "
    "U-2PO dested as written. "
    "He Is Not Ready & Imperial Propcganda dested He Is Not Ready "
    "(combo title is not a wiki dest). "
    "Where Are You Taking This ... Thing? dested as written. "
    "Dark Maneuvers & Tallon Roll dested Dark Maneuvers & Tallon Roll. "
    "Short Range Fighters & Watch Your Back! dested "
    "Short Range Fighters & Watch Your Back!. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing"),
    n("Tatooine: Slave Quarters"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Draw Their Fire"),
    n("Alderaan Consular Ship"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Lando Calrissian, Scoundrel", True, qty=2),
    n("Chewie, Enraged", True, qty=3),
    n("Luke With Lightsaber", qty=3),
    n("Shmi Skywalker"),
    n("Yoda, Great Warrior"),
    n("Senator Leia Organa"),
    n("Leia, Rebel Princess"),
    n("Bail Organa, Father Of Rebellion"),
    n("Admiral Ackbar", True),
    n("Han With Heavy Blaster Pistol"),
    n("Wedge Antilles", True),
    n("Threepio With His Parts Showing"),
    n("Corran Horn"),
    n("Chewbacca's Bowcaster"),
    n("Launching The Assault"),
    n("K'lor'slug"),
    n("Seeking An Audience", True),
    n("Flash Of Insight", True, qty=2),
    n("Rebel Gunrunner"),
    n("Much To Learn, You Still Have"),
    n("Imperial Atrocity", True),
    n("Civil Disorder", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Out Of Commission", qty=2),
    n("Houjix", qty=2),
    n("Use The Force", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True, qty=2),
    n("Run Luke, Run!", True, qty=2),
    n("A Jedi's Resilience"),
    n("Inconsequential Barriers"),
    n("Tatooine"),
    n("Home One: War Room"),
    n("Tatooine: Cantina"),
    n("Tatooine: Obi-Wan's Hut"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Ounee Ta"),
    n("Wise Advice"),
]
LS_ADD = []


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("According To My Design"),
    n("I'll Take Them Myself"),
    n("I'm Sorry", True),
    n("Combat Response"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Mara Jade With Lightsaber"),
    n("Darth Vader With Lightsaber"),
    n("Darth Maul With Lightsaber", qty=2),
    n("DS-61-2"),
    n("DS-61-3"),
    n("DS-61-5"),
    n("OS-72-10"),
    n("Moruth Doole, Kessel Administrator"),
    n("Arica"),
    n("Baron Soontir Fel"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("U-2PO"),
    n("Emperor Palpatine"),
    n("Black Leader"),
    n("Kessel Surveillance System"),
    n("Tibanna Floating Refinery"),
    n("Spice Mine Operations"),
    n("Kessel"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Clouds"),
    n("Storm Clouds"),
    n("Black 1"),
    n("Black 2", True),
    n("Black 3", True),
    n("Black 5"),
    n("Obsidian 10"),
    n("Saber 1"),
    n("Something Special Planned For Them", True),
    n("Tarkin's Bounty", True),
    n("Image Of The Dark Lord", True),
    n("He Is Not Ready"),
    n("Where Are You Taking This ... Thing?"),
    n("Protocol Failure", qty=2),
    n("All Power To Weapons", qty=4),
    n("Force Lightning"),
    n("Dark Maneuvers & Tallon Roll", qty=2),
    n("Atmospheric Assault", True, qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Ghhhk"),
    n("You Are Beaten"),
    n("Masterful Move & Endor Occupation"),
    n("A Dark Time For The Rebellion"),
    n("Cold Feet", True),
    n("Limited Resources"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Imperial Detention"),
]
DS_ADD = []
