#!/usr/bin/env python3
"""2015 European Championship Day 2: Christopher Claßen (place 21).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p09 DS / p10 LS typed lists.
"""
from __future__ import annotations

PLAYER = "Christopher Claßen"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2015 European Championship Christopher Claßen LS.png"
DS_SCAN = "2015 European Championship Christopher Claßen DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 21 circled. Typed lists signed 'C. Claßen'; no username. "
    "DS header 'Throne Room Villains', DS 3:1. LS header 'Richard's QMC', LS 1:3."
)
LS_NOTE = (
    "Main 61 as written: section headers sum to 60 (8+3+16+2+6+5+20 after hand edits) but typed characters are 16 "
    "before handwritten Ten Numb (header 15 corrected to 16), so characters list 17. Kept sheet lines; likely extra is the "
    "odd 'Jabba's Prize (V6)' character line. Starships 4->6 with handwritten Blue Squadron 5 and Wedge In Red Squadron 1; "
    "interrupts 23->20. "
    "Crossed out: Alternatives To Fighting, Escape Pod (V), Free Ride & Endor Celebration, Grimtaash; It's A Trap handwritten in. "
    "REVIEWED: CONFIRM characters line 'Jabba's Prize (V6)' dested Jabba's Prize v=True (wiki has Light Jabba's Prize character, Virtual Block 6). "
    "REVIEWED: CONFIRM handwritten 'Blue Squadron 5' dested Blue Squadron 5 (clear at 300 dpi; DSII starship). "
    "Posted Quiet Mining Colony/Independent Operation dested Quiet Mining Colony / Independent Operation. "
    "Posted The Rebublic No Longer Functions dested The Republic No Longer Functions."
)
DS_NOTE = (
    "Typed list 60 + 15 shields. No objective: starting Knowledge And Defense (V) + Death Star II: Throne Room. "
    "TITLE MISMATCH: wiki says Set Your Course For Alderaan, sheet starts Death Star II: Throne Room (Throne Room Villains). "
    "Emperor Palpatine typed under Characters is crossed out (already in Starting)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Squadron Assignments"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Captain Han Solo"),
    n("Corran Horn"),
    n("Dash Rendar"),
    n("Harc Seff", True),
    n("Jabba's Prize", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia Organa", True),
    n("Leia, Rebel Princess"),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Pucumir Thryss"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Ten Numb"),
    n("Intruder Missile"),
    n("X-wing Laser Cannon"),
    n("Gold Leader In Gold 1", True),
    n("Millennium Falcon"),
    n("Outrider"),
    n("Overseer"),
    n("Blue Squadron 5"),
    n("Wedge In Red Squadron 1"),
    n("Cloud City Celebration", qty=2),
    n("Evacuation Control", True),
    n("Honor Of The Jedi"),
    n("Menace Fades"),
    n("A Few Maneuvers"),
    n("A Jedi's Resilience", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Alter", True),
    n("Dodge"),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix & Out Of Nowhere"),
    n("Impressive, Most Impressive", True),
    n("Off The Edge"),
    n("Out Of Commission & Transmission Terminated"),
    n("Path Of Least Resistance", qty=2),
    n("Power Pivot"),
    n("Rapid Fire"),
    n("Rebel Artillery"),
    n("Rebel Barrier", qty=2),
    n("Sorry About The Mess"),
    n("It's A Trap!"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Goldenrod"),
    n("He Can Go About His Business"),
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Death Star II: Throne Room"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Death Star II: Throne Room"),
    n("According To My Design"),
    n("Emperor Palpatine"),
    n("Ability, Ability, Ability", True),
    n("Crush The Rebellion"),
    n("Endor Shield", True),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Coruscant"),
    n("Dagobah: Cave"),
    n("Hoth: Ice Plains"),
    n("Tatooine: Desert Landing Site"),
    n("4-LOM With Concussion Rifle", True, qty=2),
    n("Count Dooku", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Grand Admiral Thrawn", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Sith Probe Droid", True),
    n("Executor"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Blizzard 4", qty=2),
    n("After Her!"),
    n("Emperor's Power"),
    n("Enter The Bureaucrat"),
    n("First Strike"),
    n("Presence Of The Force", qty=2),
    n("The Phantom Menace", qty=2),
    n("You Cannot Hide Forever"),
    n("Elis Helrot"),
    n("Evader & Monnok"),
    n("Force Field"),
    n("Force Lightning", qty=3),
    n("Ghhhk"),
    n("I Have You Now", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Overload"),
    n("Sense & Uncertain Is The Future", qty=6),
    n("We Must Accelerate Our Plans"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("Vote Of No Confidence"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
