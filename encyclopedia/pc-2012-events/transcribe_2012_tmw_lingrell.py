#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Scott Lingrell.

Source: 2012TMWDay1.pdf pages 5–6 (handwritten 2009 Print Form, 12 shields,
left 1-36 / right 37-60). Name Advocate dested Scott Lingrell analog leftover
player-stubs/Scott_Lingrell.wiki GEMP handle advocate. Username blank.
p05 Dark Deck Name Dark. p06 Light Deck Name Light. LIGHT/DARK empty;
dest from filled 60s + Deck Name. Event Date/Name blank.
Do not dest as a new person Advocate. Do not dest as Chris Schoenthal.
Do not dest 2012 MPC Lingrell 60s again.
"""
from __future__ import annotations

PLAYER = "Scott Lingrell"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2012 Texas Mini Worlds Day 1 Scott Lingrell LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Scott Lingrell DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2009 Print Form (12 shields, left 1-36 / right 37-60). "
    "Name Advocate dested Scott Lingrell analog leftover player-stubs/Scott_Lingrell.wiki "
    "GEMP handle advocate. Username blank. Event Date blank Event Name blank. "
    "Do not dest as a new person Advocate. Do not dest as Chris Schoenthal. "
    "Do not dest 2012 MPC Lingrell 60s again."
)
LS_NOTE = (
    "Handwritten 2009 Print Form. Name Advocate dested Scott Lingrell. "
    "Username blank. LIGHT/DARK empty; dest Light from filled 60s + Deck Name Light skip. "
    "Hidden Base True dested Hidden Base True. "
    "Republic Star dested Republic Starfighter True analog leftover qty=3. "
    "Consular Ship dested Tantive IV analog leftover Lingrell True. "
    "I'll try spinning dested I'll Try Spinning analog leftover 2013 MPC Lingrell. "
    "Atrocity dested Imperial Atrocity analog leftover True. "
    "Unc. Fury dested Uncontrollable Fury analog leftover. "
    "Sit Room dested Rebel Cell - Situation Room analog leftover 2013 MPC Lingrell True. "
    "Hidden Landing Site dested Rebel Cell - Hidden Landing Site analog leftover True. "
    "Aquarius dested Aquaris analog leftover 2013 MPC Lingrell. "
    "Bacta dested Bacta Tank analog leftover Peterson. "
    "Hiding in the dested Hiding In The Garbage analog leftover True. "
    "Automatic Pilot dested It's On Automatic Pilot! analog leftover 2013. "
    "Get to your ship dested Get To Your Ships analog leftover 2013 Lingrell. "
    "Uncharted dested Uncharted Settlements analog leftover True. "
    "Are You Brain Dead dested Are You Brain Dead?! analog leftover 2013. "
    "Not Your Fault dested It's Not My Fault! analog leftover 2012 MPC Lingrell True. "
    "Houjix Combo dested Houjix & Out Of Nowhere analog leftover Lingrell. "
    "Heading to The dested Heading For The Medical Frigate analog leftover. "
    "All Wings combo dested All Wings Report In & Darklighter Spin analog leftover qty=4. "
    "Wookiee Win dested Let The Wookiee Win analog leftover True qty=2. "
    "Its A Hit dested It's A Hit! analog leftover Atkin. "
    "Control Combo dested Control & Tunnel Vision analog leftover 2013. "
    "Senator Leia dested Senator Leia Organa analog leftover True. "
    "Dolphe dested Officer Dolphe analog leftover. "
    "Yoda MOTF dested Yoda, Master Of The Force analog leftover qty=2. "
    "Ric BL dested Ric Olie, Bravo Leader analog leftover. "
    "Clone Pilot True x2 then empty x1 sheet-accurate differing checkboxes. "
    "Panaka dested Panaka, Protector Of The Queen analog leftover. "
    "Jerus dested Jerus Jannick analog leftover. "
    "Padme dested Padme Naberrie analog leftover. "
    "Anger Fear dested Anger, Fear, Aggression True analog leftover IN THE 60. "
    "Shield YISYW dested Your Insight Serves You Well analog leftover True. "
    "Shield Professor dested The Professor analog leftover True. "
    "Shield DDTA dested Don't Do That Again analog leftover. "
    "Shield Simple Tricks dested Simple Tricks And Nonsense analog leftover True. "
    "Shield A Tragedy dested A Tragedy Has Occurred analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2009 Print Form. Name Advocate dested Scott Lingrell. "
    "Username blank. LIGHT/DARK empty; dest Dark from filled 60s + Deck Name Dark skip. "
    "AOBS empty dested Agents Of Black Sun. "
    "Dark Recon dested Dark Reconnaissance True analog leftover Lingrell. "
    "Mara, TEH dested Mara Jade, The Emperor's Hand analog leftover Lingrell qty=2. "
    "Gardulla dested Gardulla The Hutt analog leftover Lingrell. "
    "Aurra dested Aurra Sing analog leftover. "
    "Kitik dested Kitik Keed'kak analog leftover Lingrell True. "
    "Boonta dested Boonta Eve Podrace analog leftover Lingrell. "
    "Sebulba's racer dested Sebulba's Podracer analog leftover Lingrell. "
    "Pod Arena dested Tatooine: Podrace Arena analog leftover Lingrell. "
    "Imp City dested Coruscant: Imperial City analog leftover Lingrell. "
    "Wampa Cave dested Hoth: Wampa Cave (7th Marker) analog leftover Lingrell. "
    "Bridge dested Blockade Flagship: Bridge analog leftover Lingrell. "
    "War Room dested Death Star: War Room analog leftover Lingrell True. "
    "Trophy of a Kill dested analog leftover Lingrell True qty=4 unique overcount. "
    "Dengar in ship dested Dengar In Punishing One analog leftover Lingrell. "
    "Zuck in ship dested Zuckuss In Mist Hunter analog leftover Lingrell. "
    "Elis in ship dested Mist Hunter analog leftover Lingrell True. "
    "Elis dested Elis Helrot analog leftover. "
    "Wookie Kiss dested I'd Just As Soon Kiss A Wookiee analog leftover Lingrell qty=4 unique overcount. "
    "Dark Time dested A Dark Time For The Rebellion analog leftover Lingrell True qty=4. "
    "Accelerate our plans dested We Must Accelerate Our Plans analog leftover Lingrell qty=2. "
    "Imp Barrier dested Imperial Barrier analog leftover Lingrell qty=2. "
    "Weapon Lev dested Weapon Levitation analog leftover 2013 Lingrell. "
    "Start Your Engine dested Start Your Engines! analog leftover Grant/Lingrell. "
    "Comscan dested Comscan Detection analog leftover Skilton True. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover Cooleo True IN THE 60. "
    "Shield I Find Your Lack of Faith dested I Find Your Lack Of Faith Disturbing analog leftover True. "
    "Shield YCHF dested You Cannot Hide Forever analog leftover Lingrell True. "
    "Shield Code Clearance dested Do They Have A Code Clearance? analog leftover Lingrell. "
    "Shield Oppressive dested Oppressive Enforcement analog leftover. "
    "Shield TINT dested There Is No Try analog leftover. "
    "Shield Come Here You Big C dested Come Here You Big Coward analog leftover. "
    "Shield Allegations dested Allegations Of Corruption analog leftover. "
    "Shield Fantare dested Fanfare analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base"
LS_CARDS = [
    n("Hidden Base", True),
    n("Bravo 1"),
    n("Bravo 2"),
    n("Bravo 3"),
    n("Bravo 4"),
    n("Bravo 5"),
    n("Bravo Fighter"),
    n("Republic Starfighter", True, qty=3),
    n("Tantive IV", True),
    n("Flash Of Insight", True),
    n("Taking Them With Us", True),
    n("I'll Try Spinning"),
    n("Imperial Atrocity", True),
    n("Wokling", True),
    n("Uncontrollable Fury"),
    n("We'll Take The Long Way", True),
    n("Rebel Cell - Situation Room", True),
    n("Rebel Cell - Hidden Landing Site", True),
    n("Naboo"),
    n("Kiffex"),
    n("Aquaris"),
    n("Bacta Tank"),
    n("Hiding In The Garbage", True),
    n("It's On Automatic Pilot!"),
    n("Get To Your Ships"),
    n("We Didn't Hit It"),
    n("Uncharted Settlements", True),
    n("Are You Brain Dead?!"),
    n("It's Not My Fault!", True),
    n("Alter", True),
    n("Houjix & Out Of Nowhere"),
    n("Firefight", True, qty=2),
    n("Heading For The Medical Frigate"),
    n("All Wings Report In & Darklighter Spin", qty=4),
    n("Let The Wookiee Win", True, qty=2),
    n("It's A Hit!"),
    n("Sabotage", True),
    n("Control & Tunnel Vision"),
    n("Senator Leia Organa", True),
    n("Officer Dolphe"),
    n("Yoda, Master Of The Force", qty=2),
    n("Ric Olie, Bravo Leader"),
    n("Clone Pilot", True, qty=2),
    n("Clone Pilot"),
    n("Jedi Pilot", True, qty=3),
    n("Panaka, Protector Of The Queen"),
    n("Jerus Jannick"),
    n("Padme Naberrie"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun"
DS_CARDS = [
    n("Agents Of Black Sun"),
    n("Dark Reconnaissance", True),
    n("Presence Of The Force", qty=2),
    n("Jabba's Haven"),
    n("No Escape", True),
    n("Shada", True),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Prophetess", True),
    n("Probot", True),
    n("P-60"),
    n("P-59"),
    n("IG-88"),
    n("Gardulla The Hutt"),
    n("Aurra Sing"),
    n("Kitik Keed'kak", True),
    n("Boonta Eve Podrace"),
    n("Sebulba's Podracer"),
    n("Coruscant"),
    n("Tatooine: Podrace Arena"),
    n("Coruscant: Imperial City"),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room", True),
    n("Trophy Of A Kill", True, qty=4),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Mist Hunter", True),
    n("Elis Helrot"),
    n("Vader's Obsession", qty=2),
    n("I'd Just As Soon Kiss A Wookiee", qty=4),
    n("Stunning Leader", True, qty=3),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("We Must Accelerate Our Plans", qty=2),
    n("Control", qty=2),
    n("Projective Telepathy", qty=2),
    n("Imperial Barrier", qty=2),
    n("Weapon Levitation"),
    n("Surprise"),
    n("Start Your Engines!"),
    n("Comscan Detection", True),
    n("No Bargain", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
    n("Abyss", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("Secret Plans"),
]
DS_ADD = []
