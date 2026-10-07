#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Brian Herold.

Source: 2012mpcday1.pdf pages 81–82 (2002 DECK LIST print form).
Name Brian Herold dested Brian Herold (existing stub / generate analog).
p81 Light Yavin 4 (V). p82 Dark Agents Of Black Sun.
Username blank (2002 form). Pack player-stubs/Brian_Herold.wiki.
Do not dest as a new person. Do not rewrite 2013 leftovers
(2013 PLAYER Brian Herold LS Mind What You Have Learned (V) / DS Kessel).
"""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 81
DS_PAGE = 82
LS_SCAN = "2012 Match Play Championship Day 1 Brian Herold LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Brian Herold DS.png"
LS_DECK_NAME = "Attack of the Revenge of the Phantom Sith Clone Menace"
DS_DECK_NAME = "Eric Hunter's Restore Feminism To The Galaxy"
NOTE = "Handwritten 2002 DECK LIST print form."
LS_NOTE = (
    "Handwritten 2002 DECK LIST. Name Brian Herold dested Brian Herold. "
    "Username blank. LIGHT checked. Event MPC Date Feb 11, 2012. "
    "Deck Title Attack of the Revenge of the Phantom Sith Clone Menace. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Yavin 4 v dested Yavin 4 True. "
    "Communing dested Communing. "
    "Coruscant (EP1) dested Coruscant (Coruscant). "
    "Tatooine (EP1) dested Tatooine (Coruscant). "
    "Yavin 4: Massassi War Room non-V dested empty. "
    "Biggs, Legendary Rogue Legend dested Biggs, Rogue Legend. "
    "Krug Krang dested Krug Krang. "
    "Lt. Tarn Mison dested Lieutenant Tarn Mison. "
    "Phylo Gandish v dested Phylo Gandish True. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Red Squadron 7 v dested Red Squadron 7 True. "
    "Rogue Squadron X-Wing dested Rogue Squadron X-Wing x6. "
    "Dual Laser Cannon v dested Dual Laser Cannon True. "
    "Enhanced Proton Torpedoes v dested Enhanced Proton Torpedoes True. "
    "Restore Freedom To The Galaxy dested Restore Freedom To The Galaxy. "
    "Strikeforce crossed, Man Flaps v dested Maneuvering Flaps True. "
    "It's Not My Fault v dested It's Not My Fault! True x3. "
    "AFA v dested Anger, Fear, Aggression True. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2002 DECK LIST. Name Brian Herold dested Brian Herold. "
    "Username blank. DARK checked. Event MPC Date Feb 11, 2012. "
    "Deck Title Eric Hunter's Restore Feminism To The Galaxy. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Agents Of Black Sun dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Coruscant (Special Ed) dested Coruscant. "
    "No Bargain v dested No Bargain True. "
    "Prepared Defenses v dested Prepared Defenses True. "
    "Gurdulla The Hutt v dested Gardulla The Hutt True. "
    "4-LOM w/ Concussion Rifle dested 4-LOM With Concussion Rifle x2. "
    "IG-88 with Riot Gun dested IG-88 With Riot Gun x2. "
    "Retraining Bolt dested Restraining Bolt. "
    "I've Lost Artoo! v dested I've Lost Artoo! True. "
    "Tarkin's Bounty Virtual dested Tarkin's Bounty True. "
    "Control & Set For Stun dested Control & Set For Stun. "
    "Force Push v dested Force Push True. "
    "Jabba's Through With You dested Jabba's Through With You x2. "
    "Stunning Leader v dested Stunning Leader True x2. "
    "We Must Accelerate Our Plans x5 sheet-accurate. "
    "Knowledge & Defense v dested Knowledge And Defense True. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Communing"),
    n("Coruscant (Coruscant)"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Yavin 4: Briefing Room"),
    n("Yavin 4: Massassi War Room"),
    n("Biggs, Rogue Legend"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Commander Wedge Antilles", True),
    n("Corran Horn"),
    n("Dack Ralter", True),
    n("Dash Rendar", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Jek Porkins", True),
    n("Keir Santage"),
    n("Krug Krang"),
    n("Lieutenant Tarn Mison"),
    n("Phylo Gandish", True),
    n("Master Kenobi"),
    n("Yoda, Great Warrior"),
    n("Red 6"),
    n("Red Squadron 7", True),
    n("Rogue Squadron X-Wing", qty=6),
    n("Rogue 1", qty=2),
    n("Dual Laser Cannon", True),
    n("Enhanced Proton Torpedoes", True),
    n("Rebel Aces"),
    n("Restore Freedom To The Galaxy"),
    n("Echo Base Garrison"),
    n("Imperial Atrocity", True, qty=4),
    n("Massassi Base Sentry"),
    n("Obi-Wan's Apparition", True),
    n("Rebel Fleet"),
    n("Rebel Gunrunner"),
    n("Squadron Assignments"),
    n("Maneuvering Flaps", True),
    n("The Camp"),
    n("It's Not My Fault!", True, qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Organized Attack", qty=3),
    n("Power Pivot", qty=2),
    n("Use The Force"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Shada"),
    n("No Bargain", True),
    n("Prepared Defenses", True),
    n("Corulag"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Spaceport Docking Bay"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Aurra Sing", qty=3),
    n("Gardulla The Hutt", True),
    n("Gragra"),
    n("Prophetess", True),
    n("Sy Snootles", True),
    n("4-LOM With Concussion Rifle", qty=2),
    n("IG-88 With Riot Gun", qty=2),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Mara Jade's Lightsaber"),
    n("Restraining Bolt"),
    n("Trophy Of A Kill", qty=2),
    n("Ability, Ability, Ability"),
    n("Blast Door Controls"),
    n("Broken Concentration"),
    n("Establish Control", True),
    n("First Strike"),
    n("Gift Of The Master"),
    n("I've Lost Artoo!", True),
    n("Jabba's Haven"),
    n("Ket Maliss", True),
    n("Lateral Damage"),
    n("No Escape"),
    n("Tarkin's Bounty", True),
    n("Cease Fire!"),
    n("Control & Set For Stun"),
    n("Elis Helrot", qty=2),
    n("Force Push", True),
    n("Imperial Barrier", qty=3),
    n("Jabba's Through With You", qty=2),
    n("Stunning Leader", True, qty=2),
    n("We Must Accelerate Our Plans", qty=5),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
