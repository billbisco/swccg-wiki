#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Wayne Cullen.

Source: 2012mpcday1.pdf pages 61–62 (2010 form, 12 shields).
Name Wayne Cullen dested Wayne Cullen. Username KissMyWookiee.
p61 Light Rescue The Princess. p62 Dark Combat Readiness.
Do not dest as a new person. Do not rewrite 2013 leftovers.
2013 leftover PLAYER="Wayne Cullen" USERNAME="KissMyWookiee"; pack player-stubs/Wayne_Cullen.wiki.
"""
from __future__ import annotations

PLAYER = "Wayne Cullen"
USERNAME = "KissMyWookiee"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 61
DS_PAGE = 62
LS_SCAN = "2012 Match Play Championship Day 1 Wayne Cullen LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Wayne Cullen DS.png"
LS_DECK_NAME = "Thank You Artoo! But Our Princess Is In Another Death Star!"
DS_DECK_NAME = "Pew, pew, Pew"
NOTE = "Typed 2010 Xerox form."
LS_NOTE = (
    "Typed 2010 Xerox. Name Wayne Cullen. Username KissMyWookiee. LIGHT checked. "
    "Deck Name Thank You Artoo! But Our Princess Is In Another Death Star!. "
    "Event MPC 2012 Date 02/11/12. Email [redacted]. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Rescue The Princess/Sometimes I Amaze Even Myself dested Rescue The Princess "
    "/ Sometimes I Amaze Even Myself empty. "
    "Luke With Lightsaber dested Luke With Lightsaber. "
    "Artoo & Threepio dested Artoo & Threepio True. "
    "Odin Nesloor & First Aid dested Odin Nesloor & First Aid x3. "
    "SATM dested Sorry About The Mess & Blaster Proficiency x2 (line 57 second copy; "
    "Amato analog has Wedge In Red Squadron 1). "
    "Antilles Maneuver & Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Desperate Reach True from L31_40 band. "
    "he Can go about his buisiness dested He Can Go About His Business True. "
    "Unique 60. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Wayne Cullen. Username Kissmywookiee dested KissMyWookiee. "
    "DARK checked. Deck Name Pew, pew, Pew. Event MPC 2012 Date 2/11/12. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Tatooine (ep1) dested Tatooine (Coruscant). "
    "Combat Readiness True dested Combat Readiness True (Effect starting). "
    "Dengar with gun dested Dengar With Blaster Carbine True x2. "
    "4-lom with gun empty dested 4-LOM With Concussion Rifle empty. "
    "Mara jade with saber dested Mara Jade With Lightsaber True. "
    "Probot dested Probot True. "
    "Scum & Villainy dested as written. "
    "we'll let fate decide dested We'll Let Fate-a Decide, Huh? True. "
    "i find your lack of pants disturbing dested I Find Your Lack Of Faith Disturbing True. "
    "You Cannot Hide Forever shield True from SH crop. "
    "reistance dested Resistance empty. "
    "Unique 60. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rescue The Princess / Sometimes I Amaze Even Myself"
LS_CARDS = [
    n("Rescue The Princess / Sometimes I Amaze Even Myself"),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Docking Bay"),
    n("Death Star: Docking Bay 327"),
    n("Death Star: Detention Block Corridor"),
    n("Senator Leia Organa"),
    n("Prisoner 2187"),
    n("Scomp Link Access", True),
    n("Cell 2187", True),
    n("Rycar Ryjerd", True),
    n("Artoo & Threepio", True),
    n("IL-19"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Captain Verrack", True),
    n("Luke With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Home One"),
    n("Tantive IV", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Home One: War Room"),
    n("Kiffex"),
    n("Thank The Maker"),
    n("A Jedi's Resilience", qty=3),
    n("Houjix"),
    n("Sense", qty=2),
    n("Escape Pod", True),
    n("Desperate Reach", True),
    n("Inconsequential Barriers"),
    n("Odin Nesloor & First Aid", qty=3),
    n("We're Doomed"),
    n("How Did We Get Into This Mess?", qty=2),
    n("Rebel Leadership", True),
    n("Houjix & Out Of Nowhere"),
    n("Grimtaash"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Hopping Mad", True),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("K'lor'slug", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Our Most Desperate Hour", True),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Combat Readiness"
DS_CARDS = [
    n("Tatooine (Coruscant)"),
    n("Combat Readiness", True),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Haven", True),
    n("Imperial Stockpile", True),
    n("Naboo Blaster Rifle"),
    n("Trophy Of A Bounty Hunter", True),
    n("Knowledge And Defense", True),
    n("Danz Borin", True),
    n("Jabba The Hutt", True),
    n("Jodo Kast", qty=2),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Dengar With Blaster Carbine", True, qty=2),
    n("Snoova"),
    n("Bossk", True),
    n("Gela Yeens", True),
    n("Garindan", True),
    n("Aurra Sing", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber", True),
    n("4-LOM With Concussion Rifle"),
    n("Probot", True),
    n("Guri"),
    n("Darth Maul"),
    n("Hutt Bounty", True),
    n("Desilijic Tattoo", True),
    n("Scum & Villainy"),
    n("Search And Destroy"),
    n("Tatooine Occupation"),
    n("First Strike"),
    n("Combat Response", True),
    n("Stunning Leader"),
    n("Imperial Barrier"),
    n("Wounded Warrior", qty=2),
    n("Blow Parried"),
    n("Hidden Weapons", qty=2),
    n("Jabba's Through With You"),
    n("Nothing Can Get Through Our Shield", True),
    n("Defensive Fire", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("None Shall Pass", True),
    n("Elis Helrot"),
    n("Weapon Levitation"),
    n("Jabba's Palace: Lower Passages"),
    n("Jabba's Palace: Audience Chamber"),
    n("Nal Hutta"),
    n("Hound's Tooth", True),
    n("Zuckuss In Mist Hunter"),
    n("Elis In Hinthra", True),
    n("Maul's Sith Infiltrator"),
    n("Punishing One", True),
    n("Stinger", True),
    n("Vibro-Ax"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Resistance"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("There Is No Try"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
