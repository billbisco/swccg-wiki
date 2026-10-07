#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Mike D'Ambrosio Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Mike D'Ambrosio"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 28
DS_PAGE = 27
LS_SCAN = "2013 Match Play Championship p28 Mike D'Ambrosio LS.png"
DS_SCAN = "2013 Match Play Championship p27 Mike D'Ambrosio DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Mike D'Ambrosio. Light. Starting Communing. "
    "Master Kenobi as written. Commando Training combo dested Commando Training & K'lor'slug. "
    "Wyvern Scepter dested as written. LTWW dested Let The Wookiee Win. "
    "Luke w/ saber dested Luke With Lightsaber. Tatooine: Obi Hut dested Tatooine: Obi-Wan's Hut. "
    "Tatooine (EP1) dested Tatooine. Alderaan Consular Ship as written. "
    "Threepio w/ parts dested Threepio With His Parts Showing. Line 19 fully crossed; omitted. "
    "Out Of Commission + Transmission dested Out Of Commission & Transmission Terminated. "
    "Incom T-16 / Tactical Barrier dested Incom T-16 Skyhopper. "
    "Found Someone + Higher Ground dested Found Someone You Have & Higher Ground. "
    "Chewie Enraged dested Chewie, Enraged. Bail Organa FoR dested Bail Organa, Father Of Rebellion. "
    "Han w/ blaster pistol dested Han With Heavy Blaster Pistol. "
    "Lando's Luxury Yacht dested Lady Luck. Run Luke Run dested Run Luke, Run!. "
    "Form left column reprints 37–38 on lines 39–40 are Houjix and Flash Of Insight. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Mike D'Ambrosio. Dark. Starting Contract + Collars / Enforced. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "A Sith's Wrath as written. Jabba's Palace dested Tatooine: Jabba's Palace. "
    "Galen saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Aurra Sing Deadly Assassin as written. Maul dested Darth Maul. "
    "Never Yalual dested Nevar Yalnal. Dr. Evazan as written. "
    "IG-88 The Black dested IG-88. Death Mark & Hutt Bounty as written. "
    "Galen dested Galen Marek, Starkiller. The Mandalorian FoF dested Jango Fett, The Assassin. "
    "Mara Jade saber dested Mara Jade With Lightsaber. "
    "Masterful Move & Endor Occ dested Masterful Move & Endor Occupation. "
    "Juri Juice & Kianber dested Juri Juice. Jovill dested Jodo Kast. "
    "Coruscant: 500 City Lair dested Coruscant: Private Platform (Docking Bay). "
    "Ket Maliss, Shadow Killer as written. I've Lost Artoo dested I've Lost Artoo. "
    "Form left column reprints 37–38 on lines 39–40 are Coruscant and Mara Jade saber. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Master Kenobi"),
    n("Communing"),
    n("Commando Training & K'lor'slug"),
    n("Wyvern Scepter", True),
    n("Let The Wookiee Win", True),
    n("Chewbacca's Bowcaster"),
    n("Luke With Lightsaber"),
    n("Wokling", True),
    n("Rebel Gunrunner"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Home One: War Room"),
    n("Tatooine"),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Senator Leia Organa"),
    n("Alderaan Consular Ship"),
    n("Threepio With His Parts Showing"),
    n("Let The Wookiee Win", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Incom T-16 Skyhopper"),
    n("Luke's Lightsaber", True),
    n("Found Someone You Have & Higher Ground"),
    n("Draw Their Fire"),
    n("Rebel Leadership", True),
    n("Chewie, Enraged", True),
    n("Bail Organa, Father Of Rebellion"),
    n("Corran Horn"),
    n("Chewie, Enraged", True),
    n("Han With Heavy Blaster Pistol"),
    n("Tantive IV", True),
    n("Houjix"),
    n("Wedge Antilles", True),
    n("Chewie, Enraged", True),
    n("Rebel Leadership", True),
    n("Lady Luck"),
    n("Run Luke, Run!", True),
    n("Houjix"),
    n("Flash Of Insight", True),
    n("Escape Pod", True),
    n("Luke With Lightsaber"),
    n("Run Luke, Run!", True),
    n("Escape Pod", True),
    n("Yoda, Great Warrior"),
    n("Artoo-Detoo In Red 5"),
    n("Flash Of Insight"),
    n("Use The Force"),
    n("Escape Pod", True),
    n("Seeking An Audience", True),
    n("A Jedi's Resilience"),
    n("Shmi Skywalker"),
    n("Luke With Lightsaber"),
    n("Out Of Commission"),
    n("Use The Force"),
    n("Rebel Leadership", True),
    n("Imperial Atrocity", True),
    n("Out Of Commission"),
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Yavin Sentry", True),
    n("Battle Plan", True),
    n("Aim High", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred", True),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("A Sith's Wrath"),
    n("Blaster Rack", True),
    n("Coruscant: Palpatine's Quarters"),
    n("Tatooine: Jabba's Palace"),
    n("Guild Of Assassins"),
    n("Gift Of The Master"),
    n("On The Hunt"),
    n("Trophy Of A Kill", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Darth Maul", True),
    n("One Beautiful Thing", qty=2),
    n("Nevar Yalnal", qty=2),
    n("Dr. Evazan", qty=2),
    n("Aurra Sing's Blaster Rifle"),
    n("Slave I, Symbol Of Fear"),
    n("Ghhhk"),
    n("Abyssin Ornament", True, qty=3),
    n("IG-88"),
    n("Death Mark & Hutt Bounty"),
    n("Arica", True, qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("Prepared Defenses", True),
    n("Something Special Planned For Them", True),
    n("Jango Fett, The Assassin"),
    n("Coruscant"),
    n("Mara Jade With Lightsaber", True),
    n("Masterful Move & Endor Occupation"),
    n("Juri Juice"),
    n("Force Field"),
    n("Sonic Bombardment", True, qty=3),
    n("Cold Feet"),
    n("Operational As Planned", True),
    n("Jodo Kast", True),
    n("Boba Fett, Prepared Hunter"),
    n("Nal Hutta"),
    n("Cloud City: Security Tower"),
    n("Coruscant: Casino"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Ket Maliss, Shadow Killer"),
    n("Darth Maul", True),
    n("Guri"),
    n("Force Push", True),
    n("I've Lost Artoo", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Battle Order", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Secret Plans", True),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("Fanfare"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
]
DS_ADD = []
