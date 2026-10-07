#!/usr/bin/env python3
"""2014 Match Play Championship Day 2 Xerox: Stephen Cellucci.

Source: MPC-2014-Day-2-Main-Event.pdf pages 1–2 (2013 form, 15 shields).
Name Stephen Cellucci. Username nolimit. Email [redacted].
Dark full 60 Agents Of Black Sun. Light Trevastation Same as Day 1 with In/Out.
"""
from __future__ import annotations

PLAYER = "Stephen Cellucci"
USERNAME = "nolimit"
STAGE = "Day 2"
PDF = "2014 Match Play Championship Day 2.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2014 Match Play Championship Day 2 Stephen Cellucci LS.png"
DS_SCAN = "2014 Match Play Championship Day 2 Stephen Cellucci DS.png"
LS_DECK_NAME = "Trevastation"
DS_DECK_NAME = "AOBS"
NOTE = "Handwritten 2013 Xerox. Light Same as Yesterday with In/Out."
LS_PUBLIC_NOTE = (
    "Same as Day 1 Light with In/Out substitutions listed on the scan."
)
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Stephen Cellucci. Username nolimit. LIGHT checked. "
    "Deck Trevastation. Same as Day 1. OUT Scrambled Transmission (V), Obi-Wan's Lightsaber, "
    "Houjix. IN Nick Of Time (V), Jawa Siesta, Odin Nesloor & First Aid. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Stephen Cellucci. Username nolimit. Email [redacted]. "
    "DARK checked. AOBS dested Agents Of Black Sun / Vengeance Of The Dark Prince. Dual-title "
    "(V) empty. Imperial Stockpile dested Imperial Stockpile. Desilijic Tatoo dested Desilijic Tattoo (V). "
    "They're Still Coming Through dested They're Still Coming Through!. "
    "He's All Yours dested He's All Yours, Bounty Hunter (V). "
    "Line 56 Something Special Planned For Them crossed; Hidden Fortress CARD #56 "
    "Cloud City: Security Tower (V) replacement. Dittos inherit (V). "
    "Unique overcounts sheet-accurate (We Must Accelerate Our Plans x2, Unexpected Interruption x2, "
    "Sonic Bombardment (V) x2, Lightsaber Deficiency (V) x2, He's All Yours, Bounty Hunter (V) x2, "
    "Defensive Fire (V) x2, Zuckuss (V) x2, Jodo Kast x2, Garindan (V) x2, "
    "Dengar With Blaster Carbine (V) x2, Bane Malar, Spike Addict x2, IG-88 With Riot Gun x2, "
    "Maul's Sith Infiltrator x2, They're Still Coming Through! x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Treva Horme"),
    n("IL-19"),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Corran Horn"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Chewbacca, Protector", qty=2),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Stone Pile", qty=2),
    n("Seeking An Audience", True),
    n("Lightsaber Proficiency"),
    n("K'lor'slug", True),
    n("Anger, Fear, Aggression", True),
    n("Mechanical Failure"),
    n("It Is The Future You See", True),
    n("Clash Of Sabers"),
    n("Jedi Presence", qty=2),
    n("Control & Tunnel Vision"),
    n("Courage Of A Skywalker", qty=2),
    n("Gift Of The Mentor"),
    n("Rebel Leadership", True, qty=2),
    n("Sense"),
    n("NOOOOOOOOOOOO!", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Nabrun Leids"),
    n("You Will Go To The Dagobah System", True, qty=4),
    n("Wesa Gotta Grand Army", qty=3),
    n("Precise Hit", True),
    n("Either Way, You Win", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Dagobah: Yoda's Hut"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Battle Plains"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Chewbacca's Bowcaster"),
    n("Nick Of Time", True),
    n("Jawa Siesta"),
    n("Odin Nesloor & First Aid"),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
]
LS_ADD = []


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Information Exchange", True),
    n("Scum And Villainy"),
    n("Trophy Of A Bounty Hunter"),
    n("Prince Xizor", True),
    n("Twi'lek Advisor", True),
    n("Protocol Failure"),
    n("Ket Maliss", True),
    n("Imperial Stockpile"),
    n("Desilijic Tattoo", True),
    n("They're Still Coming Through!", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Unexpected Interruption", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Imperial Barrier"),
    n("Hidden Weapons"),
    n("He's All Yours, Bounty Hunter", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Defensive Fire", True, qty=2),
    n("Comscan Detection", True),
    n("Zuckuss", True, qty=2),
    n("Reegesk", True),
    n("Jodo Kast", qty=2),
    n("Greedo With Blaster Pistol"),
    n("Greedo", True),
    n("Garindan", True, qty=2),
    n("Dengar With Blaster Carbine", True, qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("Bane Malar, Spike Addict", qty=2),
    n("Aurra Sing"),
    n("IG-88 With Riot Gun", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Spaceport Docking Bay"),
    n("Death Star: War Room", True),
    n("Blockade Flagship: Bridge"),
    n("Naboo Blaster Rifle"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Cloud City: Security Tower", True),
    n("OOM-9", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Abyss"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Imperial Detention"),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("Resistance", True),
    n("Oppressive Enforcement", True),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
]
DS_ADD = []
