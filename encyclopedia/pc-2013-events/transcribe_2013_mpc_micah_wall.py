#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Micah Wall Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Micah Wall"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 109
DS_PAGE = 110
LS_SCAN = "2013 Match Play Championship p109 Micah Wall LS.png"
DS_SCAN = "2013 Match Play Championship p110 Micah Wall DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Micah Wall #14. Light. Dated 10/25/13; event name MPC 2013 "
    "(dested as this MPC PDF). Starting Dantooine Base Operations / More Dangerous Than You Realize. "
    "Dantooine Base - Docking Bay dested Dantooine: Base - Docking Bay. "
    "Dantooine Base Operations Center dested Dantooine: Base - Operations Center. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. Farm dested Tatooine: Lars' Moisture Farm. "
    "Lando with vibro-ax dested Lando With Vibro-Ax. Chewie with blaster rifle dested Chewie With Blaster Rifle. "
    "Don't Get Cocky dittos. Princess Leia Lost Scion dested Princess Leia, Lost Scion. "
    "Don't Underestimate Our Chances (V). Control merlot dested Control & Tunnel Vision. "
    "Form left column reprints 37–38 on lines 39–40 are Revolution and Dantooine: Base - Operations Center. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Micah Wall #14. Dark. Dated 10/25/13; event name MPC 2013. "
    "Ralltiir Operations / in the hands of dested Ralltiir Operations / In The Hands Of The Empire. "
    "Royal Guard thirteen copies as written. The Emperor (V). Lord Vader dested Lord Vader. "
    "Mara Jade, The Emperor's Hand as written. Sim Aloo as written. Janus Greejatus as written. "
    "Kir Kanos as written. Myn Kyneugh as written. Lord Sidious as written. "
    "Ralltiir: Spaceport Financial District as written. Carnor Jax, Royal Guard dested Carnor Jax. "
    "You Overestimate Their Chances (V). Insignificant Rebellion (V). "
    "Come here you big coward dested Come Here You Big Coward (V). Leave Them To Me as a shield. "
    "Form left column reprints 37–38 on lines 39–40 are Presence Of The Force and Ralltiir: Supply Route. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Dantooine Base Operations / More Dangerous Than You Realize"
LS_CARDS = [
    n("Luke Skywalker, Rebel Scout", qty=3),
    n("Dantooine Engineering Corps"),
    n("Obi-Wan With Lightsaber"),
    n("Dantooine: Base - Docking Bay"),
    n("Gift Of The Mentor", qty=2),
    n("Red Leader In Red 1"),
    n("Obi-Wan Kenobi"),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Corran Horn"),
    n("Leia With Blaster Rifle"),
    n("Han Solo", True),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Han Solo, Courageous Smuggler"),
    n("Rebel Barrier", qty=2),
    n("Revolution", qty=2),
    n("Ultimatum"),
    n("Tatooine: Lars' Moisture Farm"),
    n("The Force Is Strong With This One"),
    n("Lando With Vibro-Ax"),
    n("Chewie With Blaster Rifle"),
    n("Obi-Wan's Lightsaber"),
    n("Artoo-Detoo In Red 5"),
    n("Redemption"),
    n("Gold Leader In Gold 1", qty=2),
    n("Independence"),
    n("Han, Chewie, And The Falcon"),
    n("Dantooine: Base - Operations Center", qty=2),
    n("Dantooine"),
    n("The Force Is Strong With This One", True),
    n("Skywalkers", qty=2),
    n("Rebel Banter"),
    n("Jedi Presence"),
    n("Spaceport Speeders"),
    n("Outrider"),
    n("Han With Heavy Blaster Pistol"),
    n("Dash Rendar"),
    n("Projection Of A Skywalker"),
    n("Don't Get Cocky", qty=2),
    n("Out Of Somewhere"),
    n("Heading For The Medical Frigate"),
    n("The Bith Shuffle"),
    n("Smoke Screen"),
    n("Wise Advice"),
    n("Goo Nee Tay"),
    n("Clash Of Sabers"),
    n("Princess Leia, Lost Scion"),
    n("Chewie, Enraged"),
    n("Don't Underestimate Our Chances", True),
    n("Control & Tunnel Vision"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Royal Guard", qty=13),
    n("Monnok", qty=2),
    n("Overseeing It Personally", qty=3),
    n("Ghhhk", qty=2),
    n("Abyssin Ornament", qty=2),
    n("Bad Feeling Have I"),
    n("Dark Jedi Presence", qty=2),
    n("The Emperor", True, qty=2),
    n("Darth Maul"),
    n("Lord Vader"),
    n("Grand Moff Tarkin", qty=2),
    n("Mara Jade, The Emperor's Hand"),
    n("Force Lightning", qty=2),
    n("Sim Aloo"),
    n("Janus Greejatus"),
    n("Stormtrooper Garrison"),
    n("Kir Kanos"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Myn Kyneugh"),
    n("Emperor Palpatine", qty=2),
    n("Lord Sidious"),
    n("Presence Of The Force", qty=2),
    n("Ralltiir: Supply Route"),
    n("Spaceport Prefect's Office"),
    n("Spaceport City"),
    n("Spaceport Street"),
    n("Ralltiir: Spaceport Financial District", True),
    n("Ralltiir"),
    n("Force Pike"),
    n("Twi'lek Advisor"),
    n("Carnor Jax"),
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Strategic Reserves"),
    n("Fear Is My Ally"),
    n("Imperial Arrest Order"),
    n("You Overestimate Their Chances", True),
    n("Insignificant Rebellion", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("Firepower"),
    n("Leave Them To Me"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Battle Order"),
]
DS_ADD = []
