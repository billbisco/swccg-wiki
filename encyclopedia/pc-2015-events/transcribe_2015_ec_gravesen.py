#!/usr/bin/env python3
"""2015 European Championship Day 2: Jesper Gravesen (place 28).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p23 DS / p24 LS handwritten deck list forms.
"""
from __future__ import annotations

PLAYER = "Jesper Gravesen"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 24
DS_PAGE = 23
LS_SCAN = "2015 European Championship Jesper Gravesen LS.png"
DS_SCAN = "2015 European Championship Jesper Gravesen DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #28 (circled). Forms signed only 'Ninja'; standings p01 of Place 01-17 PDF list "
    "'28 Jesper (Ninja) Gravesen, Japan' -> confirmed Jesper Gravesen. Username blank, no date/event. "
    "DS deck name 'Legal Advice', DS 2:1. LS deck name 'Suck my cloud' (reading), LS 0:4."
)
LS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "Posted QMC dested Quiet Mining Colony / Independent Operation. Posted CC: Guest Quarters dested Cloud City: Guest Quarters. "
    "Posted Heading for the m... dested Heading For The Medical Frigate. "
    "Posted Beldon's Eye (V box) kept. Posted Falcon dested Millennium Falcon. "
    "Posted Ounee Ta (sheet 'Oueseer'-like scrawl) dested Ounee Ta. Posted Luke Skywalker J/K x2 dested Luke Skywalker, Jedi Knight. "
    "Posted Co Jedi Chamber dested Coruscant: Jedi Council Chamber. Posted Leia with blaster x2 dested Leia With Blaster Rifle. "
    "Posted CC Lower Corridor dested Cloud City: Lower Corridor. Posted Sorry about combo dested Sorry About The Mess & Blaster Proficiency. "
    "Posted Speak with Jedi Council x3 dested Speak With The Jedi Council. Posted Corran in Rogue 9 dested Corran Horn In Rogue 9. "
    "Posted Wedge in Rogue/Red Sq 1 dested Wedge In Red Squadron 1. "
    "REVIEWED: CONFIRM line 31 \"Dash rendar\" dested Dash Rendar. Posted X-wing laser cannon dested X-wing Laser Cannon. "
    "REVIEWED: CONFIRM line 33 \"Strike force\" (V box) dested Strikeforce (V) (wiki page exists). "
    "Posted Control combo dested Control & Tunnel Vision. Posted Darklighter Spin combo x2 dested All Wings Report In & Darklighter Spin. "
    "REVIEWED: CONFIRM line 41 \"Free ride combo\" dested Free Ride & Endor Celebration. "
    "Posted Anakin Skywalker kept as Anakin Skywalker (character vs interrupt not stated). "
    "Posted CC Celebration dested Cloud City Celebration. Posted A Jedi resilience dested A Jedi's Resilience. "
    "Posted Lando Scoundrel dested Lando Calrissian, Scoundrel. Posted Chewie (V box) dested Chewie (V). "
    "Posted CC West Gallery dested Cloud City: West Gallery. Posted Obi with stick x2 dested Obi-Wan With Lightsaber. "
    "Posted Nabrun cards dested Nabrun Leids. Posted Jedi Levitation (V box) kept. Posted Lukes light saber dested Luke's Lightsaber. "
    "Shield 9 'Professor' dested The Professor (no shield version in 2015; transcribed as written). "
    "Posted Do or Do not dested Do, Or Do Not."
)
DS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "TITLE MISMATCH: wiki says Senate Occupied, sheet starts I Will Make It Legal (My Lord, Is That Legal? / I Will Make It Legal). "
    "Posted Senate dested Coruscant: Galactic Senate. Posted Flagship Bridge dested Blockade Flagship: Bridge. "
    "Posted Arrest order combo dested Imperial Arrest Order & Secret Plans. Posted Endor docking bay dested Endor: Landing Platform (Docking Bay). "
    "Posted Short range fighter combo x2 dested Short Range Fighters & Watch Your Back!. "
    "Posted Maul + stick x3 dested Darth Maul With Lightsaber. Posted Vaders shuttle dested Vader's Personal Shuttle. "
    "Posted Death Star II docking bay dested Death Star II: Docking Bay. Posted Senate hovercam dested Senate Hovercam. "
    "Posted Sniper combo dested Sniper & Dark Strike. Posted Count Dooku x3, Lott Dod x4 (lines 38-41 ditto) sheet-accurate. "
    "Posted SFS L-s9.3 laser cannons dested SFS L-s9.3 Laser Cannons. "
    "REVIEWED: AS-WRITTEN line 46 \"Tradoor\" (no DS card fits; Toonbuck Toora/Trandoshan were guesses). "
    "Posted Dr. Evazan combo dested Dr. Evazan & Ponda Baba. "
    "REVIEWED: CONFIRM line 52 \"Sense\" (faint S) dested Sense. Posted Dookus saber dested Dooku's Lightsaber. "
    "Posted Endor Back door dested Endor: Back Door. Posted Omni box combo dested Ommni Box & It's Worse. "
    "Posted Executor docking bay dested Executor: Docking Bay. "
    "Line 60 original crossed out, replacement 'K+D' (V box) dested Knowledge And Defense. "
    "Shield 4 Do They Have A Code Clearance? box filled solid (not an X) - left non-(V). "
    "Posted Weapon of the Sith dested Weapon Of A Sith. Posted Vote of no confidence (V box) kept True."
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
    n("Squadron Assignments"),
    n("Keeping The Empire Out Forever"),
    n("Melas", True),
    n("Captain Han Solo", qty=2),
    n("Millennium Falcon"),
    n("Harc Seff", True),
    n("A Few Maneuvers"),
    n("Ounee Ta"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Leia With Blaster Rifle", qty=2),
    n("Cloud City: Lower Corridor"),
    n("Escape Pod", True),
    n("Path Of Least Resistance", qty=2),
    n("Sense"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council", qty=3),
    n("Corran Horn In Rogue 9"),
    n("Wedge In Red Squadron 1"),
    n("Dash Rendar"),
    n("X-wing Laser Cannon"),
    n("Strikeforce", True),
    n("Depa Billaba"),
    n("Control & Tunnel Vision"),
    n("Wokling", True),
    n("Yoxgit"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Blaster Deflection"),
    n("Free Ride & Endor Celebration"),
    n("Outrider"),
    n("Plo Koon"),
    n("Anakin Skywalker"),
    n("Cloud City Celebration"),
    n("A Jedi's Resilience"),
    n("Houjix"),
    n("Menace Fades"),
    n("Lando Calrissian, Scoundrel"),
    n("Dodge"),
    n("Chewie", True),
    n("Cloud City: West Gallery"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Rebel Barrier"),
    n("Nabrun Leids"),
    n("It Could Be Worse"),
    n("Jedi Levitation", True),
    n("Luke's Lightsaber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display"),
    n("Simple Tricks And Nonsense"),
    n("A Close Race"),
    n("The Republic No Longer Functions", True),
    n("Don't Do That Again", True),
    n("The Professor"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Blockade Flagship: Bridge"),
    n("Prepared Defenses"),
    n("Combat Response", True),
    n("Imperial Arrest Order & Secret Plans"),
    n("Establish Control", True),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Saber 1", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Saber 4"),
    n("All Power To Weapons", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Black 2", True),
    n("Vader's Personal Shuttle", True),
    n("Edcel Bar Gane"),
    n("Masterful Move & Endor Occupation"),
    n("Death Star II: Docking Bay"),
    n("Squabbling Delegates", qty=2),
    n("Ghhhk"),
    n("This Is Outrageous!"),
    n("Senate Hovercam"),
    n("Force Field", True),
    n("DS-61-2"),
    n("Sniper & Dark Strike"),
    n("Security Precautions"),
    n("Maul Strikes"),
    n("Maul's Sith Infiltrator"),
    n("Count Dooku", qty=3),
    n("Lott Dod", qty=4),
    n("SFS L-s9.3 Laser Cannons"),
    n("The Phantom Menace", qty=2),
    n("Accepting Trade Federation Control"),
    n("Tradoor"),
    n("Darth Vader", True),
    n("Baron Soontir Fel", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("DS-181-4"),
    n("Sense"),
    n("Tikkes"),
    n("Orn Free Taa"),
    n("Dooku's Lightsaber"),
    n("Endor: Back Door"),
    n("Ommni Box & It's Worse"),
    n("Grand Moff Tarkin", True),
    n("Executor: Docking Bay"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("No Escape"),
    n("Oppressive Enforcement"),
    n("Do They Have A Code Clearance?"),
    n("There Is No Try"),
    n("Vote Of No Confidence", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
