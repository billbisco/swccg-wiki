#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: John Veasey.

Source: 2012NationalsDay1.pdf pages 78–81 (typed GEMP dump, not a 2010 Xerox form).
p78–p79 Light Rogues 1/2. p80–p81 Dark Rops 1/2. Handwritten Veez dested John Veasey
analog leftover 2013 Worlds VeeZ / generate_2012_nats CANON / pages/John_Veasey.wiki.
Username veez analog leftover 2013 MPC. Pack pages/John_Veasey.wiki (is_bio).
Do not dest as a new person. Do not dest as Veez as a new person.
"""
from __future__ import annotations

PLAYER = "John Veasey"
USERNAME = "veez"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 78
DS_PAGE = 80
LS_SCAN = "2012 US Nationals Day 1 John Veasey LS.png"
DS_SCAN = "2012 US Nationals Day 1 John Veasey DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed GEMP dump p78–p81. Handwritten Veez dested John Veasey analog leftover "
    "2013 Worlds VeeZ / generate CANON. Username veez analog leftover 2013 MPC. "
    "Do not dest as a new person."
)
LS_NOTE = (
    "Typed GEMP dump p78–p79 Rogues 1/2. Handwritten Veez dested John Veasey analog leftover 2013 Worlds. "
    "Username veez analog leftover 2013 MPC. Do not dest as a new person. Do not dest as Veez as a new person. "
    "(1 starting) dested LS_SHIELDS 12 analog leftover Vince Hutchins / Casey Anis. "
    "Center Of Tyranny / A Liberated World dested analog leftover McCune IN THE 60 AND START. "
    "Blast The Door, Kid! printed x3 dest replacement x2. "
    "Too Close For Comfort handwritten dested analog leftover McCune extra written line unique 60. "
    "Corellian Retort (V) handwritten margin dest-note skip (60 already unique). "
    "Leia (V) dested Princess Leia (V) analog leftover McCune Leia dest Princess Leia. "
    "Obi-Wan in Radiant VII dested Obi-Wan In Radiant VII analog leftover McCune. "
    "Odin Nesloor & First Aid dested analog leftover McCune. "
    "Han, Chewie, And The Falcon dested analog leftover McCune. "
    "Commando Training & K'lor'slug dested analog leftover McCune. "
    "Derek 'Hobbie' Klivian (V) dested dest-as-written. "
    "Wes Janson, Rogue Veteran dested dest-as-written. "
    "Veteran Rogue dested analog leftover McCune x3 unique overcount. "
    "Yub Yub, Commander dested analog leftover McCune x3. "
    "Anger, Fear, Aggression (V) dested analog leftover McCune IN THE 60. "
    "Hindsight (V) dested analog leftover SAN. "
    "It's Not My Fault! (V) dested analog leftover SAN. "
    "Civil Disorder (V) dested analog leftover Haglund. Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump p80–p81 Rops 1/2. Handwritten Veez dested John Veasey analog leftover 2013 Worlds. "
    "Username veez analog leftover 2013 MPC. Do not dest as a new person. "
    "(1 starting) dested DS_SHIELDS 12 analog leftover Vince Hutchins. "
    "Ralltiir Operations / In The Hands Of The Empire dested analog leftover Shannon IN THE 60 AND START. "
    "Masterful Move & Endor Occupation printed x2 dest replacement x1 analog leftover Shannon. "
    "Handwritten Masterful Move dested extra written line unique 60. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin analog leftover Shannon. "
    "Ice-Heart dested Ysanne Isard analog leftover Echeverria. "
    "Short Range Fighters & Watch Your Back! dested analog leftover. "
    "Imbalance & Kintan Strider dested analog leftover 2014 Worlds. "
    "Alter (Coruscant) (V) dested Alter (V) analog leftover GEMP icon. "
    "Ni Chuba Na?? (V) dested analog leftover Anderson. "
    "Prepared Defenses (V) dested analog leftover McCune IN THE 60. "
    "Knowledge And Defense (V) dested analog leftover McCune IN THE 60. "
    "<>Spaceport Street dested Spaceport Street analog leftover Shannon. "
    "Emperor's Personal Shuttle dested dest-as-written. "
    "The Phantom Menace (AI) dested dest-as-written. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberated World"
LS_CARDS = [
    n("Blast The Door, Kid!", qty=2),
    n("Civil Disorder", True),
    n("It's Not My Fault!", True),
    n("Return Of The Jedi"),
    n("Odin Nesloor & First Aid", qty=2),
    n("Escape Pod", True),
    n("Projection Of A Skywalker"),
    n("Houjix"),
    n("We Wish To Board At Once"),
    n("Dash Rendar", True),
    n("Hindsight", True),
    n("Obi-Wan In Radiant VII"),
    n("Coruscant Celebration", qty=2),
    n("Honor Of The Jedi"),
    n("Corran Horn"),
    n("Menace Fades"),
    n("Han, Chewie, And The Falcon"),
    n("Bright Hope", True),
    n("Spiral"),
    n("Tantive IV", True),
    n("Luke's Blaster Pistol", True),
    n("Field Dressing"),
    n("Princess Leia", True),
    n("Yub Yub, Commander", qty=3),
    n("Veteran Rogue", qty=3),
    n("Keir Santage"),
    n("Wes Janson, Rogue Veteran"),
    n("Tycho Celchu", True),
    n("Ten Numb", True),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Derek 'Hobbie' Klivian", True),
    n("Dack Ralter", True),
    n("Commander Narra"),
    n("Biggs, Rogue Legend"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Commando Training & K'lor'slug"),
    n("Coruscant: Jedi Council Chamber"),
    n("Dressel"),
    n("Rogue Squadron Tactics"),
    n("Declaration Of Rebellion"),
    n("Bacta Infirmary"),
    n("Heading For The Medical Frigate", True),
    n("Rogue Insertion"),
    n("Planetary Shield"),
    n("Coruscant: Main Power Plant"),
    n("Coruscant: Lower Levels"),
    n("Coruscant", True),
    n("Center Of Tyranny / A Liberated World"),
    n("Anger, Fear, Aggression", True),
    n("Too Close For Comfort"),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Short Range Fighters & Watch Your Back!"),
    n("Imperial Justice", True),
    n("Imperial Decree", True),
    n("Jabba's Haven"),
    n("Masterful Move & Endor Occupation"),
    n("Masterful Move"),
    n("Sith Fury", True),
    n("Outflank", True),
    n("Sniper & Dark Strike"),
    n("Imbalance & Kintan Strider"),
    n("Cold Feet", True),
    n("Imperial Barrier"),
    n("Close Call", True),
    n("Alter", True),
    n("Sense"),
    n("You Are Beaten"),
    n("Ghhhk"),
    n("I Have You Now"),
    n("Disarmed"),
    n("Search And Destroy"),
    n("First Strike"),
    n("Tarkin's Bounty", True),
    n("The Phantom Menace (AI)"),
    n("Blizzard 4", True),
    n("Blizzard 2", True),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Victory"),
    n("Emperor's Personal Shuttle"),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Kir Kanos With Force Pike"),
    n("Ysanne Isard"),
    n("Colonel Davod Jon"),
    n("Janus Greejatus"),
    n("Emperor Palpatine", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Darth Vader With Lightsaber", qty=2),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Ozzel"),
    n("General Veers", True),
    n("General Nevar"),
    n("Nal Hutta"),
    n("Spaceport Street"),
    n("Spaceport Prefect's Office"),
    n("Spaceport Docking Bay"),
    n("Ralltiir: Spaceport Financial District"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Prepared Defenses", True),
    n("Ralltiir"),
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
]
DS_ADD = []
