#!/usr/bin/env python3
"""2015 European Championship Day 2: Franck Dufreney (place 32).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p31 Dark / p32 Light (2013 PC deck list forms).
"""
from __future__ import annotations

PLAYER = "Franck Dufreney"
USERNAME = "fduff"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 32
DS_PAGE = 31
LS_SCAN = "2015 European Championship Franck Dufreney LS.png"
DS_SCAN = "2015 European Championship Franck Dufreney DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 18-35 p31 Dark / p32 Light, PC deck list forms, circled 32. "
    "Username fduff on both. Event Euro Championship, 17/OCT/15. "
    "Deck Name boxes: DS HDuff, LS TRMDuff (kept off DECK_NAME). DS 1:3 / LS 1:3 handwritten."
)
LS_NOTE = (
    "START Yavin 4: Massissi Throne room dested Yavin 4: Massassi Throne Room. "
    "Posted Anger, Fear, agression dested Anger, Fear, Aggression. "
    "Posted Squadron Assignment dested Squadron Assignments. "
    "Posted Luke My Father Before Me dested Like My Father Before Me. "
    "Posted Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Posted Luke Skywalker Jedi Knight dested Luke Skywalker, Jedi Knight (qty 3 unique overcount sheet-accurate). "
    "Posted Obi-Wan epp dested Obi-Wan With Lightsaber. "
    "Posted Leia Rebel Princess dested Leia, Rebel Princess. "
    "Posted Yoda Keeper of the Peace dested Yoda, Keeper Of The Peace. "
    "Posted Azur Angel dested Azure Angel. "
    "Posted Han, Chewie and the Falcon dested Han, Chewie, And The Falcon. "
    "Posted Impressive Most Impressive dested Impressive, Most Impressive. "
    "Line 53 Put That Down crossed out, handwritten Wesa Gotta Grand Army (V box marked) -> Wesa Gotta Grand Army qty 4. "
    "Shield Wise Advice and Do, Or Do Not are the Defensive Shield versions. "
    "Posted Simple Tricks and Non Sense dested Simple Tricks And Nonsense. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START HD/ their Fire as Gone dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Posted Executor: Holotheater dested Executor: Holotheatre. "
    "Posted 4-Lom epp dested 4-LOM With Concussion Rifle. "
    "Posted Knowledge & Def. dested Knowledge And Defense. "
    "Posted Any Method Necessary dested Any Methods Necessary. "
    "Posted Darth Maul epp dested Darth Maul With Lightsaber (qty 3 overcount sheet-accurate). "
    "Emperor Palpatine qty 3, Darth Vader, Dark Lord Of The Sith qty 3, Count Dooku qty 3 sheet-accurate. "
    "Posted Gran Moff Tarkin dested Grand Moff Tarkin. "
    "Posted Mara Jade epp dested Mara Jade With Lightsaber. "
    "Posted Dengar epp dested Dengar With Blaster Carbine. "
    "Posted Dr Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Posted Allegation of Corruption dested Allegations Of Corruption. "
    "Posted Wipe them out dested Wipe Them Out, All Of Them. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("Draw Their Fire"),
    n("Like My Father Before Me", True),
    n("Nar Shaddaa", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Night Club", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Honor Of The Jedi"),
    n("Civil Disorder", True),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Anakin Skywalker, Padawan Learner", True, qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Luke Skywalker", True),
    n("Leia, Rebel Princess"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda, Keeper Of The Peace", True),
    n("Threepio With His Parts Showing"),
    n("Mace Windu's Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Corran Horn"),
    n("Jar Jar Binks"),
    n("Tantive IV", True),
    n("Azure Angel", True),
    n("Artoo-Detoo In Red 5"),
    n("Red Squadron 1"),
    n("Han, Chewie, And The Falcon"),
    n("X-wing Laser Cannon"),
    n("Wesa Gotta Grand Army", qty=4),
    n("Speak With The Jedi Council", qty=2),
    n("Escape Pod", True),
    n("Rebel Barrier"),
    n("Houjix"),
    n("Impressive, Most Impressive", True),
    n("Hear Me Baby, Hold Together", True),
    n("Sorry About The Mess"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("The Bith Shuffle & Desperate Reach"),
    n("All Wings Report In & Darklighter Spin"),
    n("Were You Looking For Me?"),
    n("Free Ride & Endor Celebration"),
    n("Mindful Of The Future"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Goldenrod", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Ounee Ta"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("The Republic No Longer Functions", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Another Pathetic Lifeform"),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Cloud City: Security Tower", True),
    n("4-LOM With Concussion Rifle", True),
    n("Knowledge And Defense", True),
    n("Any Methods Necessary"),
    n("Tatooine: Cantina"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Visage Of The Emperor", qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Emperor Palpatine", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Count Dooku", True, qty=3),
    n("Maul Strikes", qty=2),
    n("We Must Accelerate Our Plans", qty=4),
    n("Force Field", True, qty=2),
    n("The Phantom Menace", qty=2),
    n("Dooku's Lightsaber", True),
    n("Vader's Lightsaber"),
    n("Force Lightning", qty=2),
    n("Ghhhk"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber", True),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("P-59"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Masterful Move"),
    n("Search And Destroy"),
    n("Weapon Levitation"),
    n("They're Still Coming Through!"),
    n("Sneak Attack", True),
    n("A Dark Time For The Rebellion", True),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("Presence Of The Force"),
    n("Blow Parried"),
    n("Force Push", True),
    n("Sith Fury", True),
    n("First Strike"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Battle Order"),
    n("Wipe Them Out, All Of Them"),
    n("Come Here You Big Coward"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Vote Of No Confidence", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Imperial Detention", True),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Leave Them To Me"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
]
DS_ADD = []
