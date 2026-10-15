#!/usr/bin/env python3
"""2015 European Championship Day 2: Martin den Boef (place 33).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p33 Dark / p34 Light (2015 PC forms, handwritten).
"""
from __future__ import annotations

PLAYER = "Martin den Boef"
USERNAME = "martindb"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 34
DS_PAGE = 33
LS_SCAN = "2015 European Championship Martin den Boef LS.png"
DS_SCAN = "2015 European Championship Martin den Boef DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 18-35 p33 Dark / p34 Light, handwritten PC forms, circled 33. "
    "Username martindb on both. Event EC Bochum 17/10/15. "
    "Deck Name boxes: DS Agents of Black Sun, LS Profit. DS 1:2 handwritten."
)
LS_NOTE = (
    "START ycyprofit / or be destroyed dested You Can Either Profit By This... / Or Be Destroyed. "
    "Posted Heading for the medical dested Heading For The Medical Frigate. "
    "Posted Sai'tor kal Fas dested Sai'torr Kal Fas. "
    "Posted LSJK dested Luke Skywalker, Jedi Knight. "
    "Posted C-3PO with parts showing dested Threepio With His Parts Showing. "
    "Posted Qui Gonn Jin w lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "Posted Lando w Vibro-Ax dested Lando With Vibro-Ax. "
    "Posted Pricess Leia + Princess Leia dested Princess Leia qty 2 (sheet-accurate). "
    "Posted Chewbacca Protector dested Chewbacca, Protector. "
    "Posted Speak with the jedi dested Speak With The Jedi Council. "
    "Posted A jedi's Resilliance dested A Jedi's Resilience. "
    "Line 44 crossed out, replacement Coruscant: JCC dested Coruscant: Jedi Council Chamber. "
    "Posted The force is strong dested The Force Is Strong With This One. "
    "Posted Alter / friendly Fire dested Alter & Friendly Fire. "
    "Posted Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Posted Tatooine Lars Moisture Farm dested Tatooine: Lars' Moisture Farm. "
    "Shield Professor (V) dested The Professor True; Do or do not dested Do, Or Do Not. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START Aobs/votdp dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Posted Battle order/First strike dested Battle Order & First Strike. "
    "Posted You cannot hide/mob. points dested You Cannot Hide Forever & Mobilization Points. "
    "Posted Imp arrest order/Secret Plans dested Imperial Arrest Order & Secret Plans. "
    "Posted Coruscant Imperial City dested Coruscant: Imperial City True. "
    "Posted DS II: docking bay dested Death Star II: Docking Bay. "
    "Emperor Palpatine qty 6 sheet-accurate overcount. "
    "Posted 4-Lom w conc. Rifle dested 4-LOM With Concussion Rifle qty 2 True. "
    "Posted Boba Fett w. Blaster Rifle dested Boba Fett With Blaster Rifle. "
    "Posted Bossk in Houndtooth dested Bossk In Hound's Tooth. "
    "Posted Ghhhk & those rebels won't dested Ghhhk & Those Rebels Won't Escape Us. "
    "Posted Oh switch off dested Oh, Switch Off. Posted Look sir droids dested Look Sir, Droids. "
    "Posted Control / set for stun dested Control & Set For Stun. "
    "Posted Sense/uncertain is the future dested Sense & Uncertain Is The Future. "
    "Shield line 2 Secret Plans crossed out, Resistance written -> Resistance. "
    "Posted We'll let Fate-a Decide huh? dested We'll Let Fate-a Decide, Huh?. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("I Must Be Allowed To Speak", True),
    n("Sai'torr Kal Fas", True),
    n("Han", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Master Luke", qty=2),
    n("Threepio With His Parts Showing"),
    n("Yoxgit"),
    n("Anakin Skywalker", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Mace Windu", True),
    n("Lando With Vibro-Ax"),
    n("Princess Leia", qty=2),
    n("Chewbacca, Protector"),
    n("Ben Kenobi"),
    n("Corran Horn"),
    n("Owen Lars & Beru Lars"),
    n("Mace Windu's Lightsaber", True),
    n("Landing Claw"),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Anakin's Lightsaber", True),
    n("Obi-Wan's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Bravo Fighter"),
    n("Rebel Barrier", qty=2),
    n("Harvest"),
    n("Jedi Levitation"),
    n("Speak With The Jedi Council", qty=2),
    n("Bacta Tank"),
    n("A Gift"),
    n("Crash Site Memorial"),
    n("A Jedi's Resilience", qty=2),
    n("Wesa Gotta Grand Army"),
    n("Coruscant: Jedi Council Chamber"),
    n("Sense"),
    n("Blaster Deflection"),
    n("Impressive, Most Impressive", True),
    n("Weapon Levitation"),
    n("Someone Who Loves You"),
    n("The Force Is Strong With This One"),
    n("Droid Shutdown"),
    n("Alter & Friendly Fire"),
    n("Were You Looking For Me?"),
    n("Nabrun Leids"),
    n("Lightsaber Proficiency"),
    n("Hear Me Baby, Hold Together"),
    n("Tatooine"),
    n("Naboo: Boss Nass' Chambers"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Another Pathetic Lifeform"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Ounee Ta"),
    n("The Republic No Longer Functions", True),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Prepared Defenses"),
    n("Battle Order & First Strike"),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Coruscant"),
    n("Coruscant: Imperial City", True),
    n("Coruscant: Docking Bay"),
    n("Rendili"),
    n("Death Star II: Docking Bay"),
    n("Prince Xizor", qty=2),
    n("Emperor Palpatine", qty=6),
    n("Guri", qty=2),
    n("Daroe", True),
    n("Vigo", qty=2),
    n("P-59"),
    n("P-60"),
    n("IG-88 With Riot Gun"),
    n("Dengar With Blaster Carbine", True),
    n("4-LOM With Concussion Rifle", True, qty=2),
    n("Jango Fett", True),
    n("Boba Fett With Blaster Rifle"),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Bossk In Hound's Tooth"),
    n("Stinger"),
    n("Boba Fett In Slave I"),
    n("Broken Concentration"),
    n("Jabba's Through With You"),
    n("Main Course"),
    n("Lateral Damage"),
    n("Imperial Barrier", qty=2),
    n("Force Lightning", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("We're The Bait"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Blast Door Controls"),
    n("Projective Telepathy", qty=2),
    n("Oh, Switch Off", qty=2),
    n("Look Sir, Droids"),
    n("Control & Set For Stun", qty=2),
    n("Sense & Uncertain Is The Future"),
    n("Blockade Flagship: Bridge"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("There Is No Try"),
    n("Vote Of No Confidence", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = []
