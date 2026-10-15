#!/usr/bin/env python3
"""2015 European Championship Day 2: Koen Meijssen (place 19).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p5 Dark / p6 Light typed deckbuilder exports (Card Name / Card Type / Deck qty).
"""
from __future__ import annotations

PLAYER = "Koen Meijssen"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2015 European Championship Koen Meijssen LS.png"
DS_SCAN = "2015 European Championship Koen Meijssen DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 19. Typed deckbuilder exports with quantity column, no form, no username. Name handwritten Koen Meijssen. "
    "Handwritten deck names: DS Pimp My Planet, LS WC Eend. DS 3:1 / LS 1:3."
)
LS_NOTE = (
    "TITLE MISMATCH: wiki says Combat Preparedness, sheet starts We'll Handle This / Duel Of The Fates (Objective line). "
    "Posted We'll Handle This/Duel Of The Fates dested We'll Handle This / Duel Of The Fates. "
    "Posted The Rebublic No Longer Functions dested The Republic No Longer Functions. "
    "Antilles Maneuver (V) and Antilles Maneuver listed as separate lines. Alter (V) ambiguous Premiere/Coruscant V on wiki; left to generator. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "Starts Imperial Entanglements (Objective line), matches wiki. "
    "Posted Imperial Entanglements/No One To Stop Us This Time dested Imperial Entanglements / No One To Stop Us This Time. "
    "Posted Captain Wulf Yularen (V) dested Colonel Wullf Yularen True. Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("I'll Take The Leader"),
    n("Threepio With His Parts Showing"),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Luke Skywalker", True, qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Evacuation Control", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("A New Secret Base", True),
    n("Anger, Fear, Aggression", True),
    n("Inner Strength"),
    n("Rebel Barrier"),
    n("Sense", qty=2),
    n("Alter", True),
    n("Control & Tunnel Vision"),
    n("Escape Pod", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("It's A Trap!"),
    n("Houjix"),
    n("Jedi Levitation", True),
    n("Free Ride & Endor Celebration", qty=2),
    n("Were You Looking For Me?"),
    n("We're Doomed"),
    n("Weapon Levitation"),
    n("It Could Be Worse"),
    n("A Few Maneuvers"),
    n("Antilles Maneuver", True),
    n("Antilles Maneuver"),
    n("Dodge"),
    n("Blast The Door, Kid!", qty=2),
    n("Heading For The Medical Frigate"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Nar Shaddaa"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("We'll Handle This / Duel Of The Fates"),
    n("Azure Angel"),
    n("Han, Chewie, And The Falcon"),
    n("Red Squadron 1"),
    n("Artoo-Detoo In Red 5", qty=4),
    n("X-wing Laser Cannon"),
    n("Qui-Gon's Lightsaber", qty=2),
]
LS_SHIELDS = [
    n("He Can Go About His Business"),
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Republic No Longer Functions"),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("Goldenrod"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Aim High"),
]
LS_ADD = []

DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Battle Deployment"),
    n("We're In Attack Position Now", qty=2),
    n("Captain Godherdt"),
    n("Admiral Motti", True),
    n("Admiral Ozzel"),
    n("Admiral Piett"),
    n("Commander Desanne"),
    n("Corporal Drelosyn"),
    n("Darth Vader", True),
    n("Colonel Wullf Yularen", True),
    n("General Veers", True),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Sergeant Irol"),
    n("Sergeant Elsek"),
    n("Sergeant Barich"),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine"),
    n("Imperial Decree", True),
    n("Imperial Justice", True),
    n("Something Special Planned For Them", True),
    n("Tatooine Occupation", qty=3),
    n("Endor Shield", True),
    n("Imperial Arrest Order"),
    n("Mobilization Points"),
    n("Knowledge And Defense", True),
    n("Cease Fire!", qty=2),
    n("Close Call", True),
    n("Force Push", True),
    n("I Can't Shake Him!", True, qty=3),
    n("Imperial Barrier"),
    n("Trample"),
    n("Turn It Off! Turn It Off!", True),
    n("Imperial Command", qty=3),
    n("Prepared Defenses"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Executor: Docking Bay"),
    n("Tatooine"),
    n("Tatooine: Desert Heart"),
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Conquest", True),
    n("Flagship Executor"),
    n("Devastator"),
    n("Blizzard 1"),
    n("Blizzard 2", True),
    n("Blizzard 4", qty=2),
    n("Tempest Scout 1"),
    n("Tempest Scout 3", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Vote Of No Confidence"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
