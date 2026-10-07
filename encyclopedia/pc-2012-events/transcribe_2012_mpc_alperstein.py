#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Barry Alperstein.

Source: 2012mpcday1.pdf pages 33–34 (2010 form, 12 shields, inverted scan).
Name Barry dested Barry Alperstein. Username MrFromMars.
p33 Dark Hunt Down (V). p34 Light Hidden Base.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Barry Alperstein"
USERNAME = "MrFromMars"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 34
DS_PAGE = 33
LS_SCAN = "2012 Match Play Championship Day 1 Barry Alperstein LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Barry Alperstein DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox inverted. Name Barry dested Barry Alperstein. "
    "Username Mr From Mars dested MrFromMars. Event MPC. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Hidden Base dested Hidden Base / Systems Will Slip Through Your Fingers empty. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Mon Cal Dockyards dested Mon Calamari: Dockyards. "
    "A Jedi's Plans dested A Jedi's Plans. "
    "Projection dested Projection Of A Skywalker. "
    "Heavy Laser Turbo Battery dested Heavy Turbolaser Battery. "
    "Mon Cal Star Cruiser dested Mon Calamari Star Cruiser. "
    "Mirax dested Mirax Terrik. "
    "3PO, Parts dested Threepio With His Parts Showing. "
    "Antilles Maneuver & RR dested Antilles Maneuver & Rebel Reinforcements. "
    "Form 25 Major Bren In Karie N crossed with no replacement, skipped. "
    "Form 40 ICBW empty and forms 41–42 True dittos kept separate. "
    "Light unique 59 sheet-accurate. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox inverted. Name Barry dested Barry Alperstein. "
    "Username MrFromMars. Event MPC. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Hunt Down dested Hunt Down And Destroy The Jedi True. "
    "Gift of the Mentor dested Gift Of The Master. "
    "Cyborg's Lightsabers dested Grievous' Lightsabers. "
    "S+D dested Sniper & Dark Strike. "
    "Weapon Levitation + TEB dested Weapon Levitation & The Empire's Back. "
    "Accelerate dested We Must Accelerate Our Plans. "
    "Elis dested Elis Helrot. "
    "Coruscant Detention dested as written. "
    "MM + Endor Occupation dested Masterful Move & Endor Occupation. "
    "Dengar w/ Carbine dested Dengar With Blaster Carbine. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "Mara w/ Saber dested Mara Jade With Lightsaber. "
    "Dr. E + Ponda dested Dr. Evazan & Ponda Baba. "
    "Kir Kanos w/ Pike dested Kir Kanos With Force Pike. "
    "Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Galen dested Galen Marek, Starkiller. "
    "Naboo: Theed Generator Core dested Naboo: Theed Palace Generator Core. "
    "Death Star: War Room dested Death Star: War Room. "
    "K+D dested Knowledge And Defense. "
    "Coward dested Come Here You Big Coward. "
    "Shield 12 A Useless Gesture crossed, Weapon Of A Sith dest replacement. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Rendezvous Point"),
    n("Heading For The Medical Frigate"),
    n("Republic Logistics"),
    n("Superficial Damage", True),
    n("Mon Calamari: Dockyards"),
    n("Merc Sunlet", True),
    n("A Jedi's Plans"),
    n("Projection Of A Skywalker", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Heavy Turbolaser Battery", qty=3),
    n("Mon Calamari Star Cruiser", True, qty=5),
    n("Liberty"),
    n("Defiance", qty=2),
    n("Mirax Terrik"),
    n("Captain Verrack", True),
    n("Dack Ralter"),
    n("Kin Kian"),
    n("Luke Skywalker", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("On Target", qty=3),
    n("Rebel Barrier", qty=2),
    n("Escape Pod", True, qty=2),
    n("Stay Sharp", qty=2),
    n("It Could Be Worse"),
    n("It Could Be Worse", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Were You Looking For Me?"),
    n("Hit And Run"),
    n("We're Doomed"),
    n("Power Pivot"),
    n("Grimtaash"),
    n("Kiffex"),
    n("Naboo"),
    n("Mon Calamari"),
    n("Kashyyyk"),
    n("Sullust"),
    n("Kessel"),
    n("Dagobah"),
    n("Dagobah: Yoda's Hut"),
    n("Hear Me Baby, Hold Together", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("I've Lost Artoo", True),
    n("Trophy Of A Kill", qty=2),
    n("Restraining Bolt"),
    n("Darth Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Presence Of The Force"),
    n("Sniper & Dark Strike"),
    n("Blaster Rack", True),
    n("Program Trap", True),
    n("No Escape"),
    n("A Sith's Weapon"),
    n("First Strike"),
    n("Blast Door Controls"),
    n("Revenge Of The Sith", qty=2),
    n("Weapon Levitation & The Empire's Back", qty=3),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Lightning"),
    n("Elis Helrot"),
    n("Coruscant Detention", True),
    n("Cold Feet", True),
    n("The Circle Is Now Complete"),
    n("Force Field", True),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Dengar With Blaster Carbine", True),
    n("Garindan", True),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Emperor Palpatine", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Kir Kanos With Force Pike"),
    n("4-LOM With Concussion Rifle", True),
    n("P-59"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("There Is No Try"),
    n("Leave Them To Me", True),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith", True),
]
DS_ADD = [
    n("Weapon Of A Sith"),
]
