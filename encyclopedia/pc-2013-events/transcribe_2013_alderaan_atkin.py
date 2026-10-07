#!/usr/bin/env python3
"""2013 Alderaan Regionals: Clayton Atkin handwritten 2010 Xerox LS+DS.

Username same as name / Same as above. Dest Clayton Atkin.
Do not rewrite SoCal Atkin leftovers.
"""
from __future__ import annotations

PLAYER = "Clayton Atkin"
USERNAME = "Clayton Atkin"
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2013 Alderaan Regionals p10 Clayton Atkin LS.png"
DS_SCAN = "2013 Alderaan Regionals p09 Clayton Atkin DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Clayton Atkin. "
    "Username ditto of name dested Clayton Atkin. Event Alderaan Regional. LIGHT checked. "
    "Deck Name Might as well play it since I won't be able to again. "
    "MWYHL/SYC empty dested Mind What You Have Learned / Save You It Can. "
    "Strong is Vader dested Strong Is Vader. GP/DTF dested Battle Plan & Draw Their Fire. "
    "DoDN/WA dested Do, Or Do Not & Wise Advice. Wooooooooo! dested Wookiee Roar. "
    "Elegant Lightsaber dested Elegant Lightsaber. Fallen Jedi dested as written. "
    "Armed & Dangerous/KDH dested Armed And Dangerous & Krayt Dragon Howl. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Lando's Luxury Yacht dested Lady Luck. AWRI/DS dested "
    "All Wings Report In & Darklighter Spin. LSJK dested Luke Skywalker, Jedi Knight. "
    "Antilles Man/Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "Naboo: Theed Palace Generator dested Naboo: Theed Palace Generator. "
    "Dag Swamp dested Dagobah: Swamp. Overflow shields 13-15 Chasm / Affect Mind / "
    "Keep a Little Opt dested in Additional. Jedi Tests in Additional: Great Warrior, "
    "A Jedi's Strength, Domain Of Evil, Size Matters Not, It Is The Future You See, "
    "You Must Confront Vader."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Clayton Atkin. "
    "Username Same as above dested Clayton Atkin. DARK checked. Deck Name Rops. "
    "Ralltiir Operations/ITHOTE empty dested Ralltiir Operations / In The Hands Of The Empire. "
    "Victory dested Victory as written. The Mandalorian F.O.F. dested Jango Fett, The Assassin. "
    "Colonel David Jon dested Colonel Davod Jon. Slave I Symbol of Fear dested "
    "Slave I, Symbol Of Fear. MM/Endor Occupation dested Masterful Move & Endor Occupation. "
    "Darth Vader B.O.T.J. dested Darth Vader, Betrayer Of The Jedi. Ice-Heart dested "
    "Ysanne Isard. Something Special Planned dested Something Special Planned For Them. "
    "Where are you taking this dested Where Are You Taking This... Thing?. "
    "C.H.Y.B.C. dested Come Here You Big Coward. I.F.Y.L.O.F.D. dested "
    "I Find Your Lack Of Faith Disturbing. Imperial Decree empty (line 21) and True "
    "(line 50) kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can"),
    n("Dagobah"),
    n("Strong Is Vader"),
    n("It Is The Future You See", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Wokling", True),
    n("Rebel Leadership", True, qty=3),
    n("Wookiee Roar", True, qty=2),
    n("Luke's Backpack"),
    n("Weapon Levitation"),
    n("Imperial Atrocity", True),
    n("Clash Of Sabers"),
    n("Daughter Of Skywalker", True),
    n("Coruscant"),
    n("Corran Horn"),
    n("Projection Of A Skywalker"),
    n("Home One"),
    n("Elegant Lightsaber", qty=2),
    n("Master Qui-Gon", True),
    n("Yoda", True),
    n("Houjix"),
    n("Mace Windu, Master Of The Order"),
    n("Fallen Jedi"),
    n("Dodge"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Home One: War Room"),
    n("The Way Of Things"),
    n("Han, Chewie, And The Falcon", True),
    n("Naboo: Theed Palace Generator"),
    n("Dagobah: Swamp"),
    n("Escape Pod", True, qty=2),
    n("A Jedi's Plans"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Reflection", True),
    n("Launching The Assault"),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Jedi Levitation", True),
    n("A Jedi's Resilience"),
    n("Admiral Ackbar", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Jungle"),
    n("Yoda's Hope"),
    n("Quick Draw", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Luke Skywalker", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Redeemed Apprentice"),
    n("Artoo-Detoo In Red 5"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High", True),
    n("Battle Plan", True),
    n("Ultimatum", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
]

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("Insignificant Rebellion", True),
    n("Endor Shield", True),
    n("Special Delivery", True),
    n("Grand Admiral Thrawn"),
    n("Force Push", True),
    n("Victory"),
    n("Spaceport Prefect's Office"),
    n("Outflank", True),
    n("Monnok"),
    n("Kashyyyk"),
    n("Close Call", True),
    n("Spaceport Docking Bay"),
    n("Sonic Bombardment", True, qty=2),
    n("General Nevar"),
    n("Ralltiir: Spaceport Financial District"),
    n("Imperial Decree"),
    n("Endor"),
    n("Cold Feet", True),
    n("Spaceport Street"),
    n("Colonel Davod Jon"),
    n("Slave I, Symbol Of Fear"),
    n("Blizzard 2", True),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Jango Fett, The Assassin"),
    n("General Veers", True),
    n("Conquest", True),
    n("Emperor Palpatine", qty=2),
    n("Imperial Command", qty=2),
    n("Force Lightning"),
    n("Grand Moff Tarkin", True),
    n("He Hasn't Come Back Yet"),
    n("Admiral Ozzel"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Imperial Justice", True),
    n("Zuckuss In Mist Hunter"),
    n("Stop Motion", True),
    n("Janus Greejatus"),
    n("Where Are You Taking This... Thing?"),
    n("Imperial Barrier"),
    n("Blizzard 4", qty=2),
    n("Imperial Decree", True),
    n("Ysanne Isard"),
    n("Image Of The Dark Lord", True),
    n("Boba Fett, Prepared Hunter"),
    n("Something Special Planned For Them", True),
    n("Arica"),
    n("Blizzard 1", True),
    n("Cloud City: Security Tower", True),
    n("Ghhhk"),
    n("Garindan", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Leave Them To Me", True),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Fanfare", True),
]
DS_ADD = [
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("We'll Let Fate-a Decide, Huh?", True),
]
