#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Peter Grouty.

Source: 2012NationalsDay1.pdf pages 17–18 (handwritten 2010 Xerox, 12 shields).
Name Peter Grouty dested Peter Grouty as written. Username blank.
p17 Dark Tatooine (Coruscant).
p18 Light Watch Your Step.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Peter Grouty"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 18
DS_PAGE = 17
LS_SCAN = "2012 US Nationals Day 1 Peter Grouty LS.png"
DS_SCAN = "2012 US Nationals Day 1 Peter Grouty DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form. Username blank. Event Date 6/9/12."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Peter Grouty dested Peter Grouty as written. Username blank. "
    "LIGHT checked. Deck Name blank. Event Date 6/9/12 Event Name blank. "
    "Do not dest as a new person. Analog generate empty dest as written. "
    "Do not dest as Peter Srodoski. Do not dest as Peter Tenneson. Do not dest as Peter Huderich. "
    "WYS / TPCBATR dested Watch Your Step / This Place Can Be A Little Rough True analog leftover Veasey. "
    "General Solo dested analog leftover Murray. "
    "CEC dested leftover_xerox. Spaceport City dested leftover_xerox. "
    "No Questions Asked dested analog leftover Cooleo. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover Pinto. "
    "Luke Skywalker JTR dested Luke Skywalker, Jedi Knight analog leftover Booker. "
    "BoShek dested BoShek, Brash Smuggler analog leftover Shannon. "
    "Pulejo Peshad dested Paljo Recbed leftover_xerox. "
    "Dash Rendar dested analog leftover. "
    "General Crix Madine dested analog leftover Murray. "
    "Sergeant Bruckman dested analog leftover Veasey. "
    "Melas dested analog leftover O'Hare. "
    "BoShek's Modified Light Freighter dested BoShek's Modified Freighter analog leftover Howland. "
    "K'lor'slug & Commando Training dested Commando Training & K'lor'slug analog leftover Lepine. "
    "Antilles combo dested Antilles Maneuver & Rebel Reinforcements analog leftover Grant. "
    "All Wings combo dested All Wings Report In & Darklighter Spin analog leftover Veasey. "
    "It's not my fault dested It's Not My Fault! True analog leftover Anderson. "
    "Run Luke Run dested Run Luke, Run! analog leftover Hilbun. "
    "A few maneuvers dested A Few Maneuvers analog leftover Srodoski. "
    "Anger Fear dested Anger, Fear, Aggression analog leftover Bali. "
    "Shield Don't Do That dested Don't Do That Again True analog leftover. "
    "Shield Yavin Sentry dested analog leftover Marty. "
    "Additional Jabba's Prize dested leftover_xerox. "
    "True vs empty kept separate. Unique 60. Shields 11 slot 12 blank skip."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Peter Grouty dested Peter Grouty as written. Username blank. "
    "DARK checked. Deck Name blank. Event Date 6/9/12 Event Name blank. "
    "Do not dest as a new person. Analog generate empty dest as written. "
    "Tatooine (Coruscant) dested analog leftover Cullen START. "
    "Combat Readiness dested analog leftover Richards. "
    "Combat Response dested analog leftover Graham. "
    "Power of the Hutt dested Power Of The Hutt analog leftover Hodur. "
    "Breached Defenses & Molator dested analog leftover Ziagos. "
    "Nothing Can Get Through Our Shield dested leftover_xerox. "
    "Jabba's Space Cruiser dested leftover_xerox. "
    "Maul's Sith Infiltrator dested analog leftover Ziagos. "
    "Punishing One dested leftover_xerox. "
    "Stinger dested analog leftover Schoenthal. "
    "Out Hoth dested leftover_xerox. "
    "They're Still Coming Through dested leftover_xerox. "
    "None Shall Pass dested analog leftover Ziagos. True vs empty kept separate. "
    "SABLE-YEP dested Sable-Yep leftover_xerox. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back! analog leftover Anderson. "
    "Masterful Move dested Masterful Move & Endor Occupation analog leftover Marlow. "
    "Something Special dested Something Special Planned For Them analog leftover Wirfs. "
    "4-LOM dested 4-LOM With Concussion Rifle analog leftover Ziagos. "
    "IG-88 dested IG-88 With Riot Gun analog leftover Bordier. "
    "Probot dested analog leftover Anderson. "
    "Garindan dested analog leftover Wirfs. "
    "Boba Fett dested Boba Fett, Bounty Hunter analog leftover. "
    "Prison Xinx dested Prisoner 8059 leftover_xerox. "
    "Gela Yeosa dested leftover_xerox. "
    "Chelluk dested leftover_xerox. "
    "Ghhhk Gleeorst dested leftover_xerox. "
    "Thuk & Thus dested leftover_xerox. "
    "Mandalorian Father dested Jango Fett, The Assassin analog leftover. "
    "Knowledge dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Shield Code Clearance dested Do They Have A Code Clearance? True analog leftover Anderson. "
    "Shield Come To Me dested leftover_xerox analog leftover Cooleo. "
    "True vs empty kept separate. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("General Solo", True),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("CEC", True),
    n("Strike Planning"),
    n("Insurrection & Aim High"),
    n("No Questions Asked", True, qty=3),
    n("Chewie", True),
    n("Lando", True),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("BoShek, Brash Smuggler", True),
    n("Wedge Antilles"),
    n("Paljo Recbed"),
    n("Dash Rendar"),
    n("Hire Fett"),
    n("Mirax Terrik"),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Melas"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Home One: Docking Bay"),
    n("Red Squadron 1"),
    n("Outrider"),
    n("BoShek's Modified Freighter"),
    n("Luke's Lightsaber"),
    n("X-wing Laser Cannon"),
    n("Menace Fades"),
    n("Commando Training & K'lor'slug", True),
    n("Corellian Retort", True),
    n("Corellian Retort"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=3),
    n("Jedi Levitation", True),
    n("Dodge"),
    n("Run Luke, Run!"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Rebel Barrier", qty=3),
    n("Like Dirt", qty=2),
    n("Punch It!", qty=2),
    n("A Few Maneuvers"),
    n("It's Not My Fault!", True),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Chasm"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Jabba's Prize", True),
]

