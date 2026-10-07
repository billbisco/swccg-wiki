#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Vikram Bali.

Source: 2012mpcday1.pdf pages 43–44 (2010 form, 12 shields).
Name Vikram Bali dested Vikram Bali. Username DVD ROTS.
p43 Light Anger, Fear, Aggression. p44 Dark Hunt Down (V).
Do not dest as a new person. Do not rewrite 2013 leftovers.
Do not skip as 2013 Worlds Bali empty Same as Yesterday (2012 sheets have 60s).
"""
from __future__ import annotations

PLAYER = "Vikram Bali"
USERNAME = "DVD ROTS"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 43
DS_PAGE = 44
LS_SCAN = "2012 Match Play Championship Day 1 Vikram Bali LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Vikram Bali DS.png"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Vikram Bali dested Vikram Bali. "
    "Username DVD ROTS. Event MPC 2012. LIGHT checked. Deck Name blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Line 1 Yavin 4: Massassi Throne Room. Line 2 Anger, Fear, Aggression True. "
    "LS_START Anger, Fear, Aggression matching 2013 Worlds analog. "
    "Honor of the Jedi dested Honor Of The Jedi. "
    "Naboo: Boss Nass' Chambers dested Naboo: Boss Nass' Chambers. "
    "Qui-Gon Jinn w/ Lightsaber dested Qui-Gon Jinn With Lightsaber x2. "
    "Obi-Wan w/ Lightsaber dested Obi-Wan With Lightsaber x2. "
    "Luke w/ Lightsaber dested Luke With Lightsaber x2. "
    "Padme Naberrie dested Padmé Naberrie True. "
    "Threepio w/ His Parts Showing dested Threepio With His Parts Showing. "
    "Han, Chewie, & the Falcon dested Han, Chewie, And The Falcon empty + True. "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1 True. "
    "Strike Force dested Strikeforce True. "
    "Down with the Emperor! dested Down With The Emperor! True. "
    "Let the Wookiee Win dested Let The Wookiee Win True x3. "
    "A Jedi's Resilience dested A Jedi's Resilience x3. "
    "Do or Do Not dested Do, Or Do Not. Unique 60. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Vikram Bali dested Vikram Bali. "
    "Username DVD ROTS. Event MPC 2012. DARK checked. Deck Name blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Hunt Down and Destroy the Jedi/TFHGOOTU True dested Hunt Down And Destroy "
    "The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "Knowledge & Defense True dested Knowledge And Defense True in the 60. "
    "Coruscant (Special Edition) dested Coruscant. "
    "<>Storm Clouds dested Storm Clouds x2. <<>Clouds dested Clouds. "
    "Floating Refinery dested Tibanna Floating Refinery True x2. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Galen's Fighter dested Rogue Shadow. "
    "OS-72-1 in Obsidian 1 dested OS-72-1 In Obsidian 1. "
    "OS-72-2 in Obsidian 2 dested OS-72-2 In Obsidian 2. "
    "Dark Maneuvers & Tallon Roll dested Dark Maneuvers & Tallon Roll x3. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back x2. "
    "Ghhhk & Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us x2. "
    "One Beautiful Thing dested as written. "
    "A Dark Time for the Rebellion dested A Dark Time For The Rebellion True x2. "
    "Fanfare dested Fanfare True. Abyss dested Abyss True. "
    "A Useless Gesture dested A Useless Gesture True. "
    "Firepower dested Firepower True. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "Do They Have A Code Clearance? dested Do They Have A Code Clearance? True. "
    "Unique 60. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
    n("Podrace Prep"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Anakin's Podracer"),
    n("Goo Nee Tay"),
    n("Honor Of The Jedi"),
    n("I Did It!"),
    n("Malastare"),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Yavin 4: Massassi War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Leia", True),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Padmé Naberrie", True),
    n("Ki-Adi-Mundi", True),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Tantive IV", True),
    n("Spiral"),
    n("Han, Chewie, And The Falcon"),
    n("Han, Chewie, And The Falcon", True),
    n("Wedge In Red Squadron 1"),
    n("Gold Leader In Gold 1", True),
    n("Civil Disorder", True),
    n("Draw Their Fire"),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Revolution", qty=5),
    n("Down With The Emperor!", True),
    n("A Vergence In The Force"),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience", qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Were You Looking For Me?"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Knowledge And Defense", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses"),
    n("Combat Response"),
    n("I'm Sorry", True),
    n("Endor Shield", True),
    n("Endor"),
    n("Storm Clouds", qty=2),
    n("Clouds"),
    n("Tibanna Floating Refinery", True, qty=2),
    n("Darth Vader With Lightsaber", qty=3),
    n("DS-61-2"),
    n("DS-61-3"),
    n("Juno Eclipse, Black Leader"),
    n("Baron Soontir Fel"),
    n("OS-72-10"),
    n("Admiral Ozzel"),
    n("General Veers", True),
    n("Myn Kyneugh", True),
    n("Rogue Shadow"),
    n("Black 2", True),
    n("Black 3", True),
    n("Saber 1"),
    n("Obsidian 10", True),
    n("Obsidian 7"),
    n("Obsidian 8"),
    n("OS-72-1 In Obsidian 1"),
    n("OS-72-2 In Obsidian 2"),
    n("Blizzard 4", True, qty=2),
    n("Presence Of The Force"),
    n("Royal Escort", True),
    n("Lateral Damage"),
    n("Protocol Failure", qty=2),
    n("Dark Maneuvers & Tallon Roll", qty=3),
    n("All Power To Weapons", qty=3),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Atmospheric Assault", True),
    n("Force Push", True),
    n("One Beautiful Thing"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Operational As Planned", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("You Cannot Hide Forever"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
