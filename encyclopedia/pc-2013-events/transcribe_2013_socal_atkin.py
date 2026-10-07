#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Clayton Atkin Xerox LS+DS.

Day 2 Same as Yesterday is transcribe_2013_socal_atkin_d2.py.
"""
from __future__ import annotations

PLAYER = "Clayton Atkin"
USERNAME = "Clayton Atkin"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2013 SoCal Grand Prix Day 1 p07 Clayton Atkin LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p08 Clayton Atkin DS.png"
LS_NOTE = (
    "Handwritten Xerox form. Username same as name. Event San Diego G.P. "
    "Starting interrupt Anger, Fear, Aggression (V); objective Communing; "
    "starting location Tatooine: Slave Quarters. Lando's Luxury Yacht → Lady Luck. "
    "Corellian Horn → Corran Horn. Wookiee (V) → Wookiee Roar (V). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Xerox form. Line 1 Knowledge And Defense (V); line 2 Hunt Down "
    "And Destroy The Jedi / Their Fire Has Gone Out Of The Universe (V) over a "
    "struck title. Galen, Secret Apprentice → Galen Marek, Starkiller. "
    "Cyborg Commander, Hunter Of Jedi → General Grievous. "
    "Cyborg Commander's Lightsaber → Grievous' Lightsabers. "
    "Black Leader → Juno Eclipse, Black Leader. Galen's Fighter → Rogue Shadow. "
    "Ni Chuba Na?? → Ni Chuba Na?. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Nick Of Time", True),
    n("Wookiee Roar", True),
    n("Master Kenobi"),
    n("Rebel Leadership", True, qty=3),
    n("Threepio With His Parts Showing"),
    n("Run Luke, Run", True, qty=3),
    n("Chewbacca, Protector", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Han With Heavy Blaster Pistol"),
    n("Captain Yutani With Blaster Cannon"),
    n("Imperial Atrocity", True),
    n("Luke With Lightsaber", qty=2),
    n("Padme Naberrie", True),
    n("Tatooine: Cantina"),
    n("Lucky Shot", True),
    n("Grimtaash"),
    n("Seeking An Audience", True),
    n("Luke Skywalker", True),
    n("R-3PO", True),
    n("Use The Force", qty=2),
    n("Chewbacca's Bowcaster"),
    n("Bail Organa, Father Of Rebellion"),
    n("Launching The Assault"),
    n("Home One: War Room"),
    n("Lady Luck"),
    n("Shmi Skywalker"),
    n("Chewie, Enraged", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Inconsequential Barriers"),
    n("Projection Of A Skywalker"),
    n("All Wings Report In & Darklighter Spin"),
    n("Yoda, Great Warrior"),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Admiral Ackbar", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Draw Their Fire"),
    n("Rebel Gunrunner"),
    n("Houjix"),
    n("Tatooine"),
    n("Home One"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Corran Horn"),
    n("Jabba's Palace: Audience Chamber"),
    n("A Gift"),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Aim High"),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses"),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na?", True),
    n("Force Field", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Endor"),
    n("4-LOM With Concussion Rifle", True),
    n("Galen Marek, Starkiller", qty=3),
    n("Lord Vader", qty=2),
    n("P-59"),
    n("Lightsaber Deficiency", True),
    n("Revenge Of The Sith"),
    n("Blizzard 4", qty=2),
    n("Sniper & Dark Strike"),
    n("General Grievous", qty=2),
    n("Force Lightning"),
    n("Masterful Move", qty=2),
    n("Vader's Lightsaber"),
    n("Juno Eclipse, Black Leader"),
    n("Protocol Failure"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("One Beautiful Thing"),
    n("Dr. Evazan & Ponda Baba"),
    n("No Escape"),
    n("Boba Fett, Bounty Hunter"),
    n("Blockade Flagship: Bridge"),
    n("Blaster Rack", True),
    n("Emperor Palpatine", qty=2),
    n("Gaderffii Stick", True),
    n("Emperor's Power", True),
    n("Endor: Back Door"),
    n("A Sith's Weapon"),
    n("General Nevar"),
    n("Mara Jade With Lightsaber"),
    n("Victory"),
    n("Grand Moff Tarkin", True),
    n("Ghhhk"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Rogue Shadow"),
    n("Grievous' Lightsabers"),
    n("Grand Admiral Thrawn"),
    n("Cold Feet", True),
    n("Image Of The Dark Lord", True),
    n("Force Push", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Leave Them To Me", True),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Weapon Of A Sith"),
]
DS_ADD = []
