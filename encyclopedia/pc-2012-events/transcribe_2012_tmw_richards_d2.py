#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: Mike Richards.

Source: 2012TMWDay2.pdf pages 1–2 (typed Dark 2010 Xerox / handwritten Light 2010 Xerox).
Name Michael Richards dested Mike Richards analog leftover Day 1 CANON / Username mr007agent.
p01 Dark Kessel. p02 Light Hidden Base. Do not dest as a new person.
Do not dest Day 1 TMW / 2012 MPC / 2013 TMW Richards 60s again.
"""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "mr007agent"
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2012 Texas Mini Worlds Day 2 Mike Richards LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 Mike Richards DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p01 typed 2010 Xerox Dark Kessel. p02 handwritten 2010 Xerox Light Hidden Base. "
    "Name Michael Richards dested Mike Richards analog leftover Day 1 CANON. "
    "Username mr007agent. Do not dest as a new person. "
    "Do not dest Day 1 TMW / 2012 MPC / 2013 TMW Richards 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p02 Light Deck Name Man Cals HB. LIGHT checked. Event TMW 2012 4/29/12. "
    "Name Michael Richards dested Mike Richards analog leftover Day 1. Username mroo7agent dested mr007agent. "
    "Hidden Base empty dested Hidden Base analog leftover Herold. "
    "Mon Cal Dockyards dested Mon Calamari: Dockyards analog leftover Alperstein. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "Were You Looking For Me dested analog leftover Skilton. "
    "Antilles Man & Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements analog leftover Walseth. "
    "Wahoo dested Wookiee Roar analog leftover Anderson. "
    "Out of Commission & TCF dested Out Of Commission & Transmission Terminated analog leftover. "
    "Mon Cal Star Cruiser dested Mon Calamari Star Cruiser analog leftover. "
    "Stay Sharp dested Stay Sharp! analog leftover. "
    "S-foil dested S-Foils analog leftover. "
    "3-PO w/ Parts Showing dested Threepio With His Parts Showing analog leftover Banger. "
    "Dagobah Yodas Hut dested Dagobah: Yoda's Hut analog leftover. "
    "Cloak dested Cloak Of Deception analog leftover. "
    "A Jedi's Plan dested A Jedi's Plans analog leftover Alperstein. "
    "Hear Me Baby dested Hear Me Baby, Hold Together analog leftover. "
    "King Kian dested Kin Kian analog leftover Richards. "
    "Anger Fear Aggression dested Anger, Fear, Aggression analog leftover Anderson IN THE 60. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox p01 Dark Deck Name DDM Spice or Brangus v6.0. DARK checked. Event TMW 2012 Day 2 04/29/12. "
    "Name Michael Richards dested Mike Richards analog leftover Day 1. Username mr007agent. "
    "Kessel empty dested Kessel analog leftover Stenerson. "
    "Combat Readiness True dested analog leftover Jake Nelson Day 2 IN THE 60. "
    "He is not ready combo dested He Is Not Ready & Imperial Propaganda analog leftover Banger. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover Anderson IN THE 60. "
    "Spice Mine Operations True dested analog leftover 2012 MPC Richards IN THE 60. "
    "Operation As Planned dested Operational As Planned analog leftover Massung. "
    "Sniper Combo dested Sniper & Dark Strike analog leftover Richards. "
    "Control Combo dested Control & Set For Stun analog leftover Tom H. "
    "Masterful Move combo dested Masterful Move & Endor Occupation analog leftover. "
    "YAB dested You Are Beaten analog leftover. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Nelson Day 2. "
    "We'll let Fate Decide dested We'll Let Fate-a Decide, Huh? analog leftover Lush. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base"
LS_CARDS = [
    n("Hidden Base"),
    n("Republic Logistics", True),
    n("Superficial Demise", True),
    n("Mon Calamari: Dockyards", True),
    n("Heading For The Medical Frigate"),
    n("Rendezvous Point"),
    n("Escape Pod", True, qty=2),
    n("Wedge Antilles"),
    n("Were You Looking For Me?", qty=2),
    n("Kashyyyk"),
    n("Luke Skywalker", True, qty=2),
    n("On Target", qty=3),
    n("Heavy Turbolaser Battery", qty=3),
    n("It Could Be Worse"),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=2),
    n("Wookiee Roar"),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Mon Calamari Star Cruiser", True, qty=4),
    n("Imperial Atrocity", True, qty=3),
    n("Mon Calamari"),
    n("Dash Rendar"),
    n("Projection Of A Skywalker", qty=2),
    n("Stay Sharp!", qty=2),
    n("S-Foils"),
    n("Defiance", qty=2),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Kiffex"),
    n("Dagobah: Yoda's Hut"),
    n("Cloak Of Deception"),
    n("Home One"),
    n("Kessel"),
    n("A Jedi's Plans", True),
    n("Hear Me Baby, Hold Together", True),
    n("Kin Kian"),
    n("Hindsight", True),
    n("Alter", True, qty=2),
    n("Dagobah"),
    n("Rebel Barrier"),
    n("Power Pivot", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Endor Shield", True),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Kuat Drive Yards", True),
    n("Kessel: Spice Mines - Extraction Facility", True),
    n("Knowledge And Defense", True),
    n("Spice Mine Operations", True),
    n("Kessel Surveillance System", True),
    n("Something Special Planned For Them", True),
    n("Blockade Support Ship", True),
    n("Operational As Planned", True),
    n("Gravity Shadow"),
    n("Kashyyyk"),
    n("4-LOM With Concussion Rifle", True),
    n("U-3PO"),
    n("Blizzard 2", True),
    n("The Phantom Menace"),
    n("Lateral Damage"),
    n("Sniper & Dark Strike"),
    n("Dengar In Punishing One"),
    n("Control & Set For Stun"),
    n("Overwhelmed"),
    n("Kessel: Spice Mines - Prison", True),
    n("Grand Moff Tarkin", True),
    n("Blizzard 1", True),
    n("Imperial Command", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Grand Admiral Thrawn"),
    n("Close Call", True, qty=3),
    n("Imperial Barrier"),
    n("Ghhhk"),
    n("Victory", True, qty=2),
    n("Tyrant"),
    n("Lost In Space"),
    n("Spice Mine Administrator", True, qty=2),
    n("Endor"),
    n("Mara Jade With Lightsaber", True),
    n("Kessel: Spice Mines - Administrator's Office", True),
    n("You Are Beaten"),
    n("Blizzard 4"),
    n("Spice Mines Of Kessel", True),
    n("Masterful Move & Endor Occupation"),
    n("Battle Deployment"),
    n("Protocol Failure", True),
    n("Image Of The Dark Lord", True),
    n("Devastator", True),
    n("I'll Take Them Myself", True),
    n("Darth Vader With Lightsaber"),
    n("General Veers", True),
    n("Admiral Ozzel"),
    n("Conquest", True),
    n("Cold Feet", True),
    n("Maarek Stele, The Emperor's Reach", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Battle Order"),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("Secret Plans", True),
]
DS_ADD = []
