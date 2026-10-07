#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 2 typed printout: Paul Bonsall.

Source: 2014-TMW-Day-2.pdf pages 13–16 (type-grouped printout).
Handwritten header Paul Bonsall / Dark Bro / Texas Mini-Worlds Day 2.
Day 2 Changes applied (crossed dest replacement).
"""
from __future__ import annotations

PLAYER = "Paul Bonsall"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 15
DS_PAGE = 13
LS_SCAN = "2014 Texas Mini Worlds Day 2 p15 Paul Bonsall LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 2 p13 Paul Bonsall DS.png"
NOTE = "Typed printout (not a handwritten Xerox form). Day 2 Changes applied."
EXTRA_SCANS = [
    ("2014 Texas Mini Worlds Day 2 p14 Paul Bonsall DS.png", "Page 14 of [[:File:2014 Texas Mini Worlds Day 2.pdf]]."),
    ("2014 Texas Mini Worlds Day 2 p16 Paul Bonsall LS.png", "Page 16 of [[:File:2014 Texas Mini Worlds Day 2.pdf]]."),
]
LS_NOTE = (
    "Typed Light Hyperdrive printout plus handwritten Day 2 Changes. "
    "Name Paul Bonsall. Deck Name Dark Bro. "
    "The Hyperdrive Generator's Gone/We'll Need A New One dested "
    "The Hyperdrive Generator's Gone / We'll Need A New One. "
    "Mace Windu, Master of the order (AI) dested Mace Windu, Master Of The Order. "
    "Master Qui-Gon (V) (AI) dested Master Qui-Gon. "
    "Senator Leia Organa dested Senator Leia Organa. "
    "Dorme' dested Dorme. "
    "Maris Brood, Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Obi-Wan Kenobi, Padawan Learner dested Obi-Wan Kenobi, Padawan Learner. "
    "Captain Rex, 501st Legion dested Captain Rex, 501st Legion. "
    "A/D Combo → Under Attack already in the typed interrupt list. "
    "Advantage → Rebel Barrier already in the typed interrupt list. "
    "Inconsequential Barriers dested Sabotage (V). "
    "Do Or Do Not crossed, Affect Mind dested Affect Mind. "
    "Qui-Gon Jinn's Lightsaber (AI) dested Qui-Gon Jinn's Lightsaber. "
    "Yoda Stew & You Do Have Your Moments dested Yoda Stew & You Do Have Your Moments. "
    "Armed And Dangerous & Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "Unique overcounts sheet-accurate (Master Qui-Gon x2, Obi-Wan Kenobi, Padawan Learner x2, "
    "Clash Of Sabers x2, A Jedi's Resilience x2, Into The Garbage Chute, Flyboy x2, "
    "Wesa Gotta Grand Army x2, Sorry About The Mess & Blaster Proficiency x2, "
    "Blaster Deflection x2). "
    "(V) from the typed (V) mark."
)
DS_NOTE = (
    "Typed Dark Kessel CR(V) printout plus handwritten substitutions. "
    "Name Paul Bonsall. Deck Name Dark Bro. "
    "Kessel CR(V) starting location dested Kessel. "
    "4-LOM With Concussion Rifle (V) handwritten added. "
    "Arica handwritten beside Mara Jade With Lightsaber dested as a persona note; "
    "Mara Jade With Lightsaber dested as printed. "
    "Darth Vader, Dark Lord Of The Sith (x2) crossed, Darth Vader, Betrayer Of The Jedi dested. "
    "Imperial Detention crossed, Do They Have A Code Clearance? dested. "
    "I Find Your Lack Of Faith Disturbing crossed, We'll Let Fate-a Decide, Huh? dested. "
    "No Escape crossed, A Sith's Weapon dested. "
    "Where Are You Taking This ... Thing? crossed, Wipe Them Out, All Of Them dested. "
    "Alter (Coruscant) (V) Premiere note dested Alter (Coruscant). "
    "Blaster Rifle handwritten at the footer dested Blaster Rifle as the 60th main card. "
    "NO_DEST remaining: none after Blaster Rifle / Ni Chuba Na? dests. "
    "Moruth Doole, Kessel Administrator dested Moruth Doole, Kessel Administrator. "
    "Kir Kanos With Force Pike dested Kir Kanos With Force Pike. "
    "Kessel: Spice Mines - Administrator's Office dested Kessel: Spice Mines - Administrator's Office. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Unique overcounts sheet-accurate (Count Dooku x2, Emperor Palpatine x2, "
    "Galen Marek, Starkiller x2, Masterful Move & Endor Occupation x2, "
    "Sonic Bombardment x2, Short Range Fighters & Watch Your Back! x2, "
    "Force Lightning x2, Force Field x2). "
    "(V) from the typed (V) mark / handwritten checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Aayla Secura"),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True),
    n("Senator Leia Organa"),
    n("Dorme"),
    n("Maris Brood, Fallen Jedi"),
    n("Ki-Adi-Mundi", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Captain Rex, 501st Legion"),
    n("Credits Will Do Fine"),
    n("A Remote Planet", True),
    n("Quick Draw", True),
    n("Disarmed"),
    n("Sai'torr Kal Fas", True),
    n("Lightsaber Proficiency"),
    n("Rycar Ryjerd", True),
    n("Scrambled Transmission", True),
    n("Temporary Foothold"),
    n("Meditation"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
    n("Clash Of Sabers", qty=2),
    n("Houjix"),
    n("A Jedi's Resilience", qty=2),
    n("Under Attack"),
    n("Sense"),
    n("Sabotage", True),
    n("Dark Approach", True),
    n("Desperate Reach", True),
    n("Rebel Barrier"),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Blaster Deflection", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Heading For The Medical Frigate", True),
    n("Let The Wookiee Win", True),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Watto's Junkyard"),
    n("Naboo: Boss Nass' Chambers"),
    n("Tatooine"),
    n("Alderaan Consular Ship"),
    n("Guardian's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("4-LOM With Concussion Rifle", True),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Garindan", True),
    n("Moruth Doole, Kessel Administrator"),
    n("Mara Jade With Lightsaber"),
    n("Count Dooku", qty=2),
    n("Emperor Palpatine", qty=2),
    n("P-59"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Kir Kanos With Force Pike"),
    n("Galen Marek, Starkiller", qty=2),
    n("Darth Maul"),
    n("Kessel Surveillance System"),
    n("Imperial Justice", True),
    n("Blast Door Controls"),
    n("Blaster Rack", True),
    n("Gift Of The Master"),
    n("I'll Take Them Myself"),
    n("Ni Chuba Na?", True),
    n("A Sith's Weapon"),
    n("Revenge Of The Sith"),
    n("Wipe Them Out, All Of Them", True),
    n("Knowledge And Defense", True),
    n("Ghhhk"),
    n("Force Push", True),
    n("Sniper & Dark Strike"),
    n("Combat Readiness", True),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Cold Feet", True),
    n("Sith Fury & End This Destructive Conflict"),
    n("Sonic Bombardment", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Monnok"),
    n("Force Lightning", qty=2),
    n("Force Field", True, qty=2),
    n("Alter (Coruscant)", True),
    n("Blaster Rifle"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Prison"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Cloud City: Security Tower", True),
    n("Spice Mine Operations"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Blizzard 4"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dooku's Lightsaber"),
    n("Vader's Lightsaber"),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Death Star Sentry", True),
]
DS_ADD = []
