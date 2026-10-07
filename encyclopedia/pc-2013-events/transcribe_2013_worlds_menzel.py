#!/usr/bin/env python3
"""2013 World Championship Day 2: Chris Menzel typed Senate + Hunt Down."""
from __future__ import annotations

PLAYER = "Chris Menzel"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 65
DS_PAGE = 64
LS_SCAN = "2013 Worlds Day 2 p65 Chris Menzel LS.png"
DS_SCAN = "2013 Worlds Day 2 p64 Chris Menzel DS.png"
LS_NOTE = (
    "Typed spreadsheet printout (not a handwritten Xerox form). "
    "Header Worlds Day 2 | 10.08.2013 | Chris Menzel. "
    "LS Menzel Senate Deck Worlds 2013, VB 09.01. Header 5 Starting Cards. "
    "Do not rewrite the 2013 Alderaan Chris Menzel leftover. "
    "Plead My Case To The Senate / Sanity and Compassion dested "
    "Plead My Case To The Senate / Sanity And Compassion. "
    "Don't Tread On Me (V) 12 Hand Start dested Don't Tread On Me (V). "
    "Anger Fear Agression dested Anger, Fear, Aggression. "
    "Bail Organa: Father of the Rebellion (V) dested Bail Organa, Father Of Rebellion. "
    "Senator Palpatine Organa (V) struck omitted. "
    "Obi with Lightsaber dested Obi-Wan With Lightsaber. "
    "Yoda: Master of the Force dested Yoda, Master Of The Force. "
    "Handwritten Tyranus Jar Jar dested Darth Tyranus. "
    "Alderaan Consular Ship (V) struck omitted. "
    "Republic Gunship Wing (V) dested Republic Gunship Wing. "
    "Coruscant System (Special Edition) dested Coruscant. "
    "Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "StrikeForce (V) dested StrikeForce (V). "
    "So, This Is How Liberty Dies (V) dested So This Is How Liberty Dies (V). "
    "Field Dressing (V) dested Field Dressing. "
    "Alter (Episode 1) (V) dested Alter (V). "
    "Yoda Stew & You Do Have Your Moments dested Yoda Stew & You Do Have Your Moments. "
    "Handwritten Nogoodoo (V) dested Nocoo!. "
    "Simple Tricks And Knowledge (V) dested Simple Tricks And Nonsense (V). "
    "Another Pathetic Lifeform (V) struck omitted. "
    "He Can Go About His Business / Affect Mind / Traffic Control struck omitted. "
    "Handwritten Jungles Panic (V) dested Panic (V) as extra Interrupt. "
    "Handwritten 4 Affect Mind (V) dested Affect Mind (V) shields."
)
DS_NOTE = (
    "Typed spreadsheet printout (not a handwritten Xerox form). "
    "Header Worlds Day 2 | 10.08.2013 | Chris Menzel. "
    "Hunt Down and Destroy zee Germans, V 9.01. Header 6 Starting Cards. "
    "Do not rewrite the 2013 Alderaan Chris Menzel leftover. "
    "Hunt Down and Destroy the Jedi / Their Fire has gone out of the Universe dested "
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Character qty rewrite: Vader DLOTS 2 to 1, Vader with Lightsaber 2 to 3, "
    "Mara Jade 4 to 2. Handwritten Grand Admiral Thrawn extra. "
    "The Mandalorian, Father of Fett (V) dested The Mandalorian (V). "
    "Visage of the Emperor effects 1 to 2. Program Trap 1 to 2. "
    "Sith Fury & End This Destructive Conflict (V) 2 to 1. "
    "Weapon Of A Sith struck omitted; Death Star Sentry (V) dested Death Star Sentry (V). "
    "After Her (V) dested After Her! (V). "
    "Handwritten Alter / Evacuate? (V) / Vader's Obsession extra Interrupts."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Don't Tread On Me", True),
    n("Anger, Fear, Aggression", True),
    n("Bail Organa, Father Of Rebellion", True, qty=3),
    n("Supreme Chancellor Valorum", True),
    n("Senator Mon Mothma", True),
    n("Senator Padme Amidala", True),
    n("Senator Jar Jar Binks", True),
    n("Mas Amedda"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Han Solo, Courageous Smuggler", True, qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Yoda, Master Of The Force"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Chewie", True),
    n("Ki-Adi-Mundi", True),
    n("Owen Lars & Beru Lars"),
    n("Darth Tyranus"),
    n("Home One"),
    n("Millennium Falcon"),
    n("Republic Gunship Wing"),
    n("Coruscant"),
    n("Coruscant: Senate Landing Platform"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Senate Hovercam"),
    n("Imperial Atrocity", True),
    n("StrikeForce", True),
    n("So This Is How Liberty Dies", True),
    n("Menace Fades"),
    n("Field Dressing"),
    n("Might Of The Republic", qty=4),
    n("Rebel Leadership", True, qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Control & Tunnel Vision"),
    n("Corellian Retort", True),
    n("Desperate Reach", True),
    n("I've Got A Bad Feeling About This"),
    n("Alter", True),
    n("Sense"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Jedi Presence"),
    n("Houjix & Out Of Nowhere"),
    n("I've Decided To Go Back"),
    n("Let The Wookiee Win", True),
    n("Nocoo!", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True, qty=4),
]
LS_ADD = [
    n("Panic", True),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Visage Of The Emperor"),
    n("Surface Defense", True),
    n("Knowledge And Defense", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader With Lightsaber", qty=3),
    n("Mara Jade With Lightsaber", True, qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Battle Droid Squad", True, qty=2),
    n("P-59", qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("The Mandalorian", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Garindan", True),
    n("Grand Admiral Thrawn"),
    n("Slave I, Symbol Of Fear", True),
    n("Victory", True),
    n("Restraining Bolt"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Cloud City: Security Tower", True),
    n("Imperial Holotable"),
    n("Visage Of The Emperor", qty=2),
    n("The Phantom Menace"),
    n("Revenge Of The Sith", True),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Program Trap", qty=2),
    n("Something Special Planned For Them", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Sith Fury & End This Destructive Conflict", True),
    n("They're Still Coming Through!", qty=2),
    n("Imperial Barrier"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("A Dark Time For The Rebellion", True),
    n("You Swindled Me!", True),
    n("Imbalance & Kintan Strider", True),
    n("You Are Beaten"),
    n("Sense"),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("Force Field", True),
    n("Alter"),
    n("Evacuate?", True),
    n("Vader's Obsession"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("After Her!", True),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
