#!/usr/bin/env python3
"""2013 World Championship Day 2: Chris Westergard Infiltration + Agents."""
from __future__ import annotations

PLAYER = "Chris Westergard"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 113
DS_PAGE = 114
LS_SCAN = "2013 Worlds Day 2 p113 Chris Westergard LS.png"
DS_SCAN = "2013 Worlds Day 2 p114 Chris Westergard DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields). Name Chris Westergard. "
    "Username blank. Email blank. LIGHT box empty; dested from objective. "
    "Infiltration / Unlikely Allies dested Infiltration / Unlikely Allies. "
    "Ditto Charm dested Scoundrel's Charm. "
    "Ingenuity dested Scoundrel's Ingenuity. "
    "Heading for the Med. Frigate dested Heading For The Medical Frigate. "
    "Luke Trust Me dested Luke, Trust Me. "
    "Get To Your Ships dested Get To Your Ships!. "
    "Spaceport docking bay dested Spaceport Docking Bay. "
    "Spaceport Scoundrels Guild dested Spaceport Scoundrels Guild. "
    "Nar Shaddaa: Undercity Street dested Nar Shaddaa: Undercity Street. "
    "Artoo & Threepio dested Artoo & Threepio. "
    "Obi-Wan in Radiant VII dested Obi-Wan In Radiant VII. "
    "Imperial Nav. Charts dested Imperial Navigation Charts. "
    "I Can't Believe He Is Gone dested I Can't Believe He's Gone. "
    "All Wings / Darklighter dested All Wings Report In & Darklighter Spin. "
    "Artoo, I Have a Bad Feeling dested Artoo, I Have A Bad Feeling About This. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Stay Sharp dested Stay Sharp!. "
    "Han's Tool kit dested Han's Toolkit. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Form left column reprints 37-38 on lines 39-40 are Desperate Reach "
    "and Houjix & Out Of Nowhere. "
    "Additional Ultimatum / Battle Plan / A Tragedy Has Occurred moved to Light shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields). Name Chris Westergard. "
    "Username blank. Email blank. DARK box empty; dested from objective. "
    "Agents of the Black Sun / Vengeance dested "
    "Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Start Your Engines dested Start Your Engines!. "
    "Death Star War Room dested Death Star: War Room. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "Hoth Wampa Cave dested Hoth: Wampa Cave (7th Marker). "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter. "
    "Dengar in Punishing One dested Dengar In Punishing One. "
    "Elis in Hinthra dested Elis In Hinthra. "
    "P.59 dested P-59. "
    "Gragra dested Gragra. "
    "IG-88 w/ Riot Gun dested IG-88 With Riot Gun. "
    "Mara Jade the Emp. Hand dested Mara Jade, The Emperor's Hand. "
    "Gardulla the Hutt dested Gardulla The Hutt. "
    "Com Scan Detection dested ComScan Detection. "
    "I'd Just as Soon Kiss a Wookiee dested I'd Just As Soon Kiss A Wookiee. "
    "Oh Switch Off dested Oh, Switch Off. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Form left column reprints 37-38 on lines 39-40 are Control. "
    "Lines 35-37 dittos of A Dark Time For The Rebellion. "
    "Surprise unique overcount (lines 51 and 55) kept sheet-accurate. "
    "Shada unique overcount (lines 5 and 25) kept sheet-accurate. "
    "Shields and Additional empty. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies", True),
    n("Nar Shaddaa", True),
    n("Nar Shaddaa: Undercity"),
    n("Scoundrel's Luck", True),
    n("Scoundrel's Bravado", True),
    n("Scoundrel's Charm", True),
    n("Scoundrel's Ingenuity", True),
    n("Heading For The Medical Frigate"),
    n("Luke, Trust Me"),
    n("Wokling", True),
    n("Get To Your Ships!"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild", True),
    n("Nar Shaddaa: Undercity Street"),
    n("Kyle Katarn", True, qty=2),
    n("Corran Horn", qty=2),
    n("Artoo & Threepio", qty=2),
    n("Captain Han Solo"),
    n("Boushh"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Dash Rendar"),
    n("Chewbacca, Walking Carpet"),
    n("Millennium Falcon", qty=2),
    n("Outrider"),
    n("Obi-Wan In Radiant VII", True),
    n("Legendary Starfighter"),
    n("Imperial Navigation Charts", True),
    n("I Can't Believe He's Gone", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Artoo, I Have A Bad Feeling About This", qty=2),
    n("A Few Maneuvers"),
    n("Dodge"),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere"),
    n("I've Got A Bad Feeling About This", qty=2),
    n("Power Pivot", qty=2),
    n("Stay Sharp!", qty=2),
    n("Moving To Attack Position", qty=3),
    n("We Wish To Board At Once", qty=2),
    n("Were You Looking For Me?"),
    n("Rapid Fire"),
    n("Intruder Missile", qty=2),
    n("Dual Laser Cannon"),
    n("Concussion Missile"),
    n("Han's Toolkit"),
    n("Concentrate All Fire"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again"),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well"),
    n("Yavin Sentry"),
    n("Wise Advice"),
    n("Ounee Ta"),
    n("Another Pathetic Lifeform"),
    n("Let's Keep A Little Optimism Here"),
    n("The Professor"),
    n("Aim High"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("No Bargain", True),
    n("Shada", True, qty=2),
    n("Start Your Engines!"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Sebulba's Podracer"),
    n("Presence Of The Force"),
    n("Death Star: War Room"),
    n("Blockade Flagship: Bridge"),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Zuckuss In Mist Hunter"),
    n("Dengar In Punishing One"),
    n("Elis In Hinthra", True),
    n("Trophy Of A Kill", qty=3),
    n("Aurra Sing"),
    n("Prophetess", True),
    n("P-59"),
    n("Gragra"),
    n("IG-88 With Riot Gun"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Gardulla The Hutt"),
    n("Guri"),
    n("Battle Droid Squad", True),
    n("Dark Reconnaissance", True),
    n("No Escape"),
    n("Jabba's Haven", True),
    n("A Dark Time For The Rebellion", qty=4),
    n("ComScan Detection"),
    n("Control", qty=2),
    n("Elis Helrot"),
    n("I'd Just As Soon Kiss A Wookiee", qty=4),
    n("Imperial Barrier", qty=2),
    n("Levitation Attack"),
    n("Stunning Leader", qty=2),
    n("Surprise", qty=2),
    n("Projective Telepathy", qty=2),
    n("Oh, Switch Off"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Vader's Obsession", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = []
DS_ADD = []
