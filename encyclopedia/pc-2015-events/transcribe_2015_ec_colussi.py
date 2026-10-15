#!/usr/bin/env python3
"""2015 European Championship Day 2: Massimiliano Colussi (place 29).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p25 DS / p26 LS typed-in deck list forms (2013 form).
"""
from __future__ import annotations

PLAYER = "Massimiliano Colussi"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2015 European Championship Massimiliano Colussi LS.png"
DS_SCAN = "2015 European Championship Massimiliano Colussi DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #29 (circled). Typed forms, name handwritten 'Massimiliano Colussi', event 'EC 2015', no username. "
    "DS deck name 'Chokk that!', DS 0:4. LS deck name 'RST Talz', LS 3:1 (corrected from DS 0), header note 'A DDM DECK!'. "
    "LS form has neither LIGHT nor DARK ticked."
)
LS_NOTE = (
    "Typed 60 + 15 shields; several typed lines crossed out with handwritten replacements (replacements dested). "
    "Posted Endor: Rebel Landing Site dested Endor: Rebel Landing Site (Forest). "
    "Posted Sai'Tor Kal'Fass dested Sai'torr Kal Fas. "
    "Line 25 Obi-Wan In Radiant VII crossed -> 'Arcona'. Line 26 Clash Of Sabers crossed -> Luke Skywalker, Jedi Knight. "
    "Posted Nar Shadda Wind Chimes x3 dested Nar Shaddaa Wind Chimes. "
    "Line 41 Sorry About The Mess & Blaster Proficiency crossed -> 'JL'; lines 42-43 Weapon Levitation crossed -> Jedi Levitation; dested Jedi Levitation x3. "
    "Line 44 We Wish To Board At Once crossed -> The Signal. Line 45 same crossed -> 'General Madine' dested General Crix Madine. "
    "Line 56 Draw Their Fire crossed -> Obi-Wan's Lightsaber. "
    "Line 57 Civil Disorder crossed -> Obi-Wan Kenobi; (V) box ticked (was Civil Disorder's), kept True. "
    "Posted K'lor Slug dested K'lor'slug. Line 59 I Hope She's Alright crossed -> Mace Windu (no V). "
    "Line 60 Anger, Fear, Aggression crossed -> Lando Calrissian Scoundrel; (V) box ticked, kept True. "
    "Posted A Tragedy Has Occured dested A Tragedy Has Occurred."
)
DS_NOTE = (
    "Typed 60 + 15 shields. "
    "Posted Death Star: Docking Bay dested Death Star: Docking Bay 327. "
    "Posted You Cannot Hide Forever & Mobilization P. dested You Cannot Hide Forever & Mobilization Points. "
    "Posted Dreadnaught x4 dested Dreadnaught-Class Heavy Cruiser. Posted Tie Interceptor x8 / Tie Scout x2 dested TIE Interceptor / TIE Scout. "
    "Posted WED-15-I7 'Septoid Droid' x2 dested WED15-l7 'Septoid' Droid. Posted U-3PO dested U-3PO (Yoo-Threepio). "
    "Posted Dreaded Imperial Fleet dested Dreaded Imperial Starfleet. "
    "Posted We'll Let Fate Decide, Huh ? dested We'll Let Fate-a Decide, Huh?."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rebel Strike Team / Garrison Destroyed"
LS_CARDS = [
    n("Rebel Strike Team / Garrison Destroyed"),
    n("Endor"),
    n("Endor: Rebel Landing Site (Forest)"),
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("The Shield Is Down!"),
    n("Sai'torr Kal Fas", True),
    n("Endor: Back Door"),
    n("Endor: Bunker"),
    n("Talz", qty=3),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Corran Horn"),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Arcona"),
    n("Luke Skywalker, Jedi Knight"),
    n("Houjix"),
    n("Nabrun Leids", qty=2),
    n("Throw Me Another Charge", qty=3),
    n("Escape Pod", True, qty=2),
    n("Sense", qty=3),
    n("Nar Shaddaa Wind Chimes", qty=3),
    n("Jedi Levitation", qty=3),
    n("The Signal"),
    n("General Crix Madine"),
    n("Under Attack"),
    n("Scramble"),
    n("Deactivate The Shield Generator"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Mace Windu's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Explosive Charge", qty=3),
    n("Obi-Wan's Lightsaber"),
    n("K'lor'slug", True),
    n("Mace Windu"),
    n("Lando Calrissian, Scoundrel", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Affect Mind", True),
    n("Battle Plan"),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
    n("Goldenrod"),
    n("The Republic No Longer Functions"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Your Ship?"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Alderaan"),
    n("Death Star: Docking Bay 327"),
    n("Prepared Defenses"),
    n("Kuat Drive Yards", True),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("Imperial Justice", True),
    n("Death Star: War Room"),
    n("Naboo"),
    n("Sullust"),
    n("Kashyyyk"),
    n("Endor"),
    n("Dreadnaught-Class Heavy Cruiser", qty=4),
    n("TIE Interceptor", qty=8),
    n("TIE Scout", qty=2),
    n("Chokk", qty=2),
    n("WED15-l7 'Septoid' Droid", qty=2),
    n("Imperial Trooper Guard Dainsom", qty=2),
    n("SFS L-s9.3 Laser Cannons", qty=4),
    n("Heavy Fire Zone", qty=3),
    n("Flawless Marksmanship", qty=3),
    n("Short Range Fighters", qty=2),
    n("Imperial Barrier", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Force Push", True),
    n("Wakeelmui"),
    n("U-3PO (Yoo-Threepio)"),
    n("Blizzard 4", qty=2),
    n("Sienar Fleet Systems", qty=2),
    n("Inconsequential Losses"),
    n("Dreaded Imperial Starfleet"),
    n("Lateral Damage"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Battle Order"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Imperial Detention", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?"),
    n("Vote Of No Confidence"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Resistance"),
]
DS_ADD = []
