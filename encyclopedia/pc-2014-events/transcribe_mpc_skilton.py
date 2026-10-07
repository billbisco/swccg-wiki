#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Steve Skilton.

Source: MPC-2014-Day-1-Main-Event.pdf pages 100–101 (2013 form, 15 shields).
Name Steve S. dested Steve Skilton. Username stevetotheizzo.
"""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = "stevetotheizzo"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 100
DS_PAGE = 101
LS_SCAN = "2014 Match Play Championship Day 1 Steve Skilton LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Steve Skilton DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Steve S. dested Steve Skilton. Username stevetotheizzo. "
    "LIGHT checked. Plead My Case dested Plead My Case To The Senate / Mad About The Won-Won. "
    "EBI Coruscant dested Coruscant. H4:WR dested Home One: War Room. Yoda GW dested "
    "Yoda, Great Warrior. Bail, FDR dested Bail Organa, Father To One Destined For Leadership. "
    "ERP Obi dested Obi-Wan Kenobi, Padawan Learner analog EPP Obi-Wan With Lightsaber. "
    "ACS dested A Change Of Season. AZSO dested Anakin's Podracer analog AZSO as written. "
    "Unique overcounts sheet-accurate (Let The Wookiee Win (V) x3, A Change Of Season x2, "
    "Bail Organa, Father To One Destined For Leadership x3, Luke Skywalker, Rebel Scout (V) x2, "
    "Lando Calrissian, Scoundrel x2, Obi-Wan With Lightsaber x2, Yoda, Great Warrior x2, "
    "Might x3, Sense x2, Rebel Barrier x2, Jedi Presence x2, Imperial Atrocity x2). "
    "NO_DEST Plead My Case To The Senate / Mad About The Won-Won; A Change Of Season; Bail Organa, Father To One Destined For Leadership; General Cracken; Queen Beru; Narra; Might. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Steve S. dested Steve Skilton. Username stevetotheizzo. "
    "DARK checked. Kessel starting. Spice Mine Ops dested Spice Mine Operations. "
    "K+D dested Knowledge And Defense. Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Sniper Combo dested Sniper & Dark Strike. Short Range Combo dested Short Range Fighters & Watch Your Back!. "
    "Galen dested Galen Marek, Starkiller. Emp Maul dested Darth Maul, Young Apprentice analog Emperor's Maul. "
    "Slave I SOF dested Slave I, Symbol Of Fear. Unique overcounts sheet-accurate "
    "(Sense (V) then Sense x3, Force Field (V) x3, Force Lightning x2, Sith Fury (V) x2, "
    "Short Range Fighters & Watch Your Back! x2, Emperor Palpatine x3, Darth Maul x2, "
    "Galen Marek, Starkiller x3, Count Dooku x2). NO_DEST Kessel: Administrator's Office; Blown Communications; Spice Mine Administrator; Kessel: Cantina. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Mad About The Won-Won"
LS_CARDS = [
    n("Plead My Case To The Senate / Mad About The Won-Won"),
    n("Coruscant"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Lower Level"),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("A Change Of Season", qty=2),
    n("Anakin Skywalker, Padawan Learner", True),
    n("Mas Amedda"),
    n("Bail Organa"),
    n("Senator Padme Amidala"),
    n("Senator Mon Mothma"),
    n("Bail Organa, Father To One Destined For Leadership", qty=3),
    n("Senator Leia Organa"),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Wedge Antilles"),
    n("General Solo"),
    n("General Cracken"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Queen Beru"),
    n("Narra"),
    n("Corran Horn"),
    n("Chewbacca, Protector"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Dash Rendar", True),
    n("Might", qty=3),
    n("Sense", qty=2),
    n("Rebel Barrier", qty=2),
    n("Jedi Presence", qty=2),
    n("Imperial Atrocity", qty=2),
    n("Strike Planning"),
    n("Wokling"),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Menace Fades"),
    n("Senate Hovercam"),
    n("K'lor'slug"),
    n("Field Dressing"),
    n("So This Is How Liberty Dies"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Ultimatum"),
    n("Aim High"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Weapons Display"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("He Can Go About His Business"),
]
LS_ADD = []


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Kessel: Administrator's Office"),
    n("Spice Mine Operations"),
    n("Gift Of The Master"),
    n("I'll Take Them Myself"),
    n("Ni Chuba Na??", True),
    n("Combat Readiness", True),
    n("Knowledge And Defense", True),
    n("Imperial Justice", True),
    n("Dark Maneuvers"),
    n("Blown Communications"),
    n("Why Didn't You Tell Me?", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sniper & Dark Strike"),
    n("4-LOM"),
    n("A Dark Time For The Rebellion", True),
    n("Sense", True),
    n("Sense", qty=2),
    n("Force Field", True, qty=2),
    n("Sith Fury", True, qty=2),
    n("Force Field", True),
    n("Force Lightning", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Lightsaber Deficiency", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Arica"),
    n("Spice Mine Administrator"),
    n("Darth Sidious"),
    n("Emperor Palpatine", qty=3),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Count Dooku", qty=2),
    n("Garindan", True),
    n("P-59"),
    n("Blizzard 4"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dooku's Lightsaber"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Kessel: Cantina"),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mines - Prison"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Protocol Failure"),
    n("Blaster Rack", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Do They Have A Code Clearance"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Fanfare"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
]
DS_ADD = []
