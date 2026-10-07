#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Scott Lingrell Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Scott Lingrell"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 58
DS_PAGE = 57
LS_SCAN = "2013 Match Play Championship p58 Scott Lingrell LS.png"
DS_SCAN = "2013 Match Play Championship p57 Scott Lingrell DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Scott Lingrell. Light. Deck title Recycling Republicas Part 2. "
    "Hidden Base dested Hidden Base / Systems Will Slip Through Your Fingers. "
    "Aquarius dested Aquaris. Situation Room dested Rebel Cell - Situation Room. "
    "Landing Site dested Rebel Cell - Hidden Landing Site. "
    "Monitoring Station dested Rebel Cell - Monitoring Station. "
    "Taking Them With Me dested Taking Them With Us. Panaka P&Q dested Panaka, Protector Of The Queen. "
    "Dolphe dested Officer Dolphe. Ric Blender dested Ric Olie, Bravo Leader. "
    "Padme dested Padme Naberrie. Jerus dested Jerus Jannick. "
    "Brain Dead dested Are You Brain Dead?!. Control/TV dested Control & Tunnel Vision. "
    "Don't Need Their Scum dested I Don't Need Their Scum, Either. "
    "Houjix + OON dested Houjix & Out Of Nowhere. All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "Eject Eject Combo dested Eject! Eject!. Hiding In The Garbage dested Hiding In The Garbage. "
    "It's On Automatic Pilot dested It's On Automatic Pilot!. "
    "Bota Frik crossed; Redeemed Apprentice dested Redeemed Apprentice. "
    "Form 1-index gutter prints a leading 1 so line numbers look like 11–38. "
    "Form left column reprints 37–38 on lines 39–40; reprint 38 is blank. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Scott Lingrell. Dark. Deck title Linsanity. "
    "Agents of the Black Sun dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Podrace Arena dested Tatooine: Podrace Arena. Bridge dested Blockade Flagship: Bridge. "
    "Imperial City dested Coruscant: Imperial City. Sebulba's Racer dested Sebulba's Podracer. "
    "Start Your Engines dested Start Your Engines!. Dark Recon dested Dark Reconnaissance. "
    "Elis In Hinthra dested Mist Hunter. DS War Room dested Death Star: War Room. "
    "Wampa Cave dested Hoth: Wampa Cave (7th Marker). Mara Jade TEH dested Mara Jade, The Emperor's Hand. "
    "Poogletess dested Prophetess. Kitk dested Kitik Keed'kak. Gardulla dested Gardulla The Hutt. "
    "Form 1-index gutter prints a leading 1 so line numbers look like 11–38. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Anger, Fear, Aggression", True),
    n("Naboo"),
    n("Aquaris"),
    n("Kiffex"),
    n("Rebel Cell - Situation Room", True),
    n("Rebel Cell - Hidden Landing Site", True),
    n("Rebel Cell - Monitoring Station", True),
    n("I'll Try Spinning"),
    n("Taking Them With Us", True),
    n("Republic Starfighter", True, qty=2),
    n("Bravo 1"),
    n("Bravo 2"),
    n("Bravo 3"),
    n("Bravo Fighter"),
    n("Bravo 4"),
    n("Panaka, Protector Of The Queen"),
    n("Sio Bibble"),
    n("Senator Leia Organa", True),
    n("Officer Dolphe"),
    n("Ric Olie, Bravo Leader"),
    n("Padme Naberrie", True),
    n("Jerus Jannick"),
    n("Clone Pilot", True, qty=2),
    n("Jedi Pilot", True, qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Heading For The Medical Frigate"),
    n("Alter", True),
    n("Are You Brain Dead?!"),
    n("Control & Tunnel Vision"),
    n("I Don't Need Their Scum, Either", True),
    n("Ambush", True),
    n("Houjix & Out Of Nowhere"),
    n("It's Not My Fault"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Firefight", True, qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Menace Fades"),
    n("We Didn't Hit It"),
    n("Get To Your Ships"),
    n("Eject! Eject!", True, qty=2),
    n("Hiding In The Garbage", True),
    n("Uncharted Settlements", True),
    n("We'll Take The Long Way", True),
    n("Wokling", True),
    n("Redeemed Apprentice", True),
    n("It's On Automatic Pilot!"),
    n("Flash Of Insight", True, qty=2),
]
LS_SHIELDS = [
    n("Chasm"),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Knowledge And Defense", True),
    n("Tatooine: Podrace Arena"),
    n("Bestine"),
    n("Coruscant"),
    n("Blockade Flagship: Bridge"),
    n("No Bargain"),
    n("Presence Of The Force"),
    n("Coruscant: Imperial City"),
    n("Sebulba's Podracer"),
    n("Shada", True),
    n("Start Your Engines!"),
    n("Presence Of The Force"),
    n("No Escape"),
    n("Dark Reconnaissance", True),
    n("Jabba's Haven", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Control", qty=2),
    n("Stunning Leader", True, qty=3),
    n("Surprise"),
    n("Weapon Levitation"),
    n("Elis Helrot"),
    n("Conquest", True),
    n("Imperial Barrier", qty=2),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("Projective Telepathy", qty=2),
    n("I'd Just As Soon Kiss A Wookiee", qty=4),
    n("Levitation Attack", True),
    n("Vader's Obsession", qty=2),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Mist Hunter", True),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Death Star: War Room"),
    n("Trophy Of A Kill", True, qty=3),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("IG-88"),
    n("Prophetess", True, qty=2),
    n("Aurra Sing"),
    n("P-59"),
    n("P-60"),
    n("Kitik Keed'kak"),
    n("Gardulla The Hutt"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Fanfare"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
