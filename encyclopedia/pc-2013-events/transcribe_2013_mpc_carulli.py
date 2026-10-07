#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Matt Carulli Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Matt Carulli"
USERNAME = "quickdraw3457"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 22
DS_PAGE = 21
LS_SCAN = "2013 Match Play Championship p22 Matt Carulli LS.png"
DS_SCAN = "2013 Match Play Championship p21 Matt Carulli DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username quickdraw3457. Event MPC 2013, dated 1/26/13. "
    "Deck title B-Wings!!!. Light. Yavin 4 (V) system with Careful Planning. "
    "AFA → Anger, Fear, Aggression. Luke, Trust Me as written. "
    "Giftex dested A Gift. Roche as written. "
    "Yavin 4: Massassi War Room dested from Yavin 4: Massassi War Room. "
    "Blue Squadron B-wing x4 and B-wing Bomber x3 as written. "
    "Han Chewie And The Falcon as written. SW-4 Ion Cannon as written. "
    "It's Not My Fault dested It's Not My Fault!. Let's Go Left as written. "
    "Restore Freedom To The Galaxy as written. Slayn & Korpil Facilities as written. "
    "Shield Your Shift dested Your Ship?. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username quickdraw3457. Event MPC 2013, dated 1/26/13. "
    "Deck title 12 Card HD. Dark. Hunt Down And Destroy The Jedi (7-side Fire Come Out). "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Darth Vader, Betrayer Of The Jedi x4 as written. Emperor Palpatine x3. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "He Is Not Ready & Imperial Propaganda dested He Is Not Ready. "
    "Comscan Detection dested ComScan Detection. "
    "Short Range Fighters & Watch Your Back as written. "
    "We Must Accelerate Our Plans x4 as written. Young Fool x2. Restraining Bolt as written. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning"
LS_CARDS = [
    n("Yavin 4", True),
    n("Anger, Fear, Aggression", True),
    n("Careful Planning", True),
    n("Yavin 4: Massassi Headquarters"),
    n("Luke, Trust Me"),
    n("Aim High"),
    n("Superficial Damage", True),
    n("A Gift"),
    n("Naboo"),
    n("Roche", True),
    n("Yavin 4: Massassi War Room", True),
    n("Boushh"),
    n("Mirax Terrik"),
    n("Lando Calrissian, Scoundrel"),
    n("Mace Windu, Master Of The Order"),
    n("Luke Skywalker", True),
    n("Captain Verrack", True),
    n("Blue Squadron B-wing", qty=4),
    n("B-wing Bomber", qty=3),
    n("Tantive IV", True),
    n("Han, Chewie, And The Falcon"),
    n("Enhanced Proton Torpedoes", True, qty=4),
    n("SW-4 Ion Cannon", qty=2),
    n("Intruder Missile", qty=2),
    n("Power Pivot", qty=3),
    n("Lucky Shot", True),
    n("Rebel Artillery", qty=2),
    n("It's Not My Fault", True, qty=2),
    n("It's A Hit!", qty=2),
    n("Steady Aim"),
    n("Houjix"),
    n("Let The Wookiee Win", True, qty=2),
    n("It Could Be Worse"),
    n("Rebel Barrier"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Rebel Fleet"),
    n("Massassi Base Sentry"),
    n("Slayn & Korpil Facilities"),
    n("Concentrate All Fire", qty=2),
    n("Let's Go Left", qty=2),
    n("Restore Freedom To The Galaxy"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Do Or Do Not", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Your Ship?"),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Knowledge And Defense", True),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor"),
    n("Executor: Meditation Chamber"),
    n("Surface Defense", True),
    n("Darth Vader, Betrayer Of The Jedi", qty=4),
    n("Emperor Palpatine", qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("4-LOM With Concussion Rifle", True),
    n("Battle Droid Squad", qty=2),
    n("Imperial Justice", True),
    n("Revenge Of The Sith"),
    n("Jabba's Haven"),
    n("No Escape"),
    n("The Phantom Menace"),
    n("Visage Of The Emperor", qty=2),
    n("Emperor's Power", True),
    n("He Is Not Ready"),
    n("Maul Strikes"),
    n("Ghhhk"),
    n("Force Push", True),
    n("ComScan Detection", True),
    n("We Must Accelerate Our Plans", qty=4),
    n("Force Field", True, qty=2),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Force Lightning", qty=2),
    n("Young Fool", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Nal Hutta"),
    n("Cloud City: Security Tower", True),
    n("Death Star: War Room", True),
    n("Blizzard 4"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Restraining Bolt"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
