#!/usr/bin/env python3
"""2014 US Nationals Day 1 typed/notebook lists: Vince Hutchins.

Source: Nationals-2014-day-1.pdf pages 25–27 (typed GEMP-style lists with
handwritten IN/OUT). Name as written Vince; identified Vince Hutchins.
p25 Dark. p26 Light start/shields. p27 Light 60.
"""
from __future__ import annotations

PLAYER = "Vince Hutchins"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 27
DS_PAGE = 25
LS_SCAN = "2014 US Nationals Day 1 p27 Vince Hutchins LS.png"
DS_SCAN = "2014 US Nationals Day 1 p25 Vince Hutchins DS.png"
NOTE = "Typed lists with handwritten IN/OUT. Name as written Vince; dest Vince Hutchins."
LS_NOTE = (
    "Typed GEMP list, heading Vince pg 2 (p26 start/shields) and Vince pg 3 (p27 60). "
    "Name as written Vince. Identified Vince Hutchins. "
    "QMC dested Quiet Mining Colony / Independent Operation. "
    "Jabba's Prize (1 starting) dested Jabba's Prize in the Light 60. "
    "Strike Force (V) / Arcon dested Strike Planning as written then Strike Force. "
    "Jar Jar Binks dested Senator Jar Jar Binks. "
    "All My Urchins & Cloud City Celebration dested All My Urchins & Cloud City Celebration. "
    "Unique overcounts sheet-accurate (Let The Wookiee Win x2, Path Of Least Resistance x2, "
    "Choke x2, Rebel Barrier x2, Imperial Atrocity x2). (V) from a trailing (V) on the printout."
)
DS_NOTE = (
    "Typed GEMP list, heading Vince pg 1. Handwritten Something Special Planned for them (V) "
    "and He Is Not Ready (V). Leave Them To Me (V) crossed, Firepower (V) IN. "
    "Masterful Move handwritten Endor Occupation dested Masterful Move & Endor Occupation. "
    "Handwritten IN: I'm Sorry (V), Combat Response (V), Cloud City: Security Tower (V), "
    "Combat Readiness (V), Bespin (V), Knowledge And Defense (V). "
    "Short Range Fighters + WYB dested Short Range Fighters & Watch Your Back!. "
    "U-3PO dested U-3PO (Yoo-Threepio). SFS L-s9.3 dested SFS L-s9.3 Laser Cannons. "
    "(1 starting) lines dested as shields. Unique overcounts sheet-accurate "
    "(Saber Squadron TIE x3, Saber Squadron Pilot x3, Sonic Bombardment x3, "
    "Nevar Yalnal x2, Ghhhk x2, Lightsaber Deficiency x2, Abyssin Ornament x2, "
    "Short Range Fighters & Watch Your Back! x2, Keder The Black x2, Baron Soontir Fel x2, "
    "Saber 1 x2). (V) from a trailing (V) on the printout."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("Jabba's Prize"),
    n("Nien Nunb, Sullustan Smuggler"),
    n("Foul Moudama"),
    n("Grimtaash"),
    n("Houjix"),
    n("Escape Pod"),
    n("Outrider"),
    n("It Could Be Worse"),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Tanus Spijek", True),
    n("Luke With Lightsaber"),
    n("It's A Trap!"),
    n("Errant Venture"),
    n("Blast The Door, Kid!"),
    n("Trooper Utris M'toc", True),
    n("Desperate Reach", True),
    n("Let The Wookiee Win", True, qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("It's A Hit!"),
    n("Dash Rendar", True),
    n("Mirax Terrik"),
    n("Sergeant Edian", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Alter"),
    n("Dark Approach", True),
    n("Booster In Pulsar Skate"),
    n("Melas", True),
    n("Path Of Least Resistance", qty=2),
    n("Choke", qty=2),
    n("Rebel Barrier", qty=2),
    n("Leia, Rebel Princess"),
    n("Chewbacca, Walking Carpet"),
    n("Senator Jar Jar Binks"),
    n("Leslomy Tacema", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Harc Seff", True),
    n("Overseer"),
    n("Kebyc", True),
    n("Aayla Secura"),
    n("Leesub Sirln", True),
    n("Ellorrs Madak", True),
    n("Menace Fades"),
    n("Imperial Atrocity", True, qty=2),
    n("Hiding In The Garbage", True),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("All My Urchins & Cloud City Celebration"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Anger, Fear, Aggression", True),
]
LS_ADD = []


DS_START = "Darth Vader, Dark Lord Of The Sith"
DS_CARDS = [
    n("Something Special Planned For Them", True),
    n("He Is Not Ready", True),
    n("Executor"),
    n("Operational As Planned", True),
    n("Nevar Yalnal", qty=2),
    n("Sienar Fleet Systems"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Tibanna Floating Refinery"),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Limited Resources"),
    n("Ghhhk", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Abyssin Ornament", True, qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("All Power To Weapons"),
    n("Protocol Failure"),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Arica"),
    n("Keder The Black", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Jango Fett, The Assassin"),
    n("Baron Soontir Fel", qty=2),
    n("OS-72-10"),
    n("Obsidian 10", True),
    n("Saber Squadron TIE", qty=3),
    n("Saber Squadron Pilot", qty=3),
    n("Saber 4"),
    n("Saber 1", qty=2),
    n("Wakeelmui"),
    n("Storm Clouds"),
    n("Bespin: Cloud City"),
    n("Mobilization Points"),
    n("I'm Sorry", True),
    n("Combat Response", True),
    n("Cloud City: Security Tower", True),
    n("Combat Readiness", True),
    n("Bespin", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
]
DS_ADD = []
