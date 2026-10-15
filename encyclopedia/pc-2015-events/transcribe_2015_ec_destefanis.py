#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: David Destefanis Day 2 (place 3).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p08 Dark (handwritten) / p09 Light (typed).
"""
from __future__ import annotations

PLAYER = "David Destefanis"
USERNAME = "DDM"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 9
DS_PAGE = 8
LS_SCAN = "2015 European Championship David Destefanis LS.png"
DS_SCAN = "2015 European Championship David Destefanis DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 3 circled. p08 Dark handwritten / p09 Light typed. Event Name EC2015 / EC. "
    "Username DDM on both sheets. DS 3:1 / LS 3:1. "
    "Sheet deck names: DS 'DDM's Racks', LS 'Ketwol Madness' (not used as DECK_NAME)."
)
LS_NOTE = (
    "No objective; starting interrupt Careful Planning (V) on line 4, Hoth sites lines 1-3. "
    "TITLE MISMATCH: wiki says Echo Base Operations, sheet starts Careful Planning (Echo Base Operations is line 57, an Effect). "
    "Line 53 Sabotage crossed out, handwritten 'X-W Cannon' dested X-wing Laser Cannon; (V) box scribbled over, left v=False. "
    "Posted Hoth: Main Power Generators dested Hoth: Main Power Generators (1st Marker). "
    "Posted Hoth: North Ridge dested Hoth: North Ridge (4th Marker). "
    "Posted Hoth: Echo War Room dested Hoth: Echo Command Center (War Room). "
    "Posted Boussh dested Boushh. Posted Han, Chewie And The Falcon dested Han, Chewie, And The Falcon. "
    "Posted Artoo Detoo In Red 5 dested Artoo-Detoo In Red 5. Posted Collision dested Collision!. "
    "Shields: posted A Tragedy Has Occured / Your Insights Serves You Well / The Republic No Longer Function fixed spelling. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "Handwritten. Dash lines (18,19,21,29,30,34,37,42-44,46,48,59) read as ditto of the card above. "
    "Line 60 blank: main 59 as written. "
    "Posted HDADTJ dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Posted Holotheatre dested Executor: Holotheatre. Posted Med Chamber dested Executor: Meditation Chamber. "
    "Line 3 Visage dested Visage Of The Emperor (HDADTJ pulls it). "
    "REVIEWED: CONFIRM line 27 \"VISAGE\" dested Visage (sheet text is exactly this card title; second copy of unique Effect impossible) (DS-II starship, unique Effect already on line 3). "
    "Posted Prep Defenses dested Prepared Defenses. Posted Blaster Racks dested Blaster Rack (4 total: lines 6 (V), 15, 45, 46 ditto). "
    "Posted Wipe Them Out dested Wipe Them Out, All Of Them. Posted Fir(s)t Strike dested First Strike. "
    "Posted Blockade Flagship Bridge dested Blockade Flagship: Bridge. Posted Darth Maul Young App dested Darth Maul, Young Apprentice. "
    "Posted Darth Sidious kept. Posted Ability x3 dested Ability, Ability, Ability qty 1 (x3 read as the name; qty 3 would make 61). "
    "Posted Dr Evazan combo dested Dr. Evazan & Ponda Baba (lines 36, 37 ditto, 40 = 3). "
    "Posted Maul's Double LS dested Maul's Double-Bladed Lightsaber. Posted We Must Accelerate dested We Must Accelerate Our Plans. "
    "Posted Masterful Move & EO dested Masterful Move & Endor Occupation. Posted POTF dested Presence Of The Force. "
    "Posted Weapon Lev dested Weapon Levitation. Posted Something Spe For Them dested Something Special Planned For Them. "
    "Posted Sniper & DS dested Sniper & Dark Strike. Posted Imp. Barrier dested Imperial Barrier. "
    "Unique overcounts sheet-accurate (Blizzard 4 x3, Lord Vader x3, Darth Maul YA x3 via lines 16, 20, 21 ditto). "
    "Shields 15 as written. Shields: Secret Plans, A Useless Gesture, Battle Order each listed twice as written; "
    "'We'll let fate decide, huh!' dested We'll Let Fate-a Decide, Huh?. Shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning"
LS_CARDS = [
    n("Hoth"),
    n("Hoth: Main Power Generators (1st Marker)"),
    n("Hoth: North Ridge (4th Marker)"),
    n("Careful Planning", True),
    n("A New Secret Base"),
    n("Strike Planning"),
    n("Get To Your Ships!"),
    n("Endor"),
    n("Hoth: Echo Docking Bay", qty=4),
    n("Hoth: Echo Command Center (War Room)"),
    n("Hoth: Echo Med Lab"),
    n("General Crix Madine"),
    n("Corporal Beezer"),
    n("Ketwol"),
    n("Luke Skywalker", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Boushh"),
    n("Threepio With His Parts Showing"),
    n("Han, Chewie, And The Falcon"),
    n("Corran Horn In Rogue 9"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Red Squadron 1"),
    n("Azure Angel"),
    n("Green Leader In Green Squadron 1"),
    n("Electrobinoculars"),
    n("Control & Tunnel Vision"),
    n("We're Doomed"),
    n("Were You Looking For Me?", qty=2),
    n("A Few Maneuvers"),
    n("Collision!", qty=2),
    n("Rebel Barrier", qty=2),
    n("Sense", qty=2),
    n("Escape Pod", True, qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Houjix"),
    n("Life Debt"),
    n("X-wing Laser Cannon"),
    n("It Could Be Worse"),
    n("On The Edge"),
    n("Smoke Screen"),
    n("Echo Base Operations"),
    n("Scramble"),
    n("Draw Their Fire"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("He Can Go About His Business"),
    n("Your Ship?"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Goldenrod"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("The Republic No Longer Functions"),
    n("Battle Plan"),
    n("Affect Mind", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor"),
    n("Executor: Meditation Chamber"),
    n("Prepared Defenses"),
    n("Blaster Rack", True),
    n("Wipe Them Out, All Of Them"),
    n("Crush The Rebellion"),
    n("Dooku's Lightsaber"),
    n("Vader's Lightsaber"),
    n("First Strike"),
    n("Blockade Flagship: Bridge"),
    n("Elis Helrot", qty=2),
    n("I Have You Now", qty=2),
    n("Blaster Rack", qty=3),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Blizzard 4", qty=3),
    n("Count Dooku", qty=2),
    n("Darth Sidious"),
    n("Ability, Ability, Ability", True),
    n("No Escape"),
    n("Visage"),
    n("Lord Vader", qty=3),
    n("Force Push", True),
    n("Maul Strikes", qty=2),
    n("Dr. Evazan & Ponda Baba", qty=3),
    n("Maul's Double-Bladed Lightsaber"),
    n("The Phantom Menace"),
    n("We Must Accelerate Our Plans", qty=4),
    n("Force Field", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Energy Walls"),
    n("Crash Landing"),
    n("Ghhhk"),
    n("Sebulba's Podracer"),
    n("Presence Of The Force"),
    n("Weapon Levitation"),
    n("Something Special Planned For Them", True),
    n("Sniper & Dark Strike"),
    n("Imperial Barrier", qty=2),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward"),
    n("Secret Plans", qty=2),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever"),
    n("Vote Of No Confidence"),
    n("A Useless Gesture", qty=2),
    n("Firepower"),
    n("Battle Order", qty=2),
    n("Allegations Of Corruption"),
    n("Fanfare"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
