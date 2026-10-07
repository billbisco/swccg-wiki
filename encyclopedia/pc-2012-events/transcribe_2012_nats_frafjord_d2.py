#!/usr/bin/env python3
"""2012 US Nationals Day 2 leftover Xerox: Tom Frafjord.

Source: 2012NationalsDay2.pdf pages 3–4 (handwritten 2010 Xerox, 12 shields).
Name Tom Frafjord dested Tom Frafjord analog leftover Day 1 / 2008 Worlds.
Username citizenSwanky.
p03 Dark My Lord, Is That Legal?. p04 Light Mind What You Have Learned.
Do not dest as a new person. Do not dest Day 1 Frafjord 60s again.
"""
from __future__ import annotations

PLAYER = "Tom Frafjord"
USERNAME = "citizenSwanky"
STAGE = "Day 2"
PDF = "2012 US Nationals Day 2.pdf"
LS_PAGE = 4
DS_PAGE = 3
LS_SCAN = "2012 US Nationals Day 2 Tom Frafjord LS.png"
DS_SCAN = "2012 US Nationals Day 2 Tom Frafjord DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Username citizenSwanky. Event Date 06/10/12 Event Name Nationals. "
    "Do not dest as a new person. Do not dest Day 1 Frafjord 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Tom Frafjord dested Tom Frafjord analog leftover Day 1 / 2008 Worlds. "
    "Username citizenSwanky. LIGHT checked. Event Date 06/10/12 Event Name Nationals. "
    "Mind What You Have Learned / Save You It Can dested analog leftover McCune empty. "
    "Strong Is Vader True dested dest-as-written analog leftover Consoli Day 2. "
    "Battle Plan & Draw Their Fire dested analog leftover Consoli Day 2. "
    "Do, Or Do Not & Wise Advice True dested analog leftover Consoli Day 2. "
    "Sai'torr Kal Fas True dested analog leftover Virtual Block. "
    "Strikeforce dested Strike Force analog leftover Day 1. "
    "Imperial Atrocity crossed dested Artoo-Detoo In Red 5 True analog leftover McCune. "
    "Yoda dested Yoda, Senior Council Member analog leftover Day 1. "
    "Padme Naberrie dested Padmé Naberrie analog leftover. "
    "Threepio with His Parts Showing dested analog leftover. "
    "Woooo dested Wookiee Roar analog leftover Day 1. "
    "Were You Looking For Me dested Were You Looking For Me? analog leftover. "
    "We Gotta Grand Army dested Wesa Gotta Grand Army analog leftover Day 1 x3. "
    "Planetary Defenses dested analog leftover shield. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Tom Frafjord dested Tom Frafjord analog leftover Day 1 / 2008 Worlds. "
    "Username citizenSwanky. DARK checked. Event Date 06/10/12 Event Name Nationals. "
    "My Lord, Is That Legal? / I Will Make It dested analog leftover Kurten. "
    "Ni Chuba Na dested Ni Chuba Na?? True analog leftover Day 1. "
    "Accepting Trade Federation Control dested analog leftover Dalton. "
    "Our Blockade Is Perfectly Legal dested analog leftover Dalton. "
    "This Is Outrageous dested This Is Outrageous! analog leftover Dalton. "
    "Something Special dested Something Special Planned For Them analog leftover Day 1. "
    "The Phantom Menace crossed dested Black Door Controls analog leftover. "
    "Boba Fett Prepared Hunter dested Boba Fett, Renowned Bounty Hunter True analog leftover Hunter. "
    "The Mandalorian Father of Fett dested Jango Fett, The Assassin True analog leftover Day 1. "
    "Yeb Yeb Ademthorn dested Yeb Yeb Adem'thorn analog leftover Dalton. "
    "Toonbuck Toora dested analog leftover Dalton x2. "
    "Lott Dod dested analog leftover Dalton x3. "
    "Orn Free Taa dested analog leftover Dalton x2. "
    "Slave I, Symbol of Fear dested analog leftover. "
    "Short Range Fighters & Watch Your Back dested analog leftover Grouty x3. "
    "Squabbling Delegates dested analog leftover Stirling. "
    "Knowledge dested Knowledge And Defense True analog leftover Day 1 IN THE 60. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can"),
    n("Dagobah"),
    n("Strong Is Vader", True),
    n("It Is The Future You See"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice", True),
    n("Quick Draw"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Jungle"),
    n("Dagobah: Bog Clearing"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains", True),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Seeking An Audience"),
    n("Yoda's Hope", True),
    n("Hindsight"),
    n("Projection Of A Skywalker"),
    n("Projection Of A Skywalker", True),
    n("Strike Force"),
    n("The Way Of Things", True),
    n("Artoo-Detoo In Red 5", True),
    n("Imperial Atrocity"),
    n("Home One"),
    n("Luke's Backpack"),
    n("Luke's Lightsaber", True),
    n("Jedi Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Jedi Knight", True),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Daughter Of Skywalker", True),
    n("Yoda, Senior Council Member"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Padmé Naberrie", True),
    n("See-Threepio With His Parts Showing"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection", True),
    n("Rebel Leadership", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Wookiee Roar"),
    n("Out Of Commission & Transmission Terminated"),
    n("We're Doomed"),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=3),
    n("A Jedi's Resilience"),
    n("A Jedi's Resilience", True),
    n("Escape Pod", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Another Pathetic Lifeform"),
    n("Aim High", True),
    n("Chasm"),
    n("Don't Do That Again"),
    n("Let's Keep A Little Optimism Here"),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor"),
    n("Ultimatum", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It"),
    n("Coruscant: Galactic Senate"),
    n("Blockade Flagship: Bridge", True),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Combat Response", True),
    n("Kuat Drive Yards"),
    n("Naboo"),
    n("Kashyyyk"),
    n("Senate Hovercam"),
    n("Accepting Trade Federation Control"),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("This Is Outrageous!"),
    n("Imperial Decree", True),
    n("Something Special Planned For Them"),
    n("Black Door Controls"),
    n("The Phantom Menace"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Baron Soontir Fel"),
    n("Boba Fett, Renowned Bounty Hunter", True),
    n("Darth Vader", True),
    n("Dengar"),
    n("DS-61-2"),
    n("Jango Fett, The Assassin", True),
    n("Zuckuss"),
    n("Aks Moe"),
    n("Baskol Yeeleshim"),
    n("Edcel Bar Gane"),
    n("Lott Dod", qty=3),
    n("Orn Free Taa", qty=2),
    n("Tikkek"),
    n("Toonbuck Toora", qty=2),
    n("Yeb Yeb Adem'thorn", qty=2),
    n("Black 2", True),
    n("Mist Hunter", True),
    n("Punishing One", True),
    n("Saber 1"),
    n("Slave I, Symbol Of Fear", True),
    n("Vader's Personal Shuttle"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Fighters Coming In"),
    n("You Are Beaten"),
    n("Sneak Attack", True),
    n("Cold Feet"),
    n("Limited Resources"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Squabbling Delegates", qty=2),
    n("Squabbling Delegates", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare"),
    n("Oppressive Enforcement"),
    n("Resistance", True),
    n("Secret Plans"),
    n("There Is No Try", True),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
