#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Erich Hawbaker.

Source: MPC-2014-Day-1-Main-Event.pdf pages 53–54 (2013 form, 15 shields).
Username Der Junker.
"""
from __future__ import annotations

PLAYER = "Erich Hawbaker"
USERNAME = "Der Junker"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 53
DS_PAGE = 54
LS_SCAN = "2014 Match Play Championship Day 1 Erich Hawbaker LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Erich Hawbaker DS.png"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username Der Junker. You Can Either Profit By This... dested "
    "You Can Either Profit By This... / Or Be Destroyed. Yoda, Great Warrior dested Yoda, "
    "Great Warrior (V). SATM & Blaster Pro dested Sorry About The Mess & Blaster "
    "Proficiency. Han's Blaster So Uncivilized dested Han's Heavy Blaster Pistol (V). "
    "(V) from checkbox. Unique overcounts sheet-accurate (Obi-Wan Kenobi (V) x3, Luke "
    "Skywalker, Strong In The Force (V) x2, Leia, Rebel Princess x2, Lando With A "
    "Vibro-Ax x2, A280 Sharpshooter Rifle (V) x2, Old Ben x3, Rebel Barrier x2, Someone "
    "Who Loves You x2, Panic (V) x2, Sorry About The Mess & Blaster Proficiency x2, Flash "
    "Of Insight (V) x2)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username Der Junker. Hunt Down And Destroy The Jedi (V) "
    "starting Objective. Knowledge And Defense (V) line 1. Galen Marek, Starkiller dested "
    "Galen Marek, Starkiller (V). Grievous, Hunter Of Jedi dested Grievous, Hunter Of Jedi "
    "(V). Ice-Heart analog already Ysanne Isard on the sheet dested Ysanne Isard (V). "
    "Galen's Lightsaber dested Galen's Lightsaber (V). Slave I, Symbol Of Fear dested "
    "Slave I, Symbol Of Fear (V). 3B3-888 dested 3B3-888. (V) from checkbox. Unique "
    "overcounts sheet-accurate (Galen Marek, Starkiller (V) x3, Lord Vader x2, Grievous, "
    "Hunter Of Jedi (V) x2, Trophy Of A Kill (V) x3, Restraining Bolt x2, Levitation "
    "Attack x3, Weapon Levitation & The Empire's Back (V) x2, Sniper & Dark Strike x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han With Heavy Blaster Pistol", True),
    n("Tatooine: Jabba's Palace"),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("I Must Be Allowed To Speak", True),
    n("Quick Draw", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("Lando With A Vibro-Ax", qty=2),
    n("Chewbacca, Protector"),
    n("Threepio With His Parts Showing"),
    n("Artoo, Brave Little Droid", True),
    n("Yoda, Great Warrior", True),
    n("Padme Naberrie", True),
    n("Anakin Skywalker, Padawan Learner", True),
    n("Shmi Skywalker"),
    n("Orrimaarko", True),
    n("Lieutenant Greeve"),
    n("Corporal Janse"),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Han's Heavy Blaster Pistol", True),
    n("A280 Sharpshooter Rifle", True, qty=2),
    n("Luke's Bionic Hand"),
    n("Tatooine Utility Belt"),
    n("Old Ben", qty=3),
    n("Rebel Barrier", qty=2),
    n("Someone Who Loves You", qty=2),
    n("Panic", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Don't Forget The Droids", True),
    n("Smoke Screen"),
    n("Keep Your Eyes Open", True),
    n("Sai'torr Kal Fas", True),
    n("Rycar Ryjerd", True),
    n("Imperial Atrocity", True),
    n("Much To Learn You Still Have", True),
    n("Lightsaber Proficiency"),
    n("A Gift"),
    n("Flash Of Insight", True, qty=2),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("Wise Advice", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans", True),
    n("If The Trace Was Correct", True),
    n("Prepared Defenses"),
    n("Endor Shield", True),
    n("Combat Response", True),
    n("Gift Of The Master", True),
    n("Hoth: Defensive Perimeter"),
    n("Kashyyyk"),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Lord Vader", qty=2),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Emperor Palpatine"),
    n("Mara Jade With Lightsaber", True),
    n("Grand Moff Tarkin", True),
    n("Ysanne Isard", True),
    n("Janus Greejatus"),
    n("4-LOM With Concussion Rifle", True),
    n("Dengar With Blaster Carbine", True),
    n("Aurra Sing, Deadly Assassin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Bane Malar", True),
    n("3B3-888"),
    n("General Nevar", True),
    n("Admiral Pellaeon", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Juno Eclipse, Black Leader", True),
    n("Zuckuss", True),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber", True),
    n("Grievous's Lightsaber", True),
    n("Aurra Sing's Blaster Rifle"),
    n("Trophy Of A Kill", True, qty=3),
    n("Restraining Bolt", qty=2),
    n("Justifier", True),
    n("Slave I, Symbol Of Fear", True),
    n("Rogue Shadow", True),
    n("Mist Hunter", True),
    n("Levitation Attack", qty=3),
    n("Weapon Levitation & The Empire's Back", True, qty=2),
    n("Sniper & Dark Strike", qty=2),
    n("Force Lightning"),
    n("Why Didn't You Tell Me?", True),
    n("Join Me", True),
    n("Blaster Rack", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans", True),
    n("There Is No Try"),
]
DS_ADD = []
