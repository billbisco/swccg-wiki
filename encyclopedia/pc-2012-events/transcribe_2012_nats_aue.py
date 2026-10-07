#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Devin Aue.

Source: 2012NationalsDay1.pdf pages 3–4 (2010 Xerox, 12 shields).
Name Devin Aue dested Devin Aue as written. Username blank.
p03 Light Night of the Living Gungans / Naboo.
p04 Dark Mystri'l / Agents Of Black Sun.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Devin Aue"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2012 US Nationals Day 1 Devin Aue LS.png"
DS_SCAN = "2012 US Nationals Day 1 Devin Aue DS.png"
LS_DECK_NAME = "Night of the Living Gungans"
DS_DECK_NAME = "Mystri'l"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Devin Aue dested Devin Aue as written. Username blank. "
    "LIGHT checked. Deck Name Night of the Living Gungans. "
    "Naboo dested Naboo (starting location, no Objective). "
    "Wesa Ready to do Oursa Fate dested We're Doomed True. "
    "Senator Jar Jar dested Senator Jar Jar Binks. "
    "Naboo Swamp dested Naboo: Swamp. "
    "Steady Steady dested Steady, Steady. "
    "Away Put Your Weapon dested Away Put Your Weapon. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Rep Been dested Rep Been as written leftover_xerox. "
    "Kaadu dested Kaadu. "
    "Honour of the Jedi dested Honor Of The Jedi. "
    "Antilles Maneuver + Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Your Insight Serves You Well dested in the 60. "
    "Shield You Will Take Me To Jabba Now dested You Will Take Me To Jabba Now True. "
    "Unique overcounts sheet-accurate (Gungan Warrior x2, Gungan General x3, "
    "Electropole x3, Capital Support x3, Rebel Artillery x3, Rebel Leadership x3, "
    "Slight Weapons Malfunction x3, Fambaa x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Devin Aue dested Devin Aue as written. Username blank. "
    "DARK checked. Deck Name Mystri'l. "
    "Agents Of Black Sun empty dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Coruscant (SE) dested Coruscant (Dark). "
    "Scum and Villainy dested Scum And Villainy. "
    "Kitik Keedkak dested Kitik Keed'kak. "
    "Twilek Advisor dested Twi'lek Advisor True. "
    "Omni Box + It's Worse dested Omni Box & It's Worse. "
    "Tonnika Sisters empty vs True kept separate. "
    "Stunning Leader empty vs True kept separate. "
    "Quietly Observing True vs empty kept separate. "
    "Bacht Hyt dested Bacht Hyt as written leftover_xerox. "
    "Rystall dested Rystall analog leftover Chu. "
    "Bossk in Hounds Tooth dested Bossk In Hound's Tooth. "
    "Aurra Sing's Blaster Rifle dested Aurra Sing's Blaster Rifle. "
    "Mara Jade, The Emperor's Hand dested Mara Jade, The Emperor's Hand. "
    "A Bright Center to the Universe dested A Bright Center To The Universe. "
    "Shield Wipe Them Out All of Them dested Wipe Them Out, All Of Them True. "
    "Unique overcounts sheet-accurate (A Dark Time For The Rebellion True x3, "
    "Zuckuss In Mist Hunter x2, Prophetess True x2, Trophy Of A Kill True x2, "
    "Presence Of The Force x2, Limited Resources x2, Stunning Leader True x3 plus empty x1). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Naboo"
