#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: SAN.

Source: MPC-2014-Day-1-Main-Event.pdf pages 122–123 (2013 form, 15 shields).
Deck Name SAN both sides. Name boxes joke titles. Username Pancakes on Light.
Dest SAN as 2013 MPC.
"""
from __future__ import annotations

PLAYER = "SAN"
USERNAME = "Pancakes"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 123
DS_PAGE = 122
LS_SCAN = "2014 Match Play Championship Day 1 SAN LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 SAN DS.png"
LS_DECK_NAME = "SAN"
DS_DECK_NAME = "SAN"
NOTE = "Handwritten 2013 Xerox form. Name as written SAN."
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2013 Xerox. Deck Name SAN. Name box Clark Gable's Intangible Elephant. "
    "Username Pancakes. LIGHT 60. TIGITH dested There Is Good In Him / I Can Save Him. "
    "LS, RS dested Luke Skywalker, Rebel Scout (V). W/YLEM dested Watch Your Step analog as written. "
    "Chewie RAWR dested Chewie, Enraged. Odin Neslor & First Aid dested Odin Nesloor & First Aid. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. Booster in PS dested "
    "Booster In Pulsar Skate. Unique overcounts sheet-accurate (Imperial Atrocity (V) x2, "
    "Wesa Gotta Grand Army x2, Chewie, Enraged x2, Master Qui-Gon (V) x2, Lando Calrissian, Scoundrel x2, "
    "Rebel Leadership (V) x2). NO_DEST IG-88. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Deck Name SAN. Name box Crocodile Rock. Username blank. DARK 60. "
    "CCT dested Carbon Chamber Testing / My Favorite Decoration. Prison Security Dues dested "
    "as written. Neural Inhibitor dested IG-88's Neural Inhibitor (V). Mandalorian FOF dested "
    "Jango Fett, The Assassin. Slave I SOF dested Slave I, Symbol Of Fear. SRF & WYB dested "
    "Short Range Fighters & Watch Your Back!. Control & SFS dested Control & Set For Stun. "
    "Dr. E & Baba Officially dested Dr. Evazan & Ponda Baba. Unique overcounts sheet-accurate "
    "(The Emperor (V) x3, Darth Vader (V) x2, Sense x2, Stunning Leader x3, Force Lightning x2, "
    "Defensive Fire (V) x2). NO_DEST Prison Security Dues (V); Jabba's Prize; Luke Skywalker (V); Battle Plan (shield). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Anger, Fear, Aggression", True),
    n("Weapon Levitation"),
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Don't Tread On Me", True),
    n("Sai'torr Kal Fas", True),
    n("I Feel The Conflict"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Home One: War Room"),
    n("Escape Pod", True),
    n("Chewie, Enraged", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Odin Nesloor & First Aid"),
    n("IG-88"),
    n("On The Edge"),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Naboo: Boss Nass' Chambers"),
    n("Blaster Deflection"),
    n("Draw Their Fire"),
    n("Obi-Wan's Lightsaber"),
    n("Houjix"),
    n("Smoke Screen"),
    n("Let The Wookiee Win", True),
    n("Seeking An Audience", True),
    n("Boonta Eve Podrace"),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Booster In Pulsar Skate"),
    n("Yavin 4: Massassi War Room", True),
    n("Rebel Leadership", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Speak With The Jedi Council"),
    n("Naboo: Battle Plains"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True),
    n("Tantive IV", True),
    n("Obi-Wan With Lightsaber"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sense"),
    n("Admiral Ackbar", True),
    n("Jedi Lightsaber", True),
    n("Quick Draw", True),
    n("Corran Horn"),
    n("Home One"),
    n("Coruscant: Jedi Council Chamber", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Jabba's Prize"),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("The Professor"),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("There Is Another"),
    n("Your Ship?"),
    n("Only Jedi Carry That Weapon"),
    n("Wise Advice"),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console"),
    n("Prison Security Dues", True),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Jabba's Prize"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Death Star: War Room"),
    n("The Emperor", True, qty=3),
    n("A Dark Time For The Rebellion", True),
    n("Mara Jade With Lightsaber"),
    n("Imperial Artillery", qty=2),
    n("Imperial Barrier"),
    n("Coruscant: Private Platform"),
    n("Victory", qty=2),
    n("Darth Maul With Lightsaber"),
    n("Kashyyyk"),
    n("Luke Skywalker", True),
    n("Protocol Failure"),
    n("Lateral Damage"),
    n("Boba Fett, Prepared Hunter"),
    n("Short Range Fighters & Watch Your Back!"),
    n("4-LOM With Concussion Rifle", True),
    n("Jabba's Palace: Dungeon"),
    n("I Have You Now"),
    n("Control & Set For Stun"),
    n("Stunning Leader", qty=3),
    n("Force Lightning", qty=2),
    n("Defensive Fire", True, qty=2),
    n("Sense", qty=2),
    n("Darth Vader", True, qty=2),
    n("Despair", True),
    n("Lightsaber Deficiency", True),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("Sniper & Dark Strike"),
    n("Cold Feet", True),
    n("Jango Fett, The Assassin"),
    n("Slave I, Symbol Of Fear"),
    n("Blockade Flagship: Bridge"),
    n("Jabba's Palace: Audience Chamber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Any Methods Necessary"),
    n("Juno Eclipse, Black Leader"),
    n("First Strike"),
    n("Darth Maul With Lightsaber"),
    n("IG-88", True),
]
DS_SHIELDS = [
    n("Leave Them To Me", True),
    n("After Her!", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Do They Have A Code Clearance", True),
    n("Battle Plan"),
]
DS_ADD = []
