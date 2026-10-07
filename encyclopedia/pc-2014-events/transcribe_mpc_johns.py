#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Print Form: Jeffrey Johns.

Source: MPC-2014-Day-1-Main-Event.pdf pages 59–60 (2013 Print Form).
Username jademasters.
"""
from __future__ import annotations

PLAYER = "Jeffrey Johns"
USERNAME = "jademasters"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 60
DS_PAGE = 59
LS_SCAN = "2014 Match Play Championship Day 1 Jeffrey Johns LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Jeffrey Johns DS.png"
NOTE = "Typed 2013 Print Form."
LS_NOTE = (
    "Typed 2013 Print Form. Username jademasters. We'll Handle This / Duel Of The "
    "Fates. Antillies Maneuver dested Antilles Maneuver & Rebel Reinforcements. "
    "Qui-Gon's Lightsaber (Reflections III) dested Qui-Gon's Lightsaber. (V) from "
    "checkbox. Unique overcounts sheet-accurate (Qui-Gon Jinn, Jedi Master x3, "
    "Mace Windu, Master Of The Order x2, Lando Calrissian, Scoundrel x2, Wesa Gotta "
    "Grand Army x2, Escape Pod (V) x2, Aayla Secura x2, Luke Skywalker, Strong In "
    "The Force (V) x3, Clinging To The Edge (V) x2, Luke's Bionic Hand (V) x3, "
    "Artoo-Detoo In Red 5 x3, The Bith Shuffle & Desperate Reach x2)."
)
DS_NOTE = (
    "Typed 2013 Print Form. Username jademasters. Set Your Course For Alderaan / "
    "The Ultimate Power In The Universe. Kaut Drive Yards dested Kuat Drive Yards. "
    "Devestator dested Devastator. Death star: Central Core dested Death Star: "
    "Central Core (Reactor Shaft). Visage dested Visage Of The Emperor. U-3PO "
    "[Yoo-Threepio] dested U-3PO (Yoo-Threepio). (V) from checkbox. Unique overcounts "
    "sheet-accurate (Darth Sidious x3, Judicator x2, Relentless Pursuit x2, "
    "Lightsaber Deficiency (V) x2, Intensify The Forward Batteries x3, Cease Fire! "
    "x2, Lateral Damage x2, Nevar Yalnal x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Anger, Fear, Aggression", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Inner Strength"),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Lando Calrissian, Scoundrel"),
    n("Naboo: Boss Nass' Chambers"),
    n("Guardian's Lightsaber"),
    n("Redeemed Apprentice"),
    n("Lightsaber Proficiency"),
    n("Luke's Bionic Hand", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Artoo-Detoo In Red 5"),
    n("I'm With You Too", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Qui-Gon Jinn, Jedi Master"),
    n("Escape Pod", True),
    n("Aayla Secura"),
    n("Corran Horn"),
    n("Wesa Gotta Grand Army"),
    n("Escape Pod", True),
    n("Mace Windu, Master Of The Order"),
    n("Sergeant Doallyn", True),
    n("Qui-Gon Jinn, Jedi Master"),
    n("Mace Windu, Master Of The Order"),
    n("Let The Wookiee Win", True),
    n("Aayla Secura"),
    n("Weapon Levitation"),
    n("Wesa Gotta Grand Army"),
    n("Qui-Gon Jinn, Jedi Master"),
    n("Away Put Your Weapon", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Jedi Levitation", True),
    n("Undercover", True),
    n("Lando Calrissian, Scoundrel"),
    n("Qui-Gon's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Imperial Atrocity", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Artoo-Detoo In Red 5"),
    n("Clinging To The Edge", True),
    n("Artoo-Detoo In Red 5"),
    n("Houjix"),
    n("Blaster Deflection"),
    n("Mercenary Armor", True),
    n("Han, Chewie, And The Falcon"),
    n("Luke Skywalker, Strong In The Force", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Obi-Wan's Journal"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Clinging To The Edge", True),
    n("Luke's Bionic Hand", True),
    n("Luke's Lightsaber"),
    n("Blaster Deflection"),
    n("Luke's Bionic Hand", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("The Professor", True),
    n("Wise Advice", True),
    n("A Close Race", True),
    n("Another Pathetic Lifeform"),
    n("Planetary Defenses", True),
    n("Do, Or Do Not"),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense", True),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Knowledge And Defense", True),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Protocol Failure"),
    n("Operational As Planned", True),
    n("TIE Sentry Ships", True),
    n("Rendili"),
    n("Judicator"),
    n("Thunderflare"),
    n("Conquest", True),
    n("He Is Not Ready", True),
    n("Darth Sidious"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Death Star: War Room", True),
    n("Dominator"),
    n("Cease Fire!"),
    n("Victory", True),
    n("Imperial Propaganda", True),
    n("Overwhelmed"),
    n("Presence Of The Force"),
    n("Intensify The Forward Batteries"),
    n("Lightsaber Deficiency", True),
    n("Darth Sidious"),
    n("Judicator"),
    n("Relentless Pursuit"),
    n("Devastator", True),
    n("Nal Hutta"),
    n("Lightsaber Deficiency", True),
    n("Nevar Yalnal"),
    n("Intensify The Forward Batteries"),
    n("Cease Fire!"),
    n("Arica"),
    n("Corulag"),
    n("U-3PO (Yoo-Threepio)"),
    n("They've Shut Down The Main Reactor"),
    n("Intensify The Forward Batteries"),
    n("Lateral Damage"),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Nevar Yalnal"),
    n("Where Are You Taking Them?"),
    n("Lateral Damage"),
    n("Darth Sidious"),
    n("Tarkin Doctrine"),
    n("Keder The Black"),
    n("Relentless Pursuit"),
    n("Dreaded Imperial Starfleet", True),
    n("Death Star: Central Core (Reactor Shaft)", True),
    n("Visage Of The Emperor"),
    n("Vengeance"),
    n("Imperial Barrier"),
    n("Force Push", True),
    n("Cease Fire!"),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Allegations Of Corruption", True),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever"),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("After Her!", True),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("Imperial Detention", True),
    n("Secret Plans", True),
    n("Battle Order"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
