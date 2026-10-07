#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Greg Shaw Xerox LS+DS.

Sheet name Gregory Shaw.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 33
DS_PAGE = 34
LS_SCAN = "2013 SoCal Grand Prix Day 1 p33 Greg Shaw LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p34 Greg Shaw DS.png"
LS_NOTE = (
    "Handwritten Print Form. Sheet name Gregory Shaw. Event SoCal Grand Prix, 26 October 2013. "
    "Spaceport City / Docking Bay / Street / Scoundrels Guild as Corellia spaceport sites. "
    "Insurrection & Aim High is the Reflections combo. All Wings & Darklighter → "
    "All Wings Report In & Darklighter Spin. Antilles Maneuver & Rebel Reinforcements is the "
    "Reflections combo. Corellian Report → Corellian Retort. Houjix & Out of Nowhere is the "
    "Reflections combo. Sense (Premiere) → Sense. Landica → Booster In Pulsar Skate. "
    "Palio Rashid → Palejo Reshad. Ramiz 'Leoh' Nermani → Leesub Sirln. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. Sheet name Gregory Shaw. Carbon Chamber Testing / My Favorite Decoration. "
    "Carkoonite Chamber → Cloud City: Carbonite Chamber. IG-88 on line 9 struck; Elis Helrot remains. "
    "Boba Fett (SE) → Boba Fett. 4-LOM with Concussion Rifle as written. "
    "Jabba's Palace Dungeon / Audience Chamber as those sites. "
    "Short Range Fighters & WYB → Short Range Fighters & Watch Your Back!. "
    "Sense (Premiere) → Sense. WMAOP → We Must Accelerate Our Plans. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Captain Han Solo"),
    n("Millennium Falcon", True),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Scoundrels Guild"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Yoda, Great Warrior"),
    n("Mace Windu, Master Of The Order"),
    n("Leia, Rebel Princess", qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Dash Rendar", True),
    n("Corran Horn"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Booster In Pulsar Skate", True),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Palejo Reshad"),
    n("Leesub Sirln"),
    n("Chewie", True),
    n("Mirax Terrik"),
    n("Padme Naberrie", True),
    n("Lady Luck"),
    n("Tantive IV", True),
    n("Leia's Blaster Rifle"),
    n("No Questions Asked", True, qty=3),
    n("Imperial Atrocity", True),
    n("Strikeforce", True),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("Corellian Slip", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Punch It!"),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Corellian Retort", True, qty=2),
    n("Sense"),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Chasm", True),
    n("Your Ship?"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Jabba's Prize", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Carbonite Chamber Console", True),
    n("Jabba's Prize"),
    n("Any Methods Necessary"),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Elis Helrot"),
    n("Despair", True),
    n("Darth Vader With Lightsaber"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Maul"),
    n("Darth Maul With Lightsaber"),
    n("Boba Fett, Prepared Hunter"),
    n("Boba Fett", True),
    n("Dr. Evazan & Ponda Baba"),
    n("The Emperor", True, qty=2),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("Jango Fett, The Assassin"),
    n("U-3PO (Yoo-Threepio)"),
    n("4-LOM With Concussion Rifle", True),
    n("Blockade Flagship: Bridge"),
    n("Jabba's Palace: Dungeon"),
    n("Jabba's Palace: Audience Chamber"),
    n("Kashyyyk"),
    n("Dagobah: Cave"),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Black Sun Fleet"),
    n("Disarmed", qty=2),
    n("Protocol Failure"),
    n("The Phantom Menace"),
    n("Much Anger In Him"),
    n("No Escape"),
    n("Sneak Attack"),
    n("Defensive Fire", True, qty=2),
    n("Imperial Artillery"),
    n("Imperial Barrier"),
    n("Imperial Command"),
    n("Lightsaber Deficiency", True),
    n("A Dark Time For The Rebellion", True),
    n("Control & Set For Stun"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Stunning Leader", qty=2),
    n("Masterful Move"),
    n("Sense", qty=2),
    n("Cold Feet", True),
    n("Force Lightning", qty=2),
    n("We Must Accelerate Our Plans"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
]
DS_ADD = []
