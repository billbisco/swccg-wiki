#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Alex W.

Source: 2012mpcday1.pdf pages 141–142 (2010 form, 12 shields).
Name Alex W dested as written analog 2013 leftover PLAYER="Alex W".
Username blank.
p141 Dark Hunt Down And Destroy The Jedi. p142 Light Quiet Mining Colony.
Pack player-stubs/Alex_W.wiki (is_bio False).
Do not dest as a new person.
Do not rewrite 2013 leftover Quiet Mining Colony / Wookiee Slaving Operation.
Do not rewrite 2014 leftover Quiet Mining Colony / Invasion.
"""
from __future__ import annotations

PLAYER = "Alex W"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 142
DS_PAGE = 141
LS_SCAN = "2012 Match Play Championship Day 1 Alex W LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Alex W DS.png"
LS_DECK_NAME = "Quiet leper Colony"
DS_DECK_NAME = "One Mediocre Thing"
NOTE = "Typed 2010 Xerox form."
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Typed 2010 Xerox. Name Alex W dested as written analog 2013 leftover. "
    "Username blank. LIGHT checked. Deck Name Quiet leper Colony. Event MPC Date 2/11/12. "
    "Do not dest as a new person. "
    "Do not rewrite 2013 leftover Quiet Mining Colony / Independent Operation. "
    "Quiet Mining Colony/Independent Operation dested Quiet Mining Colony / Independent Operation empty analog leftover. "
    "AFA True dested Anger, Fear, Aggression True in the 60 analog Casey. "
    "KTEOF True dested Keeping The Empire Out Forever True analog 2013 leftover. "
    "HCF True dested Han, Chewie, And The Falcon True analog leftover. "
    "CC: Guest Quarters dested Cloud City: Guest Quarters analog leftover. "
    "CC: North Corridor dested Cloud City: North Corridor analog leftover. "
    "CC: West Gallery dested Cloud City: West Gallery analog leftover. "
    "CC: Carbonite Chamber dested Cloud City: Carbonite Chamber analog leftover. "
    "It's a Trap dested It's A Trap! analog leftover. "
    "Blast the Door Kid dested Blast The Door, Kid! analog leftover. "
    "Lando's Not a System, He's a Man dested Lando's Not A System, He's A Man analog leftover. "
    "Pucumir Thriss dested Pucumir Thryss analog leftover. "
    "Leia, Rebel Princess dested analog leftover. "
    "Luke with Lightsaber dested Luke With Lightsaber analog leftover. "
    "Rebel Leadership True x3 sheet-accurate. Unique 60. Shields 12. "
    "Traffic Control True dested analog leftover."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Alex W dested as written analog 2013 leftover. "
    "Username blank. DARK checked. Deck Name One Mediocre Thing. Event MPC Date 2/11/12. "
    "Do not dest as a new person. "
    "Do not rewrite 2013 leftover Wookiee Slaving Operation. "
    "HDADTJ/TFHGOTU True dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True analog leftover. "
    "JP: Audience Chamber dested Jabba's Palace: Audience Chamber analog leftover. "
    "JP: Lower Passages dested Jabba's Palace: Lower Passages analog leftover. "
    "Galen, Secret Apprentice True x3 dested as written analog leftover. "
    "Black Leader empty AND True dested Juno Eclipse, Black Leader analog Eier True AND empty kept separate analog Foth. "
    "Dengar with Blaster Carbine True dested Dengar With Blaster Carbine True analog leftover. "
    "4-Lom with Concussion Rifle dested 4-LOM With Concussion Rifle analog leftover. "
    "Galen's Fighter True dested Rogue Shadow True analog leftover. "
    "Galen's Lightsaber, Vader's Gift True dested analog leftover. "
    "Weapon Levitation & Empire's Back True dested Weapon Levitation & The Empire's Back True analog leftover. "
    "Control & Set For Stun crossed Sith Fury dest replacement True analog leftover. "
    "One Beautiful Thing True x2 dested as written analog leftover. Unique 60. Shields 12. "
    "CHYBC dested Come Here You Big Coward analog leftover. "
    "Knowledge and Defense empty dested in the 60 analog leftover."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Heading For The Medical Frigate"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Wokling", True),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever", True),
    n("Booster In Pulsar Skate", True),
    n("Gold Leader In Gold 1", True),
    n("Overseer", True),
    n("Han, Chewie, And The Falcon", True),
    n("Home One"),
    n("Spiral"),
    n("Cloud City: North Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: Carbonite Chamber"),
    n("Home One: War Room"),
    n("Houjix & Out Of Nowhere"),
    n("Alter", True),
    n("It's A Trap!"),
    n("Rebel Leadership", True, qty=3),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Sense"),
    n("Rebel Barrier", qty=2),
    n("Alternatives To Fighting"),
    n("Path Of Least Resistance", qty=2),
    n("Blast The Door, Kid!", qty=2),
    n("Imperial Atrocity", True),
    n("Lando's Not A System, He's A Man"),
    n("Evacuation Control", True),
    n("Cloud City Celebration", qty=2),
    n("Honor Of The Jedi"),
    n("BoShek, Brash Smuggler", True),
    n("Padme Naberrie"),
    n("Leia, Rebel Princess"),
    n("Captain Verrack", True),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Obi-Wan Kenobi", True),
    n("Wedge Antilles", True),
    n("Luke With Lightsaber"),
    n("Lando Calrissian, Scoundrel", True),
    n("Yoda, Great Warrior", True),
    n("Harc Seff", True),
    n("Kebyc", True),
    n("Yoxgit", True),
    n("Lobot", True),
    n("Lando Calrissian", True),
    n("Mirax Terrik"),
    n("Pucumir Thryss"),
    n("Kal'Falnl C'ndros"),
    n("Menace Fades"),
    n("No Questions Asked"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Your Insight Serves You Well"),
    n("Weapons Display", True),
    n("The Professor"),
    n("Affect Mind", True),
    n("Traffic Control", True),
    n("Don't Do That Again"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Prepared Defenses"),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Combat Response", True),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans", True),
    n("Coruscant"),
    n("Tatooine"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Lower Passages"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader", True),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Arica", True, qty=2),
    n("Baron Soontir Fel"),
    n("Juno Eclipse, Black Leader"),
    n("Juno Eclipse, Black Leader", True),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan", True),
    n("Grand Moff Tarkin", True, qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("4-LOM With Concussion Rifle"),
    n("Zuckuss", True),
    n("Rogue Shadow", True),
    n("Saber 1"),
    n("Mist Hunter", True),
    n("Victory", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Mara Jade's Lightsaber"),
    n("Vader's Lightsaber"),
    n("SFS L-s9.3 Laser Cannons"),
    n("One Beautiful Thing", True, qty=2),
    n("Elis Helrot"),
    n("Force Field", True, qty=2),
    n("Stunning Leader"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Masterful Move & Endor Occupation"),
    n("Sniper & Dark Strike"),
    n("You Are Beaten"),
    n("One Bright Spot"),
    n("Sith Fury", True),
    n("Imperial Barrier"),
    n("None Shall Pass", True, qty=2),
    n("Short Range Fighters & Watch Your Back"),
    n("Blaster Rack", True),
    n("Disarmed"),
    n("Ability, Ability, Ability", True),
    n("Sense", qty=2),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("Fanfare"),
    n("Resistance"),
    n("Reactor Terminal"),
]
DS_ADD = []
