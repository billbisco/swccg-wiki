#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Amar Banger.

Source: MPC-2014-Day-1-Main-Event.pdf pages 15–16 (typed HTML 2002/Print Form).
Username blank. Deck titles HDv / Chewmuning.
"""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2014 Match Play Championship Day 1 Amar Banger LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Amar Banger DS.png"
LS_DECK_NAME = "Chewmuning"
DS_DECK_NAME = "HDv"
NOTE = "Typed HTML leftover Xerox."
LS_NOTE = (
    "Typed HTML leftover Xerox p16. Username blank. Deck title Chewmuning dested "
    "Communing. HTML (VN) is Virtual Block. Communing / Master Kenobi / Yoda, Great "
    "Warrior virtual-only v=False. Tatooine (EP1) dested Tatooine. Unique overcounts "
    "sheet-accurate (Artoo-Detoo In Red 5 x2, Chewbacca, Protector x2, Chewie, Enraged "
    "(V) x2, Escape Pod (V) x3, Houjix x2, Let The Wookiee Win (V) x3, Luke With "
    "Lightsaber x2, Rebel Leadership (V) x3, Run Luke, Run! (V) x3, The Bith Shuffle "
    "& Desperate Reach x2). (V) from HTML (VN) on Decipher reprints."
)
DS_NOTE = (
    "Typed HTML leftover Xerox p15. Username blank. Deck title HDv. Hunt Down (V) "
    "dested Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The "
    "Universe (V). Line 38 Jabba's Haven crossed, After Her! dested After Her!. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "P-59 dested P-59. Unique overcounts sheet-accurate (Blizzard 4 x2, Darth Vader, "
    "Dark Lord Of The Sith x2, Emperor Palpatine x2, Force Field (V) x2, Galen Marek, "
    "Starkiller x3, Lightsaber Deficiency (V) x2, Revenge Of The Sith (V) x2, We Must "
    "Accelerate Our Plans x3). (V) from HTML (VN) on Decipher reprints."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Nick Of Time", True),
    n("Tatooine: Slave Quarters"),
    n("Wokling", True),
    n("A Jedi's Resilience"),
    n("Admiral Ackbar", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Chewbacca's Bowcaster"),
    n("Chewbacca, Protector", qty=2),
    n("Chewie, Enraged", True, qty=2),
    n("Corran Horn"),
    n("Escape Pod", True, qty=3),
    n("Flash Of Insight", True),
    n("Han With Heavy Blaster Pistol"),
    n("Hear Me Baby, Hold Together", True),
    n("Home One"),
    n("Home One: War Room"),
    n("Houjix", qty=2),
    n("Imperial Atrocity", True),
    n("K'lor'slug", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Leia, Rebel Princess"),
    n("Let The Wookiee Win", True, qty=3),
    n("Lucky Shot", True),
    n("Luke Skywalker", True),
    n("Luke With Lightsaber", qty=2),
    n("Much To Learn, You Still Have", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Padme Naberrie", True),
    n("Rebel Gunrunner", True),
    n("Rebel Leadership", True, qty=3),
    n("Run Luke, Run!", True, qty=3),
    n("Seeking An Audience", True),
    n("Shmi Skywalker"),
    n("Strikeforce", True),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("The Force Is Strong With This One"),
    n("Threepio With His Parts Showing"),
    n("Use The Force", True),
    n("Yoda, Great Warrior"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Ship?"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("A Sith's Plans", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Endor Shield", True),
    n("Gift Of The Master", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Knowledge And Defense", True),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses", True),
    n("Blaster Rack", True),
    n("Blizzard 4", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Boba Fett, Bounty Hunter"),
    n("Cold Feet", True),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine", qty=2),
    n("Endor"),
    n("Endor: Back Door"),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("Force Push", True),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("General Nevar", True),
    n("Ghhhk"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("I Have You Now"),
    n("After Her!"),
    n("Juno Eclipse, Black Leader", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Mara Jade With Lightsaber", True),
    n("Masterful Move"),
    n("No Escape"),
    n("Ommni Box & It's Worse"),
    n("One Beautiful Thing", True),
    n("P-59"),
    n("Protocol Failure", True),
    n("Revenge Of The Sith", True, qty=2),
    n("Rogue Shadow", True),
    n("Sense & Uncertain Is The Future"),
    n("Something Special Planned For Them", True),
    n("Stop Motion", True),
    n("Vader's Lightsaber"),
    n("Victory", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Wipe Them Out, All Of Them", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