DS_START = "Tatooine (Coruscant)"
DS_CARDS = [
    n("Tatooine (Coruscant)"),
    n("Combat Readiness", True),
    n("Tatooine: Jabba's Palace"),
    n("Combat Response", True),
    n("Power Of The Hutt"),
    n("Breached Defenses & Molator"),
    n("Nothing Can Get Through Our Shield", True, qty=2),
    n("Jabba's Space Cruiser", True),
    n("Maul's Sith Infiltrator"),
    n("Punishing One", True),
    n("Stinger", True),
    n("Out Hoth", True),
    n("Jabba's Palace: Lower Passages"),
    n("Jabba's Palace: Audience Chamber"),
    n("Elis Helrot"),
    n("They're Still Coming Through!", qty=2),
    n("None Shall Pass", True, qty=2),
    n("None Shall Pass"),
    n("Sable-Yep"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Collateral Damage"),
    n("Scum And Villainy"),
    n("Hutt Bounty", True),
    n("Something Special Planned For Them", True),
    n("Search And Destroy"),
    n("Tatooine Occupation", qty=2),
    n("Ghhhk"),
    n("Force Push", True),
    n("Arica", True),
    n("4-LOM With Concussion Rifle", True),
    n("OOM-9", True),
    n("Guri"),
    n("P-59"),
    n("IG-88 With Riot Gun"),
    n("Probot"),
    n("Garindan", True),
    n("Boba Fett, Bounty Hunter"),
    n("J'quille", True),
    n("Zuckuss", True),
    n("Bane Malar", True),
    n("Prisoner 8059"),
    n("Ephant Mon"),
    n("Dengar", True),
    n("Mara Jade With Lightsaber"),
    n("Gela Yeosa", True),
    n("Boelo"),
    n("Snoova"),
    n("Chelluk"),
    n("Ghhhk Gleeorst"),
    n("Jabba The Hutt", True),
    n("Thuk & Thus"),
    n("Darth Maul"),
    n("Jango Fett, The Assassin"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Come To Me", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
