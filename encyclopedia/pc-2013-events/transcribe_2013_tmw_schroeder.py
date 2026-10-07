#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Olaf Schroeder Xerox Hunt Down / Plead My Case."""
from __future__ import annotations

PLAYER = "Olaf Schroeder"
USERNAME = "Joe Freedom"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 39
DS_PAGE = 38
LS_SCAN = "2013 Texas Mini Worlds Day 1 p39 Olaf Schroeder LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p38 Olaf Schroeder DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Olaf Schroeder. Username Joe Freedom. "
    "Deck Name Senate Redemption. LIGHT checked. Event TX MINI. "
    "Do not dest as a new person. Do not rewrite TMW Gamble leftover "
    "or Hendon Plead My Case leftover. "
    "Plead My Case To The Sen dested Plead My Case To The Senate / "
    "Sanity And Compassion. "
    "Coruscant (SE) dested Coruscant: Galactic Senate. "
    "Senate crossed, Cor Gal Senate dested Coruscant: Galactic Senate. "
    "Squad Assignments dested Squadron Assignments. "
    "Heading For The Med Frig dested Heading For The Medical Frigate. "
    "Naboo Boss Nass Chamber dested Naboo: Boss Nass' Chambers. "
    "Han Chewie And The Fal dested Han, Chewie, And The Falcon. "
    "Artoo Detoo In Red 5 crossed with no replacement skipped. "
    "Red Squad 7 dested Red Squadron 7. "
    "Alderaan Consular Ship dested Alderaan Consular Ship. "
    "Wedge in Red Squad 1 dested Wedge In Red Squadron 1. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1. "
    "Artoo, Brave Little Droid dested Artoo, Brave Little Droid. "
    "Lando Calrissian, Scoun dested Lando Calrissian, Scoundrel. "
    "Bail Organa, FoR dested Bail Organa. "
    "Sen Mon Mothma dested Senator Mon Mothma. "
    "Sen Padme Amidala dested Senator Padme Amidala. "
    "Qui-Gon Jinn w/ LS dested Qui-Gon Jinn With Lightsaber. "
    "Our Most Desp Hour dested Our Most Desperate Hour. "
    "All Wings In & DS dested All Wings Report In & Darklighter Spin. "
    "Are U Brain Dead? dested Are You Brain Dead?!. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army. "
    "So This Is How Liberty D dested So This Is How Liberty Dies. "
    "Out of Commission & TT dested Out Of Commission & Transmission Terminated. "
    "Anger, Fear, Agg dested Anger, Fear, Aggression. "
    "Shield Anger Both crossed, Aim High dested Aim High. "
    "A Tragedy HO dested A Tragedy Has Occurred. "
    "Let's Keep A Little Opt dested Let's Keep A Little Optimism Here. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Ultimatum crossed, Do or Do Not dested Do, Or Do Not. "
    "Weapon Disp dested Weapons Display. "
    "Your Insight dested Your Insight Serves You Well. "
    "Form extra 37-38 labeled 39-40 are unique Qui-Gon copies. "
    "Unique overcounts sheet-accurate: Coruscant: Galactic Senate x2, "
    "Han, Chewie, And The Falcon x2, Redemption x3, "
    "Qui-Gon Jinn With Lightsaber x3, Might Of The Republic x2, "
    "All Wings Report In & Darklighter Spin x2, Are You Brain Dead?! x3. "
    "Bail Organa / Senator Leia Organa / Our Most Desperate Hour / "
    "Rebel Leadership checkbox splits kept as separate copies. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Olaf Schroeder. Username Joe Freedom. "
    "Deck Name Search & Destroy. DARK checked. Event TX Mini. "
    "Do not dest as a new person. Do not rewrite TMW Gamble leftover "
    "or Alperstein Hunt Down leftover. "
    "Hunt Down And Destroy The Jedi dested Hunt Down And Destroy The Jedi / "
    "Their Fire Has Gone Out Of The Universe. "
    "Gift of the Mentor dested Gift Of The Master. "
    "Ni Chuba Na? dested Ni Chuba Na??. "
    "Naboo: Theed Palace Courty dested Naboo: Theed Palace Courtyard. "
    "Trophy of a Kill dested Trophy Of A Kill. "
    "Vader's LS dested Vader's Lightsaber. "
    "Cyborg Commander's LS dested Grievous' Lightsabers. "
    "Galen's LS, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Galen's Fighter dested Rogue Shadow. "
    "Cyborg Commander, HoJ dested Grievous, Hunter Of Jedi. "
    "Emperor Palp dested Emperor Palpatine. "
    "Galen, SA dested Galen Marek, Starkiller. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Mara Jade w/ LS dested Mara Jade With Lightsaber. "
    "4-LOM w dested 4-LOM With Concussion Rifle. "
    "Boba Fett, BH dested Boba Fett, Bounty Hunter. "
    "Dr Evazan + PB dested Dr. Evazan & Ponda Baba. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Myn Kyneusk dested Myn Kyneusk as written. "
    "Gardindar dested Garindan. "
    "We Must Acc Our Plans dested We Must Accelerate Our Plans. "
    "Masterful Move & Endor Occ dested Masterful Move & Endor Occupation. "
    "Weapon Lev + TEB dested Weapon Levitation & The Empire's Back. "
    "Search + Destroy dested Search And Destroy. "
    "Knowledge and Defense dested Knowledge And Defense. "
    "Alleg of Corrupt dested Allegations Of Corruption. "
    "Come Here You Big C dested Come Here You Big Coward. "
    "Imperial Dominion dested Imperial Dominion as written. "
    "You Cannot Hide For dested You Cannot Hide Forever. "
    "Form extra 37-38 are unique Black Leader / Myn Kyneusk. "
    "Unique overcounts sheet-accurate: Trophy Of A Kill x2, Victory x2, "
    "Emperor Palpatine x2, Galen Marek, Starkiller x3, "
    "Darth Vader, Dark Lord Of The Sith x3, We Must Accelerate Our Plans x2, "
    "Force Field x2, Grievous, Hunter Of Jedi x2. "
    "Weapon Levitation & The Empire's Back checkbox split kept as separate copies. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Strike Planning"),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("Coruscant: Galactic Senate"),
    n("Heading For The Medical Frigate"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo"),
    n("Kiffex"),
    n("Chandrila"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Red Squadron 7", True),
    n("Bright Hope", True),
    n("Alderaan Consular Ship", True),
    n("Wedge In Red Squadron 1", True),
    n("Gold Leader In Gold 1", True),
    n("Redemption", True, qty=3),
    n("Artoo, Brave Little Droid", True),
    n("Lando Calrissian, Scoundrel"),
    n("Keir Santage"),
    n("Bail Organa", True),
    n("Bail Organa"),
    n("Senator Leia Organa", True),
    n("Senator Leia Organa"),
    n("General Calrissian"),
    n("Corran Horn"),
    n("General Crix Madine"),
    n("Luke Skywalker", True),
    n("Admiral Ackbar", True),
    n("Senator Mon Mothma", True),
    n("Senator Padme Amidala", True),
    n("Qui-Gon Jinn With Lightsaber", qty=3),
    n("Plo Koon", True),
    n("A Jedi's Resilience"),
    n("Our Most Desperate Hour", True),
    n("Our Most Desperate Hour"),
    n("Might Of The Republic", qty=2),
    n("All Wings Report In & Darklighter Spin", True, qty=2),
    n("Are You Brain Dead?!", qty=3),
    n("Wesa Gotta Grand Army"),
    n("Insurrection"),
    n("Bacta Tank"),
    n("So This Is How Liberty Dies", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Jedi Levitation", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses"),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("A Sith's Plans"),
    n("Naboo: Theed Palace Courtyard"),
    n("Endor"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Trophy Of A Kill", True, qty=2),
    n("Vader's Lightsaber", True),
    n("Grievous' Lightsabers", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Maul's Sith Infiltrator"),
    n("Victory", True, qty=2),
    n("Rogue Shadow", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Emperor Palpatine", qty=2),
    n("Galen Marek, Starkiller", True, qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber", True),
    n("General Nevar"),
    n("Battle Droid Squad", True),
    n("4-LOM With Concussion Rifle", True),
    n("Boba Fett, Bounty Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("Juno Eclipse, Black Leader", True),
    n("Myn Kyneusk", True),
    n("Garindan", True),
    n("Vader's Obsession"),
    n("Revenge Of The Sith", True),
    n("Masterful Move"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Field", True, qty=2),
    n("A Sith's Weapon", True),
    n("No Escape"),
    n("Elis Helrot"),
    n("Imperial Justice", True),
    n("Blaster Rack", True),
    n("Search And Destroy"),
    n("Ghhhk"),
    n("Grievous, Hunter Of Jedi", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Imperial Dominion", True),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever"),
    n("Weapon Of A Sith"),
]
DS_ADD = []
