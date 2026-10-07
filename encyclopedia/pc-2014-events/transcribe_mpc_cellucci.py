#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Stephen Cellucci.

Source: MPC-2014-Day-1-Main-Event.pdf pages 31–34 (typed GEMP).
Username blank. LS Treva Horme Beatdown / DS Dark Senate.
"""
from __future__ import annotations

PLAYER = "Stephen Cellucci"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 31
DS_PAGE = 33
LS_SCAN = "2014 Match Play Championship Day 1 Stephen Cellucci LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Stephen Cellucci DS.png"
LS_DECK_NAME = "Treva Horme Beatdown"
DS_DECK_NAME = "Dark Senate"
NOTE = "Typed GEMP leftover Xerox."
LS_NOTE = (
    "Typed GEMP leftover Xerox p31–p32. Username blank. Deck Treva Horme Beatdown. "
    "IITFYS (V) dested It Is The Future You See (V) (starting Epic Event). Gift Of The "
    "Mentor dested Gift Of The Mentor. A Vengeance In The Force crossed, Scrambled "
    "Transmission (V) dested Scrambled Transmission (V). Obi-Wan's Lightsaber (Premiere) "
    "dested Obi-Wan's Lightsaber. Yoda, Great Warrior virtual-only v=False. Unique "
    "overcounts sheet-accurate (Yoda, Great Warrior x2, Obi-Wan Kenobi (V) x2, Chewbacca, "
    "Protector x2, Stone Pile x2, Jedi Presence x2, Courage Of A Skywalker x2, Rebel "
    "Leadership (V) x2, NOOOOOOOOOOOO! (V) x2, Escape Pod (V) x2, You Will Go To The "
    "Dagobah System (V) x4, Wesa Gotta Grand Army x3, Let The Wookiee Win (V) x2). "
    "(V) from typed (V)."
)
DS_NOTE = (
    "Typed GEMP leftover Xerox p33–p34. Username blank. Deck Dark Senate. MLITL dested "
    "My Lord, Is That Legal? / I Will Make It Legal. Jango Fett, The Assassin (AI) dested "
    "Jango Fett, The Assassin. U-3PO dested U-3PO. SRF+WYB dested Short Range Fighters "
    "& Watch Your Back!. Unique overcounts sheet-accurate (Lott Dod x3, Orn Free Taa x2, "
    "Toonbuck Toora x2, Baskol Yeesrim x2, Darth Maul With Lightsaber x2, Senate Hovercam "
    "x2, We Must Accelerate Our Plans x2, Sonic Bombardment (V) x2, Squabbling Delegates "
    "x3, Short Range Fighters & Watch Your Back! x2, Dengar In Punishing One x2). "
    "(V) from typed (V)."
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
    n("Scrambled Transmission", True),
    n("Anger, Fear, Aggression", True),
    n("Mechanical Failure"),
    n("It Is The Future You See", True),
    n("Clash Of Sabers"),
    n("Jedi Presence", qty=2),
    n("Control & Tunnel Vision"),
    n("Courage Of A Skywalker", qty=2),
    n("Houjix"),
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
    n("Obi-Wan's Lightsaber"),
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


DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("Black Sun Fleet"),
    n("Boba Fett, Prepared Hunter"),
    n("Bossk", True),
    n("Jango Fett, The Assassin"),
    n("Arica"),
    n("U-3PO"),
    n("4-LOM With Concussion Rifle"),
    n("Darth Vader With Lightsaber"),
    n("Tikkes"),
    n("Lott Dod", qty=3),
    n("Yeb Yeb Adem'thorn"),
    n("Passel Argente"),
    n("Edcel Bar Gane"),
    n("Orn Free Taa", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Baskol Yeesrim", qty=2),
    n("Aks Moe"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Senate Hovercam", qty=2),
    n("No Escape"),
    n("Jabba's Haven"),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True),
    n("Accepting Trade Federation Control"),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("This Is Outrageous!"),
    n("Knowledge And Defense", True),
    n("Look Sir, Droids"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Cold Feet", True),
    n("Squabbling Delegates", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Surface Defense", True),
    n("Coruscant: Galactic Senate"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo"),
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Hound's Tooth", True),
    n("Dengar In Punishing One", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
]
DS_ADD = []
