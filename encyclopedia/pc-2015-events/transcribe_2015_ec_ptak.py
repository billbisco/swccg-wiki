#!/usr/bin/env python3
"""2015 European Championship Day 2: Piotr Ptak (place 25).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p17 DS / p18 LS handwritten deck list forms.
"""
from __future__ import annotations

PLAYER = "Piotr Ptak"
USERNAME = "Mr. Bind"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 18
DS_PAGE = 17
LS_SCAN = "2015 European Championship Piotr Ptak LS.png"
DS_SCAN = "2015 European Championship Piotr Ptak DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place #25. Forms signed 'Piotr Ptak', event 'EC Bochum 2015', date 10/16/15. "
    "Username 'Mr. Bind' on both (could be 'Mr. Blind'; DS deck-name box has 'Blind' overwritten). "
    "DS deck name 'DSC by Mr. Bind', DS 1:3. LS deck name 'LSG by Mr. Bind', LS 2:2."
)
LS_NOTE = (
    "Form 60 lines + 15 shields. "
    "TITLE MISMATCH: wiki says Combat Preparedness, sheet starts We'll Handle This / Flip (Duel Of The Fates). "
    "Posted We'll Handle This/Flip dested We'll Handle This / Duel Of The Fates. "
    "REVIEWED: CONFIRM line 3 \"Naboo: 3/2 site\" dested Naboo: Theed Palace Generator Core (only 3/2 Naboo site; objective deploys it). "
    "REVIEWED: CONFIRM line 4 \"Naboo: 2/2 site\" dested Naboo: Theed Palace Generator (objective deploys Generator + Core). "
    "Posted Anakin Skywalker, PL dested Anakin Skywalker, Padawan Learner. Posted LSJK x3 dested Luke Skywalker, Jedi Knight. "
    "REVIEWED: CONFIRM line 22 \"Threepio - Naked\" dested Threepio With His Parts Showing. "
    "Posted Luke's Bionic Hand x2 kept. Posted Qui-Gon's Lightsaber x2 kept as written. "
    "Posted R2-D2 in Red 5 x2 dested Artoo-Detoo In Red 5. Posted Hold Me Baby, Hold Together dested Hear Me Baby, Hold Together. "
    "Posted A Tragedy Has Ocurred dested A Tragedy Has Occurred. Posted Only Jedi Carry This Weapon dested Only Jedi Carry That Weapon. "
    "Posted Planetary Defences dested Planetary Defenses."
)
DS_NOTE = (
    "Form 60 lines + 15 shields. "
    "TITLE MISMATCH: wiki says Combat Readiness, sheet starts Let Them Make The First Move (/ At Last We Will Have Revenge). "
    "Line 44 Alter crossed out, replaced at foot by '44. Omni Box & It's Worse' dested Ommni Box & It's Worse. "
    "Line 49 The Ebb Of Battle crossed out, replaced at foot by '49. A Dark Time For The Rebellion (V)'. "
    "REVIEWED: CONFIRM line 3 \"Naboo: 3/2 site\" dested Naboo: Theed Palace Generator Core (only 3/2 Naboo site; objective deploys it). "
    "REVIEWED: CONFIRM line 4 \"Naboo: 2/2 site\" dested Naboo: Theed Palace Generator (objective deploys Generator + Core). "
    "REVIEWED: CONFIRM line 28 \"U-3PO\" dested U-3PO (Yoo-Threepio). "
    "Posted Blaster Rock dested Blaster Rack. Posted Evader / Monnok dested Evader & Monnok. "
    "Posted Maul's Double Stick x2 dested Maul's Double-Bladed Lightsaber. Posted Dooku's Lightsaber kept. "
    "Posted Imperial Detention box ticked (V) as on sheet. Posted Weapon Of A Sith in shields kept."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Inner Strength"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Podrace Prep"),
    n("Anger, Fear, Aggression", True),
    n("Sai'torr Kal Fas", True),
    n("Anakin Skywalker, Padawan Learner", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("Mace Windu", True, qty=2),
    n("Yoda, Master Of The Force"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Threepio With His Parts Showing"),
    n("Weapon Of A Fallen Mentor"),
    n("Projection Of A Skywalker", qty=2),
    n("Like My Father Before Me", True),
    n("A Jedi's Resilience", qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Jedi Levitation", True, qty=2),
    n("Sense", qty=2),
    n("Alter", True),
    n("Escape Pod", True),
    n("Dodge"),
    n("Rebel Barrier"),
    n("Blast The Door, Kid!"),
    n("Houjix"),
    n("Blaster Deflection"),
    n("Hear Me Baby, Hold Together", True),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Anakin's Podracer", qty=2),
    n("Luke's Bionic Hand", qty=2),
    n("Mace Windu's Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Qui-Gon's Lightsaber", qty=2),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Naboo: Boss Nass' Chambers"),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Planetary Defenses"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("The Republic No Longer Functions", True),
    n("Simple Tricks And Nonsense", True),
    n("Goldenrod", True),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Aim High"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Let Them Make The First Move / At Last We Will Have Revenge"
DS_CARDS = [
    n("Let Them Make The First Move / At Last We Will Have Revenge"),
    n("Deep Hatred"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("According To My Design", True),
    n("Knowledge And Defense", True),
    n("Wipe Them Out, All Of Them"),
    n("Crush The Rebellion"),
    n("Blaster Rack", True),
    n("Emperor Palpatine", qty=3),
    n("Lord Maul", qty=4),
    n("Count Dooku", True, qty=2),
    n("Mara Jade With Lightsaber", True, qty=2),
    n("Janus Greejatus", qty=2),
    n("P-59", qty=2),
    n("Mosep", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("U-3PO (Yoo-Threepio)"),
    n("Sith Fury", True),
    n("Masterful Move"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Field"),
    n("Force Field", True),
    n("I Have You Now", qty=2),
    n("Force Push"),
    n("Evader & Monnok"),
    n("Ghhhk"),
    n("Force Lightning"),
    n("Stunning Leader", qty=2),
    n("Ommni Box & It's Worse"),
    n("Sense", qty=2),
    n("The Ebb Of Battle", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Maul Strikes"),
    n("Search And Destroy"),
    n("The Phantom Menace", qty=4),
    n("Disarmed"),
    n("Dooku's Lightsaber", True),
    n("Maul's Double-Bladed Lightsaber", qty=2),
    n("Blockade Flagship: Bridge"),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?"),
    n("Vote Of No Confidence"),
    n("Come Here You Big Coward"),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
