#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Rustin Sharer informal LS+DS."""
from __future__ import annotations

PLAYER = "Rustin Sharer"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 84
DS_PAGE = 83
LS_SCAN = "2013 Match Play Championship p84 Rustin Sharer LS.png"
DS_SCAN = "2013 Match Play Championship p83 Rustin Sharer DS.png"
LS_NOTE = (
    "Informal handwritten list on a custom Obi-Wan overlay form (not a 2010 Xerox Print Form). "
    "Player name Rustin Sharer M.D. Event MPC, 26 January 2013. "
    "Deck title Why is it so Cold?!. Light. "
    "HFTMF dested Heading For The Medical Frigate. "
    "I'll Handle This (V) / Build Path (V) dested We'll Handle This (V) / Duel Of The Fates (V). "
    "Cor: JCC dested Coruscant: Jedi Council Chamber. "
    "Republic logistes dested Republic Logistics. A Jedi's Plan dested A Jedi's Plans. "
    "Sai tor kal fas dested Sai'torr Kal Fas. Menace Fades as written. "
    "Sense + Uncertain Is The Future kept as written (Dark combo title on the Light sheet). "
    "Speak ē Jedi council dested Speak With The Jedi Council. SATM + Blaster Prof. dested "
    "Sorry About The Mess & Blaster Proficiency. NOOOOOOOOOOOO! as written. "
    "Nabrun Leids as written. Cor: Jedi Archives dested Coruscant: Jedi Archives. "
    "Cor: Senate Landing Platform dested Coruscant: Senate Landing Platform. "
    "Cor: Night Club dested Coruscant: Night Club. Qui-gon ē Saber dested Qui-Gon Jinn With Lightsaber. "
    "Ki-Adi-Mundi as written. Obi-Wan, Jedi Knight dested Obi-Wan Kenobi, Jedi Knight. "
    "Yoda, SCM dested Yoda, Senior Council Member. Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "AFA dested Anger, Fear, Aggression. "
    "(V) from a written v / checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Informal handwritten list on a custom Obi-Wan overlay form (not a 2010 Xerox Print Form). "
    "Player name Rustin Sharer M.D. Event MPC, 26 January 2013. "
    "Deck title Emperor's hit Squad. Dark. "
    "According To My Design as written. Gift of the Master dested Gift Of The Master. "
    "Coruscant (SE) dested Coruscant. Cor: Sub city Car dested Coruscant: Sub City Lair. "
    "Contract Killers / Feard Thru galaxy dested Contract Killers / Feared Throughout The Galaxy. "
    "Death Mark + Hutt Bounty dested Death Mark & Hutt Bounty. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. Thrawn's Pet dested Thrawn's Ysalamir. "
    "Cor: Casino dested Coruscant: Casino. Dane Malar, Spice Addict dested Bane Malar, Spice Addict. "
    "Ket Maliss, Shadow Killer as written. Volker Tezeri dested Prince Xizor. "
    "The Mando, Papa Fett dested Jango Fett, The Assassin. IG88 ē Riot gun dested IG-88 With Riot Gun. "
    "Mara Jade, The Emp. Hand dested Mara Jade, The Emperor's Hand. Galen dested Galen Marek, Starkiller. "
    "Aurra Sing as written. Mara Jade's Saber dested Mara Jade's Lightsaber. "
    "Galen's Saber, Vader's gift dested Galen's Lightsaber, Vader's Gift. "
    "Black Sun Fleet as written. Elis in Anthar dested Mist Hunter. ZEMH dested Zuckuss In Mist Hunter. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Cloud City Sec. Tower dested Cloud City: Security Tower. Abyssin Orn. dested Abyssin Ornament. "
    "Sense + Uncertain Is Future dested Sense & Uncertain Is The Future. "
    "Alter (Cor) dested Alter (Coruscant). Imp. Propaganda dested Imperial Propaganda. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Leave Them to me dested Leave Them To Me. "
    "I Fnd your lack of Faith Dist dested I Find Your Lack Of Faith Disturbing. "
    "There Is No Try struck on shield 3; Fanfare remains. CHYBC dested Come Here You Big Coward. "
    "(V) from a written v / checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("Heading For The Medical Frigate"),
    n("We'll Handle This / Duel Of The Fates", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Your Insight Serves You Well"),
    n("Quick Draw"),
    n("Republic Logistics"),
    n("A Jedi's Plans"),
    n("Sai'torr Kal Fas", True),
    n("Honor Of The Jedi"),
    n("Menace Fades"),
    n("Draw Their Fire"),
    n("Civil Disorder", True),
    n("A Disturbance In The Force"),
    n("Imperial Atrocity", True),
    n("Disarmed"),
    n("Evacuation Control", True),
    n("Sense & Uncertain Is The Future", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Smoke Screen", qty=3),
    n("A Jedi's Resilience", qty=3),
    n("Jedi Levitation", True),
    n("Seeking An Audience", True),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("NOOOOOOOOOOOO!", True),
    n("Nabrun Leids", qty=2),
    n("Blaster Deflection", qty=2),
    n("It Could Be Worse"),
    n("Clash Of Sabers"),
    n("Let The Wookiee Win", qty=2),
    n("Coruscant: Jedi Archives"),
    n("Coruscant: Senate Landing Platform"),
    n("Coruscant: Night Club"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Ki-Adi-Mundi", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Jedi Advisor", True, qty=2),
    n("Depa Billaba"),
    n("Plo Koon"),
    n("Mace Windu", True),
    n("Yoda, Senior Council Member", True),
    n("Maris Brood, Fallen Jedi"),
    n("Jedi Survivor"),
    n("Elegant Lightsaber", qty=2),
    n("Jedi Lightsaber", qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Affect Mind"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("According To My Design"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Guild Of Assassins"),
    n("Coruscant"),
    n("Coruscant: Sub City Lair"),
    n("Emperor Palpatine"),
    n("On The Hunt"),
    n("Contract Killers / Feared Throughout The Galaxy", True),
    n("Death Mark & Hutt Bounty"),
    n("Nal Hutta"),
    n("Blaster Rack", True),
    n("Evacuate?", True),
    n("Sniper & Dark Strike"),
    n("You Are Beaten"),
    n("Thrawn's Ysalamir"),
    n("Coruscant: Casino"),
    n("Trophy Of A Kill", qty=2),
    n("Bane Malar, Spice Addict"),
    n("Ket Maliss, Shadow Killer"),
    n("Prince Xizor", True),
    n("Guri"),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Jango Fett, The Assassin"),
    n("IG-88 With Riot Gun"),
    n("P-59"),
    n("Mara Jade, The Emperor's Hand"),
    n("Arica", True),
    n("Galen Marek, Starkiller", qty=2),
    n("Aurra Sing", qty=2),
    n("Mara Jade's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dark Jedi Lightsaber"),
    n("Black Sun Fleet"),
    n("Mist Hunter", True),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Sonic Bombardment", True, qty=3),
    n("Cloud City: Security Tower", True),
    n("Abyssin Ornament", True, qty=3),
    n("Sense & Uncertain Is The Future", qty=2),
    n("Sense", qty=2),
    n("Alter (Coruscant)", True),
    n("Force Lightning"),
    n("A Dark Time For The Rebellion", True, qty=3),
    n("Imperial Propaganda", True, qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Leave Them To Me", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever"),
    n("A Useless Gesture", True),
    n("Secret Plans"),
]
DS_ADD = []
