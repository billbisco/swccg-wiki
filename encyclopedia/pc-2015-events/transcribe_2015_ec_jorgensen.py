#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: Casper Jørgensen Day 2 (place 5).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p12 Dark / p13 Light (handwritten PC forms).
"""
from __future__ import annotations

PLAYER = "Casper Jørgensen"
USERNAME = "aevumct69"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 13
DS_PAGE = 12
LS_SCAN = "2015 European Championship Casper Jørgensen LS.png"
DS_SCAN = "2015 European Championship Casper Jørgensen DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 5 circled. p12 Dark / p13 Light handwritten PC forms. Event Date 10/17/15, Event Name EC 15. "
    "Name box 'Casper' only; surname from page map. Username reads 'aevumct69' on both (handwriting; could be 'aevunct69'). "
    "DS 3:1 / LS 3:1. Sheet deck names: DS 'Danish Parliament', LS 'Hidden Wings' (not used as DECK_NAME). "
    "Ditto marks expanded to repeat the line above."
)
LS_NOTE = (
    "START Hidden Base / Systems Will Slip Through Your Fingers (sheet 'Hidden Base / ...'). "
    "Posted Heading to the medical.. dested Heading For The Medical Frigate. Posted Rocke dested Roche. "
    "Posted Wedge in Red Squad 1 dested Wedge In Red Squadron 1. Posted Gold Leader in G1 dested Gold Leader In Gold 1. "
    "Posted Green Leader in GS1 dested Green Leader In Green Squadron 1. Posted Obi in Radiant dested Obi-Wan In Radiant VII (wiki; not in GEMP file). "
    "Posted HCF dested Han, Chewie, And The Falcon. Posted Hit n Run dested Hit And Run. "
    "Combined Attack kept (wiki page exists; not in GEMP file). Posted Closer!? dested Closer?!. "
    "Posted Yoda Stew & Combo dested Yoda Stew & You Do Have Your Moments. "
    "Lines 51-52 'All Wings Report In' kept as plain card (not combo) as written. "
    "Shields: Golden Rod dested Goldenrod; Tradegy dested A Tragedy Has Occurred; Do, Or Do Not kept (shield version); "
    "line 12 He Can Go About His Business (V) box scribbled over, left v=False. Main 60, shields 15."
)
DS_NOTE = (
    "START My Lord, Is That Legal? / I Will Make It Legal (sheet 'My Lord Is That Legal / ...'). "
    "TITLE MISMATCH: wiki says Senate Occupied, sheet starts My Lord, Is That Legal? (no 'Senate Occupied' card exists; likely deck nickname). "
    "Posted Galactic Senate dested Coruscant: Galactic Senate. Posted Tat: Landing Site dested Tatooine: Desert Landing Site. "
    "Posted Lott Dod x3 kept (unique overcount sheet-accurate). Posted Edcel Bar Gane kept. "
    "Posted A Dark Time For the Rebels dested A Dark Time For The Rebellion (line 14 (V), ditto line 15 unchecked). "
    "Posted EPP Maul x3 dested Darth Maul With Lightsaber (no EPP Maul exists; slang). "
    "Posted Emp Palpatine dested Emperor Palpatine. Posted Darth Vader Dark Lord dested Darth Vader, Dark Lord Of The Sith x2. "
    "Posted Dreadnaught x2 dested Dreadnaught-Class Heavy Cruiser. Posted Bossk in Hounds Tooth dested Bossk In Hound's Tooth. "
    "Posted Boba in Slave I dested Boba Fett In Slave I. Posted 4-lom w/ Gun dested 4-LOM With Concussion Rifle. "
    "Posted Blockade Flagship Bridge dested Blockade Flagship: Bridge. Posted Naboo: Generator dested Naboo: Theed Palace Generator. "
    "REVIEWED: CONFIRM line 45 \"Imba Combo\" (only DS Im- combo) dested Imbalance & Kintan Strider. "
    "Posted Als Moe dested Aks Moe. Posted Boba, BH dested Boba Fett, Bounty Hunter. "
    "Posted Ommi Box & it's worse dested Ommni Box & It's Worse. Posted Something Special Planned dested Something Special Planned For Them. "
    "Shields: Death Star Sentry (V); line 11 'Do, or Do Not' crossed out, replacement 'There Is No Try'; "
    "'We'll Let Fate Decide' dested We'll Let Fate-a Decide, Huh?. Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Rendezvous Point"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("A New Secret Base", True),
    n("Superficial Damage"),
    n("Nar Shaddaa"),
    n("Roche"),
    n("Naboo"),
    n("Kiffex"),
    n("Tatooine"),
    n("Anoat", True),
    n("Blue Squadron B-wing", qty=3),
    n("Red Squadron X-wing"),
    n("Acclamator-Class Assault Ship"),
    n("Red 8", True),
    n("Wedge In Red Squadron 1"),
    n("Gold Leader In Gold 1", True),
    n("Green Leader In Green Squadron 1"),
    n("Obi-Wan In Radiant VII"),
    n("Han, Chewie, And The Falcon"),
    n("Proton Torpedoes", qty=2),
    n("Concussion Missiles", qty=3),
    n("Intruder Missile"),
    n("X-wing Laser Cannon"),
    n("Power Pivot"),
    n("Hit And Run"),
    n("Combined Attack"),
    n("Steady Aim"),
    n("Stay Sharp!", qty=2),
    n("Rapid Fire", qty=2),
    n("Alter"),
    n("Let's Go Left"),
    n("Concentrate All Fire", qty=2),
    n("Projection Of A Skywalker", qty=2),
    n("Slayn & Korpil Facilities"),
    n("Control & Tunnel Vision"),
    n("Boushh"),
    n("Luke Skywalker, Jedi Knight"),
    n("Closer?!"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("All Wings Report In", qty=2),
    n("Sabotage", True),
    n("Slight Weapons Malfunction"),
    n("They Win This Round"),
    n("We Wish To Board At Once"),
    n("Rebel Artillery"),
    n("Rebel Barrier", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Goldenrod"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("The Republic No Longer Functions"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("He Can Go About His Business"),
    n("Wise Advice"),
    n("Ultimatum"),
    n("Your Ship?"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Tatooine: Desert Landing Site"),
    n("Surface Defense", True),
    n("Lott Dod", qty=3),
    n("Toonbuck Toora"),
    n("Edcel Bar Gane"),
    n("Passel Argente"),
    n("Squabbling Delegates", qty=2),
    n("The Phantom Menace"),
    n("A Dark Time For The Rebellion", True),
    n("A Dark Time For The Rebellion"),
    n("Blast Door Controls"),
    n("First Strike"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Count Dooku"),
    n("Emperor Palpatine", qty=2),
    n("Force Lightning"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Dreadnaught-Class Heavy Cruiser", qty=2),
    n("Bossk In Hound's Tooth", True),
    n("Boba Fett In Slave I", True),
    n("Blockade Support Ship"),
    n("Binder"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("Arica", True),
    n("Senate Hovercam"),
    n("The Point Is Conceded"),
    n("4-LOM With Concussion Rifle", True),
    n("Blockade Flagship: Bridge"),
    n("We Must Accelerate Our Plans"),
    n("Endor"),
    n("Naboo: Theed Palace Generator"),
    n("Security Precautions"),
    n("Baskol Yeesrim"),
    n("Imbalance & Kintan Strider"),
    n("Aks Moe"),
    n("Enter The Bureaucrat"),
    n("Control & Set For Stun"),
    n("Imperial Decree", True),
    n("We're In Attack Position Now"),
    n("Overwhelmed"),
    n("Boba Fett, Bounty Hunter"),
    n("Ommni Box & It's Worse"),
    n("Something Special Planned For Them", True),
    n("No Escape"),
    n("Blizzard 4"),
    n("Cold Feet", True),
    n("I Have You Now"),
    n("Close Call", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Vote Of No Confidence"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Allegations Of Corruption"),
    n("Death Star Sentry", True),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
]
DS_ADD = []
