#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Ganden Yanaga Xerox LS+DS.

Sheet name Camden Yanaga / Cam Solusar. Light deck Cloud Age Symphony The Encore.
"""
from __future__ import annotations

PLAYER = "Ganden Yanaga"
USERNAME = "Cam Solusar"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 45
DS_PAGE = 46
LS_SCAN = "2013 SoCal Grand Prix Day 1 p45 Ganden Yanaga LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p46 Ganden Yanaga DS.png"
LS_NOTE = (
    "Handwritten Xerox form. Sheet name Camden Yanaga (username Cam Solusar). "
    "Deck title Cloud Age Symphony The Encore. HFTMF → Heading For The Medical Frigate. "
    "KTEOF → Keeping The Empire Out Forever. Lando UH → Lando Calrissian, Unlikely Hero. "
    "Houjix & OON → Houjix & Out Of Nowhere. Ellorrs Madak written in Japanese then (Elors). "
    "Uutkik as Uutkik. POLR → Path Of Least Resistance. NQA → No Questions Asked. "
    "AWRI & DS → All Wings Report In & Darklighter Spin. Alter (Cor) → Alter. "
    "Chewbacca Of Kashyyyk (sheet scrawl). (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Xerox form. Sheet name Camden Yanaga (username Cam Solusar). "
    "Deck title I<3:1. Endor Operations / Imperial Outpost. Endor: LP → Endor: Landing Platform "
    "(Docking Bay). IAO & SP → Imperial Arrest Order & Secret Plans. "
    "TT Oh-No! → Oh, Switch Off!. Control & SFS → Control & Set For Stun. "
    "Japanese (GMT) → Grand Moff Tarkin. Maarek Stele, TER → Maarek Stele, The Emperor's Reach. "
    "DSII sites as Death Star II. WMAOP → We Must Accelerate Our Plans. "
    "K&D → Knowledge And Defense. Tatooine (Cor) → Tatooine. "
    "Black Leader → Juno Eclipse, Black Leader. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Alternatives To Fighting"),
    n("Booster In Pulsar Skate"),
    n("Seeking An Audience", True),
    n("Dark Approach", True, qty=2),
    n("Luke With Lightsaber"),
    n("Strikeforce", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Landing Claw"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Lady Luck"),
    n("Rebel Barrier", qty=2),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Dash Rendar", True),
    n("Mirax Terrik"),
    n("Desperate Reach", True),
    n("It's A Trap!"),
    n("Leia, Rebel Princess"),
    n("Imperial Atrocity", True),
    n("Ellorrs Madak", True),
    n("Overseer"),
    n("Errant Venture"),
    n("Cloud City: West Gallery"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: North Corridor"),
    n("Kal'Falnl C'ndros"),
    n("Leesub Sirln", True),
    n("Kebyc", True),
    n("Tanus Spijek", True),
    n("Uutkik", True),
    n("Sergeant Edian", True),
    n("Yoxgit"),
    n("Trooper Utris M'toc", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Aayla Secura", qty=2),
    n("Caldera Righim"),
    n("Lobot", True),
    n("Chewbacca Of Kashyyyk"),
    n("No Questions Asked"),
    n("Leslomy Tacema", True),
    n("Harc Seff", True),
    n("Melas", True),
    n("Path Of Least Resistance & Revealed"),
    n("Path Of Least Resistance"),
    n("Choke"),
    n("Alter", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("Jabba's Prize"),
]
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Bunker"),
    n("Operational As Planned"),
    n("Death Star II"),
    n("Moff Jerjerrod"),
    n("Imperial Arrest Order & Secret Plans"),
    n("We're In Attack Position Now", qty=3),
    n("Conquest", True),
    n("Imperial Command", qty=2),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Oh, Switch Off!"),
    n("General Veers", True),
    n("Control & Set For Stun", qty=4),
    n("Grand Moff Tarkin", True),
    n("Do They Have A Code Clearance?"),
    n("Accuser", True),
    n("Devastator", True),
    n("A Dark Time For The Rebellion", True),
    n("Blizzard 1", True),
    n("Admiral Pellaeon"),
    n("No Escape"),
    n("Death Star II: Coolant Shaft"),
    n("Admiral Piett"),
    n("Endor Shield", True),
    n("Chimaera"),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Maarek Stele, The Emperor's Reach"),
    n("Death Star II: Docking Bay"),
    n("We Shall Double Our Efforts!"),
    n("Cold Feet", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Forced Landing"),
    n("Admiral Motti", True),
    n("Tyrant"),
    n("General Nevar"),
    n("Darth Vader", True),
    n("Naboo"),
    n("Superlaser Mark II"),
    n("Force Push", True),
    n("Death Star II: Reactor Core"),
    n("Something Special Planned For Them", True),
    n("Admiral Ozzel"),
    n("Grand Admiral Thrawn"),
    n("Juno Eclipse, Black Leader"),
    n("Operational As Planned", True),
    n("Tatooine"),
    n("Death Star II: Capacitors"),
    n("Imperial Barrier"),
    n("Victory"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Leave Them To Me", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Imperial Detention"),
    n("Fanfare", True),
    n("Abyss"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Battle Order"),
]
DS_ADD = []
