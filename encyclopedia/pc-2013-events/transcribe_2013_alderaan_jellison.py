#!/usr/bin/env python3
"""2013 Alderaan Regionals: Ryan Jellison typed 2010 Print Form LS+DS."""
from __future__ import annotations

PLAYER = "Ryan Jellison"
USERNAME = "sac89837"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2013 Alderaan Regionals p11 Ryan Jellison LS.png"
DS_SCAN = "2013 Alderaan Regionals p12 Ryan Jellison DS.png"
LS_NOTE = "Typed 2010 Xerox Print Form. (Vn) tags on the printout are Holotable virtual versions. Deck title Speeder Jank."
DS_NOTE = "Typed 2010 Xerox Print Form. (Vn) tags on the printout are Holotable virtual versions. Deck title Sandwhirl Jank."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Grimtaash"),
    n("Hyper Escape"),
    n("All Wings Report In"),
    n("Escape Pod", True, qty=2),
    n("Houjix", qty=3),
    n("Out Of Nowhere", qty=2),
    n("Rebel Barrier", qty=2),
    n("Flash Of Insight", True),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("Rebel Fleet"),
    n("Incom Corporation & Koensayr Manufacturing", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Ben Kenobi", qty=2),
    n("Incom Engineer"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker", True),
    n("Commander Wedge Antilles", True, qty=2),
    n("Spiral", qty=2),
    n("Dash In Rogue 10", True),
    n("X-wing", qty=10),
    n("Sand Speeder", qty=10),
    n("Roche", True),
    n("Dressel", True),
    n("Corulag"),
    n("Rebel Cell - Situation Room", True),
    n("Rebel Cell - Perimeter", True),
    n("Rebel Cell - Monitoring Station", True),
    n("Don't Tread On Me", True),
    n("Rebel Cell - Hidden Landing Site", True),
    n("Tatooine"),
    n("Uncharted Settlements", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Ship?"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
]
LS_ADD = [
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time", True),
    n("Lieutenant Arnet"),
    n("Grand Moff Tarkin", True),
    n("AT-AT Commander", True),
    n("Sergeant Irol", True),
    n("Sergeant Barich"),
    n("Reserve Pilot", True),
    n("Commander Desanne"),
    n("Lieutenant Grond", True),
    n("Admiral Ozzel"),
    n("Admiral Piett"),
    n("General Nevar", True),
    n("Commander Daine Jir", True),
    n("ISB Sector Commander", True),
    n("Admiral Chiraneau"),
    n("Major Mianda"),
    n("Commander Praji", True),
    n("Commander Nemet", True),
    n("Commander Merrejk"),
    n("Grand Admiral Thrawn", True),
    n("Imperial Barrier", qty=2),
    n("Monnok"),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk", qty=3),
    n("We're In Attack Position Now", qty=4),
    n("Deflector Shield Generators", True),
    n("Sandwhirl", qty=2),
    n("Alert My Star Destroyer!"),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Tatooine Occupation", qty=2),
    n("Imperial Arrest Order"),
    n("He Always Wins!", True),
    n("Tempest Scout 6"),
    n("Tempest Scout 5"),
    n("Tempest Scout 1"),
    n("Blizzard Scout 1", True),
    n("Tatooine: Desert", qty=2),
    n("Tatooine: Desert Heart"),
    n("Tatooine: Jundland Wastes"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Tatooine: Tusken Canyon"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Podrace Arena"),
    n("Flagship", True),
    n("Sebulba's Podracer"),
    n("Boonta Eve Podrace"),
    n("Start Your Engines!"),
    n("Devastator", True),
    n("Tatooine: Imperial Vanguard Camp", True),
    n("Tatooine"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?"),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = [
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
]
