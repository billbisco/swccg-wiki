#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Vikram Bali.

Source: Yavin42012.pdf pages 29–30.
p29 Dark typed 2010 Xerox / p30 Light typed 2010 Xerox.
Name Vikram Bali dested Vikram Bali analog leftover generate_2012_nats.py
CANON / player-stubs/Vikram_Bali.wiki / transcribe_2012_mpc_bali.py.
Username DVD ROTS dested USERNAME analog leftover 2013 Worlds / 2012 MPC.
Pack player-stubs/Vikram_Bali.wiki.
Do not dest as a new person. Do not dest 2012 MPC / 2013 Worlds /
2014 MPC Vikram Bali 60s again.
"""
from __future__ import annotations

PLAYER = "Vikram Bali"
USERNAME = "DVD ROTS"
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 30
DS_PAGE = 29
LS_SCAN = "2012 Yavin 4 Regionals Vikram Bali LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Vikram Bali DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p29 Dark typed 2010 Xerox / p30 Light typed 2010 Xerox. "
    "Name Vikram Bali dested Vikram Bali analog leftover generate_2012_nats.py "
    "CANON / player-stubs/Vikram_Bali.wiki. Username DVD ROTS dested USERNAME. "
    "Event Date 06/30/12 Event Name blank dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name You Got A Problem? / I Got A Problem Solver dested off article. "
    "Do not dest as a new person. Do not dest 2012 MPC / 2013 Worlds / "
    "2014 MPC Vikram Bali 60s again. Pack player-stubs/Vikram_Bali.wiki."
)
LS_NOTE = (
    "Typed 2010 Xerox p30 Light. Name Vikram Bali Username DVD ROTS. "
    "Event Date 06/30/12 Event Name blank dest Yavin 4 facing pair. LIGHT checked. "
    "Yavin IV: Massassi Throne Room dested Yavin 4: Massassi Throne Room analog leftover dest as written slang. "
    "START dested from line 1 site analog leftover Nathan no-objective. "
    "Qui-Gon Jinn w/ Lightsaber dested Qui-Gon Jinn With Lightsaber analog leftover dest as written slang qty=2. "
    "Obi-Wan w/ Lightsaber dested Obi-Wan With Lightsaber analog leftover dest as written slang qty=2. "
    "Luke w/ Lightsaber dested Luke Skywalker With Lightsaber analog leftover Orthner TYPE_OVERRIDE qty=2. "
    "Lando Calrissian, Scoundrel empty qty=2 analog leftover consecutive Westergard. "
    "Leia, Rebel Princess empty KEEP SEPARATE from Leia True analog leftover dest as written. "
    "Ki-Adi Mundi dested Ki-Adi-Mundi analog leftover dest as written slang. "
    "Han, Chewie, and the Falcon empty line 35 KEEP SEPARATE from True line 36 analog leftover McCune differing checkboxes. "
    "Revolution empty qty=5 analog leftover consecutive unique overcount sheet-accurate. "
    "Imperial Atrocity crossed dest Hindsight True analog leftover crossed-with-replacement. "
    "Let The Wookiee Win True qty=3 analog leftover consecutive. "
    "Rebel Leadership True qty=2 analog leftover consecutive. "
    "Wesa Gotta Grand Army empty qty=2 analog leftover consecutive. "
    "A Jedi's Resilience empty qty=3 analog leftover consecutive. "
    "Down With The Emperor dested analog leftover dest as written slang. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense analog leftover dest as written slang. "
    "Shields 1–12 filled. Unique 60 shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox p29 Dark. Name Vikram Bali Username DVD ROTS. "
    "Event Date 06/30/12 Event Name blank dest Yavin 4 facing pair. DARK checked. "
    "Hunt Down & Destroy the Jedi/Their Fire... dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True analog leftover dest as written dual-title. "
    "Knowledge & Defense dested Knowledge And Defense True analog leftover Anderson IN THE 60. "
    "<>Storm Clouds dested Cloud City: Storm Clouds analog leftover dest as written slang qty=2. "
    "<><><>Clouds dested Cloud City: Clouds analog leftover dest as written slang. "
    "Floating Refinery dested Cloud City: Floating Refinery analog leftover dest as written slang qty=2. "
    "Darth Vader w/ Lightsaber dested Darth Vader With Lightsaber analog leftover dest as written slang qty=3. "
    "Galen's Fighter dested Rogue Shadow analog leftover Walseth. "
    "Myn Kyneugh dested analog leftover dest as written TYPE_OVERRIDE myn kenaugh. "
    "Blizzard 4 True qty=2 analog leftover consecutive. "
    "Protocol Failure empty qty=2 analog leftover consecutive. "
    "Lightsaber Deficiency True qty=2 analog leftover consecutive. "
    "Dark Maneuvers & Tallon Roll empty qty=3 analog leftover consecutive dest as written combo. "
    "Short Range Fighters & Watch Your Back empty qty=2 analog leftover consecutive dest as written combo. "
    "All Power to Weapons dested All Power To Weapons analog leftover dest as written qty=3. "
    "Ghhhk & Those Rebels Won't Escape Us empty qty=2 analog leftover consecutive dest as written combo Haid. "
    "A Dark Time For The Rebellion True qty=2 analog leftover consecutive. "
    "Do They Have A Code Clearance dested as written as shield analog leftover dest as written slang. "
    "Shields 1–12 filled. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
    n("Podrace Prep"),
    n("Tatooine: Podrace Arena"),
    n("Anakin's Podracer"),
    n("Boonta Eve Podrace"),
    n("Goo Nee Tay"),
    n("Honor Of The Jedi"),
    n("I Did It!"),
    n("Yavin 4: Massassi War Room", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Malastare"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke Skywalker With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Leia", True),
    n("Padme Naberrie", True),
    n("Corran Horn"),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Ki-Adi-Mundi", True),
    n("Home One"),
    n("Tantive IV", True),
    n("Spiral"),
    n("Gold Leader In Gold 1", True),
    n("Wedge In Red Squadron 1"),
    n("Han, Chewie, And The Falcon"),
    n("Han, Chewie, And The Falcon", True),
    n("Revolution", qty=5),
    n("Hindsight", True),
    n("Civil Disorder", True),
    n("Draw Their Fire"),
    n("Strikeforce", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience", qty=3),
    n("Were You Looking For Me?"),
    n("Inconsequential Barriers"),
    n("Down With The Emperor", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("The Professor", True),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Knowledge And Defense", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses"),
    n("Combat Response"),
    n("Endor Shield", True),
    n("I'm Sorry", True),
    n("Endor"),
    n("Cloud City: Storm Clouds", qty=2),
    n("Cloud City: Clouds"),
    n("Cloud City: Floating Refinery", True, qty=2),
    n("Darth Vader With Lightsaber", qty=3),
    n("General Veers", True),
    n("Admiral Ozzel"),
    n("DS-61-2"),
    n("DS-61-3"),
    n("Black Leader"),
    n("Baron Soontir Fel"),
    n("OS-72-10"),
    n("Myn Kyneugh", True),
    n("Blizzard 4", True, qty=2),
    n("Black 2", True),
    n("Black 3", True),
    n("Rogue Shadow"),
    n("Saber 1"),
    n("Obsidian 10", True),
    n("OS-72-1 In Obsidian 1"),
    n("OS-72-2 In Obsidian 2"),
    n("Obsidian 7"),
    n("Obsidian 8"),
    n("Royal Escort", True),
    n("Presence Of The Force"),
    n("Lateral Damage"),
    n("Protocol Failure", qty=2),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Dark Maneuvers & Tallon Roll", qty=3),
    n("Force Push", True),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("All Power To Weapons", qty=3),
    n("Atmospheric Assault", True),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("One Beautiful Thing"),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Resistance"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
