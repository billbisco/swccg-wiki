#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Steve Baroni.

Source: 2012mpcday2.pdf pages 9–10.
p09 notebook remainder HDADTJ-v Dark Hunt Down (V). Vertical BARONI / SAME ONE B-FRED match note.
p10 Light empty Same as Yesterday ~ Bug Hug skip card text analog leftover TMW Shaw.
Username blank. Do not dest as Brian Fred. Do not dest as a new person.
Do not rewrite Day 1 leftover Hunt Down / Communing.
Pack player-stubs/Steve_Baroni.wiki.
"""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = ""
DS_SCAN = "2012 Match Play Championship Day 2 Steve Baroni DS.png"
LS_DECK_NAME = "Same as Yesterday ~ Bug Hug"
DS_DECK_NAME = "HDADTJ-v"
LS_PUBLIC_NOTE = "Same as Yesterday ~ Bug Hug"
NOTE = "Handwritten notebook remainder Dark. Light empty Same as Yesterday."
LS_NOTE = (
    "p10 Light empty Same as Yesterday ~ Bug Hug. Name Baroni dested Steve Baroni analog leftover. "
    "Username blank. LIGHT. Main 60 blank except Same as Yesterday. No Light 60. "
    "Do not dest as Brian Fred. Do not dest as a new person. "
    "Do not duplicate Day 1 leftover Communing. Hub Light stays empty. "
    "Do not rewrite Day 1 leftover Communing."
)
DS_NOTE = (
    "Handwritten notebook remainder. Vertical BARONI dested Steve Baroni analog leftover. "
    "Username blank. Event Day 2 MPC. Deck Name HDADTJ-v. DARK. "
    "Vertical SAME ONE B-FRED is a match note vs Brian Fred; dest BARONI as Steve Baroni. "
    "Do not dest as Brian Fred. Do not dest as a new person. "
    "Do not rewrite Day 1 leftover Hunt Down. "
    "HDADTJ - v dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True analog leftover Baroni/Chu IN THE 60 AND START. "
    "Blizz 4 dested Blizzard 4 analog leftover Baroni Day 1. "
    "D.S. war room - v dested Death Star II: Throne Room True analog leftover Bordier. "
    "NABOO: TPGC dested Naboo: Theed Palace Generator Core analog leftover Chu. "
    "Cor: Imp. City dested Coruscant: Imperial City analog leftover Nelson/Chu. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge analog leftover Harpster/Chu. "
    "Coruscant dested Coruscant analog leftover Foth. "
    "I have you now dested I Have You Now analog leftover Anis. "
    "Prepared Defenses dested analog leftover IN THE 60. "
    "A Sith's Plans dested analog leftover Alperstein/Chu. "
    "Blaster Rack - v dested Blaster Rack True analog leftover Harpster. "
    "Gift of the Master dested Gift Of The Master analog leftover Chu. "
    "N. Chuba Na ?? - v dested Ni Chuba Na?? True analog leftover Chu. "
    "Imperial Justice - v dested Imperial Justice True analog leftover. "
    "Ability Ability Ability - v dested Ability, Ability, Ability True analog leftover Shaw. "
    "Imperial Propaganda - v CROSSED skipped. "
    "Wipe Them Out All Of Them - v dested Wipe Them Out, All Of Them True analog leftover Baroni/Chu. "
    "First Strike dested analog leftover. "
    "Force Lightning dested analog leftover Bordier. "
    "Cold Feet - v dested Cold Feet True analog leftover. "
    "Stop Motion - v dested Stop Motion True analog leftover Brodsky/Booker. "
    "No Escape dested analog leftover. "
    "Masterful Move & Endor Occupation dested analog leftover Chu/Harpster. "
    "Force Push - v dested Force Push True analog leftover. "
    "Force Field - v dested Force Field True analog leftover unique overcount. "
    "Revenge of the Sith dested Revenge Of The Sith analog leftover unique overcount. "
    "We Must Accelerate Our Plans x3 analog leftover Harpster/Chu. "
    "Blast Door Controls dested analog leftover. "
    "Emperor's Power - v dested Emperor's Power True analog leftover. "
    "Counter Detection - v CROSSED skipped. "
    "DISARMED dested Disarmed analog leftover Walter unique overcount. "
    "Imperial Barrier dested analog leftover unique overcount. "
    "4-LOM - v dested 4-LOM With Concussion Rifle True analog leftover Foth. "
    "Dengar w/ Blaster Carbine - v dested Dengar With Blaster Carbine True analog leftover Alex W. "
    "Dr. Evazan & Ponda Baba dested analog leftover Shaw/Chu. "
    "Boba Fett B.H. dested Boba Fett, Bounty Hunter analog leftover Booker. "
    "Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber analog leftover Chu. "
    "P-59 dested analog leftover. "
    "Cyborg Commander, HoJ dested Grievous, Hunter Of Jedi analog leftover Chu/Shaw unique overcount. "
    "Galen, SA dested Galen, Secret Apprentice analog leftover Shaw unique overcount. "
    "Emperor Palpatine dested analog leftover unique overcount. "
    "Darth Vader, BOTJ dested Darth Vader, Betrayer Of The Jedi analog leftover Chu/Field unique overcount. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Chu. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover Chu. "
    "Vader's Lightsaber dested analog leftover. "
    "Knowledge & Defense - v dested Knowledge And Defense True analog leftover Murray IN THE 60. "
    "Sith Fury (v) dested Sith Fury True. "
    "Restraining Bolt dested analog leftover. "
    "Empire's New Order (v) dested Empire's New Order True analog leftover 2014 Tom H. "
    "Shield D.S. Sentry v dested Death Star Sentry True analog leftover. "
    "Shield Battle Order dested analog leftover. "
    "Shield Lack of Faith v dested I Find Your Lack Of Faith Disturbing True analog leftover Ziagos. "
    "Shield Abyss dested analog leftover. "
    "Shield Secret Plans dested analog leftover. "
    "Shield Allegations dested Allegations Of Corruption analog leftover. "
    "Shield Oppressive Enforcement dested analog leftover. "
    "Shield Coward dested Come Here You Big Coward analog leftover. "
    "Shield Weapon of Sith dested Weapon Of A Sith analog leftover. "
    "Shield YCHF dested You Cannot Hide Forever analog leftover. "
    "Shield Code Clearance dested Do They Have A Code Clearance? analog leftover. "
    "Unique overcounts sheet-accurate. Unique 60. Shields 11 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Blizzard 4"),
    n("Death Star II: Throne Room", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Coruscant: Imperial City"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant"),
    n("I Have You Now"),
    n("Prepared Defenses"),
    n("A Sith's Plans"),
    n("Blaster Rack", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Imperial Justice", True),
    n("Ability, Ability, Ability", True),
    n("Wipe Them Out, All Of Them", True),
    n("First Strike"),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("No Escape"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Force Field", True, qty=2),
    n("Revenge Of The Sith", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Blast Door Controls"),
    n("Emperor's Power", True),
    n("Disarmed", qty=2),
    n("Imperial Barrier", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Bounty Hunter"),
    n("Mara Jade With Lightsaber"),
    n("P-59"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Emperor Palpatine", qty=3),
    n("Darth Vader, Betrayer Of The Jedi", qty=3),
    n("Grievous' Lightsabers"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Knowledge And Defense", True),
    n("Sith Fury", True),
    n("Restraining Bolt"),
    n("Empire's New Order", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever"),
    n("Do They Have A Code Clearance?"),
]
DS_ADD = []
