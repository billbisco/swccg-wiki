#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Mike Richards.

Source: 2012TMWDay1.pdf pages 1–2 (typed 2010 Xerox, 12 shields).
Name Michael Richards dested Mike Richards analog leftover 2012 MPC / 2013 TMW CANON.
Username mr007agent. p01 Light Yavin 4. p02 Dark Invasion.
Do not dest as a new person. Do not dest 2012 MPC Richards 60s again.
"""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "mr007agent"
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2012 Texas Mini Worlds Day 1 Mike Richards LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Mike Richards DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed 2010 Xerox. Name Michael Richards dested Mike Richards analog leftover 2012 MPC. "
    "Username mr007agent. Event Date 04/28/12 Event Name TMW 2012. "
    "Do not dest as a new person. Do not dest 2012 MPC Richards 60s again."
)
LS_NOTE = (
    "Typed 2010 Xerox. Name Michael Richards dested Mike Richards analog leftover 2012 MPC. "
    "Username mr007agent. LIGHT checked. Deck Name Freedom Jizz skip. "
    "Yavin IV True dested Yavin 4 True analog leftover MPC Richards. "
    "Restore Freedom dested Restore Freedom To The Galaxy analog leftover Grant B virtual-only IN THE 60. "
    "Tatoooine (Coruscant) dested Tatooine (Coruscant) analog leftover grouty. "
    "Tatooine: Obi's Hut dested Tatooine: Obi-Wan's Hut True analog leftover Herold. "
    "Yoda GW dested Yoda, Great Warrior True analog leftover Stenerson. "
    "Derek 'Hobbie' Klivian dested Derek \"Hobbie\" Klivian True analog leftover Herold. "
    "It's Not My Fault dested analog leftover MPC Richards True qty=3. "
    "Bigg's Rogue Leader dested Biggs' Rogue Squadron True analog leftover MPC Richards. "
    "Strikeforce dested Strike Force True analog leftover pistone. "
    "Master Kenobi dested analog leftover Stenerson True. "
    "AFA dested Anger, Fear, Aggression True analog leftover MPC Richards IN THE 60. "
    "Yavin IV: Massassi War Room dested Yavin 4: Massassi War Room analog leftover Herold. "
    "Yavin IV: Briefing Room dested Yavin 4: Briefing Room analog leftover Herold. "
    "Coruscant (Coruscant) dested Coruscant analog leftover MPC Richards. "
    "Shield Simple Trix dested Simple Tricks And Nonsense True analog leftover Herold. "
    "Shield Let's Keep A Little Optimism dested Let's Keep A Little Optimism Here True analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Michael Richards dested Mike Richards analog leftover 2012 MPC. "
    "Username mr007agent. DARK checked. Deck Name Double D Invasion skip. "
    "Invasion dested Invasion / In Complete Control analog leftover Buck. "
    "Where are those droidekas dested Where Are Those Droidekas? True analog leftover Tony. "
    "Search & Destroy dested Search And Destroy analog leftover Anderson. "
    "Oh Switch Off dested Oh, Switch Off analog leftover srodoski qty=2. "
    "Short Range Combo dested Short Range Fighters & Watch Your Back! analog leftover. "
    "Those Rebels won't escape us dested Those Rebels Won't Escape Us True analog leftover. "
    "Rolling Rolling Rolling dested Rolling, Rolling, Rolling analog leftover srodoski qty=2. "
    "Sniper Combo dested Sniper & Dark Strike analog leftover MPC Richards. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover srodoski. "
    "Master Destroyers dested Master, Destroyers! analog leftover srodoski qty=2. "
    "3720 to 1 dested 3,720 To 1 True analog leftover gemme / shaw. "
    "Self Destruct Mechanism dested Self-Destruct Mechanism analog leftover srodoski. "
    "Nute Gunray, Viceroy dested Nute Gunray, Neimoidian Viceroy analog leftover srodoski. "
    "Blockade Flagship (Virtual) True dested Blockade Flagship True analog leftover srodoski. "
    "Knowledge & Defense dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Naboo: Battle Plains (LS) dested Naboo: Battle Plains analog leftover srodoski. "
    "Masterful Move combo dested Masterful Move & Endor Occupation analog leftover. "
    "Shield You Cannot hide Forever dested You Cannot Hide Forever True analog leftover. "
    "Shield We'll Let Fate Decide, Huh dested analog leftover. Shield 12 clipped skip. "
    "Unique 60. Shields 11 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Imperial Atrocity", True, qty=4),
    n("Obi-Wan's Apparition", True),
    n("Power Pivot", qty=2),
    n("Phylo Gandish", True),
    n("Organized Attack", qty=3),
    n("Keir Santage"),
    n("Massassi Base Sentry", True),
    n("Yoda, Great Warrior", True),
    n("Rogue Squadron X-wing", True, qty=6),
    n("Rogue 1", qty=2),
    n("Yavin 4: Massassi War Room"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Kin Kian"),
    n("Derek \"Hobbie\" Klivian", True),
    n("Dash Rendar", True),
    n("It's Not My Fault", True, qty=3),
    n("Restore Freedom To The Galaxy"),
    n("Rebel Aces", True),
    n("The Camp", True),
    n("Biggs' Rogue Squadron", True),
    n("Tatooine: City Outskirts"),
    n("Commander Wedge Antilles", True),
    n("Communing", True),
    n("Hear Me Baby, Hold Together", True),
    n("Use The Force", True, qty=2),
    n("Red 6"),
    n("Coruscant"),
    n("Strike Force", True),
    n("Jek Porkins", True),
    n("Corran Horn"),
    n("Master Kenobi", True),
    n("Squadron Assignments"),
    n("Rebel Fleet"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Lieutenant Tarn Mison"),
    n("Dack Ralter", True),
    n("Echo Base Garrison"),
    n("Enhanced Proton Torpedoes", True),
    n("Yavin 4: Briefing Room"),
    n("Red Squadron 7", True),
    n("Rebel Gunrunner", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business"),
]
LS_ADD = []

DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Droid Racks", True),
    n("You Cannot Hide Forever"),
    n("At Last We Are Getting Results", True),
    n("Where Are Those Droidekas?", True),
    n("Darth Maul"),
    n("Maul's Sith Infiltrator"),
    n("Blockade Flagship: Bridge"),
    n("Outflank", True),
    n("Naboo: Theed Palace Throne Room"),
    n("Search And Destroy"),
    n("Destroyer Droid", qty=9),
    n("P-59", qty=2),
    n("P-60", qty=2),
    n("Stinger", True),
    n("Naboo: Theed Palace Courtyard"),
    n("Guri", qty=2),
    n("Daultay Dofine", True),
    n("Forced Servitude"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Blockade Support Ship", True),
    n("Self-Destruct Mechanism"),
    n("Oh, Switch Off", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Those Rebels Won't Escape Us", True),
    n("Abyssin Ornament"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Elis Helrot"),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Sniper & Dark Strike"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Master, Destroyers!", qty=2),
    n("3,720 To 1", True),
    n("P-13 & P-14", True),
    n("Wounded Warrior", qty=2),
    n("Naboo: Battle Plains"),
    n("Crossfire"),
    n("Masterful Move & Endor Occupation"),
    n("Tey How"),
    n("Prepared Defenses"),
    n("Naboo"),
    n("Naboo: Swamp"),
    n("Blockade Flagship", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Secret Plans"),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("We'll Let Fate Decide, Huh"),
]
DS_ADD = []
