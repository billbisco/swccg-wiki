#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Jeremy Gardner.

Source: 2012TMWDay1.pdf pages 28–29 (typed slang printout, not a handwritten
Xerox form). Name Jeremy Gardner dested Jeremy Gardner analog leftover 2013
Worlds / player-stubs/Jeremy_Gardner.wiki. Username blank analog leftover
2013 Worlds. p28 Dark Imperial Entanglements. p29 Light Watch Your Step (V).
Do not dest as a new person. Do not dest 2013 Worlds Gardner 60s again.
"""
from __future__ import annotations

PLAYER = "Jeremy Gardner"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 29
DS_PAGE = 28
LS_SCAN = "2012 Texas Mini Worlds Day 1 Jeremy Gardner LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Jeremy Gardner DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout p28 Dark / p29 Light. "
    "Name Jeremy Gardner dested Jeremy Gardner analog leftover 2013 Worlds. "
    "Username blank analog leftover 2013 Worlds. Do not dest as a new person. "
    "Do not dest 2013 Worlds Gardner 60s again."
)
LS_NOTE = (
    "Typed slang printout p29 Light. Name Jeremy Gardner dested Jeremy Gardner analog leftover 2013 Worlds. "
    "Username blank. Do not dest as a new person. "
    "Watch Your Step/This Place Can Be A Little Rough True dested Watch Your Step analog leftover dual-title. "
    "BoShek, Brash Smuggler crossed dest replacement BoShek True analog leftover McCarthy. "
    "Ben Kenobi x2 crossed dest skip analog leftover. "
    "Commando Training True crossed dest skip analog leftover. "
    "Sense crossed dest replacement Corellian Retort True analog leftover. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi analog leftover. "
    "Blind Jedi dested analog leftover Veasey. "
    "Palejo Rashad dested analog leftover. "
    "Spaceport Scoundrels Guild dested Scoundrel's Guild analog leftover. "
    "Artoo uniqueness asterisk dest ignore. Qty from (xN). "
    "Unique 61 sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Typed slang printout p28 Dark. Name Jeremy Gardner dested Jeremy Gardner analog leftover 2013 Worlds. "
    "Username blank. Do not dest as a new person. "
    "Imperial Entanglements/No One To Stop Us This Time dested Imperial Entanglements analog leftover dual-title. "
    "The Emperor True crossed dest skip analog leftover. "
    "Tatooine: Lars' Moisture Farm crossed dest replacement Jundland Wastes analog leftover. "
    "Knowledge And Defense True (1 starting) dested analog leftover Anderson IN THE 60. "
    "Myn Keneugh dested analog leftover. "
    "We Have A Prisoner & I Can't Shake Him! dested analog leftover 2013 Worlds Gardner. "
    "Ghhhk & Those Rebels Won't Escape Us dested analog leftover. "
    "Control & Set For Stun dested analog leftover Tom H. "
    "Marquand In Blizzard 6 dested analog leftover. "
    "Asterisk uniqueness dest ignore. Qty from (xN). "
    "Unique 62 sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step", True),
    n("No Questions Asked", True, qty=3),
    n("Dash Rendar", True, qty=2),
    n("Mirax Terrik"),
    n("BoShek", True),
    n("Palejo Rashad"),
    n("Laudica", True),
    n("Yoda, Great Warrior", qty=2),
    n("Leia, Rebel Princess"),
    n("Corran Horn", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Chewie", True),
    n("Sergeant Bruckman"),
    n("Leia", True),
    n("Blind Jedi"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Captain Han Solo"),
    n("Romas 'Lock' Navander", True),
    n("Maris Brood, Fallen Jedi"),
    n("Hindsight", True),
    n("Insurrection & Aim High"),
    n("Bacta Tank"),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True, qty=2),
    n("Anger, Fear, Aggression", True),
    n("Desperate Reach", True),
    n("Corellian Retort", True),
    n("Antilles Maneuver", True),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=2),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport City"),
    n("Scoundrel's Guild"),
    n("Corellia", True),
    n("Tantive IV", True),
    n("Spiral"),
    n("Millennium Falcon", True),
    n("Booster In Pulsar Skate"),
    n("BoShek's Modified Light Freighter"),
    n("Obi-Wan In Radiant VII"),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Ultimatum"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("The Professor"),
    n("Chasm"),
    n("Weapons Display"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Imperial Entanglements"
DS_CARDS = [
    n("Imperial Entanglements"),
    n("We're In Attack Position Now"),
    n("Garindan", True),
    n("Mara Jade With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("AT-AT Driver", True, qty=3),
    n("General Veers", True),
    n("Commander Praji", True),
    n("Lieutenant Grond", True),
    n("Commander Igar", True),
    n("Grand Admiral Thrawn"),
    n("Corporal Derdram", True),
    n("Commander Daine Jir"),
    n("Admiral Ozzel"),
    n("Kir Kanos With Force Pike"),
    n("Myn Keneugh", True),
    n("Ni Chuba Na??", True),
    n("Fleet Security Protocols"),
    n("Imperial War Machine"),
    n("Tatooine Occupation", qty=2),
    n("Imperial Decree", True),
    n("Imperial Domination", True, qty=2),
    n("Protocol Failure"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Sandwhirl"),
    n("Knowledge And Defense", True),
    n("Occupied Territory"),
    n("Control & Set For Stun"),
    n("Heavy Fire Zone"),
    n("Imperial Barrier"),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True),
    n("A Dark Time For The Rebellion", True),
    n("Trample", qty=2),
    n("Outflank", True),
    n("We Have A Prisoner & I Can't Shake Him!", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Prepared Defenses", True),
    n("AT-AT Deployment Platform", qty=3),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: Jundland Wastes"),
    n("Star Destroyer: Command Station"),
    n("Tatooine: Desert Heart"),
    n("Tatooine"),
    n("Victory"),
    n("Devastator"),
    n("Blizzard 1", True),
    n("Cyclone Walker", qty=3),
    n("Marquand In Blizzard 6"),
    n("AT-AT Cannon", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("Battle Order"),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare"),
    n("A Useless Gesture"),
    n("Oppressive Enforcement"),
    n("Firepower"),
]
DS_ADD = []
