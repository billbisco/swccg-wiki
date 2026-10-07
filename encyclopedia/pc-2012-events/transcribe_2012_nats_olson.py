#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Nick Olson.

Source: 2012NationalsDay1.pdf pages 54–55 (typed 2010 Xerox, 11 shields).
p54 Dark / p55 Light Name Nick Olson Username Nick1652 dested Nick Olson analog leftover empty.
Pack player-stubs/Nick_Olson.wiki.
"""
from __future__ import annotations

PLAYER = "Nick Olson"
USERNAME = "Nick1652"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 55
DS_PAGE = 54
LS_SCAN = "2012 US Nationals Day 1 Nick Olson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Nick Olson DS.png"
LS_DECK_NAME = "<<10011-01100>>"
DS_DECK_NAME = "<<10011-00100>>"
NOTE = (
    "Typed 2010 Xerox. Name Nick Olson dested Nick Olson analog leftover empty. "
    "Username Nick1652. Event Date 6/9/2012 Event Name Nationals."
)
LS_NOTE = (
    "Typed 2010 Xerox. Name Nick Olson dested Nick Olson analog leftover empty. "
    "Username Nick1652. LIGHT checked. Event Date 6/9/2012 Event Name Nationals. "
    "Deck Name <<10011-01100>> stays off the article. "
    "LS_START You Can Either Profit By This... / Or Be Destroyed analog leftover Brady. "
    "Han dested Han Solo True analog leftover Brady. "
    "IL-19 dested IL-19 True analog leftover Morgan leftover_xerox. "
    "Threepio With His Parts Showing dested Threepio With His Parts Showing analog leftover Burgt. "
    "Padme Naberrie dested Padmé Naberrie True analog leftover Brady. "
    "Eject combo dested Eject! Eject! Eject! & Imperial Atrocity True analog leftover Grant. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas True analog leftover Virtual Block. "
    "Run Luke, Run dested Run Luke, Run! analog leftover Grouty. "
    "Anger, Fear, Aggression dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Shield 12 blank skip. Unique 60. Shields 11."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Nick Olson dested Nick Olson analog leftover empty. "
    "Username Nick1652. DARK checked. Event Date 6/9/2012 Event Name Nationals. "
    "Deck Name <<10011-00100>> stays off the article. "
    "Imperial Occupation / Imperial Command dested Imperial Occupation / Imperial Control True analog leftover Twigg. "
    "Knowledge And Defense dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Hoth: Main Power Generators (LS) dested Hoth: Main Power Generators leftover_xerox. "
    "Black Leader dested Juno Eclipse, Black Leader True analog leftover George. "
    "Galen's Fighter dested Rogue Shadow True analog leftover George. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back! analog leftover. "
    "Shield You Cannot Hide Forever dested You Cannot Hide Forever True analog leftover. "
    "Shields 12 blank skip. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han Solo", True),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Boushh"),
    n("Princess Leia", True),
    n("Corran Horn"),
    n("Chewbacca, Protector"),
    n("Lando With Vibro-Ax"),
    n("Yoda, Great Warrior", True, qty=2),
    n("Padmé Naberrie", True, qty=2),
    n("IL-19", True),
    n("Artoo, Brave Little Droid", True),
    n("Threepio With His Parts Showing"),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Hoth: Echo Command Center"),
    n("Home One: War Room"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Anakin's Lightsaber", True),
    n("Leia's Blaster Rifle"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand", True),
    n("Tatooine Utility Belt", True),
    n("Eject! Eject! Eject! & Imperial Atrocity", True),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
    n("Lightsaber Proficiency"),
    n("Nabrun Leids"),
    n("Don't Forget The Droids", True, qty=2),
    n("Rebel Leadership", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Run Luke, Run!"),
    n("Impressive, Most Impressive", True),
    n("Jedi Levitation", True),
    n("Skywalkers"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Out Of Commission & Transmission Terminated"),
    n("Blaster Deflection"),
    n("Gift Of The Mentor"),
    n("Clash Of Sabers"),
]
LS_SHIELDS = [
    n("Battle Plan", True),
    n("Do, Or Do Not", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Ultimatum", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Knowledge And Defense", True),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("Prepared Defenses"),
    n("Prepare For A Surface Attack"),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Admiral Motti", True),
    n("Darth Maul", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("General Nevar", True),
    n("Grand Admiral Thrawn"),
    n("Garindan", True, qty=2),
    n("Admiral Piett"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Juno Eclipse, Black Leader", True),
    n("ISB Sector Commander", True),
    n("Veers", True),
    n("Commander Igar", True),
    n("The Empire's Back"),
    n("AT-AT Cannon", True),
    n("Maul's Sith Infiltrator"),
    n("Rogue Shadow", True),
    n("Executor"),
    n("Zuckuss In Mist Hunter"),
    n("Target The Main Generator"),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6", True),
    n("Something Special Planned For Them", True),
    n("Do They Have A Code Clearance?"),
    n("Protocol Failure", True),
    n("Lateral Damage"),
    n("Hoth Blockade", True),
    n("We're In Attack Position Now", qty=2),
    n("Battle Deployment"),
    n("Limited Resources"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control & Set For Stun", qty=2),
    n("Walker Garrison"),
    n("Cold Feet", True),
    n("Stop Motion", True, qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("He Hasn't Come Back Yet"),
    n("Trample", qty=2),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
]
DS_SHIELDS = [
    n("Battle Order", True),
    n("There Is No Try", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward", True),
    n("Secret Plans", True),
    n("Fanfare", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Resistance", True),
    n("Firepower", True),
]
DS_ADD = []
