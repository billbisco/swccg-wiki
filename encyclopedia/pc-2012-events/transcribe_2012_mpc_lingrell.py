#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Scott Lingrell.

Source: 2012mpcday1.pdf pages 3–4 (2010 form, 12 shields).
Name Scott Lingrell. Username blank.
p03 Light checked. Deck Name Justin Montgomery is my Muse.
p04 LIGHT/DARK both empty — dest Dark by pairing with p03 Light.
"""
from __future__ import annotations

PLAYER = "Scott Lingrell"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2012 Match Play Championship Day 1 Scott Lingrell LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Scott Lingrell DS.png"
LS_DECK_NAME = "Justin Montgomery is my Muse"
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Scott Lingrell. Username blank. LIGHT checked. "
    "Event MPC 2/11/12. Deck Name Justin Montgomery is my Muse. "
    "Kashyyyk (V) is the starting location (no Objective). "
    "Protector dested Protector. Kash Forest Depths dested Kashyyyk: Forest Depths. "
    "Creeeghrrgh dested Grrrghrrrgh!. Learn About The Force dested Learn About The Force, Luke. "
    "K: Sacred Forest dested Kashyyyk: Sacred Forest. K: Wookiee Haven dested Kashyyyk: Wookiee Haven. "
    "Let's Go Left dested Let's Go Left. Alderaan Consular dested Tantive IV. "
    "Luke's Blaster dested Luke's Blaster Pistol. Chewie of Kashyyyk dested Chewbacca Of Kashyyyk. "
    "It's Not My Fault dested It's Not My Fault!. Solo Han dested Han Solo. "
    "Nabrun dested Nabrun Leids. Jedi Lev dested Jedi Levitation. "
    "Nar Shadda Combo dested Nar Shaddaa Wind Chimes. "
    "K'lor'slug Combo dested Houjix & Out Of Nowhere. "
    "Bargaining Table dested Bargaining Table. Wookiee Courage dested as written. "
    "Unique overcounts sheet-accurate (Wookiee x8, Let's Go Left x3, Tantive IV x3, "
    "Wookiee Roar x3, Wookiee Guide x3, Imperial Atrocity x3, Yoda x2, Yoda, Great Warrior x2, "
    "Luke Skywalker, Rebel Hero x2, Chewbacca Of Kashyyyk x2, Corran Horn x2, "
    "Let The Wookiee Win x2, Might Of The Republic x2, Nar Shaddaa Wind Chimes x2). "
    "(V) from checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Scott Lingrell. Username blank. "
    "LIGHT/DARK both empty; dest Dark by pairing with p03 Light. Event MPC 2/11/12. "
    "Agents of Black Sun dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Imp City dested Coruscant: Imperial City. Podrace Arena dested Tatooine: Podrace Arena. "
    "Boonta Eve dested Boonta Eve Podrace. Sebulba's Racer dested Sebulba's Podracer. "
    "Wampa Cave dested Hoth: Wampa Cave (7th Marker). DS War Room dested Death Star: War Room. "
    "Flagship Bridge dested Blockade Flagship: Bridge. Mara TEH dested Mara Jade, The Emperor's Hand. "
    "Kitik dested Kitik Keed'kak. Gardulla dested Gardulla The Hutt. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. Elis in Hinthra dested Mist Hunter. "
    "Dengar in P1 dested Dengar In Punishing One. Dark Time dested A Dark Time For The Rebellion. "
    "I'd Just As Soon A Wook dested I'd Just As Soon Kiss A Wookiee. "
    "Coruscant Detention dested as written. Dark Recon dested Dark Reconnaissance. "
    "Jabba's Haven dested Jabba's Haven. Shield Imperial Detention crossed, "
    "You Cannot Hide Forever dested. You Never Won A Race crossed, "
    "Do They Have A Code Clearance? dested. "
    "Unique overcounts sheet-accurate (Trophy Of A Kill x4, A Dark Time For The Rebellion x5, "
    "I'd Just As Soon Kiss A Wookiee x4, Stunning Leader x3, P-59 x2, Mara Jade x2, "
    "Control x2, Projective Telepathy x2, Vader's Obsession x2, We Must Accelerate Our Plans x2, "
    "Imperial Barrier x2, Presence Of The Force x2). "
    "(V) from checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Kashyyyk"
LS_CARDS = [
    n("Kashyyyk", True),
    n("Protector", True),
    n("Kashyyyk: Forest Depths"),
    n("Grrrghrrrgh!"),
    n("Learn About The Force, Luke"),
    n("Rycar Ryjerd", True),
    n("Kashyyyk: Sacred Forest"),
    n("Kashyyyk: Wookiee Haven"),
    n("Let's Go Left", True, qty=3),
    n("Tantive IV", True, qty=3),
    n("Luke's Blaster Pistol", True),
    n("Wookiee", True, qty=8),
    n("Yoda", True, qty=2),
    n("Yoda, Great Warrior", True, qty=2),
    n("Luke Skywalker, Rebel Hero", True, qty=2),
    n("Senator Leia Organa", True),
    n("Chewbacca Of Kashyyyk", True, qty=2),
    n("Corran Horn", qty=2),
    n("It's Not My Fault!", True),
    n("Wookiee Courage"),
    n("Han Solo"),
    n("Nabrun Leids"),
    n("Jedi Levitation", True),
    n("Nar Shaddaa Wind Chimes", qty=2),
    n("Wookiee Roar", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Wookiee Guide", True, qty=3),
    n("Might Of The Republic", qty=2),
    n("Advantage"),
    n("Ellorrs Madak"),
    n("Houjix & Out Of Nowhere"),
    n("Our Most Desperate Hour", True),
    n("Imperial Atrocity", True, qty=3),
    n("Bargaining Table"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Chasm", True),
    n("Weapons Display"),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Knowledge And Defense", True),
    n("Coruscant"),
    n("Shada", True),
    n("No Bargain", True),
    n("Start Your Engines!"),
    n("Coruscant: Imperial City"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Sebulba's Podracer"),
    n("Presence Of The Force", qty=2),
    n("Trophy Of A Kill", True, qty=4),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Death Star: War Room", True),
    n("Blockade Flagship: Bridge"),
    n("Tonnika Sisters"),
    n("P-59", qty=2),
    n("IG-88", True),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Aurra Sing"),
    n("Kitik Keed'kak"),
    n("Prophetess", True),
    n("Gardulla The Hutt"),
    n("Zuckuss In Mist Hunter"),
    n("Mist Hunter", True),
    n("Dengar In Punishing One"),
    n("A Dark Time For The Rebellion", True, qty=5),
    n("Control", qty=2),
    n("Elis Helrot"),
    n("Surprise"),
    n("Projective Telepathy", qty=2),
    n("Vader's Obsession", qty=2),
    n("I'd Just As Soon Kiss A Wookiee", qty=4),
    n("Stunning Leader", True, qty=3),
    n("We Must Accelerate Our Plans", qty=2),
    n("Imperial Barrier", qty=2),
    n("Coruscant Detention"),
    n("Dark Reconnaissance", True),
    n("Jabba's Haven", True),
    n("No Escape"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Fanfare"),
]
DS_ADD = []
