#!/usr/bin/env python3
"""2015 European Championship: Tobias Bukkehave Day 2 (place 10).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p22 Dark / p23 Light (typed free-form lists, player slang).
"""
from __future__ import annotations

PLAYER = "Tobias Bukkehave"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 23
DS_PAGE = 22
LS_SCAN = "2015 European Championship Tobias Bukkehave LS.png"
DS_SCAN = "2015 European Championship Tobias Bukkehave DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 10 circled. p22 Dark / p23 Light are typed free-form lists (no PC form), header handwritten 'Tobias Bukkehave (TB)'. "
    "No username. DS 3:1 / LS 2:2. Sheet deck labels 'TBRINGHIM' / 'We'll handle this TB' not used as DECK_NAME. "
    "Both lists are slang; every mapping logged below."
)
LS_NOTE = (
    "START We'll Handle This / Duel Of The Fates (sheet 'We'll handle this TB'). "
    "TITLE MISMATCH: wiki says Combat Preparedness, sheet starts We'll Handle This. "
    "Posted 2/3 site dested Naboo: Theed Palace Generator Core (2 DS/3 LS icons; objective deploys it). "
    "Posted 2/2 site dested Naboo: Theed Palace Generator (2/2 icons). "
    "REVIEWED: CONFIRM line 7 \"squassin\" dested Squadron Assignments (standard \"Squad Ass\" slang). "
    "Posted heading for the med frigate dested Heading For The Medical Frigate. Posted AFA v dested Anger, Fear, Aggression V. "
    "Posted ill take the leader dested I'll Take The Leader. Posted weapon lev dested Weapon Levitation. "
    "Posted were u looking for me dested Were You Looking For Me?. Posted wesa gota a great army dested Wesa Gotta Grand Army. "
    "Posted hear me baby dested Hear Me Baby, Hold Together. Posted wariors courage dested Warrior's Courage. "
    "Posted control combo dested Control & Tunnel Vision. Posted quigon jedi master dested Qui-Gon Jinn, Jedi Master (x3, unique overcount sheet-accurate). "
    "Posted all wings combo dested All Wings Report In & Darklighter Spin. Posted yoda motf dested Yoda, Master Of The Force (x2 sheet-accurate). "
    "Posted jedi lev dested Jedi Levitation. Posted ant man dested Antilles Maneuver. Posted blast the door kid dested Blast The Door, Kid!. "
    "Posted its a trap dested It's A Trap!. REVIEWED: CONFIRM \"qiu gons stick\" dested Qui-Gon's Lightsaber (RIII saber paired with QGJ Jedi Master in this WHT deck; Ptak's WHT lists it by name). Posted xwing cannon dested X-wing Laser Cannon. "
    "Posted nar shadaa dested Nar Shaddaa. Posted boss nass chamber dested Naboo: Boss Nass' Chambers. "
    "Posted leia rebel princess dested Leia, Rebel Princess. "
    "REVIEWED: CONFIRM \"corran\" dested Corran Horn (Corran Horn, Jedi is Virtual Set 23, post-2015). "
    "Posted wedge rsl dested Wedge Antilles, Red Squadron Leader. Posted lando scoundrel dested Lando Calrissian, Scoundrel. "
    "Posted threepio with his parts dested Threepio With His Parts Showing. "
    "REVIEWED: AS-WRITTEN \"anakin\" (character block, version not given; title Anakin Skywalker is the DSII Interrupt). "
    "Posted arto in r5 x4 dested Artoo-Detoo In Red 5 x4 (unique overcount sheet-accurate). Posted hcf dested Han, Chewie, And The Falcon x2. "
    "Posted green leader in ship dested Green Leader In Green Squadron 1. "
    "Shields: Do or do not dested Do, Or Do Not; This republic is b0rken dested The Republic No Longer Functions; Simple tricks dested Simple Tricks And Nonsense; "
    "Your insights serve u well dested Your Insight Serves You Well; Wise advise dested Wise Advice; Goldenrod kept as written. "
    "Main 63 as listed (sheet overcount; not 60). Shields 15."
)
DS_NOTE = (
    "START Bring Him Before Me / Take Your Father's Place (sheet 'BHBM'). "
    "Posted Throne room dested Death Star II: Throne Room. Posted K and D v dested Knowledge And Defense V. "
    "Posted A dark time for the rebellion dested A Dark Time For The Rebellion. Posted WMAOP dested We Must Accelerate Our Plans. "
    "Posted Turn it off v dested Turn It Off! Turn It Off! V. Posted I cant shake him v dested I Can't Shake Him! V. Posted Ghhk dested Ghhhk. "
    "Posted Emperors power dested Emperor's Power. Posted TPM dested The Phantom Menace. "
    "Posted Bossk in ship dested Bossk In Hound's Tooth. Posted Ellis in ship dested Elis In Hinthra. "
    "Posted Zimh dested Zuckuss In Mist Hunter (x2). Posted Boba in ship v dested Boba Fett In Slave I V. "
    "Posted Cc: security tower / downtown plaza dested Cloud City: Security Tower / Cloud City: Downtown Plaza. "
    "Posted Bf: bridge / hall way dested Blockade Flagship: Bridge / Blockade Flagship: Hallway. Posted Kashyyk dested Kashyyyk. "
    "Posted Woof v dested Wooof V. "
    "REVIEWED: AS-WRITTEN \"Ice heart\" (no matching DS card; Heart Of The Chasm / Ice Storm both guesses). "
    "Posted GMTv dested Grand Moff Tarkin V. Posted Epp mara x2 dested Mara Jade With Lightsaber x2. "
    "Posted Epp maul x3 dested Darth Maul With Lightsaber x3. Posted Epp vader x3 dested Darth Vader With Lightsaber x3. "
    "Posted Epp 4lom v dested 4-LOM With Concussion Rifle V. (unique overcounts sheet-accurate) "
    "Shields: Opressive enforcement dested Oppressive Enforcement; A useles gesture dested A Useless Gesture; Do they have code claer? dested Do They Have A Code Clearance?; "
    "You cannot hide dested You Cannot Hide Forever; Coward dested Come Here You Big Coward; There is not ry dested There Is No Try; "
    "Allegations of cor dested Allegations Of Corruption; I find your lack dested I Find Your Lack Of Faith Disturbing. "
    "Main 59 as listed (sheet count; not 60). Shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Inner Strength"),
    n("Wokling", True),
    n("A New Secret Base", True),
    n("Squadron Assignments"),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
    n("I'll Take The Leader"),
    n("Alter", True),
    n("Smoke Screen"),
    n("Weapon Levitation"),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sense", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Warrior's Courage"),
    n("Escape Pod"),
    n("Control & Tunnel Vision"),
    n("Moving To Attack Position"),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Rebel Barrier"),
    n("Jedi Levitation", True),
    n("It Could Be Worse"),
    n("Antilles Maneuver", True),
    n("Blast The Door, Kid!", qty=2),
    n("A Few Maneuvers"),
    n("It's A Trap!", qty=2),
    n("Houjix"),
    n("Qui-Gon's Lightsaber"),
    n("X-wing Laser Cannon"),
    n("Landing Claw"),
    n("Evacuation Control", True),
    n("Nar Shaddaa"),
    n("Naboo: Boss Nass' Chambers"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker", True),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lando Calrissian, Scoundrel"),
    n("Threepio With His Parts Showing"),
    n("Mace Windu", True, qty=2),
    n("anakin"),
    n("Artoo-Detoo In Red 5", qty=4),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Pulsar Skate"),
    n("Green Leader In Green Squadron 1"),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Affect Mind"),
    n("Battle Plan"),
    n("Weapons Display"),
    n("Goldenrod"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again"),
    n("Your Insight Serves You Well"),
    n("Wise Advice"),
    n("Yavin Sentry"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Your Destiny"),
    n("Insignificant Rebellion"),
    n("Death Star II: Throne Room"),
    n("Surface Defense", True),
    n("Knowledge And Defense", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", qty=2),
    n("Turn It Off! Turn It Off!", True),
    n("Force Push", True),
    n("Neimoidian Advisor"),
    n("Imperial Barrier"),
    n("I Can't Shake Him!", True),
    n("Masterful Move"),
    n("I Have You Now"),
    n("Sith Fury", True, qty=2),
    n("Dark Maneuvers"),
    n("Ghhhk"),
    n("Force Lightning"),
    n("Emperor's Power"),
    n("The Phantom Menace"),
    n("First Strike"),
    n("No Escape"),
    n("Blast Door Controls"),
    n("Blizzard 4", qty=2),
    n("Bossk In Hound's Tooth"),
    n("Elis In Hinthra"),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Boba Fett In Slave I", True),
    n("Cloud City: Security Tower"),
    n("Cloud City: Downtown Plaza"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Kashyyyk"),
    n("Emperor Palpatine"),
    n("Wooof", True),
    n("Sith Probe Droid", True, qty=2),
    n("Ice heart"),
    n("Grand Moff Tarkin", True),
    n("Darth Sidious"),
    n("Mara Jade With Lightsaber", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader With Lightsaber", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("Count Dooku"),
]
DS_SHIELDS = [
    n("Imperial Detention", True),
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Resistance"),
    n("Vote Of No Confidence"),
    n("Firepower"),
    n("Secret Plans"),
    n("Death Star Sentry"),
    n("I Find Your Lack Of Faith Disturbing"),
]
DS_ADD = []
