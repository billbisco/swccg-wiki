#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Aaron Nelson.

Source: 2012mpcday2.pdf pages 1–2 (2010 form, 12 shields).
Name Aaron Nelson dested Aaron Nelson. Username Airdog 2003 dested Airdog2003.
p01 Light SoCal TRM. p02 Dark SoCal AOBS.
Do not dest as Jake Nelson. Do not rewrite 2013 leftovers.
Do not rewrite Day 1 leftover Watch Your Step / Kessel.
Pack player-stubs/Aaron_Nelson.wiki.
"""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "Airdog2003"
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2012 Match Play Championship Day 2 Aaron Nelson LS.png"
DS_SCAN = "2012 Match Play Championship Day 2 Aaron Nelson DS.png"
LS_DECK_NAME = "SoCal TRM"
DS_DECK_NAME = "SoCal AOBS"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson. "
    "Username Airdog 2003 dested Airdog2003. Event MPC Day 2. Deck Name SoCal TRM. LIGHT. "
    "Do not dest as Jake Nelson. Do not rewrite 2013 leftovers. "
    "Do not rewrite Day 1 leftover Watch Your Step. "
    "Yavin 4: Massassi Throne Room dested analog leftover TRM IN THE 60 AND START. "
    "NOOOOO etc True dested NOOOOOOOOOOOO! True analog leftover. "
    "Leia RP dested Leia, Rebel Princess analog leftover HT. "
    "Qui-Gon w/ stick crossed dested Hindsight analog leftover Wirfs. "
    "AJR dested A Jedi's Resilience analog leftover Wirfs. "
    "SATM & BP empty AND True kept separate analog leftover Shaw. "
    "Imp Atrocity True dested Imperial Atrocity True analog leftover. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover. "
    "Naboo: Boss Nas Chamber dested Naboo: Boss Nass' Chambers analog leftover HT. "
    "Luke Skywalker SITF True dested Luke Skywalker, Strong In The Force True analog leftover Wirfs. "
    "Antilles Man Combo True dested Antilles Maneuver & Rebel Reinforcements True analog leftover Wirfs. "
    "Leia True dested Leia True analog leftover Jourdan. "
    "Luke Skywalker JK dested Luke Skywalker, Jedi Knight analog leftover. "
    "Han Chewie & The Falcon dested Han, Chewie, And The Falcon analog leftover Wirfs. "
    "HCF crossed dested Tantive IV True analog leftover. "
    "Sai Tor Kal Fas True dested Sai'torr Kal Fas True analog leftover Wirfs. "
    "Imperial Atrocity crossed dested Honor Of The Jedi analog leftover HT. "
    "Line 60 cropped dested Anger, Fear, Aggression True analog leftover Wirfs IN THE 60. "
    "Shield 4 DDTA dested Don't Do That Again True analog leftover Anderson. "
    "Shield 9 LKALOH dested Let's Keep A Little Optimism Here True analog leftover Shaw. "
    "Shield 11–12 cropped dested Weapons Display analog leftover Wirfs and Do, Or Do Not analog leftover Murray. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson. "
    "Username Airdog 2003 dested Airdog2003. Event MPC Day 2. Deck Name SoCal AOBS. DARK. "
    "Do not dest as Jake Nelson. Do not rewrite 2013 leftovers. "
    "Do not rewrite Day 1 leftover Kessel. "
    "AOBS dested Agents Of Black Sun / Vengeance Of The Dark Prince analog leftover Foth IN THE 60 AND START. "
    "Coruscant (SE) dested Coruscant (Dark) analog leftover. "
    "Imperial City dested Coruscant: Imperial City analog leftover. "
    "Private Platform True dested Coruscant: Private Platform (Docking Bay) True analog leftover Foth. "
    "Spaceport DB dested Spaceport Docking Bay analog leftover Foth. "
    "Reejeedu True dested Reegesk True analog leftover Kelly. "
    "Tendry to My Design True dested as written. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover. "
    "Blast Door Controls crossed dested Blast Door Controls True analog leftover Foth. "
    "Dengar w/ Gun True dested Dengar With Blaster Carbine True analog leftover HT. "
    "Guri Escape True dested Guri True analog leftover unique overcount. "
    "Boba Fett BH dested Boba Fett, Bounty Hunter analog leftover Booker. "
    "Boba Fett (SE) True dested Boba Fett True analog leftover. "
    "Wal Hutta dested Nal Hutta analog leftover Tom. "
    "Breyus Glee True dested Brangus Glee True analog leftover. "
    "Tatooine Cantina dested Tatooine: Cantina analog leftover. "
    "Dr. E dested Dr. Evazan & Ponda Baba analog leftover HT. "
    "ZIMH dested Zuckuss In Mist Hunter analog leftover Foth. "
    "Jabba's Tent True dested as written. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover Hilbun. "
    "Prepared / Master Combo dested Prepared Defenses analog leftover Foth IN THE 60. "
    "Line 40 cropped dested We Must Accelerate Our Plans True analog leftover Foth. "
    "Line 60 cropped dested Knowledge And Defense analog leftover Murray IN THE 60. "
    "Shield AUG dested A Useless Gesture True analog leftover Eier. "
    "Shield YCHF dested You Cannot Hide Forever True analog leftover Foth. "
    "Shield CHYBC dested Come Here You Big Coward analog leftover Lepine. "
    "Shield TINT dested There Is No Try analog leftover Eier. "
    "Shield 11–12 cropped dested Do They Have A Code Clearance analog leftover Foth and Oppressive Enforcement analog leftover Foth. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Mace Windu", True),
    n("NOOOOOOOOOOOO!", True),
    n("Leia, Rebel Princess"),
    n("Houjix"),
    n("Lando Calrissian, Scoundrel"),
    n("Hindsight"),
    n("A Jedi's Resilience"),
    n("Admiral Ackbar", True),
    n("Obi-Wan With Lightsaber"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Speak With The Jedi Council"),
    n("Imperial Atrocity", True, qty=2),
    n("Ki-Adi-Mundi", True),
    n("Under Attack"),
    n("Escape Pod", True),
    n("Jedi Lightsaber", True),
    n("Mace Windu", True),
    n("Artoo-Detoo In Red 5"),
    n("Naboo: Boss Nass' Chambers"),
    n("Luke Skywalker, Strong In The Force", True),
    n("A Jedi's Plans", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Blaster Deflection"),
    n("Strikeforce", True),
    n("Under Attack"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Leia", True),
    n("Leia's Blaster Rifle"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Rebel Leadership", True),
    n("Kiffex"),
    n("Sense"),
    n("Home One: Docking Bay"),
    n("Wesa Gotta Grand Army"),
    n("Luke Skywalker, Jedi Knight"),
    n("Sorry About The Mess & Blaster Proficiency", True),
    n("Coruscant: Night Club", True),
    n("Sense"),
    n("Han, Chewie, And The Falcon"),
    n("Blaster Deflection"),
    n("A Jedi's Resilience"),
    n("Tantive IV", True),
    n("Rebel Leadership", True),
    n("Seeking An Audience", True),
    n("Home One: War Room"),
    n("Let The Wookiee Win", True),
    n("Sai'torr Kal Fas", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Corran Horn"),
    n("Scrambled Transmission", True),
    n("Honor Of The Jedi"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Insurrection & Aim High"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("A Tragedy Has Occurred", True),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Elis Helrot"),
    n("Voyeur", True),
    n("They're Still Coming Through!"),
    n("Coruscant: Private Platform (Docking Bay)", True),
    n("Spaceport Docking Bay"),
    n("Reegesk", True),
    n("Cold Feet", True),
    n("Tendry To My Design", True),
    n("Hidden Weapons"),
    n("We Must Accelerate Our Plans"),
    n("Blast Door Controls", True),
    n("Imperial Justice", True),
    n("Dengar With Blaster Carbine", True),
    n("Unexpected Interruption", True),
    n("Frozen Assets"),
    n("Ghhhk"),
    n("Dengar With Blaster Carbine", True),
    n("Guri", True, qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("Unexpected Interruption"),
    n("P-59"),
    n("Boba Fett", True),
    n("Jabba The Hutt", True),
    n("Gartogg", True),
    n("4-LOM With Concussion Rifle"),
    n("Ability, Ability, Ability"),
    n("The Emperor", True),
    n("Nal Hutta"),
    n("Cease Fire!"),
    n("Brangus Glee", True),
    n("4-LOM With Concussion Rifle"),
    n("Tatooine: Cantina"),
    n("Gardulla The Hutt", True),
    n("Hidden Weapons"),
    n("Ket Maliss", True),
    n("We Must Accelerate Our Plans", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Sense"),
    n("Vigo"),
    n("Blockade Flagship: Bridge"),
    n("Scum & Villainy"),
    n("Hidden Weapons"),
    n("Zuckuss In Mist Hunter"),
    n("Jabba's Tent", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("No Escape"),
    n("Jabba's Space Cruiser", True),
    n("Elis Helrot"),
    n("Cease Fire!"),
    n("Dismay"),
    n("Jabba's Tent", True),
    n("Broken Concentration", True),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven"),
    n("Prepared Defenses"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Resistance"),
    n("Battle Order", True),
    n("There Is No Try"),
    n("Do They Have A Code Clearance"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
