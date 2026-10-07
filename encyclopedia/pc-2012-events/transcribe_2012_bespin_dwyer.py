#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Morgan Dwyer.

Source: 2012BespinRegionals.pdf pages 27–28.
p27 Dark handwritten 2010 Xerox / p28 Light handwritten 2010 Xerox.
Name Morgan Dwyer dested Morgan Dwyer analog leftover encyclopedia / generate /
player-stubs empty dest Name box as written. USERNAME blank.
Event Surg / Star dested off article dest both as Bespin facing pair analog leftover
Herold joke Event. Pack player-stubs/Morgan_Dwyer.wiki.
"""
from __future__ import annotations

PLAYER = "Morgan Dwyer"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 28
DS_PAGE = 27
LS_SCAN = "2012 Bespin Regionals Morgan Dwyer LS.png"
DS_SCAN = "2012 Bespin Regionals Morgan Dwyer DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p27 Dark handwritten 2010 Xerox / p28 Light handwritten 2010 Xerox. "
    "Name Morgan Dwyer dested Morgan Dwyer analog leftover empty dest Name box as written. "
    "USERNAME blank. Event Date blank. Event Surg / Star dested off article dest both as "
    "Bespin facing pair analog leftover Herold joke Event. Deck Name walkin war dested off article. "
    "Pack player-stubs/Morgan_Dwyer.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p28 Light. Name Morgan Dwyer dested Morgan Dwyer. USERNAME blank. LIGHT checked. "
    "MWYH True dested Mind What You Have Learned / Save You It Can True analog leftover Consoli Day 2. "
    "Strong Is Vader dested dest-as-written analog leftover Consoli. "
    "Battle Plan Combo dested Battle Plan & Draw Their Fire analog leftover Consoli. "
    "Do or Do Not Combo dested Do, Or Do Not & Wise Advice analog leftover Consoli. "
    "It Is The Future You See dested analog leftover Consoli. "
    "Mace Windu True line 15 and empty line 16 kept separate. "
    "Obi-Wan Kenobi True line 17 and empty line 26 kept separate. "
    "Luke Skywalker, Jedi Knight empty line 25 and True line 52 kept separate analog leftover Frafjord. "
    "The Signal empty line 53 and True line 54 kept separate. "
    "Major Haash'n dested analog leftover Consoli. Fallen Jedi True dested analog leftover Consoli. "
    "The Way Of Things dested analog leftover Consoli. Yoda's Hope True dested analog leftover Frafjord. "
    "Anger, Fear, Aggression True IN THE 60. Shield 12 empty skip unique 11 sheet-accurate analog leftover clip. Unique 60 shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p27 Dark. Name Morgan Dwyer dested Morgan Dwyer. USERNAME blank. DARK checked. "
    "Tatooine dested Tatooine analog leftover Brist line 1 site. "
    "Combat Readiness dested Combat Readiness / Full Scale Alert analog leftover Brist. "
    "Blizzard 4 dested analog leftover Peterson. AT-AT Cannon True dested analog leftover Rambo. "
    "Native's Hut dested Tatooine: Native Hut dest as written. "
    "Darth Vader, Betrayer Of Jedi dested analog leftover TYPE_OVERRIDE. "
    "See-Threepio dested U-3PO analog leftover Wirfs. "
    "Walker Garrison dested analog leftover Rambo. AT-AT dest as written TYPE_OVERRIDE Starship. "
    "Knowledge And Defense True IN THE 60 analog leftover. "
    "Shield 12 empty skip unique 11 sheet-accurate analog leftover clip. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Strong Is Vader"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("It Is The Future You See"),
    n("Houjix", qty=2),
    n("A Jedi's Resilience"),
    n("A Jedi's Plans"),
    n("Alter", True),
    n("Escape Pod", True),
    n("Always In Motion The Future Is", True),
    n("Sense", True),
    n("Dagobah: Yoda's Hut"),
    n("Imperial Atrocity", True),
    n("Mace Windu", True),
    n("Mace Windu"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Lightsaber Proficiency"),
    n("Rebel Barrier"),
    n("Luke's Backpack", True),
    n("Quick Draw", True),
    n("Artoo-Detoo In Red 5"),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Jedi Knight"),
    n("Obi-Wan Kenobi"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Dagobah: Jungle"),
    n("Blaster Deflection", qty=2),
    n("Major Haash'n"),
    n("Yoda", True, qty=2),
    n("Scrambled Transmission", True),
    n("Fallen Jedi", True),
    n("Sense & Recoil In Fear"),
    n("A Jedi's Focus", True),
    n("Anakin's Lightsaber", True),
    n("Obi-Wan's Lightsaber", qty=2),
    n("Thrown Back", True),
    n("Admiral Ackbar", True),
    n("Yoda, Senior Council Member"),
    n("The Way Of Things"),
    n("Grimtaash", True),
    n("Ben Kenobi"),
    n("Luke Skywalker", qty=3),
    n("Luke Skywalker, Jedi Knight", True),
    n("The Signal"),
    n("The Signal", True),
    n("Yoda's Hope", True, qty=2),
    n("Dash Rendar"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Wise Advice"),
    n("The Professor"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("A Jedi's Resilience"),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here"),
]
LS_ADD = []

DS_START = "Combat Readiness / Full Scale Alert"
DS_CARDS = [
    n("Tatooine"),
    n("Blizzard 4"),
    n("Arica"),
    n("Tatooine: Native Hut"),
    n("AT-AT Cannon", True),
    n("Combat Readiness / Full Scale Alert"),
    n("Darth Vader"),
    n("TIE/ln", True),
    n("Probe Droid"),
    n("Snowtrooper"),
    n("Darth Maul"),
    n("IG-88", qty=2),
    n("Jabba The Hutt"),
    n("Stormtrooper"),
    n("Boba Fett"),
    n("U-3PO"),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Ghhhk", True),
    n("Presence Of The Force"),
    n("Control"),
    n("Imperial Command"),
    n("Trample", True),
    n("Walker Garrison"),
    n("Weapon Levitation"),
    n("Force Field", True),
    n("Mara Jade", True),
    n("AT-AT", qty=2),
    n("Imperial Decree", True),
    n("Search And Destroy", True),
    n("Hoth: Ice Plains"),
    n("Hoth: Main Power Generators"),
    n("You May Start Your Landing"),
    n("Sense", qty=2),
    n("Cease Fire!"),
    n("Cold Feet", True),
    n("Protocol Failure"),
    n("You Are Beaten"),
    n("A Dark Time For The Rebellion", True),
    n("Masterful Move & Endor Occupation", True),
    n("Imbalance & Kintan Strider", True),
    n("Target The Main Generator"),
    n("Something Special Planned For Them", True),
    n("Image Of The Dark Lord", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Tempest 1"),
    n("Veers", True),
    n("General Nevar"),
    n("Commander Igar", True),
    n("Grand Moff Tarkin", True),
    n("Admiral Motti", True),
    n("Flagship Executor"),
    n("Endor Shield", True),
    n("Prepared Defenses"),
    n("Hoth: Mountains"),
    n("Hoth Blockade"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Firepower"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture"),
    n("Secret Plans"),
    n("You Cannot Hide Forever"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
]
DS_ADD = []
