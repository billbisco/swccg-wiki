#!/usr/bin/env python3
"""2012 Match Play Championship Day 2 Xerox: Brian Fred.

Source: 2012mpcday2.pdf pages 7–8 (2010 form, 12 shields).
Name Brian Fred dested Brian Fred analog leftover 2013 SoCal / Worlds Fred.
Username blank. p07 Light ADM is GOD. p08 Dark Executor: Med Chamber.
Do not dest as Brian Field. Do not dest as a new person.
Do not rewrite Day 1 leftover Field Hunt Down / Watch Your Step.
Do not rewrite 2013 leftover Fred 60s.
Pack player-stubs/Brian_Fred.wiki.
"""
from __future__ import annotations

PLAYER = "Brian Fred"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Match Play Championship Day 2.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2012 Match Play Championship Day 2 Brian Fred LS.png"
DS_SCAN = "2012 Match Play Championship Day 2 Brian Fred DS.png"
LS_DECK_NAME = "ADM is GOD"
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Fred dested Brian Fred analog leftover. "
    "Username blank. Event MPC Day 2. Deck Name ADM is GOD. LIGHT. "
    "Do not dest as Brian Field. Do not dest as a new person. "
    "Do not rewrite Day 1 leftover Field Watch Your Step. "
    "Do not rewrite 2013 leftover Fred Watch Your Step / Mind What You Have Learned. "
    "Captain Yularen With Blaster dested Captain Yutani With Blaster Cannon analog leftover. "
    "Well handle this dested We'll Handle This / Duel Of The Fates analog leftover Angelo IN THE 60 AND START. "
    "Clinging to the Edge True dested Clinging To The Edge True analog leftover Johns. "
    "A Presence in the Force dested as written. "
    "Artoo in red 5 dested Artoo-Detoo In Red 5 analog leftover Field. "
    "Flash of Insight True dested analog leftover. "
    "Qui-Gon Jinn Jedi Master dested Qui-Gon Jinn, Jedi Master analog leftover. "
    "Mace Windu True dested analog leftover Angelo. "
    "Blast the door kid dested Blast The Door, Kid! analog leftover. "
    "Yoda Muto dested Yoda, Senior Council Member analog leftover Angelo. "
    "or this thing dested as written. "
    "Jedi res dested A Jedi's Resilience analog leftover SoCal Fred. "
    "Luke's Bionic Hand dested analog leftover. "
    "I thought generally Cut dested as written. "
    "Wesa dested Wesa Gotta Grand Army analog leftover SoCal Fred. "
    "LSJK dested Luke Skywalker, Jedi Knight analog leftover Harpster. "
    "Both Shuttle / Rescue from dested The Bith Shuffle & Desperate Reach analog leftover. "
    "I did it dested I Did It! analog leftover Brummett. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Harpster. "
    "Luke's Saber dested Luke's Lightsaber analog leftover. "
    "Jedi Saber True dested Jedi Lightsaber True analog leftover Angelo. "
    "Hear me baby hold together True dested Hear Me Baby, Hold Together True analog leftover Baroni. "
    "Swing and a miss dested as written. "
    "Luke SITF dested Luke Skywalker, Strong In The Force analog leftover Angelo. "
    "Death Star Presence dested Jedi Presence analog leftover Brentson. "
    "Bess Maya Hut dested as written. "
    "fallen generals dested Maris Brood, Fallen Jedi analog leftover Sharer. "
    "Podrace Arena dested Tatooine: Podrace Arena analog leftover Lingrell. "
    "Sai'torr dested Sai'torr Kal Fas analog leftover Angelo. "
    "HCF dested Han, Chewie, And The Falcon analog leftover Harpster. "
    "Oh Wan Kenobi True dested Obi-Wan Kenobi, Jedi Knight True analog leftover Angelo. "
    "Andress freq dested as written. "
    "Another prisoner dested Insidious Prisoner analog leftover. "
    "Control / Tunnel dested Control & Tunnel Vision analog leftover Field. "
    "Army Put Your Weapons True dested Away Put Your Weapon True analog leftover Billetta. "
    "On your mark True dested as written. "
    "AFA True dested Anger, Fear, Aggression True analog leftover IN THE 60. "
    "AFA empty and AFA True kept separate. "
    "Shield Yavin Sentry True dested analog leftover Harpster. "
    "Shield Ultimatum True dested analog leftover. "
    "Shield Only Jedi Carry That Weapon dested analog leftover Bordier. "
    "Shield Do or do not dested Do, Or Do Not analog leftover Murray. "
    "Shield Wise Advice dested analog leftover. "
    "Shield Another pathetic lifeform True dested analog leftover. "
    "Shield Aim High True dested analog leftover. "
    "Shield Prof True dested The Professor True analog leftover Harpster. "
    "Shield Tragedy dested A Tragedy Has Occurred analog leftover Harpster. "
    "Unique overcounts sheet-accurate. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Fred dested Brian Fred analog leftover. "
    "Username blank. LIGHT/DARK empty dest Dark from Executor: Med Chamber. Deck Name empty. "
    "Do not dest as Brian Field. Do not dest as a new person. "
    "Do not rewrite Day 1 leftover Field Hunt Down. "
    "Do not rewrite 2013 leftover Fred Endor Operations. "
    "Executor: Med Chamber dested Executor: Meditation Chamber analog leftover START. "
    "Bring Him Before Me not listed; dest as written without inventing the objective. "
    "Exec: Main Corridor dested Executor: Main Corridor analog leftover Walter. "
    "Exec: Control Station dested Executor: Control Station analog leftover Walter. "
    "Exec: Comm Station dested Executor: Comm Station analog leftover Walter. "
    "Exec: DB dested Executor: Detention Block analog leftover. "
    "Exec: Holotheatre dested Executor: Holotheatre analog leftover. "
    "Black Squad TIE dested Black Squadron TIE analog leftover. "
    "Flagship Executor dested Flagship Executor analog leftover Walter. "
    "YCHF dested You Cannot Hide Forever analog leftover Booker. "
    "Protocol Failure True dested analog leftover Harpster. "
    "Where are you taking this thing True dested Where Are You Taking This ... Thing? True analog leftover Harpster. "
    "Why Didn't You Tell Me True dested analog leftover Lepine. "
    "Ghhhk & TRWEU dested Ghhhk & Those Rebels Won't Escape Us analog leftover. "
    "Never Yalnal dested Nevar Yalnal analog leftover TMW Banger. "
    "Imp Stockpile dested Imperial Stockpile analog leftover Amato. "
    "Concussion Missile True dested Concussion Missiles True analog leftover. "
    "Tractor dested Tractor Beam analog leftover. "
    "Combat dested Combat Readiness analog leftover Richards. "
    "Galactic Dominator dested as written. "
    "Tinnelini / Dark Strike dested Sniper & Dark Strike analog leftover Shaw. "
    "Prepared Defenses dested analog leftover Foth IN THE 60. "
    "I'll Take Them Myself dested analog leftover. "
    "Short Range Fighters dested analog leftover Worlds Fred. "
    "Lightsaber Deficiency True dested analog leftover Harpster. "
    "4-LOM w/ Gun True dested 4-LOM With Concussion Rifle True analog leftover Foth. "
    "Force True dested Force Field True analog leftover Harpster. "
    "Labrina True dested Labria True analog leftover. "
    "U-3PO dested analog leftover Shaw. "
    "Control / SFS dested Control & Set For Stun analog leftover SoCal Fred. "
    "K+D True dested Knowledge And Defense True analog leftover Murray IN THE 60. "
    "Shield Oppressive Enforcement dested analog leftover Bordier. "
    "Shield Useless Gesture True dested A Useless Gesture True analog leftover Harpster. "
    "Shield Coward True dested Come Here You Big Coward True analog leftover Lepine. "
    "Shield CHYBL dested Come Here You Big Coward analog leftover Booker unique overcount. "
    "Shield TINT dested There Is No Try analog leftover Harpster. "
    "Shield YCHF True dested You Cannot Hide Forever True analog leftover. "
    "Shield Fanfare True dested analog leftover Harpster. "
    "Unique overcounts sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("Captain Yutani With Blaster Cannon"),
    n("We'll Handle This / Duel Of The Fates"),
    n("Clinging To The Edge", True),
    n("A Presence In The Force"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Flash Of Insight", True),
    n("Qui-Gon Jinn, Jedi Master", qty=2),
    n("Mace Windu", True, qty=2),
    n("Blast The Door, Kid!", qty=2),
    n("Yoda, Senior Council Member", qty=3),
    n("or this thing"),
    n("A Jedi's Resilience"),
    n("Luke's Bionic Hand", qty=2),
    n("I thought generally Cut"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("The Bith Shuffle & Desperate Reach"),
    n("I Did It!"),
    n("Lando Calrissian, Scoundrel"),
    n("Luke's Lightsaber", qty=2),
    n("Alter", True),
    n("Jedi Lightsaber", True, qty=2),
    n("Inner Strength"),
    n("Dodge", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Blaster Deflection", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Swing And A Miss"),
    n("Wookiee Courage"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Jedi Presence"),
    n("Bess Maya Hut"),
    n("Maris Brood, Fallen Jedi"),
    n("Warrior's Courage"),
    n("Tatooine: Podrace Arena"),
    n("Anger, Fear, Aggression"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Sai'torr Kal Fas"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Andress freq"),
    n("Insidious Prisoner"),
    n("Control & Tunnel Vision"),
    n("Away Put Your Weapon", True),
    n("On Your Mark", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Ultimatum", True),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Another Pathetic Lifeform", True),
    n("Aim High", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Executor: Meditation Chamber"
DS_CARDS = [
    n("Executor: Meditation Chamber"),
    n("Executor: Main Corridor"),
    n("Executor: Control Station"),
    n("Executor: Comm Station"),
    n("Executor: Detention Block"),
    n("Executor: Holotheatre"),
    n("TIE Scout", qty=3),
    n("Black Squadron TIE", qty=3),
    n("TIE Interceptor", qty=4),
    n("Flagship Executor"),
    n("You Cannot Hide Forever"),
    n("Protocol Failure", True),
    n("Relentless Pursuit", qty=2),
    n("Where Are You Taking This ... Thing?", True),
    n("Why Didn't You Tell Me?", True),
    n("Flagship Operations", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Nevar Yalnal", qty=3),
    n("Flawless Marksmanship", qty=2),
    n("Imperial Stockpile"),
    n("Concussion Missiles", True),
    n("Tractor Beam"),
    n("Combat Readiness"),
    n("Galactic Dominator"),
    n("Sniper & Dark Strike", qty=2),
    n("Prepared Defenses"),
    n("I'll Take Them Myself"),
    n("Short Range Fighters"),
    n("Lightsaber Deficiency", True),
    n("Limited Resources"),
    n("Unsalvageable", qty=2),
    n("Force Push"),
    n("4-LOM With Concussion Rifle", True),
    n("Force Field", True, qty=2),
    n("Labria", True),
    n("U-3PO"),
    n("Arica"),
    n("Undercover", True, qty=3),
    n("Control & Set For Stun", qty=2),
    n("Imperial Decree", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Resistance"),
]
DS_ADD = []
