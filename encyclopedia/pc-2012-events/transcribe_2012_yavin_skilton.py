#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Steve Skilton.

Source: Yavin42012.pdf pages 5–8 typed GEMP dumps.
p05–p06 Light Name Steve S. (LS) / p07–p08 Dark Name Steve S. (DS)
dested Steve Skilton analog leftover generate_2013_mpc.py CANON Steve S. /
player-stubs/Steve_Skilton.wiki / transcribe_2012_mpc_skilton.py /
transcribe_2012_tmw_skilton.py.
Username blank. Facing pair analog leftover Cooleo.
Pack player-stubs/Steve_Skilton.wiki.
Do not dest as Steve Baroni / Steve Harpster / Steve Sanders / Steve Izzo.
Do not dest as a new person Steve S.
Do not dest 2012 TMW / 2012 MPC Steve Skilton 60s again.
Do not dest Yavin p05–p06 Light 60s again.
"""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 5
DS_PAGE = 7
LS_SCAN = "2012 Yavin 4 Regionals Steve Skilton LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Steve Skilton DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p05–p06 Light / p07–p08 Dark typed GEMP dumps 1 of 2 / 2 of 2. "
    "Name Steve S. dested Steve Skilton analog leftover generate_2013_mpc.py CANON Steve S. "
    "Username blank. Print footer 7/2/2012 11:39 AM dest notes. "
    "Do not dest as Steve Baroni / Harpster / Sanders / Izzo. "
    "Do not dest as a new person Steve S. "
    "Do not dest 2012 TMW / 2012 MPC Steve Skilton 60s again. "
    "Do not dest Yavin p05–p06 Light 60s again. "
    "Pack player-stubs/Steve_Skilton.wiki."
)
LS_NOTE = (
    "Typed GEMP dump p05–p06 Light 1 of 2 / 2 of 2. Name Steve S. (LS) dested Steve Skilton "
    "analog leftover generate_2013_mpc.py CANON Steve S. Username blank. "
    "Print footer 7/2/2012 11:39 AM dest notes. "
    "Do not dest as Steve Baroni / Harpster / Sanders / Izzo. "
    "Do not dest as a new person Steve S. "
    "(1 starting) on shields dest LS_SHIELDS analog leftover light_frank. "
    "(1 starting) on cards dest IN THE 60 analog leftover light_frank. "
    "Concentrate All Fire (x2) dested qty=2 analog leftover dump. "
    "Chewbacca, Walking Carpet (x2) dested qty=2 analog leftover dump. "
    "Sergeant Doallyn (V) dested True. "
    "Corran Horn (x2) dested qty=2 analog leftover TYPE_OVERRIDE Character. "
    "Boushh (x2) dested qty=2 analog leftover Westergard. "
    "Rebel Agent (x3) dested qty=3 analog leftover dump. "
    "Lando Calrissian, Scoundrel (x2) dested qty=2 analog leftover Westergard. "
    "Yavin Sentry (V) dested True analog leftover typical shield. "
    "Chasm (V) dested True analog leftover Scott. "
    "Scoundrel's Luck / Ingenuity / Bravado / Charm (1 starting) dested IN THE 60 analog leftover light_frank. "
    "Rebel Gunrunner (1 starting) dested IN THE 60 analog leftover dump. "
    "StrikeForce (V) dested Strikeforce True analog leftover TYPE_OVERRIDE. "
    "Wokling (V) (1 starting) dested IN THE 60 True analog leftover light_frank. "
    "K'lor'slug (V) dested True analog leftover dump. "
    "Anger, Fear, Aggression (V) (1 starting) dested IN THE 60 True analog leftover light_frank. "
    "Power Pivot (x3) dested qty=3 analog leftover dump. "
    "Escape Pod (V) (x2) dested qty=2 True analog leftover TYPE_OVERRIDE Device. "
    "Armed And Dangerous & Krayt Dragon Howl dested analog leftover combo. "
    "All Wings Report In & Darklighter Spin (x2) dested qty=2 analog leftover light_frank. "
    "Heading For The Medical Frigate (1 starting) dested IN THE 60 analog leftover light_frank. "
    "Nar Shaddaa: Undercity (1 starting) dested IN THE 60 analog leftover dump. "
    "<>Spaceport Scoundrels Guild dested Spaceport Scoundrels Guild analog leftover TYPE_OVERRIDE. "
    "Nar Shaddaa (1 starting) dested IN THE 60 analog leftover dump. "
    "Infiltration/Unlikely Allies (1 starting) dested Infiltration / Unlikely Allies analog leftover Herold. "
    "Red Squadron 7 (V) dested True analog leftover TYPE_OVERRIDE Starship. "
    "Enhanced Proton Torpedoes (V) (1 starting) dested IN THE 60 True analog leftover dump. "
    "Unique 60 shields 12."
)
DS_NOTE = (
    "Typed GEMP dump p07–p08 Dark 1 of 2 / 2 of 2. Name Steve S. (DS) dested Steve Skilton "
    "analog leftover generate_2013_mpc.py CANON Steve S. Username blank. "
    "Print footer 7/2/2012 11:39 AM dest notes. Facing p05–p06 Light analog leftover Cooleo. "
    "Do not dest as Steve Baroni / Harpster / Sanders / Izzo. "
    "Do not dest as a new person Steve S. "
    "(1 starting) on shields dest DS_SHIELDS analog leftover light_frank. "
    "(1 starting) on cards dest IN THE 60 analog leftover light_frank. "
    "***Rodian (V) dested Rodian True analog leftover dump. "
    "The Mandalorian, Father Of Fett (x2) dested Jango Fett, The Assassin qty=2 analog leftover Anderson. "
    "Aurra Sing (V) (AI) (x2) dested Aurra Sing True qty=2 analog leftover dump unique variant. "
    "Ket Maliss, Shadow Killer dested analog leftover Yanaga. "
    "Arica (V) (x2) dested qty=2 True analog leftover dump. "
    "Galen, Secret Apprentice (x3) dested qty=3 analog leftover Massung. "
    "Trophy Of A Kill (x3) dested qty=3 analog leftover dump Device section. "
    "I've Lost Artoo! (V) dested I've Lost Artoo True analog leftover Foth. "
    "On The Hunt (1 starting) dested IN THE 60 analog leftover Yanaga. "
    "You Cannot Hide Forever dested IN THE 60 analog leftover dump. "
    "A Sith's Weapon dested analog leftover TYPE_OVERRIDE. "
    "Guild of Assassins (1 starting) dested Guild Of Assassins IN THE 60 analog leftover Yanaga. "
    "Gift Of The Master (1 starting) dested IN THE 60 analog leftover light_frank. "
    "Blaster Rack (V) dested True analog leftover TYPE_OVERRIDE. "
    "Knowledge And Defense (V) (1 starting) dested IN THE 60 True analog leftover Foth. "
    "Death Mark & Hutt Bounty dested analog leftover dest as written combo. "
    "Sniper & Dark Strike dested analog leftover Brist. "
    "Sonic Bombardment (V) (x3) dested qty=3 True analog leftover dump. "
    "Imperial Barrier (x2) dested qty=2 analog leftover Scott. "
    "Masterful Move & Endor Occupation dested analog leftover Brist. "
    "Abyssin Ornament (V) (x3) dested qty=3 True analog leftover Yanaga. "
    "Prepared Defenses (1 starting) dested IN THE 60 analog leftover light_frank. "
    "Coruscant: Sub City Lair (1 starting) dested IN THE 60 analog leftover dump. "
    "Cloud City: Security Tower (V) dested True analog leftover dump. "
    "Coruscant (1 starting) dested IN THE 60 analog leftover dump. "
    "Contract Killers/Feared Throughout The Galaxy dested Contract Killers / Feared Throughout The Galaxy analog leftover Yanaga. "
    "Slave I, Symbol Of Fear dested analog leftover Brady. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover dump. "
    "Weapon Of A Sith dested analog leftover light_frank shield. "
    "Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Concentrate All Fire", qty=2),
    n("Chewbacca, Walking Carpet", qty=2),
    n("Dash Rendar"),
    n("Sergeant Doallyn", True),
    n("Mirax Terrik"),
    n("Corran Horn", qty=2),
    n("Captain Han Solo"),
    n("Boushh", qty=2),
    n("Han With Heavy Blaster Pistol"),
    n("Rebel Agent", qty=3),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Scoundrel's Luck"),
    n("Scoundrel's Ingenuity"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Charm"),
    n("Rebel Gunrunner"),
    n("Strikeforce", True),
    n("Imperial Navigation Charts"),
    n("Wokling", True),
    n("K'lor'slug", True),
    n("Squadron Assignments"),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Anger, Fear, Aggression", True),
    n("Power Pivot", qty=3),
    n("Protector"),
    n("Houjix"),
    n("Dark Approach", True),
    n("A Few Maneuvers"),
    n("Escape Pod", True, qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Weapon Levitation"),
    n("Heading For The Medical Frigate"),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Nar Shaddaa: Undercity"),
    n("Nar Shaddaa: Undercity Street"),
    n("Spaceport Scoundrels Guild"),
    n("Nar Shaddaa"),
    n("Infiltration / Unlikely Allies"),
    n("Booster's Star Destroyer"),
    n("Millennium Falcon"),
    n("Red Squadron 7", True),
    n("Outrider"),
    n("Leia's Blaster Rifle"),
    n("Rebel Agent's Blaster Rifle"),
    n("Enhanced Proton Torpedoes", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Bane Malar", True),
    n("Rodian", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin", qty=2),
    n("Aurra Sing", True, qty=2),
    n("Ket Maliss, Shadow Killer"),
    n("Arica", True, qty=2),
    n("Guri"),
    n("Galen, Secret Apprentice", qty=3),
    n("Trophy Of A Kill", qty=3),
    n("Jabba's Haven"),
    n("I've Lost Artoo", True),
    n("No Escape"),
    n("On The Hunt"),
    n("You Cannot Hide Forever"),
    n("A Sith's Weapon"),
    n("Guild Of Assassins"),
    n("Gift Of The Master"),
    n("Disarmed"),
    n("Blaster Rack", True),
    n("Protocol Failure"),
    n("Knowledge And Defense", True),
    n("Death Mark & Hutt Bounty"),
    n("Sniper & Dark Strike"),
    n("You Are Beaten"),
    n("Ghhhk"),
    n("Lightsaber Deficiency", True),
    n("Sonic Bombardment", True, qty=3),
    n("Cold Feet", True),
    n("Operational As Planned", True),
    n("One Beautiful Thing"),
    n("Imperial Barrier", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Abyssin Ornament", True, qty=3),
    n("Force Field", True),
    n("Prepared Defenses"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Sub City Lair"),
    n("Coruscant: Casino"),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Coruscant"),
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dark Jedi Lightsaber", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
