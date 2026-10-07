#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Steve Izzo Xerox Contract Killers. Light unpublished."""
from __future__ import annotations

PLAYER = "Steve Izzo"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 25
DS_PAGE = 25
LS_SCAN = ""
DS_SCAN = "2013 Texas Mini Worlds Day 1 p25 Steve Izzo DS.png"
LS_NOTE = (
    "No Light sheet in the Day 1 PDF for Steve Izzo. Hub Light stays empty."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Steve Izzo. Username blank. "
    "Deck Name blank. Event Date and Event Name blank. LIGHT/DARK boxes empty. "
    "No Light sheet. Hub Light stays empty. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "Trophy of a Kill dested Trophy Of A Kill. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. "
    "Barrier dested Imperial Barrier. "
    "Sonic Bomb dested Sonic Bombardment. "
    "Imbalance Combo dested Imbalance & Kintan Strider. "
    "Galen dested Galen Marek, Starkiller. "
    "Sniper Combo dested Sniper & Dark Strike. "
    "Lightsaber Def dested Lightsaber Deficiency. "
    "Abyssin Orn dested Abyssin Ornament. "
    "Slave I Symbol dested Slave I, Symbol Of Fear. "
    "Dannik Jerriko dested Dannik Jerriko. "
    "Death Mark + Bounty dested Death Mark & Hutt Bounty. "
    "EPP Mara dested Mara Jade With Lightsaber. "
    "YAB dested You Are Beaten. "
    "Galen's Gaunt Saber dested Galen's Lightsaber, Vader's Gift. "
    "Dark Jedi Saber dested Dark Jedi Lightsaber. "
    "keder dested Keder The Black. "
    "Kel Maliss dested Ket Maliss. "
    "Boba PH dested Boba Fett, Prepared Hunter. "
    "Jango dested Jango Fett, The Assassin. "
    "MM Combo dested Masterful Move & Endor Occupation. "
    "Proto Fail dested Protocol Failure. "
    "Prepared Def dested Prepared Defenses. "
    "Palp's Quarters dested Coruscant: Palpatine's Quarters. "
    "Cor Casino dested Coruscant: Casino. "
    "Sub City Lair dested Coruscant: Sub City Lair. "
    "I've lost Artoo dested I've Lost Artoo!. "
    "Velken dested Velken Tezeri. "
    "K+D dested Knowledge And Defense. "
    "Coward dested Come Here You Big Coward. "
    "Oppressive Enf dested Oppressive Enforcement. "
    "Sentry dested Death Star Sentry. "
    "YCHF dested You Cannot Hide Forever. "
    "Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "There is No Try dested There Is No Try. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "Allegations dested Allegations Of Corruption. "
    "Form left column reprints 37-38 on extra 37-38 are Boba Fett, Prepared Hunter "
    "and Jango Fett, The Assassin. "
    "Unique overcounts sheet-accurate: Trophy Of A Kill x3, Imperial Barrier x2, "
    "Sonic Bombardment x3, Galen Marek, Starkiller x3, Abyssin Ornament x3, "
    "Mara Jade With Lightsaber x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Trophy Of A Kill", qty=3),
    n("Disarmed"),
    n("Zuckuss In Mist Hunter"),
    n("Imperial Barrier", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("One Beautiful Thing"),
    n("Imbalance & Kintan Strider"),
    n("Galen Marek, Starkiller", qty=3),
    n("Sniper & Dark Strike"),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True),
    n("Aurra Sing", True),
    n("Bane Malar", True),
    n("Cold Feet", True),
    n("On The Hunt"),
    n("Coruscant"),
    n("Force Field", True),
    n("Abyssin Ornament", True, qty=3),
    n("Slave I, Symbol Of Fear"),
    n("Dannik Jerriko"),
    n("Stop Motion"),
    n("Death Mark & Hutt Bounty"),
    n("Mara Jade With Lightsaber", qty=2),
    n("Sith Fury", True),
    n("You Are Beaten"),
    n("A Sith's Weapon"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dark Jedi Lightsaber"),
    n("Keder The Black"),
    n("Ket Maliss"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Ghhhk"),
    n("Guri"),
    n("Masterful Move & Endor Occupation"),
    n("Protocol Failure"),
    n("Aurra Sing"),
    n("Prepared Defenses"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Casino"),
    n("Coruscant: Sub City Lair"),
    n("Nal Hutta"),
    n("I've Lost Artoo!", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Guild Of Assassins"),
    n("Blaster Rack", True),
    n("Velken Tezeri", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("After Her!"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Firepower"),
    n("Death Star Sentry"),
    n("You Cannot Hide Forever"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("A Useless Gesture"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Abyss"),
    n("Do They Have A Code Clearance?"),
]
DS_ADD = [
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
]
