#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: John Anderson typed LS + Xerox DS.

Light is the typed 2013 Print Form (p05). Dark is handwritten Xerox (p06).
Event Name on the Light sheet is '13 Worlds Day #2 overwritten SoCal 2013, dated 10/26/13.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "puck71"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2013 SoCal Grand Prix Day 1 p05 John Anderson LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p06 John Anderson DS.png"
LS_NOTE = (
    "Typed 2013 Xerox Print Form. Username puck71. Event Name was '13 Worlds Day #2, "
    "overwritten SoCal 2013 and dated 10/26/13. Line 13 Houjix struck, handwritten "
    "Redeemed Apprentice. Line 14 Artoo And Dangerous & Krayt Dragon Howl struck with "
    "no replacement (59 in the 60). Shield 7 Let's Keep A Little Optimism Here struck, "
    "handwritten Yavin Sentry."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


DS_NOTE = (
    "Handwritten Xerox form. Username puck71. Dated 10/26/13. "
    "Ni Chuba Na?? → Ni Chuba Na?. Kir Kanos with Force Pike → Kir Kanos With Force Pike. "
    "Dr. Evazan + Ponda Baba → Dr. Evazan & Ponda Baba. "
    "Masterful Move + Endor Occupation → Masterful Move & Endor Occupation. "
    "Sniper + Dark Strike → Sniper & Dark Strike. Coruscant Detention → Coruscant: Imperial City. "
    "Sidious's Lightsaber → Sidious' Lightsaber. (V) from the checkbox."
)
DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor", qty=3),
    n("Executor: Meditation Chamber"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Ni Chuba Na?", True),
    n("Conduct Your Search"),
    n("Lord Sidious", qty=2),
    n("Blizzard 4"),
    n("Darth Sidious"),
    n("Emperor Palpatine", qty=3),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Kir Kanos With Force Pike"),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=4),
    n("Masterful Move & Endor Occupation"),
    n("I Have You Now", qty=2),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("Force Push", True),
    n("Coruscant: Imperial City", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Revenge Of The Sith", qty=2),
    n("No Escape"),
    n("Emperor's Power", True),
    n("First Strike"),
    n("Blaster Rack", True),
    n("Crush The Rebellion"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room", True),
    n("Vader's Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Maul's Sith Infiltrator"),
    n("You Are Beaten"),
    n("Sniper & Dark Strike"),
    n("Sith Fury", True),
    n("Blast Door Controls"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever"),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("After Her!", True),
    n("Imperial Detention"),
]
DS_ADD = []


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Scoundrel's Luck"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Ingenuity"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Luke, Trust Me"),
    n("Squadron Assignments"),
    n("Hear Me Baby, Hold Together", True),
    n("Redeemed Apprentice"),
    n("Corellian Retort", True),
    n("Rebel Artillery"),
    n("Control & Tunnel Vision", qty=2),
    n("Moving To Attack Position", qty=2),
    n("Booster Terrik"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Escape Pod", True, qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Scrambled Transmission", True),
    n("Flash Of Insight", True),
    n("Imperial Atrocity", True),
    n("Projection Of A Skywalker"),
    n("I Can't Believe He's Gone", True),
    n("Menace Fades"),
    n("Landing Claw"),
    n("Kessel Run", True),
    n("Han's Toolkit"),
    n("Kyle Katarn's Blaster Rifle"),
    n("Spaceport Scoundrels Guild"),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Kessel"),
    n("Obi-Wan In Radiant VII"),
    n("Outrider"),
    n("Red Squadron 7", True),
    n("Pulsar Skate"),
    n("Millennium Falcon"),
    n("Kyle Katarn", qty=4),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Dash Rendar"),
    n("Corran Horn", qty=2),
    n("Captain Han Solo"),
    n("Boushh"),
    n("LE-BO2D9 (Leebo)", True),
    n("Tycho Celchu", True),
    n("Mirax Terrik"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("There Is Another"),
    n("Wise Advice"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Chasm", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
]
LS_ADD = []
