#!/usr/bin/env python3
"""2013 World Championship Day 2: Scott Lingrell Xerox Linsanity + Profit."""
from __future__ import annotations

PLAYER = "Scott Lingrell"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 59
DS_PAGE = 58
LS_SCAN = "2013 Worlds Day 2 p59 Scott Lingrell LS.png"
DS_SCAN = "2013 Worlds Day 2 p58 Scott Lingrell DS.png"
LS_PUBLIC_NOTE = (
    "Day 2 Light sheet has a blank name box. Listed here as Scott Lingrell "
    "from the adjacent Dark Linsanity sheet."
)
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name box empty. Username blank. "
    "You Can Either Profit. Rebel Artillery on line 41. LIGHT inferred. "
    "Dested as Scott Lingrell from p58 Scott Lingrell Dark Linsanity. "
    "Do not rewrite the 2013 MPC Scott Lingrell leftover. "
    "You Can Either Profit dested You Can Either Profit By This... / Or Be Destroyed. "
    "Heading For The dested Heading For The Medical Frigate. "
    "Han dested Captain Han Solo. Jabba's Palace dested Jabba's Palace. "
    "Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Lars Farm dested Tatooine: Lars' Moisture Farm. "
    "Council Chamber dested Coruscant: Jedi Council Chamber. "
    "I Hope Shes Alright dested I Hope She's All Right. "
    "Saitor dested Sai'torr Kal Fas. Imp Atrocity dested Imperial Atrocity. "
    "Obi Saber dested Obi-Wan's Lightsaber. A280 Gun dested A280 Sharpshooter Rifle. "
    "Luke's Gun dested Luke's Blaster Pistol. Chewie's Bow dested Chewbacca's Bowcaster. "
    "Utility Belt dested Tatooine Utility Belt. Chew Protector dested Chewbacca, Protector. "
    "EPP Leia dested Leia With Blaster Rifle. Cap Yutani w/ Blaster dested "
    "Captain Yutani With Blaster Cannon. Leia, RP dested Leia, Rebel Princess. "
    "Tantel dested Tantive IV. Naked Threepio dested Threepio With His Parts Showing. "
    "Ortimarks dested Orrimaarko. Nabrun dested Nabrun Leids. "
    "Armed & Dangerous Combo dested Armed And Dangerous & Krayt Dragon Howl. "
    "Slight Weapons dested Slight Weapons Malfunction. "
    "Here Me Baby dested Hear Me Baby, Hold Together. Skywalker dested Luke Skywalker. "
    "Jedi Lev dested Jedi Levitation. Houjix Combo dested Houjix & Out Of Nowhere. "
    "Were Doomed dested We're Doomed. Run Luke Run dested Run Luke, Run!. "
    "Speak w Jedi dested Speak With The Jedi Council. "
    "Out Of Commission or Trans Term dested Transmission Terminated. "
    "A Jedi Concern dested A Jedi's Concentration. Anger Fear dested Anger, Fear, Aggression. "
    "Additional Don't Do That Again / Aim High / Tragedy moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Scott Lingrell. Username blank. "
    "Event 2013 Worlds. Deck title Linsanity. DARK. "
    "Do not rewrite the 2013 MPC Scott Lingrell leftover. "
    "Agents of Black Sun dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Start Your Engines dested Start Your Engines!. "
    "Sebulba's Racer dested Sebulba's Podracer. Pod Arena dested Tatooine: Podrace Arena. "
    "Imperial City dested Coruscant: Imperial City. "
    "Jabba's Haven dested Jabba's Haven. Elis Helrot dested Elis Helrot. "
    "Weapon Lev dested Weapon Levitation. "
    "I'd Just As Soon Kiss A Wookiee dested I'd Just As Soon Kiss A Wookiee. "
    "Coruscan Detection dested ComScan Detection. "
    "We Must Accelerate Our Plans dested We Must Accelerate Our Plans. "
    "Hoth Wampa Cave dested Hoth: Wampa Cave (7th Marker). "
    "DS War Room dested Death Star: War Room. Bridge dested Blockade Flagship: Bridge. "
    "Mara Jade TEH dested Mara Jade, The Emperor's Hand. Probot dested Probot. "
    "IG-88 w/ Gun dested IG-88 With Riot Gun. Kitik dested Kitik Keed'kak. "
    "Gardula dested Gardulla The Hutt. Elis dested Mist Hunter. "
    "Dengar in PT dested Dengar In Punishing One. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "We'll Let Fate dested We'll Let Fate-a Decide, Huh?. "
    "I Find Your Lack dested I Find Your Lack Of Faith Disturbing. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "YCHF dested You Cannot Hide Forever. "
    "Additional Fanfare / Coward / Secret Plans moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Heading For The Medical Frigate"),
    n("Captain Han Solo", True),
    n("Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("I Hope She's All Right"),
    n("A Gift"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True, qty=2),
    n("Advantage", True),
    n("Obi-Wan's Lightsaber"),
    n("A280 Sharpshooter Rifle", True),
    n("Luke's Blaster Pistol"),
    n("Chewbacca's Bowcaster"),
    n("Luke's Lightsaber"),
    n("Tatooine Utility Belt", True),
    n("Chewbacca, Protector", qty=2),
    n("Leia With Blaster Rifle"),
    n("Master Luke", qty=4),
    n("Padme Naberrie", True),
    n("Captain Yutani With Blaster Cannon"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Tantive IV", True),
    n("Threepio With His Parts Showing"),
    n("Orrimaarko", True),
    n("Nabrun Leids"),
    n("It Could Be Worse"),
    n("Rebel Artillery", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Slight Weapons Malfunction", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Luke Skywalker"),
    n("Jedi Levitation", True),
    n("Houjix & Out Of Nowhere"),
    n("We're Doomed"),
    n("Run Luke, Run!"),
    n("Speak With The Jedi Council", qty=2),
    n("Precise Hit", True, qty=2),
    n("Let The Wookiee Win", True),
    n("Out Of Commission"),
    n("Transmission Terminated"),
    n("A Jedi's Concentration", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("He Can Go About His Business", True),
    n("Planetary Defenses", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Start Your Engines!"),
    n("Sebulba's Podracer"),
    n("No Bargain", True),
    n("Presence Of The Force"),
    n("Coruscant"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Coruscant: Imperial City"),
    n("Shada", True),
    n("No Escape"),
    n("Jabba's Haven"),
    n("Dark Reconnaissance", True),
    n("Presence Of The Force"),
    n("Surprise"),
    n("Elis Helrot"),
    n("Weapon Levitation"),
    n("Levitation Attack", True),
    n("Vader's Obsession", qty=2),
    n("Stunning Leader", True, qty=3),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("Control", qty=2),
    n("Imperial Barrier", qty=2),
    n("Projective Telepathy", qty=2),
    n("I'd Just As Soon Kiss A Wookiee", qty=4),
    n("ComScan Detection", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Death Star: War Room", True),
    n("Blockade Flagship: Bridge"),
    n("Aurra Sing"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Probot"),
    n("P-60"),
    n("P-59"),
    n("IG-88 With Riot Gun"),
    n("Kitik Keed'kak", True),
    n("Gardulla The Hutt"),
    n("Prophetess", True),
    n("Mist Hunter", True),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Trophy Of A Kill", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Leave Them To Me", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Fanfare"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
]
DS_ADD = []
