#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Jeeps.

Source: 2012NationalsDay1.pdf pages 32–33 (handwritten 2010 Xerox, 12 shields).
Name blank both. Username Jeeps / jeeps dested Jeeps as written.
p32 Light Hidden Base. p33 Dark A Stunning Move.
Analog leftover generate empty dest Username as written.
Do not dest as Unknown Player. Do not dest as a new identified person until analog identifies.
Pack player-stubs/Jeeps.wiki.
"""
from __future__ import annotations

PLAYER = "Jeeps"
USERNAME = "Jeeps"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 32
DS_PAGE = 33
LS_SCAN = "2012 US Nationals Day 1 Jeeps LS.png"
DS_SCAN = "2012 US Nationals Day 1 Jeeps DS.png"
LS_DECK_NAME = "Matt Thornton Wishes It was here so hard"
DS_DECK_NAME = "Widdershins!"
NOTE = "Handwritten 2010 Xerox. Name blank. Username Jeeps dested Jeeps as written."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name blank. Username Jeeps dested Jeeps as written. "
    "LIGHT checked. Deck Name Matt Thornton Wishes It was here so hard. "
    "Event Name Nat '12. Analog leftover generate empty dest Username as written. "
    "Do not dest as Unknown Player. Do not dest as a new identified person until analog identifies. "
    "Hidden Base True dested Hidden Base / Systems Will Slip Through Your Fingers True analog leftover Herold. "
    "Strikeforce True dested analog leftover Hanson. "
    "Uncharted Settlements True dested analog leftover Herold. "
    "Rebel Cell sites dested Rebel Cell - Hidden Landing Site / Monitoring Station / Situation Room True analog leftover Jankowski. "
    "Rebell Cell Situation Room (with Wolf Blitzer) dested Rebel Cell - Situation Room True analog leftover. "
    "Yavin IV dested Yavin 4 True analog leftover. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin analog leftover Veasey x4 unique overcount. "
    "Red 5 dested Artoo-Detoo In Red 5 True analog leftover. "
    "Obi-Wan with Lightsaber dested Obi-Wan With Lightsaber analog leftover Graham. "
    "Qui-Gon Jinn with Lightsaber dested Qui-Gon Jinn With Lightsaber analog leftover Graham. "
    "X-win Laser Cannon dested X-wing Laser Cannon analog leftover Erwin. "
    "Millenium Falcon dested Millennium Falcon True analog leftover Grouty. "
    "Out of Commission & Trans. Term. dested Out Of Commission & Transmission Terminated analog leftover Amato. "
    "Chewie dested Chewie, Enraged True analog leftover Erwin. "
    "R2-D2 dested R2-D2 (Artoo-Detoo) True analog leftover Ziagos. "
    "Leia dested Princess Leia True analog leftover. "
    "Captain Han dested Captain Han Solo True analog leftover. "
    "Projection of a Skywalker dested Projection Of A Skywalker analog leftover 2013 MPC Herold. "
    "Line 41 cropped dest Houjix analog leftover sequential before Houjix. "
    "Let the Wookiee Win dested Let The Wookiee Win True analog leftover Hanson. "
    "Owen Lars & Beru Lars dested analog leftover Nelson. "
    "Artoo & Threepio dested analog leftover. "
    "AFA dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "Battle Plab dested Battle Plan analog leftover. "
    "Only a Jedi Carry That Weapon dested Only Jedi Carry That Weapon analog leftover Bordier. "
    "Your Ship? dested analog leftover. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name blank. Username jeeps dested Jeeps as written. "
    "DARK checked. Deck Name Widdershins!. Event Name Nationals 2012. "
    "Analog leftover generate empty dest Username as written. "
    "Do not dest as Unknown Player. Do not dest as a new identified person until analog identifies. "
    "A Stunning Move / A Valuable Hostage True dested analog leftover Anderson. "
    "Slave 1 dested Slave I, Symbol Of Fear True analog leftover TMW Herold. "
    "Boba Fett, Prepared Hunter dested Boba Fett, Bounty Hunter True analog leftover Anderson. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin True analog leftover. "
    "Galen, Secret Apprentice dested as written analog leftover True x3 unique overcount. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover TMW Herold. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi analog leftover True then empty kept separate. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "The Phatom Menace dested The Phantom Menace analog leftover Kelly. "
    "Gift of the Master dested Gift Of The Master True analog leftover TMW Herold. "
    "Ni Chuba Na?? dested analog leftover Anderson. "
    "Dr. Evazan & Ponda Paba dested Dr. Evazan & Ponda Baba analog leftover Herold. "
    "Elis in Hinthra dested Elis In Hinthra True analog leftover Anderson. "
    "Grotto Werribee dested analog leftover Pinto. "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter analog leftover Anderson. "
    "Trophy of a Kill dested Trophy Of A Kill True analog leftover TMW Herold. "
    "Weapon Levitation & The Empire's Back dested analog leftover TMW Herold. "
    "Line 41 cropped dest You Are Beaten analog leftover sequential before You Are Beaten. "
    "Dengar With Blaster Carbine dested analog leftover. "
    "P-59 dested analog leftover Frafjord. "
    "Breached Defenses & Molator dested analog leftover combo. "
    "Prepared Defenses True dested analog leftover IN THE 60. "
    "Come Back Here You Big Coward dested Come Here You Big Coward analog leftover Anderson. "
    "Allegations of Corruptions dested Allegations Of Corruption analog leftover. "
    "I Find Your Lack of Faith Disturbing dested analog leftover Ziagos. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Strikeforce", True),
    n("Uncharted Settlements", True),
    n("Squadron Assignments"),
    n("Rebel Cell - Hidden Landing Site", True),
    n("Rebel Cell - Monitoring Station", True),
    n("Rebel Cell - Situation Room", True),
    n("Yavin 4", True),
    n("Haven"),
    n("All Wings Report In & Darklighter Spin", qty=4),
    n("Artoo-Detoo In Red 5", True),
    n("Tigran Jamiro", True),
    n("Luke Skywalker", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda, Great Warrior", True),
    n("Red Squadron 1"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Corellian Retort", True),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("X-wing Laser Cannon"),
    n("K'lor'slug", True),
    n("Spiral", qty=2),
    n("Hindsight", True),
    n("Rogue 1"),
    n("Commander Luke Skywalker", True),
    n("Millennium Falcon", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Chewie, Enraged", True),
    n("Dual Laser Cannon"),
    n("Tantive IV", True),
    n("Corran Horn"),
    n("Jedi Levitation", True),
    n("Colonel Feyn Gospic", True),
    n("R2-D2 (Artoo-Detoo)", True),
    n("Princess Leia", True, qty=2),
    n("Captain Han Solo", True),
    n("Projection Of A Skywalker"),
    n("Houjix", qty=2),
    n("Escape Pod", True, qty=2),
    n("Han Solo", True),
    n("Scomp Link Access", True),
    n("Let The Wookiee Win", True),
    n("Desperate Tactics", True),
    n("A Jedi's Resilience"),
    n("Chewbacca, Protector"),
    n("Artoo & Threepio", True),
    n("Leia's Blaster Rifle"),
    n("Combined Fleet Action"),
    n("Owen Lars & Beru Lars"),
    n("Taking Them With Us"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Battle Plan"),
    n("Your Ship?"),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Slave I, Symbol Of Fear", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("OOM-9", True),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Coruscant: Private Platform", True),
    n("Coruscant: Palpatine's Quarters"),
    n("Grievous, Hunter Of Jedi", True),
    n("Knowledge And Defense", True),
    n("The Phantom Menace", qty=2),
    n("Jabba's Haven", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Nal Hutta"),
    n("Disarmed"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Insidious Prisoner"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Elis In Hinthra", True),
    n("Battle Droid Squad", True, qty=2),
    n("Grotto Werribee", True),
    n("Grievous, Hunter Of Jedi"),
    n("Dark Jedi Lightsaber", True),
    n("Zuckuss In Mist Hunter"),
    n("Trophy Of A Kill", True),
    n("Death Star: War Room", True),
    n("Blockade Flagship: Bridge"),
    n("Weapon Levitation & The Empire's Back", True),
    n("No Escape"),
    n("Operational As Planned", True),
    n("Guri"),
    n("Force Field", True),
    n("You Are Beaten", qty=2),
    n("Probot", True),
    n("Dengar With Blaster Carbine", True),
    n("Maul Strikes"),
    n("Prince Xizor"),
    n("P-59"),
    n("ComScan Detection", True),
    n("Tarkin's Bounty", True),
    n("Victory", True),
    n("Cold Feet", True),
    n("Restraining Bolt"),
    n("Breached Defenses & Molator"),
    n("Why Didn't You Tell Me?", True),
    n("Masterful Move"),
    n("Prepared Defenses", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("After Her!", True),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
