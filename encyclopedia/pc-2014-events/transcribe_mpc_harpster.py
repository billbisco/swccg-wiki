#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Steve Harpster.

Source: MPC-2014-Day-1-Main-Event.pdf pages 47–48 (2013 form, 15 shields).
HARPSTER dested Steve Harpster.
"""
from __future__ import annotations

PLAYER = "Steve Harpster"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 48
DS_PAGE = 47
LS_SCAN = "2014 Match Play Championship Day 1 Steve Harpster LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Steve Harpster DS.png"
LS_DECK_NAME = "IITFYS"
DS_DECK_NAME = "1-6"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. HARPSTER dested Steve Harpster. IITFYS dested It Is The "
    "Future You See (V). Mace MotO dested Mace Windu, Master Of The Order (V). Sorry "
    "Combo dested Sorry About The Mess & Blaster Proficiency. Control Tunnel Vision "
    "dested Control & Tunnel Vision. Do Or Do Not Combo dested Do, Or Do Not & Wise "
    "Advice. Battle Plan Combo dested Battle Plan & Draw Their Fire. Lando Luxury Yacht "
    "dested Lady Luck (V). Lando Calrissian Hero dested Lando Calrissian, Unlikely Hero "
    "(V). Quigon's Stick dested Qui-Gon's Lightsaber. Speak With A Jedi Council x5 unique "
    "overcount. (V) from checkbox. Unique overcounts sheet-accurate (Jedi Lightsaber (V) "
    "x2, Artoo-Detoo In Red 5 x2, Han, Chewie, And The Falcon (V) x2, Master Qui-Gon x2, "
    "Yoda, Master Of The Order x3, Mace Windu (V) x2, Luke Skywalker, Strong In The Force "
    "(V) x3, Sorry About The Mess & Blaster Proficiency x2, Escape Pod (V) x2, Blaster "
    "Deflection x2, Wesa Gotta Grand Army x2, Let The Wookiee Win x2, Speak With The Jedi "
    "Council x5, Leia, Rebel Princess x2)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. HARPSTER dested Steve Harpster. Deck name 1-6. Death Star II "
    "Throne Room header. CCT OBJ dested Carbon Chamber Testing / My Favorite Decoration. "
    "Dagobah Cave crossed, skipped (main=59). The Mandalorian dested Jango Fett, The "
    "Assassin (V). Practical Failure dested Protocol Failure (V). Control Combo dested "
    "Control & Set For Stun. Short Range Combo dested Short Range Fighters & Watch Your "
    "Back!. Reegesh dested Reegesh (V). Slave I Symbol Of Fear dested Slave I, Symbol Of "
    "Fear (V). Vader w/ Stick dested Darth Vader With Lightsaber. (V) from checkbox. Unique "
    "overcounts sheet-accurate (A Dark Time For The Rebellion (V) x2, Sneak Attack (V) x2, "
    "Count Dooku x2, Force Lightning x3, Sense x2, Disarmed x2, Imperial Artillery x2, "
    "Stunning Leader x2, Defensive Fire (V) x2, The Emperor (V) x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Coruscant: Nightclub"),
    n("Mace Windu, Master Of The Order", True),
    n("Naboo: Boss Nass' Chambers"),
    n("It Is The Future You See", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Jedi Lightsaber", True, qty=2),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Qui-Gon's Lightsaber"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Corran Horn"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Master Qui-Gon", True),
    n("Master Qui-Gon"),
    n("Yoda, Master Of The Order", qty=3),
    n("Mace Windu", True, qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Houjix"),
    n("Control & Tunnel Vision"),
    n("Sense"),
    n("Escape Pod", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Jedi Levitation", True),
    n("Speak With The Jedi Council", qty=5),
    n("Sai'torr Kal Fas", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("Mantellian Savrip"),
    n("Scrambled Transmission", True),
    n("Imperial Atrocity", True),
    n("Much To Learn You Still Have", True),
    n("Lady Luck", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Leia, Rebel Princess"),
    n("Leia, Rebel Princess"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Disarmed Creature", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Ultimatum"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Jabba's Prize", True),
    n("Cloud City: Security Tower", True),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console", True),
    n("Naboo"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sneak Attack", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Count Dooku", True),
    n("Count Dooku"),
    n("Black Sun Fleet"),
    n("Force Lightning", qty=3),
    n("Blockade Flagship: Bridge"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Jabba's Haven", True),
    n("Sense"),
    n("We Must Accelerate Our Plans"),
    n("Any Methods Necessary"),
    n("Elis Helrot"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sense"),
    n("Control & Set For Stun"),
    n("Imperial Barrier"),
    n("Maul's Sith Infiltrator"),
    n("Disarmed", qty=2),
    n("Mara Jade With Lightsaber", True),
    n("Imperial Artillery", qty=2),
    n("Close Call", True),
    n("Jango Fett, The Assassin", True),
    n("Protocol Failure", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Stunning Leader", True),
    n("Stunning Leader"),
    n("Dr. Evazan"),
    n("Defensive Fire", True, qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Darth Maul"),
    n("U-3PO (Yoo-Threepio)"),
    n("Lightsaber Deficiency", True),
    n("Darth Vader With Lightsaber"),
    n("16-88", True),
    n("16-88's Neural Inhibitor", True),
    n("Reegesh", True),
    n("The Emperor", True, qty=2),
    n("Despair", True),
    n("No Escape"),
    n("Feltipern Trevagg's Stun Rifle", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
