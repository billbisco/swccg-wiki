#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: Brian Herold.

Source: 2012TMWDay2.pdf pages 5–6 (handwritten 2010 Xerox with stickers,
left 1-40 / right 41-60 / 12 shields). Name Brian Herold dested Brian Herold
analog leftover Day 1 CANON / 2012 Nats/MPC. Username Dark Doug Johnson /
Light Wang Brady dested joke handles; USERNAME blank analog leftover Day 1.
p05 Dark Agents Of Black Sun. p06 Light Hidden Base.
Do not dest as a new person. Do not dest as Aaron Nelson.
Do not dest as Doug Johnson. Do not dest as Wang Brady.
Do not dest Day 1 TMW / 2012 Nats / 2012 MPC Herold 60s again.
"""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2012 Texas Mini Worlds Day 2 Brian Herold LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 Brian Herold DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p05 handwritten 2010 Xerox Dark The Bitch Is Back (stickers). "
    "p06 handwritten 2010 Xerox Light Hey ladies! (stickers). "
    "Name Brian Herold dested Brian Herold analog leftover Day 1 CANON. "
    "Username Dark Doug Johnson / Light Wang Brady dested joke handles; USERNAME blank. "
    "Do not dest as a new person. Do not dest as Aaron Nelson. "
    "Do not dest Day 1 TMW / 2012 Nats / 2012 MPC Herold 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p06 Light Deck Name Hey ladies! skip. LIGHT checked. "
    "Event Texas Mini-Worlds Date 4/29/12. Name Brian Herold dested Brian Herold analog leftover Day 1. "
    "Username Wang Brady dested joke handle. "
    "Hidden Base empty dested Hidden Base analog leftover Day 1 Herold. "
    "Superficial Damage dested Superficial Damage analog leftover McCarthy. "
    "Mon Calamari Dockyards dested Mon Calamari: Dockyards analog leftover Alperstein. "
    "Threepio WHPS dested Threepio With His Parts Showing analog leftover Banger. "
    "Dash Ralder dested Dash Rendar analog leftover Richards. "
    "Dagobah: Yoda's Hutt dested Dagobah: Yoda's Hut analog leftover. "
    "Stay Sharp dested Stay Sharp! analog leftover. "
    "Rebel Reinforcements & Antilles Maneuver dested Antilles Maneuver & Rebel Reinforcements analog leftover Walseth. "
    "Were U looking 4 Me dested Were You Looking For Me? analog leftover. "
    "Hear Me Baby Hold Together dested Hear Me Baby, Hold Together analog leftover. "
    "A Jedi's Plans dested analog leftover Alperstein. "
    "Anger, Fear, Aggression dested analog leftover Anderson IN THE 60. "
    "Shield YISYW dested Your Insight Serves You Well analog leftover. "
    "Shield Simple Trix dested Simple Tricks And Nonsense analog leftover Herold. "
    "Shield Your Ship dested Your Ship? analog leftover Jellison. "
    "Additional cards extra systems dested LS_ADD analog leftover Hidden Base extras. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p05 Dark Deck Name The Bitch Is Back skip. DARK checked. "
    "Event Texas Mini-Worlds Day 2 Date 4/28/12. Name Brian Herold dested Brian Herold analog leftover Day 1. "
    "Username Doug Johnson dested joke handle. "
    "Agents Of Black Sun empty dested Agents Of Black Sun analog leftover 2012 MPC Herold. "
    "Coruscant (Special Ed) dested Coruscant (Dark) analog leftover Simmering. "
    "Coruscant?: Imp City dested Coruscant: Imperial City analog leftover. "
    "Coruscant?: Private Platform (DB) dested Coruscant: Private Platform (Docking Bay) analog leftover MPC Herold. "
    "Spaceport DB dested Spaceport Docking Bay analog leftover MPC Herold. "
    "24 sweeties dested Sy Snootles analog leftover MPC Herold. "
    "Cragra dested Gragra analog leftover MPC Herold. "
    "Gardulla The Hut dested Gardulla The Hutt analog leftover. "
    "IG-88 w/ Riot Gun dested IG-88 With Riot Gun analog leftover. "
    "4-LOM w/ Concussion Rifle dested 4-LOM With Concussion Rifle analog leftover. "
    "Retraining Bolt dested Restraining Bolt analog leftover MPC Herold. "
    "Jabba's Through Wit U dested Jabba's Through With You analog leftover MPC Herold. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover MPC Herold qty=5. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover Anderson IN THE 60. "
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
    n("Republic Logistics", True),
    n("Mon Calamari: Dockyards", True),
    n("Kiffex"),
    n("Kessel"),
    n("Naboo"),
    n("Sullust"),
    n("Mon Calamari"),
    n("Chandrila"),
    n("Admiral Ackbar", True),
    n("Luke Skywalker", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Captain Verrack"),
    n("Dash Rendar"),
    n("Kin Kian"),
    n("Home One"),
    n("Liberty"),
    n("Defiant"),
    n("Defiant", True),
    n("Mon Calamari Star Cruiser", True, qty=5),
    n("Heavy Turbolaser Battery", qty=4),
    n("Imperial Atrocity", True, qty=3),
    n("Hindsight", True),
    n("Projection Of A Skywalker", qty=2),
    n("A Jedi's Plans"),
    n("Dagobah: Yoda's Hut"),
    n("Stay Sharp!", qty=2),
    n("Rebel Barrier", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("On Target", qty=3),
    n("Alter", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Were You Looking For Me?"),
    n("We're Doomed"),
    n("It Could Be Worse"),
    n("Power Pivot"),
    n("Escape Pod", True, qty=2),
    n("Dagobah"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Wise Advice"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Another Pathetic Lifeform", True),
    n("Your Ship?"),
]
LS_ADD = [
    n("Kiffex"),
    n("Kessel"),
    n("Naboo"),
    n("Sullust"),
    n("Mon Calamari"),
    n("Chandrila"),
]

DS_START = "Agents Of Black Sun"
DS_CARDS = [
    n("Agents Of Black Sun"),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("Shada"),
    n("No Bargain", True),
    n("Prepared Defenses", True),
    n("Ket Maliss", True),
    n("I've Lost Artoo!", True),
    n("Establish Control", True),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Spaceport Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Corulag"),
    n("Aurra Sing", True),
    n("Aurra Sing", qty=2),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Sy Snootles", True),
    n("Gragra"),
    n("Gardulla The Hutt"),
    n("Prophetess", True),
    n("IG-88 With Riot Gun", qty=2),
    n("4-LOM With Concussion Rifle", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Mara Jade's Lightsaber"),
    n("Restraining Bolt"),
    n("Trophy Of A Kill", qty=2),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Ability, Ability, Ability"),
    n("No Escape"),
    n("Broken Concentration"),
    n("Jabba's Haven"),
    n("First Strike"),
    n("Tarkin's Bounty", True),
    n("Lateral Damage"),
    n("Gift Of The Master"),
    n("Stunning Leader", True, qty=2),
    n("Elis Helrot", qty=2),
    n("Imperial Barrier", qty=3),
    n("Jabba's Through With You", qty=2),
    n("Cease Fire!"),
    n("Force Push", True),
    n("Vader's Obsession"),
    n("Control & Set For Stun"),
    n("We Must Accelerate Our Plans", qty=5),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
]
DS_ADD = []
