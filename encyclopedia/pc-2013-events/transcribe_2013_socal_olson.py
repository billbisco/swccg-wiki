#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Joe Olson typed Holotable LS+DS with handwritten amendments."""
from __future__ import annotations

PLAYER = "Joe Olson"
USERNAME = "ARebelSpy"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 29
DS_PAGE = 30
LS_SCAN = "2013 SoCal Grand Prix Day 1 p29 Joe Olson LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p30 Joe Olson DS.png"
LS_NOTE = (
    "Typed Holotable printout (not a handwritten Xerox form). Header LS Combat.txt, "
    "signed Joe Olson, username ARebelSpy. A struck line after All Wings Report In "
    "& Darklighter Spin is replaced by handwritten Obi's Jewel (no matching printed "
    "title; not dested). Your Ship? struck, handwritten Do, Or Do Not (shield). "
    "Were You Looking For Me and Threepio With His Parts Showing are handwritten "
    "at the top of the sheet (not counted in the 60)."
)
DS_NOTE = (
    "Typed Holotable printout (not a handwritten Xerox form). Header ds senate space.txt, "
    "signed Joe Olson, username ARebelSpy. First line struck, handwritten Black Sun Fleet. "
    "SFS L-s9.3 Laser Cannons struck, handwritten Coruscant Guard. Vader's Personal Shuttle "
    "struck, handwritten Slave I, Symbol Of Fear. Struck shuttle/hunter line replaced by "
    "Boba Fett, Bounty Hunter. Dr. Evazan struck, handwritten EPP Mara "
    "(Mara Jade With Lightsaber). Darth Vader struck, handwritten EPP "
    "(Darth Vader With Lightsaber). Bottom reminder Ghhk / Fel / EPP Maul / Jango is not "
    "a second list."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("Jedi Levitation", True),
    n("Clinging To The Edge", True),
    n("Seeking An Audience", True),
    n("Caldera Righim", qty=2),
    n("Battle Plan"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Weapon Levitation"),
    n("Let The Wookiee Win", True, qty=3),
    n("Houjix"),
    n("Escape Pod", True, qty=2),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Blaster Deflection"),
    n("Away Put Your Weapon", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("All Wings Report In & Darklighter Spin"),
    n("I'm With You Too", True),
    n("Lightsaber Proficiency"),
    n("Undercover", True),
    n("Imperial Atrocity", True),
    n("Mercenary Armor", True),
    n("Luke's Bionic Hand", qty=2),
    n("Jedi Lightsaber", True),
    n("Qui-Gon's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Artoo-Detoo In Red 5", qty=3),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("Luke Skywalker, Strong In The Force", qty=4),
    n("Naboo: Boss Nass' Chambers"),
    n("Rycar Ryjerd", True),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Heading For The Medical Frigate"),
    n("Inner Strength"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("We'll Handle This / Duel Of The Fates"),
    n("Jabba's Prize"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Aim High"),
    n("Do, Or Do Not"),
]
LS_ADD = []


DS_START = "My Lord, Is That Legal / I Will Make It Legal"
DS_CARDS = [
    n("Black Sun Fleet"),
    n("The Phantom Menace"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Limited Resources"),
    n("Cloud City: Security Tower", True),
    n("Sonic Bombardment", True, qty=2),
    n("Coruscant Guard"),
    n("Squabbling Delegates", qty=3),
    n("We Must Accelerate Our Plans", qty=2),
    n("Mist Hunter", True),
    n("Punishing One", True),
    n("Slave I, Symbol Of Fear"),
    n("Boba Fett, Bounty Hunter"),
    n("Hound's Tooth", True),
    n("Saber 1"),
    n("Accepting Trade Federation Control"),
    n("This Is Outrageous!"),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("Ability, Ability, Ability"),
    n("Combat Response", True, qty=2),
    n("First Strike"),
    n("Senate Hovercam", qty=2),
    n("Blast Door Controls"),
    n("Bossk", True),
    n("Dengar", True),
    n("Mara Jade With Lightsaber"),
    n("Darth Vader With Lightsaber"),
    n("Zuckuss", True),
    n("Baron Soontir Fel"),
    n("Jango Fett, The Assassin"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Yeb Yeb Adem'thorn"),
    n("Tikkes"),
    n("Toonbuck Toora", qty=2),
    n("Passel Argente"),
    n("Baskol Yeesrim"),
    n("Orn Free Taa", qty=2),
    n("Aks Moe"),
    n("Edcel Bar Gane"),
    n("Lott Dod", qty=3),
    n("Blockade Flagship: Bridge"),
    n("Surface Defense", True),
    n("Naboo"),
    n("Tatooine: Desert Landing Site"),
    n("Coruscant: Galactic Senate"),
    n("My Lord, Is That Legal / I Will Make It Legal"),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
    n("Imperial Detention"),
    n("A Useless Gesture", True),
    n("After Her!", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Knowledge And Defense", True),
]
DS_ADD = []
