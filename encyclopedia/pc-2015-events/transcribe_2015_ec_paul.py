#!/usr/bin/env python3
"""2015 European Championship Day 2: Jordi Paul (place 27).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p21 DS / p22 LS typed lists.
"""
from __future__ import annotations

PLAYER = "Jordi Paul"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 22
DS_PAGE = 21
LS_SCAN = "2015 European Championship Jordi Paul LS.png"
DS_SCAN = "2015 European Championship Jordi Paul DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #27 (circled). Typed lists signed 'J.Paul', no username. "
    "DS 'Same Old Senate', D 1:3. LS 'Engelking's Watch Your Step', LS 1:2."
)
LS_NOTE = (
    "Typed, grouped with counts; 60 + 15 shields. "
    "Posted Watch Your Step / This Place Can Get A Little Rough dested Watch Your Step / This Place Can Be A Little Rough. "
    "Posted Anger, Fear, Agression (v) + 15 Shields dested Anger, Fear, Aggression True. "
    "Posted Chewbacca With Blaster Rifle dested Chewie With Blaster Rifle. Posted Millenium Falcon dested Millennium Falcon. "
    "Posted Leebo dested LE-BO2D9 (Leebo). Posted Pulsar Skate kept (GEMP Reflections II Pulsar Skate). "
    "Posted Run Luke, Run dested Run Luke, Run!. Posted Sorry About The Mess & Blaster Profiency dested Sorry About The Mess & Blaster Proficiency. "
    "Luke Skywalker, Jedi Knight x3 sheet-accurate."
)
DS_NOTE = (
    "Typed, grouped with counts; 60 + 15 shields. "
    "TITLE MISMATCH: wiki says Senate Occupied, sheet starts My Lord, Is That Legal? / I Will Make It Legal. "
    "Posted Coruscant: Docking Bay (Special Edition) dested Coruscant: Docking Bay. "
    "Posted Short Range Fighters & Watch Your Back! x2 kept. Lott Dod x3 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Like My Father Before Me"),
    n("Menace Fades"),
    n("Squadron Assignments"),
    n("Corellia"),
    n("Coruscant: Jedi Council Chamber"),
    n("Kessel"),
    n("Artoo, Brave Little Droid"),
    n("Artoo & Threepio"),
    n("Captain Han Solo"),
    n("Chewie With Blaster Rifle"),
    n("Dash Rendar"),
    n("Lando With Blaster Pistol"),
    n("LE-BO2D9 (Leebo)"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Melas", True, qty=2),
    n("Mirax Terrik"),
    n("R2-D2", True),
    n("Talon Karrde"),
    n("Wedge Antilles", True),
    n("Luke's Lightsaber", qty=2),
    n("Millennium Falcon"),
    n("Outrider"),
    n("Pulsar Skate"),
    n("I'll Take The Leader"),
    n("Civil Disorder", True),
    n("Honor Of The Jedi"),
    n("Kessel Run", qty=3),
    n("Legendary Starfighter"),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin"),
    n("Artoo, I Have A Bad Feeling About This"),
    n("Blaster Deflection"),
    n("Control & Tunnel Vision", qty=2),
    n("Escape Pod", True),
    n("Fallen Portal"),
    n("Free Ride & Endor Celebration"),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("How Did We Get Into This Mess?", qty=3),
    n("Hyper Escape"),
    n("Inconsequential Barriers"),
    n("Run Luke, Run!"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council"),
    n("We're Doomed"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Goldenrod"),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Your Ship?"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Tatooine: Desert Landing Site"),
    n("Prepared Defenses"),
    n("Combat Response", True),
    n("First Strike"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Coruscant: Docking Bay"),
    n("Naboo"),
    n("Aks Moe"),
    n("Baron Soontir Fel", qty=2),
    n("Baskol Yeesrim"),
    n("Coruscant Guard"),
    n("DS-61-2"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader", True),
    n("Edcel Bar Gane"),
    n("Lott Dod", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Orn Free Taa", qty=2),
    n("Tikkes"),
    n("Toonbuck Toora", qty=2),
    n("Yeb Yeb Adem'thorn"),
    n("SFS L-s9.3 Laser Cannons", qty=2),
    n("Black 2", True),
    n("Maul's Sith Infiltrator"),
    n("Saber 1", qty=2),
    n("Vader's Personal Shuttle", True),
    n("Blizzard 4"),
    n("Ability, Ability, Ability"),
    n("Accepting Trade Federation Control"),
    n("Blast Door Controls"),
    n("Imperial Decree", True),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("Senate Hovercam", qty=2),
    n("The Phantom Menace"),
    n("This Is Outrageous!"),
    n("Cold Feet", True),
    n("Ghhhk"),
    n("I Have You Now"),
    n("Masterful Move & Endor Occupation"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Squabbling Delegates", qty=3),
    n("Turn It Off! Turn It Off!", True),
    n("Vote Now!", qty=2),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Death Star Sentry"),
    n("There Is No Try"),
    n("Vote Of No Confidence"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
