#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Smith Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = "3MW0J8"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 90
DS_PAGE = 89
LS_SCAN = "2013 Match Play Championship p90 Smith LS.png"
DS_SCAN = "2013 Match Play Championship p89 Smith DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Smith. Username 3MW0J8. Light. "
    "Tatooine: Slave Quarters as written. Communing as written. "
    "Commando Training & K'lor'slug dested Commando Training & K'lor'slug. "
    "Tatooine (EP1) dested Tatooine. "
    "Tatooine: Obi-Wan's Hut dested Tatooine: Obi-Wan's Hut. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Luke Skywalker, Jedi Knight as written. "
    "Chewie, Enraged dested Chewie, Enraged. "
    "Leia, Rebel Princess dested Leia, Rebel Princess. "
    "Bail Organa Father of Rebellion dested Bail Organa, Father Of Rebellion. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "Han With Heavy Blaster Pistol dested Han With Heavy Blaster Pistol. "
    "Threepio With His Parts Showing dested Threepio With His Parts Showing. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Chewbacca's Bowcaster as written. "
    "Let The Wookiee Win dested Let The Wookiee Win. "
    "Wookiee Roar dested Wookiee Roar. "
    "Run Luke Run! dested Run Luke, Run!. "
    "Inconsequential Barriers as written. "
    "Antilles Maneuver & Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Imperial Atrocity dested Imperial Atrocity. "
    "Evacuation Control dested Evacuation Control. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Simple Tricks And Nonsense dested Simple Tricks And Nonsense. "
    "A Tragedy Has Occurred dested A Tragedy Has Occurred. "
    "Don't Do That Again dested Don't Do That Again. "
    "Let's Keep A Little Optimism Here dested Let's Keep A Little Optimism Here. "
    "Your Insight Serves You Well dested Your Insight Serves You Well. "
    "Form left column reprints 37–38 on lines 39–40 are Let The Wookiee Win and Wookiee Roar. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Smith. Username 3MW8J8. Dark. Starting Kessel. "
    "Combat Readiness dested Combat Readiness. "
    "Kessel: Spice Mines - Administrator's Office dested Kessel: Spice Mines - Administrator's Office. "
    "You Cannot Hide Forever & Mobilization Points dested You Cannot Hide Forever & Mobilization Points. "
    "I'll Take Them Myself as written. "
    "I'm Sorry dested I'm Sorry. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Darth Maul With Lightsaber dested Darth Maul With Lightsaber. "
    "Baron Soontir Fel as written. "
    "U-3PO dested U-3PO (Yoo-Threepio). "
    "DS-61-4 in Black 4 dested DS-61-4. "
    "OS-72-1 in Obsidian 1 dested OS-72-1 In Obsidian 1. "
    "OS-72-2 in Obsidian 2 dested OS-72-2 In Obsidian 2. "
    "Dreadnaught-Class Heavy Cruiser as written. "
    "SFS L-s9.3 Laser Cannons as written. "
    "Operational As Planned dested Operational As Planned. "
    "All Power To Weapons dested All Power To Weapons. "
    "Short Range Fighters & Watch Your Back! dested Short Range Fighters & Watch Your Back. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Dark Maneuvers & Tallon Roll dested Dark Maneuvers & Tallon Roll. "
    "A Dark Time For The Rebellion dested A Dark Time For The Rebellion. "
    "Control & Set For Stun dested Control & Set For Stun. "
    "Presence Of The Force dested Presence Of The Force. "
    "He Is Not Ready & Imperial Propaganda dested He Is Not Ready. "
    "Knowledge And Defense dested Knowledge And Defense. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "We'll Let Fate-a Decide, HUH? dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40 are Short Range Fighters & Watch Your Back and Masterful Move & Endor Occupation. "
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
    n("Commando Training & K'lor'slug"),
    n("Tatooine"),
    n("Tatooine: Cantina"),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Yoda, Great Warrior"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Chewie, Enraged", True, qty=4),
    n("Corran Horn", qty=2),
    n("Wedge Antilles"),
    n("Leia, Rebel Princess"),
    n("Bail Organa, Father Of Rebellion"),
    n("Lando Calrissian, Scoundrel", True),
    n("Shmi Skywalker"),
    n("Admiral Ackbar", True),
    n("Han With Heavy Blaster Pistol"),
    n("Threepio With His Parts Showing"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Chewbacca's Bowcaster"),
    n("Escape Pod", True, qty=3),
    n("Let The Wookiee Win", True, qty=3),
    n("Wookiee Roar", True, qty=2),
    n("Run Luke, Run!", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Grimtaash"),
    n("Houjix"),
    n("Inconsequential Barriers"),
    n("Use The Force"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Imperial Atrocity", True, qty=3),
    n("Evacuation Control", True, qty=2),
    n("Redeemed Apprentice"),
    n("Rebel Gunrunner"),
    n("Draw Their Fire"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("I'll Take Them Myself"),
    n("I'm Sorry", True),
    n("Spice Mine Operations"),
    n("Wakeelmui"),
    n("Storm Clouds", qty=2),
    n("Juno Eclipse, Black Leader"),
    n("DS-61-2"),
    n("Darth Maul With Lightsaber"),
    n("Baron Soontir Fel"),
    n("Arica"),
    n("DS-61-5"),
    n("DS-61-3"),
    n("U-3PO (Yoo-Threepio)"),
    n("Black 1"),
    n("Black 2", True),
    n("Black 3", True),
    n("Black 5"),
    n("DS-61-4"),
    n("OS-72-1 In Obsidian 1"),
    n("OS-72-2 In Obsidian 2"),
    n("Saber 1"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Kessel Surveillance System"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Floating Refinery"),
    n("Operational As Planned", True, qty=3),
    n("All Power To Weapons", qty=3),
    n("Short Range Fighters & Watch Your Back", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Monnok"),
    n("Ghhhk"),
    n("Dark Maneuvers & Tallon Roll", qty=4),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Lightsaber Deficiency", True),
    n("Control & Set For Stun", qty=2),
    n("Presence Of The Force", qty=2),
    n("Limited Resources"),
    n("Protocol Failure"),
    n("Combat Response"),
    n("He Is Not Ready"),
    n("Sienar Fleet Systems"),
    n("Lateral Damage"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans", True),
]
DS_ADD = []
