#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Jeremy G Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Jeremy G"
USERNAME = "Jedi Jer"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 34
DS_PAGE = 33
LS_SCAN = "2013 Match Play Championship p34 Jeremy G LS.png"
DS_SCAN = "2013 Match Play Championship p33 Jeremy G DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Jeremy G. Username Jedi Jer. Light. "
    "Deck title Ti Kwon Leap. Dated 01/25/13. "
    "Center of Tyranny / A Liberal World dested Center Of Tyranny / A Liberated World. "
    "Coruscant (SE) dested Coruscant. Rogue Insertion (TWS) dested Rogue Insertion. "
    "Yub Yub Commander dested Yub Yub, Commander. WWTBAO dested We Wish To Board At Once. "
    "Wes Janson, Rogue Vet dested Wes Janson, Veteran Rogue. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Blast The Door Kid dested Blast The Door, Kid!. Dark Ralter dested Dack Ralter. "
    "Commando Training & K'lor'slug dested Commando Training & K'lor'slug. "
    "AntMan combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Booster's Star Destroyer dested Errant Venture. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Han, Chewie & The Falcon dested Han, Chewie, And The Falcon. "
    "It's Not My Fault dested It's Not My Fault!. "
    "Line 60 Knowledge & Defense struck dested Anger, Fear, Aggression. "
    "Form left column reprints 37–38 on lines 39–40 are Corran Horn and Wedge Antilles, Red Squadron Leader. "
    "Shield 5 fully crossed; omitted. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Jeremy G. Username Jedi Jer. Dark. "
    "Deck title Boot To The Head. Dated 1/25/13. Starting Kessel. "
    "Kessel: Spice Mine Admin Office dested Kessel: Spice Mines - Administrator's Office. "
    "Breached Defenses & Molator dested Breached Defenses & Molator. "
    "Maul's Double Saber dested Maul's Double-Bladed Lightsaber. "
    "Colonel Jendon in Onyx 1 dested Colonel Jendon In Onyx 1. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Cyborg Commander dested General Grievous. "
    "He Isn't Ready Combo dested He Is Not Ready. "
    "Weapon Levitation Combo dested Weapon Levitation & The Empire's Back. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Darth Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "The Mandalorian Father dested Jango Fett, The Assassin. "
    "Sniper Combo dested Sniper & Dark Strike. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Form left column reprints 37–38 on lines 39–40 are Galen's Lightsaber, Vader's Gift and Blaster Rack. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Center Of Tyranny / A Liberated World"),
    n("Coruscant", True),
    n("Planetary Shield"),
    n("Rogue Insertion"),
    n("Heading For The Medical Frigate"),
    n("Rogue Squadron Tactics"),
    n("Declaration Of Rebellion"),
    n("Bacta Infirmary"),
    n("Field Dressing"),
    n("Commander Narra"),
    n("Veteran Rogue", qty=2),
    n("Yub Yub, Commander", qty=4),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Dressel"),
    n("Wes Janson, Veteran Rogue"),
    n("Senator Leia Organa"),
    n("We Wish To Board At Once"),
    n("Ten Numb", True),
    n("Blast The Door, Kid!", qty=2),
    n("Kier Santage"),
    n("Dack Ralter", True),
    n("Zev Senesca"),
    n("Commander Wedge Antilles", True),
    n("Echo Base Garrison"),
    n("Commando Training & K'lor'slug"),
    n("Derek 'Hobbie' Klivian", True),
    n("Coruscant: Main Power Plant"),
    n("Coruscant: Lower Levels"),
    n("Luke's Blaster Pistol", True),
    n("Dash Rendar", True, qty=2),
    n("Civil Disorder", True),
    n("Imperial Atrocity", True),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Corellian Slip", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Nabrun Leids"),
    n("Disruptor Pistol"),
    n("Artoo-Detoo In Red 5"),
    n("Obi-Wan In Radiant VII"),
    n("Red Squadron 7", True),
    n("Alderaan Consular Ship"),
    n("Coruscant Celebration"),
    n("Menace Fades"),
    n("Houjix & Out Of Nowhere"),
    n("Errant Venture"),
    n("Desperate Reach", True),
    n("It's Not My Fault!", True),
    n("Tycho Celchu", True),
    n("Han, Chewie, And The Falcon"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Wise Advice"),
    n("Your Insight Serves You Well"),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Breached Defenses & Molator"),
    n("Kessel: Spice Mines - Prison"),
    n("Grand Admiral Thrawn"),
    n("Force Field", True, qty=2),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("He Hasn't Come Back Yet"),
    n("Stop Motion", True),
    n("Colonel Jendon In Onyx 1"),
    n("Grievous' Lightsabers"),
    n("Kessel Surveillance System"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Spice Mine Operations"),
    n("Spice Mine Administrator"),
    n("He Is Not Ready"),
    n("Spice Mines Of Kessel", True),
    n("Sonic Bombardment", True),
    n("Weapon Levitation & The Empire's Back"),
    n("Something Special Planned For Them", True),
    n("Grand Moff Tarkin", True),
    n("Aurra Sing, Deadly Assassin"),
    n("Revenge Of The Sith"),
    n("Darth Vader's Lightsaber"),
    n("Galen Marek, Starkiller", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", qty=2),
    n("Trophy Of A Kill", qty=2),
    n("Imperial Barrier"),
    n("Aurra Sing's Blaster Rifle"),
    n("Operational As Planned", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blaster Rack", True),
    n("Protocol Failure"),
    n("Cold Feet", True),
    n("Lightsaber Deficiency", True),
    n("Boba Fett, Prepared Hunter"),
    n("Fighter Cover"),
    n("Conquest", True),
    n("A Dark Time For The Rebellion", True),
    n("General Grievous", qty=2),
    n("Jango Fett, The Assassin"),
    n("Monnok"),
    n("Sniper & Dark Strike"),
    n("Ghhhk"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Close Call", True),
    n("Arica", True),
    n("Masterful Move"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Oppressive Enforcement"),
    n("Fanfare"),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("Resistance"),
    n("Imperial Detention"),
    n("There Is No Try"),
]
DS_ADD = []
