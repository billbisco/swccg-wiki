#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Jan B.

Source: 2012NationalsDay1.pdf pages 7–8 (handwritten 2010 Xerox, 12 shields).
Name Jan B. dested Jan B as written. Username rHylrisH.
p07 Light Yavin 4 starting / Restore Freedom To The Galaxy True in the 60.
p08 Dark Contract Killers.
Do not dest as Jan Berueda. Do not dest as Jan Westergard. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Jan B"
USERNAME = "rHylrisH"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2012 US Nationals Day 1 Jan B LS.png"
DS_SCAN = "2012 US Nationals Day 1 Jan B DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jan B. dested Jan B as written. Username rHylrisH. "
    "LIGHT checked. Deck Name blank. Event Nationals Date 6/9/12. "
    "Do not dest as Jan Berueda. Do not dest as Jan Westergard. Do not dest as a new person. "
    "Yavin 4 STARTING LOCATION dested Yavin 4. "
    "Yavin 4: Headquarters dested Yavin 4: Massassi Headquarters analog leftover Grant. "
    "AFA dested Anger, Fear, Aggression True analog leftover Grant. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Grant. "
    "Tantive 4 dested Tantive IV True analog leftover Anderson. "
    "Blue Squad B wing dested Blue Squadron B-wing analog leftover Carulli. "
    "Threepio w/ parts dested Threepio With His Parts Showing analog leftover Bollentino. "
    "Derek Klivian dested Derek \"Hobbie\" Klivian True analog leftover Grant. "
    "Fallen Jedi dested Fallen Jedi True leftover_xerox analog leftover Alperstein. "
    "Obi wan w/ saber dested Obi-Wan With Lightsaber analog leftover Grant. "
    "X-wing laser Cannon dested X-wing Laser Cannon analog leftover Grant. "
    "Star Destroyer dested Star Destroyer! analog leftover Brodsky. "
    "All wings Report In / combo dested All Wings Report In & Darklighter Spin analog leftover Grant. "
    "I've got a bad Feeling dested I've Got A Bad Feeling About This analog leftover. "
    "Antilles Maneuver / combo dested Antilles Maneuver & Rebel Reinforcements True analog leftover Grant. "
    "Eject Eject / combo dested Eject! Eject! Eject! & Imperial Atrocity True analog leftover Grant. "
    "Goo Nee Tay dested analog leftover. "
    "Projection of Skywalker dested Projection Of A Skywalker analog leftover Grant. "
    "Y4: Docking Bay dested Yavin 4: Docking Bay analog leftover Erwin. "
    "Y4: War Room dested Yavin 4: Massassi War Room analog leftover Grant. "
    "Y4: Briefing Room dested Yavin 4: Briefing Room analog leftover Grant. "
    "Restore Freedom dested Restore Freedom To The Galaxy True analog leftover Grant. "
    "Leia w/ Rifle dested Leia With Blaster Rifle analog leftover. "
    "Chewie w/ Rifle dested Chewie With Blaster Rifle analog leftover. "
    "Hanjix dested Odin Nesloor & First Aid analog leftover Booker. "
    "Shield Simple Tricks dested Simple Tricks And Nonsense analog leftover Grant. "
    "Shield Insight serves you well dested Your Insight Serves You Well analog leftover Grant. "
    "Shields 7–12 blank skip. Unique overcounts sheet-accurate "
    "(Artoo-Detoo In Red 5 x2, X-wing Laser Cannon x3, Steady Aim x2, "
    "Tunnel Vision x2, Projection Of A Skywalker x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Jan B. dested Jan B as written. Username rHylrisH. "
    "DARK checked. Deck Name blank. Event Nationals Date 6/9/12. "
    "Do not dest as Jan Berueda. Do not dest as Jan Westergard. Do not dest as a new person. "
    "Contract Killers / Feared Throughout The Galaxy True dested analog leftover Bollentino. "
    "gift of the mandalor dested Gift Of The Mentor True analog leftover Ziagos. "
    "Coruscant dested Coruscant (Dark) analog leftover Grant. "
    "Coruscant - Sub City Lair dested Coruscant: Sub City Lair analog leftover Izzo. "
    "Prepared Defenses True dested in the 60 analog leftover Anderson. "
    "D'vullle dested D'vullle True leftover_xerox. "
    "mara jade w/ saber dested Mara Jade With Lightsaber analog leftover 2014 Worlds. "
    "Bansha Raah dested Bane Malar True analog leftover Bollentino. "
    "he's not Ready + imp propaganda dested He Is Not Ready & Imperial Propaganda True analog leftover Bordier. "
    "Death mark + light blinky dested Death Mark & Hutt Bounty analog leftover. "
    "Slave One symbol of Fear dested Slave I, Symbol Of Fear True analog leftover Anderson. "
    "Boba Fett prepared hunter dested Boba Fett, Bounty Hunter True analog leftover Anderson. "
    "The mandalorian Father of Fett dested Jango Fett, The Assassin True analog leftover Anderson. "
    "This in nonsense dested This Is Just Wrong True analog leftover. "
    "Coruscant - Casino dested Coruscant: Casino True analog leftover. "
    "Coruscant Chancellors Office dested Coruscant: Chancellor's Office True analog leftover. "
    "Proton Rifle dested Proton Rifle True leftover_xerox. "
    "Aurra Sing Deadly assassin dested Aurra Sing True analog leftover Foth. "
    "Aurra's blaster rifle dested Aurra Sing's Blaster Rifle True analog leftover Aue. "
    "Bane Malar Spice Addict dested Bane Malar, Spice Addict analog leftover. "
    "Dr Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba True analog leftover Anderson. "
    "Ket Maliss shadow killer dested Ket Maliss True analog leftover Grant. "
    "Weapon of an Ungrateful son dested Weapon Of An Ungrateful Son analog leftover. "
    "Cloud City - Security Tower dested Cloud City: Security Tower True analog leftover Grant. "
    "wounded wookiee dested Wounded Wookiee leftover_xerox. "
    "Galen secret apprentice dested Galen, Secret Apprentice True analog leftover Anderson. "
    "Shield wont let Fate-a decide Huh dested We'll Let Fate-a Decide, Huh? analog leftover Pistone. "
    "Shield I Pity yo luck + Path disharmons dested I Pity Yo Luck & Path Of Disharmony True leftover_xerox. "
    "Shield Do they have a code clearance dested Do They Have A Code Clearance? True analog leftover Anderson. "
    "Unique overcounts sheet-accurate (Trophy Of A Kill True x2, Lateral Damage x2, "
    "Sonic Bombardment True x2, Projective Telepathy x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Yavin 4"),
    n("Yavin 4: Massassi Headquarters"),
    n("Anger, Fear, Aggression", True),
    n("Careful Planning", True),
    n("Squadron Assignments"),
    n("Superficial Damage", True),
    n("Luke, Trust Me", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Tantive IV", True),
    n("Red 6"),
    n("Outrider"),
    n("Blue Squadron B-wing"),
    n("Dash Rendar"),
    n("Jek Porkins", True),
    n("Threepio With His Parts Showing"),
    n("Derek \"Hobbie\" Klivian", True),
    n("Fallen Jedi", True),
    n("Corran Horn"),
    n("Obi-Wan With Lightsaber"),
    n("Luke Skywalker", True),
    n("SW-4 Ion Cannon"),
    n("X-wing Laser Cannon", qty=3),
    n("Diversionary Tactics"),
    n("Clash Of Sabers"),
    n("Steady Aim", qty=2),
    n("Star Destroyer!"),
    n("Tunnel Vision", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("A Few Maneuvers"),
    n("I've Got A Bad Feeling About This"),
    n("Organized Attack"),
    n("Smoke Screen"),
    n("Rebel Artillery"),
    n("Power Pivot"),
    n("Darklighter Spin"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Eject! Eject! Eject! & Imperial Atrocity", True),
    n("Goo Nee Tay"),
    n("Massassi Base Sentry", True),
    n("Uncontrollable Fury"),
    n("Menace Fades"),
    n("Projection Of A Skywalker", qty=2),
    n("Yavin 4: Docking Bay"),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Briefing Room"),
    n("Ralltiir"),
    n("Coruscant"),
    n("Restore Freedom To The Galaxy", True),
    n("It Could Be Worse"),
    n("Inconsequential Barriers"),
    n("Leia With Blaster Rifle"),
    n("Chewie With Blaster Rifle"),
    n("Odin Nesloor & First Aid"),
    n("Concentrate All Fire"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Battle Plan"),
    n("Your Insight Serves You Well"),
    n("Don't Do That Again"),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy", True),
    n("On The Hunt", True),
    n("Gift Of The Mentor", True),
    n("Guild Of Assassins", True),
    n("Jabba's Haven", True),
    n("Coruscant (Dark)"),
    n("Coruscant: Sub City Lair"),
    n("Prepared Defenses", True),
    n("Knowledge And Defense"),
    n("Trophy Of A Kill", True, qty=2),
    n("Set For Stun"),
    n("Weapon Levitation"),
    n("Abyssin Ornament", True),
    n("Lateral Damage", qty=2),
    n("Control"),
    n("Reegesk", True),
    n("Rodian", True),
    n("D'vullle", True),
    n("Mara Jade With Lightsaber"),
    n("Bane Malar", True),
    n("Search And Destroy"),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Death Mark & Hutt Bounty"),
    n("Nal Hutta"),
    n("Dengar In Punishing One"),
    n("Slave I, Symbol Of Fear", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("This Is Just Wrong", True),
    n("Coruscant: Casino", True),
    n("Coruscant: Chancellor's Office", True),
    n("Proton Rifle", True),
    n("IG-88 With Riot Gun"),
    n("Grotto Werribee"),
    n("Velken Tezeri", True),
    n("Aurra Sing", True),
    n("Aurra Sing's Blaster Rifle", True),
    n("Arica", True),
    n("Mara Jade's Lightsaber"),
    n("Vader's Lightsaber"),
    n("One Beautiful Thing", True),
    n("Bane Malar, Spice Addict"),
    n("Lightsaber Deficiency"),
    n("Special Delivery"),
    n("Zuckuss In Mist Hunter"),
    n("Projective Telepathy", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Dr. Evazan & Ponda Baba", True),
    n("Ket Maliss", True),
    n("Sniper"),
    n("Bossk With Mortar Gun"),
    n("Weapon Of An Ungrateful Son"),
    n("Cloud City: Security Tower", True),
    n("Wounded Wookiee"),
    n("Ghhhk"),
    n("Galen, Secret Apprentice", True),
]
DS_SHIELDS = [
    n("Battle Order", True),
    n("Abyss"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Pity Yo Luck & Path Of Disharmony", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward", True),
    n("Oppressive Enforcement", True),
    n("A Useless Gesture"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
