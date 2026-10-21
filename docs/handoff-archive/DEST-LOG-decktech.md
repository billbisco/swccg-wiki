# DeckTech dest log (archived from SKILL.md 2026-10-10)

Verbatim per-deck notes written by Grok Bot / Grok Build / Claude up to 22701. Grep, don't read whole. New decks: `authoring/decktech-decks/<id>.json` `notes` in billbisco/swccg-wiki.

[[DeckTech decks]] dests Stephen Skilton's [SWCCG Decktech Archives](https://www.stephenskilton.com/decktech_archives/).
`www.stephenskilton.com/decktech_archives/` and `stevetotheizz0.github.io/decktech_archives/` are the **same GitHub Pages site** (www CNAME → stevetotheizz0.github.io; github.io 301 to the custom domain).
Dest FROM Skilton UTF-8 posts.
Live decktech.net is the July 2022 PC recast (`swccgpc/decktech.net`) of that dump on the original 1999 domain; catalog is the same 3,923 posts (ids 3–26555).
Cite live `http://www.decktech.net/starwarsccg/deck/{id}` (singular) + Skilton + GitHub Pages + a working Wayback.
Inventory `wiki/decktech-inventory.json`: 3,923 deck posts and 1,406 tournament-report URLs.
Listing Light/Dark tags are unreliable (Shaw Hunt Down 26555 tagged Light).
**Dest title:** `{Event} {Player} {Published title}` for tournament dests when the post names the deck (published casing).
Worked example: [[2002 World Championship Greg Shaw Force Lightning is TECH]]; Shaw Light is [[2002 World Championship Greg Shaw DCon2k2 Runner Up - LS]]; [[2002 Origins Open Ken Cross Squires Origins Profit]]; [[Matthew Harrison-Trainor Secret Siths Profit]]; [[2002 Vegas DPC Brian Hunter LS Senate done RIGHT aka Ghhhks Away]]; [[2002 Alderaan Regionals Clayton Atkin Atkins’ Alderaan 2nd Place TDIGWATT]]; [[2002 Yavin 4 Regionals Kevin Elia 2002 Yavin 4 regional 2nd Place- I Am Jacks Anger]].
Keep a vulgar published title **off** dest TITLE; dest `{Event} {Player} {DS|LS}` instead (Consoli 26297 stays [[2002 World Championship Angelo Consoli DS]]; original post heading may still show the published string).
Tournament dest without a usable published title stays `{Event} {Player} {DS|LS}`.
Redirect the old `{Event} {Player} {DS|LS}` title after a rename.
Non-tournament dest title is `{Player} {Published title}` (worked [[Mike Stevens ls senate]], [[Jacob Taylor Jacob's Profit aka Big Trouble]], [[Dunya Ertan beefed up profit]], [[Chris Burnett My senate]], [[Taylor Hayward A Hidden Base Deck]], [[Dennis Jeffris Rebel Strike Team - Da Non-Bomb]], [[Dunya Ertan we dont need a sticking hypergenerator]], [[Jason Herrin Voice of the council solid]], [[Taylor Hayward Agents In The Court]], [[Dunya Ertan power of Rebel strike team]], [[Thomas Papp HDADTJ aka there are no Jedi alive]], [[Sam Diamond The CIA Is Trying To Kill Me]], [[Drew Scott BHBM how to kill combat]], [[Jacob Taylor Jacob's BHBM aka Blame Canada]], [[Lewis Blake YEEeeah I've got the Hoth (Big) Blues Baby]], [[Taylor Hayward I like blowin sht up]], [[Peter Jurcovic There Are Those Droidekas]], [[Peter Jurcovic Hold Me Thrill Me Kiss Me Kill Me]], [[Keith Watabayashi G-Scum]], [[Daniel Blackford Rock The Projects]], [[Vjeko Keskic My Keskic Is This Deal Legal aka The Croatian Deal v2 1]], [[Justin Fiedler we will reveal ourselves to the jedi at last we will have revenge]], [[Greg Zinn Shes Virtually Back]], [[Maximilien Bouchard Fear Will Keep Them In Line (V) ALPHA]], [[John Irving 3B3-888 Superstar aka Agents of pure BS]], [[Ryan McLain The Rx Throne Room Wrex]], [[Steve Marshall Viperstyle - Keeping The Senators Out Forever]], [[Justin Warren Raging Bull (Hoostino's Hunt Down Hammer)]], [[David Burnett JediGamler's Watto aka The Unstoppable Machine]], [[Kyle Krueger the beast on the beach v2]], [[Seth Van Winkle Seth's Mad Huntdown Deck]], [[Pyry Nystrom Empire is virtually back]], [[Bill Kafer LSC TacoBill style]], [[Kyle Krueger The Beast on the Beach]], [[Mike (Quione) Saber combat my way]], [[Matt Carulli Hunt Down and Revive the SCUM]], [[Chris Davis TDIGWATT/PIDAIAF CC Dark Deal Deck]], [[Chris McCoy Quiet Macking of Cloud city]], [[Mike Guarino I’m Getting Too Old For This]], [[Zach Mann What my step It’s yours I should be watching]], [[Adam Nelson Droid Deal v 1 0]], [[James Zajic die die die]], [[David Kangas QMC Clouds]], [[Matt Wehner Good PunJab Hunting]], [[Zach Mann None shall pass choke damn I guess you can]], [[Arvind Bhasker Maul’s Combat]], [[Vjeko Keskic Rumble In The Bronx With Mains]], [[Geoff Bowman BHBM - Bastard He Bit Me - Well that’s cuz you won]], [[Matt Wehner Court Of the Vile Gangsta - Limp Bizkit Style]], [[Chris Wodicka 6th place Coruscant regionals]], [[Adam McCombie Throne Room Mains So Hot Right Now]], [[Stephen Beckham Too Hot in da Hot Tub]], [[Uriah Watkins Testing Testing 1 2 3 (4 5 6)]], [[2002 Ralltiir Regionals Vjeko Keskic Court Likes Direct Damage aka Gailid Superstar]], [[Brian Hunter Saber Combat done RIGHT aka No Mans Land]], [[Quirin Fürgut Unbeatable EBO aka fun for everyone]], [[Jon Manning Cloud City trooper deck]], [[Maximilien Bouchard WYS Choke BETA]], [[Vjeko Keskic All Your Damage Belongs To Watto]], [[Vjeko Keskic H-TOWN Jedis vs NRW Jedis]], [[Mike (Quione) Rebel Strike Team- Stay the hell of endor]], [[Wes Brown Imperial Blues]], [[Cody Jewell ’Saber Combat My Way V1 00(UnRevised)]], [[Matthew Harrison-Trainor Secret Siths Profit]]).
**Original post (standard):** after the CardLink dest 60, `== Original post ==` with published title, Author (alias as posted), Published date, Rating, Description (YAML if present).
`=== Strategy ===` is wiki paragraphs; standalone matchup/section lines become `==== Heading ====`.
`=== Original card list ===` is `{| class="wikitable mw-collapsible mw-collapsed" …` caption `As posted on DeckTech`, slang 60 in `<div style="white-space:pre-wrap"><nowiki>…</nowiki></div>`, collapsed by default.
Deck info `* '''Published title:''' ''{title}''` when usable (omit when vulgar).
Keep published spelling (`tendancy`, `By thBy the way`).
Wiki is the reading copy; readers should not need Skilton's site.
2002 original-VS dests: `Prophetess (V) (Virtual Set 1)`, `Molator (V) (Virtual Set 2)`, `I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)`, `Hyperwave Scan (V) (Virtual Set 3)`, `Ket Maliss (V) (Virtual Set 3)`, `Reactor Terminal (V) (Virtual Set 3)`, `Reegesk (V) (Virtual Set 3)`, `Sai'torr Kal Fas (V) (Virtual Set 1)`, `Blaster Rack (V) (Virtual Set 1)`, `Affect Mind (V) (Virtual Set 2)`, `Escape Pod (V) (Virtual Set 2)`, `Leia's Back (V) (Virtual Set 2)`, `Yavin Sentry (V) (Virtual Set 2)`, `Fear Will Keep Them In Line (V) (Virtual Set 2)`, `Imperial-Class Star Destroyer (V) (Virtual Set 2)`, `Leia (V) (Virtual Set 3)`, `Scanner Techs (V) (Virtual Set 3)`, `Traffic Control (V) (Virtual Set 3)`, `Rodian (V) (Virtual Set 3)`, `Greedo (V) (Virtual Set 3)`, `Oo-ta Goo-ta, Solo? (V) (Virtual Set 3)`, `Cell 2187 (V) (Virtual Set 3)`, `Tarkin (V) (Virtual Set 3)`, `Luke Skywalker (V) (Virtual Set 1)`, `Imperial Reinforcements (V) (Virtual Set 2)`, `Darth Vader (V) (Virtual Set 1)`, `Commander Praji (V) (Virtual Set 2)`, `The Empire's Back (V) (Virtual Set 2)`, `Black 2 (V) (Virtual Set 1)`, `Rycar Ryjerd (V) (Virtual Set 2)`, `K'lor'slug (V) (Virtual Set 2)`, `Bo Shek (V) (Virtual Set 1)`, `Han's Heavy Blaster Pistol (V) (Virtual Set 1)` — not current-virtual V21, Virtual Block, or Virtual Shields.
Format cell is [[Premiere - Original VS3]] (skill `swccg-wiki-formats`).
Fear Is My Ally holds up to 10 cards from outside the 60; dest those separately and keep qty 60.
Krueger 26173 posted 10 Defensive Shields outside the 60 (no invented FIMA).
25033 FIMA is inside the starting 9 and counts toward 60 (do not invent Held 10).
Do not dest a DeckTech handle onto an existing `{{Card}}` title (Black 1 is Premiere Dark vs [[Justin Fiedler]]).
Tournament reports: [[DeckTech tournament reports]] — they name pairings, finishes, and sometimes a 60; dest the report and fill event hubs / player tables from it.
Helper: `wiki/generate_decktech.py` (`formatted_original_post`), `wiki/inventory_decktech.py`, post bodies `wiki/decktech-posts/{id}.txt`.
Ingest incrementally.
HANDOFF Wiki TODO: GPN remaining listing pages + Trandosite / Anagramed Decipherians.
[[Red 32's Star Wars CCG decks]] LIVE.
CEC / Plarathas dests are on [[Corellian Engineering Corporation decks]].
General rows land on [[DeckTech decks]] `== General lists ==` and player `== Miscellaneous decklists ==`.
YAML Light/Dark tags are unreliable (26448/26425/26368/25033/24965/24905/24783/24516/24511 tagged Light, bodies Dark).
Next dest: 22698 Ralltir Ops (9 Apr 2002).
22701 Darryll Silva DS LIVE (rev 64335; NEW stub Darryll Silva rev 64336; hub rev 64337; Format [[Premiere - Original VS1]] rev 64338; Claude 2026-10-10).
Published title "WifeBeater- No hold barred" kept OFF dest TITLE (author's own note says readers found it offensive) — dest {Player} DS; original post heading keeps it.
Body Dark Hoth walkers / YAML Light.
YMSYL posted under Effects dested OBJECTIVE.
Unnamed shields under FIMA dest 60 only.
Full posted→dested notes in generate_decktech.py above SILVA_DS.
22705 Casey Merry Celebration what LIVE (43838/64283; Grok Build 2026-10-09 — applied and reviewed, but the session died before this write-back; dest notes in generate_decktech.py above MERRY_LS).
22886 Mike Stevens ls senate LIVE (43836/64279; hub 41112/64281; NEW stub Mike Stevens 43837/64280).
Format [[Premiere - Original VS1]] (41588/64282).
Qty 70.
YAML Light / body Light Plead My Case To The Senate.
General dest TITLE.
No Defensive Shields listed dest 70 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect omitted.
Starting Card printed dual Plead My Case To The Senate.
Posted senator valorum dested as posted (strategy oops Palpatine).
Posted stay here where its safe dested Stay Here, Where It's Safe.
Posted kin kain dested Kin Kian.
Posted sei teria dested Sei Taria.
Posted dont get @#$%y dested Don't Get Cocky.
Posted vote now dested Vote Now!.
Posted master luke dested Luke Skywalker, Jedi Knight.
Posted x wing laser cannon dested X-wing Laser Cannon.
Posted tantive 4 dested Tantive IV.
Posted jedi prescence dested Jedi Presence.
Skip GEMP.
Handle mikezap cited; no mikezap page.
YAML author Mike "mikezap" Stevens.
Inventory author_guess was the Light tag.
Do not dest onto Chris Burnett My senate.
Do not dest onto 2002 Vegas DPC Brian Hunter LS Senate.
Do not dest onto Yoda card.
Do not dest onto Mace Windu as player.
Do not dest onto Admiral Ackbar as player.
Do not dest onto Home One as player.
Do not dest onto Coruscant Guard as player.
Do not dest onto mikezap as a new person.
Do not dest onto Senator Palpatine as the posted Senator Valorum row.
Do not dest onto inventory author_guess.
22919 2002 Yavin 4 Regionals Kevin Elia 2002 Yavin 4 regional 2nd Place- I Am Jacks Anger LIVE (43792/64222; hub 41112/64227; Kevin Elia dump-not-stub 31588/64223; Stephen Turner 43793/64224; 2002 Yavin 4 Regionals 43794/64225; List 22433/64226).
Format [[Premiere - Original VS1]] (41588/64228).
Qty 60.
YAML Dark / body Dark YMSYL walkers.
Tournament dest TITLE.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Starting Card You May Start Your Landing.
Posted YMSYL Effect dested OBJECTIVE.
Posted Ice Plains dested Hoth: Ice Plains (5th Marker).
Posted Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker).
Posted Hoth Docking Bay dested Hoth: Echo Docking Bay.
Posted Naboo Docking Bay dested Naboo: Theed Palace Docking Bay.
Posted Executor starship dested Flagship Executor.
Posted Imperial Walker dested Imperial Walker.
Posted Come Back Here You Big Coward dested Come Here You Big Coward.
Posted A Useless Gestures dested A Useless Gesture.
Posted Dr.
Evazen and Ponda Baba dested Dr.
Evazan & Ponda Baba.
Skip GEMP.
Handle KevOfCrofton cited; no KevOfCrofton page.
YAML author Kevin "KevOfCrofton" Elia.
Inventory author_guess was the description fragment.
Do not dest onto 2012 Yavin 4 Regionals.
Do not dest onto KevOfCrofton as a new person.
Do not dest onto Lewis Blake YEEeeah dest.
Do not dest onto You May Start Your Landing as player.
Do not dest onto Blizzard 4 as player.
Do not dest onto Grand Admiral Thrawn as player.
Do not dest onto Emperor Palpatine as player.
Do not dest onto Darth Maul as player.
Do not dest onto Darth Vader as player.
Do not dest onto Imperial Walker as player.
Do not dest onto AT-AT Cannon.
Do not dest onto Executor (Dark) Dagobah system.
Do not dest onto inventory author_guess.
22978 Jacob Taylor Jacob's Profit aka Big Trouble LIVE (43791/64218; hub 41112/64220; Jacob Taylor dump-not-stub 43457/64219).
Format [[Premiere - Original VS1]] (41588/64221).
Qty 60.
YAML Light / body Light Profit.
General dest TITLE.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect omitted.
Starting Card printed dual You Can Either Profit By This...
/ Or Be Destroyed.
Posted Sai?torr Kal Fas dested Sai'torr Kal Fas (V) original VS1.
Posted Run Luke, Run dested Run Luke, Run!.
Posted A Tragedy Has Occured dested A Tragedy Has Occurred.
Posted Home One Docking Bay dested Home One: Docking Bay.
Posted Ben Kenobi dested Special Edition Ben Kenobi.
Posted Qui-Gon's Lightsaber dested Reflections III.
Skip GEMP.
Handle Armaedes already cited; no Armaedes page.
YAML author Jacob "Armaedes" Taylor.
Inventory author_guess was the Light tag.
Do not dest onto You Can Either Profit By This as player.
Do not dest onto Armaedes as a new person.
Do not dest onto Sai'torr Kal Fas (V) current-virtual as player.
Do not dest onto Ben Kenobi as player.
Do not dest onto Obi-Wan Kenobi as player.
Do not dest onto Han Solo as player.
Do not dest onto Leia, Rebel Princess as player.
Do not dest onto Dunya Ertan beefed up profit.
Do not dest onto Ken Cross Origins Profit.
Do not dest onto HT Secret Siths Profit.
Do not dest onto Jacob Taylor Jacob's BHBM as player.
Do not dest onto Doug Taylor.
Do not dest onto Taylor Hayward.
Do not dest onto Justin Warren as this player.
Do not dest onto inventory author_guess.
22997 Dunya Ertan beefed up profit LIVE (43747/64160; hub 41112/64162; Dunya Ertan dump-not-stub 43557/64161).
Format [[Premiere - Original VS1]] (41588/64163).
Qty 62.
YAML Light / body Light Profit.
General dest TITLE.
Unnamed 10 shields dest 62 only.
Starting Interrupt The Signal.
Starting Effect omitted.
Starting Card printed dual You Can Either Profit By This...
/ Or Be Destroyed.
Posted profit dested printed dual.
Posted jabba palace dested Tatooine: Jabba's Palace.
Posted han dested Han Solo.
Posted jabba's palace dested Jabba's Palace: Audience Chamber.
Posted trafic control dested Traffic Control.
Posted jedis home dested Coruscant: Jedi Council Chamber.
Posted tatooine farm dested Tatooine: Lars' Moisture Farm.
Posted freon drevan dested Theron Nett.
Posted liet too veers dested Lieutenant s'Too Vees.
Posted chewie engraed dested Chewie, Enraged.
Posted i've got a bad feeling about this dested I Have A Bad Feeling About This.
Posted are u brain dead dested Are You Brain Dead?!.
Posted free ride dested Free Ride & Endor Celebration.
Posted alter combo dested Alter & Friendly Fire.
Skip GEMP.
Handle Hardpack already cited; no Hardpack page.
YAML author Dunya "Hardpack" Ertan.
Inventory author_guess was the Light tag.
Do not dest onto You Can Either Profit By This as player.
Do not dest onto Hardpack as a new person.
Do not dest onto Dunya Ertan hyper dest.
Do not dest onto Dunya Ertan RST dest.
Do not dest onto Ken Cross Origins Profit.
Do not dest onto HT Secret Siths Profit.
Do not dest onto Chris Burnett My senate.
Do not dest onto Han Solo as player.
Do not dest onto Lieutenant s'Too Vees as player.
Do not dest onto inventory author_guess.
23021 Chris Burnett My senate LIVE (43745/64156; hub 41112/64158; NEW stub Chris Burnett 43746/64157).
Format [[Premiere - Original VS1]] (41588/64159).
Qty 60.
YAML Dark / body Dark Senate.
General dest TITLE.
Unnamed D-shields dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Starting Card printed dual My Lord, Is That Legal? / I Will Make It Legal.
Posted MLITL/IWMIL dested printed dual.
Posted Tatooine Desert landing site dested Tatooine: Desert Landing Site.
Posted Corusant Glactic senate dested Coruscant: Galactic Senate.
Posted Naboo Battle plans dested Naboo: Battle Plains.
Posted this is outrageous dested This Is Outrageous!.
Posted vote now dested Vote Now!.
Posted Oh Switch off dested Oh, Switch Off.
Posted Do They Have A Code Clearance dested Do They Have A Code Clearance?.
Posted ommni box & its worse dested Ommni Box & It's Worse.
Skip GEMP.
Handle Putz cited; no Putz page.
YAML author chris "Putz" burnett.
Inventory author_guess was the Dark tag.
Do not dest onto My Lord, Is That Legal? as player.
Do not dest onto Putz as a new person.
Do not dest onto lastname Burnett.
Do not dest onto David Burnett.
Do not dest onto Emperor Palpatine as player.
Do not dest onto Lord Maul as player.
Do not dest onto Darth Maul as player.
Do not dest onto Darth Vader as player.
Do not dest onto Guri as player.
Do not dest onto P-59 as player.
Do not dest onto Peter Jurcovic Senate dest.
Do not dest onto Brian Hunter Vegas DPC Senate dest.
Do not dest onto inventory author_guess.
23033 Taylor Hayward A Hidden Base Deck LIVE (43690/64078; hub 41112/64080; Taylor Hayward dump-not-stub 43342/64079).
Format [[Premiere - Original VS1]] (41588/64081).
Qty 59 as published (Locations (7) Hidden Base Indicator duplicates Objective).
YAML Light / body Light Hidden Base.
General dest TITLE.
Unnamed Pick Any 10 shields dest 59 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Starting Card printed dual Hidden Base.
Posted Hidden Base Indicator dested Hidden Base dual.
Posted Kiffix dested Kiffex.
Posted Niem Numb dested Nien Nunb.
Posted Luke Skywalker (V) dested Luke Skywalker (V) (VS1).
Posted Stay Sharp dested Stay Sharp!.
Skip GEMP.
Handle JediMaster10 already cited; no JediMaster10 page.
YAML author Taylor "JediMaster10" Hayward.
Inventory author_guess was the description fragment.
Do not dest onto Hidden Base as player (current-virtual redirect).
Do not dest onto JediMaster10 as a new person.
Do not dest onto Luke Skywalker as player.
Do not dest onto Dash Rendar as player.
Do not dest onto Tycho Celchu as player.
Do not dest onto Wedge Antilles as player.
Do not dest onto Nien Nunb as player.
Do not dest onto Ten Numb as player.
Do not dest onto Outrider as player.
Do not dest onto Taylor Hayward I like blowin sht up.
Do not dest onto Taylor Hayward Agents In The Court as player.
Do not dest onto Dennis Jeffris RST dest.
Do not dest onto Matt Wehner Good PunJab Hunting.
Do not dest onto Wedge231 Hidden Base dest.
Do not dest onto inventory author_guess.
23036 Dennis Jeffris Rebel Strike Team - Da Non-Bomb LIVE (43688/64074; hub 41112/64076; NEW stub Dennis Jeffris 43689/64075).
Format [[Premiere - Original VS1]] (41588/64077).
Qty 60.
YAML Light / body Light Rebel Strike Team.
General dest TITLE.
Unnamed defensive shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Starting Card printed dual Rebel Strike Team.
Posted The Shiled Is Down dested The Shield Is Down!.
Posted I Hope She's Alright dested I Hope She's All Right.
Posted Threepio WHPS dested Threepio With His Parts Showing.
Posted Lando, Scoundrel dested Lando Calrissian, Scoundrel.
Posted Chewbacca of Kashyyyk dested Chewbacca Of Kashyyyk.
Posted Luke, Rebel Scout dested Luke Skywalker, Rebel Scout.
Posted All Wings Report In combo dested All Wings Report In & Darklighter Spin.
Posted Insurrection under Effects dested INTERRUPT Insurrection.
Skip GEMP.
Handle Denethor cited; no Denethor page.
YAML author Dennis "Denethor" Jeffris.
Inventory author_guess was the description fragment.
Do not dest onto Rebel Strike Team as player (current-virtual redirect).
Do not dest onto Denethor as a new person.
Do not dest onto Dunya Ertan RST dest.
Do not dest onto Mike (Quione) RST dest.
Do not dest onto Luke Skywalker as player.
Do not dest onto Leia Organa as player.
Do not dest onto Chewbacca as player.
Do not dest onto Han Solo as player.
Do not dest onto Home One as player.
Do not dest onto Wuta as player.
Do not dest onto General Crix Madine as player.
Do not dest onto inventory author_guess.
23051 Dunya Ertan we dont need a sticking hypergenerator LIVE (43643/64012; hub 41112/64014; Dunya Ertan dump-not-stub 43557/64013).
Format [[Premiere - Original VS1]] (41588/64015).
Qty 60.
YAML Light / body Light The Hyperdrive Generator's Gone.
General dest TITLE.
Unnamed (effect) u can choose and defensive shields dest 60 only.
Starting Effect Credits Will Do Fine.
Starting Interrupt omitted.
Starting Card printed dual The Hyperdrive Generator's Gone.
Posted hypergenerator is gone dested The Hyperdrive Generator's Gone.
Posted lieutnant chamberlynn dested Lieutenant Chamberlyn.
Posted ric olie dested Ric Olie.
Posted debnoli dested Deneb Both.
Posted freon orevan dested Theron Nett.
Posted alter combo dested Alter & Friendly Fire.
Posted yodas stew combo dested Houjix & Out Of Nowhere.
Skip GEMP.
Handle Hardpack already cited; no Hardpack page.
YAML author Dunya "Hardpack" Ertan.
Inventory author_guess was the Light tag.
Do not dest onto The Hyperdrive Generator's Gone as player.
Do not dest onto You Can Either Profit By This as player.
Do not dest onto Hardpack as a new person.
Do not dest onto Watto / Yoda / Qui-Gon Jinn / Obi-Wan Kenobi / Jar Jar Binks / Padme Naberrie / Sio Bibble / Lieutenant Chamberlyn / Ric Olie as players.
Do not dest onto inventory author_guess.
23087 Jason Herrin Voice of the council solid LIVE (43600/63957; hub 41112/63959; NEW stub Jason Herrin 43601/63958).
Format [[Premiere - Original VS1]] (41588/63960).
Qty 60.
YAML Light / body Light We'll Handle This.
General dest TITLE.
AUOF inside Starting counts.
Unnamed shields none posted dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Starting Card printed dual We'll Handle This.
Posted Saitor Kal Fass dested Sai'torr Kal Fas (V) original VS1.
Posted We'll Handle This dested printed dual We'll Handle This / Duel Of The Fates.
Posted Blast The Door Kid dested Blast The Door, Kid!.
Posted Qui Gon's Lightsaber R3 dested Reflections III Qui-Gon's Lightsaber.
Posted Restraining Bolt dested as published; Update 4 Scramble is strategy-only.
Skip GEMP.
Handle Mr.
Black cited; no Mr.
Black page.
YAML author Jason "Mr.
Black" Herrin.
Inventory author_guess was the description fragment.
Do not dest onto We'll Handle This as player (current-virtual redirect).
Do not dest onto Lightsaber Combat as player.
Do not dest onto Mr.
Black as a new person.
Do not dest onto Yoda as player.
Do not dest onto Qui-Gon Jinn as player.
Do not dest onto Obi-Wan Kenobi as player.
Do not dest onto Luke Skywalker as player.
Do not dest onto Mace Windu as player.
Do not dest onto Padme Naberrie as player.
Do not dest onto Darth Maul as player.
Do not dest onto Sai'torr Kal Fas as player.
Do not dest onto inventory author_guess.
23121 Taylor Hayward Agents In The Court LIVE (43598/63951; hub 41112/63953; Taylor Hayward dump-not-stub 43342/63952).
Format [[Premiere - Original VS1]] (41588/63954).
Qty 60.
YAML Light / body Light Agents In The Court.
General dest TITLE.
AUOF inside Starting counts.
Unnamed 10 shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Starting Card printed dual Agents In The Court.
Posted Uh-Oh dested Uh-oh!.
Posted Nar shadda Wind Chimes & Out Of Somewhere dested Nar Shaddaa Wind Chimes & Out Of Somewhere.
Posted Tatooine Mos Espa Docking Bay dested Tatooine: Mos Espa Docking Bay.
Posted Wookie dested Wookiee.
Posted Chewbacca (Rep) dested Premiere Chewbacca.
Skip GEMP.
Handle JediMaster10 already cited; no JediMaster10 page.
YAML author Taylor "JediMaster10" Hayward.
Inventory author_guess was the description fragment.
Do not dest onto Agents In The Court as player (wiki card page missing — dest CardLink, do not mint).
Do not dest onto JediMaster10 as a new person.
Do not dest onto Dunya Ertan.
Do not dest onto Rebel Strike Team as player.
Do not dest onto inventory author_guess.
23127 Dunya Ertan power of Rebel strike team LIVE (43556/63898; hub 41112/63900; Dunya Ertan 43557/63899).
Format [[Premiere - Original VS1]] (41588/63901).
Qty 59 as published (objective omitted from the list; author forgot Endor system and AUOF — do not invent).
YAML Light / body Light RST.
General dest TITLE.
Unnamed shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect omitted.
Starting Card printed dual RST.
Posted Leit greeve dested Lieutenant Greeve.
Posted Major hassh dested Major Haash'n.
Posted Rep ben dested Rep Been.
Posted Owen and brue combo dested Owen Lars & Beru Lars.
Posted Gold one dested Gold Squadron 1.
Posted Out of commison dested Out Of Commission.
Posted Gift of a mentor dested Gift Of The Mentor.
Posted The bith shuffle combo dested The Bith Shuffle & Desperate Reach.
Posted Jin with stick dested Qui-Gon Jinn With Lightsaber.
Posted Obi with stick dested Obi-Wan With Lightsaber.
Posted Chewbacc of kashyyyk dested Chewbacca Of Kashyyyk.
Posted Chewie with blaster dested Chewie With Blaster Rifle.
Posted Shield is down dested The Shield Is Down!.
Posted Strike planing dested Strike Planning.
Posted Home one dested Home One.
Posted Artoo in red 5 dested Artoo-Detoo In Red 5.
Skip GEMP.
Handle Hardpack cited; no Hardpack page.
YAML author Dunya "Hardpack" Ertan.
Inventory author_guess was the description fragment.
Do not dest onto Rebel Strike Team as player (current-virtual redirect).
Do not dest onto Hardpack as a new person.
Do not dest onto Luke Skywalker as player.
Do not dest onto Qui-Gon Jinn as player.
Do not dest onto Obi-Wan Kenobi as player.
Do not dest onto Jar Jar Binks as player.
Do not dest onto Endor as player.
Do not dest onto Rep Been as player.
Do not dest onto Taylor Hayward RST dest as player.
Do not dest onto Mike (Quione) RST dest as player.
Do not dest onto Thomas Papp dest as player.
Do not dest onto inventory author_guess.
23136 Thomas Papp HDADTJ aka there are no Jedi alive LIVE (43546/63882; hub 41112/63884; Thomas Papp 43547/63883).
Format [[Premiere - Original VS1]] (41588/63885).
Qty 61 as published (Interrupts labeled 15, listed 16).
YAML Dark / body Dark Hunt Down.
General dest TITLE.
FIMA inside Starting (9) counts.
Named 10 Defensive Shields dest outside 61.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Starting Card printed dual HDADTJ.
Posted HDADTJ/There are no Jedi dested Hunt Down And Destroy The Jedi.
Posted ExecutorHolotheatre dested Executor: Holotheatre.
Posted ExecutorMed.
Chamber dested Executor: Meditation Chamber.
Posted Prep.
Defenses dested Prepared Defenses.
Posted They Will B No Match 4 U dested They Will Be No Match For You.
Posted IAO/Secret Plans dested Imperial Arrest Order & Secret Plans.
Posted Mob.
Point/ You Cannot Hide Forever dested You Cannot Hide Forever & Mobilization Points.
Posted Lord Vader dested Lord Vader.
Posted DVDLOTS dested Darth Vader, Dark Lord Of The Sith.
Posted Vader w/ stick dested Darth Vader With Lightsaber.
Posted Mara Jade, TEH dested Mara Jade, The Emperor's Hand.
Posted Janus Grejatus dested Janus Greejatus.
Posted Zuckuss In Boat dested Zuckuss In Mist Hunter.
Posted Bossk In Bus dested Bossk In Hound's Tooth.
Posted Fett In S1 dested Boba Fett In Slave I.
Posted Dengar In P1 dested Dengar In Punishing One.
Posted Chimaera dested Chimaera.
Posted DB dested Executor: Docking Bay.
Posted Endor DB dested Endor: Landing Platform (Docking Bay).
Posted DS DB dested Death Star II: Docking Bay.
Posted Mara’s dested Mara Jade's Lightsaber.
Posted Maul’s dested Maul's Double-Bladed Lightsaber.
Posted Vader’s dested Vader's Lightsaber.
Posted Darth Vader’s dested Darth Vader's Lightsaber.
Posted Sniper/Dark Strike dested Sniper & Dark Strike.
Posted Ghhhk/TRWEU dested Ghhhk & Those Rebels Won't Escape Us.
Posted Weapon Lev.
dested Weapon Levitation.
Posted Masterful Move dested Masterful Move.
Posted Sec.
Prec.
dested Security Precautions.
Posted The Phantom Manace dested The Phantom Menace.
Posted You've Never Won A Podrace dested You've Never Won A Race?.
Skip GEMP.
Handle Yoda TP cited; no Yoda TP page.
YAML author Thomas "Yoda TP" Papp.
Inventory author_guess was the description fragment.
Do not dest onto Yoda card pageid 4339.
Do not dest onto Papp as a last-name-only page.
Do not dest onto Hunt Down And Destroy The Jedi as player.
Do not dest onto Darth Vader.
Do not dest onto Darth Maul.
Do not dest onto Emperor Palpatine as player.
Do not dest onto Mara Jade as player.
Do not dest onto Blizzard 4 as player.
Do not dest onto Grand Admiral Thrawn as player.
Do not dest onto Yoda TP as a new person.
Do not dest onto inventory author_guess.
23152 Sam Diamond The CIA Is Trying To Kill Me LIVE (43502/63818; hub 41112/63820; Sam Diamond 43503/63819).
Format [[Premiere - Original VS1]] (41588/63821).
Qty 60.
YAML Light / body Light QMC.
General dest TITLE.
AUOF inside Starting counts.
Unnamed shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Starting Card printed dual QMC.
Posted QMC/Balls dested Quiet Mining Colony / Independent Operation.
Posted Bespin dested Light Bespin.
Posted CC Guest Quarters dested Cloud City: Guest Quarters.
Posted An Unusual Amount of Feast (fear) dested An Unusual Amount Of Fear.
Posted Squad A$$ dested Squadron Assignments.
Posted Keeping the emp out forever dested Keeping The Empire Out Forever.
Posted Heading for the frig dested Heading For The Medical Frigate.
Posted CC slang dested colon Cloud City: titles.
Posted Luke EPP dested Luke With Lightsaber.
Posted Obi EPP dested Obi-Wan With Lightsaber.
Posted Qui Gon w/ stick dested Qui-Gon Jinn With Lightsaber.
Posted Leia EPP dested Leia With Blaster Rifle.
Posted DS2 Wedge dested Wedge Antilles, Red Squadron Leader.
Posted Lando, Scoundrel dested Lando Calrissian, Scoundrel.
Posted Han, Chewie, and Falcon dested Han, Chewie, And The Falcon.
Posted Red Squad 1 dested Red Squadron 1.
Posted Blue Squad 5 dested Blue Squadron 5.
Posted OOC/TT dested Out Of Commission & Transmission Terminated.
Posted A Jedi's Reslience dested A Jedi's Resilience.
Posted SATM/BP dested Sorry About The Mess & Blaster Proficiency.
Posted Off the Edge dested On The Edge.
Posted CC Celebration dested Cloud City Celebration.
Skip GEMP.
Handle AgentSD cited; no AgentSD page.
YAML author Sam "AgentSD" Diamond.
Inventory author_guess was the Non Phixion description fragment.
Do not dest onto CIA as player.
Do not dest onto Non Phixion as player.
Do not dest onto Quiet Mining Colony as player.
Do not dest onto AgentSD as a new person.
Do not dest onto Drew Scott.
Do not dest onto Luke Skywalker as player.
Do not dest onto Obi-Wan Kenobi as player.
Do not dest onto Qui-Gon Jinn as player.
Do not dest onto Leia Organa as player.
Do not dest onto Dash Rendar as player.
Do not dest onto Ten Numb as player.
Do not dest onto Corran Horn as player.
Do not dest onto inventory author_guess Non Phixion.
23182 Drew Scott BHBM how to kill combat LIVE (43458/63763; hub 41112/63765; Drew Scott 41620/63764).
Format [[Premiere - Original VS1]] (41588/63766).
Qty 60 as posted (objective omitted from the list).
YAML Light / body Dark BHBM.
General dest TITLE (4-0 at freedom con in strategy; do not mint Freedom Con hub; do not dest as 2001 Worlds).
FIMA inside Starting counts.
Unnamed (you pick shields) dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Starting Card printed dual BHBM.
Posted Igar dested Commander Igar.
Posted Blow parred dested Blow Parried.
Posted 4-lom dested 4-LOM.
Posted twi lek dested Twi'lek Advisor.
Posted YCHF/mob.
points dested You Cannot Hide Forever & Mobilization Points.
Posted IAO/Secret plans dested Imperial Arrest Order & Secret Plans.
Posted ponda boba/dr.
E dested Dr.
Evazan & Ponda Baba.
Posted Fett in ship dested Boba Fett In Slave I.
Posted bossk in ship dested Bossk In Hound's Tooth.
Posted zuckuss in ship dested Zuckuss In Mist Hunter.
Posted maras sabre dested Mara Jade's Lightsaber.
Posted naboo DB dested Naboo: Theed Palace Docking Bay.
Posted rendilli dested Rendili.
Posted sniper/ DS dested Sniper & Dark Strike.
Posted monnok/ evader dested Evader & Monnok.
Posted barrier dested Imperial Barrier.
Skip GEMP.
Handle drew man1 cited; no drew man1 page.
YAML author drew "drew man1" scott.
Inventory author_guess was the Light tag.
Do not dest onto Scott pageid 40447.
Do not dest onto Bring Him Before Me as player.
Do not dest onto Darth Maul.
Do not dest onto Darth Vader.
Do not dest onto Emperor Palpatine as player.
Do not dest onto Mara Jade as player.
Do not dest onto Blizzard 4 as player.
Do not dest onto Jacob Taylor.
Do not dest onto Geoff Bowman BHBM dest as player.
Do not dest onto drew man1 as a new person.
Do not dest onto inventory author_guess Light.
23249 Jacob Taylor Jacob's BHBM aka Blame Canada LIVE (43456/63759; hub 41112/63761; Jacob Taylor 43457/63760).
Format [[Premiere - Original VS1]] (41588/63762).
Qty 60.
YAML Dark / body Dark BHBM sevens.
General dest TITLE (Canada title origin is co-author Dominic Gaudreault; do not mint a tournament or Canada hub).
FIMA inside Effects (19) counts.
Named 10 Defensive Shields dest outside 60.
Unnamed none.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Starting Card printed dual BHBM.
Posted After Her dested After Her!.
Posted Drop dested Drop!.
Posted Rise My Friend dested Rise, My Friend.
Posted This Is Some Rescue dested This Is Some Rescue!.
Skip GEMP.
Handle Armaedes cited; no Armaedes page.
YAML author Jacob "Armaedes" Taylor.
Inventory author_guess was the description fragment.
Do not dest onto Bring Him Before Me as player.
Do not dest onto Darth Maul as player.
Do not dest onto Darth Vader as player.
Do not dest onto Emperor Palpatine as player.
Do not dest onto Aurra Sing as player.
Do not dest onto Blizzard 4 as player.
Do not dest onto Doug Taylor.
Do not dest onto Taylor Hayward.
Do not dest onto Geoff Bowman BHBM dest.
Do not dest onto Armaedes as a new person.
Do not dest onto inventory author_guess.
23279 Lewis Blake YEEeeah I've got the Hoth (Big) Blues Baby LIVE (43389/63672; hub 41112/63674; Lewis Blake 43390/63673).
Format [[Premiere - Original VS1]] (41588/63678).
Qty 60.
YAML Dark / body Dark YMSYL walkers.
General dest TITLE.
FIMA inside Starting counts.
Named 8 Defensive Shields dest outside 60.
Unnamed (2 more) dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Starting Card You May Start Your Landing.
Posted YMSYL dested You May Start Your Landing.
Posted Ice Plains dested Hoth: Ice Plains (5th Marker).
Posted Prepare for a SA dested Prepare For A Surface Attack.
Posted Imperial walker dested Imperial Walker.
Posted Chimera dested Chimaera.
Posted Ad Piet dested Admiral Piett.
Posted Commander Merrijk dested Commander Merrejk.
Posted 4-LOM w/ gun dested 4-LOM With Concussion Rifle.
Posted Dr.
E and PB dested Dr.
Evazan & Ponda Baba.
Posted DV with saber dested Darth Vader With Lightsaber.
Posted DM with saber dested Darth Maul With Lightsaber.
Skip GEMP.
Handle Duke Devil cited; no Duke Devil page.
Do not dest onto Admiral Piett.
Do not dest onto Grand Admiral Thrawn.
Do not dest onto General Veers.
Do not dest onto Blizzard 4 as player.
Do not dest onto Darth Vader.
Do not dest onto Darth Maul.
Do not dest onto Hoth as player.
Do not dest onto You May Start Your Landing as player.
Do not dest onto Duke Devil as a new person.
Do not dest onto inventory author_guess Dark.
23334 Taylor Hayward I like blowin sht up LIVE (43341/63613; hub 41112/63615; Taylor Hayward 43342/63614).
Format [[Premiere - Original VS1]] (41588/63616).
Qty 60.
YAML Light / body Light RST.
General dest TITLE.
Unnamed shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect omitted.
Posted Rebel Strike Team dested printed dual.
Posted Luke Skywalker dested Luke Skywalker (V) (VS1) File VS1O-05-Luke Skywalker.png.
Posted Chewbacca Of Kashyyk dested Chewbacca Of Kashyyyk.
Posted Niem Numb dested Nien Nunb.
Posted Orrimarko dested Orrimaarko.
Posted Wedge Red squad leader dested Wedge Antilles, Red Squadron Leader.
Posted Rebel Landing Platform dested Endor: Rebel Landing Site (Forest).
Skip GEMP.
Handle JediMaster10 cited; no JediMaster10 page.
YAML title keep I like blowin sht up (minced; Consoli-only vulgar-off).
Do not dest onto Rebel Strike Team as player.
Do not dest onto Luke Skywalker as player.
Do not dest onto JediMaster10 as a new person.
Do not dest onto Doug Taylor.
Do not dest onto Jacob Taylor.
Do not dest onto Mike (Quione) Rebel Strike Team- Stay the hell of endor.
Do not dest onto inventory author_guess Light.
23346 Peter Jurcovic There Are Those Droidekas LIVE (43340/63609; hub 41112/63611; Peter Jurcovic 41536/63610).
Format [[Premiere - Original VS1]] (41588/63612).
Qty 60.
YAML Light / body Dark TDIGWATT Dark Deal.
General dest TITLE (unnamed tournament prize pack).
FIMA inside Effects (10) counts.
Unnamed shields dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted TDIGWATT/Droid Manufacturing Platform dested printed dual.
Posted P59 (The Rep) dested P-59.
Posted Owo1 w/backup dested OWO-1 With Backup.
Posted Where Are Those Droidekas? dested Where Are Those Droidekas?!.
Posted Bossk in Buss dested Bossk In Hound's Tooth.
Posted Bespin Cloud City dested Bespin: Cloud City.
Posted Precision Targetting dested Precision Targeting.
Posted Dard Deal dested Dark Deal.
Skip GEMP.
Handle marvin already cited.
Do not dest onto Peter Jurcovic Hold Me Thrill Me Kiss Me Kill Me.
Do not dest onto Where Are Those Droidekas?! as player.
Do not dest onto Maul.
Do not dest onto Darth Maul.
Do not dest onto Lord Maul.
Do not dest onto Destroyer Droid as player.
Do not dest onto TDIGWATT as player.
Do not dest onto Guri as player.
Do not dest onto P-59 as player.
Do not dest onto marvin as a new person.
Do not dest onto inventory author_guess.
23385 Matthew Harrison-Trainor Secret Siths Profit LIVE (43284/63518; hub 41112/63520; Matthew Harrison-Trainor 21373/63519).
Format [[Premiere - Original VS1]] (41588/63521).
Qty 60.
YAML Light / body Light Profit.
General dest TITLE.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect omitted.
Unnamed shields dest 60 only.
Posted Profit dested printed dual You Can Either Profit By This...
/ Or Be Destroyed.
Posted BoShek (V) dested Bo Shek (V) (VS1) File VS1O-01-Bo Shek.png.
Posted Han's Heavy Blaster Pistol (V) dested Han's Heavy Blaster Pistol (V) (VS1) File VS1O-04-Hans Heavy Blaster Pistol.png.
Posted Jedi saber dested Jedi Lightsaber.
Posted Swing and A Miss dested Swing-And-A-Miss.
Posted Tatooine Docking Bay dested Tatooine: Docking Bay 94.
Posted Master Luke dested Luke Skywalker, Jedi Knight.
Posted Don't Get @#$%y dested Don't Get Cocky.
Skip GEMP.
Handle Secret Sith cited.
Do not dest onto Profit.
Do not dest onto Secret Sith as a new person.
Do not dest onto BoShek.
Do not dest onto Han's Heavy Blaster Pistol (V) current-virtual.
Do not dest onto Jedi Lightsaber as player.
Do not dest onto Bravo 2 as player.
Do not dest onto 2002 Origins Open Ken Cross Squires Origins Profit.
Do not dest onto CL.
23407 2002 Vegas DPC Brian Hunter LS Senate done RIGHT aka Ghhhks Away LIVE (43239/63457; hub 41112/63461; Brian Hunter 36782/63458; 2002 Vegas DPC 43240/63459; List 22433/63460).
Format [[Premiere - Original VS1]] (41588/63462).
Qty 60.
YAML Light / body Light Senate.
Tournament dest TITLE.
AUOF inside Starting Effect counts.
Unnamed (w/10 shields) dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted Plead My Case to the Senate/Sanity and Compassion dested printed dual.
Posted 3PO w/ His Parts Showing dested Threepio With His Parts Showing.
Posted AWRI/Darklighter Spin dested All Wings Report In & Darklighter Spin.
Posted Alter (coruscant version) dested Alter (Coruscant).
Posted Queen Amidala, Ruler of the Naboo dested Queen Amidala, Ruler Of Naboo.
Posted Ascertaining the Truth dested Ascertaining The Truth.
Posted The Gravest of Circumstances dested The Gravest Of Circumstances.
Skip GEMP.
Handle HuntaWarya already redirected.
Do not dest onto Ghhhk.
Do not dest onto Senate.
Do not dest onto Plead My Case as player.
Do not dest onto Brian Hunter Saber Combat done RIGHT aka No Mans Land.
23438 2002 Alderaan Regionals Clayton Atkin Atkins’ Alderaan 2nd Place TDIGWATT LIVE (43191/63386; hub 41112/63398; Clayton Atkin 28553/63387; 2002 Alderaan Regionals 43192/63388; List 22433/63389).
Format [[Premiere - Original VS1]] (41588/63408).
Qty 60.
YAML Dark / body Dark TDIGWATT.
Tournament dest TITLE.
FIMA inside Starting (8) counts.
Unnamed (with 10 sheilds) dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted TDIGWATT/I'm getting Shafted dested printed dual.
Posted Executor dested Flagship Executor.
Posted Black 2 dested Black 2 (V) (VS1).
Posted Prophetess (virtual) dested Prophetess (V) (VS1).
Posted Bespin Cloud City dested Bespin: Cloud City.
Posted Masterful Move & Endor Celebration dested Masterful Move & Endor Occupation.
Posted Short Range Fighters & Watch your Back dested Short Range Fighters & Watch Your Back!.
Skip GEMP.
Handle TheDohMan cited.
Do not dest onto Clayton Atkins.
Do not dest onto Atkins as player.
Do not dest onto TDIGWATT.
Do not dest onto Maul.
Do not dest onto Vader.
Do not dest onto Blizzard 4.
23458 Cody Jewell ’Saber Combat My Way V1 00(UnRevised) LIVE (43151/63323; hub 41112/63325; Cody Jewell 43152/63324).
Format [[Premiere - Original VS1]] (41588/63326).
Qty 60.
YAML Light / body Light We'll Handle This.
General dest TITLE.
AUOF inside Starting counts.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt omitted.
Starting Effect An Unusual Amount Of Fear.
Posted We'll Handle This/ Duel of the Fates dested printed dual.
Posted Sai.Torr Kal Fas dested Sai'torr Kal Fas (V) (VS1).
Posted Goo Nee Tay OR Honor OR Sai.Torr dest all three.
Posted Shocking Information/ Grimtaash dested combo wrap File.
Skip GEMP.
Handle MegaScrub cited.
Do not dest onto Mike (Quione) Saber combat my way.
Do not dest onto We'll Handle This current-virtual.
Do not dest onto Lightsaber Combat.
Do not dest onto Yoda.
Do not dest onto Qui-Gon.
Do not dest onto Luke.
Do not dest onto Obi-Wan.
Do not dest onto Sai'torr as player.
23459 Wes Brown Imperial Blues LIVE (43093/63235; hub 41112/63238; Wes Brown 43094/63236; SeaRaptor redirect 41776/63237).
Format [[Premiere - Original VS1]] (41588/63239).
Qty 60.
YAML Dark / body Dark Endor Ops.
General dest TITLE.
FIMA inside Starting (9) counts.
Unnamed DEFENSIVE SHIELDS [pick 10, any 10] dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted Endor Operations dested printed dual.
Posted Darth Vader (V) dested Darth Vader (V) (VS1).
Posted Executor starship dested Flagship Executor.
Posted Denegar in Punishing One dested Dengar In Punishing One.
Posted Endor Occupation & Masterful Move dested Masterful Move & Endor Occupation.
Posted Imperial Arrest Order dested printed.
Posted Tempest 1 dested Tempest 1.
Skip GEMP.
Handle SeaRaptor redirected to Wes Brown.
Do not dest onto SeaRaptor Imperial Blues (EOPS).
Do not dest onto Darth Maul.
Do not dest onto Darth Vader.
Do not dest onto Admiral Piett.
Do not dest onto Blizzard 4.
Do not dest onto Endor Operations as player.
23490 Mike (Quione) Rebel Strike Team- Stay the hell of endor LIVE (43042/63151; hub 41112/63153; Mike (Quione) 42159/63152).
Format [[Premiere - Original VS1]] (41588/63154).
Qty 60.
YAML Light / body Light RST.
General dest TITLE.
AUOF inside Starting counts.
Unnamed (Pick your 10) dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted Rebel Strike Team/Garrison Destroyed dested printed dual.
Posted Endor Landing Site dested Endor: Rebel Landing Site (Forest).
Posted The Shield is Down dested The Shield Is Down!.
Posted Squadren Assignments dested Squadron Assignments.
Posted Orimaarko dested Orrimaarko.
Posted Nien Numb dested Nien Nunb.
Posted Gold Squadren 1 dested Gold Squadron 1.
Posted Green Squadren 3 dested Green Squadron 3.
Posted Ill take the leader dested I'll Take The Leader.
Posted Deactivate the shield generator dested Deactivate The Shield Generator.
Skip GEMP.
Handle Quione cited.
Do not dest onto Rebel Strike Team as player.
Do not dest onto Mike Thomas.
Do not dest onto Endor as player.
23520 Vjeko Keskic H-TOWN Jedis vs NRW Jedis LIVE (43037/63134; hub 41112/63136; Vjeko Keskic 33155/63135).
Format [[Premiere - Original VS1]] (41588/63137).
Qty 60.
YAML Light / body Light We'll Handle This.
General dest TITLE (team-matchup published title; do not mint H-TOWN/NRW hubs).
AUOF inside Effects (7) counts.
Unnamed shields dest 60 only.
Starting Interrupt omitted.
Starting Effect An Unusual Amount Of Fear.
Posted We'll Handle This/Duel Of The Fates dested printed dual.
Posted Sai’torr Kal Fas dested Sai'torr Kal Fas (V) (VS1).
Posted Han With Blaster Rifle dested Han With Heavy Blaster Pistol.
Posted Inner Strengh dested Inner Strength.
Posted I Did It dested I Did It!.
Posted Interuder Missile dested Intruder Missile.
Posted Armament Dismanteld dested Armament Dismantled.
Posted Lando,Scroundel dested Lando Calrissian, Scoundrel.
Posted Run Luke,Run dested Run Luke, Run!.
Skip GEMP.
Handle mighty_maul already cited.
Do not dest onto We'll Handle This current-virtual.
Do not dest onto Yoda.
Do not dest onto Qui-Gon.
Do not dest onto Luke.
Do not dest onto Obi-Wan.
Do not dest onto Han.
Do not dest onto Leia.
Do not dest onto Sai'torr as player.
Do not dest onto 23606 Court.
23561 Vjeko Keskic All Your Damage Belongs To Watto LIVE (42992/63062; hub 41112/63064; Vjeko Keskic 33155/63063).
Format [[Premiere - Original VS1]] (41588/63065).
Qty 60.
YAML Light / body Dark Watto.
General dest TITLE.
FIMA inside Effects (8) counts.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt omitted.
Starting Effect Fear Is My Ally.
Posted No Money,No Parts,No Deal/You're A Slave dested No Money, No Parts, No Deal! / You're A Slave?.
Posted Executor starship dested Flagship Executor.
Posted Mighty Jabba dested Mighty Jabba.
Posted Ghhk dested Ghhhk.
Posted Search & Destroy dested Search And Destroy.
Posted Imperial Rest Order & Secret Plans dested Imperial Arrest Order & Secret Plans.
Posted There Is No Try in shields dested There Is No Try & Oppressive Enforcement.
Skip GEMP.
Handle mighty_maul already cited.
Do not dest onto Watto.
Do not dest onto Maul.
Do not dest onto Darth Maul.
Do not dest onto Lord Maul.
Do not dest onto No Money, No Parts, No Deal as player.
23567 Maximilien Bouchard WYS Choke BETA LIVE (42945/62876; hub 41112/62879; Maximilien Bouchard 41729/62877; Kiriel redirect 41805/62878).
Format [[Premiere - Original VS1]] (41588/62880).
Qty 60.
YAML Light / body Light WYS.
General dest TITLE (Tournement 2-0 without event name).
AUOF inside Starting (9) counts.
Unnamed 10 shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted Watch Your Step/This place can Be a little Rough dested printed dual.
Posted Threepio with His Parts Showing dested Threepio With His Parts Showing.
Posted Strike bloked dested Strike Blocked.
Posted Were are you looking for me ? dested Were You Looking For Me?.
Skip GEMP.
Handle Kiriel redirected to Maximilien Bouchard.
Do not dest onto Kiriel WYS Choke BETA GPN dest.
Do not dest onto Watch Your Step as player.
Do not dest onto Talon Karrde as player.
Do not dest onto Wedge Antilles as player.
23571 Jon Manning Cloud City trooper deck LIVE (42905/62669; hub 41112/62676; Jon Manning 42911/62675).
Format [[Premiere - Original VS1]] (41588/62678).
Qty 60.
YAML Dark / body Dark Cloud City troopers.
General dest TITLE.
Starting Effect omitted.
Unnamed shields dest 60 only.
Starting Interrupt Any Methods Necessary.
Starting Card Cloud City: Dining Room.
Posted Cloud CityDinning Room dested Cloud City: Dining Room.
Posted Seargean Merril dested Sergeant Merril.
Posted Lando Calrisian dested Lando Calrissian (Dark).
Posted 4-Lom dested 4-LOM (Dagobah).
Posted Boba Fett dested Cloud City Boba Fett.
Posted Storm Trooper Cadet dested Stormtrooper Cadet (OTSD).
Posted Den of Theives dested Den Of Thieves.
Posted Reactor Terminal dested printed Premiere.
Skip GEMP.
Handle joker_phreak cited.
Do not dest onto Cloud City Limited.
Do not dest onto Cloud City Trooper as player.
Do not dest onto Boba Fett as player.
23592 Quirin Fürgut Unbeatable EBO aka fun for everyone LIVE (42890/62651; hub 41112/62653; Quirin Fürgut 22639/62652).
Format [[Premiere - Original VS1]] (41588/62654).
Qty 60.
YAML Light / body Light EBO.
General dest TITLE.
AUOF inside Starting counts.
Unnamed 10 shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted Objective NONE; Starting Card Echo Base Operations dested dual.
Posted Imperial Barrier dested as published (author later meant Rebel Barrier).
Posted D2 Wedge dested Wedge Antilles, Red Squadron Leader.
Posted Echo War Room dested Hoth: Echo Command Center (War Room).
Posted Nar Shadda dested Nar Shaddaa Wind Chimes.
Posted Han&Chewie in Falcon dested Han, Chewie, And The Falcon.
Posted Hoth Main Power Generators dested Hoth: Main Power Generators (1st Marker).
Posted Hoth North Ridge dested Hoth: North Ridge (4th Marker).
Skip GEMP.
Handle el-diablo cited.
Do not dest onto Echo Base Operations as player.
23598 Brian Hunter Saber Combat done RIGHT aka No Mans Land LIVE (42889/62646; hub 41112/62649; Brian Hunter 36782/62647; HuntaWarya redirect 41710/62648).
Format [[Premiere - Original VS1]] (41588/62650).
Qty 60.
YAML Dark / body Dark LSC.
General dest TITLE (3 unnamed tournaments 8-0 then 11-0 after VS1; do not mint hubs).
FIMA inside Starting Effect counts.
Unnamed 10 shields dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted Executor starship dested Flagship Executor.
Posted Monnok/Evader dested Evader & Monnok.
Posted Prophetess (Virtual version) dested Prophetess (V) (VS1).
Posted Blaster Rack (virtual version) dested Blaster Rack (V) (VS1).
Posted We Must Accelerate our Plans dested printed Coruscant Dark.
Posted Theed Palace Generator dested Naboo: Theed Palace Generator.
Posted Let them make the first move dested dual.
Admiral Ozzel amendment dest as published.
Skip GEMP.
Handle HuntaWarya redirected to Brian Hunter.
Do not dest onto Maul.
Do not dest onto Darth Maul.
Do not dest onto Lord Maul.
23606 2002 Ralltiir Regionals Vjeko Keskic Court Likes Direct Damage aka Gailid Superstar LIVE (42845/62584; hub 41112/62586; Vjeko Keskic 33155/62585; 2002 Ralltiir Regionals 42846/62588; List 22433/62589).
Format [[Premiere - Original VS1]] (41588/62587).
Qty 60.
YAML Dark / body Dark Court.
Tournament dest TITLE.
FIMA inside Effects counts.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt omitted.
Starting Effect Fear Is My Ally.
Posted Court Of The Ville Gangster dested Court Of The Vile Gangster.
Posted Jabba dested Jabba The Hutt.
Posted We Must Accerlerate Our Plans dested printed Coruscant Dark.
Posted Start Your Engines dested Start Your Engines!.
Posted Scum And Villiany dested Scum And Villainy.
Posted Zukuss dested Zuckuss In Mist Hunter.
Posted We'll Let Fate-a Deside,Huh? dested We'll Let Fate-a Decide, Huh?.
Posted Allegation Of Corruption dested Allegations Of Corruption.
Posted There Is No Try in shields dested There Is No Try & Oppressive Enforcement (dump MISSING dest combo without minting).
Skip GEMP.
Handle mighty_maul already cited.
Do not dest onto Maul.
Do not dest onto Court.
Do not dest onto Gailid as player.
23661 Uriah Watkins Testing Testing 1 2 3 (4 5 6) LIVE (42802/62526; hub 41112/62528; Uriah Watkins 42803/62527).
Format [[Premiere - Original VS1]] (41588/62529).
Qty 59 as published.
YAML Light / body Light MWYHL.
General dest TITLE.
AUOF inside Starting counts.
Named 10 Defensive Shields dest outside 59.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted Sai’torr Kal Fas (Virtual) dested Sai'torr Kal Fas (V) (VS1).
Posted Mind What You Have Learned/Save You It Can dested dual.
Posted Dagobah dested Light Dagobah system.
Posted Obi-Wan’s Lightsaber (Premiere) dested Premiere.
Posted Traffic Control dested printed.
Posted Another Pathetic Lifeform in shields dested Another Pathetic Lifeform (Reflections III: A Collector's Bounty).
Skip GEMP.
Handle travler.
Do not dest onto Yoda.
Do not dest onto Jar Jar Binks.
Do not dest onto Padme Naberrie.
Do not dest onto Great Warrior.
Duplicate posts 23658/23657/23654/23653 skipped.
23798 Stephen Beckham Too Hot in da Hot Tub LIVE (42753/62466; hub 41112/62468; Stephen Beckham 42754/62467).
Format [[Premiere - Original VS2]] (41677/62469).
Qty 61 as published.
YAML Light / body Light We'll Handle This.
General dest TITLE.
AUOF inside Starting counts.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted the new virtual saber puller dested Sai'torr Kal Fas (V) (VS1).
Posted we'll handle this/duel of the fates dested We'll Handle This / Duel Of The Fates.
Posted theed palace generator dested Naboo: Theed Palace Generator.
Posted theed palace generator core dested Naboo: Theed Palace Generator Core.
Posted jedi council chamber dested Coruscant: Jedi Council Chamber.
Posted obi-wan, jedi knight dested Obi-Wan Kenobi, Jedi Knight.
Posted threepio with this parts showing dested C-3PO (See-Threepio).
Posted lando, scoundrel dested Lando Calrissian, Scoundrel.
Posted enraged chewie dested Chewie, Enraged.
Posted jar jars electopole dested Jar Jar's Electropole.
Posted shocking info/grimtaash dested Shocking Information & Grimtaash.
Posted free ride& endor celebration dested Free Ride & Endor Celebration.
Posted star destroyer dested Star Destroyer!.
Skip GEMP.
Handle Texan.
Do not dest onto Qui-Gon Jinn.
Do not dest onto Yoda.
Do not dest onto We'll Handle This current-virtual.
Do not dest onto Sense.
Do not dest onto Inner Strength.
Do not dest onto Baragwin.
23820 Adam McCombie Throne Room Mains So Hot Right Now LIVE (42751/62462; hub 41112/62464; Adam McCombie 42752/62463).
Format [[Premiere - Original VS2]] (41677/62465).
Qty 60.
YAML Light / body Light TRM.
General dest TITLE.
AUOF inside Starting counts.
Unnamed shields dest 60 only.
Starting Interrupt Heading For The Medical Frigate.
Starting Effect An Unusual Amount Of Fear.
Posted Sal'torr Kal Fas(v) dested Sai'torr Kal Fas (V) (VS1).
Posted 3-P0 with no clothes dested C-3PO (See-Threepio).
Posted OOC & Transmision Terminated dested Out Of Commission & Transmission Terminated.
Posted SATM & Blaster Proficency dested Sorry About The Mess & Blaster Proficiency.
Posted Dont Get @#$%y dested Don't Get Cocky.
Skip GEMP.
Handle kida117.
Do not dest onto Tycho Celchu.
Do not dest onto Wedge Antilles.
Do not dest onto Qui-Gon Jinn.
23830 Chris Wodicka 6th place Coruscant regionals LIVE (42705/62351; hub 41112/62354; Chris Wodicka 42706/62352; Wedge231 redirect 41975/62353; 2002 Coruscant Regionals 42707/62356; 2002 NYC Mini-Open 42708/62357).
Format [[Premiere - Original VS2]] (41677/62355).
Qty 60.
YAML Dark / body Dark ISB.
General dest TITLE (two events).
FIMA inside Start (7) counts.
Unnamed shields dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted Darth Vader (V) dested Darth Vader (V) (VS1).
Skip GEMP.
Handle Wedge231 redirected to Chris Wodicka.
Do not dest onto Wedge Antilles.
Do not dest onto Admiral Piett.
Do not dest onto Blizzard 4.
Do not dest onto Maul cards.
23843 Matt Wehner Court Of the Vile Gangsta - Limp Bizkit Style LIVE (42662/62248; hub 41112/62250; Matt Wehner dump-not-stub 36764/62249).
Format [[Premiere - Original VS2]] (41677/62251).
Qty 60.
YAML Dark / body Dark Court.
General dest TITLE.
FIMA inside Starting counts.
Unnamed shields dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted Court of The Vile Gangeter dested Court Of The Vile Gangster.
Posted Dungeon dested Jabba's Palace: Dungeon.
Posted Audience Chamber dested Jabba's Palace: Audience Chamber.
Posted Great Pit of the Sarlaac dested Tatooine: Great Pit Of Carkoon.
Posted Rancor Pitt dested Jabba's Palace: Rancor Pit.
Posted Galid dested Gailid.
Posted Master, Destroyers dested Master, Destroyers!.
Posted Molator (v) dested Molator (V) (VS2).
Skip GEMP.
Handle Tasa already cited.
Do not dest onto Court card.
Do not dest onto Rancor.
23847 Geoff Bowman BHBM - Bastard He Bit Me - Well that’s cuz you won LIVE (42614/62189; hub 41112/62191; Geoff Bowman dump-not-stub 24621/62190).
Format [[Premiere - Original VS2]] (41677/62192).
Qty 60.
YAML Dark / body Dark BHBM.
General dest TITLE.
FIMA inside Starting (9) counts.
Unnamed shields dest 60 only.
Starting Interrupt Prepared Defenses.
Starting Effect Fear Is My Ally.
Posted BHBM/TYFP dested Bring Him Before Me.
Posted Throne Room dested Death Star II: Throne Room.
Posted DVDLOTS dested Darth Vader, Dark Lord Of The Sith.
Posted Boba Fett BH dested Boba Fett, Bounty Hunter.
Posted Janus dested Janus Greejatus.
Posted Mara Jade TEH dested Mara Jade, The Emperor's Hand.
Posted Ability Ability Ability dested Ability, Ability, Ability.
Posted Sebulba?s dested Sebulba's Podracer.
Posted Mobilization Points dested printed Mobilization Points.
Skip GEMP.
Handle GG BLADE.
Do not dest onto Maul card pageid 13908.
Do not dest onto Darth Maul card pageid 6743.
Do not dest onto Lord Maul pageid 7882.
Do not dest onto Blizzard 4.
23859 Vjeko Keskic Rumble In The Bronx With Mains LIVE (42613/62185; hub 41112/62187; Vjeko Keskic dump-not-stub 33155/62186).
Format [[Premiere - Original VS2]] (41677/62188).
Qty 60.
YAML Light / body Light Profit.
General dest TITLE.
AUOF inside Starting counts.
Named 10 Defensive Shields dest outside 60.
Starting Interrupt HFTMF.
Posted Han With Blaster Pistol dested Han With Heavy Blaster Pistol.
Posted Master Luke dested Luke Skywalker, Jedi Knight.
Posted Sal'torr Kal Fas dested Sai'torr Kal Fas (V) (VS1).
Posted Dunee Ta dested Ounee Ta.
Posted Do Or Do Not dested Do, Or Do Not.
Posted Utimatum dested Ultimatum.
Posted Insurrection & Aim High dested combo.
Skip GEMP.
Handle mighty_maul already cited.
Do not dest onto Maul card pageid 13908.
Do not dest onto Darth Maul card pageid 6743.
Do not dest onto Lord Maul pageid 7882.
23914 Arvind Bhasker Maul’s Combat LIVE (42567/62126; hub 41112/62128; Arvind Bhasker 42568/62127 stub).
Format [[Premiere - Original VS2]] (41677/62129).
Qty 60.
YAML Dark / body Dark LSC.
General dest TITLE (3–0 May World Qualifiers in lead; do not mint May World Qualifiers hub).
FIMA inside Starting (10) counts.
Unnamed 10 shields dest 60 only.
Starting Interrupt omitted.
Posted Let Them Make the First Move/ALWSHR dested Let Them Make The First Move / At Last We Will Have Revenge.
Posted Start your engines dested Start Your Engines!.
Posted Fear is my ally dested Fear Is My Ally.
Posted Control dested Control (Dark).
Posted Alter Combo dested Alter & Collateral Damage.
Posted Sense Combo dested Sense & Uncertain Is The Future.
Posted Masterful move/endor occupation dested Masterful Move & Endor Occupation.
Posted Drop dested Drop!.
Posted Qui Gon’s End dested Qui-Gon's End.
Skip GEMP.
Handle Master Chief.
Do not dest onto Maul card pageid 13908.
Do not dest onto Darth Maul card pageid 6743.
Do not dest onto Lord Maul pageid 7882.
23958 Zach Mann None shall pass choke damn I guess you can LIVE (42566/62113; hub 41112/62115; Zach Mann dump-not-stub 42349/62114).
Format [[Premiere - Original VS2]] (41677/62116).
Qty 60.
YAML Dark / body Dark palace.
General dest TITLE.
Starting Effect omitted.
Unnamed shields dest 60 only.
Posted Tatooine jabba's palace dested Tatooine: Jabba's Palace.
Posted prepared fences dested Prepared Defenses.
Posted no bargain dested No Bargain.
Posted power of the hutt dested Power Of The Hutt.
Posted Bib fortuna dested JP Bib Fortuna.
Posted Boba Fett dested CC Boba Fett.
Posted Jodo cast dested Jodo Kast.
Posted none shall pass dested None Shall Pass x9.
Skip GEMP.
Handle Greedosalive already cited.
Do not dest onto Greedo card pageid 3689.
23962 Matt Wehner Good PunJab Hunting LIVE (42524/62060; hub 41112/62062; Matt Wehner dump-not-stub 36764/62061).
Format [[Premiere - Original VS2]] (41677/62063).
Qty 60.
YAML Light / body Light Hidden Base.
General dest TITLE.
AUOF inside Starting (8) counts.
Unnamed shields dest 60 only.
Posted Hidden Base dested Hidden Base / Systems Will Slip Through Your Fingers.
Posted Rendevous Point dested Rendezvous Point.
Posted Rycar Ryjerd (v) dested Rycar Ryjerd (V) (VS2).
Posted Escape Pod (v) dested Escape Pod (V) (VS2).
Posted KLorSlug (v) dested K'lor'slug (V) (VS2).
Posted The Planet Furthest From dested The Planet That It's Farthest From.
Posted Bith Shuffle/Desperate Reach dested The Bith Shuffle & Desperate Reach.
Posted Qui Gon w/stick dested Qui-Gon Jinn With Lightsaber.
Posted EPP Luke dested Luke With Lightsaber.
Posted EPP Obi dested Obi-Wan With Lightsaber.
Posted An Unusal Ammount Of Fear dested An Unusual Amount Of Fear.
Posted Goo Ney Tay dested Goo Nee Tay.
Posted Sorry About The Mess/Blaster Prof dested Sorry About The Mess & Blaster Proficiency.
Skip GEMP.
Handle Tasa.
Do not dest onto Hidden Base (V).
Do not dest onto a card.
23975 David Kangas QMC Clouds LIVE (42403/61911; hub 41112/61917; David Kangas 42404/61913 stub; Icebreath redirect 42092/61915).
Format [[Premiere - Original VS2]] (41677/61919).
Qty 60.
YAML Light / body Light QMC.
General dest TITLE.
AUOF inside Starting (8) counts.
Unnamed 10 shields dest 60 only.
Posted QMC/Independent Ops dested Quiet Mining Colony.
Posted Sai’tor Kal Fas (V) dested Sai'torr Kal Fas (V) (VS1).
Posted Z-95 Bespin Defense Fighter dested Z-95 Bespin Defense Fighter.
Posted H, C, and the F dested Han, Chewie, And The Falcon.
Posted Cloud Car dested Cloud Car.
Posted Quiggy’s Saber (tat) dested Qui-Gon Jinn's Lightsaber.
Posted All Wings & Darklighter Spin dested combo.
Posted Off The Edge dested On The Edge.
Posted Threepio, Naked dested C-3PO (See-Threepio).
Posted Ric Olie’ dested Ric Olie.
Skip GEMP.
Handle Icebreath.
Do not dest onto a card.
23976 James Zajic die die die LIVE (42351/61817; hub 41112/61819; James Zajic 42352/61818 stub).
Format [[Premiere - Original VS2]] (41677/61820).
Qty 58 as published.
YAML Light / body Light TIGIH.
General dest TITLE.
Starting Effect omitted.
Unnamed 10 defensive sheilds dest 60 only.
Posted there is good in him dested There Is Good In Him.
Posted i feel the conflect dested I Feel The Conflict.
Posted opee sea killeer dested Opee Sea Killer.
Posted insurrection/ aim high dested Insurrection & Aim High.
Posted strik planing dested Strike Planning.
Posted artoo and threepio dested Artoo & Threepio.
Posted artoo detoo in red 5 dested Artoo-Detoo In Red 5.
Posted leia with gun dested Leia With Blaster Rifle.
Posted trafic control dested printed.
Posted houjix combo dested Houjix & Out Of Nowhere.
Posted free ride combo dested Free Ride & Endor Celebration.
Skip GEMP.
Handle dabora.
Do not dest onto a card.
23994 Adam Nelson Droid Deal v 1 0 LIVE (42350/61813; hub 41112/61815; Adam Nelson dump-not-stub 37460/61814).
Format [[Premiere - Original VS2]] (41677/61816).
Qty 60.
YAML Dark / body Dark TDIGWATT Dark Deal.
General dest TITLE.
FIMA inside Starting (7) counts.
Named 10 Defensive Shields dest outside 60.
Posted TDIGWATT dested This Deal Is Getting Worse All The Time.
Posted There They Are dested There They Are!.
Posted U-3PO dested U-3PO (Yoo-Threepio).
Posted Death Star Sentry (V) dested Death Star Sentry (V) (VS2).
Posted Imperial-class Star Destroyer(V) dested Imperial-Class Star Destroyer (V) (VS2).
Posted IIFYLOFD (V) dested IIFYLOFD (V) (VS2).
Posted Executor dested Executor (Dark).
Posted Bespin dested Bespin (Dark).
Posted CC slang dested colon Cloud City: titles.
Skip GEMP.
Handle Skipray.
Do not dest onto Skipray Blastboat.
24003 Zach Mann What my step It’s yours I should be watching LIVE (42348/61808; hub 41112/61810; Zach Mann 42349/61809 stub).
Format [[Premiere - Original VS2]] (41677/61811).
Qty 60.
YAML Light / body Light WYS.
General dest TITLE.
Starting Effect omitted.
Posted WYSTPCGALR dested Watch Your Step.
Posted Artoo in red 5 dested Artoo-Detoo In Red 5.
Posted Star destroyer dested Star Destroyer!.
Posted Houjix combo dested Houjix & Out Of Nowhere.
Posted Rattlir dested Ralltiir Freighter Captain.
Posted Millenium falcon dested Millennium Falcon.
Skip GEMP.
Handle Greedosalive.
Do not dest onto Greedo card pageid 3689.
24020 Mike Guarino I’m Getting Too Old For This LIVE (42302/61752; hub 41112/61754; Mike Guarino 42303/61753 stub).
Format [[Premiere - Original VS2]] (41677/61755).
Qty 60.
YAML Light / body Light MBO.
General dest TITLE.
Starting Effect omitted.
Posted Proton Torpedoes(Ep.1) dested Proton Torpedoes (Theed Palace).
Posted Luke w/Lightsaber dested Luke With Lightsaber.
Posted Master Qui-Gon dested Master Qui-Gon.
Posted Princess Organa dested Princess Organa.
Posted Traffic Control dested printed.
Posted Battle Plan & Draw Their Fire dested combo.
Skip GEMP.
Handle Darth Dago.
Do not dest onto [[Mike]] (redirects to Mike Thomas).
Do not dest onto Qui-Gon Jinn card pageid 6703.
Do not dest onto Bravo 3 as player.
24022 Chris McCoy Quiet Macking of Cloud city LIVE (42255/61697; hub 41112/61699; Chris McCoy 42256/61698 stub).
Format [[Premiere - Original VS2]] (41677/61700).
Qty 60.
YAML Light / body Light QMC.
General dest TITLE.
AUOF inside Starting(8) counts.
Unnamed Ten D shields dest 60 only.
Posted Escape Pod V dested Escape Pod (V) (VS2).
Posted Luke w/ Stick dested Luke With Lightsaber.
Posted CC slang dested colon Cloud City: titles.
Posted Docking Bay dested Platform 327.
Skip GEMP.
Handle Golfercwm.
Do not dest onto Qui-Gon Jinn card pageid 6703.
24025 Chris Davis TDIGWATT/PIDAIAF CC Dark Deal Deck LIVE (42253/61693; hub 41112/61695; Chris Davis 42254/61694 stub).
Format [[Premiere - Original VS2]] (41677/61696).
Qty 60.
YAML Dark / body Dark Deal.
General dest TITLE.
No FIMA.
Unnamed shields dest 60 only.
Posted Black 2 (V) dested Black 2 (V) (VS1).
Posted Imperial-Class Star Destroyer (V is possible) dested printed.
Posted The Empire's Back dested printed.
Posted CC slang dested colon Cloud City: titles.
Posted Lando Calrissian dested Lando Calrissian (Dark).
Posted IG-88 dested printed.
Posted Dark Maneuvers & Tallon Roll dested combo.
Skip GEMP.
Handle Fred.
Do not dest onto Admiral Piett card pageid 137.
24026 Matt Carulli Hunt Down and Revive the SCUM LIVE (42206/61635; hub 41112/61637; Matt Carulli dump-not-stub 17151/61636).
Format [[Premiere - Original VS2]] (41677/61638).
Qty 60.
YAML Dark / body Dark Court.
General dest TITLE.
FIMA inside Starting (9) counts.
Named 10 Defensive Shields dest outside 60.
Posted Blaster Rack (V) dested Blaster Rack (V) (VS1).
Posted IIFYLOFD (V) dested IIFYLOFD (V) (VS2).
Posted Bib Fortuna (Reflections III) dested Bib Fortuna (Dark).
Posted Boba Fett (CC) dested Cloud City Boba Fett.
Posted Dr.
Evazans Blaster dested Dr.
Evazan's Sawed-off Blaster.
Posted Naboo DB dested Naboo: Theed Palace Docking Bay.
Posted Spaceport DB dested Spaceport Docking Bay.
Posted Sniper/ Dark Strike dested Sniper & Dark Strike.
Skip GEMP.
Handle QuiGon57.
Do not dest onto a Qui-Gon card; Matt Carulli pageid 17151 already exists.
24089 Mike (Quione) Saber combat my way LIVE (42158/61579; hub 41112/61581; Mike (Quione) 42159/61580 stub).
Format [[Premiere - Original VS2]] (41677/61582).
Qty 60.
YAML Light / body Light We'll Handle This.
General dest TITLE.
AUOF inside Starting counts.
Unnamed extra dest 60 only.
Posted Palace Generator Core dested Naboo: Theed Palace Generator Core.
Posted Theed Palace Generator dested Naboo: Theed Palace Generator.
Posted Podrace Arena dested Tatooine: Podrace Arena.
Posted Anakins Podracer dested Anakin's Podracer.
Posted Squadren Assignments dested Squadron Assignments.
Posted Captain Han dested Captain Han Solo.
Posted Tat Obi dested Obi-Wan Kenobi, Padawan Learner.
Posted Ref 3 Qui gon dested Qui-Gon Jinn, Jedi Master.
Posted Tat Padme dested Padme Naberrie.
Posted Chewie w/ Blaster dested Chewie With Blaster Rifle.
Posted Firgin D'an dested Figrin D'an.
Posted Eject Eject dested Eject! Eject!.
Posted Artoo I have a bad feeling about this dested Artoo, I Have A Bad Feeling About This.
Posted Run Luke Run dested Run Luke, Run!.
Posted Intruder Missle dested Intruder Missile.
Posted I did it dested I Did It!.
Inner Strength dested Reflections III Epic Event.
Skip GEMP.
Handle Quione.
Do not dest onto [[Mike]] (redirects to Mike Thomas).
Do not dest onto a card.
24104 Krueger The Beast on the Beach LIVE (42106/61518; hub 41112/61520; Kyle Krueger dump-not-stub 21369/61519).
Format [[Premiere - Original VS2]] (41677/61521).
Qty 60.
YAML Dark / body Dark mains.
General dest TITLE (3 tournaments undefeated posted without a finish; do not mint Endor Regionals hub).
FIMA inside Starting(4) counts.
Unnamed 10 D-shields dest 60 only.
Posted Imperial Holotable dested Imperial Holotable.
Posted Zuckass dested Zuckuss In Mist Hunter.
Posted Omni Box dested Ommni Box & It's Worse.
Posted Alter(Coruscant) dested Alter (Dark) (Coruscant).
Posted Imperial Reinforcements(v) dested Imperial Reinforcements (V) (VS2).
Posted They're Still Coming Through dested They're Still Coming Through!.
Posted Drop dested Drop!.
Skip GEMP.
Handle Meto already cited from 26173.
Do not dest onto a card; Kyle Krueger pageid 21369 already exists.
24142 Kafer LSC TacoBill style LIVE (42105/61514; hub 41112/61516; Bill Kafer dump-not-stub 21342/61515).
Format [[Premiere - Original VS2]] (41677/61517).
Qty 60.
YAML Dark / body Dark LSC.
General dest TITLE.
FIMA inside Starting (9) counts.
Unnamed 10 shields dest 60 only.
Posted LTMTFM/ALWWHR dested Let Them Make The First Move.
Posted Commander Merrejek dested Commander Merrejk.
Posted Boba Fett In Slave One dested Boba Fett In Slave I.
Posted Naboo Theed Palace Generator dested Naboo: Theed Palace Generator.
Posted Blockade Flagship Bridge dested Blockade Flagship: Bridge.
Posted Executor Docking Bay dested Executor: Docking Bay.
Posted YCHF & Mobilization Points dested You Cannot Hide Forever & Mobilization Points.
Posted Theyre Still Coming Through dested They're Still Coming Through!.
Posted Ommni Box & Its Worse dested Ommni Box & It's Worse.
Posted Blaster Rack (V) dested Blaster Rack (V) (VS1).
Posted Executor dested Executor (Dark).
Posted Endor dested Endor (Dark).
Posted Bespin dested Bespin (Dark).
Posted We Must Accelerate Our Plans dested as printed Coruscant Dark.
Skip GEMP.
Handle TacoBill.
Do not dest onto a card; Bill Kafer pageid 21342 already exists.
Do not dest onto Admiral Piett card pageid 137.
24274 Nystrom Empire is virtually back LIVE (42103/61510; hub 41112/61512; Pyry Nystrom 42104/61511 stub).
Format [[Premiere - Original VS2]] (41677/61513).
Qty 60.
YAML Dark / body Dark SYCFA.
General dest TITLE.
FIMA inside Starting(10) counts.
Named 5 of 10 Defensive Shields dest outside 60; unnamed rest dest 60 only.
Posted Allocations Of Corruption dested Allegations Of Corruption.
Posted DSDocking Bay dested Death Star: Docking Bay 327.
Posted Darth Vader(V) dested Darth Vader (V) (VS1).
Posted Commander Praji(V) dested Commander Praji (V) (VS2).
Posted The Empires Back(V) dested The Empire's Back (V) (VS2).
Posted Imperial Class Star Destroyer(V) dested Imperial-Class Star Destroyer (V) (VS2).
Posted Fear Will Keep Them In Line(V) dested Fear Will Keep Them In Line (V) (VS2).
Posted I Find Your Lack Of Fate Disturbing(V) dested IIFYLOFD (V) (VS2).
Skip GEMP.
Handle Blizzard.
Do not dest onto Blizzard 4.
Do not dest onto Admiral Piett card pageid 137.
24316 Van Winkle Seth's Mad Huntdown Deck LIVE (42050/61451; hub 41112/61453; Seth Van Winkle 42051/61452 stub).
Format [[Premiere - Original VS2]] (41677/61454).
Qty 60.
YAML Dark / body Dark Hunt Down.
General dest TITLE.
FIMA inside Start (10); unnamed shields dest 60 only.
Posted Holotheater dested Executor: Holotheatre.
Posted Med.
Chamber dested Executor: Meditation Chamber.
Posted DVDLOTS dested Darth Vader, Dark Lord Of The Sith.
Posted Darth Vader dested Premiere Darth Vader.
Posted Vader with Saber dested Darth Vader With Lightsaber.
Posted Darth Maul, YA dested Darth Maul, Young Apprentice.
Posted Emperor Palpy dested Emperor Palpatine.
Posted IG88 with Gun dested IG-88 With Riot Gun.
Posted Dr.
E and Ponda B.
dested Dr.
Evazan & Ponda Baba.
Posted ZiMH dested Zuckuss In Mist Hunter.
Posted BFiS1 dested Boba Fett In Slave I.
Posted BiHT dested Bossk In Hound's Tooth.
Posted Maul's Double Bladed Saber dested Maul's Double-Bladed Lightsaber.
Posted Executor DB dested Executor: Docking Bay.
Posted D2 DB dested Death Star II: Docking Bay.
Posted Endor DB dested Endor: Landing Platform (Docking Bay).
Posted IAO/Plans dested Imperial Arrest Order & Secret Plans.
Posted YCHF/Mob.
Points dested You Cannot Hide Forever & Mobilization Points.
Posted TCINC dested The Circle Is Now Complete.
Posted Control/SFS dested Control & Set For Stun.
Posted YAB dested You Are Beaten.
Posted Visage start + Visage x2 dested x3 as published.
Skip GEMP.
Handle Ooryl.
Do not dest onto Ooryl Qrygg.
24467 Krueger the beast on the beach v2 LIVE (41998/61390; hub 41112/61391; Kyle Krueger dump-not-stub 21369/61392).
Format [[Premiere - Original VS2]] (41677/61393).
Qty 60.
YAML Dark / body Dark mains.
General dest TITLE (12-0 across four tournaments posted without a finish; do not mint Endor Regionals or RebelCon hubs).
FIMA inside Starting(4); unnamed 10 D-shields dest 60 only.
Posted Interrupts(26) listed 25.
Posted Omni Box dested Ommni Box & It's Worse.
Posted Drop dested Drop!.
Posted They're Still Coming Through dested They're Still Coming Through!.
Posted Imperial Reinforcements(v) dested Imperial Reinforcements (V) (VS2).
Posted Emperor dested Emperor Palpatine.
Posted Zuckass dested Zuckuss In Mist Hunter.
Skip GEMP.
Handle Meto.
Do not dest onto a card; Kyle Krueger pageid 21369 already exists.
24511 Burnett JediGamler's Watto aka The Unstoppable Machine LIVE (41994/61382; hub 41112/61383; David Burnett 41995/61384 stub; Aaron Pawlik 41996/61385 stub; 2002 Dantooine Regionals 41997/61386; 2002 Houston DPC 41941/61387).
Format [[Premiere - Original VS2]] (41677/61388).
Qty 60.
YAML Light / body Dark Watto.
General dest TITLE with Dantooine Regionals 3-0 Aaron Pawlik and Houston DPC 2-1 Burnett rows.
FIMA inside STARTING-8; unnamed shields dest 60 only.
Posted /I Win dested No Money, No Parts, No Deal!.
Posted Graga dested Gragra.
Posted Force Lighting dested Force Lightning.
SpaceportDocking Bay dested Spaceport Docking Bay.
Skip GEMP.
Handle JediGambler.
Do not dest onto Admiral Piett card pageid 137.
24516 Warren Raging Bull (Hoostino's Hunt Down Hammer) LIVE (41938/61316; hub 41112/61317; Justin Warren 41939/61318 stub; Brian Hunter 36782/61319 dump-not-stub; 2002 Houston Mini-Open 41940/61320; 2002 Houston DPC 41941/61321).
Format [[Premiere - Original VS2]] (41677/61322).
Qty 60.
YAML Light / body Dark Hunt Down.
General dest TITLE with Mini-Open 1st and DPC 2nd rows.
10 Defensive Shields outside the 60 (IIFYLOFD (V) VS2).
FIMA inside EFFECTS.
Visage x3 as published.
We Must Accelerate Our Plans dested as printed Coruscant Dark.
Skip GEMP.
Handle hoostino.
24668 Cross Squires Origins Profit LIVE (41883/61254; hub 41112/61255; Ken Cross 23809/61256 dump-not-stub; 2002 Origins Open 41884/61257).
Format [[Premiere - Original VS2]] (41677/61258).
Qty 60.
YAML Light / body Light Profit.
Tournament dest Origins Open 7th 3-0.
Master Luke dested Luke Skywalker, Jedi Knight.
naked 3po dested C-3PO (See-Threepio).
hologame board dested Dejarik Hologameboard.
Sai'torr Kal Fas (V) (VS1) + Escape Pod (V) (VS2).
AUOF inside EFFECTS.
Unnamed 10 D-shields dest 60 only.
Skip GEMP.
Handle Squires.
Do not dest onto a card; Ken Cross pageid 23809 already exists.
24688 Marshall Viperstyle - Keeping The Senators Out Forever LIVE (41881/61250; hub 41112/61251; Steve Marshall 41882/61252 stub).
Format [[Premiere - Original VS2]] (41677/61253).
Qty 60.
YAML Light / body Light QMC.
General dest.
CC Leia's Hut dested Guest Quarters.
Cloud City Docking Bay dested Platform 327.
Luke Skywalker (V) (VS1).
AUOF inside EFFECTS.
Skip GEMP.
Handle BlackViper.
24783 Sneed Subterranean Homesick Alien LIVE (41831/61186; hub 41112/61187; Michael Sneed 41832/61188 stub; Tulsa Mini-Open 41833/61189).
Format [[Premiere - Original VS2]] (41677/61190).
Qty 60.
FIMA inside START (8).
Tournament dest.
Alter (Dark) (Coruscant).
Yeb Yeb Adem'thorn.
Skip GEMP.
Do not dest onto Admiral Piett card pageid 137.
24807 McLain The Rx Throne Room Wrex LIVE (41782/61128; hub 41112/61129; Ryan McLain 41783/61130 stub).
Format [[Premiere - Original VS2]] (41677/61131).
Qty 59 as published (Revolution x dested x1).
Sense & Uncertain Is The Future Dark combo File.
We Must Accelerate dested We Wish To Board At Once.
No tournament row.
24905 Irving 3B3-888 Superstar aka Agents of pure BS LIVE (41780/61123; hub 41112/61124; John Irving 41781/61125 dump-not-stub; Jirving00 redirect 41261/61126).
Format [[Premiere - Original VS2]] (41677/61127).
Qty 60.
FIMA inside Starting 9; unnamed 10 shields dest 60 only.
YAML extra space before aka off dest TITLE.
Sense & Recoil In Fear Light combo File.
24965 Bouchard Fear Will Keep Them In Line (V) ALPHA LIVE (41728/61063; hub 41112/61064; Maximilien Bouchard 41729/61065 stub).
Format [[Premiere - Original VS2]] (41677/61066).
Qty 61 as published.
FIMA inside Starting 9.
Original-VS Fear Will Keep Them In Line (V) (VS2) and Imperial-Class Star Destroyer (V) (VS2).
25015 Zinn Shes Virtually Back LIVE (41676/61004; hub 41112/61005; Greg Zinn 17150/61006 dump-not-stub).
Format [[Premiere - Original VS2]] (41677/61007; redirect POVS2 41678/61008).
10 Defensive Shields outside the 60.
Original-VS Leia's Back (V) (VS2) and Yavin Sentry (V) (VS2).
25033 Fiedler we will reveal ourselves to the jedi at last we will have revenge LIVE (41622/60937; hub 41112/60938; Justin Fiedler 41623/60939).
2002 Worlds lists LIVE (Consoli 26297, Shaw DS 26555, Shaw LS 26204, Watabayashi 26273, Krueger 26173).
Nov–Dec 2002 general dests LIVE (26448/26425/26421/26368).

# DeckTech dest log addendum (moved out of swccg-wiki SKILL.md, 2026-10-20)

Verbatim text cut from the DeckTech paragraph. Append to `DEST-LOG-decktech.md`. Grep, do not read whole.

## Worked non-tournament dest titles

Non-tournament dest title is `{Player} {Published title}` (worked [[Mike Stevens ls senate]], [[Jacob Taylor Jacob's Profit aka Big Trouble]], [[Dunya Ertan beefed up profit]], [[Chris Burnett My senate]], [[Taylor Hayward A Hidden Base Deck]], [[Dennis Jeffris Rebel Strike Team - Da Non-Bomb]], [[Dunya Ertan we dont need a sticking hypergenerator]], [[Jason Herrin Voice of the council solid]], [[Taylor Hayward Agents In The Court]], [[Dunya Ertan power of Rebel strike team]], [[Thomas Papp HDADTJ aka there are no Jedi alive]], [[Sam Diamond The CIA Is Trying To Kill Me]], [[Drew Scott BHBM how to kill combat]], [[Jacob Taylor Jacob's BHBM aka Blame Canada]], [[Lewis Blake YEEeeah I've got the Hoth (Big) Blues Baby]], [[Taylor Hayward I like blowin sht up]], [[Peter Jurcovic There Are Those Droidekas]], [[Peter Jurcovic Hold Me Thrill Me Kiss Me Kill Me]], [[Keith Watabayashi G-Scum]], [[Daniel Blackford Rock The Projects]], [[Vjeko Keskic My Keskic Is This Deal Legal aka The Croatian Deal v2 1]], [[Justin Fiedler we will reveal ourselves to the jedi at last we will have revenge]], [[Greg Zinn Shes Virtually Back]], [[Maximilien Bouchard Fear Will Keep Them In Line (V) ALPHA]], [[John Irving 3B3-888 Superstar aka Agents of pure BS]], [[Ryan McLain The Rx Throne Room Wrex]], [[Steve Marshall Viperstyle - Keeping The Senators Out Forever]], [[Justin Warren Raging Bull (Hoostino's Hunt Down Hammer)]], [[David Burnett JediGamler's Watto aka The Unstoppable Machine]], [[Kyle Krueger the beast on the beach v2]], [[Seth Van Winkle Seth's Mad Huntdown Deck]], [[Pyry Nystrom Empire is virtually back]], [[Bill Kafer LSC TacoBill style]], [[Kyle Krueger The Beast on the Beach]], [[Mike (Quione) Saber combat my way]], [[Matt Carulli Hunt Down and Revive the SCUM]], [[Chris Davis TDIGWATT/PIDAIAF CC Dark Deal Deck]], [[Chris McCoy Quiet Macking of Cloud city]], [[Mike Guarino I’m Getting Too Old For This]], [[Zach Mann What my step It’s yours I should be watching]], [[Adam Nelson Droid Deal v 1 0]], [[James Zajic die die die]], [[David Kangas QMC Clouds]], [[Matt Wehner Good PunJab Hunting]], [[Zach Mann None shall pass choke damn I guess you can]], [[Arvind Bhasker Maul’s Combat]], [[Vjeko Keskic Rumble In The Bronx With Mains]], [[Geoff Bowman BHBM - Bastard He Bit Me - Well that’s cuz you won]], [[Matt Wehner Court Of the Vile Gangsta - Limp Bizkit Style]], [[Chris Wodicka 6th place Coruscant regionals]], [[Adam McCombie Throne Room Mains So Hot Right Now]], [[Stephen Beckham Too Hot in da Hot Tub]], [[Uriah Watkins Testing Testing 1 2 3 (4 5 6)]], [[2002 Ralltiir Regionals Vjeko Keskic Court Likes Direct Damage aka Gailid Superstar]], [[Brian Hunter Saber Combat done RIGHT aka No Mans Land]], [[Quirin Fürgut Unbeatable EBO aka fun for everyone]], [[Jon Manning Cloud City trooper deck]], [[Maximilien Bouchard WYS Choke BETA]], [[Vjeko Keskic All Your Damage Belongs To Watto]], [[Vjeko Keskic H-TOWN Jedis vs NRW Jedis]], [[Mike (Quione) Rebel Strike Team- Stay the hell of endor]], [[Wes Brown Imperial Blues]], [[Cody Jewell ’Saber Combat My Way V1 00(UnRevised)]], [[Matthew Harrison-Trainor Secret Siths Profit]])

## Per-deck dest fragments

Body Dark Hoth walkers / YAML Light. Evazan & Ponda Baba. AUOF inside Starting counts. Black cited; no Mr. Black page. Black" Herrin. Black as a new person. AUOF inside Starting counts. FIMA inside Starting (9) counts. AUOF inside Starting counts. FIMA inside Starting counts. Evazan & Ponda Baba. FIMA inside Effects (19) counts. FIMA inside Starting counts. Named 8 Defensive Shields dest outside 60. Evazan & Ponda Baba. YAML title keep I like blowin sht up (minced; Consoli-only vulgar-off). FIMA inside Effects (10) counts. AUOF inside Starting Effect counts. FIMA inside Starting (8) counts. AUOF inside Starting counts. FIMA inside Starting (9) counts. AUOF inside Starting counts. AUOF inside Effects (7) counts. FIMA inside Effects (8) counts. AUOF inside Starting (9) counts. AUOF inside Starting counts. FIMA inside Starting Effect counts. Admiral Ozzel amendment dest as published. FIMA inside Effects counts. AUOF inside Starting counts. AUOF inside Starting counts. AUOF inside Starting counts. FIMA inside Start (7) counts. FIMA inside Starting counts. FIMA inside Starting (9) counts. AUOF inside Starting counts. FIMA inside Starting (10) counts. AUOF inside Starting (8) counts. AUOF inside Starting (8) counts. FIMA inside Starting (7) counts. AUOF inside Starting(8) counts. No FIMA. FIMA inside Starting (9) counts. Evazan's Sawed-off Blaster. AUOF inside Starting counts. FIMA inside Starting(4) counts. FIMA inside Starting (9) counts. FIMA inside Starting(10) counts. Named 5 of 10 Defensive Shields dest outside 60; unnamed rest dest 60 only. FIMA inside Start (10); unnamed shields dest 60 only. Evazan & Ponda Baba. FIMA inside Starting(4); unnamed 10 D-shields dest 60 only. FIMA inside STARTING-8; unnamed shields dest 60 only. FIMA inside EFFECTS. Visage x3 as published. Tournament dest Origins Open 7th 3-0. Sai'torr Kal Fas (V) (VS1) + Escape Pod (V) (VS2). AUOF inside EFFECTS. General dest. Luke Skywalker (V) (VS1). AUOF inside EFFECTS. FIMA inside START (8). Tournament dest. Alter (Dark) (Coruscant). Yeb Yeb Adem'thorn. Sense & Uncertain Is The Future Dark combo File. FIMA inside Starting 9; unnamed 10 shields dest 60 only. YAML extra space before aka off dest TITLE. FIMA inside Starting 9.
