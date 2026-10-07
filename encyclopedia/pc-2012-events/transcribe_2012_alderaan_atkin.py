#!/usr/bin/env python3
"""2012 Alderaan Regionals leftover Xerox: Clayton Atkin.

Source: 2012AlderaanRegionals.pdf pages 1–2 (handwritten 2010 Xerox).
Name Clayton Atkin dested Clayton Atkin analog leftover 2013 Alderaan /
2012 MPC / player-stubs/Clayton_Atkin.wiki. Username ditto quotes dested blank.
p01 Light Hidden Base. p02 Dark Hunt Down. Date 7/7/12.
Do not dest as a new person. Do not dest 2013 Alderaan / 2012 MPC Atkin 60s again.
"""
from __future__ import annotations

PLAYER = "Clayton Atkin"
USERNAME = ""
STAGE = ""
PDF = "2012 Alderaan Regionals.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2012 Alderaan Regionals Clayton Atkin LS.png"
DS_SCAN = "2012 Alderaan Regionals Clayton Atkin DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p01 Light / p02 Dark. "
    "Name Clayton Atkin dested Clayton Atkin analog leftover 2013 Alderaan / 2012 MPC. "
    "Username ditto quotes dested blank. Event Alderaan Regional 7/7/12. "
    "Do not dest as a new person. Do not dest 2013 Alderaan / 2012 MPC Atkin 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p01 Light. Name Clayton Atkin dested Clayton Atkin. "
    "Username ditto quotes dested blank. LIGHT checked. "
    "Hidden Base / Systems will Slip dested Hidden Base / Systems Will Slip True. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas True. "
    "LTWW dested Let The Wookiee Win True qty=2. "
    "Luke Skywalker, S.I.T.F. dested Luke Skywalker, Strong In The Force qty=3. "
    "AJR dested A Jedi's Resilience qty=2 analog leftover. "
    "SATM/Blaster Prof dested Sorry About The Mess & Blaster Proficiency analog leftover Anderson. "
    "Jedi Levitation dested Weapon Levitation True analog leftover 2013 Atkin. "
    "Noooooooooooo True qty=2. "
    "Aim High shield crossed skip. Shield 5 crossed dest Another Pathetic Lifeform. "
    "Unique 60 shields 10 sheet-accurate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p02 Dark. Name Clayton Atkin dested Clayton Atkin. "
    "Username ditto quotes dested blank. DARK checked. "
    "Hunt Down / TFHGOOTU dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "The Mandalorian, FOF dested Jango Fett, The Assassin analog leftover 2013 Atkin. "
    "WMAOP dested We Must Accelerate Our Plans qty=3 analog leftover Lush. "
    "Cyborg Commander, HOJ dested Grievous, Hunter Of Jedi qty=2 analog leftover Banger. "
    "Victory True (line 29) and Victory empty (line 30) kept separate. "
    "Ghhhk True (line 14) and Ghhhk empty (line 52) kept separate. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith qty=3 analog leftover Lush. "
    "Vader's Lightsaber dested Darth Vader's Lightsaber analog leftover. "
    "4-lom w/ Concussion Rifle dested 4-LOM With Concussion Rifle True analog leftover Lush. "
    "DEE/Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover Lush. "
    "Ice-Heart dested Ysanne Isard analog leftover 2013 Atkin. "
    "MM/Endor Occupation dested Masterful Move & Endor Occupation analog leftover 2013 Atkin. "
    "Naboo: Theed Palace Gen. Core dested Naboo: Theed Palace Generator Core analog leftover. "
    "CHYBC dested Come Here You Big Coward analog leftover 2013 Atkin. "
    "YCHF dested You Cannot Hide Forever analog leftover Lush. "
    "DTHA Code Clearance dested Do They Have A Code Clearance? analog leftover Lush. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing analog leftover 2013 Atkin. "
    "Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip", True),
    n("Yavin 4", True),
    n("Rebel Cell: Hidden Landing Site"),
    n("Uncharted Settlements"),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Master Qui-Gon", True, qty=2),
    n("Commander Vanden Willard", True),
    n("Sai'torr Kal Fas", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Home One: War Room"),
    n("Launching The Assault"),
    n("Jedi Lightsaber", True),
    n("First Officer Thaneespi"),
    n("Luke's Lightsaber"),
    n("Imperial Atrocity", True, qty=2),
    n("Noooooooooooo", True, qty=2),
    n("Sense & Recoil In Fear", qty=2),
    n("Rebel Cell: Situation Room"),
    n("Let The Wookiee Win", True, qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Quite A Mercenary"),
    n("Rebel Leadership", True, qty=3),
    n("Rebel Barrier"),
    n("Home One"),
    n("Lightsaber Proficiency"),
    n("Admiral Ackbar", True),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan's Journal"),
    n("Han, Chewie, And The Falcon", True),
    n("Leia, Rebel Princess"),
    n("On The Edge"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Rebel Cell: Monitoring Station"),
    n("A Jedi's Resilience", qty=2),
    n("Run Luke Run"),
    n("Bothawui"),
    n("Obi-Wan's Lightsaber"),
    n("Corran Horn"),
    n("Blaster Deflection"),
    n("Leia's Blaster Rifle"),
    n("Undercover", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Luke's Bionic Hand"),
    n("Weapon Levitation", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("Another Pathetic Lifeform"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("I've Lost Artoo", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Imperial Justice", True),
    n("Trophy Of A Kill", qty=2),
    n("Restraining Bolt"),
    n("Revenge Of The Sith"),
    n("Ghhhk", True),
    n("Jango Fett, The Assassin"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("No Escape"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Dark Reconnaissance"),
    n("Sith Fury", True),
    n("Force Field", True, qty=2),
    n("Victory", True),
    n("Victory"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("4-LOM With Concussion Rifle", True),
    n("A Sith's Weapon"),
    n("Naboo: Theed Palace Generator Core"),
    n("General Nevar"),
    n("Grand Admiral Thrawn"),
    n("Dr. Evazan & Ponda Baba"),
    n("Endor"),
    n("Sonic Bombardment", True),
    n("Cold Feet", True),
    n("Ysanne Isard"),
    n("Force Push", True),
    n("Cyborg Commander's Lightsabers"),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk"),
    n("Blaster Rack", True),
    n("Blast Door Controls"),
    n("Battle Droid Squadron"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Sniper & Dark Strike"),
    n("Search And Destroy"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
