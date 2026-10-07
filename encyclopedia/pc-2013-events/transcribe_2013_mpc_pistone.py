#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Pistone Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Pistone"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 73
DS_PAGE = 74
LS_SCAN = "2013 Match Play Championship p73 Pistone LS.png"
DS_SCAN = "2013 Match Play Championship p74 Pistone DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Pistone. Light. "
    "Deck title Bunkers Full of Women. "
    "WYS / TPCBALT dested Watch Your Step / This Place Can Be A Little Rough. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Corellian Engineering Corp dested Corellian Engineering Corporation. "
    "Spaceport: City dested Spaceport City. H1: Docking Bay dested Home One: Docking Bay. "
    "Spaceport: Docking Bay dested Spaceport Docking Bay. "
    "Spaceport: Scoundrel's Guild dested Spaceport Scoundrels Guild. "
    "Spaceport: Street dested Spaceport Street. "
    "Corellian Retort as written. All Wings Report In & Darklighter dested "
    "All Wings Report In & Darklighter Spin. "
    "Antilles Maneuver Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Boshek's Modified Light Freighter dested BoShek's Modified Light Freighter. "
    "Lando's Luxury Yacht dested Lady Luck. Sergeant Bruckman dested Sergeant Bruckman. "
    "Wedge Antilles, Red Squadron Leader dested Wedge Antilles, Red Squadron Leader. "
    "Boshkk, Brash Smuggler dested BoShek, Brash Smuggler. Chewie dested Chewie, Enraged. "
    "LSJK dested Luke Skywalker, Jedi Knight. Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Jabba's Prize dested Jabba's Prize. Do or Do Not dested Do, Or Do Not. "
    "Simple Tricks And Nonsense struck; Don't Do That Again written below Additional. "
    "Form left column reprints 37–38 on lines 39–40 are Sergeant Bruckman and General Crix Madine. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Pistone. Dark. Deck title Jango Unchained. "
    "HDADTJ / Their Fire Has Gone Out dested Hunt Down And Destroy The Jedi / "
    "Their Fire Has Gone Out Of The Universe. Knowledge And Defense as written. "
    "Ni Chuba Na?? dested Ni Chuba Na?. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Galen's Fighter dested Rogue Shadow. "
    "Weapon Levitation & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Blockade: Flagship Bridge dested Blockade Flagship: Bridge. "
    "Naboo: Theed Palace Generator Core dested Naboo: Theed Palace Generator Core. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Coruscant (SE) dested Coruscant. Dudlots as written. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "EPP Mara dested Mara Jade With Lightsaber. "
    "Kir Kanos w/ Force Pike dested Kir Kanos With Force Pike. "
    "The Mandalorian, FOF dested Jango Fett, The Assassin. "
    "Cyborg Commander, HOJ dested Grievous, Hunter Of Jedi. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Sniper & Dark Strike dested Sniper & Dark Strike. Thrawn dested Grand Admiral Thrawn. "
    "We'll Let Fate-a Delie, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Form left column reprints 37–38 on lines 39–40 are A Sith's Plans and Coruscant: Imperial City. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Heading For The Medical Frigate"),
    n("Captain Han Solo"),
    n("Millennium Falcon", True),
    n("Spaceport City"),
    n("Corellia", True),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Spaceport Street"),
    n("No Questions Asked", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Corellian Retort", True),
    n("Rebel Barrier", True, qty=2),
    n("K'lor'slug", True),
    n("Menace Fades"),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver", True),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("BoShek's Modified Light Freighter"),
    n("Lady Luck"),
    n("Spiral"),
    n("Mirax Terrik"),
    n("Sergeant Bruckman"),
    n("General Crix Madine"),
    n("Corran Horn"),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Leia, Rebel Princess"),
    n("Chewie, Enraged", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("BoShek, Brash Smuggler"),
    n("Yoda, Great Warrior", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Padme Naberrie", True),
    n("Maris Brood, Fallen Jedi"),
    n("Imperial Atrocity", True),
    n("Grimtaash"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Weapons Display", True),
    n("Chasm", True),
    n("Battle Plan"),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Prepared Defenses", True),
    n("Ni Chuba Na?", True),
    n("Gift Of The Master"),
    n("Endor Shield", True),
    n("Endor"),
    n("Dudlots", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Vader's Lightsaber"),
    n("Emperor's Power", True),
    n("Emperor Palpatine", qty=3),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Rogue Shadow"),
    n("Weapon Levitation & The Empire's Back"),
    n("Blast Door Controls"),
    n("Monnok"),
    n("Blockade Flagship: Bridge"),
    n("Restraining Bolt"),
    n("Naboo: Theed Palace Generator Core"),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("Juno Eclipse, Black Leader"),
    n("Grand Moff Tarkin", True),
    n("Force Lightning"),
    n("Garindan", True),
    n("Protocol Failure"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Coruscant"),
    n("A Sith's Plans"),
    n("Coruscant: Imperial City"),
    n("A Sith's Weapon"),
    n("Blaster Rack", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Imperial Justice", True),
    n("Blizzard 4"),
    n("Mara Jade With Lightsaber"),
    n("Force Field", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Victory"),
    n("Grand Admiral Thrawn"),
    n("Force Push", True),
    n("Kir Kanos With Force Pike"),
    n("Jango Fett, The Assassin"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Grievous' Lightsabers"),
    n("Revenge Of The Sith"),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
