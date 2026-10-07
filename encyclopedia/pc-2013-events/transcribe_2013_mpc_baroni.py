#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Steve Baroni Xerox LS+DS (champion)."""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2013 Match Play Championship p11 Steve Baroni LS.png"
DS_SCAN = "2013 Match Play Championship p12 Steve Baroni DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni; dested Steve Baroni. "
    "Light. TIGH → There Is Good In Him. Obi two LS / EPP Obi → Obi-Wan With Lightsaber. "
    "DTOM → Don't Tread On Me. HFTMF → Heading For The Medical Frigate. "
    "LTWW → Let The Wookiee Win (five copies as written, lines 8–10 and 35–36). "
    "Jedi Resilience → A Jedi's Resilience. RL → Rebel Leadership. "
    "Wesa Gotta Grand → Wesa Gotta Grand Army. Line 23 A Jedi Catch dested A Jedi's Focus. "
    "SATM+BP → Sorry About The Mess & Blaster Proficiency. Speak With Jedi Coun → Speak With The Jedi Council. "
    "Mace Master of the Order → Mace Windu, Master Of The Order. Luke SK → Luke Skywalker, Jedi Knight. "
    "Qui-Gon Lightsaber → Qui-Gon Jinn With Lightsaber. Han Chewie Falcon → Han, Chewie, And The Falcon. "
    "Lando Scoundrel → Lando Calrissian, Scoundrel. Luke RS → Luke Skywalker, Rebel Scout. "
    "Yoda MSTR Jedi dested Yoda, Master Of The Force. Jedi CC → Coruscant: Jedi Council Chamber. "
    "Echo DB → Hoth: Echo Docking Bay. Hm One War Rm → Home One: War Room. "
    "Boss Nass Chambers → Naboo: Boss Nass' Chambers. Battle Plains → Naboo: Battle Plains. "
    "AFA → Anger, Fear, Aggression. Insight → Your Insight Serves You Well. "
    "Keep a Little Op → Let's Keep A Little Optimism Here. "
    "He Can Go About Bus → He Can Go About His Business. Simple tricks → Simple Tricks And Nonsense. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni; dested Steve Baroni. Dark. "
    "HDV → Hunt Down And Destroy The Jedi. A Sith's Legacy dested A Sith's Plans. "
    "Galen Starkiller → Galen Marek, Starkiller. DuDlots dested Droideka. "
    "Dark Jedi Betrayer → Darth Vader, Betrayer Of The Jedi. Boba Fett BH → Boba Fett, Bounty Hunter. "
    "Danger with Blaster dested Dengar With Blaster Carbine. Black Leader → Juno Eclipse, Black Leader. "
    "Convindra dested Count Dooku. EPP Maul → Darth Maul With Lightsaber. "
    "Geln Arm V → General Veers (V). 4LM → 4-LOM With Concussion Rifle. "
    "DrE Ponda → Dr. Evazan & Ponda Baba. Galen's Fighter dested Rogue Shadow. "
    "Victory dested Victory (virtual Effect). Vader Saber Vader dested Darth Vader's Lightsaber. "
    "3rd Marker → Hoth: Defensive Perimeter (3rd Marker). POFF → Coruscant: Palpatine's Quarters. "
    "Coruscant SE dested Coruscant: Imperial City. M'Lord dested My Lord, Is That Legal? / I Will Make It Legal. "
    "Prep Defense → Prepared Defenses. Our Beautiful Home dested One Beautiful Thing. "
    "Emperor's Power. We Must Accelerate dested We Must Accelerate Our Plans. "
    "Weapon Lev / Empire's Back → Weapon Levitation & The Empire's Back. "
    "MM+EO → Masterful Move & Endor Occupation. Where are you taking this → Where Are You Taking This ... Thing?. "
    "Lightsaber Deflection dested Lightsaber Parry. Beware Of The Sith dested No Match For A Sith. "
    "A Sith's Pleasure dested A Sith's Weapon. A SM dested A Stunning Move. "
    "YD dested Your Destiny. Useless Gesture → A Useless Gesture. "
    "Line 6 Powered dested Come Here You Big Coward. Fire Power → Firepower. "
    "Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Obi-Wan With Lightsaber"),
    n("Don't Tread On Me", True),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("Heading For The Medical Frigate"),
    n("Projection Of A Skywalker"),
    n("Let The Wookiee Win", True, qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Sense", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Blaster Deflection"),
    n("A Jedi's Focus"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Weapon Levitation"),
    n("Draw Their Fire"),
    n("Imperial Atrocity", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Speak With The Jedi Council"),
    n("Scrambled Transmission", True),
    n("Houjix"),
    n("Imperial Atrocity", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Master Qui-Gon", True, qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Jedi Lightsaber", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("Yoda, Master Of The Force"),
    n("Luke's Lightsaber"),
    n("Endor: Chief Chirpa's Hut"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hoth: Echo Docking Bay"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One"),
    n("Naboo: Battle Plains"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("The Professor", True),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here", True),
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("Aim High", True),
    n("Battle Plan", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("A Sith's Plans", True),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Droideka", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Emperor Palpatine", qty=2),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Grand Admiral Thrawn"),
    n("Juno Eclipse, Black Leader", True),
    n("Count Dooku", True),
    n("Darth Maul With Lightsaber", True),
    n("General Veers", True),
    n("P-59"),
    n("4-LOM With Concussion Rifle", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Blizzard 4", qty=2),
    n("Rogue Shadow", True),
    n("Victory", True),
    n("Vader's Lightsaber"),
    n("Darth Vader's Lightsaber", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Blockade Flagship: Bridge"),
    n("Executor"),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("Coruscant: Palpatine's Quarters"),
    n("Endor Shield", True),
    n("Blaster Rack", True),
    n("My Lord, Is That Legal? / I Will Make It Legal", True),
    n("Gift Of The Master", True),
    n("Prepared Defenses", True),
    n("One Beautiful Thing", True),
    n("No Escape"),
    n("Emperor's Power", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Lightsaber Parry", True),
    n("Protocol Failure", True),
    n("Superlaser Mark II"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Imperial Reinforcements", True),
    n("Force Push", True),
    n("Force Lightning"),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Imperial Justice", True),
    n("Force Field", True),
    n("Ghhhk"),
    n("Where Are You Taking This ... Thing?", True),
    n("No Match For A Sith", True),
    n("A Sith's Weapon", True),
    n("A Stunning Move", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Your Destiny", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Allegiance", True),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Fanfare", True),
]
DS_ADD = []
