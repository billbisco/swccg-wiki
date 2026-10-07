#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Joe Olson.

Source: MPC-2014-Day-1-Main-Event.pdf pages 82–83.
Light handwritten 2013 form; Dark typed CCT.txt with handwritten replacements.
Name Joe Okan dested Joe Olson. Username A Rebel Spy.
"""
from __future__ import annotations

PLAYER = "Joe Olson"
USERNAME = "A Rebel Spy"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 82
DS_PAGE = 83
LS_SCAN = "2014 Match Play Championship Day 1 Joe Olson LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Joe Olson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "CCT.txt"
NOTE = "Light handwritten 2013 Xerox; Dark typed Holotable list with replacements."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Joe Okan dested Joe Olson. Username A Rebel Spy. "
    "LIGHT checked. Coruscant: Night Club starting location. IITFYS (V) dested "
    "It Is The Future You See (V) / A Tremor In The Force (V). SATM/BP dested "
    "Sorry About The Mess & Blaster Proficiency. Control/Tunnel dested Control & Tunnel Vision. "
    "HCF dested Hear Me Baby, Hold Together. Yoda MOF dested Yoda, Master Of The Force. "
    "Speak With The Jedi Council qty=5 unique overcount sheet-accurate. "
    "Unique overcounts sheet-accurate (Sorry About The Mess & Blaster Proficiency x2, "
    "Escape Pod (V) x2, Blaster Deflection x2, Wesa Gotta Grand Army x2, Let The Wookiee Win (V) x2, "
    "Jedi Levitation (V) x2, Speak With The Jedi Council x5, Luke Skywalker, Strong In The Force x3, "
    "Leia, Rebel Princess x2, Mace Windu (V) x2, Yoda, Master Of The Force x3, Master Qui-Gon (V) x2, "
    "Artoo-Detoo In Red 5 x2, Jedi Lightsaber (V) x2, Hear Me Baby, Hold Together (V) x2). "
    "(V) from checkbox."
)
DS_NOTE = (
    "Typed CCT.txt with handwritten replacements. Name Joe Olson. Username A Rebel Spy. "
    "Carbon Chamber Testing / My Favorite Decoration starting. Imbalance & Kintan Strider "
    "replaced Count Dooku x2. Leave Them To Me replaced I Find Your Lack Of Faith Disturbing (V). "
    "Imperial Detention replaced We'll Let Fate-a Decide, Huh?. Elis Helrot replaced Close Call (V). "
    "Darth Vader, Dark Lord Of The Sith replaced Darth Vader, Betrayer Of The Jedi. "
    "Monnok replaced Evader / You Are Beaten. (AI) without (V) dested without (V). "
    "Unique overcounts sheet-accurate (Count Dooku x2, The Emperor (V) x2, Darth Maul With Lightsaber x2, "
    "Stunning Leader x3, Sense x2, Sneak Attack (V) x2, Force Lightning x3, "
    "The Phantom Menace x2, Disarmed x2). NO_DEST Jabba's Prize. (V) from typed (V) or checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Coruscant: Nightclub"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Anger, Fear, Aggression", True),
    n("Weapon Levitation"),
    n("Much To Learn You Still Have"),
    n("Hear Me Baby, Hold Together", True),
    n("Scrambled Transmission", True),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Houjix"),
    n("Control & Tunnel Vision"),
    n("Sense"),
    n("Escape Pod", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Jedi Levitation", True, qty=2),
    n("Speak With The Jedi Council", qty=5),
    n("Seeking An Audience", True),
    n("Mantellian Savrip"),
    n("Imperial Atrocity", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Leia, Rebel Princess", qty=2),
    n("Mace Windu", True, qty=2),
    n("Yoda, Master Of The Force", qty=3),
    n("Corran Horn"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Master Qui-Gon", True, qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Lady Luck"),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True, qty=2),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Your Ship?"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon", True),
    n("Planetary Defenses", True),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Carbonite Chamber Console", True),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Blockade Flagship: Bridge"),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Any Methods Necessary"),
    n("Despair", True),
    n("Jabba's Prize"),
    n("Maul's Sith Infiltrator"),
    n("Janus Greejatus"),
    n("Count Dooku", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Jango Fett, The Assassin"),
    n("The Emperor", True, qty=2),
    n("Mara Jade With Lightsaber"),
    n("Grand Admiral Thrawn"),
    n("Darth Vader With Lightsaber"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Maul"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Black Sun Fleet"),
    n("Stunning Leader", qty=3),
    n("Sense", qty=2),
    n("Imperial Barrier"),
    n("Imperial Artillery"),
    n("Force Lightning", qty=3),
    n("Defensive Fire", True),
    n("Control & Set For Stun"),
    n("A Dark Time For The Rebellion", True),
    n("The Phantom Menace", qty=2),
    n("No Escape"),
    n("Disarmed", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sneak Attack", True, qty=2),
    n("Evader / You Are Beaten"),
    n("Close Call", True),
    n("We Must Accelerate Our Plans"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance", True),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
]
DS_ADD = []
