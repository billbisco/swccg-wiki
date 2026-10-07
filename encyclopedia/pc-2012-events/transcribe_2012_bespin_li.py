#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Jim Li.

Source: 2012BespinRegionals.pdf pages 23–24.
p23 Light typed 2010 Xerox / p24 Dark typed 2010 Xerox.
Name Jim Li dested Jim Li analog leftover generate CANON /
player-stubs/Jim_Li.wiki. Username jimli.
Do not dest as a new person. Do not dest 2016–2019 Jim Li 60s again.
"""
from __future__ import annotations

PLAYER = "Jim Li"
USERNAME = "jimli"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2012 Bespin Regionals Jim Li LS.png"
DS_SCAN = "2012 Bespin Regionals Jim Li DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p23 Light typed 2010 Xerox / p24 Dark typed 2010 Xerox. "
    "Name Jim Li dested Jim Li analog leftover generate CANON / "
    "player-stubs/Jim_Li.wiki. Username jimli. Date 7/14/12 Event Bespin Regional. "
    "Do not dest as a new person. Do not dest 2016–2019 Jim Li 60s again."
)
LS_NOTE = (
    "Typed 2010 Xerox p23 Light. Name Jim Li dested Jim Li. Username jimli. LIGHT checked. "
    "Watch Your Step dested Watch Your Step / This Place Can Be A Little Rough analog leftover. "
    "Tatooine (EP1) dested Tatooine analog leftover Brist. Tatooine: DB dested Tatooine: Docking Bay. "
    "Artoo Detoo In Red 5 dested Artoo-Detoo In Red 5 qty=2. "
    "BoShek, Brash Smuggler dested analog leftover Gardner. "
    "Chewie's ATST dested Chewie's AT-ST True. "
    "Antilles Maneuver/Rebel Reinforcement dested Antilles Maneuver & Rebel Reinforcements True analog leftover Cooleo. "
    "OOC/TT dested Out Of Commission & Transmission Terminated qty=2. "
    "Han Solo, Courageous Smuggler True analog leftover. "
    "Tatooine: Lar's Moisture Farm dested Tatooine: Lars' Moisture Farm True. "
    "Houjix/Out Of Nowhere dested Houjix & Out Of Nowhere. "
    "Control/Tunnel Vision dested Control & Tunnel Vision qty=2. "
    "Anger, Fear, Agression dested Anger, Fear, Aggression True IN THE 60. "
    "Shield 12 empty skip unique 11 sheet-accurate analog leftover clip. Unique 60 shields 11."
)
DS_NOTE = (
    "Typed 2010 Xerox p24 Dark. Name Jim Li dested Jim Li. Username jimli. DARK checked. "
    "My Lord, Is That Legal? dested My Lord, Is That Legal? / I Will Make It Legal analog leftover Hendon. "
    "Short Range Fighters/Watch Your Back dested Short Range Fighters analog leftover Massung qty=2. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin analog leftover Atkin. "
    "Slave 1 dested Slave I, Symbol Of Fear True analog leftover. "
    "Yeb Yeb Adem 'thorn dested Yeb Yeb Adem'thorn analog leftover. "
    "Line 40 empty skip unique 60 sheet-accurate analog leftover clip. "
    "We'll Let Fate-a Decide crossed dest There Is No Try True analog leftover replacement. "
    "Knowledge And Defense True IN THE 60 analog leftover clip line 60. "
    "Shield 11 A Useless Gesture dested analog leftover clip. Shield 12 empty skip unique 11. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Docking Bay"),
    n("Tatooine: Cantina"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("I Must Be Allowed To Speak", True),
    n("Get To Your Ships"),
    n("Lando With Blaster Pistol"),
    n("Corellia", True),
    n("Talon Karrde", qty=2),
    n("Luke Skywalker", True, qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Wedge Antilles", True),
    n("Red Squadron 1"),
    n("BoShek, Brash Smuggler", True),
    n("Cantina Brawl"),
    n("Chewie's AT-ST", True),
    n("BoShek's Modified Light Freighter", True),
    n("Sergeant Doallyn", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Choke"),
    n("Grimtaash"),
    n("Melas", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Projection Of A Skywalker"),
    n("Sabotage", True),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Chewbacca", True),
    n("Dash Rendar"),
    n("Outrider"),
    n("Han Solo, Courageous Smuggler", True),
    n("Millennium Falcon"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Yotts Orren"),
    n("Ralltiir Freighter Captain"),
    n("Kessel"),
    n("X-wing Laser Cannon"),
    n("Corellian Retort", True),
    n("Houjix & Out Of Nowhere"),
    n("It Could Be Worse"),
    n("Mirax Terrik"),
    n("Imperial Atrocity", True, qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("A Few Maneuvers"),
    n("Pulsar Skate"),
    n("We're Doomed"),
    n("Old Ben"),
    n("It's A Hit"),
    n("Scrambled Transmission", True),
    n("Rebel Barrier"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Jabba's Prize", True),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Naboo"),
    n("Lott Dod", qty=3),
    n("Our Blockade Is Perfectly Legal"),
    n("Surface Defense", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("Limited Resources"),
    n("Senate Hovercam", qty=2),
    n("Short Range Fighters", qty=2),
    n("This Is Outrageous!"),
    n("Death Star: War Room"),
    n("Darth Vader", True),
    n("Comscan Detection"),
    n("Coruscant Guard"),
    n("Passel Argente"),
    n("Squabbling Delegates", qty=3),
    n("SFS L-s9.3 Laser Cannon"),
    n("Blast Door Controls"),
    n("Tatooine: Desert Landing Site"),
    n("Toonbuck Toora", qty=2),
    n("DS-61-2"),
    n("Stop Motion", True),
    n("First Strike"),
    n("Combat Response"),
    n("Baskol Yeesim"),
    n("Punishing One", True),
    n("The Phantom Menace"),
    n("Jango Fett, The Assassin", True),
    n("Baron Soontir Fel"),
    n("Orn Free Taa", qty=2),
    n("Dengar", True),
    n("Vader's Personal Shuttle", True),
    n("We Must Accelerate Our Plans"),
    n("Tikkes"),
    n("Saber 1"),
    n("Accepting Trade Federation Control"),
    n("Zuckuss", True),
    n("Mist Hunter", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("I Have You Now"),
    n("Yeb Yeb Adem'thorn"),
    n("Black 2", True),
    n("Edcel Bar Gane"),
    n("Aks Moe"),
    n("Motion Supported"),
    n("Cold Feet", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("Battle Order", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("There Is No Try", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Resistance", True),
    n("Secret Plans", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture"),
]
DS_ADD = []
