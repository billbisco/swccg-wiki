#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Hayes Hunter.

Source: 2012mpcday1.pdf pages 89–90 (2010 form).
Name Hayes Hunter dested Hayes Hunter (existing stub).
p89 Light Strike Communing. p90 Dark Chicks w/Dicks courtesy of Eric Hunter.
Username blank. Do not dest as Eric Hunter. Do not dest as Brian Hunter.
Pack player-stubs/Hayes_Hunter.wiki.
"""
from __future__ import annotations

PLAYER = "Hayes Hunter"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 89
DS_PAGE = 90
LS_SCAN = "2012 Match Play Championship Day 1 Hayes Hunter LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Hayes Hunter DS.png"
LS_DECK_NAME = "Strike Communing"
DS_DECK_NAME = "Chicks w/Dicks courtesy of Eric Hunter"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Hayes Hunter dested Hayes Hunter. "
    "Username blank. LIGHT checked. Deck Name Strike Communing. "
    "Event Date 2/11/12 Event Name MPC. "
    "Do not dest as Eric Hunter. Do not dest as Brian Hunter. "
    "Line 1 remnant AFA dested Anger, Fear, Aggression True. "
    "Communing empty dested Communing. "
    "Nick of Time dested Nick Of Time True. "
    "H: Echo Command Center dested Hoth: Echo Command Center (War Room). "
    "T: Obi-Hut dested Tatooine: Obi-Wan's Hut True. "
    "3PO w/ Parts dested Threepio With His Parts Showing. "
    "Chewbacca Protector dested Chewbacca, Protector x3. "
    "Han w/ Heavy Blaster Pistol dested Han With Heavy Blaster Pistol x2. "
    "Home of the Jedi dested Honor Of The Jedi. "
    "GOO NEE TAY dested Goo Nee Tay. "
    "Seizure on Ambition dested Seeking An Audience True. "
    "Sorry Abt The Mess / Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Run Luke Run dested Run Luke, Run! True x2. "
    "Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Hayes Hunter dested Hayes Hunter. "
    "Username blank. LIGHT/DARK boxes empty; dest Dark from the 60s. "
    "Deck Name Chicks w/Dicks courtesy of Eric Hunter. "
    "Event Date 2/11/12 Event Name MPC. "
    "Do not dest as Eric Hunter. Foth analog same Eric Hunter AOBS. "
    "Knowledge + Defense dested Knowledge And Defense True. "
    "AOBS / VotDP dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Coruscant (sped) dested Coruscant (Dark). "
    "Spaceport: DBay dested Spaceport Docking Bay. "
    "C: Private Platform (DB) dested Coruscant: Private Platform (Docking Bay). "
    "Blockade ship: Br. Jag dested Blockade Flagship: Bridge. "
    "4-Lom w/ Rifle dested 4-LOM With Concussion Rifle x2. "
    "Mara Jade Lightsaber dested Mara Jade's Lightsaber. "
    "Retraining Bolt dested Restraining Bolt. "
    "Mara Jade, The Emp Hand dested Mara Jade, The Emperor's Hand x2. "
    "Jabbas Haven dested Jabba's Haven. "
    "Line 40 cropped; dest unique 59. "
    "Line 42 crossed dest Vader's Obsession empty replacement. "
    "Cease Fire dested Cease Fire!. "
    "Elis Helrot True then empty kept separate. "
    "Jabba Through w/ you dested Jabba's Through With You x2. "
    "We Must Accelerate Our Plans x5. "
    "Will of Fate Decide dested We'll Let Fate-a Decide, Huh? True. "
    "Unique 59. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Scrambled Transmission", True),
    n("Strike Planning"),
    n("Nick Of Time", True),
    n("Commando Training & K'lor'slug"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Kashyyyk: Forest Depths"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: City Outskirts"),
    n("Alderaan Consular Ship", qty=2),
    n("Chewbacca's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("General Carlist Rieekan", True),
    n("Senator Mon Mothma"),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Chewbacca, Protector", qty=3),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Leia, Rebel Princess"),
    n("Senator Leia Organa"),
    n("Padme Naberrie", True),
    n("Corran Horn"),
    n("Rebel Gunrunner"),
    n("Security Breach"),
    n("Goo Nee Tay"),
    n("Honor Of The Jedi"),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("Hindsight", True),
    n("Obi-Wan's Apparition", True),
    n("Houjix"),
    n("Grimtaash"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Nabrun Leids"),
    n("Lucky Shot", True),
    n("Inconsequential Barriers", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Sabotage", True),
    n("Too Close For Comfort"),
    n("It's Not My Fault", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Run Luke, Run!", True, qty=2),
]
LS_SHIELDS = [
    n("Aim High", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Shada"),
    n("No Bargain", True),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses", True),
    n("Ket Maliss", True),
    n("I've Lost Artoo", True),
    n("Establish Control", True),
    n("Spaceport Docking Bay"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Blockade Flagship: Bridge"),
    n("Corulag"),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Trophy Of A Kill", qty=2),
    n("Mara Jade's Lightsaber"),
    n("Restraining Bolt"),
    n("Dark Jedi Lightsaber", True),
    n("Sy Snootles", True),
    n("4-LOM With Concussion Rifle", qty=2),
    n("Aurra Sing", qty=3),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Gragra"),
    n("Prophetess", True),
    n("IG-88 With Riot Gun", qty=2),
    n("Gardulla The Hutt", True),
    n("Ability, Ability, Ability"),
    n("Broken Concentration"),
    n("Lateral Damage"),
    n("Jabba's Haven"),
    n("No Escape"),
    n("First Strike"),
    n("Vader's Obsession"),
    n("Tarkin's Bounty", True),
    n("Control & Set For Stun"),
    n("Cease Fire!"),
    n("Elis Helrot", True),
    n("Elis Helrot"),
    n("Imperial Barrier", qty=3),
    n("Stunning Leader", True, qty=2),
    n("Force Push", True),
    n("Jabba's Through With You", qty=2),
    n("We Must Accelerate Our Plans", qty=5),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Imperial Detention", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?", True),
]
DS_ADD = []
