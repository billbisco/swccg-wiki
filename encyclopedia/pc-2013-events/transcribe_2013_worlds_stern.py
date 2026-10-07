#!/usr/bin/env python3
"""2013 World Championship Day 2: Brandon Stern Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Brandon Stern"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 20
DS_PAGE = 19
LS_SCAN = "2013 Worlds Day 2 p20 Brandon Stern LS.png"
DS_SCAN = "2013 Worlds Day 2 p19 Brandon Stern DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Brandon. # box Stern v Beatdown. "
    "Username blank. Deck title David Beatdown. LIGHT. "
    "Watch Your Step dested Watch Your Step. "
    "Tatooine (Ep 1) dested Tatooine (Coruscant). "
    "Desperate Plea dested as written. "
    "Cardo Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Han Solo Courageous Smuggler dested Han Solo, Courageous Smuggler. "
    "I'll Take The Leader dested I'll Take The Leader. "
    "Insurrection (Aim High) dested Insurrection. "
    "Control / Tunnel Vision dested Control & Tunnel Vision. "
    "Spaceport - DB dested Spaceport Docking Bay. "
    "Garto Corellian dested as written. "
    "Nar Shaddaa with Ch / Out of Service dested "
    "Nar Shaddaa Wind Chimes & Out Of Somewhere. "
    "Taller Farris dested Tallon Roll. "
    "Houjix / Out of Somewhere dested Houjix & Out Of Nowhere. "
    "Phyfo Gardan dested Phylo Gandish. "
    "This A Hut dested Tatooine: Obi-Wan's Hut. "
    "We're Moving dested as written. "
    "Relian dested as written. "
    "Fallen Skies dested as written. "
    "Dark Thunder dested as written. "
    "We Can Still Avoid This Being dested We Can Still Outmaneuver Them. "
    "Oance Ta dested as written. "
    "Planetary Defender dested Planetary Defenses. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Brandon. # box Stern v Beatdown. "
    "Username blank. Deck title Skilling Numbers. DARK. "
    "My Lord Is That Legal dested My Lord, Is That Legal? / I Will Make It Legal. "
    "Ghhhk / Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "eNassoo dested Naboo. "
    "Darth Vader w/ stick dested Darth Vader With Lightsaber. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Darth Maul w/ stick dested Darth Maul With Lightsaber. "
    "Omni Box / It's Worse dested Ommni Box & It's Worse. "
    "SRF / Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Spotting Delegate dested Squabbling Delegates. "
    "Ability, Ability, Ability (V) box struck dested without (V). "
    "Accusing Trade Federation Consul dested Accepting Trade Federation Control. "
    "Naboo: Generator Core dested Naboo: Theed Palace Generator Core. "
    "Coruscant: Senate dested Coruscant: Galactic Senate. "
    "They're Still Coming Through dested They're Still Coming Through!. "
    "Slave One, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Mara Jade w/ stick dested Mara Jade With Lightsaber. "
    "Toonbuck Toora dested Toonbuck Toora. "
    "Yes Yak dested as written. "
    "Raikel Ueesnn dested as written. "
    "Aro Moe dested Aks Moe. "
    "Federal Box Gun dested as written. "
    "System Defense dested as written. "
    "The Emperor dested The Emperor. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Mos Eisley"),
    n("Desperate Plea", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Han Solo, Courageous Smuggler", True),
    n("I'll Take The Leader", qty=2),
    n("Tatooine: Docking Bay 94"),
    n("Squadron Assignments"),
    n("Insurrection", True),
    n("Wokling"),
    n("Control & Tunnel Vision", qty=2),
    n("Spaceport Docking Bay", True),
    n("Garto, Corellian"),
    n("Patrol Craft", qty=5),
    n("Luke Skywalker", True),
    n("Tatooine Celebration", qty=2),
    n("Infinity", True),
    n("Moving To Attack Position"),
    n("Fallen Portal", qty=2),
    n("Palace Raider", qty=6),
    n("Artoo-Detoo In Red 5"),
    n("Rebel Barrier"),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Wedge Antilles", True),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("Menace Fades"),
    n("Fallen Skies"),
    n("BoShek, Brash Smuggler", True),
    n("Tallon Roll"),
    n("Imperial Atrocity", True),
    n("Heading For The Medical Frigate"),
    n("Relian", True, qty=2),
    n("Mirax Terrik"),
    n("Houjix & Out Of Nowhere"),
    n("Phylo Gandish"),
    n("Millennium Falcon"),
    n("It Could Be Worse"),
    n("Outrider"),
    n("Dark Thunder"),
    n("Tatooine: Obi-Wan's Hut"),
    n("We're Moving"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("The Professor"),
    n("We Can Still Outmaneuver Them", True),
    n("Oance Ta", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
]
LS_ADD = [
    n("Ultimatum"),
    n("Jabba's Prize"),
    n("Simple Tricks And Nonsense", True),
]


DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Naboo"),
    n("Darth Vader With Lightsaber", qty=2),
    n("Cloud City: Security Tower", True),
    n("Senate Hovercam"),
    n("Sense", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Jango Fett, The Assassin", True),
    n("Vote Now!"),
    n("Ommni Box & It's Worse"),
    n("First Strike"),
    n("The Phantom Menace"),
    n("Protocol Failure", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Squabbling Delegates", qty=3),
    n("Imperial Barrier"),
    n("Lord Sidious"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Ability, Ability, Ability"),
    n("This Is Outrageous!"),
    n("Our Blockade Is Perfectly Legal"),
    n("Motion Supported"),
    n("Accepting Trade Federation Control"),
    n("Naboo: Theed Palace Generator Core"),
    n("Coruscant: Galactic Senate"),
    n("Limited Resources"),
    n("Sonic Bombardment", True),
    n("Cold Feet", True),
    n("They're Still Coming Through!"),
    n("Alter"),
    n("The Emperor", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("Mara Jade With Lightsaber", True),
    n("P-59"),
    n("Lott Dod", qty=3),
    n("Toonbuck Toora", qty=2),
    n("Yes Yak"),
    n("Tikkes", qty=2),
    n("Raikel Ueesnn", qty=2),
    n("Aks Moe"),
    n("Orn Free Taa", qty=2),
    n("Federation Box Gun"),
    n("System Defense", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("A Useless Gesture"),
    n("You Cannot Hide Forever", True),
    n("Imperial Detention", True),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Fanfare", True),
]
DS_ADD = [
    n("We'll Let Fate-A Decide, Huh?"),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
]
