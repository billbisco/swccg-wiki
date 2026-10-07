#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Amar Banger.

Source: 2012TMWDay1.pdf pages 24–25 (HTML GEMP printouts Court.html / Profit.html,
not a handwritten Xerox form). Handwritten Amar Banger dested Amar Banger analog
leftover 2013 TMW / 2012 MPC / 2013 Worlds / player-stubs/Amar_Banger.wiki.
Username abanger analog leftover 2013 TMW. p24 Dark Courtroom Mains. p25 Light
False Profit. Do not dest as a new person. Do not dest 2013 TMW / 2012 MPC /
2013 Worlds / 2014 TMW / 2014 MPC Banger 60s again.
"""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = "abanger"
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 25
DS_PAGE = 24
LS_SCAN = "2012 Texas Mini Worlds Day 1 Amar Banger LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Amar Banger DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "HTML GEMP printouts p24 Dark Court.html / p25 Light Profit.html. "
    "Handwritten Amar Banger dested Amar Banger analog leftover 2013 TMW. "
    "Username abanger analog leftover 2013 TMW. Do not dest as a new person. "
    "Do not dest 2013 TMW / 2012 MPC / 2013 Worlds / 2014 TMW / 2014 MPC Banger 60s again."
)
LS_NOTE = (
    "HTML GEMP printout Profit.html p25 Light False Profit. "
    "Handwritten Amar Banger dested Amar Banger analog leftover 2013 TMW. "
    "Username abanger analog leftover 2013 TMW. Do not dest as a new person. "
    "You Can Either Profit By This.../Or Be Destroyed dested You Can Either Profit By This analog leftover dual-title. "
    "Han (V3) dested Han analog leftover 2013 MPC Tuan Le. "
    "Chewie (V2) dested Chewie analog leftover 2013 Alderaan. "
    "Leia (V1) dested Leia analog leftover 2012 MPC. "
    "Artoo-Detoo In Red 5 dested analog leftover Hendon. "
    "Luke Skywalker, Strong In The Force dested analog leftover. "
    "Captain Yutani With Blaster Cannon dested analog leftover 2014 Worlds. "
    "Wesa Gotta Grand Army dested analog leftover. "
    "Threepio With His Parts Showing dested analog leftover 2013 TMW Banger Naked 3PO. "
    "Sai'torr Kal Fas dested analog leftover True. "
    "Coruscant: Jedi Council Chamber dested analog leftover JCC. "
    "Naboo: Boss Nass' Chambers dested analog leftover Nass Chamber. "
    "Seeking An Audience dested analog leftover Angelo. "
    "Heading For The Medical Frigate dested analog leftover HFTMF. "
    "Under Attack crossed dest replacement Mechanical Failure analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "HTML GEMP printout Court.html p24 Dark Courtroom Mains. "
    "Handwritten Amar Banger dested Amar Banger analog leftover 2013 TMW. "
    "Username abanger analog leftover 2013 TMW. Do not dest as a new person. "
    "Court Of The Vile Gangster/I Shall Enjoy Watching You Die dested Court Of The Vile Gangster analog leftover dual-title. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi analog leftover Hendon. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover. "
    "Galen, Secret Apprentice dested analog leftover. "
    "Knowledge And Defense True dested analog leftover Anderson IN THE 60. "
    "Gift Of The Master dested analog leftover. "
    "Ni Chuba Na?? dested analog leftover. "
    "4-LOM With Concussion Rifle dested analog leftover Erwin. "
    "Boba Fett, Bounty Hunter dested analog leftover Nats. "
    "Jabba's Palace: Dungeon dested analog leftover Krueger. "
    "Masterful Move & Endor Occupation dested analog leftover Kirkpatrick. "
    "Weapon Levitation & The Empire's Back dested analog leftover Nathan. "
    "Where Are You Taking This ... Thing? dested analog leftover 2013 MPC Shaw. "
    "The Phantom Menace dested analog leftover Kirkpatrick. "
    "Victory dested analog leftover mpc. "
    "Zuckuss In Mist Hunter dested analog leftover MPC Anderson. "
    "IG-88 With Riot Gun dested analog leftover. "
    "We'll Let Fate-a Decide, Huh? dested analog leftover Lush. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Han", True),
    n("Heading For The Medical Frigate"),
    n("Jabba's Palace: Audience Chamber"),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("Tatooine: Jabba's Palace"),
    n("Wokling", True),
    n("You Can Either Profit By This"),
    n("A Gift"),
    n("Admiral Ackbar", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Artoo-Detoo In Red 5"),
    n("Blaster Deflection", qty=2),
    n("Captain Yutani With Blaster Cannon", True),
    n("Chewie", True),
    n("Corran Horn"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Draw Their Fire"),
    n("Hear Me Baby, Hold Together", True),
    n("Hindsight", True),
    n("Home One"),
    n("Home One: War Room"),
    n("Impressive, Most Impressive", True),
    n("Inconsequential Barriers"),
    n("Insurrection"),
    n("Jedi Lightsaber", True),
    n("Ki-Adi-Mundi", True),
    n("Kiffex"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia", True),
    n("Lucky Shot", True),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Luke's Lightsaber"),
    n("Mace Windu", True, qty=2),
    n("Merc Sunlet"),
    n("Millennium Falcon"),
    n("Naboo: Boss Nass' Chambers"),
    n("Nick Of Time", True),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Rebel Leadership", True, qty=3),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Speak With The Jedi Council"),
    n("Threepio With His Parts Showing"),
    n("Mechanical Failure"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Your Insight Serves You Well"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Only Jedi Carry That Weapon"),
    n("Ounee Ta"),
    n("Simple Tricks And Nonsense", True),
    n("Traffic Control", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Court Of The Vile Gangster"
DS_CARDS = [
    n("Court Of The Vile Gangster"),
    n("Gift Of The Master", True),
    n("Jabba's Haven", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Knowledge And Defense", True),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses", True),
    n("Tatooine: Great Pit Of Carkoon"),
    n("4-LOM With Concussion Rifle", True),
    n("Ability, Ability, Ability", True),
    n("Aurra Sing"),
    n("Blast Door Controls"),
    n("Blaster Rack", True),
    n("Boba Fett, Bounty Hunter"),
    n("Bounty", True),
    n("Comscan Detection", True, qty=2),
    n("Crossfire", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Dark Jedi Lightsaber", True),
    n("Darth Maul", qty=3),
    n("Darth Sidious"),
    n("Darth Vader With Lightsaber"),
    n("Dengar With Blaster Carbine", True),
    n("Executor: Docking Bay"),
    n("Executor: Meditation Chamber"),
    n("First Strike"),
    n("Force Field", True, qty=2),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Garindan", True),
    n("Ghhhk"),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("I've Lost Artoo!", True),
    n("IG-88 With Riot Gun"),
    n("Mara Jade With Lightsaber", True),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("Maul's Sith Infiltrator"),
    n("Nal Hutta"),
    n("No Escape"),
    n("Rodian", True),
    n("Search And Destroy"),
    n("Something Special Planned For Them", True),
    n("Special Delivery", True),
    n("Swilla Corey"),
    n("The Phantom Menace"),
    n("Victory", True),
    n("Weapon Levitation & The Empire's Back", True),
    n("Where Are You Taking This ... Thing?", True),
    n("Wipe Them Out, All Of Them", True),
    n("You Cannot Hide Forever"),
    n("Zuckuss In Mist Hunter"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Reactor Terminal", True),
    n("Resistance"),
    n("Secret Plans"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