LS_CARDS = [
    n("Naboo"),
    n("Careful Planning", True),
    n("Naboo: Boss Nass' Chambers"),
    n("We're Doomed", True),
    n("Wokling", True),
    n("Anger, Fear, Aggression", True),
    n("Senator Jar Jar Binks"),
    n("Luke Skywalker, Jedi Knight", True),
    n("Gungan Warrior", qty=2),
    n("Gungan General"),
    n("Electropole"),
    n("Naboo: Otoh Gunga Entrance"),
    n("Let The Wookiee Win", True),
    n("Home One"),
    n("Naboo: Swamp"),
    n("Gungan General"),
    n("Rebel Artillery"),
    n("Slight Weapons Malfunction"),
    n("Capital Support"),
    n("Rebel Leadership"),
    n("Launching The Assault"),
    n("Capital Support"),
    n("Rebel Artillery"),
    n("Lando Calrissian, Scoundrel"),
    n("Electropole"),
    n("Rebel Leadership"),
    n("Steady, Steady"),
    n("Fambaa"),
    n("Slight Weapons Malfunction"),
    n("Menace Fades"),
    n("Boss Nass"),
    n("Major Hassh'n"),
    n("Captain Tarpals"),
    n("Gungan Energy Shield"),
    n("Electropole"),
    n("Capital Support"),
    n("Han, Chewie, And The Falcon"),
    n("Superficial Damage"),
    n("Scrambled Transmission"),
    n("Away Put Your Weapon"),
    n("Gungan General"),
    n("Leia, Rebel Princess"),
    n("Bright Hope", True),
    n("Your Insight Serves You Well"),
    n("Slight Weapons Malfunction"),
    n("Rep Been"),
    n("Fambaa"),
    n("Kaadu"),
    n("Rebel Leadership"),
    n("Corran Horn"),
    n("Naboo: Battle Plains"),
    n("Gungan Guard"),
    n("Admiral Ackbar", True),
    n("Luke With Lightsaber"),
    n("Rebel Artillery"),
    n("Honor Of The Jedi"),
    n("Jar Jar Binks"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Revolution"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("You Will Take Me To Jabba Now", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan", True),
    n("Weapons Display", True),
    n("Aim High", True),
    n("Do, Or Do Not", True),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Another Pathetic Lifeform", True),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Tonnika Sisters"),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("Information Exchange", True),
    n("Scum And Villainy"),
    n("No Escape"),
    n("No Bargain", True),
    n("Knowledge And Defense"),
    n("Coruscant: Docking Bay"),
    n("A Dark Time For The Rebellion", True),
    n("4-LOM With Concussion Rifle", True),
    n("Spaceport Docking Bay"),
    n("Kitik Keed'kak"),
    n("Twi'lek Advisor", True),
    n("Zuckuss In Mist Hunter"),
    n("Omni Box & It's Worse"),
    n("A Dark Time For The Rebellion", True),
    n("Trophy Of A Kill", True),
    n("Zuckuss In Mist Hunter"),
    n("Stunning Leader", True),
    n("A Dark Time For The Rebellion", True),
    n("Tonnika Sisters", True),
    n("Stunning Leader", True),
    n("Stunning Leader"),
    n("Presence Of The Force"),
    n("Virago"),
    n("Prophetess", True),
    n("Ni Chuba Na??", True),
    n("Weapon Levitation"),
    n("Limited Resources"),
    n("Bacht Hyt"),
    n("Prophetess", True),
    n("Lateral Damage"),
    n("First Strike"),
    n("Quietly Observing", True),
    n("Endor"),
    n("Gardulla The Hutt"),
    n("Always Thinking With Your Stomach"),
    n("Rystall"),
    n("Trophy Of A Kill", True),
    n("Quietly Observing"),
    n("Presence Of The Force"),
    n("Mara Jade's Lightsaber", True),
    n("Arica"),
    n("U-3PO"),
    n("Boba Fett In Slave I", True),
    n("Guri", True),
    n("Stunning Leader", True),
    n("Nevar Yalnal"),
    n("Alter"),
    n("Bossk In Hound's Tooth"),
    n("Aurra Sing's Blaster Rifle"),
    n("Gragra"),
    n("Mara Jade, The Emperor's Hand"),
    n("Aurra Sing", True),
    n("Stinger", True),
    n("Ket Maliss"),
    n("Limited Resources"),
    n("A Bright Center To The Universe"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans", True),
    n("Come Here You Big Coward", True),
    n("Firepower", True),
    n("Battle Order", True),
    n("Allegations Of Corruption"),
    n("There Is No Try", True),
    n("Abyss", True),
    n("Death Star Sentry", True),
    n("Wipe Them Out, All Of Them", True),
    n("Resistance", True),
]
DS_ADD = []
