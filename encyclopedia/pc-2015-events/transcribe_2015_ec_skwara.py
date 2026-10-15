#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: Ziemowit Skwara Day 2 (place 4).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p10 Dark / p11 Light (typed dumps, handwritten edits).
"""
from __future__ import annotations

PLAYER = "Ziemowit Skwara"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 11
DS_PAGE = 10
LS_SCAN = "2015 European Championship Ziemowit Skwara LS.png"
DS_SCAN = "2015 European Championship Ziemowit Skwara DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 4 circled. p10 Dark / p11 Light: typed list dumps, no PC form. "
    "Headers handwritten 'KRYPTO (DS)' / 'KRYPTO (LS)' (nickname; no Username box, USERNAME left blank). "
    "No player name on sheets; name from page map. DS 3:1 / LS 3:1."
)
LS_NOTE = (
    "START Quiet Mining Colony / Independent Operation. "
    "Crossed out (not in deck): Yoda Stew & You Do Have Your Moments, Shocking Information & Grimtaash (typed line), "
    "Ascension Guns (V) x2, Wedge Antilles (V), Moving To Attack Position, Sense, Gold Leader In Gold 1 (V), Pulsar Skate, "
    "Inconsequential Barriers. "
    "'Side:' block with handwritten adds (player numbered 53-59 + Corran Horn) counted as main deck: "
    "Antilles Maneuver, Leesub Sirln (V), Red Squadron 1, It's A Trap!, It's A Hit!, Shocking Inf. & Grimtaash, Chewie (V), Corran Horn. "
    "Posted Leesub Sirlin dested Leesub Sirln. Posted Shocking Inf. & Grimtash dested Shocking Information & Grimtaash. "
    "Posted Alter (Premiere) (V) dested Alter True. "
    "Anger, Fear, Aggression (V) listed in shield column as '(1 starting)' = starting effect, counted in the 60. "
    "Posted Jabba's Prize/Jabba's Prize dested Jabba's Prize. "
    "Main 60 by my count (player's own numbering skips one: Corran Horn unnumbered 60th). Shields 15."
)
DS_NOTE = (
    "START Imperial Entanglements / No One To Stop Us This Time (listed last in main column). "
    "Knowledge And Defense (V) listed in shield column as '(1 starting)' = starting effect, counted in the 60. "
    "Posted I Can't Shake Him! (V) (x4) dested I Can't Shake Him! True qty 4. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Captain Han Solo"),
    n("Millennium Falcon"),
    n("Don't Get Cocky"),
    n("Green Leader In Green Squadron 1"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Path Of Least Resistance", qty=2),
    n("Rebel Barrier", qty=2),
    n("Free Ride & Endor Celebration"),
    n("A Few Maneuvers", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Alter", True),
    n("Antilles Maneuver", True),
    n("Overseer"),
    n("Artoo-Detoo In Red 5"),
    n("Outrider"),
    n("Kal'Falnl C'ndros"),
    n("Commander Narra"),
    n("Dash Rendar"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Luke Skywalker", True),
    n("Leia, Rebel Princess"),
    n("Yoxgit"),
    n("Pucumir Thryss"),
    n("Mirax Terrik"),
    n("Lobot", True),
    n("Jar Jar Binks"),
    n("Lando Calrissian", True),
    n("Melas", True),
    n("Yoda, Keeper Of The Peace"),
    n("Aayla Secura"),
    n("Obi-Wan Kenobi", True),
    n("Harc Seff", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Lando's Not A System, He's A Man"),
    n("Ounee Ta"),
    n("Cloud City Celebration"),
    n("Evacuation Control", True),
    n("Beldon's Eye", True),
    n("Squadron Assignments"),
    n("Keeping The Empire Out Forever"),
    n("Heading For The Medical Frigate"),
    n("Cloud City: Guest Quarters"),
    n("Bespin"),
    n("Quiet Mining Colony / Independent Operation"),
    n("Anger, Fear, Aggression", True),
    n("Antilles Maneuver"),
    n("Leesub Sirln", True),
    n("Red Squadron 1"),
    n("It's A Trap!"),
    n("It's A Hit!"),
    n("Shocking Information & Grimtaash"),
    n("Chewie", True),
    n("Corran Horn"),
]
LS_SHIELDS = [
    n("He Can Go About His Business"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Jabba's Prize"),
    n("Goldenrod"),
    n("Wise Advice"),
    n("The Republic No Longer Functions"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Affect Mind", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("We're In Attack Position Now", qty=2),
    n("Battle Deployment"),
    n("Gravity Shadow"),
    n("Cold Feet", True),
    n("Turn It Off! Turn It Off!", True),
    n("Imperial Barrier"),
    n("I Can't Shake Him!", True, qty=4),
    n("Close Call", True),
    n("Imperial Command", qty=3),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Tatooine: Mos Espa"),
    n("Executor: Docking Bay"),
    n("Flagship Executor"),
    n("Binder"),
    n("Conquest", True),
    n("Blizzard 4", qty=2),
    n("Tempest Scout 3", True),
    n("Tempest Scout 1"),
    n("Blizzard 2", True),
    n("Tempest 1"),
    n("Corporal Drelosyn"),
    n("Sergeant Irol"),
    n("Sergeant Elsek"),
    n("Sergeant Barich"),
    n("DS-61-5"),
    n("Captain Godherdt"),
    n("Arica"),
    n("General Veers", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Admiral Ozzel"),
    n("Admiral Piett"),
    n("Emperor Palpatine"),
    n("Commander Desanne"),
    n("Darth Vader", True),
    n("Grand Moff Tarkin", True),
    n("Tatooine Occupation", qty=3),
    n("Imperial Decree", True),
    n("Imperial Justice", True),
    n("Imperial Arrest Order"),
    n("Mobilization Points"),
    n("Endor Shield", True),
    n("Prepared Defenses"),
    n("Tatooine: Desert Heart"),
    n("Devastator"),
    n("Tatooine"),
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Detention", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
]
DS_ADD = []
