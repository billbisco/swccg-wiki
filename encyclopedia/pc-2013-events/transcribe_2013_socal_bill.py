#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Bill handwritten Print Form LS+DS.

Name field Bill. Username blank. Dest Bill as written (first name only).
Do not dest as Bill Kafer.
"""
from __future__ import annotations

PLAYER = "Bill"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2013 SoCal Grand Prix Day 1 p23 Bill LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p24 Bill DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Bill dested as written. Username blank. "
    "LIGHT/DARK empty; dest Light from Communing. "
    "Slave Quarters dested Tatooine: Slave Quarters. "
    "AFA dested Anger, Fear, Aggression True in the 60. "
    "Communing checkbox empty dested Communing without True. "
    "Wokling dested Wokling True. "
    "Tat Bl dested Tatooine: Bluffs as written. "
    "Shmi dested Shmi Skywalker. "
    "Artoo dested Artoo as written. "
    "Leia PP dested Leia, Rebel Princess. "
    "Lando Scoun dested Lando Calrissian, Scoundrel. "
    "Ell Man dested Ellorrs Madak. "
    "Chew Prat dested Chewbacca, Protector. "
    "Chew Enraged line 21 True / line 22 empty kept split. "
    "EPP Luke dested Luke With Lightsaber. "
    "Han pistol dested Han With Heavy Blaster Pistol. "
    "Seeking dested Seeking An Audience. "
    "Nick of Time dested Nick Of Time. "
    "Flash dested Flash as written. "
    "OTF dested Draw Their Fire. "
    "A Jedi Fail dested A Jedi's Fail as written. "
    "SATM+BP dested Sorry About The Mess & Blaster Proficiency. "
    "Jedi Lev dested Jedi Levitation. "
    "Throw dested Throw as written. "
    "HMBHT dested HMBHT as written. "
    "EWYW dested EWYW as written. "
    "Luck Shot dested Lucky Shot. "
    "RLR dested Run Luke, Run!. "
    "Gunrunner dested Rebel Gunrunner. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Bill dested as written. Username blank. "
    "LIGHT/DARK empty; dest Dark from Hunt Down True. "
    "HD dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "BAD dested BAD as written. "
    "PD dested Prepared Defenses. "
    "Ni Cha dested Ni Chuba Na?. "
    "E Shed dested Endor Shield. "
    "GOTM dested Gift Of The Master. "
    "ASP dested A Sith's Plans. "
    "Cor SE dested Coruscant. "
    "Back Door dested Endor: Back Door. "
    "Bridge dested Blockade Flagship: Bridge. "
    "Garindan dested Garindan. "
    "Black Lead dested Juno Eclipse, Black Leader. "
    "Galen SA dested Galen Marek, Starkiller. "
    "Dr E + PB dested Dr. Evazan & Ponda Baba. "
    "Dengar w Gun dested Dengar With Blaster Carbine. "
    "Victory dested Victory. "
    "Galen Saber VG dested Galen's Lightsaber, Vader's Gift. "
    "Jade Saber dested Mara Jade's Lightsaber. "
    "S+PF dested Stop Motion. "
    "WTOAOT dested Wipe Them Out, All Of Them. "
    "POTJ dested Presence Of The Force. "
    "POTF dested POTF as written. "
    "B Rack dested Blaster Rack. "
    "Emp Pow dested Emperor's Power. "
    "Light Def dested Lightsaber Deficiency. "
    "S+PS dested Sniper & Dark Strike. "
    "M Move dested Masterful Move. "
    "WL+TEB dested Weapon Levitation & The Empire's Back. "
    "Force Lightning line 54 True / line 55 empty kept split. "
    "Maul dested Darth Maul. "
    "WOTAS shield dested Weapon Of A Sith. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Tatooine: Bluffs"),
    n("Tatooine: Cantina"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Yoda, Great Warrior"),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Artoo", True),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("Ellorrs Madak"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Chewbacca, Protector"),
    n("Chewbacca, Protector"),
    n("Chewie, Enraged", True),
    n("Chewie, Enraged"),
    n("Luke Skywalker", True),
    n("Luke With Lightsaber"),
    n("Luke With Lightsaber"),
    n("Luke With Lightsaber"),
    n("Chewbacca's Bowcaster"),
    n("Han With Heavy Blaster Pistol"),
    n("Artoo-Detoo In Red 5"),
    n("Artoo-Detoo In Red 5"),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("Projection Of A Skywalker"),
    n("Nick Of Time", True),
    n("Imperial Atrocity", True),
    n("Flash", True),
    n("Draw Their Fire"),
    n("A Jedi's Fail"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Jedi Levitation", True),
    n("Throw"),
    n("HMBHT", True),
    n("EWYW", True),
    n("Control & Tunnel Vision"),
    n("Houjix"),
    n("Houjix"),
    n("Escape Pod", True),
    n("Escape Pod", True),
    n("Escape Pod", True),
    n("Lucky Shot", True),
    n("Use The Force"),
    n("Run Luke, Run!", True),
    n("Run Luke, Run!", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership", True),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", True),
    n("Rebel Leadership", True),
    n("Rebel Gunrunner"),
    n("On The Edge"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Your Ship?"),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("BAD", True),
    n("Prepared Defenses", True),
    n("Ni Chuba Na?", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("A Sith's Plans"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Endor"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Garindan", True),
    n("P-59"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("General Nevar"),
    n("Galen Marek, Starkiller"),
    n("Galen Marek, Starkiller"),
    n("Galen Marek, Starkiller"),
    n("Emperor Palpatine"),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Boba Fett, Bounty Hunter"),
    n("Blizzard 4"),
    n("Blizzard 4"),
    n("Rogue Shadow"),
    n("Victory"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Mara Jade's Lightsaber"),
    n("Stop Motion", True),
    n("Wipe Them Out, All Of Them", True),
    n("Presence Of The Force"),
    n("Protocol Failure"),
    n("POTF"),
    n("No Escape"),
    n("Blaster Rack", True),
    n("Emperor's Power", True),
    n("One Beautiful Thing"),
    n("Lightsaber Deficiency", True),
    n("Cold Feet", True),
    n("Sniper & Dark Strike"),
    n("Masterful Move"),
    n("Masterful Move"),
    n("Ghhhk"),
    n("We Must Accelerate Our Plans"),
    n("We Must Accelerate Our Plans"),
    n("We Must Accelerate Our Plans"),
    n("Weapon Levitation & The Empire's Back"),
    n("Sith Fury", True),
    n("Force Lightning", True),
    n("Force Lightning"),
    n("Force Push", True),
    n("Sense"),
    n("Mara Jade With Lightsaber"),
    n("Emperor Palpatine"),
    n("Darth Maul"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Do They Have A Code Clearance?"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
