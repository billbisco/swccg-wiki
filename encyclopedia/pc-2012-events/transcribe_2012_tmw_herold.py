#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Brian Herold.

Source: 2012TMWDay1.pdf pages 3–4 (handwritten 2009 Print Form, 12 shields,
left 1-36 / right 37-60). Name Brian Herold dested Brian Herold analog leftover
2012 Nats/MPC / 2013 Worlds/MPC/TMW/SoCal. Username blank (2009 form has no
Username box). p03 Light Hidden Base. p04 Dark Hunt Down (V).
Do not dest as a new person. Do not dest as Aaron Nelson.
Do not dest 2012 Nats Herold 60s again.
"""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2012 Texas Mini Worlds Day 1 Brian Herold LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Brian Herold DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2009 Print Form (12 shields, left 1-36 / right 37-60). "
    "Name Brian Herold dested Brian Herold analog leftover 2012 Nats/MPC. "
    "Username blank. Event Texas Mini-Worlds. Date blank. "
    "Do not dest as a new person. Do not dest as Aaron Nelson. "
    "Do not dest 2012 Nats Herold 60s again."
)
LS_NOTE = (
    "Handwritten 2009 Print Form. Name Brian Herold dested Brian Herold. "
    "Username blank. LIGHT checked. Deck Title 50 Shades of Green skip. "
    "Hidden Base empty dested Hidden Base. "
    "Nabooo dested Naboo analog leftover Fernando. "
    "Dagobah: Yoda's Hutt dested Dagobah: Yoda's Hut. "
    "Threepio WAPS dested Threepio With His Parts Showing analog leftover Alperstein. "
    "King Kian dested Kin Kian analog leftover Richards. "
    "Mon Cal Star Cruiser dested Mon Calamari Star Cruiser True analog leftover Alperstein qty=5. "
    "Heavy Turbolaser Battery dested analog leftover Alperstein qty=4. "
    "Antilles Maneuver & Rebel Reinforcements dested analog leftover Walseth. "
    "Were You Looking For Me? dested analog leftover mpc. "
    "Stay Sharp dested Stay Sharp! analog leftover Grant B qty=2. "
    "Simple Trix dested Simple Tricks And Nonsense analog leftover Herold. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2009 Print Form. Name Brian Herold dested Brian Herold. "
    "Username blank. DARK checked. Deck Title Gungan + Ewok + Jawa = Gungawokawa skip. "
    "Hunt Down v dested Hunt Down And Destroy The Jedi True. "
    "Coruscant ? (Special Ed) dested Coruscant (Dark) analog leftover Simmering. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi analog leftover Morgan qty=2. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith analog leftover qty=3. "
    "Dr. E & Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover Nats Herold. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Nelson. "
    "Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber. "
    "Victory dested Victory analog leftover mpc qty=2. "
    "Galen's Fighter dested Rogue Shadow analog leftover Shaw. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover Simmering. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Morgan. "
    "Search & Destroy dested Search And Destroy analog leftover Anderson. "
    "A Sith's Weapon dested Weapon Of A Sith analog leftover TMW Herold. "
    "Ni Chuba Na?? v dested Ni Chuba Na?? True analog leftover Simmering. "
    "Gift of The Master dested Gift Of The Master analog leftover Simmering. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover Banger qty=3. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover srodoski. "
    "Sniper & Dark Strike dested analog leftover Richards. "
    "Sense & Uncertain Is The Future dested analog leftover qty=2. "
    "Leave Them 2 Me dested Leave Them To Me True analog leftover Nelson. "
    "Weapon of A Sith shield dested Weapon Of A Sith analog leftover TMW Herold. "
    "Garidan v dested Garidan True leftover_xerox as written. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base"
LS_CARDS = [
    n("Hidden Base"),
    n("Rendezvous Point"),
    n("Heading For The Medical Frigate"),
    n("Superficial Damage", True),
    n("Mon Calamari Dockyards"),
    n("Republic Logistics"),
    n("Sullust"),
    n("Naboo"),
    n("Kessel"),
    n("Kiffex"),
    n("Mon Calamari"),
    n("Chandrila"),
    n("Dagobah"),
    n("Dagobah: Yoda's Hut"),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Captain Verrack"),
    n("Dack Ralter"),
    n("Kin Kian"),
    n("Luke Skywalker", True, qty=2),
    n("Home One"),
    n("Defiant", qty=2),
    n("Liberty"),
    n("Mon Calamari Star Cruiser", True, qty=5),
    n("Heavy Turbolaser Battery", qty=4),
    n("Projection Of A Skywalker", qty=2),
    n("A Jedi's Plans"),
    n("Hindsight", True),
    n("Imperial Atrocity", True, qty=3),
    n("Alter", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Escape Pod", True, qty=2),
    n("On Target", qty=3),
    n("It Could Be Worse"),
    n("We're Doomed"),
    n("Were You Looking For Me?"),
    n("Hear Me Baby, Hold Together", True),
    n("Power Pivot"),
    n("Stay Sharp!", qty=2),
    n("Rebel Barrier", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Another Pathetic Lifeform", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Endor"),
    n("Kashyyyk"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Garidan", True),
    n("General Nevar"),
    n("Dr. Evazan & Ponda Baba"),
    n("The Emperor", True),
    n("Grand Admiral Thrawn"),
    n("Juno Eclipse, Black Leader"),
    n("Mara Jade With Lightsaber"),
    n("Battle Droid Squad", qty=2),
    n("Victory", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Rogue Shadow"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Imperial Propaganda", True),
    n("Search And Destroy"),
    n("Ability, Ability, Ability", True),
    n("Disarmed", qty=2),
    n("Weapon Of A Sith"),
    n("Endor Shield", True),
    n("Protocol Failure"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Gift Of The Master"),
    n("Revenge Of The Sith"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Push", True),
    n("Force Field", True),
    n("Sniper & Dark Strike"),
    n("Sense & Uncertain Is The Future", qty=2),
    n("Stunning Leader"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
]
DS_ADD = []
