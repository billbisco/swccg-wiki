#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Chris Westergard.

Source: MPC-2014-Day-1-Main-Event.pdf pages 120–121 (2013 form, 15 shields).
Name blank; Deck Name Chris Westergard both sides dested Chris Westergard.
"""
from __future__ import annotations

PLAYER = "Chris Westergard"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 120
DS_PAGE = 121
LS_SCAN = "2014 Match Play Championship Day 1 Chris Westergard LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Chris Westergard DS.png"
LS_DECK_NAME = "Chris Westergard"
DS_DECK_NAME = "Chris Westergard"
NOTE = "Handwritten 2013 Xerox form. Name blank; Deck Name Chris Westergard."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name blank. Deck Name Chris Westergard dested Chris Westergard. "
    "LIGHT/DARK empty; Light 60. The Hyperdrive Generator's Gone starting. "
    "Lando's Luxury Yacht dested Lady Luck. Lando Calrissian, Unlikely Hero dested "
    "Lando Calrissian, Unlikely Hero. SATM dested Sorry About The Mess. SATM / Blaster Prof dested "
    "Sorry About The Mess & Blaster Proficiency. Out of Commission / TT dested "
    "Out Of Commission & Transmission Terminated. Unique overcounts sheet-accurate "
    "(Alderaan Consular Ship x2, Lady Luck x2, Fallen Jedi (V) x2, Lando Calrissian, Unlikely Hero (V) x2, "
    "Master Qui-Gon (V) x2, Mace Windu (V) x2, Imperial Atrocity (V) x2, Into The Garbage Chute, Flyboy! (V) x2, "
    "Sorry About The Mess x2 plus combo, Rebel Barrier x2). NO_DEST The Hyperdrive Generator's Gone; Fallen Jedi (V). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name blank. Deck Name Chris Westergard dested Chris Westergard. "
    "DARK 60. Death Star: Conference Room (V) starting location. There Is No Try / Oppressive Enforcement dested "
    "There Is No Try / Oppressive Enforcement. Mara Jade, TEH dested Mara Jade, The Emperor's Hand. "
    "Darth Vader, BOTS dested Darth Vader, Betrayer Of The Jedi. Unique overcounts sheet-accurate "
    "(Darth Vader, Betrayer Of The Jedi (V) x2, Emperor Palpatine x2, Imperial Dominion (V) x2, "
    "Trophy Of A Kill (V) x2, Dark Collaboration (V) x3, Imperial Command x2, None Shall Pass (V) x2). "
    "NO_DEST I'll Take It Personally. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone"),
    n("Tatooine: Watto's Junkyard", True),
    n("Tatooine: City Outskirts", True),
    n("Credits Will Do Fine"),
    n("Heading For The Medical Frigate", True),
    n("A Remote Planet", True),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Tatooine"),
    n("Coruscant: Jedi Council Chamber"),
    n("Alderaan Consular Ship", qty=2),
    n("Lady Luck", qty=2),
    n("Elegant Lightsaber", True),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Journal"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Fallen Jedi", True, qty=2),
    n("Ki-Adi-Mundi", True),
    n("Lando Calrissian, Unlikely Hero", True, qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Mace Windu", True),
    n("Senator Leia Organa", True),
    n("Senator Padme Amidala", True),
    n("Tawss Khaa", True),
    n("Flash Of Insight", True),
    n("Imperial Atrocity", True, qty=2),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Strike Planning", True),
    n("Temporary Foothold", True),
    n("Alter", True),
    n("Blaster Deflection"),
    n("Clash Of Sabers"),
    n("Escape Pod", True),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("Inconsequential Barriers"),
    n("Into The Garbage Chute, Flyboy!", True, qty=2),
    n("It Could Be Worse"),
    n("Jedi Levitation", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Rebel Barrier"),
    n("Sense"),
    n("Sorry About The Mess"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Smoke Screen"),
    n("Rebel Barrier"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here"),
    n("Your Insight Serves You Well"),
    n("Ultimatum"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Only Jedi Carry That Weapon"),
    n("Wise Advice"),
    n("Yavin Sentry"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("Ultimatum"),
    n("The Professor"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
]
LS_ADD = []


DS_START = "Death Star: Conference Room"
DS_CARDS = [
    n("Death Star: Conference Room", True),
    n("Prepared Defenses", True),
    n("The Inner Circle", True),
    n("There Is No Try / Oppressive Enforcement", True),
    n("Ability, Ability, Ability"),
    n("Endor Shield", True),
    n("Sim Aloo", True),
    n("Arica", True),
    n("Mara Jade, The Emperor's Hand", True),
    n("Admiral Ozzel"),
    n("Admiral Piett", True),
    n("Captain Bewil", True),
    n("Colonel Wullf Yularen", True),
    n("Darth Vader, Betrayer Of The Jedi", True, qty=2),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Emperor Palpatine", qty=2),
    n("Grand Moff Tarkin", True),
    n("General Veers", True),
    n("General Nevar", True),
    n("ISB Sector Commander", True),
    n("Janus Greejatus"),
    n("Kir Kanos With Force Pike", True),
    n("Myn Kyneugh", True),
    n("Kessel"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Empire's New Order", True),
    n("Imperial Decree", True),
    n("Imperial Decree"),
    n("Imperial Propaganda", True),
    n("No Escape"),
    n("I'll Take It Personally"),
    n("Revenge Of The Sith", True),
    n("Something Special Planned For Them", True),
    n("Visage Of The Emperor", qty=2),
    n("Justifier", True),
    n("Blizzard 2"),
    n("Mara Jade's Lightsaber", True),
    n("Trophy Of A Kill", True, qty=2),
    n("Dark Collaboration", True, qty=3),
    n("Force Lightning"),
    n("Imperial Tyranny"),
    n("I Have You Now"),
    n("Imperial Command", qty=2),
    n("Masterful Move"),
    n("None Shall Pass", True, qty=2),
    n("Outflank", True),
    n("Sith Fury", True),
    n("Twi'lek Advisor"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Weapon Of A Sith"),
    n("Wipe Them Out, All Of Them"),
    n("You Cannot Hide Forever"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("A Useless Gesture"),
    n("Secret Plans"),
    n("Firepower"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
