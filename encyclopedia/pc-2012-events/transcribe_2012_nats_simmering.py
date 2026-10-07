#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Conrad Simmering.

Source: 2012NationalsDay1.pdf pages 70–71 (typed 2010 Xerox, 12 shields).
p70 Dark / p71 Light Name Conrad Simmering Username Maul12555 dested Conrad Simmering
analog leftover 2013 Worlds. Pack player-stubs/Conrad_Simmering.wiki.
Do not dest as Alden Peterson. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Conrad Simmering"
USERNAME = "Maul12555"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 71
DS_PAGE = 70
LS_SCAN = "2012 US Nationals Day 1 Conrad Simmering LS.png"
DS_SCAN = "2012 US Nationals Day 1 Conrad Simmering DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed 2010 Xerox. Name Conrad Simmering dested Conrad Simmering analog leftover 2013 Worlds. "
    "Username Maul12555. Event Date 6/9/12 Event Name Nationals. Do not dest as Alden Peterson."
)
LS_NOTE = (
    "Typed 2010 Xerox. Name Conrad Simmering dested Conrad Simmering analog leftover 2013 Worlds. "
    "Username Maul12555. LIGHT checked. Event Date 6/9/12 Event Name Nationals. "
    "Deck Name QMC stays off the article. "
    "LS_START Quiet Mining Colony analog leftover Nieland. "
    "Padme Naberrie dested Padmé Naberrie True analog leftover Schoenthal. "
    "Path Of The Least Resistance dested Path Of Least Resistance analog leftover Nieland x4. "
    "OOC&TT dested Out Of Commission & Transmission Terminated analog leftover Olson. "
    "The Bith Shuffle combo dested The Bith Shuffle & Desperate Reach analog leftover Nelson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Nelson IN THE 60. "
    "Shield 12 Ounee Ta dested analog leftover Morgan. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Conrad Simmering dested Conrad Simmering analog leftover 2013 Worlds. "
    "Username Maul12555. DARK checked. Event Date 6/9/12 Event Name Nationals. "
    "Deck Name Hunt Down (v) stays off the article. "
    "DS_START Hunt Down And Destroy The Jedi True dested Hunt Down And Destroy The Jedi (V). "
    "Coruscant SE dested Coruscant (Dark) analog leftover Jan. "
    "Prepared Defences dested Prepared Defenses analog leftover. "
    "Ni Chuba Na?? dested Ni Chuba Na?? True analog leftover 2014 Worlds Anderson. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi analog leftover Morgan x3. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover George. "
    "Sence & Uncertain Is The Future dested Sense & Uncertain Is The Future analog leftover. "
    "He Is Not Ready & Imperial Propaganda dested analog leftover McCune. "
    "Galen's Fighter dested Rogue Shadow analog leftover George. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Morgan. "
    "Knowledge And Defence dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Shield 12 Fanfare dested Fanfare True analog leftover Shannon. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony"
LS_CARDS = [
    n("Quiet Mining Colony"),
    n("Cloud City: Guest Quarters"),
    n("Bespin"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Wokling", True),
    n("Kal'Falnl C'ndros"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel"),
    n("Pucumir Thryss"),
    n("Padmé Naberrie", True),
    n("Corran Horn"),
    n("Harc Seff", True),
    n("Kebyc", True, qty=2),
    n("Tanus Spijek", True),
    n("Escape Pod", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Blaster Deflection", qty=2),
    n("Grimtaash"),
    n("Path Of Least Resistance", qty=4),
    n("Narrow Escape", qty=2),
    n("Off The Edge"),
    n("Rebel Barrier"),
    n("Out Of Commission & Transmission Terminated"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Alternatives To Fighting", qty=3),
    n("Dodge", qty=3),
    n("It Could Be Worse"),
    n("Clash Of Sabers"),
    n("Scrambled Transmission", True),
    n("Hindsight", True),
    n("Cloud City Celebration"),
    n("Imperial Atrocity", True),
    n("Cloud City: North Corridor"),
    n("Cloud City: Carbonite Chamber"),
    n("Wedge In Red Squadron 1"),
    n("Gold Leader In Gold 1", True),
    n("Overseer"),
    n("Tantive IV", True),
    n("Landing Claw"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Chasm"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("The Professor"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Ounee Ta"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant: Imperial City"),
    n("Coruscant (Dark)"),
    n("A Sith's Plans"),
    n("Prepared Defenses"),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine", qty=3),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("General Nevar"),
    n("Juno Eclipse, Black Leader"),
    n("Admiral Ozzel"),
    n("Grand Admiral Thrawn"),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Force Field", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Lightning"),
    n("Sneak Attack", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("The Circle Is Now Complete"),
    n("Force Push", True),
    n("One Beautiful Thing"),
    n("Sense & Uncertain Is The Future"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Image Of The Dark Lord", True),
    n("Revenge Of The Sith"),
    n("Imperial Justice", True),
    n("First Strike"),
    n("Search And Destroy"),
    n("A Sith's Weapon"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
    n("Naboo: Theed Palace Generator Core"),
    n("Coruscant: Palpatine's Quarters"),
    n("Victory"),
    n("Rogue Shadow"),
    n("Grievous' Lightsabers"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Trophy Of A Kill"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Battle Order"),
    n("Resistance"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Imperial Detention"),
    n("Firepower"),
    n("Fanfare", True),
]
DS_ADD = []
