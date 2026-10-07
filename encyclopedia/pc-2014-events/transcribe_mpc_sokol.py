#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Matt Sokol.

Source: MPC-2014-Day-1-Main-Event.pdf pages 104–105 (2013 form, 15 shields).
Name Sokol dested Matt Sokol. Username blank.
"""
from __future__ import annotations

PLAYER = "Matt Sokol"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 105
DS_PAGE = 104
LS_SCAN = "2014 Match Play Championship Day 1 Matt Sokol LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Matt Sokol DS.png"
LS_DECK_NAME = "light"
DS_DECK_NAME = "Duc"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Sokol dested Matt Sokol. Username blank. LIGHT checked. "
    "Deck name light. QMC dested Quiet Mining Colony / Independent Operation. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. Jan Ors Binks dested Jar Jar Binks. "
    "Lubat dested as written. Cull Falla Clndras dested Kal'Falnl C'ndros. "
    "AMU & CCC dested All My Urchins & Cloud City Celebration. AWRI & DS dested "
    "All Wings Report In & Darklighter Spin. Alternatives to Fighting dested Choke. "
    "Unique overcounts sheet-accurate (Luke With Lightsaber x2, Lando Calrissian, Unlikely Hero x2, "
    "Choke x2, Rebel Barrier x3, Path Of Least Resistance x2, Let The Wookiee Win (V) x2). "
    "NO_DEST Lubat (V); Path Of Least Resistance & Recovered. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Sokol dested Matt Sokol. Username blank. DARK checked. "
    "Deck name Duc. HD (V) dested Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V). "
    "Storm Cloud line Imperial Barrier replacement dested Imperial Barrier (V). "
    "Abyssin Ornament replacement Imperial Barrier dested Imperial Barrier. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back!. "
    "Saber Squad TIE dested Saber Squadron TIE. Unique overcounts sheet-accurate "
    "(Protocol Failure x2, Imperial Propaganda (V) x2, Ghhhk & Those Rebels Won't Escape Us x2, "
    "All Power To Weapons x4, Lightsaber Deficiency (V) x3, Short Range Fighters & Watch Your Back! x3, "
    "One Beautiful Thing x2, Never Tell Me The Odds x2, Sonic Bombardment (V) x2, "
    "Saber Squadron TIE x3, U-3PO (Yoo-Threepio) x2, Saber Squadron Pilot x3). NO_DEST Never Tell Me The Odds; Tibanna Floating Refuge; Buboicullaar. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Overseer"),
    n("Errant Venture"),
    n("Booster In Pulsar Skate"),
    n("Lady Luck"),
    n("Landing Claw"),
    n("Luke With Lightsaber", qty=2),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Aayla Secura"),
    n("Foul Moudama"),
    n("Tawss Khaa"),
    n("Han Solo, Innocent Scoundrel"),
    n("Melas", True),
    n("Caldera Righim"),
    n("Leesub Sirln", True),
    n("Leia, Rebel Princess"),
    n("Kebyc", True),
    n("Jar Jar Binks"),
    n("Lubat", True),
    n("Dash Rendar", True),
    n("Leslomy Tacema", True),
    n("Mirax Terrik"),
    n("Kal'Falnl C'ndros"),
    n("Sergeant Edian", True),
    n("Yoxgit"),
    n("Trooper Utris M'Toc", True),
    n("Tanus Spijek", True),
    n("Chewbacca, Walking Carpet"),
    n("Ellor's Madak", True),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("All My Urchins & Cloud City Celebration"),
    n("Dark Approach", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Desperate Reach", True),
    n("Choke", qty=2),
    n("Rebel Barrier", qty=3),
    n("Houjix & Out Of Nowhere"),
    n("Clash Of Sabers"),
    n("Path Of Least Resistance & Recovered"),
    n("Path Of Least Resistance", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Heading For The Medical Frigate", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry"),
    n("The Professor"),
    n("Your Insight Serves You Well"),
    n("Affect Mind"),
    n("Planetary Defenses", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Chasm"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Jabba's Prize"),
    n("Ultimatum"),
    n("Aim High"),
    n("Do, Or Do Not", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Bespin"),
    n("Coruscant: Imperial City"),
    n("Cloud City: Security Tower", True),
    n("Bespin: Cloud City"),
    n("Storm Cloud", True),
    n("Imperial Barrier", True),
    n("Protocol Failure", qty=2),
    n("Imperial Propaganda", True, qty=2),
    n("A Sith's Plans"),
    n("Ni Chuba Na??", True),
    n("Combat Response", True),
    n("I'm Sorry", True),
    n("Prepared Defenses"),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Force Push", True),
    n("All Power To Weapons", qty=4),
    n("Lightsaber Deficiency", True, qty=3),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("One Beautiful Thing", qty=2),
    n("Never Tell Me The Odds", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Imperial Barrier"),
    n("Tibanna Floating Refuge"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Saber Squadron TIE", qty=3),
    n("Saber 4"),
    n("Rogue Shadow"),
    n("Saber 1"),
    n("Jango Fett, The Assassin"),
    n("Arica"),
    n("Buboicullaar"),
    n("Keder The Black"),
    n("U-3PO (Yoo-Threepio)", qty=2),
    n("Juno Eclipse, Black Leader"),
    n("Saber Squadron Pilot", qty=3),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Sonic Bombardment", True),
    n("Keder The Black"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement", True),
    n("Resistance", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans", True),
    n("You Cannot Hide Forever"),
    n("Do They Have A Code Clearance"),
    n("Battle Order"),
    n("Fanfare"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Abyss"),
    n("Firepower"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
