#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Peter Huderich (peterich).

Source: 2014-Alderaan-Regionals.pdf pages 7–8 (2010 form).
"""
from __future__ import annotations

PLAYER = "Peter Huderich"
USERNAME = "peterich"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2014 Alderaan Regionals p07 Peter Huderich LS.png"
DS_SCAN = "2014 Alderaan Regionals p08 Peter Huderich DS.png"
NOTE = "Handwritten Xerox form."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate", True),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye", True),
    n("All My Urchins & Cloud City Celebration", True),
    n("Cloud City: West Gallery"),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: North Corridor"),
    n("Overseer", True),
    n("Insurrection", True),
    n("Outrider"),
    n("Lady Luck", True),
    n("Booster In Pulsar Skate", True),
    n("Foul Moudama", True),
    n("Kebyc", True),
    n("Yoxgit"),
    n("Tanus Spijek", True),
    n("Aayla Secura", True),
    n("Nien Nunb, Sullustan Smuggler", True),
    n("Dash Rendar", True),
    n("Leia, Rebel Princess"),
    n("Luke With Lightsaber"),
    n("Kal'Falnl C'ndros", True),
    n("BoShek, Brash Smuggler", True),
    n("Uutik", True),
    n("Sergeant Edian", True),
    n("Caldera Righim"),
    n("Lobot", True),
    n("Leslomy Tecema", True),
    n("Pucumir Thryss", True),
    n("Mirax Terrik"),
    n("Trooper Utris M'Toc", True),
    n("Harc Seff", True),
    n("Han Solo, Innocent Scoundrel", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Chewbacca, Walking Carpet", True),
    n("Projection Of A Skywalker"),
    n("Hiding In The Garbage", True),
    n("Menace Fades"),
    n("Ellors Madak", True),
    n("Dark Approach", True),
    n("It's A Trap!", qty=2),
    n("Alter"),
    n("Blast The Door, Kid!"),
    n("Desperate Reach", True),
    n("Escape Pod", True),
    n("Grimtaash"),
    n("Rebel Barrier", qty=2),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Choke", qty=2),
    n("Path Of Least Resistance"),
    n("Path Of Least Resistance & Revealed"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Jabba's Prize", True),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("The Professor", True),
]
LS_ADD = [
    n("Affect Mind", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
]


DS_START = "Court Of The Vile Gangster / I Shall Enjoy Watching You Die"
DS_CARDS = [
    n("Court Of The Vile Gangster / I Shall Enjoy Watching You Die"),
    n("Knowledge And Defense", True),
    n("Power Of The Hutt"),
    n("Jabba's Haven", True),
    n("Jabba's Palace: Dungeon"),
    n("Tatooine: Great Pit Of Carkoon"),
    n("Jabba's Palace: Audience Chamber"),
    n("Sarlacc", True),
    n("Prince Xizor"),
    n("Bib Fortuna", True),
    n("Velken Tezeri", True),
    n("Gela Yeens", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Ket Maliss, Shadow Killer", True),
    n("Thok & Thug", True),
    n("Reegesk", True),
    n("Jango Fett, The Assassin", True),
    n("IG-88 With Riot Gun"),
    n("Boelo"),
    n("Jodo Kast", True),
    n("Dune Walker", True),
    n("Jabba The Hutt", True),
    n("Ephant Mon"),
    n("Bane Malar, Spice Addict", True),
    n("Giran", True),
    n("Probot", True),
    n("Arica", True),
    n("4-LOM With Concussion Rifle"),
    n("Nal Hutta"),
    n("Coruscant: Docking Bay"),
    n("Coruscant: Private Platform", True),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Jabba's Sail Barge", True),
    n("Jabba's Space Cruiser", True),
    n("Slave I, Symbol Of Fear", True),
    n("Broken Concentration", True),
    n("Dengar In Punishing One"),
    n("Zuckuss In Mist Hunter"),
    n("Elis Helrot", True),
    n("First Strike"),
    n("Hutt Influence"),
    n("Hutt Bounty", True),
    n("Protocol Failure"),
    n("Scum And Villainy"),
    n("Desilijic Tattoo", True),
    n("Twi'lek Advisor", True),
    n("Abyssin Ornament & Wounded Wookiee", True),
    n("Masterful Move"),
    n("Mynock"),
    n("Lightsaber Deficiency", True),
    n("Sonic Bombardment", True),
    n("Imbalance & Kintan Strider", True),
    n("Imperial Barrier"),
    n("Ghhhk & Those Rebels Won't Escape Us", True, qty=2),
    n("None Shall Pass", True, qty=2),
    n("Stunning Leader", qty=2),
    n("Cold Feet", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = [
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
]
