#!/usr/bin/env python3
"""2015 European Championship Day 2: Jonas Hagen Nørregaard (place 22).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p11 DS / p12 LS handwritten deck list forms.
"""
from __future__ import annotations

PLAYER = "Jonas Hagen Nørregaard"
USERNAME = "SuperJones"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 12
DS_PAGE = 11
LS_SCAN = "2015 European Championship Jonas Hagen Nørregaard LS.png"
DS_SCAN = "2015 European Championship Jonas Hagen Nørregaard DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #22. Forms signed 'Jonas Hagen', username 'Super Jones' on both, event Europeans Day 2, 10/17/15. "
    "DS deck name 'Bring Him', DS 3:1. LS deck name 'QMC', LS 1:3."
)
LS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "Posted QMC/Independent Operation dested Quiet Mining Colony / Independent Operation. "
    "Posted Han With Heavy Blaster P. dested Han With Heavy Blaster Pistol. "
    "Posted Anakin Skywalker, P.L. dested Anakin Skywalker, Padawan Learner. "
    "Posted Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Posted Wedge Antilles, R.S.L. dested Wedge Antilles, Red Squadron Leader. "
    "Posted All Wings Report In & D.S. dested All Wings Report In & Darklighter Spin. "
    "Posted Alter (Coruscant) dested Alter. "
    "Posted Yoda Stew & You Do Have Y.. dested Yoda Stew & You Do Have Your Moments. "
    "Posted Free Ride & Endor Cele. dested Free Ride & Endor Celebration. "
    "Posted Leesub Siln dested Leesub Sirln. Posted Do or Do Not dested Do, Or Do Not. "
    "Ounee Ta listed in shield block (kept there as written)."
)
DS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "Posted Bring Him Before Me/Take... dested Bring Him Before Me / Take Your Father's Place. "
    "Posted Cloud City: Security T. dested Cloud City: Security Tower. "
    "Posted 4-Lom w/ Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Line 18 written 'We [crossed words] Accelerate Our Pla(ns)' + ditto line 19 dested We Must Accelerate Our Plans x2. "
    "REVIEWED: CONFIRM line 32 \"Guri\" (cursive) dested Guri. "
    "Posted Dr. Evazan (x2) dested Dr. Evazan. "
    "Posted A Dark Time for the Rebs dested A Dark Time For The Rebellion. "
    "Posted Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Posted Blockade Flagship: Bridge, Zuckuss In Mist H., Elis in Hinthra, Wooof expanded to full titles. "
    "Posted Masterful Move & E.Oc. dested Masterful Move & Endor Occupation. "
    "Posted I Find Your Lack of F.D. dested I Find Your Lack Of Faith Disturbing."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Cloud City: Guest Quarters"),
    n("Bespin"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Squadron Assignments"),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("Han With Heavy Blaster Pistol"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Leia, Rebel Princess"),
    n("Princess Leia", True),
    n("Yoda, Keeper Of The Peace"),
    n("Obi-Wan With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Pucumir Thryss"),
    n("Aayla Secura"),
    n("Leesub Sirln", True),
    n("Yoxgit"),
    n("Overseer"),
    n("Harc Seff", True),
    n("Outrider"),
    n("Dash Rendar"),
    n("Artoo-Detoo In Red 5"),
    n("Luke Skywalker", True),
    n("Bravo 2"),
    n("Officer Dolphe"),
    n("Red Squadron 1"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Houjix & Out Of Nowhere", qty=2),
    n("I'll Take The Leader", qty=2),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Sorry About The Mess", qty=2),
    n("Cloud City Celebration"),
    n("A Few Maneuvers", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Landing Claw"),
    n("A Jedi's Resilience", qty=2),
    n("It's A Trap!"),
    n("Rebel Barrier", qty=2),
    n("Path Of Least Resistance", qty=2),
    n("Alter", True),
    n("It Could Be Worse"),
    n("Jedi Levitation", True),
    n("It's A Hit!"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Antilles Maneuver", True),
    n("Free Ride & Endor Celebration"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Goldenrod"),
    n("He Can Go About His Business"),
    n("Your Insight Serves You Well", True),
    n("Ounee Ta"),
    n("Affect Mind", True),
    n("Simple Tricks And Nonsense", True),
    n("The Republic No Longer Functions", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Death Star II: Throne Room"),
    n("Insignificant Rebellion"),
    n("Your Destiny"),
    n("Any Methods Necessary"),
    n("Cloud City: Security Tower", True),
    n("4-LOM With Concussion Rifle", True),
    n("No Escape"),
    n("Disarmed", qty=2),
    n("Endor: Forest Clearing"),
    n("Force Lightning", qty=2),
    n("Neimoidian Advisor", qty=2),
    n("Sith Probe Droid", True, qty=3),
    n("Sith Fury", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Lord Vader", qty=2),
    n("Imperial Barrier", qty=2),
    n("Blizzard 4", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Dr. Evazan", qty=2),
    n("Ghhhk"),
    n("Mara Jade With Lightsaber"),
    n("Guri"),
    n("Blast Door Controls"),
    n("A Dark Time For The Rebellion", True),
    n("Ysanne Isard"),
    n("Darth Sidious"),
    n("TIE Sentry Ships", True),
    n("Force Push", True),
    n("Masterful Move & Endor Occupation"),
    n("The Phantom Menace"),
    n("Restraining Bolt"),
    n("Ability, Ability, Ability", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Masterful Move"),
    n("P-59"),
    n("Blockade Flagship: Bridge"),
    n("Emperor's Power"),
    n("Kashyyyk"),
    n("Close Call", True),
    n("Cold Feet", True),
    n("First Strike"),
    n("Count Dooku"),
    n("Zuckuss In Mist Hunter"),
    n("Elis In Hinthra"),
    n("Wooof", True),
    n("Emperor Palpatine"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Vote Of No Confidence"),
    n("Imperial Detention"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("There Is No Try"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
