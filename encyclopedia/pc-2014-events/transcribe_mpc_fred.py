#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Brian Fred.

Source: MPC-2014-Day-1-Main-Event.pdf pages 39–40 (2013 form, 15 shields).
Username blank. Deck names Endor Ops / Palace Raiders.
"""
from __future__ import annotations

PLAYER = "Brian Fred"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 40
DS_PAGE = 39
LS_SCAN = "2014 Match Play Championship Day 1 Brian Fred LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Brian Fred DS.png"
LS_DECK_NAME = "Palace Raiders"
DS_DECK_NAME = "Endor Ops"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name B Fred dested Brian Fred. Username blank. LIGHT "
    "checked. Deck Palace Raiders. We'll Handle This / Fish Flag dested We'll Handle This "
    "/ Duel Of The Fates. Fallen Jedi dested Maris Brood, Fallen Jedi. Naked 3PO dested "
    "Threepio With His Parts Showing. SATM/BP dested Sorry About The Mess & Blaster "
    "Proficiency. Unique overcounts sheet-accurate (Imperial Atrocity (V) x2, Jedi "
    "Lightsaber (V) x2, Mace Windu (V) x2, Nabrun Leids x2, Blaster Deflection x2, Let "
    "The Wookiee Win (V) x3, Sorry About The Mess & Blaster Proficiency x2, Impressive, "
    "Most Impressive (V) x2, Obi-Wan Kenobi, Jedi Knight (V) x2, Jedi Advisor x2, Qui-Gon "
    "Jinn With Lightsaber x2, Speak With The Jedi Council x2, A Jedi's Resilience x3, "
    "Sense x3). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. DARK checked. Deck Endor Ops; line 1 Carbon "
    "Chamber Testing dested Carbon Chamber Testing / My Favorite Decoration. Jabba's Prize "
    "dested Jabba's Prize / Jabba's Prize. Control/SFS dested "
    "Control & Set For Stun. SRF/WYB dested Short Range Fighters & Watch Your Back!. "
    "Jango Assassin dested Jango Fett, The Assassin. Slave I Symbol dested Slave I, Symbol "
    "Of Fear. Line 40 Prepared Imp Barrier crossed dested Imperial Barrier (unique "
    "overcount). Unique overcounts sheet-accurate (Force Lightning x2, Defensive Fire (V) "
    "x2, Sense x2, Stunning Leader x2, The Emperor (V) x2, Imperial Barrier x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates", True),
    n("Much To Learn, You Still Have"),
    n("Imperial Atrocity", True, qty=2),
    n("Jedi Lightsaber", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Alter"),
    n("Nabrun Leids", qty=2),
    n("Blaster Deflection", qty=2),
    n("Civil Disorder", True),
    n("Changing The Odds", True),
    n("Hear Me Baby, Hold Together", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Impressive, Most Impressive", True, qty=2),
    n("Honor Of The Jedi"),
    n("Your Insight Serves You Well"),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("Ki-Adi-Mundi", True),
    n("Yoda, Senior Council Member", True),
    n("Maris Brood, Fallen Jedi"),
    n("Jedi Advisor", qty=2),
    n("Coruscant: Night Club"),
    n("A Jedi's Plans"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Republic Logistics"),
    n("Coruscant: Senate Landing Platform"),
    n("Coruscant: Jedi Archives"),
    n("Menace Fades"),
    n("It Could Be Worse"),
    n("Depa Billaba"),
    n("Plo Koon"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("We're Doomed"),
    n("Speak With The Jedi Council", qty=2),
    n("A Jedi's Resilience", qty=3),
    n("Sense", qty=3),
    n("Threepio With His Parts Showing"),
    n("Heading For The Medical Frigate"),
    n("Obi-Wan's Lightsaber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Ultimatum", True),
    n("He Can Go About His Business", True),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Planetary Defenses", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Despair", True),
    n("Blockade Flagship: Bridge"),
    n("Dagobah: Cave"),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console", True),
    n("Cloud City: Security Tower", True),
    n("Black Sun Fleet"),
    n("No Escape"),
    n("Protocol Failure"),
    n("Force Lightning", qty=2),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("Blow Parried"),
    n("Any Methods Necessary"),
    n("Defensive Fire", True, qty=2),
    n("The Circle Is Now Complete"),
    n("Sense", qty=2),
    n("Victory"),
    n("Grand Admiral Thrawn"),
    n("Jabba's Prize / Jabba's Prize"),
    n("Commander Igar", True),
    n("Cold Feet", True),
    n("Control & Set For Stun"),
    n("Maul's Sith Infiltrator"),
    n("Darth Maul"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Stunning Leader", qty=2),
    n("Imperial Barrier", qty=2),
    n("The Emperor", True, qty=2),
    n("I Have You Now"),
    n("Elis Helrot"),
    n("A Dark Time For The Rebellion", True),
    n("Masterful Move"),
    n("Imperial Artillery"),
    n("The Phantom Menace"),
    n("Kashyyyk"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Slave I, Symbol Of Fear"),
    n("Sneak Attack", True),
    n("Boba Fett, Prepared Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("Jango Fett, The Assassin"),
    n("We Must Accelerate Our Plans"),
    n("Lightsaber Deficiency", True),
    n("Darth Vader With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Imperial Command"),
    n("Disarmed"),
    n("Darth Maul With Lightsaber"),
    n("IG-88's Neural Inhibitor", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Leave Them To Me", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Battle Order"),
    n("Imperial Detention"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
