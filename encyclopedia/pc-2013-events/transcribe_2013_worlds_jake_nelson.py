#!/usr/bin/env python3
"""2013 World Championship Day 2: Jake Nelson Xerox QMC + NMNPND."""
from __future__ import annotations

PLAYER = "Jake Nelson"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 69
DS_PAGE = 68
LS_SCAN = "2013 Worlds Day 2 p69 Jake Nelson LS.png"
DS_SCAN = "2013 Worlds Day 2 p68 Jake Nelson DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields). Jake Nelson. Username blank. "
    "Deck title I will only Play 12 Shields. LIGHT. "
    "Do not dest as Aaron Nelson. "
    "QMC / Independent Operation dested Quiet Mining Colony / Independent Operation. "
    "Ellors Madak dested Ellorrs Madak. Kebye dested Kebyc. "
    "Togit dested Yoxgit. Tebus Sirln dested Leesub Sirln. "
    "Marc Seff dested Harc Seff. Chewie, Walking Carpet dested Chewbacca, Walking Carpet. "
    "What are you trying to Push on us dested What're You Tryin' To Push On Us?. "
    "Path of least resistance + revealed dested Path Of Least Resistance & Revealed. "
    "Projection of a Skywalker dested Projection Of A Skywalker. "
    "All my urchins + Cloud City Celebration dested All My Urchins & Cloud City Celebration. "
    "Down w/ the emperor dested Down With The Emperor!. "
    "Houjix + out of Nowhere dested Houjix & Out Of Nowhere. "
    "Strike force dested Strikeforce. Uutik dested as written. "
    "Simple tricks + nonsense dested Simple Tricks And Nonsense. "
    "Dont do that again dested Don't Do That Again. "
    "Yavin Sentry dested Yavin Sentry. Ultimatum dested Ultimatum. "
    "Form left column reprints 37-38 on lines 39-40 are Rebel Barrier x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Jake Nelson. Username blank. "
    "Deck title These shells are a TRAVESTY. DARK. "
    "Do not dest as Aaron Nelson. "
    "No Money, No Parts, No Deal / YAS? dested "
    "No Money, No Parts, No Deal! / You're A Slave?. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "J'quille dested J'Quille. P-5n dested P-59. "
    "Grovel Storm dested Gravel Storm. "
    "Jr. Evozan written over struck Masterful Move dested Dr. Evazan & Ponda Baba. "
    "Line 37 Emperor Palpatine struck; Sense dested Sense. "
    "Line 38 Garindan and 1st Strike on one slot dested Garindan and First Strike. "
    "Line 39 Wipe Them Out, All Of Them struck omitted. "
    "Ghhhk + Those Rebels wont escape us dested Ghhhk & Those Rebels Won't Escape Us. "
    "A dark time for rebellion dested A Dark Time For The Rebellion. "
    "Knowledge + defense dested Knowledge And Defense. "
    "Additional Oppressive Enforcement and Allegations Of Corruption moved to Dark shields. "
    "Additional Entrance dested Jabba's Palace: Entrance Cavern. "
    "Form left column reprints 37-38 on lines 39-40 overwritten. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("Luke, Trust Me", True),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye", True),
    n("Ellorrs Madak", True),
    n("Lando's Not A System, He's A Man"),
    n("What're You Tryin' To Push On Us?"),
    n("Menace Fades"),
    n("All My Urchins & Cloud City Celebration", True),
    n("Imperial Atrocity", True),
    n("Kebyc", True),
    n("Lobot"),
    n("Pucumir Thryss", True),
    n("Sergeant Edian"),
    n("Yoxgit", True),
    n("Aayla Secura", True),
    n("Dark Approach"),
    n("Caldera Righim", True),
    n("Chewbacca, Walking Carpet", True),
    n("Harc Seff"),
    n("Jar Jar Binks", True),
    n("Han Solo, Innocent Scoundrel", True),
    n("Melas", True),
    n("Sergeant Doallyn"),
    n("Luke With Lightsaber", qty=2),
    n("Tanus Spijek", True),
    n("Leslomy Tacema", True),
    n("Trooper Utris M'Toc", True),
    n("Uutik", True),
    n("2-1B", True),
    n("Leesub Sirln"),
    n("Kal'falnl C'ndros"),
    n("Leia, Rebel Princess", True),
    n("Overseer"),
    n("Rebel Barrier", qty=2),
    n("Path Of Least Resistance"),
    n("Bacta Tank"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Lady Luck"),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Flash Of Insight", True),
    n("Strikeforce", True),
    n("Path Of Least Resistance & Revealed"),
    n("No Questions Asked"),
    n("Down With The Emperor!", True),
    n("Choke"),
    n("Choke", True),
    n("Projection Of A Skywalker"),
    n("Weapon Levitation"),
    n("Landing Claw"),
    n("It Could Be Worse"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Chasm"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display"),
    n("Don't Do That Again"),
    n("Wise Advice"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Yavin Sentry"),
    n("Ultimatum"),
]
LS_ADD = []


DS_START = "No Money, No Parts, No Deal! / You're A Slave?"
DS_CARDS = [
    n("No Money, No Parts, No Deal! / You're A Slave?"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Mos Espa"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("You Cannot Hide Forever"),
    n("Special Delivery", True),
    n("Crossfire", True),
    n("Watto", True, qty=3),
    n("General Nevar", True),
    n("Velken Tezeri", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Darth Vader With Lightsaber", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Mara Jade With Lightsaber", True, qty=2),
    n("Jango Fett, The Assassin", True),
    n("Ket Maliss, Shadow Killer", True),
    n("J'Quille", True),
    n("P-59", True),
    n("Search And Destroy"),
    n("Outflank", True),
    n("Imperial Barrier"),
    n("Outflank", True),
    n("Imperial Barrier"),
    n("Outflank", True),
    n("Imperial Barrier"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sense"),
    n("Garindan"),
    n("First Strike"),
    n("Grand Moff Tarkin", True),
    n("The Phantom Menace"),
    n("Blizzard 4"),
    n("Gravel Storm", True),
    n("Limited Resources"),
    n("Lightsaber Deficiency", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Protocol Failure", True),
    n("Dr. Evazan & Ponda Baba", True),
    n("I Have You Now"),
    n("Executor", qty=2),
    n("Grand Admiral Thrawn"),
    n("Imperial Command", qty=2),
    n("Sith Fury", True),
    n("Sense"),
    n("Jabba's Palace: Dungeon"),
    n("Darth Sidious"),
    n("He Hasn't Come Back Yet"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry"),
    n("Imperial Detention"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Do They Have A Code Clearance?"),
    n("Firepower"),
    n("A Useless Gesture"),
    n("Resistance"),
    n("Abyss"),
    n("Leave Them To Me"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
]
DS_ADD = [
    n("Jabba's Palace: Entrance Cavern"),
]
