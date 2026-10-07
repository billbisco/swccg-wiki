#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Brian Brodsky.

Source: MPC-2014-Day-1-Main-Event.pdf pages 23–24 (2013 form, 15 shields).
Username bbrodsky50egmail.
"""
from __future__ import annotations

PLAYER = "Brian Brodsky"
USERNAME = "bbrodsky50egmail"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2014 Match Play Championship Day 1 Brian Brodsky LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Brian Brodsky DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "Give Him The Ball!!"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username blank on Light. LIGHT/DARK empty. Communing (V) "
    "dested Communing. Commando Training + K'lor'slug dested Commando Training & "
    "K'lor'slug. Alderaan Consular Ship dested Radiant VII. Control/Tunnel dested Control "
    "& Tunnel Vision. Unique overcounts sheet-accurate (Escape Pod (V) x3, Run Luke, Run! "
    "(V) x2, Luke With Lightsaber x3, Let The Wookiee Win (V) x2, Chewie, Enraged (V) x2, "
    "Chewbacca, Protector x2, Artoo-Detoo In Red 5 x2, Rebel Leadership (V) x2). Shield "
    "Odin's Prize dested Odin's Prize as written (NO_DEST). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username bbrodsky50egmail. DARK checked. Deck Give Him The "
    "Ball!!. Carbon Chamber Testing / MFD dested Carbon Chamber Testing / My Favorite "
    "Decoration. Jabba's Prize dested Jabba's Prize / Jabba's Prize. The Mandalorian, "
    "Father Of Fett dested Jango Fett, The Assassin. SRF/Watch Your Back dested Short "
    "Range Fighters & Watch Your Back!. Ghhhk + TRWEU dested Ghhhk & Those Rebels Won't "
    "Escape Us. Control/Set For Stun dested Control & Set For Stun. Unique overcounts "
    "sheet-accurate (The Emperor (V) x2, Sonic Bombardment (V) x2, Darth Maul With "
    "Lightsaber x3, Maul's Sith Infiltrator x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug", True),
    n("Master Kenobi"),
    n("Yoda, Great Warrior"),
    n("Tatooine: Cantina"),
    n("Lucky Shot", True),
    n("Escape Pod", True, qty=3),
    n("Draw Their Fire"),
    n("Nick Of Time", True),
    n("Luke With Lightsaber", qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Run Luke, Run!", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Projection Of A Skywalker"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Chewie, Enraged", True, qty=2),
    n("Seeking An Audience", True),
    n("Rebel Gunrunner", True),
    n("Chewbacca's Bowcaster"),
    n("Chewbacca, Protector", qty=2),
    n("Use The Force", True),
    n("Imperial Atrocity", True),
    n("Hear Me Baby, Hold Together", True),
    n("Tatooine"),
    n("Sorry About The Mess"),
    n("Admiral Ackbar", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Han With Heavy Blaster Pistol"),
    n("Radiant VII"),
    n("Corran Horn"),
    n("Artoo-Detoo In Red 5", True),
    n("Wedge Antilles", True),
    n("Senator Leia Organa"),
    n("Home One: War Room"),
    n("Either Way, You Win", True),
    n("Launching The Assault", True),
    n("Rebel Leadership", True, qty=2),
    n("Strikeforce", True),
    n("Artoo-Detoo In Red 5"),
    n("Lando Calrissian, Scoundrel", True),
    n("Shmi Skywalker"),
    n("Home One"),
    n("Scrambled Transmission", True),
    n("Houjix"),
    n("Jedi Levitation"),
    n("Control & Tunnel Vision"),
    n("Padme Naberrie", True),
    n("Flash Of Insight", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Odin's Prize", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console", True),
    n("Cloud City: Security Tower", True),
    n("Jabba's Prize / Jabba's Prize"),
    n("Any Methods Necessary"),
    n("Emperor's Power", True),
    n("Ghhhk"),
    n("Image Of The Dark Lord", True),
    n("Special Delivery", True),
    n("I Have You Now"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sonic Bombardment", True, qty=2),
    n("Stunning Leader"),
    n("Cold Feet", True),
    n("Sense"),
    n("The Emperor", True, qty=2),
    n("Security Precautions", True),
    n("Stormtrooper Garrison"),
    n("Black Sun Fleet", True),
    n("Protocol Failure", True),
    n("Jango Fett, The Assassin", True),
    n("Elis Helrot"),
    n("Mara Jade With Lightsaber", True),
    n("Slave I, Symbol Of Fear", True),
    n("Masterful Move & Endor Occupation"),
    n("Grand Moff Tarkin", True),
    n("No Escape"),
    n("A Dark Time For The Rebellion", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("First Strike"),
    n("Astromech Shortage", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("IG-88's Neural Inhibitor", True),
    n("4-LOM With Concussion Rifle", True),
    n("Jabba's Palace: Dungeon"),
    n("Darth Vader With Lightsaber"),
    n("Dagobah: Cave"),
    n("4-LOM With Concussion Rifle", True),
    n("Control & Set For Stun"),
    n("IG-88", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Lightsaber Deficiency", True),
    n("Boba Fett, Prepared Hunter"),
    n("The Phantom Menace"),
    n("Imperial Propaganda", True),
    n("Imperial Barrier"),
    n("Force Lightning"),
    n("Myn Kyneugh", True),
    n("Kashyyyk"),
    n("Despair", True),
    n("Imperial Artillery"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
