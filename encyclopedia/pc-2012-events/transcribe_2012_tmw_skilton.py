#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Steve Skilton.

Source: 2012TMWDay1.pdf pages 26–27 (2009 Print Form). Name Steve Skilton dested
Steve Skilton analog leftover 2013 TMW / 2012 MPC / 2013 Worlds / pages/Steve_Skilton.wiki.
Username blank analog leftover 2013 TMW. p26 Light T.M. LTWW. p27 Dark HD(V).
Do not dest as a new person. Do not dest 2013 TMW / 2012 MPC / 2013 Worlds /
2014 TMW / 2014 MPC Skilton 60s again.
"""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 26
DS_PAGE = 27
LS_SCAN = "2012 Texas Mini Worlds Day 1 Steve Skilton LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Steve Skilton DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "2009 Print Form p26 Light / p27 Dark. "
    "Name Steve Skilton dested Steve Skilton analog leftover 2013 TMW. "
    "Username blank analog leftover 2013 TMW. Do not dest as a new person. "
    "Do not dest 2013 TMW / 2012 MPC / 2013 Worlds / 2014 TMW / 2014 MPC Skilton 60s again."
)
LS_NOTE = (
    "2009 Print Form p26 Light Deck Name T.M. LTWW. LIGHT checked. Event Date 04/28/12 Event TMW. "
    "Name Steve Skilton dested Steve Skilton analog leftover 2013 TMW. Username blank. "
    "Left extra 37–40 dest all written lines unique 60. Right printed 41–60. "
    "Throne Room dested Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "Rebel Cell - Hidden Ldg Site dested Rebel Cell - Hidden Landing Site analog leftover Jellison. "
    "LTWW dested Let The Wookiee Win analog leftover. "
    "Sai'torr Kal Fas dested analog leftover True. "
    "Strike Force dested analog leftover Hendon. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency analog leftover. "
    "Hear Me Baby (one more time) dested Hear Me Baby, Hold Together analog leftover. "
    "The Force Is Strong w/ 1 dested The Force Is Strong With This One analog leftover. "
    "Were You Looking For 3-PO? dested Were You Looking For Me? analog leftover. "
    "Nooooooooo dested NOOOOOOOOOOOO! analog leftover Heine. "
    "Luke SITF dested Luke Skywalker, Strong In The Force analog leftover. "
    "Master Qui-Gon dested analog leftover Massung. "
    "Leia, RP dested Leia, Rebel Princess analog leftover 2013 TMW Skilton. "
    "EPP Obi-Wan dested Obi-Wan With Lightsaber analog leftover 2013 TMW Skilton. "
    "Screaming Lando dested Lando Calrissian, Scoundrel analog leftover 2013 TMW Skilton. "
    "Luke Skywalker, JK dested Luke Skywalker, Jedi Knight analog leftover. "
    "3-PO w/HPS dested Threepio With His Parts Showing analog leftover. "
    "Qui-Gon's Tut Saber dested Qui-Gon Jinn's Lightsaber analog leftover. "
    "Artoo in R5 dested Artoo-Detoo In Red 5 analog leftover Hendon. "
    "HCF dested Han, Chewie, And The Falcon analog leftover. "
    "JCC dested Coruscant: Jedi Council Chamber analog leftover. "
    "Hoth WR dested Hoth: War Room analog leftover. "
    "Home 1 WR dested Home One: War Room analog leftover. "
    "Battle Plains dested Naboo: Battle Plains analog leftover. "
    "Naboo- Boss Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover. "
    "YISYW dested Your Insight Serves You Well analog leftover. "
    "Battle Plan (Lisa Needs Braces) dested Battle Plan analog leftover. "
    "Another Pathetic Lifeform dested analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "2009 Print Form p27 Dark Deck Name HD(V). DARK checked. Event Date 04/28/12 Event TMW. "
    "Name Steve Skilton dested Steve Skilton analog leftover 2013 TMW. Username blank. "
    "Line 1 printed OBJECTIVE (V) checked dested Hunt Down And Destroy The Jedi analog leftover Deck Name HD(V). "
    "Left extra 37–40 dest all written lines unique 60. Right printed 41–60. "
    "Coruscant (Don't Lose A Force!) dested Coruscant analog leftover. "
    "Imperial City dested Coruscant: Imperial City analog leftover. "
    "A Sith's Plans dested analog leftover Alperstein. "
    "A Sith's Weapon dested Weapon Of A Sith analog leftover 2013 TMW Herold. "
    "Ability x3 dested Ability, Ability, Ability analog leftover. "
    "Ni Chuba Na?? dested analog leftover. "
    "I've Lost Artoo! dested analog leftover. "
    "Revenge of the Sith dested analog leftover. "
    "Search + Destroy dested Search And Destroy analog leftover. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover. "
    "Weapon Lev + Emp Back dested Weapon Levitation & The Empire's Back analog leftover Nathan. "
    "Elis Herlot dested Elis Helrot analog leftover. "
    "Masterful Move + Endor Occ dested Masterful Move & Endor Occupation analog leftover. "
    "D. Vader, Betrayer dested Darth Vader, Betrayer Of Jedi analog leftover. "
    "DUDLOTS dested Darth Vader, Dark Lord Of The Sith analog leftover. "
    "Cyborg Comm. dested Grievous, Hunter Of Jedi analog leftover Hendon. "
    "Kir Kanos w/ Force Pike dested Kir Kanos With Force Pike analog leftover. "
    "EPP Mara dested Mara Jade With Lightsaber analog leftover. "
    "Dr E + Ponda B dested Dr. Evazan & Ponda Baba analog leftover. "
    "EPP 4-LOM dested 4-LOM With Concussion Rifle analog leftover Erwin. "
    "Galen's Saber, VG dested Galen's Lightsaber, Vader's Gift analog leftover. "
    "Cyborg's Sabers dested Grievous' Lightsabers analog leftover Hendon. "
    "DS WR dested Death Star: War Room analog leftover. "
    "Generator Core dested Naboo: Theed Palace Generator Core analog leftover. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge analog leftover. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover Anderson IN THE 60. "
    "I find Your Lack of something dested I Find Your Lack Of Faith Disturbing analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Let The Wookiee Win"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Rebel Cell - Hidden Landing Site"),
    n("Quick Draw", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Hindsight", True),
    n("Seeking An Audience", True),
    n("Strike Force", True),
    n("Civil Disorder", True),
    n("Scrambled Transmission", True),
    n("Draw Their Fire"),
    n("A Jedi's Resilience", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("The Force Is Strong With This One"),
    n("Sense"),
    n("Under Attack"),
    n("Skywalkers"),
    n("Were You Looking For Me?"),
    n("NOOOOOOOOOOOO!", True),
    n("Speak With The Jedi Council"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Princess Leia", True),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Admiral Salish-Bar", True),
    n("Obi-Wan With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Luke Skywalker, Jedi Knight"),
    n("Threepio With His Parts Showing"),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Tantive IV", True),
    n("Kiffex"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hoth: War Room"),
    n("Home One: War Room"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Another Pathetic Lifeform", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Wise Advice"),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("I've Lost Artoo!", True),
    n("Ability, Ability, Ability", True),
    n("No Escape"),
    n("Weapon Of A Sith"),
    n("First Strike"),
    n("Blaster Rack", True),
    n("Emperor's Power", True),
    n("Revenge Of The Sith", True, qty=2),
    n("Presence Of The Force"),
    n("Blast Door Controls"),
    n("Search And Destroy"),
    n("Program Trap", True),
    n("Force Field", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Weapon Levitation & The Empire's Back", qty=2),
    n("Elis Helrot"),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("Comscan Detection", True),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Emperor Palpatine", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Kir Kanos With Force Pike"),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("P-59"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Toak", qty=2),
    n("Restraining Belt"),
    n("Death Star: War Room"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
