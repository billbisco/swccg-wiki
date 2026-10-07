#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Kevin Shannon Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 31
DS_PAGE = 32
LS_SCAN = "2013 SoCal Grand Prix Day 1 p31 Kevin Shannon LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p32 Kevin Shannon DS.png"
LS_NOTE = (
    "Handwritten Print Form. Plead My Case / Sanctuary Comp → Plead My Case To The Senate / "
    "Sanity And Compassion. H.F.T.M.F. → Heading For The Medical Frigate. BP/DTF → "
    "Battle Plan & Draw Their Fire. Coruscant: JCC → Coruscant: Jedi Council Chamber. "
    "U-19 → R2-D2 (Artoo-Detoo). Commander Naees → Commander Narra. "
    "Wedge Antilles, RSL → Wedge Antilles, Red Squadron Leader. "
    "Bail Organa, F.O.R. → Bail Organa, Father Of Rebellion. "
    "Temple Hovercam → Senate Hovercam. Yoda Stew / YDHYM → Yoda Stew & You Do Have Your Moments. "
    "Houjix / Out of Nowhere → Houjix & Out Of Nowhere. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. Imperial Ent / NOTSUTT → Imperial Entanglements / "
    "No One To Stop Us This Time. Prep defenses → Prepared Defenses. "
    "Tat: Imperial Hangar Camp → Tatooine: Imperial Vanguard Camp. "
    "A.D.T.F.T.R. → A Dark Time For The Rebellion. Ghhhk / T.R.W.E.U. → "
    "Ghhhk & Those Rebels Won't Escape Us. Fel Sector Commander → ISB Sector Commander. "
    "WLFADH → We'll Let Fate-a Decide, Huh?. CHYBC → Come Here You Big Coward. "
    "YCHF → You Cannot Hide Forever. DTHACC → Do They Have A Code Clearance?. "
    "T.I.N.T. → There Is No Try. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Heading For The Medical Frigate"),
    n("Battle Plan & Draw Their Fire"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("R2-D2 (Artoo-Detoo)", True),
    n("Yoda, Great Warrior", qty=2),
    n("Owen Lars & Beru Lars"),
    n("Senator Jar Jar Binks"),
    n("Corran Horn"),
    n("Commander Narra"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Chewbacca, Protector", True),
    n("General Solo", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Senator Leia Organa"),
    n("Senator Padme Amidala"),
    n("Bail Organa", qty=2),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Senator Mon Mothma"),
    n("Alderaan Consular Ship"),
    n("Much To Learn, You Still Have"),
    n("Ambush", qty=2),
    n("Jedi Presence", qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sense", qty=3),
    n("Mechanical Failure", qty=2),
    n("Desperate Reach", True),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Might Of The Republic", qty=2),
    n("Field Dressing"),
    n("Clash Of Sabers"),
    n("Coruscant: Night Club"),
    n("Might Of The Republic"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Senate Hovercam"),
    n("So This Is How Liberty Dies"),
    n("Imperial Atrocity", True),
    n("Houjix & Out Of Nowhere"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
]
LS_SHIELDS = [
    n("Planetary Defenses", True),
    n("Chasm", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan", True),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Devastator"),
    n("Tatooine"),
    n("Imperial Stockpile"),
    n("The Emperor's Sword", True),
    n("Blaster Rifle", True),
    n("Prepared Defenses"),
    n("Tatooine: Imperial Vanguard Camp"),
    n("Imperial Academy Training", True),
    n("Don't Move!"),
    n("Full Scale Alert"),
    n("Intensify The Forward Batteries", qty=2),
    n("Wounded Warrior", qty=2),
    n("Trooper Assault", qty=2),
    n("Outflank", True, qty=2),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Imperial Commander", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Coordinated Attack", True, qty=2),
    n("Control"),
    n("Close Call", True),
    n("Blast Points"),
    n("Tatooine Occupation", qty=2),
    n("Strategic Reserves", True),
    n("Protocol Failure"),
    n("Imperial Detention", True, qty=2),
    n("Imperial Stormtrooper", qty=6),
    n("Elite Squadron Stormtrooper", True),
    n("Elite Squadron Stormtrooper", qty=3),
    n("Grand Moff Tarkin", True),
    n("ISB Sector Commander"),
    n("Admiral Piett"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Laser Cannon Battery"),
    n("Deflector Shield Generators", True),
    n("Tatooine: Cantina"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Watto's Junkyard", True),
]
DS_SHIELDS = [
    n("Imperial Detention"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Abyss", True),
]
DS_ADD = []
