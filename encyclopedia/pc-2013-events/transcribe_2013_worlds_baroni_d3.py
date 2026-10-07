#!/usr/bin/env python3
"""2013 World Championship Day 3: Steve Baroni Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2013 Worlds Day 3 p02 Steve Baroni LS.png"
DS_SCAN = "2013 Worlds Day 3 p01 Steve Baroni DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni dested Steve Baroni. "
    "Username blank. Deck name blank. LIGHT/DARK boxes empty. Event Day 3. "
    "T. Slave Quarters dested Tatooine: Slave Quarters. "
    "Either Way You Win dested Either Way, You Win. "
    "Final Combat You Lost / Humble One dested We Have A Plan / "
    "They Will Be Lost And Confused. "
    "Lucky Shot dested Lucky Shot. Nick of Time dested Nick Of Time. "
    "Imp Atrocity dested Imperial Atrocity. "
    "Han w Blaster dested Han With Heavy Blaster Pistol. "
    "All Wings Men Combo dested All Wings Report In & Darklighter Spin. "
    "Strike Force dested Strikeforce. "
    "Control / Tunnel Vision dested Control & Tunnel Vision. "
    "Inconsequential Barriers dested Inconsequential Barriers. "
    "See The Good dested See-Threepio. "
    "LTWW dested Let The Wookiee Win. "
    "Run Luke Run dested Run Luke, Run!. "
    "Projection of Sky dested Projection Of A Skywalker. "
    "Padme Naberrie dested Padme Naberrie. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Master Kenobi dested Master Kenobi. Wokling dested Wokling. "
    "DTF dested Draw Their Fire; (V) struck dested without (V). "
    "Chewbacca's Bowcaster dested Chewbacca's Bowcaster. "
    "Rebel Gunrunner dested Rebel Gunrunner. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Luke w LS dested Luke With Lightsaber. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Chewie Protector dested Chewbacca, Protector; (V) struck dested without (V). "
    "Threepio w Parts dested Threepio With His Parts Showing. "
    "Shmi dested Shmi Skywalker. Leia's RP dested Leia, Rebel Princess. "
    "Emp Han dested Han Solo. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Obi Wan dested Obi-Wan With Lightsaber. "
    "Have One With Them dested Home One: War Room. "
    "Tatooine Cantina dested Tatooine: Cantina. "
    "Tatooine EP1 dested Tatooine (Coruscant). "
    "AFA dested Anger, Fear, Aggression. "
    "Tragedy dested A Tragedy Has Occurred. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "DDTA dested Don't Do That Again. "
    "Let's Keep A Little dested Let's Keep A Little Optimism Here. "
    "He Can Go About dested He Can Go About His Business. "
    "WA dested Wise Advice. "
    "Insight Serves dested Your Insight Serves You Well. "
    "Obi Your Self dested Only Jedi Carry That Weapon. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni dested Steve Baroni. "
    "Username blank. Deck name blank. LIGHT/DARK boxes empty. Event Day 3. "
    "HD V dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Back door dested Executor: Docking Bay. "
    "Blockade Bridge dested Blockade Flagship: Bridge. "
    "Gift of Master dested Gift Of The Master. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Coruscant SE dested Coruscant. Imp City dested Coruscant: Imperial City. "
    "Sith's Plans dested A Sith's Plans. "
    "Prep Defenses dested Prepared Defenses. "
    "DTF dested A Dark Time For The Rebellion. "
    "SSRFT dested Short Range Fighters & Watch Your Back!. "
    "Wipe Them Out All of Them dested Wipe Them Out, All Of Them. "
    "I Have … dested I Have You Now. "
    "Omni for The Force dested Ommni Box & It's Worse. "
    "Masterful Move dested Masterful Move. "
    "Revenge of Sith dested Revenge Of The Sith. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Galen's Saber, Vader's dested Galen's Lightsaber, Vader's Gift. "
    "Emp Palpatine dested Emperor Palpatine. "
    "Dengar w Blaster dested Dengar With Blaster Carbine. "
    "Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "DuDlots dested Droideka. "
    "Galen Secret App dested Galen, Secret Apprentice. "
    "Grand Thrawn dested Grand Admiral Thrawn. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Dr E & Ponda dested Dr. Evazan & Ponda Baba. "
    "Boba Fett BH dested Boba Fett, Bounty Hunter. "
    "Grand Moff Tarkin dested Grand Moff Tarkin. "
    "Emp Mara dested Mara Jade, The Emperor's Hand. "
    "Galen's Fighter dested Rogue Shadow. "
    "KLA dested Knowledge And Defense. "
    "Useless Gesture dested A Useless Gesture. "
    "We'll Let Fate dested We'll Let Fate-A Decide, Huh?. "
    "Weapon of Sith dested Weapon Of A Sith. "
    "Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "Opp Enforcement dested Oppressive Enforcement. "
    "YCHF dested You Cannot Hide Forever. "
    "Allegations dested Allegations Of Corruption. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Either Way, You Win", True),
    n("Yoda", True),
    n("Flash Of Insight", True, qty=2),
    n("We Have A Plan / They Will Be Lost And Confused", True),
    n("Lucky Shot", True),
    n("Nick Of Time", True),
    n("Imperial Atrocity", True),
    n("Han With Heavy Blaster Pistol", True),
    n("All Wings Report In & Darklighter Spin", True),
    n("Strikeforce", True),
    n("Control & Tunnel Vision"),
    n("Inconsequential Barriers"),
    n("See-Threepio", True, qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("Projection Of A Skywalker"),
    n("Houjix", qty=2),
    n("Escape Pod", True, qty=3),
    n("Padme Naberrie", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Communing", True),
    n("Master Kenobi", True),
    n("Wokling", True),
    n("Draw Their Fire"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Gunrunner", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Luke Skywalker", True),
    n("Luke With Lightsaber", qty=2),
    n("Chewie, Enraged", True, qty=2),
    n("Chewbacca, Protector", qty=2),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Leia, Rebel Princess"),
    n("Han Solo"),
    n("Corran Horn"),
    n("Yoda, Great Warrior", True),
    n("Admiral Ackbar", True),
    n("Obi-Wan With Lightsaber", True),
    n("Home One: War Room"),
    n("Tatooine: Cantina"),
    n("Tatooine (Coruscant)"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("Aim High", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("Battle Plan", True),
    n("Wise Advice", True),
]
LS_ADD = [
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Endor"),
    n("Executor: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Endor Shield", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans", True),
    n("Prepared Defenses", True),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure", True),
    n("A Dark Time For The Rebellion"),
    n("Cold Feet", True),
    n("Short Range Fighters & Watch Your Back!", True),
    n("Wipe Them Out, All Of Them", True),
    n("I Have You Now"),
    n("One Beautiful Thing", True),
    n("Ommni Box & It's Worse"),
    n("Masterful Move", qty=2),
    n("Ghhhk"),
    n("Monnok"),
    n("Revenge Of The Sith", True),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("No Escape"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Push", True),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Emperor Palpatine", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Droideka", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("General Veers", True),
    n("Grand Admiral Thrawn"),
    n("P-59"),
    n("Juno Eclipse, Black Leader", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Bounty Hunter"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade, The Emperor's Hand", True),
    n("Rogue Shadow", True),
    n("Victory", True),
    n("Blizzard 4", qty=3),
    n("Knowledge And Defense"),
    n("Dengar With Blaster Carbine", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("We'll Let Fate-A Decide, Huh?"),
    n("Death Star Sentry", True),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
]
DS_ADD = [
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Fanfare"),
]
