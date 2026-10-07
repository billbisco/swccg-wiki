#!/usr/bin/env python3
"""2014 Alderaan Regionals typed GEMP lists: Nathan (SolaGratia).

Source: 2014-Alderaan-Regionals.pdf pages 5–6.
Name Nathan T / Username SolaGratia dested existing Nathan stub
(same SoCal / 2013 Alderaan Nathan). Do not invent a last name.
"""
from __future__ import annotations

PLAYER = "Nathan"
USERNAME = "SolaGratia"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2014 Alderaan Regionals p05 Nathan LS.png"
DS_SCAN = "2014 Alderaan Regionals p06 Nathan DS.png"
NOTE = (
    "Typed GEMP list (not a handwritten Xerox form). "
    "Name Nathan T dested Nathan (existing stub). Username SolaGratia. "
    "LS Communing / DS Hunt Down And Destroy The Jedi. "
    "Anger, Fear, Agression dested Anger, Fear, Aggression. "
    "Threepio With Hist Parts Showing dested Threepio With His Parts Showing. "
    "Han with Heavey Blaster Pistol dested Han With Heavy Blaster Pistol. "
    "Chewie's Bowcaster dested Chewbacca's Bowcaster. "
    "Run, Luke Run dested Run Luke, Run!. "
    "Commando Training & K'lor' slug dested Commando Training & K'lor'slug. "
    "Weapon Display dested Weapons Display. "
    "Do, or Do Not dested Do, Or Do Not. "
    "Tatooine (ep 1) dested Tatooine. "
    "Huntdown & Destroy the Jedi / flip dested Hunt Down And Destroy The Jedi / "
    "Their Fire Has Gone Out Of The Universe without True. "
    "Exec: Med Chamber / Holotheatre dested Executor: Meditation Chamber / Holotheatre. "
    "Ni Chuba Na?? dested Ni Chuba Na?. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Slave 1, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Dr. E COMBO dested Dr. Evazan & Ponda Baba. "
    "EPP Maul dested Darth Maul With Lightsaber. "
    "EPP Mara dested Mara Jade With Lightsaber. "
    "EPP Dengar dested Dengar With Blaster Carbine. "
    "Masterful Move combo dested Masterful Move & Endor Occupation. "
    "Force Lightening dested Force Lightning. "
    "Sith Fury Combo dested Sith Fury & End This Destructive Conflict. "
    "Weapon Lev Combo dested Weapon Levitation & The Empire's Back. "
    "Short Range Fighters / WYB dested Short Range Fighters & Watch Your Back!. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "SSPFT dested Something Special Planned For Them. "
    "Allegation of Corruption dested Allegations Of Corruption. "
    "We'll Let Fate Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Image of the dark lord dested Image Of The Dark Lord. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "There is No Try dested There Is No Try. "
    "Chewie, Protector dested Chewbacca, Protector. "
    "(V) from written (v). Unique overcounts sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Home One: War Room"),
    n("Tatooine"),
    n("Chewbacca's Bowcaster"),
    n("Anakin's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Chewie, Enraged", True, qty=2),
    n("Chewbacca, Protector"),
    n("Yoda, Great Warrior"),
    n("Leia, Rebel Princess"),
    n("Anakin Skywalker, Padawan Learner", qty=3),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Lando Calrissian, Scoundrel", True),
    n("Jaina Solo"),
    n("Padme Naberrie", True),
    n("Han With Heavy Blaster Pistol"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Control & Tunnel Vision"),
    n("A Gift"),
    n("Use The Force"),
    n("Imperial Atrocity", True),
    n("Commando Training & K'lor'slug"),
    n("Jedi Levitation", True),
    n("Seeking An Audience", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Escape Pod", True, qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("Yub Yub, Commander", qty=2),
    n("Houjix"),
    n("Found Someone You Have & Higher Ground"),
    n("Rebel Leadership", True, qty=3),
    n("Sai'torr Kal Fas", True),
    n("Strikeforce", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum", True),
    n("Planetary Defenses", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor", qty=2),
    n("Prepared Defenses"),
    n("Conduct Your Search"),
    n("Gift Of The Master"),
    n("Ni Chuba Na?", True),
    n("Knowledge And Defense", True),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Endor: Back Door"),
    n("Vader's Lightsaber"),
    n("Dooku's Lightsaber"),
    n("Slave I, Symbol Of Fear"),
    n("Blizzard 4", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Lord Vader", qty=2),
    n("Count Dooku", qty=3),
    n("Emperor Palpatine", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Dengar With Blaster Carbine", True),
    n("P-59"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Blast Door Controls"),
    n("The Phantom Menace"),
    n("Image Of The Dark Lord", True),
    n("Revenge Of The Sith"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Masterful Move & Endor Occupation"),
    n("Force Lightning", qty=2),
    n("Force Push", True, qty=2),
    n("Sith Fury & End This Destructive Conflict", qty=2),
    n("Weapon Levitation & The Empire's Back"),
    n("Sonic Bombardment", True, qty=3),
    n("Force Field", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Something Special Planned For Them", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Imperial Detention", True),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Death Star Sentry", True),
]
DS_ADD = []
