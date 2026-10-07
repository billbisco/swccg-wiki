#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Josh Mack.

Source: Nationals-2014-day-1.pdf pages 5–6 (2010 form).
Name MACK / Mack. Username Renmaker. Dest Josh Mack.
Japanese Holotable titles dest English.
"""
from __future__ import annotations

PLAYER = "Josh Mack"
USERNAME = "Renmaker"
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2014 US Nationals Day 1 p05 Josh Mack LS.png"
DS_SCAN = "2014 US Nationals Day 1 p06 Josh Mack DS.png"
NOTE = "Handwritten 2010 Xerox. Name MACK; username Renmaker dested Josh Mack."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name MACK. Username Renmaker. LIGHT Watch Your Step. "
    "LSTV Not v dested Luke Skywalker, Jedi Knight (LSJK; checkbox checked, Not v written). "
    "Yoda, GW dested Yoda, Great Warrior. Mace, Moto dested Mace Windu, Master Of The Order. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Luke, Rebel Princess dested Leia, Rebel Princess. All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "Japanese Chewie dested Chewbacca, Walking Carpet. Japanese Corran dested Corran Horn. "
    "Antilles Maneuver Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. Japanese Consular Ship dested Alderaan Consular Ship. "
    "Obi-Wan in Red 7 dested Obi-Wan In Red 7. Houjix Combo dested Houjix & Out Of Nowhere. "
    "Japanese Tantive IV dested Tantive IV. Lando's Luxury Yacht dested Lady Luck. "
    "Japanese Chewie dested Chewie Of Kashyyyk. Japanese Artoo dested Artoo-Detoo In Red 5. "
    "Flash of Insight crossed, Sense dested Sense. AFA dested Anger, Fear, Aggression. "
    "Unique overcounts sheet-accurate (Luke Skywalker, Jedi Knight x2, Wedge Antilles, Red Squadron Leader x2, "
    "Dash Rendar x2, Leia, Rebel Princess x2, No Questions Asked x3, All Wings Report In & Darklighter Spin x2, "
    "Corran Horn x2, Antilles Maneuver x2). (V) from checkbox except LSTV Not v. "
    "NO_DEST (2014 index): Fallen Jedi; Obi-Wan In Red 7 (V)."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Mack. Username Renmaker. DARK Wookiee Slaving Operation. "
    "Japanese Kashyyyk dested Kashyyyk. Slave I, SOF dested Slave I, Symbol Of Fear. "
    "Japanese Ghhhk dested Ghhhk. Japanese Monnok dested Monnok. "
    "Japanese That's How dested That's How We're Gonna Win. "
    "Short Range Fighters & Watch Your Back! dested Short Range Fighters & Watch Your Back!. "
    "Japanese Battle Order dested Battle Order & First Strike. "
    "The Mandalorian FOF dested Jango Fett, The Assassin. Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine. "
    "Japanese Ponda Baba dested Ponda Baba. P-59 dested P-59. K+D dested Knowledge And Defense. "
    "Japanese additional dested Death Star Sentry. Unique overcounts sheet-accurate "
    "(Jabba's Sail Barge: Passenger Deck x2, Scum & Villainy x2, Cease Fire! x2, "
    "Sonic Bombardment x3, Dengar With Blaster Carbine x2, Outer Rim Scout x4). (V) from checkbox. "
    "Sonic Beam dested Sonic Bombardment. "
    "NO_DEST (2014 index): That's How We're Gonna Win (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Yoda, Great Warrior"),
    n("Fallen Jedi"),
    n("Mace Windu, Master Of The Order"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Dash Rendar", True),
    n("Dash Rendar"),
    n("Leia, Rebel Princess", qty=2),
    n("No Questions Asked", True, qty=3),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Let The Wookiee Win", True),
    n("Chewbacca, Walking Carpet", True),
    n("Corran Horn", qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Imperial Atrocity", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Corellian Retort", True),
    n("Mirax Terrik"),
    n("Palejo Reshad"),
    n("Punch It!"),
    n("Sergeant Bruckman"),
    n("Alderaan Consular Ship", True),
    n("Obi-Wan In Red 7", True),
    n("Houjix & Out Of Nowhere"),
    n("General Crix Madine"),
    n("Tantive IV", True),
    n("Seeking An Audience", True),
    n("Home One: Docking Bay"),
    n("Sense", True),
    n("Leia's Blaster Rifle"),
    n("Lady Luck"),
    n("Corran Horn"),
    n("Chewbacca Of Kashyyyk", True),
    n("Artoo-Detoo In Red 5"),
    n("Padme Naberrie", True),
    n("Desperate Reach", True),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Scoundrels Guild"),
    n("Jaina Solo"),
    n("Evacuation Control", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
    n("There Is Another"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("The Professor"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Mercenary Slavers"),
    n("Jabba's Haven"),
    n("Power Of The Hutt"),
    n("Nal Hutta"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Jabba's Sail Barge: Passenger Deck", True),
    n("Maul's Sith Infiltrator"),
    n("Jabba's Space Cruiser", True),
    n("Slave I, Symbol Of Fear"),
    n("Scum And Villainy", qty=2),
    n("Hutt Bounty", True),
    n("Imperial Propaganda", True),
    n("Something Special Planned For Them", True),
    n("Protocol Failure"),
    n("Masterful Move & Endor Occupation"),
    n("Sneak Attack", True),
    n("Ghhhk"),
    n("Monnok"),
    n("That's How We're Gonna Win", True),
    n("Cease Fire!", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sonic Bombardment", True),
    n("Sonic Bombardment", qty=2),
    n("Abyssin Ornament"),
    n("Defensive Fire & Hutt Smooch"),
    n("Battle Order & First Strike", True),
    n("Ket Maliss, Shadow Killer"),
    n("Mara Jade With Lightsaber"),
    n("Bossk", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Dengar With Blaster Carbine", True, qty=2),
    n("Prince Xizor"),
    n("Mercenary Pilot"),
    n("Jabba The Hutt", True),
    n("Outer Rim Scout", qty=4),
    n("Ephant Mon"),
    n("Velken Tezeri", True),
    n("Ponda Baba", True),
    n("Garindan", True),
    n("OOM-9", True),
    n("Probe Droid"),
    n("P-59"),
    n("P-60"),
    n("4-LOM With Concussion Rifle"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
]
DS_ADD = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing"),
]
