#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Nick Reisch typed slang printout LS+DS."""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 75
DS_PAGE = 76
LS_SCAN = "2013 Match Play Championship p75 Nick Reisch LS.png"
DS_SCAN = "2013 Match Play Championship p76 Nick Reisch DS.png"
LS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). Deck title Wookies!. "
    "(v) tags on the printout are Holotable virtual versions. "
    "Protector dested Chewbacca, Protector. Grrghrrgh dested Grrrghrrrgh!. "
    "Kashyyyk Insurgent Leader dested Tarfful, Wookiee Insurgent. "
    "Third Either Way, You Win struck; handwritten Golden Horn. "
    "Yavin 4 Sentry dested Yavin Sentry. Wookiee Guide dested Wookiee Guide."
)
DS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). Deck title SYCFA. "
    "(v) tags on the printout are Holotable virtual versions. "
    "SYCFA dested Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "DS dested Death Star. DS:DB dested Death Star: Docking Bay 327. "
    "DS WR dested Death Star: War Room. CPI dested Commence Primary Ignition. "
    "Devestator dested Devastator. Where are those Droidika dested Where Are Those Droidekas?!. "
    "Master, Destroyers! as written. K&D dested Knowledge And Defense. "
    "Come Here You Big Coward shield crossed; omitted."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Let The Wookiee Win"
LS_CARDS = [
    n("Kashyyyk"),
    n("Chewbacca, Protector", True),
    n("Kashyyyk: Forest Depths"),
    n("Wokling", True),
    n("Declaration Of Rebellion"),
    n("Grrrghrrrgh!"),
    n("Home One: War Room"),
    n("Kashyyyk: Sacred Forest"),
    n("Kashyyyk: Wookiee Haven"),
    n("Commando Training & K'lor'slug"),
    n("Let's Go Left", True),
    n("Redeemed Apprentice"),
    n("Home One"),
    n("Launching The Assault"),
    n("Bargaining Table"),
    n("Advantage"),
    n("Wedge Antilles", True),
    n("Leia, Rebel Princess"),
    n("General Solo", True),
    n("Admiral Ackbar", True),
    n("Luke Skywalker", True),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Bail Organa, Father Of Rebellion"),
    n("Chewbacca Of Kashyyyk", True, qty=3),
    n("Yarua", True, qty=2),
    n("Tarfful, Wookiee Insurgent", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wookiee", True, qty=7),
    n("Either Way, You Win", True, qty=2),
    n("Golden Horn"),
    n("Let The Wookiee Win", True, qty=3),
    n("Control & Tunnel Vision", qty=2),
    n("It's A Trap!", qty=2),
    n("Might Of The Republic"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Corellian Retort", True, qty=2),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("It's Not My Fault!", True),
    n("Wookiee Guide", True, qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Alderaan"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Prepared Defenses"),
    n("Kuat Drive Yards", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Why Didn't You Tell Me?", True),
    n("Rendili"),
    n("Kiffex"),
    n("Judicator", qty=2),
    n("Tyrant"),
    n("Thunderflare"),
    n("Stalker"),
    n("Devastator"),
    n("Conquest"),
    n("Dominator", True),
    n("Victory"),
    n("Commence Primary Ignition", True),
    n("Superlaser"),
    n("Intensify The Forward Batteries", qty=2),
    n("Imperial Decree", True),
    n("Protocol Failure", qty=2),
    n("Tarkin Doctrine"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Overwhelmed", qty=2),
    n("Relentless Pursuit", qty=2),
    n("Operational As Planned", True, qty=2),
    n("Lateral Damage", qty=2),
    n("Stunning Leader", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Where Are Those Droidekas?!", True),
    n("Destroyer Droid", qty=8),
    n("P-60"),
    n("P-59"),
    n("Master, Destroyers!", qty=2),
    n("Self-Destruct Mechanism", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Battle Order"),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
