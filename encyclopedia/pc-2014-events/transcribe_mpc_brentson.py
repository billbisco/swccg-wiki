#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Steve Brentson.

Source: MPC-2014-Day-1-Main-Event.pdf pages 21–22 (2013 form, 15 shields).
Username blank. Deck names Endor Ops / Palace Raiders.
"""
from __future__ import annotations

PLAYER = "Steve Brentson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 22
DS_PAGE = 21
LS_SCAN = "2014 Match Play Championship Day 1 Steve Brentson LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Steve Brentson DS.png"
LS_DECK_NAME = "Palace Raiders"
DS_DECK_NAME = "Endor Ops"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name S. Brentson dested Steve Brentson. Username blank. "
    "PROFIT dested You Can Either Profit By This... / Or Be Destroyed. Heading For Med "
    "Frig dested Heading For The Medical Frigate. Anakin Skywalker, PL dested Anakin "
    "Skywalker, Padawan Learner. I Must Be Allowed To Speak dested I Must Be Allowed To "
    "Speak. Jabba large AC dested Jabba's Palace: Audience Chamber. Jabba's Palace dested "
    "Tatooine: Jabba's Palace. Home Echo dested "
    "Hoth: Echo Command Center. 3PO Parts Showing dested Threepio With His Parts Showing. "
    "Mace MOTO dested Mace Windu, Master Of The Order. Unique overcounts sheet-accurate "
    "(Anakin Skywalker, Padawan Learner (V) x2, Leia, Rebel Princess x2, Obi-Wan Kenobi "
    "(V) x2, Clash Of Sabers x2, Droid Shutdown x2, Let The Wookiee Win (V) x3, Luke "
    "Skywalker, Jedi Knight x2, It's A Trap! x2, Rebel Leadership (V) x3, Mace Windu, "
    "Master Of The Order (V) x2, Wesa Gotta Grand Army x2, Sense x3). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name S. Brentson dested Steve Brentson. Deck Endor Ops. "
    "Wookiee Slaving dested Wookiee Slaving Operation / Indentured To The Empire. Potion "
    "of the Hut dested Tatooine: Jabba's Palace. Gardulla The Hutt dested Gardulla The "
    "Hutt. ORS dested Outer Rim Scout. Velken Tezeri dested Velken Tezeri. Reegesh dested "
    "Reegesh. Lightsaber Def dested Lightsaber Deficiency. Bargaining/Malakili dested "
    "Malakili. Kashyyyk slaver sites dested Kashyyyk: Wookiee Slaving Camp (unique "
    "overcount x3). Wookiee Subjugation dested Wookiee Subjugation. Physical Choke dested "
    "Physical Choke. LSD dested Lightsaber Deficiency. P-59 dested P-59. Unique overcounts "
    "sheet-accurate (Kashyyyk: Wookiee Slaving Camp (V) x3, Outer Rim Scout x5, "
    "Lightsaber Deficiency (V) x4, Imperial Barrier x3, Sonic Bombardment (V) x3, IG-88 "
    "With Riot Gun x2, Bantha Herd (V) x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Heading For The Medical Frigate"),
    n("A Gift"),
    n("Blaster Deflection"),
    n("Seeking An Audience", True),
    n("Anakin Skywalker, Padawan Learner", True, qty=2),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Leia, Rebel Princess", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Ben Kenobi"),
    n("Padme Naberrie", True),
    n("I Must Be Allowed To Speak", True),
    n("Clash Of Sabers", qty=2),
    n("Quick Draw", True),
    n("Droid Shutdown", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Tatooine: Lars' Moisture Farm", True),
    n("It's A Trap!", qty=2),
    n("Harc Seff", True),
    n("Anakin's Lightsaber", True),
    n("Inconsequential Barriers"),
    n("Admiral Ackbar", True),
    n("Rebel Leadership", True, qty=3),
    n("Jedi Levitation", True),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Chewbacca, Protector"),
    n("Threepio With His Parts Showing"),
    n("Anakin's Lightsaber"),
    n("Sense", qty=3),
    n("Sai'torr Kal Fas", True),
    n("Hoth: Echo Command Center"),
    n("Home One: War Room"),
    n("Disarmed"),
    n("Lando Calrissian, Scoundrel"),
    n("Double Agent"),
    n("Shmi Skywalker", True),
    n("Home One"),
    n("Luke Skywalker"),
    n("Obi-Wan's Lightsaber"),
    n("Corran Horn"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Planetary Defenses", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Den Of Thieves", True),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Haven", True),
    n("Mercenary Slavers", True),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Kashyyyk"),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Nal Hutta"),
    n("Scum And Villainy"),
    n("Dr. Evazan & Ponda Baba"),
    n("Gardulla The Hutt", True),
    n("Prince Xizor"),
    n("Slave I, Symbol Of Fear", True),
    n("P-59"),
    n("Boba Fett, Prepared Hunter", True),
    n("IG-88 With Riot Gun", True),
    n("Jabba's Space Cruiser", True),
    n("Outer Rim Scout", qty=5),
    n("Jabba The Hutt", True),
    n("Hutt Bounty"),
    n("Jabba's Sail Barge", True),
    n("Mara Jade With Lightsaber"),
    n("Mercenary Pilot", True),
    n("Velken Tezeri", True),
    n("Reegesh", True),
    n("Lightsaber Deficiency", True, qty=4),
    n("Malakili", True),
    n("Wookiee Subjugation", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Bantha Herd", True, qty=2),
    n("IG-88 With Riot Gun"),
    n("Imperial Barrier", qty=3),
    n("Kett Maliss", True),
    n("Zuckuss In Mist Hunter"),
    n("4-LOM With Concussion Rifle"),
    n("Garindan", True),
    n("Physical Choke", True),
    n("Cold Feet", True),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament"),
    n("Dengar With Blaster Carbine", True),
    n("Bossk With Mortar Gun", True),
    n("Ghhhk", True),
    n("Lady Valarian"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Detention", True),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Resistance"),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
