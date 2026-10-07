#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Casey Anis.

Source: MPC-2014-Day-1-Main-Event.pdf pages 7–8 (2013 form, 15 shields).
Username blank.
"""
from __future__ import annotations

PLAYER = "Casey Anis"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2014 Match Play Championship Day 1 Casey Anis LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Casey Anis DS.png"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. LIGHT checked. Communing starting "
    "Objective (Tatooine: Slave Quarters). Commando Training + Klor Slug dested "
    "Commando Training & K'lor'slug. SATM combo dested Sorry About The Mess & Blaster "
    "Proficiency. Naked 3PO dested Threepio With His Parts Showing. EPP Han dested Han "
    "With Heavy Blaster Pistol. EPP Luke dested Luke With Lightsaber. Lando Scoundrel "
    "dested Lando Calrissian, Scoundrel. R2 in Red 5 dested Artoo-Detoo In Red 5. Yoda "
    "Great Warrior dested Yoda, Great Warrior. Unique overcounts sheet-accurate (Let The "
    "Wookiee Win (V) x2, Chewbacca, Protector x2, Use The Force x2, Escape Pod (V) x2, "
    "Han With Heavy Blaster Pistol x2, Houjix x2, Rebel Leadership (V) x3, Run Luke, Run! "
    "(V) x2, Luke With Lightsaber x2, Chewie, Enraged (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. DARK checked. Hunt Down (V) dested Hunt "
    "Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V). Gift "
    "of the Master dested Gift Of The Master. DLOTS dested Darth Vader, Dark Lord Of The "
    "Sith. Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. BF: Bridge "
    "dested Blockade Flagship: Bridge. Ghhhk combo dested Ghhhk & Those Rebels Won't "
    "Escape Us. Weapon Lev + The Empire's Back dested Weapon Levitation & The Empire's "
    "Back. K+D dested Knowledge And Defense. P-59 dested P-59. Unique overcounts "
    "sheet-accurate (Darth Vader, Dark Lord Of The Sith x2, Emperor Palpatine x2, We Must "
    "Accelerate Our Plans x3, Force Field (V) x2, Revenge Of The Sith x2, Galen Marek, "
    "Starkiller x3). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug"),
    n("Nick Of Time", True),
    n("Imperial Atrocity", True),
    n("Strikeforce", True),
    n("Draw Their Fire"),
    n("Let The Wookiee Win", True, qty=2),
    n("Inconsequential Barriers"),
    n("Chewbacca, Protector", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Tatooine: Cantina", True),
    n("Seeking An Audience", True),
    n("Use The Force", qty=2),
    n("Escape Pod", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Launching The Assault"),
    n("Security Breach"),
    n("Home One: War Room"),
    n("Tatooine"),
    n("Projection Of A Skywalker"),
    n("Shmi Skywalker"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Houjix", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("Admiral Ackbar", True),
    n("Luke With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", True),
    n("Tantive IV", True),
    n("Lucky Shot", True),
    n("Home One"),
    n("Leia, Rebel Princess"),
    n("Threepio With His Parts Showing"),
    n("Out Of Commission"),
    n("Corran Horn"),
    n("Chewie, Enraged", True, qty=2),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Yoda, Great Warrior"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Gunrunner"),
    n("Wedge Antilles", True),
    n("A Jedi's Resilience"),
    n("Artoo-Detoo In Red 5"),
    n("Grimtassh"),
    n("Redeemed Apprentice"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("Do, Or Do Not"),
    n("Affect Mind"),
    n("Planetary Defenses", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Emperor Palpatine", qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("Dengar With Blaster Carbine", True),
    n("Grand Admiral Thrawn"),
    n("Garindan", True),
    n("Mara Jade With Lightsaber", True),
    n("P-59"),
    n("Grand Moff Tarkin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Victory"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Blockade Flagship: Bridge"),
    n("Endor"),
    n("Blaster Rack", True),
    n("One Beautiful Thing"),
    n("No Escape"),
    n("Emperor's Power", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure"),
    n("Sniper & Dark Strike"),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("A Sith's Weapon"),
    n("Force Field", True, qty=2),
    n("Revenge Of The Sith", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Rogue Shadow"),
    n("Juno Eclipse, Black Leader"),
    n("Galen Marek, Starkiller", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Wipe Them Out, All Of Them", True),
    n("Image Of The Dark Lord", True),
    n("Something Special Planned For Them", True),
    n("Trophy Of A Kill"),
    n("Stop Motion", True),
    n("Force Push", True),
    n("Astromech Shortage", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("Leave Them To Me"),
    n("Death Star Sentry", True),
    n("Abyss", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("After Her!", True),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
