#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 2: Matthew Harrison-Trainor typed HDv + Light change sheet."""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 SoCal Grand Prix Day 2.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2013 SoCal Grand Prix Day 2 p03 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 2 p04 Matthew Harrison-Trainor DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 SoCal Grand Prix Day 1 p15 Matthew Harrison-Trainor LS.png",
        "Page 15 of [[:File:2013 SoCal Grand Prix Day 1.pdf]].",
    ),
    (
        "2013 SoCal Grand Prix Day 1 p16 Matthew Harrison-Trainor LS.png",
        "Page 16 of [[:File:2013 SoCal Grand Prix Day 1.pdf]].",
    ),
]
DS_EXTRA_SCANS = [
    (
        "2013 SoCal Grand Prix Day 2 p05 Matthew Harrison-Trainor DS.png",
        "Page 5 of [[:File:2013 SoCal Grand Prix Day 2.pdf]].",
    )
]
LS_NOTE = (
    "Day 2 Light change sheet headed Same (the Day 1 Watch Your Step list). "
    "OUT Corellian Slip, Corellian Retort (one copy), It's A Trap, Evacuation Control, "
    "Desperate Reach, Houjix combo, Fallen Jedi. IN Booster Terrik, 2 Escape Pod, Houjix, "
    "Grimtaash, Leia's Blaster (Leia's Sporting Blaster), Captain Yutani With Blaster Cannon. "
    "Day 1 typed pages are on this article with the change sheet."
)
DS_NOTE = (
    "Typed Holotable printout (not a handwritten Xerox form). Header DS HDv, signed Matt HT. "
    "Strikethroughs and dashed lines are OUT (Jango Fett, Dengar With Blaster Carbine, "
    "Juno Eclipse, General Nevar, Grand Admiral Thrawn, Endor Shield, Ni Chuba Na?, "
    "No Escape, Presence Of The Force, Cold Feet, Masterful Move x2, Imperial Tyranny, "
    "Prepared Defenses, Hoth: Defensive Perimeter, Victory, Blizzard 4 x2). "
    "Handwritten IN Elis Helrot, 2 Lightsaber Deficiency, Protocol Failure, 2 Grievous, "
    "Grievous's Lightsaber. Galen's Fighter dests Rogue Shadow. Ambiguous handwritten "
    "+ 3/2 site and + Ghhk Combo are not dested. You Are Beaten was written then struck."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("No Questions Asked", True, qty=3),
    n("Palejo Reshad"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mirax Terrik"),
    n("Dash Rendar", True, qty=2),
    n("Laudica", True),
    n("Mace Windu, Master Of The Order"),
    n("Yoda, Great Warrior"),
    n("Chewie", True),
    n("Jabba's Prize"),
    n("Captain Han Solo"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Corran Horn"),
    n("Romas 'Lock' Navander"),
    n("Leia, Rebel Princess", qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Padme Naberrie", True),
    n("Wokling", True),
    n("Seeking An Audience", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
    n("Punch It!"),
    n("Antilles Maneuver", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Corellian Retort", True),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=2),
    n("Spaceport City"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Corellia", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII"),
    n("Millennium Falcon", True),
    n("Lady Luck"),
    n("Booster Terrik"),
    n("Escape Pod", qty=2),
    n("Houjix"),
    n("Grimtaash"),
    n("Leia's Sporting Blaster"),
    n("Captain Yutani With Blaster Cannon"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Ultimatum"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Your Ship?"),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Boba Fett, Bounty Hunter"),
    n("Garindan", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine", qty=3),
    n("Grand Moff Tarkin", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Kir Kanos With Force Pike"),
    n("Galen Marek, Starkiller", qty=3),
    n("Elis Helrot"),
    n("General Grievous", qty=2),
    n("Gift Of The Master"),
    n("A Sith's Plans"),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("A Sith's Weapon"),
    n("Blast Door Controls"),
    n("Revenge Of The Sith"),
    n("Knowledge And Defense", True),
    n("Sniper & Dark Strike"),
    n("Ghhhk"),
    n("I Have You Now"),
    n("We Must Accelerate Our Plans", qty=3),
    n("One Beautiful Thing"),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Lightning"),
    n("Force Field", True, qty=2),
    n("Lightsaber Deficiency", qty=2),
    n("Protocol Failure"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Imperial City"),
    n("Endor"),
    n("Coruscant"),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Rogue Shadow"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
]
DS_ADD = []
