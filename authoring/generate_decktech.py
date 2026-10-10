#!/usr/bin/env python3
"""Dest DeckTech archive 60s onto wiki pages.

Slang mapping lives here (LS_NOTE-style). Finished articles are lead, Deck info,
CardLink dest 60, then a formatted original post (metadata + wiki Strategy +
collapsed original Cards). Index Light/Dark tags on Skilton listings are not
source of truth. Tournament dest title is {Event} {Player} {Published title}
when the post names the deck; vulgar published titles stay off dest TITLE.

www.stephenskilton.com/decktech_archives/ and
stevetotheizz0.github.io/decktech_archives/ are the same GitHub Pages site
(www CNAME → stevetotheizz0.github.io; github.io 301 to the custom domain).
Dest FROM Skilton UTF-8 posts. Sources cite live decktech.net
(/starwarsccg/deck/{id}, PC 2022 recast on the original domain) + Skilton +
GitHub Pages + a working Wayback when we have one.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
POSTS = ROOT / "decktech-posts"
sys.path.insert(0, str(ROOT))
import wiki_cardlink as cl  # noqa: E402

TFN_RESULTS = "https://www.theforce.net/ccg/story/World_Championship_Results_announced_64778.asp"
DCON_FORMATS = "https://web.archive.org/web/20020810223927/http://www.decipher.com/deciphercon/2002/events/worldsformats.html"


def live_deck(pid: int) -> str:
    return f"http://www.decktech.net/starwarsccg/deck/{pid}"


def skilton_deck(pid: int) -> str:
    return f"https://www.stephenskilton.com/decktech_archives/{pid}/"


def github_deck(pid: int) -> str:
    return f"https://stevetotheizz0.github.io/decktech_archives/{pid}/"


# Working Wayback captures from historian (CDX 503 this sitting; /save/ 200s).
WAYBACK = {
    ("live", 26555): "https://web.archive.org/web/20261008224841/http://www.decktech.net/starwarsccg/deck/26555/",
    ("live", 26297): "https://web.archive.org/web/20261008225349/http://www.decktech.net/starwarsccg/deck/26297/",
    ("live", 26204): "https://web.archive.org/web/20261008225420/http://www.decktech.net/starwarsccg/deck/26204/",
    ("live", 26273): "https://web.archive.org/web/20261009001845/http://www.decktech.net/starwarsccg/deck/26273/",
    ("live", 26173): "https://web.archive.org/web/20261009001934/http://www.decktech.net/starwarsccg/deck/26173/",
    ("live", 26448): "https://web.archive.org/web/20261009013131/http://www.decktech.net/starwarsccg/deck/26448/",
    ("live", 26425): "https://web.archive.org/web/20261009013207/http://www.decktech.net/starwarsccg/deck/26425/",
    ("live", 26421): "https://web.archive.org/web/20261009013249/http://www.decktech.net/starwarsccg/deck/26421/",
    ("live", 26368): "https://web.archive.org/web/20261009014432/http://www.decktech.net/starwarsccg/deck/26368/",
    ("live", 25033): "https://web.archive.org/web/20261009020848/http://www.decktech.net/starwarsccg/deck/25033/",
    ("live", 25015): "https://web.archive.org/web/20261009023403/http://www.decktech.net/starwarsccg/deck/25015/",
    ("skilton", 25015): "https://web.archive.org/web/20261009023427/https://www.stephenskilton.com/decktech_archives/25015/",
    ("live", 24965): "https://web.archive.org/web/20261009025215/http://www.decktech.net/starwarsccg/deck/24965/",
    ("skilton", 24965): "https://web.archive.org/web/20261009025301/https://www.stephenskilton.com/decktech_archives/24965/",
    ("live", 24905): "https://web.archive.org/web/20261009030825/http://www.decktech.net/starwarsccg/deck/24905/",
    ("skilton", 24905): "https://web.archive.org/web/20261009030916/https://www.stephenskilton.com/decktech_archives/24905/",
    ("live", 24807): "https://web.archive.org/web/20261009032227/http://www.decktech.net/starwarsccg/deck/24807/",
    ("live", 24783): "https://web.archive.org/web/20261009033752/http://www.decktech.net/starwarsccg/deck/24783/",
    ("live", 24688): "https://web.archive.org/web/20261009035540/http://www.decktech.net/starwarsccg/deck/24688/",
    ("skilton", 24688): "https://web.archive.org/web/20261009035618/https://www.stephenskilton.com/decktech_archives/24688/",
    ("live", 24668): "https://web.archive.org/web/20261009042401/http://www.decktech.net/starwarsccg/deck/24668/",
    ("skilton", 24668): "https://web.archive.org/web/20261009042429/https://www.stephenskilton.com/decktech_archives/24668/",
    ("live", 24516): "https://web.archive.org/web/20261009044330/http://www.decktech.net/starwarsccg/deck/24516/",
    ("skilton", 24516): "https://web.archive.org/web/20261009044352/https://www.stephenskilton.com/decktech_archives/24516/",
    ("live", 24511): "https://web.archive.org/web/20261009050306/http://www.decktech.net/starwarsccg/deck/24511/",
    ("skilton", 24511): "https://web.archive.org/web/20261009050325/https://www.stephenskilton.com/decktech_archives/24511/",
    ("live", 24467): "https://web.archive.org/web/20261009052233/http://www.decktech.net/starwarsccg/deck/24467/",
    ("skilton", 24467): "https://web.archive.org/web/20261009052259/https://www.stephenskilton.com/decktech_archives/24467/",
    ("live", 24316): "https://web.archive.org/web/20261009053904/http://www.decktech.net/starwarsccg/deck/24316/",
    ("skilton", 24316): "https://web.archive.org/web/20261009053947/https://www.stephenskilton.com/decktech_archives/24316/",
    ("skilton", 24274): "https://web.archive.org/web/20261009055202/https://www.stephenskilton.com/decktech_archives/24274/",
    ("live", 24142): "https://web.archive.org/web/20261009062755/http://www.decktech.net/starwarsccg/deck/24142/",
    ("skilton", 24142): "https://web.archive.org/web/20261009062813/https://www.stephenskilton.com/decktech_archives/24142/",
    ("live", 24104): "https://web.archive.org/web/20261009064140/http://www.decktech.net/starwarsccg/deck/24104/",
    ("skilton", 24104): "https://web.archive.org/web/20261009064249/https://www.stephenskilton.com/decktech_archives/24104/",
    ("live", 24089): "https://web.archive.org/web/20261009065954/http://www.decktech.net/starwarsccg/deck/24089/",
    ("skilton", 24089): "https://web.archive.org/web/20261009070021/https://www.stephenskilton.com/decktech_archives/24089/",
    ("live", 24026): "https://web.archive.org/web/20261009072433/http://www.decktech.net/starwarsccg/deck/24026/",
    ("skilton", 24026): "https://web.archive.org/web/20261009072432/https://www.stephenskilton.com/decktech_archives/24026/",
    ("live", 24025): "https://web.archive.org/web/20261009074117/http://www.decktech.net/starwarsccg/deck/24025/",
    ("skilton", 24025): "https://web.archive.org/web/20261009074119/https://www.stephenskilton.com/decktech_archives/24025/",
    ("live", 24022): "https://web.archive.org/web/20261009080240/http://www.decktech.net/starwarsccg/deck/24022/",
    ("skilton", 24022): "https://web.archive.org/web/20261009080251/https://www.stephenskilton.com/decktech_archives/24022/",
    ("live", 24020): "https://web.archive.org/web/20261009082147/http://www.decktech.net/starwarsccg/deck/24020/",
    ("skilton", 24020): "https://web.archive.org/web/20261009082421/https://www.stephenskilton.com/decktech_archives/24020/",
    ("live", 24003): "https://web.archive.org/web/20261009084136/http://www.decktech.net/starwarsccg/deck/24003/",
    ("skilton", 24003): "https://web.archive.org/web/20261009084155/https://www.stephenskilton.com/decktech_archives/24003/",
    ("live", 23994): "https://web.archive.org/web/20261009085050/http://www.decktech.net/starwarsccg/deck/23994/",
    ("skilton", 23994): "https://web.archive.org/web/20261009085109/https://www.stephenskilton.com/decktech_archives/23994/",
    ("live", 23976): "https://web.archive.org/web/20261009091256/http://www.decktech.net/starwarsccg/deck/23976/",
    ("skilton", 23976): "https://web.archive.org/web/20261009091340/https://www.stephenskilton.com/decktech_archives/23976/",
    ("live", 23975): "https://web.archive.org/web/20261009092820/http://www.decktech.net/starwarsccg/deck/23975/",
    ("skilton", 23975): "https://web.archive.org/web/20261009092908/https://www.stephenskilton.com/decktech_archives/23975/",
    ("live", 23962): "https://web.archive.org/web/20261009100028/http://www.decktech.net/starwarsccg/deck/23962/",
    ("skilton", 23962): "https://web.archive.org/web/20261009100123/https://www.stephenskilton.com/decktech_archives/23962/",
    ("live", 23958): "https://web.archive.org/web/20261009101749/http://www.decktech.net/starwarsccg/deck/23958/",
    ("skilton", 23958): "https://web.archive.org/web/20261009101826/https://www.stephenskilton.com/decktech_archives/23958/",
    ("live", 23914): "https://web.archive.org/web/20261009104323/http://www.decktech.net/starwarsccg/deck/23914/",
    ("skilton", 23914): "https://web.archive.org/web/20261009104343/https://www.stephenskilton.com/decktech_archives/23914/",
    ("live", 23859): "https://web.archive.org/web/20261009110318/http://www.decktech.net/starwarsccg/deck/23859/",
    ("skilton", 23859): "https://web.archive.org/web/20261009110337/https://www.stephenskilton.com/decktech_archives/23859/",
    ("live", 23847): "https://web.archive.org/web/20261009111844/http://www.decktech.net/starwarsccg/deck/23847/",
    ("skilton", 23847): "https://web.archive.org/web/20261009111945/https://www.stephenskilton.com/decktech_archives/23847/",
    ("live", 23843): "https://web.archive.org/web/20261009113254/http://www.decktech.net/starwarsccg/deck/23843/",
    ("skilton", 23843): "https://web.archive.org/web/20261009113403/https://www.stephenskilton.com/decktech_archives/23843/",
    ("live", 23830): "https://web.archive.org/web/20261009115058/http://www.decktech.net/starwarsccg/deck/23830/",
    ("skilton", 23830): "https://web.archive.org/web/20261009115115/https://www.stephenskilton.com/decktech_archives/23830/",
    ("live", 23820): "https://web.archive.org/web/20261009121807/http://www.decktech.net/starwarsccg/deck/23820/",
    ("skilton", 23820): "https://web.archive.org/web/20261009121823/https://www.stephenskilton.com/decktech_archives/23820/",
    ("live", 23798): "https://web.archive.org/web/20261009123706/http://www.decktech.net/starwarsccg/deck/23798/",
    ("skilton", 23798): "https://web.archive.org/web/20261009123724/https://www.stephenskilton.com/decktech_archives/23798/",
    ("live", 23661): "https://web.archive.org/web/20261009124811/http://www.decktech.net/starwarsccg/deck/23661/",
    ("skilton", 23661): "https://web.archive.org/web/20261009124833/https://www.stephenskilton.com/decktech_archives/23661/",
    ("live", 23606): "https://web.archive.org/web/20261009130803/http://www.decktech.net/starwarsccg/deck/23606/",
    ("skilton", 23606): "https://web.archive.org/web/20261009130833/https://www.stephenskilton.com/decktech_archives/23606/",
    ("live", 23598): "https://web.archive.org/web/20261009132707/http://www.decktech.net/starwarsccg/deck/23598/",
    ("skilton", 23598): "https://web.archive.org/web/20261009132809/https://www.stephenskilton.com/decktech_archives/23598/",
    ("live", 23592): "https://web.archive.org/web/20261009134733/http://www.decktech.net/starwarsccg/deck/23592/",
    ("live", 23571): "https://web.archive.org/web/20261009140621/http://www.decktech.net/starwarsccg/deck/23571/",
    ("skilton", 23571): "https://web.archive.org/web/20261009140748/https://www.stephenskilton.com/decktech_archives/23571/",
    ("live", 23567): "https://web.archive.org/web/20261009142704/http://www.decktech.net/starwarsccg/deck/23567/",
    ("skilton", 23567): "https://web.archive.org/web/20261009142730/https://www.stephenskilton.com/decktech_archives/23567/",
    ("live", 23561): "https://web.archive.org/web/20261009143952/http://www.decktech.net/starwarsccg/deck/23561/",
    ("skilton", 23561): "https://web.archive.org/web/20261009144011/https://www.stephenskilton.com/decktech_archives/23561/",
    ("live", 23520): "https://web.archive.org/web/20261009150735/http://www.decktech.net/starwarsccg/deck/23520/",
    ("skilton", 23520): "https://web.archive.org/web/20261009150952/https://www.stephenskilton.com/decktech_archives/23520/",
    ("live", 23490): "https://web.archive.org/web/20261009153012/http://www.decktech.net/starwarsccg/deck/23490/",
    ("live", 23459): "https://web.archive.org/web/20261009155341/http://www.decktech.net/starwarsccg/deck/23459/",
    ("live", 23458): "https://web.archive.org/web/20261009160831/http://www.decktech.net/starwarsccg/deck/23458/",
    ("skilton", 23458): "https://web.archive.org/web/20261009160958/https://www.stephenskilton.com/decktech_archives/23458/",
    ("live", 23438): "https://web.archive.org/web/20261009162620/http://www.decktech.net/starwarsccg/deck/23438/",
    ("skilton", 23438): "https://web.archive.org/web/20261009162640/https://www.stephenskilton.com/decktech_archives/23438/",
    ("live", 23407): "https://web.archive.org/web/20261009165649/http://www.decktech.net/starwarsccg/deck/23407/",
    ("live", 23385): "https://web.archive.org/web/20261009171826/http://www.decktech.net/starwarsccg/deck/23385/",
    ("skilton", 23385): "https://web.archive.org/web/20261009171851/https://www.stephenskilton.com/decktech_archives/23385/",
    ("live", 23346): "https://web.archive.org/web/20261009173622/http://www.decktech.net/starwarsccg/deck/23346/",
    ("skilton", 23346): "https://web.archive.org/web/20261009173647/https://www.stephenskilton.com/decktech_archives/23346/",
    ("live", 23334): "https://web.archive.org/web/20261009174938/http://www.decktech.net/starwarsccg/deck/23334/",
    ("skilton", 23334): "https://web.archive.org/web/20261009175025/https://www.stephenskilton.com/decktech_archives/23334/",
    ("live", 23279): "https://web.archive.org/web/20261009180809/http://www.decktech.net/starwarsccg/deck/23279/",
    ("skilton", 23279): "https://web.archive.org/web/20261009180834/https://www.stephenskilton.com/decktech_archives/23279/",
    ("live", 23249): "https://web.archive.org/web/20261009181947/http://www.decktech.net/starwarsccg/deck/23249/",
    ("skilton", 23249): "https://web.archive.org/web/20261009182042/https://www.stephenskilton.com/decktech_archives/23249/",
    ("live", 23182): "https://web.archive.org/web/20261009183912/http://www.decktech.net/starwarsccg/deck/23182/",
    ("skilton", 23182): "https://web.archive.org/web/20261009184119/https://www.stephenskilton.com/decktech_archives/23182/",
    ("live", 23152): "https://web.archive.org/web/20261009185658/http://www.decktech.net/starwarsccg/deck/23152/",
    ("skilton", 23152): "https://web.archive.org/web/20261009190102/https://www.stephenskilton.com/decktech_archives/23152/",
    ("live", 23136): "https://web.archive.org/web/20261009191325/http://www.decktech.net/starwarsccg/deck/23136/",
    ("skilton", 23136): "https://web.archive.org/web/20261009191444/https://www.stephenskilton.com/decktech_archives/23136/",
    ("live", 23127): "https://web.archive.org/web/20261009192919/http://www.decktech.net/starwarsccg/deck/23127/",
    ("skilton", 23127): "https://web.archive.org/web/20261009193028/https://www.stephenskilton.com/decktech_archives/23127/",
    ("live", 23121): "https://web.archive.org/web/20261009194323/http://www.decktech.net/starwarsccg/deck/23121/",
    ("skilton", 23121): "https://web.archive.org/web/20261009194444/https://www.stephenskilton.com/decktech_archives/23121/",
    ("live", 23087): "https://web.archive.org/web/20261009200009/http://www.decktech.net/starwarsccg/deck/23087/",
    ("skilton", 23087): "https://web.archive.org/web/20261009200115/https://www.stephenskilton.com/decktech_archives/23087/",
    ("live", 23051): "https://web.archive.org/web/20261009202036/http://www.decktech.net/starwarsccg/deck/23051/",
    ("skilton", 23051): "https://web.archive.org/web/20261009202151/https://www.stephenskilton.com/decktech_archives/23051/",
    ("live", 23036): "https://web.archive.org/web/20261009203906/http://www.decktech.net/starwarsccg/deck/23036/",
    ("skilton", 23036): "https://web.archive.org/web/20261009204008/https://www.stephenskilton.com/decktech_archives/23036/",
    ("live", 23033): "https://web.archive.org/web/20261009205018/http://www.decktech.net/starwarsccg/deck/23033/",
    ("skilton", 23033): "https://web.archive.org/web/20261009205206/https://www.stephenskilton.com/decktech_archives/23033/",
    ("live", 23021): "https://web.archive.org/web/20261009210206/http://www.decktech.net/starwarsccg/deck/23021/",
    ("skilton", 23021): "https://web.archive.org/web/20261009210230/https://www.stephenskilton.com/decktech_archives/23021/",
    ("live", 22997): "https://web.archive.org/web/20261009212016/http://www.decktech.net/starwarsccg/deck/22997/",
    ("skilton", 22997): "https://web.archive.org/web/20261009212038/https://www.stephenskilton.com/decktech_archives/22997/",
    ("live", 22978): "https://web.archive.org/web/20261009213759/http://www.decktech.net/starwarsccg/deck/22978/",
    ("skilton", 22978): "https://web.archive.org/web/20261009213819/https://www.stephenskilton.com/decktech_archives/22978/",
    ("live", 22919): "https://web.archive.org/web/20261009215140/http://www.decktech.net/starwarsccg/deck/22919/",
    ("skilton", 22919): "https://web.archive.org/web/20261009215204/https://www.stephenskilton.com/decktech_archives/22919/",
    ("live", 22886): "https://web.archive.org/web/20261009221555/http://www.decktech.net/starwarsccg/deck/22886/",
    ("skilton", 22886): "https://web.archive.org/web/20261009221623/https://www.stephenskilton.com/decktech_archives/22886/",
    ("live", 22705): "https://web.archive.org/web/20261009222923/http://www.decktech.net/starwarsccg/deck/22705/",
    ("skilton", 22705): "https://web.archive.org/web/20261009222943/https://www.stephenskilton.com/decktech_archives/22705/",
    ("live", 22701): "https://web.archive.org/web/20261010110621/http://www.decktech.net/starwarsccg/deck/22701/",
    ("skilton", 22701): "https://web.archive.org/web/20261010110725/https://www.stephenskilton.com/decktech_archives/22701/",
    ("skilton", 26555): "https://web.archive.org/web/20261008193115/https://www.stephenskilton.com/decktech_archives/26555/",
    ("skilton", 26204): "https://web.archive.org/web/20261008225051/https://www.stephenskilton.com/decktech_archives/26204/",
    ("skilton", 26273): "https://web.archive.org/web/20261009002011/https://www.stephenskilton.com/decktech_archives/26273/",
    ("skilton", 26173): "https://web.archive.org/web/20261009002240/https://www.stephenskilton.com/decktech_archives/26173/",
    ("skilton", 26448): "https://web.archive.org/web/20261009013436/https://www.stephenskilton.com/decktech_archives/26448/",
    ("skilton", 26425): "https://web.archive.org/web/20261009013545/https://www.stephenskilton.com/decktech_archives/26425/",
    ("skilton", 26421): "https://web.archive.org/web/20261009013658/https://www.stephenskilton.com/decktech_archives/26421/",
    ("skilton", 26368): "https://web.archive.org/web/20261009013806/https://www.stephenskilton.com/decktech_archives/26368/",
}

SHAW_DS_TITLE = "2002 World Championship Greg Shaw Force Lightning is TECH"
SHAW_LS_TITLE = "2002 World Championship Greg Shaw DCon2k2 Runner Up - LS"
CONSOLI_DS_TITLE = "2002 World Championship Angelo Consoli DS"
WATA_LS_TITLE = "2002 World Championship Keith Watabayashi The other TIGIH at Deciphercon"
KRUEGER_LS_TITLE = "2002 World Championship Kyle Krueger It's a Kyle deck"
JURCOVIC_DS_TITLE = "Peter Jurcovic Hold Me Thrill Me Kiss Me Kill Me"
WATA_DS_TITLE = "Keith Watabayashi G-Scum"
BLACKFORD_LS_TITLE = "Daniel Blackford Rock The Projects"
KESKIC_DS_TITLE = "Vjeko Keskic My Keskic Is This Deal Legal aka The Croatian Deal v2 1"
FIEDLER_DS_TITLE = "Justin Fiedler we will reveal ourselves to the jedi at last we will have revenge"
ZINN_LS_TITLE = "Greg Zinn Shes Virtually Back"
BOUCHARD_DS_TITLE = "Maximilien Bouchard Fear Will Keep Them In Line (V) ALPHA"
IRVING_DS_TITLE = "John Irving 3B3-888 Superstar aka Agents of pure BS"
MCLAIN_LS_TITLE = "Ryan McLain The Rx Throne Room Wrex"
SNEED_DS_TITLE = "Tulsa Mini-Open Michael Sneed Subterranean Homesick Alien"
MARSHALL_LS_TITLE = "Steve Marshall Viperstyle - Keeping The Senators Out Forever"
CROSS_LS_TITLE = "2002 Origins Open Ken Cross Squires Origins Profit"
WARREN_DS_TITLE = "Justin Warren Raging Bull (Hoostino's Hunt Down Hammer)"
BURNETT_DS_TITLE = "David Burnett JediGamler's Watto aka The Unstoppable Machine"
KRUEGER_BEACH_TITLE = "Kyle Krueger the beast on the beach v2"
VAN_WINKLE_DS_TITLE = "Seth Van Winkle Seth's Mad Huntdown Deck"
NYSTROM_DS_TITLE = "Pyry Nystrom Empire is virtually back"
KAFER_DS_TITLE = "Bill Kafer LSC TacoBill style"
BEACH_V1_TITLE = "Kyle Krueger The Beast on the Beach"
SABER_LS_TITLE = "Mike (Quione) Saber combat my way"
CARULLI_DS_TITLE = "Matt Carulli Hunt Down and Revive the SCUM"
DAVIS_DS_TITLE = "Chris Davis TDIGWATT/PIDAIAF CC Dark Deal Deck"
MCCOY_LS_TITLE = "Chris McCoy Quiet Macking of Cloud city"
GUARINO_LS_TITLE = "Mike Guarino I’m Getting Too Old For This"
MANN_LS_TITLE = "Zach Mann What my step It’s yours I should be watching"
NELSON_DS_TITLE = "Adam Nelson Droid Deal v 1 0"
ZAJIC_LS_TITLE = "James Zajic die die die"
KANGAS_LS_TITLE = "David Kangas QMC Clouds"
WEHNER_LS_TITLE = "Matt Wehner Good PunJab Hunting"
MANN_DS_TITLE = "Zach Mann None shall pass choke damn I guess you can"
BHASKER_DS_TITLE = "Arvind Bhasker Maul’s Combat"
KESKIC_LS_TITLE = "Vjeko Keskic Rumble In The Bronx With Mains"
BOWMAN_DS_TITLE = "Geoff Bowman DS"  # published title withheld (Bill 2026-10-10)
WEHNER_DS_TITLE = "Matt Wehner Court Of the Vile Gangsta - Limp Bizkit Style"
WODICKA_DS_TITLE = "Chris Wodicka 6th place Coruscant regionals"
MCCOMBIE_LS_TITLE = "Adam McCombie Throne Room Mains So Hot Right Now"
BECKHAM_LS_TITLE = "Stephen Beckham Too Hot in da Hot Tub"
WATKINS_LS_TITLE = "Uriah Watkins Testing Testing 1 2 3 (4 5 6)"
KESKIC_COURT_TITLE = "2002 Ralltiir Regionals Vjeko Keskic Court Likes Direct Damage aka Gailid Superstar"
HUNTER_DS_TITLE = "Brian Hunter Saber Combat done RIGHT aka No Mans Land"
FURGUT_LS_TITLE = "Quirin Fürgut Unbeatable EBO aka fun for everyone"
MANNING_DS_TITLE = "Jon Manning Cloud City trooper deck"
BOUCHARD_LS_TITLE = "Maximilien Bouchard WYS Choke BETA"
KESKIC_WATTO_TITLE = "Vjeko Keskic All Your Damage Belongs To Watto"
KESKIC_HTOWN_TITLE = "Vjeko Keskic H-TOWN Jedis vs NRW Jedis"
QUIONE_RST_TITLE = "Mike (Quione) Rebel Strike Team- Stay the hell of endor"
BROWN_DS_TITLE = "Wes Brown Imperial Blues"
JEWELL_LS_TITLE = "Cody Jewell ’Saber Combat My Way V1 00(UnRevised)"
ATKIN_DS_TITLE = "2002 Alderaan Regionals Clayton Atkin Atkins’ Alderaan 2nd Place TDIGWATT"
HUNTER_LS_TITLE = "2002 Vegas DPC Brian Hunter LS Senate done RIGHT aka Ghhhks Away"
HT_LS_TITLE = "Matthew Harrison-Trainor Secret Siths Profit"
JURCOVIC_WATD_TITLE = "Peter Jurcovic There Are Those Droidekas"
HAYWARD_LS_TITLE = "Taylor Hayward LS"  # published title withheld (Bill 2026-10-10)
BLAKE_DS_TITLE = "Lewis Blake YEEeeah I've got the Hoth (Big) Blues Baby"
JACOB_BHBM_TITLE = "Jacob Taylor Jacob's BHBM aka Blame Canada"
SCOTT_DS_TITLE = "Drew Scott BHBM how to kill combat"
DIAMOND_LS_TITLE = "Sam Diamond The CIA Is Trying To Kill Me"
PAPP_DS_TITLE = "Thomas Papp HDADTJ aka there are no Jedi alive"
ERTAN_LS_TITLE = "Dunya Ertan power of Rebel strike team"
HAYWARD_AITC_TITLE = "Taylor Hayward Agents In The Court"
HERRIN_LS_TITLE = "Jason Herrin Voice of the council solid"
ERTAN_HYPER_TITLE = "Dunya Ertan we dont need a sticking hypergenerator"
JEFFRIS_RST_TITLE = "Dennis Jeffris Rebel Strike Team - Da Non-Bomb"
HAYWARD_HB_TITLE = "Taylor Hayward A Hidden Base Deck"
BURNETT_SENATE_TITLE = "Chris Burnett My senate"
ERTAN_PROFIT_TITLE = "Dunya Ertan beefed up profit"
JACOB_PROFIT_TITLE = "Jacob Taylor Jacob's Profit aka Big Trouble"
ELIA_YAVIN_TITLE = "2002 Yavin 4 Regionals Kevin Elia 2002 Yavin 4 regional 2nd Place- I Am Jacks Anger"
STEVENS_LS_TITLE = "Mike Stevens ls senate"
MERRY_LS_TITLE = "Casey Merry Celebration what"
SILVA_DS_TITLE = "Darryll Silva DS"
ORIGINS_2002_WB = "https://web.archive.org/web/20020802004658/http://www.decipher.com/conventions/2002/origins.html"
HOUSTON_DPC_TR = "https://www.stephenskilton.com/decktech_archives/reports/2002-07-16-houston-texas-07-14-02-dpc-houstond3841/"
HOUSTON_DPC_TR_GH = "https://stevetotheizz0.github.io/decktech_archives/reports/2002-07-16-houston-texas-07-14-02-dpc-houstond3841/"
VEGAS_DPC_TR = "https://www.stephenskilton.com/decktech_archives/reports/2002-05-15-vegas-baby-lush-at-the-vegas-dpcd3660/"
VEGAS_DPC_TR_GH = "https://stevetotheizz0.github.io/decktech_archives/reports/2002-05-15-vegas-baby-lush-at-the-vegas-dpcd3660/"
SHAW_DS_OLD = "2002 World Championship Greg Shaw DS"
SHAW_LS_OLD = "2002 World Championship Greg Shaw LS"


def post_ref(name: str, pid: int, label: str, byline: str) -> str:
    wb = WAYBACK.get(("live", pid)) or WAYBACK.get(("skilton", pid))
    body = (
        f"[{live_deck(pid)} {label}], DeckTech ({byline}). "
        f"Preservation copies: [{skilton_deck(pid)} Stephen Skilton]; "
        f"[{github_deck(pid)} GitHub Pages]"
    )
    if wb:
        body += f"; [{wb} Wayback Machine]"
    body += "."
    return f'<ref name="{name}">{body}</ref>'


def post_source_bullets(pid: int, label: str, *, github: bool = True) -> str:
    lines = [
        f"* [{live_deck(pid)} {label}], decktech.net",
        f"* [{skilton_deck(pid)} {label}], stephenskilton.com",
    ]
    if github:
        lines.append(f"* [{github_deck(pid)} {label}] (GitHub Pages)")
    wb_live = WAYBACK.get(("live", pid))
    wb_sk = WAYBACK.get(("skilton", pid))
    if wb_live:
        lines.append(f"* [{wb_live} {label}] (Wayback of decktech.net)")
    elif wb_sk:
        lines.append(f"* [{wb_sk} {label}] (Wayback)")
    return "\n".join(lines)

# Dest notes stay in this file.
# IAO + SP dested Imperial Arrest Order and Secret Plans (two cards).
# Mob Points + YCHF dested You Cannot Hide Forever & Mobilization Points.
# Bossk in MH dested Bossk In Hound's Tooth (paired with Zuckuss In Mist Hunter).
# Green 1 / Blue 7 dested as written (no Dark File: / blueprint; not Light Green Squadron 1).
# vProphetess / vHyperwave Scan / vMolator dest original-era slips, not
# current-virtual V21 or Virtual Block (2002 original-virtual pool).
# Live dests: Prophetess (V) (Virtual Set 1) File VS1O-12-Prophetess.png;
# Molator (V) (Virtual Set 2) File VS2O-42-Molator.png;
# Hyperwave Scan (V) (Virtual Set 3) File VS3O-34-Hyperwave_Scan.png.
# Blow Parried dested Blow Parried (Reflections III combo).
# MMove Combo dested Masterful Move & Endor Occupation (Coruscant combo).
# They're Still Coming dested They're Still Coming Through!
# Accelerate Plans dested We Must Accelerate Our Plans (PC glossary "Accelerate").
# Bad Feeling (listed under Effects) dested Bad Feeling Have I (Interrupt).
# Effects "Visage x3" restates the unique start Visage; dest 1 Visage Of The Emperor.
# Prep Defenses dested Prepared Defenses.
# DVDLOTS dested Darth Vader, Dark Lord Of The Sith.
# EPP Maul dested Darth Maul With Lightsaber.
# Super Fett dested Boba Fett, Bounty Hunter.
# IG W/Gun dested IG-88 With Riot Gun.
# Dr. E + PB dested Dr. Evazan & Ponda Baba.
# Exe sites dested Executor: Meditation Chamber / Holotheatre / Docking Bay.
# Qty 60. No GEMP Download: Green 1 and Blue 7 have no blueprint.
#
# Consoli 26297 dest notes stay here.
# Published DeckTech title is German vulgar slang; dest title is
# 2002 World Championship Angelo Consoli DS.
# Ket Malis (V) dested Ket Maliss (V) (Virtual Set 3) — original-era Effect
# slip, not VB1 character.
# Reegesk (V) dested Reegesk (V) (Virtual Set 3), not VB1.
# Prophetess (V) dested Prophetess (V) (Virtual Set 1).
# FIMA 10 from outside the 60: I Find Your Lack Of Faith Disturbing (V)
# dested Virtual Set 2; Reactor Terminal (V) dested Virtual Set 3; rest
# dest Decipher Effects as printed. Consoli labeled them Defensive Shields.
# Do They Have Code Clearence? dested Do They Have A Code Clearance?
# Mobilization Point dested You Cannot Hide Forever & Mobilization Points.
# DSII Docking Bay dested Death Star II: Docking Bay.
# Blockade Flagship Bridge dested Blockade Flagship: Bridge.
# 4-Lom dested 4-LOM With Concussion Rifle.
# Boba Fett Bounty Hunter dested Boba Fett, Bounty Hunter.
# Those Rebel Won't dested Ghhhk & Those Rebels Won't Escape Us.
# Executor dested Executor (Dark).
# Bad Feeling Have I listed under Effects; dest Interrupt.
# Effects (8-1) includes the matchup-dependent (s) start (Wipe / Colo /
# No Escape); that copy is in the 60, not a 61st card.
# Start (7+1+10): 7 in-60 start cards + 1 (s) already among Effects + 10
# FIMA-outside. Qty 60 excludes the 10. No GEMP: original-VS slips.
#
# Shaw LS 26204 dest notes stay here.
# Published title DCon2k2 Runner Up - LS. Dest title
# 2002 World Championship Greg Shaw DCon2k2 Runner Up - LS.
# Shaw DS dest title 2002 World Championship Greg Shaw Force Lightning is TECH.
# There Is Good in this Obj dested There Is Good In Him.
# Unusual Amount of Fear dested An Unusual Amount Of Fear.
# Endor DB dested Endor: Landing Platform (Docking Bay).
# Endor Chirpa's Hut dested Endor: Chief Chirpa's Hut.
# Jedi Luke dested Luke Skywalker, Jedi Knight.
# Luke's Stick dested Luke's Lightsaber.
# HFTMF dested Heading For The Medical Frigate.
# vMerc Sunlet dested Merc Sunlet (ANH Effect, not original-VS).
# YISYW + Staging Areas dested Your Insight Serves You Well & Staging Areas.
# EPP Qui Gon dested Qui-Gon Jinn With Lightsaber.
# Premiere Obi dested Obi-Wan Kenobi.
# EPP Leia dested Leia With Blaster Rifle.
# Lando Scoundrel dested Lando Calrissian, Scoundrel.
# Twass Khaa dested Tawss Khaa.
# Owen + Beru dested Owen Lars & Beru Lars.
# Orrimarko dested Orrimaarko.
# Chancellor Valorum dested Supreme Chancellor Valorum.
# Phylo dested Phylo Gandish.
# Threepio dested Threepio (Endor).
# HCFalcon x2 dested Millennium Falcon (unrestricted; not unique HCATF).
# HotJedi dested Honor Of The Jedi (same HOTJ slang as Consoli 26297).
# Goo dested Goo Nee Tay.
# Scanner Techs dested Scanner Techs.
# Resilience dested A Jedi's Resilience.
# Sense + Recoil dested Sense & Recoil In Fear.
# Bith Shuffle + Reach dested The Bith Shuffle & Desperate Reach.
# SATM + BP dested Sorry About The Mess & Blaster Proficiency.
# Speak with the Jedi dested Speak With The Jedi Council.
# Free Ride + EC dested Free Ride & Endor Celebration.
# Dejarik Gameboard dested Dejarik Hologameboard.
# The beatdown tripler dested as written (no File).
# Characters listed 16 copies under a Characters 15 header; dest the named
# cards. Variable start (always Merc Sunlet; 2 of DDTA / Colo / YISYW).
# No GEMP until a unique 60.
#
# Watabayashi 26273 dest notes stay here.
# Published title The other TIGIH at Deciphercon. Dest title
# 2002 World Championship Keith Watabayashi The other TIGIH at Deciphercon.
# Author Keith "Gen" Watabayashi; YAML says he and Brad Reinhold played it
# Day 2. Slang Cards heading Good @#$% II stays in original post, off TITLE.
# AUAF listed as Starting Effect; dest Interrupt.
# SpaceportDocking Bay dested Spaceport Docking Bay.
# Home OneDocking Bay dested Home One: Docking Bay.
# NabooBoss Nass' Chambers dested Naboo: Boss Nass' Chambers.
# CoruscantJedi Council Chamber dested Coruscant: Jedi Council Chamber.
# EndorLanding Platform dested Endor: Landing Platform (Docking Bay).
# EndorChief Chirpa's Hut dested Endor: Chief Chirpa's Hut.
# Leia [v] dested Leia (V) (Virtual Set 3).
# Owen & Beru Lars dested Owen Lars & Beru Lars.
# Obi-Wan w/Lightsaber dested Obi-Wan With Lightsaber.
# Qui-Gon Jinn w/Lightsaber dested Qui-Gon Jinn With Lightsaber.
# Yoda, Master of the Force dested Yoda, Master Of The Force.
# Threepio w/His Parts Showing dested Threepio With His Parts Showing.
# Scanner Techs [v] dested Scanner Techs (V) (Virtual Set 3).
# YISYW & Staging Areas dested Your Insight Serves You Well & Staging Areas.
# Escape Pod [v] dested Escape Pod (V) (Virtual Set 2).
# Speak w/The Jedi Council dested Speak With The Jedi Council.
# OOC & Transmission Terminated dested Out Of Commission & Transmission Terminated.
# Han, Chewie and the Falcon dested Han, Chewie, And The Falcon.
# Artoo in Red 5 dested Artoo-Detoo In Red 5.
# Qty 60 exact. Variable (s) start. No GEMP until a unique 60.
#
# Krueger 26173 dest notes stay here.
# Published title It's a Kyle deck (Skilton YAML It's with curly apostrophe;
# dest TITLE uses ASCII It's). Dest title
# 2002 World Championship Kyle Krueger It's a Kyle deck.
# Author Kyle "Meto" Krueger. Both Day 1s: 4-2 miss then 5-1 2nd that Day 1.
# No objective; start Coruscant: Jedi Council Chamber.
# AUAF listed under Effects; dest Interrupt.
# Chewie, Enraged dested Chewie, Enraged.
# Lando, Scoundrel dested Lando Calrissian, Scoundrel.
# Qui-Gon, Jedi Master dested Qui-Gon Jinn, Jedi Master.
# Green pile dested Weapons.
# Alter (coruscant) dested Alter.
# I Hope Shes Alright dested I Hope She's All Right.
# Sai torr Kal Fas (v) dested Sai'torr Kal Fas (V) (Virtual Set 1).
# Escape Pod (v) dested Escape Pod (V) (Virtual Set 2).
# Wise Advise dested Wise Advice (published spelling stays in original post).
# Dont Do That Again dested Don't Do That Again.
# Affect Mind (v) dested Affect Mind (V) (Virtual Set 2).
# Traffic Control (v) dested Traffic Control (V) (Virtual Set 3).
# Defensive Shields (10) posted outside the 60; dest that pile separately.
# FIMA is not in the 60; do not invent it. Qty 60 excludes the 10.
# No GEMP: original-VS slips.
#
# Jurcovic 26448 dest notes stay here.
# Published title Hold Me Thrill Me Kiss Me Kill Me (YAML extra spaces
# collapsed on dest TITLE; original post keeps the posted spacing).
# General dest (no tournament finish). Dest title
# Peter Jurcovic Hold Me Thrill Me Kiss Me Kill Me.
# YAML tags Light; body is Dark Senate.
# My Lord Is That Legal? dested My Lord, Is That Legal?
# Coruscant Docking Bay (Special Edition) dested Coruscant: Docking Bay.
# Death Star 2 Docking Bay dested Death Star II: Docking Bay.
# Blockade Flagship Bridge dested Blockade Flagship: Bridge.
# Naboo dested Naboo (Dark) system.
# Darth Vader/Maul with Lightsaber dested With Lightsaber.
# Dr Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba.
# Orn Free Ta dested Orn Free Taa.
# Yeb Yeb Ademthorn dested Yeb Yeb Adem'thorn.
# Saber1 dested Saber 1.
# Boba Fett In Slave One dested Boba Fett In Slave I.
# This Is Outrageous dested This Is Outrageous!
# Sense & Uncertain Is The Future dested the combo.
# Sniper & Dark Strike dested the combo.
# FIMA 10 named outside the 60: Do They Have A Code Clearence dested
# Do They Have A Code Clearance?; Oppresive Enforcement dested
# Oppressive Enforcement; I Find Your Lack (V) dested VS2; Reactor
# Terminal (V) dested VS3. Qty 60 excludes the 10. No GEMP: original-VS.
#
# Watabayashi 26425 G-Scum dest notes stay here.
# General dest. Dest title Keith Watabayashi G-Scum.
# YAML tags Light; body is Dark MKOS. Ket Maliss brokeness stays published.
# TatooineDesert Heart dested Tatooine: Desert Heart.
# TatooineJabba's Palace dested Tatooine: Jabba's Palace.
# Jabba's PalaceLower Passages dested Jabba's Palace: Lower Passages.
# Jabba's Sail BargePassenger Deck dested Jabba's Sail Barge: Passenger Deck.
# Rodian [v] dested Rodian (V) (Virtual Set 3).
# Greedo [v] dested Greedo (V) (Virtual Set 3).
# Molatar [v] dested Molator (V) (Virtual Set 2).
# Ket Maliss [v] dested Ket Maliss (V) (Virtual Set 3).
# Oo-ta Goo-ta Solo [v] dested Oo-ta Goo-ta, Solo? (V) (Virtual Set 3).
# Prince Xixor dested Prince Xizor.
# IG-88 w/Riot Gun dested IG-88 With Riot Gun.
# 4-Lom dested 4-LOM With Concussion Rifle.
# Bossk w/Mortar Gun dested Bossk With Mortar Gun.
# Dengar w/Blaster Carbine dested Dengar With Blaster Carbine.
# Boba Fett w/Blaster Rifle dested Boba Fett With Blaster Rifle.
# Bossk in Hound's Tooth dested Bossk In Hound's Tooth.
# Masterful Move & Endor Occ. dested Masterful Move & Endor Occupation.
# Ghhk dested Ghhhk.
# Bad Feeling Have I listed under Effects; dest Interrupt.
# Scum & Villainy dested Scum And Villainy.
# FIMA is the starting Effect; no shields named. Do not invent a 10.
# Qty 60. No GEMP: original-VS slips.
#
# Blackford 26421 dest notes stay here.
# General dest. Dest title Daniel Blackford Rock The Projects.
# RTP dested Rescue The Princess.
# Y4 WR dested Yavin 4: Massassi War Room.
# Y4 DB dested Yavin 4: Docking Bay.
# D DB dested Death Star: Docking Bay 327.
# Detention Block Corridor dested Death Star: Detention Block Corridor.
# DODN/WA dested Do, Or Do Not & Wise Advice.
# Cell 2187 dested Cell 2187 (V) (Virtual Set 3) (strategy names (V)).
# Prisoner 2187 listed in Start and Characters; dest 2 copies (published
# arithmetic that hits 60).
# Jedi Council dested Coruscant: Jedi Council Chamber.
# Yoda's Hut dested Dagobah: Yoda's Hut.
# Dejarik Gameboard dested Dejarik Hologameboard.
# EPP Luke dested Luke With Lightsaber.
# EPP Obi dested Obi-Wan With Lightsaber.
# EPP Quiggie dested Qui-Gon Jinn With Lightsaber.
# Lando, Scoundrel dested Lando Calrissian, Scoundrel.
# Artoo dested Artoo, Brave Little Droid (listed beside R2-D2).
# R2-D2 dested R2-D2 (Artoo-Detoo) (Premiere dest; bare R2-D2 has no File).
# Han & Chewie in Falcon dested Han, Chewie, And The Falcon.
# Honor dested Honor Of The Jedi.
# How Did We Get Into This Mess dested How Did We Get Into This Mess?
# Houjix/OON dested Houjix & Out Of Nowhere.
# SATM/Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency.
# Bith Shuffle/Desperate Reach dested The Bith Shuffle & Desperate Reach.
# Escape Pod x2 dested Decipher Escape Pod (no [v]).
# AUAF lists (10 Shields) unnamed. Do not invent the 10.
# Qty 60. No GEMP: Cell 2187 (V).
#
# Keskic 26368 dest notes stay here.
# Published title My Keskic Is This Deal Legal aka The Croatian Deal v2 1
# (YAML extra spaces before aka collapsed on dest TITLE).
# General dest. Dest title
# Vjeko Keskic My Keskic Is This Deal Legal aka The Croatian Deal v2 1.
# YAML tags Light; body is Dark Deal.
# Start (7+1+10): Objective, Downtown Plaza, Prepared Defenses,
# Imperial Arrest Order & Secret Plans (one combo), I'm Sorry,
# You Cannot Hide Forever & Mobilization Points, Colo Claw Fish, plus
# Fear Is My Ally, plus 10 unnamed D-Shields outside the 60.
# Fear Is My Alley dested Fear Is My Ally; Alley stays in original post.
# Mobilization Point dested You Cannot Hide Forever & Mobilization Points.
# Tarkin (v) dested Tarkin (V) (Virtual Set 3).
# Baron Soontir Fel aka Der Rote Baron dested Baron Soontir Fel.
# Prince Xizor dested Prince Xizor.
# IG-88 dested IG-88 (Premiere; no riot gun).
# Executor dested Executor (Dark).
# Endor Occupation & Masterful Move dested Masterful Move & Endor Occupation.
# Bespin Occupation dested Cloud City Occupation (no Bespin Occupation card).
# FIMA 10 incomplete (only Code Clearance and Allegations named). Dest the
# 60 only; do not invent the other eight shields.
# Qty 60. No GEMP: Tarkin (V).

# Justin Fiedler we will reveal ourselves to the jedi at last we will have revenge.
# YAML tags Light; body is Dark LSC.
# YAML title extra spaces collapsed on dest TITLE; original post keeps them.
# Start 9: Objective, Generator Core, Generator, Deep Hatred, Prepared Defenses,
# Blaster Rack (V), IAO/SP, Wipe Them Out All Of Them, Fear Is My Ally.
# FIMA is inside the 9 and counts toward 60; do not invent Held 10.
# Blaster Rack (v) dested Blaster Rack (V) (Virtual Set 1).
# Reacotor Terminal dested Reactor Terminal (V) (Virtual Set 3).
# U-3P0 dested U-3PO (Yoo-Threepio).
# Lord Maul dested Lord Maul (Ref3), not Darth Maul With Lightsaber.
# Lord Vader dested Lord Vader (DS2), not Darth Vader With Lightsaber.
# Qty 60. No GEMP: original-VS Blaster Rack (V) + Reactor Terminal (V).

# Original-era (V) dest + File for 2002 Theed Palace + VS3 lists.
# wrap() otherwise picks Virtual Block / Virtual Shields / current-virtual.
ORIGINAL_VS = {
    "Prophetess (V)": (
        "Prophetess (V) (Virtual Set 1)",
        "VS1O-12-Prophetess.png",
    ),
    "Molator (V)": (
        "Molator (V) (Virtual Set 2)",
        "VS2O-42-Molator.png",
    ),
    "I Find Your Lack Of Faith Disturbing (V)": (
        "I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)",
        "VS2O-35-I_Find_Your_Lack_Of_Faith_Disturbing.png",
    ),
    "Hyperwave Scan (V)": (
        "Hyperwave Scan (V) (Virtual Set 3)",
        "VS3O-34-Hyperwave_Scan.png",
    ),
    "Ket Maliss (V)": (
        "Ket Maliss (V) (Virtual Set 3)",
        "VS3O-38-Ket_Maliss.png",
    ),
    "Reactor Terminal (V)": (
        "Reactor Terminal (V) (Virtual Set 3)",
        "VS3O-42-Reactor_Terminal.png",
    ),
    "Reegesk (V)": (
        "Reegesk (V) (Virtual Set 3)",
        "VS3O-43-Reegesk.png",
    ),
    "Sai'torr Kal Fas (V)": (
        "Sai'torr Kal Fas (V) (Virtual Set 1)",
        "VS1O-06-Saitorr_Kal_Fas.png",
    ),
    "Blaster Rack (V)": (
        "Blaster Rack (V) (Virtual Set 1)",
        "VS1O-09-Blaster_Rack.png",
    ),
    "Affect Mind (V)": (
        "Affect Mind (V) (Virtual Set 2)",
        "VS2O-01-Affect_Mind.png",
    ),
    "Escape Pod (V)": (
        "Escape Pod (V) (Virtual Set 2)",
        "VS2O-06-Escape_Pod.png",
    ),
    "Leia (V)": (
        "Leia (V) (Virtual Set 3)",
        "VS3O-12-Leia.png",
    ),
    "Scanner Techs (V)": (
        "Scanner Techs (V) (Virtual Set 3)",
        "VS3O-20-Scanner_Techs.png",
    ),
    "Traffic Control (V)": (
        "Traffic Control (V) (Virtual Set 3)",
        "VS3O-23-Traffic_Control.png",
    ),
    "Rodian (V)": (
        "Rodian (V) (Virtual Set 3)",
        "VS3O-45-Rodian.png",
    ),
    "Greedo (V)": (
        "Greedo (V) (Virtual Set 3)",
        "VS3O-32-Greedo.png",
    ),
    "Oo-ta Goo-ta, Solo? (V)": (
        "Oo-ta Goo-ta, Solo? (V) (Virtual Set 3)",
        "VS3O-41-Oota_Goota_Solo.png",
    ),
    "Cell 2187 (V)": (
        "Cell 2187 (V) (Virtual Set 3)",
        "VS3O-03-Cell_2187.png",
    ),
    "Tarkin (V)": (
        "Tarkin (V) (Virtual Set 3)",
        "VS3O-47-Tarkin.png",
    ),
    "Leia's Back (V)": (
        "Leia's Back (V) (Virtual Set 2)",
        "VS2O-13-Leias_Back.png",
    ),
    "Yavin Sentry (V)": (
        "Yavin Sentry (V) (Virtual Set 2)",
        "VS2O-25-Yavin_Sentry.png",
    ),
    "Fear Will Keep Them In Line (V)": (
        "Fear Will Keep Them In Line (V) (Virtual Set 2)",
        "VS2O-32-Fear_Will_Keep_Them_In_Line.png",
    ),
    "Imperial-Class Star Destroyer (V)": (
        "Imperial-Class Star Destroyer (V) (Virtual Set 2)",
        "VS2O-36-Imperial_Class_Star_Destroyer.png",
    ),
    "Luke Skywalker (V)": (
        "Luke Skywalker (V) (Virtual Set 1)",
        "VS1O-05-Luke Skywalker.png",
    ),
    "Imperial Reinforcements (V)": (
        "Imperial Reinforcements (V) (Virtual Set 2)",
        "VS2O-37-Imperial_Reinforcements.png",
    ),
    "Darth Vader (V)": (
        "Darth Vader (V) (Virtual Set 1)",
        "VS1O-10-Darth_Vader.png",
    ),
    "Commander Praji (V)": (
        "Commander Praji (V) (Virtual Set 2)",
        "VS2O-28-Commander_Praji.png",
    ),
    "The Empire's Back (V)": (
        "The Empire's Back (V) (Virtual Set 2)",
        "VS2O-48-The_Empires_Back.png",
    ),
    "Black 2 (V)": (
        "Black 2 (V) (Virtual Set 1)",
        "VS1O-08-Black_2.png",
    ),
    "Death Star Sentry (V)": (
        "Death Star Sentry (V) (Virtual Set 2)",
        "VS2O-29-Death_Star_Sentry.png",
    ),
    "Rycar Ryjerd (V)": (
        "Rycar Ryjerd (V) (Virtual Set 2)",
        "VS2O-21-Rycar_Ryjerd.png",
    ),
    "K'lor'slug (V)": (
        "K'lor'slug (V) (Virtual Set 2)",
        "VS2O-12-Klorslug.png",
    ),
    "Bo Shek (V)": (
        "Bo Shek (V) (Virtual Set 1)",
        "VS1O-01-Bo Shek.png",
    ),
    "BoShek (V)": (
        "Bo Shek (V) (Virtual Set 1)",
        "VS1O-01-Bo Shek.png",
    ),
    "Han's Heavy Blaster Pistol (V)": (
        "Han's Heavy Blaster Pistol (V) (Virtual Set 1)",
        "VS1O-04-Hans Heavy Blaster Pistol.png",
    ),
}

SHAW_DS = [
    (1, "Hunt Down And Destroy The Jedi", "OBJECTIVE"),
    (1, "Executor: Meditation Chamber", "LOCATION"),
    (1, "Executor: Holotheatre", "LOCATION"),
    (1, "Visage Of The Emperor", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order", "EFFECT"),
    (1, "Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Carida", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Docking Bay", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (2, "Lord Vader", "CHARACTER"),
    (2, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (3, "Darth Maul With Lightsaber", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (2, "Janus Greejatus", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Prophetess (V)", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Green 1", "STARSHIP"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Blue 7", "STARSHIP"),
    (2, "Blizzard 4", "VEHICLE"),
    (2, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (2, "Maul's Sith Infiltrator", "STARSHIP"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Hyperwave Scan (V)", "EFFECT"),
    (1, "Molator (V)", "EFFECT"),
    (1, "Enter The Bureaucrat", "EFFECT"),
    (1, "Bad Feeling Have I", "INTERRUPT"),
    (2, "Blow Parried", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Masterful Move", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Monnok", "INTERRUPT"),
    (1, "Force Field", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (2, "They're Still Coming Through!", "INTERRUPT"),
]

CONSOLI_DS = [
    (1, "No Money, No Parts, No Deal!", "OBJECTIVE"),
    (1, "Tatooine: Watto's Junkyard", "LOCATION"),
    (1, "Tatooine: Mos Espa", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Ket Maliss (V)", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Rendili", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (3, "Watto", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Reegesk (V)", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Bossk With Mortar Gun", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Prophetess (V)", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Executor", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Tempest Scout 6", "VEHICLE"),
    (1, "Wipe Them Out, All Of Them", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Bad Feeling Have I", "INTERRUPT"),
    (1, "The Phantom Menace", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Search And Destroy", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (3, "Imperial Barrier", "INTERRUPT"),
    (3, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Force Field", "INTERRUPT"),
    (1, "Projective Telepathy", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
]

CONSOLI_FIMA = [
    (1, "I Find Your Lack Of Faith Disturbing (V)", "DEFENSIVE_SHIELD"),
    (1, "A Useless Gesture", "EFFECT"),
    (1, "Do They Have A Code Clearance?", "EFFECT"),
    (1, "Resistance", "EFFECT"),
    (1, "Battle Order", "EFFECT"),
    (1, "Reactor Terminal (V)", "DEFENSIVE_SHIELD"),
    (1, "There Is No Try", "EFFECT"),
    (1, "Allegations Of Corruption", "EFFECT"),
    (1, "Secret Plans", "EFFECT"),
    (1, "Come Here You Big Coward", "EFFECT"),
]

SHAW_LS = [
    (1, "There Is Good In Him", "OBJECTIVE"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (3, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Obi-Wan Kenobi", "CHARACTER"),
    (2, "Leia With Blaster Rifle", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Tawss Khaa", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Owen Lars & Beru Lars", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Supreme Chancellor Valorum", "CHARACTER"),
    (1, "Phylo Gandish", "CHARACTER"),
    (1, "Threepio", "CHARACTER"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (2, "Millennium Falcon", "STARSHIP"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Endor: Chief Chirpa's Hut", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Dejarik Hologameboard", "LOCATION"),
    (1, "Merc Sunlet", "EFFECT"),
    (1, "I Feel The Conflict", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Your Insight Serves You Well & Staging Areas", "EFFECT"),
    (1, "I Can't Believe He's Gone", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Scanner Techs", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Don't Do That Again", "INTERRUPT"),
    (2, "Balanced Attack", "INTERRUPT"),
    (3, "Escape Pod", "INTERRUPT"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Houjix", "INTERRUPT"),
    (1, "Grimtaash", "INTERRUPT"),
    (1, "On The Edge", "INTERRUPT"),
    (3, "Sense & Recoil In Fear", "INTERRUPT"),
    (2, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "Speak With The Jedi Council", "INTERRUPT"),
    (2, "Free Ride & Endor Celebration", "INTERRUPT"),
    (1, "Were You Looking For Me?", "INTERRUPT"),
    (1, "The beatdown tripler", "INTERRUPT"),
]

WATA_LS = [
    (1, "There Is Good In Him", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "INTERRUPT"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Naboo: Boss Nass' Chambers", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Endor: Chief Chirpa's Hut", "LOCATION"),
    (1, "Leia (V)", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Supreme Chancellor Valorum", "CHARACTER"),
    (1, "Owen Lars & Beru Lars", "CHARACTER"),
    (1, "Tawss Khaa", "CHARACTER"),
    (1, "Phylo Gandish", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (3, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (3, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Sando Aqua Monster", "EFFECT"),
    (1, "Your Insight Serves You Well & Staging Areas", "EFFECT"),
    (1, "Insurrection & Aim High", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "I Feel The Conflict", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Scanner Techs (V)", "EFFECT"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Houjix", "INTERRUPT"),
    (2, "Escape Pod (V)", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Sense", "INTERRUPT"),
    (1, "Lost In The Wilderness", "INTERRUPT"),
    (2, "Fallen Portal", "INTERRUPT"),
    (1, "Free Ride & Endor Celebration", "INTERRUPT"),
    (2, "Wesa Gotta Grand Army", "INTERRUPT"),
    (1, "Speak With The Jedi Council", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Clash Of Sabers", "INTERRUPT"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Blaster Deflection", "INTERRUPT"),
    (2, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (2, "Artoo-Detoo In Red 5", "STARSHIP"),
]

KRUEGER_LS = [
    (1, "Coruscant: Docking Bay", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Dejarik Hologameboard", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Naboo: Battle Plains", "LOCATION"),
    (1, "Naboo: Boss Nass' Chambers", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Jar Jar Binks", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (3, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Owen Lars & Beru Lars", "CHARACTER"),
    (1, "Phylo Gandish", "CHARACTER"),
    (2, "Qui-Gon Jinn, Jedi Master", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (2, "Alter", "INTERRUPT"),
    (1, "Blaster Deflection", "INTERRUPT"),
    (3, "Escape Pod (V)", "INTERRUPT"),
    (1, "Fallen Portal", "INTERRUPT"),
    (1, "Free Ride & Endor Celebration", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Houjix", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (3, "Sense & Recoil In Fear", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (3, "Wesa Gotta Grand Army", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "INTERRUPT"),
    (1, "A Vergence In The Force", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "I Hope She's All Right", "EFFECT"),
    (1, "Lightsaber Proficiency", "EFFECT"),
    (1, "Insurrection & Aim High", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Sando Aqua Monster", "EFFECT"),
    (1, "Your Insight Serves You Well", "EFFECT"),
]

KRUEGER_SHIELDS = [
    (1, "Affect Mind (V)", "DEFENSIVE_SHIELD"),
    (1, "A Tragedy Has Occurred", "DEFENSIVE_SHIELD"),
    (1, "Battle Plan", "DEFENSIVE_SHIELD"),
    (1, "Don't Do That Again", "DEFENSIVE_SHIELD"),
    (1, "He Can Go About His Business", "DEFENSIVE_SHIELD"),
    (1, "Planetary Defenses", "DEFENSIVE_SHIELD"),
    (1, "Traffic Control (V)", "DEFENSIVE_SHIELD"),
    (1, "Ultimatum", "DEFENSIVE_SHIELD"),
    (1, "Wise Advice", "DEFENSIVE_SHIELD"),
    (1, "Your Insight Serves You Well", "DEFENSIVE_SHIELD"),
]

JURCOVIC_DS = [
    (1, "My Lord, Is That Legal?", "OBJECTIVE"),
    (1, "Coruscant: Galactic Senate", "LOCATION"),
    (1, "Coruscant: Docking Bay", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Naboo", "LOCATION"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (3, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (2, "Baron Soontir Fel", "CHARACTER"),
    (3, "Lott Dod", "CHARACTER"),
    (2, "Orn Free Taa", "CHARACTER"),
    (2, "Tikkes", "CHARACTER"),
    (1, "Yeb Yeb Adem'thorn", "CHARACTER"),
    (1, "Aks Moe", "CHARACTER"),
    (1, "Toonbuck Toora", "CHARACTER"),
    (1, "Edcel Bar Gane", "CHARACTER"),
    (1, "Baskol Yeesrim", "CHARACTER"),
    (1, "Chimaera", "STARSHIP"),
    (2, "Saber 1", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (2, "SFS L-s9.3 Laser Cannons", "WEAPON"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Begin Landing Your Troops", "EFFECT"),
    (1, "Combat Response", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Ability, Ability, Ability", "EFFECT"),
    (1, "Our Blockade Is Perfectly Legal", "EFFECT"),
    (1, "Accepting Trade Federation Control", "EFFECT"),
    (1, "Motion Supported", "EFFECT"),
    (1, "This Is Outrageous!", "EFFECT"),
    (1, "Senate Hovercam", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (1, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Squabbling Delegates", "INTERRUPT"),
    (1, "Shut Him Up Or Shut Him Down", "INTERRUPT"),
    (1, "Limited Resources", "INTERRUPT"),
    (3, "Sense & Uncertain Is The Future", "INTERRUPT"),
]

JURCOVIC_FIMA = [
    (1, "A Useless Gesture", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Do They Have A Code Clearance?", "DEFENSIVE_SHIELD"),
    (1, "Oppressive Enforcement", "DEFENSIVE_SHIELD"),
    (1, "Secret Plans", "DEFENSIVE_SHIELD"),
    (1, "You Cannot Hide Forever", "DEFENSIVE_SHIELD"),
    (1, "I Find Your Lack Of Faith Disturbing (V)", "DEFENSIVE_SHIELD"),
    (1, "Reactor Terminal (V)", "DEFENSIVE_SHIELD"),
]

WATA_DS = [
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "My Kind Of Scum", "OBJECTIVE"),
    (1, "Tatooine: Desert Heart", "LOCATION"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Jabba's Palace: Lower Passages", "LOCATION"),
    (1, "Jabba's Sail Barge: Passenger Deck", "LOCATION"),
    (1, "Gailid", "CHARACTER"),
    (1, "Ephant Mon", "CHARACTER"),
    (1, "Boelo", "CHARACTER"),
    (1, "Bib Fortuna", "CHARACTER"),
    (1, "Mighty Jabba", "CHARACTER"),
    (1, "Mercenary Pilot", "CHARACTER"),
    (2, "Rodian (V)", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Chall Bekan", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Bossk With Mortar Gun", "CHARACTER"),
    (2, "Dengar With Blaster Carbine", "CHARACTER"),
    (2, "Boba Fett With Blaster Rifle", "CHARACTER"),
    (4, "Greedo (V)", "CHARACTER"),
    (1, "Well Guarded", "EFFECT"),
    (1, "Power Of The Hutt", "EFFECT"),
    (1, "Ket Maliss (V)", "EFFECT"),
    (1, "Molator (V)", "EFFECT"),
    (1, "Hutt Influence", "EFFECT"),
    (1, "Bad Feeling Have I", "INTERRUPT"),
    (1, "First Strike", "EFFECT"),
    (2, "Scum And Villainy", "EFFECT"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (2, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Stinger", "STARSHIP"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (2, "Stunning Leader", "INTERRUPT"),
    (2, "None Shall Pass", "INTERRUPT"),
    (1, "Imperial Barrier", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Abyssin Ornament", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Res Luk Ra'auf", "INTERRUPT"),
    (1, "Oo-ta Goo-ta, Solo? (V)", "INTERRUPT"),
    (2, "Jabba's Through With You", "INTERRUPT"),
    (1, "Jabba's Sail Barge", "VEHICLE"),
]

BLACKFORD_LS = [
    (1, "Rescue The Princess", "OBJECTIVE"),
    (1, "Yavin 4: Massassi War Room", "LOCATION"),
    (1, "Yavin 4: Docking Bay", "LOCATION"),
    (1, "Death Star: Docking Bay 327", "LOCATION"),
    (1, "Death Star: Detention Block Corridor", "LOCATION"),
    (2, "Prisoner 2187", "CHARACTER"),
    (1, "An Unusual Amount Of Fear", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Rycar Ryjerd", "CHARACTER"),
    (1, "Do, Or Do Not & Wise Advice", "INTERRUPT"),
    (1, "Cell 2187 (V)", "EFFECT"),
    (1, "Dejarik Hologameboard", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Dagobah: Yoda's Hut", "LOCATION"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Melas", "CHARACTER"),
    (1, "Tawss Khaa", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "R2-D2 (Artoo-Detoo)", "CHARACTER"),
    (1, "Artoo, Brave Little Droid", "CHARACTER"),
    (2, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Reflection", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Legendary Starfighter", "EFFECT"),
    (4, "How Did We Get Into This Mess?", "INTERRUPT"),
    (3, "Rebel Barrier", "INTERRUPT"),
    (2, "Fallen Portal", "INTERRUPT"),
    (4, "Leia's Back", "INTERRUPT"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (2, "Escape Pod", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (2, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Life Debt", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (1, "Speak With The Jedi Council", "INTERRUPT"),
]

KESKIC_DS = [
    (1, "This Deal Is Getting Worse All The Time", "OBJECTIVE"),
    (1, "Cloud City: Downtown Plaza", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "I'm Sorry", "INTERRUPT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Bespin", "LOCATION"),
    (1, "Bespin: Cloud City", "LOCATION"),
    (1, "Cloud City: Carbonite Chamber", "LOCATION"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (2, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (2, "Tarkin (V)", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Bane Malar", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Baron Soontir Fel", "CHARACTER"),
    (1, "IG-88", "CHARACTER"),
    (1, "Executor", "STARSHIP"),
    (1, "Stinger", "STARSHIP"),
    (1, "Saber 1", "STARSHIP"),
    (1, "Virago", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Obsidian 8", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Battle Deployment", "ADMIRALS_ORDER"),
    (3, "Imperial Command", "INTERRUPT"),
    (1, "Stunning Leader", "INTERRUPT"),
    (2, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Force Field", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (1, "Overload", "INTERRUPT"),
    (1, "The Phantom Menace", "EFFECT"),
    (1, "Cloud City Occupation", "EFFECT"),
    (1, "Dark Deal", "EFFECT"),
    (3, "They Must Never Again Leave This City", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "Combat Response", "EFFECT"),
]

FIEDLER_DS = [
    (1, "Let Them Make The First Move", "OBJECTIVE"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Deep Hatred", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Blaster Rack (V)", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Wipe Them Out, All Of Them", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (3, "Lord Maul", "CHARACTER"),
    (2, "Lord Vader", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (2, "Darth Sidious", "CHARACTER"),
    (2, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Thok & Thug", "CHARACTER"),
    (1, "Feltipern Trevagg", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "U-3PO (Yoo-Threepio)", "CHARACTER"),
    (1, "Aurra Sing", "CHARACTER"),
    (2, "Vader's Lightsaber", "WEAPON"),
    (2, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Aurra Sing's Blaster Rifle", "WEAPON"),
    (3, "Intruder Missile", "WEAPON"),
    (1, "Double Laser Cannon", "WEAPON"),
    (1, "Blow Parried", "INTERRUPT"),
    (1, "Weapon Levitation", "INTERRUPT"),
    (2, "Force Field", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (2, "It's Worse", "INTERRUPT"),
    (1, "Reactor Terminal (V)", "EFFECT"),
    (3, "Sense", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (1, "Weapon Of An Ungrateful Son", "INTERRUPT"),
    (1, "Stunning Leader", "INTERRUPT"),
    (2, "The Phantom Menace", "EFFECT"),
    (2, "Vader's Obsession", "INTERRUPT"),
    (1, "The Circle Is Now Complete", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
]

# Qty 60. 10 Defensive Shields posted outside the 60 (AUAOF). No invented Held 10.
# Leia's Back (V) dest original VS2. Posted "Yavin 4 Sentry (v)" dests Yavin Sentry (V) (VS2).
# Alter lost dests Alter (Coruscant) Lost Interrupt. I Did It dests I Did It!.
# Format Premiere - Original VS2 (13 Aug 2002; VS2 legal 1 Jun 2002; VS3 legal 20 Sep 2002).
ZINN_LS = [
    (1, "Rescue The Princess", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Yavin 4: Massassi War Room", "LOCATION"),
    (1, "Yavin 4: Docking Bay", "LOCATION"),
    (1, "Death Star: Docking Bay 327", "LOCATION"),
    (1, "Death Star: Detention Block Corridor", "LOCATION"),
    (1, "Prisoner 2187", "CHARACTER"),
    (1, "Podrace Prep", "INTERRUPT"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Anakin's Podracer", "PODRACER"),
    (1, "Echo Base Garrison", "EFFECT"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Naboo: Boss Nass' Chambers", "LOCATION"),
    (1, "Naboo: Battle Plains", "LOCATION"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (2, "8D8", "CHARACTER"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Gold Leader In Gold 1", "STARSHIP"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "I Did It!", "EPIC_EVENT"),
    (1, "Life Debt", "INTERRUPT"),
    (4, "A Jedi's Resilience", "INTERRUPT"),
    (3, "First Aid", "INTERRUPT"),
    (3, "Leia's Back (V)", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (2, "Speak With The Jedi Council", "INTERRUPT"),
    (3, "Wesa Gotta Grand Army", "INTERRUPT"),
    (3, "Too Close For Comfort", "INTERRUPT"),
    (3, "Sense", "INTERRUPT"),
    (2, "Alter (Coruscant)", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Inconsequential Barriers", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (1, "We Wish To Board At Once", "INTERRUPT"),
]

ZINN_SHIELDS = [
    (1, "A Tragedy Has Occurred", "DEFENSIVE_SHIELD"),
    (1, "Affect Mind (V)", "DEFENSIVE_SHIELD"),
    (1, "Aim High", "DEFENSIVE_SHIELD"),
    (1, "Battle Plan", "DEFENSIVE_SHIELD"),
    (1, "Don't Do That Again", "DEFENSIVE_SHIELD"),
    (1, "Ounee Ta", "DEFENSIVE_SHIELD"),
    (1, "Planetary Defenses", "DEFENSIVE_SHIELD"),
    (1, "Wise Advice", "DEFENSIVE_SHIELD"),
    (1, "Yavin Sentry (V)", "DEFENSIVE_SHIELD"),
    (1, "Your Insight Serves You Well", "DEFENSIVE_SHIELD"),
]

# Bouchard 24965 dest notes stay here.
# Published title Fear Will Keep Them In Line (V) ALPHA. YAML extra space
# before ALPHA stays off dest TITLE. YAML tags Light; body is Dark SYCFA.
# General dest (no tournament finish). Dest title
# Maximilien Bouchard Fear Will Keep Them In Line (V) ALPHA.
# Author Maximilien "Kiriel" Bouchard.
# SYCFA dested Set Your Course For Alderaan.
# Mobilization Points & YCHFE dested You Cannot Hide Forever & Mobilization Points.
# Imperial Arrest Order & Secret Plans dested the combo (wrap finds File).
# D DB dested Death Star: Docking Bay 327.
# D War room dested Death Star: War Room.
# Exec DB dested Executor: Docking Bay.
# Fear will keep them in line V dested Fear Will Keep Them In Line (V) (VS2).
# Imperial-class star destroyer V dested Imperial-Class Star Destroyer (V) (VS2).
# Zuckass dested Zuckuss In Mist Hunter.
# EPP Maul dested Darth Maul With Lightsaber.
# EPP Vader dested Darth Vader With Lightsaber.
# Boba Fett Bounty Hunter dested Boba Fett, Bounty Hunter.
# Commamder Merrejk dested Commander Merrejk.
# Janus dested Janus Greejatus.
# Force Lighning dested Force Lightning.
# Ghhk & those rebel won't dested Ghhhk & Those Rebels Won't Escape Us.
# There will be hell to pay dested There'll Be Hell To Pay.
# FIMA is inside Starting (9) and counts. Do not invent Held 10.
# Posted qty 61 (Starting 9 + Location 5 + AO 1 + Effect 7 + Starship 7
# + Characters 17 + Interrupt 15). Dest as published. No GEMP: original-VS.
# Format Premiere - Original VS2 (10 Aug 2002; VS2 legal 1 Jun 2002;
# VS3 legal 20 Sep 2002).
BOUCHARD_DS = [
    (1, "Set Your Course For Alderaan", "OBJECTIVE"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Oppressive Enforcement", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Death Star", "LOCATION"),
    (1, "Death Star: Docking Bay 327", "LOCATION"),
    (1, "Alderaan", "LOCATION"),
    (1, "Death Star: War Room", "LOCATION"),
    (1, "Kiffex", "LOCATION"),
    (1, "Rendili", "LOCATION"),
    (1, "Corulag", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "We're In Attack Position Now", "ADMIRALS_ORDER"),
    (1, "Blast Door Controls", "EFFECT"),
    (2, "Fear Will Keep Them In Line (V)", "EFFECT"),
    (1, "There'll Be Hell To Pay", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "A Bright Center To The Universe", "EFFECT"),
    (1, "Executor", "STARSHIP"),
    (2, "Chimaera", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Devastator", "STARSHIP"),
    (2, "Imperial-Class Star Destroyer (V)", "STARSHIP"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (4, "Emperor Palpatine", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "M'iiyoom Onith", "CHARACTER"),
    (4, "Imperial Command", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (2, "Sense", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Twi'lek Advisor", "INTERRUPT"),
    (1, "Force Field", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (2, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
]


# Fear is My Ally (w/ 10 good sheilds) dested Fear Is My Ally. Shields unnamed;
# dest the 60 only. Do not invent Held 10. FIMA is inside Starting (9) and counts.
# Agents of the Black Sun/ dested Agents Of Black Sun / Vengeance Of The Dark Prince.
# Coruscant (from SE) dested Coruscant (Dark).
# Coruscant Imperial City dested Coruscant: Imperial City (pageid 5653).
# Prepared Defences dested Prepared Defenses.
# Imperial Arrest Order/SP dested Imperial Arrest Order & Secret Plans.
# Mobilization Points/YCHF dested You Cannot Hide Forever & Mobilization Points.
# Crush the Rebelion dested Crush The Rebellion.
# Coruscant DB dested Coruscant: Docking Bay.
# Blockade Flagship DB dested Blockade Flagship: Docking Bay.
# Blockade Flagship Bridge dested Blockade Flagship: Bridge.
# IG-88 w/ Roit Gun dested IG-88 With Riot Gun.
# Bossk w/ Mortar Gun dested Bossk With Mortar Gun.
# Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine.
# 4-Lom w/ Concussion Rifel dested 4-LOM With Concussion Rifle.
# Boba Fett in Slave 1 dested Boba Fett In Slave I.
# Bossk in Hound's Tooth dested Bossk In Hound's Tooth.
# Bad Feeling Have I dested INTERRUPT (posted under Effects).
# Projective Telepethy dested Projective Telepathy.
# They're still coming through dested They're Still Coming Through!.
# Sense & RiF dested Sense & Recoil In Fear (Light combo File Ref2-L;
# posted as a Dark interrupt).
# YAML extra space before aka stays off dest TITLE.
# YAML tagged Light; body is Dark Agents Of Black Sun.
# Qty 60. Format Premiere - Original VS2 (7 Aug 2002; VS2 legal 1 Jun 2002;
# VS3 legal 20 Sep 2002). No (V) cards. No GEMP: original-VS format by legal day
# (open_no_virtual / no original-VS2 GEMP code; ingest consistency with 24965/25015).
# Starting Xizor + Characters Xizor dest qty 2.
IRVING_DS = [
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Agents Of Black Sun", "OBJECTIVE"),
    (1, "Coruscant", "LOCATION"),
    (1, "Coruscant: Imperial City", "LOCATION"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (1, "Coruscant: Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Carida", "LOCATION"),
    (5, "Emperor Palpatine", "CHARACTER"),
    (3, "Guri", "CHARACTER"),
    (2, "3B3-888", "CHARACTER"),
    (2, "IG-88 With Riot Gun", "CHARACTER"),
    (2, "Vigo", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Bossk With Mortar Gun", "CHARACTER"),
    (1, "Dengar With Blaster Carbine", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "P-60", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (2, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (2, "Bad Feeling Have I", "INTERRUPT"),
    (1, "Broken Concentration", "EFFECT"),
    (3, "Force Lightning", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (2, "Projective Telepathy", "INTERRUPT"),
    (2, "They're Still Coming Through!", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (2, "Sense & Recoil In Fear", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (1, "Oh, Switch Off", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
]

# 24807 McLain LS. Dest the published Cards list (59 as posted; Revolution x
# with no number dested x1). Do not dest later tourney-change paragraphs
# (Obi hut out / Shmi in, Plo Koon, Bravo Fighter, They Win This Round,
# Jedi Presence, 2x HCF, WWTBAO x2). Unnamed shields stay unpublished.
# EPP Luke dested Luke With Lightsaber (not Luke Skywalker With Lightsaber).
# Jedi's Resilience dested A Jedi's Resilience.
# Sense & Uncertain of the Future dested Dark combo Sense & Uncertain Is The Future.
# We Must Accelerate our plans dested We Wish To Board At Once (Light; strategy names WWTBAO).
# Qty 1 as published Cards list.
MCLAIN_LS = [
    (1, "Yavin 4: Massassi Throne Room", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Rendezvous Point", "LOCATION"),
    (1, "Tatooine: Obi-Wan's Hut", "LOCATION"),
    (1, "Dagobah: Yoda's Hut", "LOCATION"),
    (1, "Home One: War Room", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Hoth: Echo Command Center (War Room)", "LOCATION"),
    (1, "Coruscant: Docking Bay", "LOCATION"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (2, "Leia, Rebel Princess", "CHARACTER"),
    (1, "B'omarr Monk", "CHARACTER"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (2, "Life Debt", "INTERRUPT"),
    (2, "Were You Looking For Me?", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (2, "Tunnel Vision", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (4, "Sense & Uncertain Is The Future", "INTERRUPT"),
    (2, "Alter", "INTERRUPT"),
    (1, "We Wish To Board At Once", "INTERRUPT"),
    (1, "We're Doomed", "INTERRUPT"),
    (2, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Insurrection & Aim High", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Your Insight Serves You Well & Staging Areas", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Revolution", "EFFECT"),
    (2, "Goo Nee Tay", "EFFECT"),
    (1, "Leia's Blaster Rifle", "WEAPON"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (1, "Home One", "STARSHIP"),
]

# 24783 Sneed DS. YAML tagged Light; body Dark Senate. Named Tulsa Mini-Open
# win → tournament dest. FIMA inside START (8) counts toward 60. Qty 60.
# Yeb Yeb Adem&þ dested Yeb Yeb Adem'thorn.
# Orn Free Ta dested Orn Free Taa.
# Dr. Evazan & Ponda Boba dested Dr. Evazan & Ponda Baba.
# This Is Outrageous dested This Is Outrageous!.
# Alter (Coruscant) dested Alter (Dark) (Coruscant) File Cor-D-alter.gif.
# Alter (Premiere) dested Alter (Dark).
# Sense & Uncertain Is The Future Dark combo File (native Dark 60).
# Phantom Menace / Begin Landing Your Troops / Crush The Rebellion are
# PD-deployed — do not guess them as Starting Effect.
# Skip GEMP (printed-only POVS2). Do not dest brother Dantooine regionals
# / local tourney extra rows. Do not dest onto Admiral Piett card pageid 137.
SNEED_DS = [
    (1, "My Lord, Is That Legal?", "OBJECTIVE"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Coruscant: Galactic Senate", "LOCATION"),
    (1, "Tatooine: Desert Landing Site", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "The Phantom Menace", "EFFECT"),
    (1, "Begin Landing Your Troops", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (1, "Coruscant", "LOCATION"),
    (1, "Coruscant: Imperial Square", "LOCATION"),
    (1, "Dagobah: Cave", "LOCATION"),
    (2, "Darth Maul", "CHARACTER"),
    (1, "Darth Maul, Young Apprentice", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (1, "Rune Haako", "CHARACTER"),
    (2, "Lott Dod", "CHARACTER"),
    (1, "Toonbuck Toora", "CHARACTER"),
    (2, "Edcel Bar Gane", "CHARACTER"),
    (2, "Orn Free Taa", "CHARACTER"),
    (2, "Yeb Yeb Adem'thorn", "CHARACTER"),
    (1, "Tikkes", "CHARACTER"),
    (1, "Passel Argente", "CHARACTER"),
    (1, "Aks Moe", "CHARACTER"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Executor", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (2, "Squabbling Delegates", "INTERRUPT"),
    (1, "Elis Helrot", "INTERRUPT"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (2, "Imperial Command", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (2, "Sense & Uncertain Is The Future", "INTERRUPT"),
    (1, "Alter (Coruscant)", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
    (2, "Presence Of The Force", "EFFECT"),
    (1, "Ability, Ability, Ability", "EFFECT"),
    (2, "Senate Hovercam", "EFFECT"),
    (1, "Accepting Trade Federation Control", "EFFECT"),
    (1, "Our Blockade Is Perfectly Legal", "EFFECT"),
    (1, "This Is Outrageous!", "EFFECT"),
    (1, "Motion Supported", "EFFECT"),
    (1, "Maul's Double-Bladed Lightsaber", "WEAPON"),
]

# 24688 Marshall LS. YAML tagged Light; body Light QMC. General dest (unnamed
# tournament ruling — do not invent event/finish). Qty 60.
# CC Docking Bay dested Cloud City: Platform 327 (Docking Bay) (Light docking bay;
# East Platform is Dark-only).
# CC Leia's Hut dested Cloud City: Guest Quarters (QMC start site; Leia Guest
# Quarters slang; no Cloud City Hut).
# Chewie, Engraged dested Chewie, Enraged.
# Luke Skywalker (V) dested Luke Skywalker (V) (Virtual Set 1)
# File VS1O-05-Luke Skywalker.png.
# X-Wing Laser Cannons dested X-wing Laser Cannon.
# Alter (Lost) dested Alter (Coruscant) Light File Cor-L-alter.gif.
# Blast The Door, Kid dested Blast The Door, Kid!.
# Off The Edge dested On The Edge.
# Get To Your Ships dested Get To Your Ships!.
# Keeping The Senators Out Forever dested Keeping The Empire Out Forever
# (published deck TITLE keeps Senators joke).
# AUOF inside EFFECTS counts toward 60; do not invent Held 10.
# Chasm dested Chasm Effect (not Cloud City: Chasm Walkway).
# Get To Your Ships / Keeping The Empire Out Forever are HFTMF-deployed —
# do not guess them as Starting Effect.
# Skip GEMP (original-VS1 Luke). Do not dest onto a card title. BlackViper MISS
# (not a card). Format Premiere - Original VS2 (30 Jul 2002; VS2 legal 1 Jun 2002).
MARSHALL_LS = [
    (1, "Quiet Mining Colony", "OBJECTIVE"),
    (1, "Bespin", "LOCATION"),
    (1, "Cloud City: Platform 327 (Docking Bay)", "LOCATION"),
    (1, "Cloud City: Guest Quarters", "LOCATION"),
    (1, "Cloud City: North Corridor", "LOCATION"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (4, "Arcona", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (1, "Luke Skywalker (V)", "CHARACTER"),
    (1, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Officer Dolphe", "CHARACTER"),
    (1, "Pucumir Thryss", "CHARACTER"),
    (1, "Queen Amidala", "CHARACTER"),
    (1, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Ric Olie, Bravo Leader", "CHARACTER"),
    (1, "Tawss Khaa", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Bravo 1", "STARSHIP"),
    (1, "Bravo 2", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "X-wing Laser Cannon", "WEAPON"),
    (1, "Landing Claw", "DEVICE"),
    (1, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Ambush", "INTERRUPT"),
    (1, "All Wings Report In & Darklighter Spin", "INTERRUPT"),
    (1, "Alter (Coruscant)", "INTERRUPT"),
    (1, "Blast The Door, Kid!", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (1, "It Could Be Worse", "INTERRUPT"),
    (1, "Nar Shaddaa Wind Chimes & Out Of Somewhere", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (2, "Path Of Least Resistance & Revealed", "INTERRUPT"),
    (1, "Wookiee Strangle", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (2, "Cloud City Celebration", "EFFECT"),
    (1, "Get To Your Ships!", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Keeping The Empire Out Forever", "EFFECT"),
    (1, "Legendary Starfighter", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Projection Of A Skywalker", "EFFECT"),
    (1, "Chasm", "EFFECT"),
    (1, "You've Got A Lot Of Guts Coming Here", "EFFECT"),
]

# 24668 Cross LS. YAML tagged Light; body Light Profit. Tournament dest:
# Origins Open, 3-0, 7th place. Dest title
# 2002 Origins Open Ken Cross Squires Origins Profit.
# Author Ken "Squires" Cross. Handle Squires is not a card.
# Qty 60. Unnamed 10 D-shields dest 60 only; do not invent Held 10.
# Master Luke x2 dested Luke Skywalker, Jedi Knight (2002 slang; wrap of
# Master Luke is EJP unique Master Luke — dest LSJK; qty 2 as published).
# naked 3po dested C-3PO (See-Threepio) Premiere File Premiere-L-c3po.gif
# (C-3PO wrap NOIMG redirect; See-Threepio wrap is EJP).
# R3 lando dested Lando Calrissian (Cloud City). lando w/ ax dested
# Lando With Vibro-Ax. hologame board dested Dejarik Hologameboard.
# bith shuffle/desperate reach dested The Bith Shuffle & Desperate Reach.
# grimtash dested Grimtaash. It's a trap dested It's A Trap!.
# profit dested You Can Either Profit By This.... i did it dested I Did It!.
# sal torr kal fas(V) dested Sai'torr Kal Fas (V) (Virtual Set 1).
# escape pod(v) dested Escape Pod (V) (Virtual Set 2).
# AUOF inside EFFECTS counts toward 60.
# Sai'torr Kal Fas (V) has no STARTING: in original VS1 game text — omit
# Starting Effect. Frozen Han / Audience Chamber / Jabba's Palace are
# Profit-deployed. Anakin's Podracer / Boonta Eve / Podrace Arena are
# Podrace Prep-deployed — do not guess those as Starting Effect.
# Skip GEMP (original-VS Sai'torr + Escape Pod). Format Premiere - Original
# VS2 (29 Jul 2002 post; event 4–7 July 2002; VS2 legal 1 Jun 2002).
# Do not dest Mike Pistone helper as an extra row. Ken Cross player page
# already exists (pageid 23809) — dump-not-stub.
CROSS_LS = [
    (1, "You Can Either Profit By This...", "OBJECTIVE"),
    (2, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (3, "Ben Kenobi", "CHARACTER"),
    (2, "Chewie, Enraged", "CHARACTER"),
    (2, "Leia, Rebel Princess", "CHARACTER"),
    (2, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "C-3PO (See-Threepio)", "CHARACTER"),
    (1, "Lando Calrissian", "CHARACTER"),
    (1, "Lando With Vibro-Ax", "CHARACTER"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Rendezvous Point", "LOCATION"),
    (1, "Dagobah: Yoda's Hut", "LOCATION"),
    (1, "Dejarik Hologameboard", "LOCATION"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (3, "A Step Backward", "INTERRUPT"),
    (2, "Too Close For Comfort", "INTERRUPT"),
    (2, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (2, "Someone Who Loves You", "INTERRUPT"),
    (2, "Escape Pod (V)", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Grimtaash", "INTERRUPT"),
    (1, "Houjix", "INTERRUPT"),
    (1, "I Know", "INTERRUPT"),
    (1, "Podrace Prep", "INTERRUPT"),
    (1, "Gift Of The Mentor", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "Sorry About The Mess", "INTERRUPT"),
    (1, "Smoke Screen", "INTERRUPT"),
    (2, "It's A Trap!", "INTERRUPT"),
    (1, "I Did It!", "EPIC_EVENT"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Anakin's Podracer", "PODRACER"),
]

# 24516 Warren DS. YAML tagged Light; body Dark Hunt Down. General dest
# (two named events). Dest title Justin Warren Raging Bull (Hoostino's
# Hunt Down Hammer). Author Justin "hoostino" Warren. Handle hoostino
# is not a card. Qty 60. FIMA inside EFFECTS counts toward 60. 10
# Defensive Shields posted outside the 60 (including original-VS
# I Find Your Lack Of Faith Disturbing (V) (VS2)); dest that pile
# separately — do not invent Held 10. Visage Of The Emperor x3 dested
# x3 as published. We Must Accelerate Our Plans dested as printed
# Coruscant Dark (wrap OK). Blockade Flagship Docking Bay dested
# Blockade Flagship: Docking Bay. Death Star Docking Bay 327 dested
# Death Star: Docking Bay 327. Executor Holotheater dested Executor:
# Holotheatre. Resistance dested JP Dark Resistance (as posted).
# Skip GEMP (original-VS IIFYLOFD). Format Premiere - Original VS2
# (20 Jul 2002 post; VS2 legal 1 Jun 2002). Houston Mini-Open 1st and
# Houston DPC 2nd as posted; DPC 14 July 2002 from Jacob Taylor TR.
# Brian Hunter pageid 36782 dump-not-stub (DPC winner; his 60 unpublished).
# Do not dest Hayes Hunter / Jeremy Losee / Paul Myers extra rows.
WARREN_DS = [
    (1, "Hunt Down And Destroy The Jedi", "OBJECTIVE"),
    (1, "Blockade Flagship: Docking Bay", "LOCATION"),
    (1, "Carida", "LOCATION"),
    (1, "Death Star: Docking Bay 327", "LOCATION"),
    (1, "Executor: Holotheatre", "LOCATION"),
    (1, "Executor: Meditation Chamber", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (2, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (3, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Darth Vader", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (2, "Lord Vader", "CHARACTER"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (2, "Chimaera", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (2, "Vader's Lightsaber", "WEAPON"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (3, "Imperial Command", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (2, "Stunning Leader", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "You Are Beaten", "INTERRUPT"),
    (2, "Bad Feeling Have I", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Search And Destroy", "EFFECT"),
    (3, "Visage Of The Emperor", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
]

WARREN_SHIELDS = [
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "A Useless Gesture", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Do They Have A Code Clearance?", "DEFENSIVE_SHIELD"),
    (1, "Fanfare", "DEFENSIVE_SHIELD"),
    (1, "I Find Your Lack Of Faith Disturbing (V)", "DEFENSIVE_SHIELD"),
    (1, "Oppressive Enforcement", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
    (1, "Resistance", "DEFENSIVE_SHIELD"),
]

# 24511 Burnett DS. YAML tagged Light; body Dark Watto. General dest
# (two named events: Dantooine Regionals 3-0 Aaron Pawlik using the
# list; Houston DPC 2-1 Burnett). Dest title David Burnett
# JediGamler's Watto aka The Unstoppable Machine (published
# JediGamler spelling; handle JediGambler). Author David
# "JediGambler" Burnett. Do not dest onto Admiral Piett card
# pageid 137. Qty 60. FIMA inside STARTING-8 counts toward 60;
# unnamed shields dest 60 only. Posted No Money, No Parts, No
# Deal/I Win dested No Money, No Parts, No Deal!. Posted Graga
# dested Gragra. Posted Force Lighting dested Force Lightning.
# Posted Dengar in Punishing 1 dested Dengar In Punishing One.
# Posted Dr.E and Pondo B dested Dr. Evazan & Ponda Baba.
# Posted SpaceportDocking Bay dested Spaceport Docking Bay
# (not Tatooine: Spaceport Docking Bay). Posted ExecutorDocking
# Bay dested Executor: Docking Bay. Posted Blockade FlagshipBridge
# dested Blockade Flagship: Bridge. We Must Accelerate Our Plans
# dested as printed Coruscant Dark. Executor dest Executor (Dark).
# Tatooine dest Tatooine (Dark). Skip GEMP (printed-only POVS2;
# no original-VS2 GEMP code). Format Premiere - Original VS2
# (20 Jul 2002 post; Houston DPC 14 Jul 2002; VS2 legal 1 Jun 2002).
# Dantooine Regionals day unpublished (year-only 2002). Do not
# dest unpublished Burnett QMC. Do not dest extra 60s for Matt
# Lush / Jacob Taylor / Zane Thorp / John Contreras / Chris McClure.
BURNETT_DS = [
    (1, "No Money, No Parts, No Deal!", "OBJECTIVE"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Tatooine: Watto's Junkyard", "LOCATION"),
    (1, "Tatooine: Mos Espa", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (4, "Watto", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (2, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Stormtrooper Garrison", "CHARACTER"),
    (1, "Gragra", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (1, "Executor", "STARSHIP"),
    (2, "Chimaera", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Dengar In Punishing One", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Tatooine Occupation", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (4, "Imperial Command", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Fondor", "LOCATION"),
    (1, "Tatooine", "LOCATION"),
    (1, "Battle Deployment", "ADMIRALS_ORDER"),
]

# Posted Interrupts(26) listed 25; dest listed 60. FIMA inside Starting(4).
# Unnamed 10 D-shields dest 60 only. Posted Drop dested Drop!. Posted Omni Box dested Ommni Box.
# Posted They're Still Coming Through dested They're Still Coming Through!.
# Posted Imperial Reinforcements(v) dested Imperial Reinforcements (V) (VS2).
# Posted Zuckass dested Zuckuss In Mist Hunter. Posted Emperor dested Emperor Palpatine.
# Posted Dr. E combo dested Dr. Evazan & Ponda Baba. Posted Graga not in this 60.
KRUEGER_BEACH_DS = [
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Tatooine: Desert Landing Site", "LOCATION"),
    (1, "Combat Readiness", "INTERRUPT"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Jabba's Palace: Lower Passages", "LOCATION"),
    (1, "Imperial Holotable", "LOCATION"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (1, "Darth Maul, Young Apprentice", "CHARACTER"),
    (1, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (1, "Lord Vader", "CHARACTER"),
    (1, "Darth Vader With Lightsaber", "CHARACTER"),
    (2, "P-59", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "4-LOM", "CHARACTER"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Restraining Bolt", "DEVICE"),
    (1, "Always Thinking With Your Stomach", "INTERRUPT"),
    (2, "Ommni Box & It's Worse", "INTERRUPT"),
    (1, "Wounded Warrior", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (2, "Force Field", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "The Circle Is Now Complete", "INTERRUPT"),
    (2, "Maul Strikes", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (1, "Counter Assault", "INTERRUPT"),
    (1, "Imperial Reinforcements (V)", "INTERRUPT"),
    (1, "Overload", "INTERRUPT"),
    (1, "Shut Him Up Or Shut Him Down", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "You Are Beaten", "INTERRUPT"),
    (1, "Weapon Levitation", "INTERRUPT"),
    (1, "Elis Helrot", "INTERRUPT"),
    (1, "Furry Fury", "INTERRUPT"),
    (1, "They're Still Coming Through!", "INTERRUPT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Search And Destroy", "EFFECT"),
    (1, "Drop!", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (2, "The Phantom Menace", "EFFECT"),
    (1, "Closed Door", "EFFECT"),
    (1, "Security Precautions", "EFFECT"),
]

# 24316 Seth Van Winkle dest notes stay here.
# YAML Dark / body Dark Hunt Down. General dest TITLE {Player} {Published title}.
# No named tournament finish. Do not mint event hubs.
# FIMA inside Start (10) counts; unnamed shields dest 60 only.
# Posted Holotheater dested Executor: Holotheatre.
# Posted Med. Chamber dested Executor: Meditation Chamber.
# Posted DVDLOTS dested Darth Vader, Dark Lord Of The Sith.
# Posted Darth Vader dested Premiere Darth Vader.
# Posted Vader with Saber dested Darth Vader With Lightsaber.
# Posted Darth Maul, YA dested Darth Maul, Young Apprentice.
# Posted Emperor Palpy dested Emperor Palpatine.
# Posted IG88 with Gun dested IG-88 With Riot Gun.
# Posted Dr. E and Ponda B. dested Dr. Evazan & Ponda Baba.
# Posted Mara Jade, TEH dested Mara Jade, The Emperor's Hand.
# Posted ZiMH dested Zuckuss In Mist Hunter.
# Posted BFiS1 dested Boba Fett In Slave I.
# Posted BiHT dested Bossk In Hound's Tooth.
# Posted Maul's Double Bladed Saber dested Maul's Double-Bladed Lightsaber.
# Posted Executor DB dested Executor: Docking Bay.
# Posted D2 DB dested Death Star II: Docking Bay.
# Posted Endor DB dested Endor: Landing Platform (Docking Bay).
# Posted IAO/Plans dested Imperial Arrest Order & Secret Plans.
# Posted YCHF/Mob. Points dested You Cannot Hide Forever & Mobilization Points.
# Posted TCINC dested The Circle Is Now Complete.
# Posted Control/SFS dested Control & Set For Stun.
# Posted M. Move/Endor Occupation dested Masterful Move & Endor Occupation.
# Posted YAB dested You Are Beaten.
# Posted We Must Accelerate Our Plans dested as printed Coruscant Dark.
# Posted Visage start + Visage x2 dested x3 as published.
# Skip GEMP (printed-only POVS2). Handle Ooryl. Do not dest onto Ooryl Qrygg.
VAN_WINKLE_DS = [
    (1, "Hunt Down And Destroy The Jedi", "OBJECTIVE"),
    (1, "Executor: Holotheatre", "LOCATION"),
    (1, "Executor: Meditation Chamber", "LOCATION"),
    (1, "Visage Of The Emperor", "EFFECT"),
    (1, "Epic Duel", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "They Will Be No Match For You", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (1, "Darth Vader", "CHARACTER"),
    (2, "Lord Vader", "CHARACTER"),
    (1, "Darth Vader With Lightsaber", "CHARACTER"),
    (2, "Darth Maul", "CHARACTER"),
    (2, "Darth Maul, Young Apprentice", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (2, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Stinger", "STARSHIP"),
    (2, "Vader's Lightsaber", "WEAPON"),
    (2, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Carida", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "No Escape", "EFFECT"),
    (2, "Visage Of The Emperor", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (2, "Vader's Obsession", "INTERRUPT"),
    (2, "The Circle Is Now Complete", "INTERRUPT"),
    (2, "HoloNet Transmission", "INTERRUPT"),
    (2, "Maul Strikes", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (1, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Control & Set For Stun", "INTERRUPT"),
    (1, "Monnok", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "You Are Beaten", "INTERRUPT"),
]

# 24274 Pyry Nystrom dest notes stay here.
# YAML Dark / body Dark SYCFA racing space. General dest TITLE.
# No named tournament finish. Do not mint event hubs.
# FIMA inside Starting(10) counts. Named 5 Defensive Shields dest outside
# the 60; "+Choose some more..." unnamed rest dest 60 only. Do not invent Held 10.
# Posted Allocations Of Corruption dested Allegations Of Corruption.
# Posted DSDocking Bay dested Death Star: Docking Bay 327.
# Posted Start Your Engines dested Start Your Engines!.
# Posted TatooinePodrace Arena dested Tatooine: Podrace Arena.
# Posted Sebulbas Racer dested Sebulba's Podracer.
# Posted Wakelmuii dested Wakeelmui.
# Posted DSWar Room dested Death Star: War Room.
# Posted Darth Vader(V) dested Darth Vader (V) (VS1).
# Posted Commander Praji(V) dested Commander Praji (V) (VS2).
# Posted The Empires Back(V) dested The Empire's Back (V) (VS2).
# Posted Imperial Class Star Destroyer(V) dested Imperial-Class Star Destroyer (V) (VS2).
# Posted Fear Will Keep Them In Line(V) dested Fear Will Keep Them In Line (V) (VS2).
# Posted I Find Your Lack Of Fate Disturbing(V) dested IIFYLOFD (V) (VS2).
# Posted Executor dested Executor (Dark). Posted Death Star dested Death Star (Dark).
# Posted U-3PO dested U-3PO (Yoo-Threepio). Posted Zuckuss in MH dested Zuckuss In Mist Hunter.
# Posted Podrace Collision dested Podracer Collision.
# Posted I'd As Soon Kiss a Wookie dested I'd Just As Soon Kiss A Wookiee.
# Posted SFS 9.3 Cannons dested SFS L-s9.3 Laser Cannons.
# Posted Were In Attack Position Now dested We're In Attack Position Now.
# Posted Come here You Big Covard dested Come Here You Big Coward.
# Posted We Must Accelerate Our Plans dested as printed Coruscant Dark.
# Posted Fighters Straight Ahead dested as printed. Skip GEMP.
# Handle Blizzard. Do not dest onto Blizzard 4. Do not dest onto Admiral Piett card pageid 137.
NYSTROM_DS = [
    (1, "Set Your Course For Alderaan", "OBJECTIVE"),
    (1, "Death Star", "LOCATION"),
    (1, "Alderaan", "LOCATION"),
    (1, "Death Star: Docking Bay 327", "LOCATION"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Start Your Engines!", "INTERRUPT"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Sebulba's Podracer", "PODRACER"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Wakeelmui", "LOCATION"),
    (1, "Malastare", "LOCATION"),
    (1, "Kashyyyk", "LOCATION"),
    (1, "Fondor", "LOCATION"),
    (1, "Death Star: War Room", "LOCATION"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "Darth Vader (V)", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (1, "Commander Praji (V)", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Captain Godherdt", "CHARACTER"),
    (1, "U-3PO", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Executor", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Devastator", "STARSHIP"),
    (1, "Thunderflare", "STARSHIP"),
    (1, "Imperial-Class Star Destroyer (V)", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "The Emperor's Shield", "STARSHIP"),
    (1, "The Emperor's Sword", "STARSHIP"),
    (2, "TIE Interceptor", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Fear Will Keep Them In Line (V)", "EFFECT"),
    (1, "Sienar Fleet Systems", "EFFECT"),
    (1, "Watto's Box", "EFFECT"),
    (1, "Fighters Straight Ahead", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Twi'lek Advisor", "INTERRUPT"),
    (2, "Podracer Collision", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "Imperial Barrier", "INTERRUPT"),
    (1, "I'd Just As Soon Kiss A Wookiee", "INTERRUPT"),
    (1, "The Empire's Back (V)", "INTERRUPT"),
    (1, "Unsalvageable", "INTERRUPT"),
    (1, "Control & Set For Stun", "INTERRUPT"),
    (1, "Overload", "INTERRUPT"),
    (1, "Imperial Command", "INTERRUPT"),
    (2, "SFS L-s9.3 Laser Cannons", "WEAPON"),
    (1, "We're In Attack Position Now", "ADMIRALS_ORDER"),
]
NYSTROM_SHIELDS = [
    (1, "Battle Order", "EFFECT"),
    (1, "You've Never Won A Race?", "EFFECT"),
    (1, "Come Here You Big Coward", "EFFECT"),
    (1, "Allegations Of Corruption", "EFFECT"),
    (1, "I Find Your Lack Of Faith Disturbing (V)", "EFFECT"),
]

# 24142 Bill Kafer LSC TacoBill style. YAML Dark / body Dark LSC. Qty 60.
# FIMA INSIDE Starting (9) counts. Unnamed 10 shields dest 60 only
# (Shields are your prefrence). Skip GEMP (original-VS Blaster Rack (V) VS1).
# Posted LTMTFM/ALWWHR dested Let Them Make The First Move.
# Posted Commander Merrejek dested Commander Merrejk.
# Posted Boba Fett In Slave One dested Boba Fett In Slave I.
# Posted Naboo Theed Palace Generator dested Naboo: Theed Palace Generator.
# Posted Naboo Theed Palace Generator Core dested Naboo: Theed Palace Generator Core.
# Posted Blockade Flagship Bridge dested Blockade Flagship: Bridge.
# Posted Executor Docking Bay dested Executor: Docking Bay.
# Posted YCHF & Mobilization Points dested You Cannot Hide Forever & Mobilization Points.
# Posted Mara Jades Lightsaber dested Mara Jade's Lightsaber.
# Posted Mauls Double-Bladed Lightsaber dested Maul's Double-Bladed Lightsaber.
# Posted Vaders Lightsaber dested Vader's Lightsaber.
# Posted Qui-Gons End dested Qui-Gon's End.
# Posted Ommni Box & Its Worse dested Ommni Box & It's Worse.
# Posted Theyre Still Coming Through dested They're Still Coming Through!.
# Posted Ghhhk & Those Rebels Wont Escape Us dested Ghhhk & Those Rebels Won't Escape Us.
# Posted Executor dested Executor (Dark). Posted Endor dested Endor (Dark).
# Posted Bespin dested Bespin (Dark).
# Posted Blaster Rack (V) dested Blaster Rack (V) (Virtual Set 1).
# Posted We Must Accelerate Our Plans dested as printed Coruscant Dark.
# Posted Bad Feeling Have I under Effects dested Interrupt.
# Lord Maul dested Lord Maul. Lord Vader dested Lord Vader (not DLOTS).
# Handle TacoBill. Do not dest onto a card. Bill Kafer pageid 21342 dump-not-stub.
# YAML extra space "LSC  TacoBill style" collapsed on dest TITLE.
KAFER_DS = [
    (1, "Let Them Make The First Move", "OBJECTIVE"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Blaster Rack (V)", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Deep Hatred", "EFFECT"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (3, "Lord Maul", "CHARACTER"),
    (2, "Lord Vader", "CHARACTER"),
    (1, "Nute Gunray", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Rune Haako", "CHARACTER"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Executor", "STARSHIP"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (2, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Bad Feeling Have I", "INTERRUPT"),
    (1, "Qui-Gon's End", "EFFECT"),
    (3, "The Phantom Menace", "EFFECT"),
    (1, "They Must Never Again Leave This City", "EFFECT"),
    (2, "Blow Parried", "INTERRUPT"),
    (1, "Force Field", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "Imperial Barrier", "INTERRUPT"),
    (2, "Imperial Command", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "Ommni Box & It's Worse", "INTERRUPT"),
    (1, "Shut Him Up Or Shut Him Down", "INTERRUPT"),
    (2, "Stunning Leader", "INTERRUPT"),
    (1, "They're Still Coming Through!", "INTERRUPT"),
    (1, "Unsalvageable", "INTERRUPT"),
    (1, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Bespin", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Endor", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
]

# 24104 Kyle Krueger The Beast on the Beach. YAML Dark / body Dark mains.
# Qty 60. FIMA INSIDE Starting(4) counts. Unnamed 10 D-shields dest 60 only
# (Ten d-shields to best fit your meta). Skip GEMP (original-VS Imperial
# Reinforcements (V) VS2). General dest TITLE (3 tournaments undefeated posted
# without a finish; do not mint Endor Regionals hub).
# Posted Tatooine  Desert Landing Site dested Tatooine: Desert Landing Site.
# Posted Tatooine  Jabba's Palace dested Tatooine: Jabba's Palace.
# Posted Jabba's Palace  Audience Chamber dested Jabba's Palace: Audience Chamber.
# Posted Jabba's Palace  Lower Passages dested Jabba's Palace: Lower Passages.
# Posted Imperial Holotable dested Imperial Holotable.
# Posted Zuckass dested Zuckuss In Mist Hunter.
# Posted Maul's Sith Infiltrator dested Maul's Sith Infiltrator.
# Posted Omni Box dested Ommni Box & It's Worse.
# Posted Alter(Coruscant) dested Alter (Dark) (Coruscant).
# Posted The Circle is now Complete dested The Circle Is Now Complete.
# Posted Imperial Reinforcements(v) dested Imperial Reinforcements (V) (VS2).
# Posted Ghhk combo dested Ghhhk & Those Rebels Won't Escape Us.
# Posted They're Still Coming Through dested They're Still Coming Through!.
# Posted Drop dested Drop!.
# Posted Search and Destroy dested Search And Destroy.
# Posted Visage of the Emperor dested Visage Of The Emperor.
# Handle Meto already cited from 26173. Do not dest onto a card.
# Kyle Krueger pageid 21369 dump-not-stub.
BEACH_V1_DS = [
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Tatooine: Desert Landing Site", "LOCATION"),
    (1, "Combat Readiness", "INTERRUPT"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Jabba's Palace: Lower Passages", "LOCATION"),
    (1, "Imperial Holotable", "LOCATION"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (1, "Darth Maul, Young Apprentice", "CHARACTER"),
    (1, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (1, "Lord Vader", "CHARACTER"),
    (1, "Darth Vader With Lightsaber", "CHARACTER"),
    (3, "P-59", "CHARACTER"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Maul's Sith Infiltrator", "STARSHIP"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Restraining Bolt", "DEVICE"),
    (2, "Ommni Box & It's Worse", "INTERRUPT"),
    (2, "Wounded Warrior", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (2, "Force Field", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Alter (Dark) (Coruscant)", "INTERRUPT"),
    (1, "The Circle Is Now Complete", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (1, "Counter Assault", "INTERRUPT"),
    (1, "Imperial Reinforcements (V)", "INTERRUPT"),
    (1, "Overload", "INTERRUPT"),
    (1, "Shut Him Up Or Shut Him Down", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "They're Still Coming Through!", "INTERRUPT"),
    (1, "You Are Beaten", "INTERRUPT"),
    (1, "Weapon Levitation", "INTERRUPT"),
    (3, "Imperial Artillery", "INTERRUPT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Search And Destroy", "EFFECT"),
    (2, "Drop!", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "The Phantom Menace", "EFFECT"),
    (1, "Closed Door", "EFFECT"),
    (1, "Security Precautions", "EFFECT"),
    (1, "Visage Of The Emperor", "EFFECT"),
    (1, "Battle Deployment", "ADMIRALS_ORDER"),
]

# 24089 Mike "Quione" Noneofyourbusiness Saber combat my way.
# YAML Light / body Light We'll Handle This. Qty 60.
# Last name is a joke; [[Mike]] redirects to [[Mike Thomas]] — stub
# [[Mike (Quione)]]. Do not dest onto Mike Thomas. Handle Quione.
# General dest TITLE (no published finish).
# AUOF INSIDE Starting counts. Unnamed extra dest 60 only. Skip GEMP
# (printed-only POVS2). Inner Strength is Reflections III Epic Event.
# Squadron Assignments is Death Star II Effect (not STARTING).
# Posted Palace Generator Core dested Naboo: Theed Palace Generator Core.
# Posted Theed Palace Generator dested Naboo: Theed Palace Generator.
# Posted Podrace Arena dested Tatooine: Podrace Arena.
# Posted Anakins Podracer dested Anakin's Podracer.
# Posted Squadren Assignments dested Squadron Assignments.
# Posted Captain Han dested Captain Han Solo.
# Posted Tat Obi dested Obi-Wan Kenobi, Padawan Learner.
# Posted Ref 3 Qui gon dested Qui-Gon Jinn, Jedi Master (x2 as published).
# Posted Tat Padme dested Padme Naberrie.
# Posted Luke Skywalker, JK dested Luke Skywalker, Jedi Knight.
# Posted Ref 3 Lando dested Lando Calrissian, Scoundrel.
# Posted Chewie w/ Blaster dested Chewie With Blaster Rifle.
# Posted Firgin D'an dested Figrin D'an.
# Posted Eject Eject dested Eject! Eject!.
# Posted Artoo I have a bad feeling about this dested Artoo, I Have A Bad Feeling About This.
# Posted Run Luke Run dested Run Luke, Run!.
# Posted Thank the Maker dested Thank The Maker.
# Posted Ref 3 Obi lightsaber dested Obi-Wan's Lightsaber.
# Posted Ref 3 Qui-gon lightsaber dested Qui-Gon's Lightsaber.
# Posted Lukes Lightsaber dested Luke's Lightsaber.
# Posted Intruder Missle dested Intruder Missile.
# Posted I did it dested I Did It!.
SABER_LS = [
    (1, "We'll Handle This / Duel Of The Fates", "OBJECTIVE"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Inner Strength", "EPIC_EVENT"),
    (1, "Podrace Prep", "INTERRUPT"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Anakin's Podracer", "PODRACER"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Captain Han Solo", "CHARACTER"),
    (1, "Mirax Terrik", "CHARACTER"),
    (2, "Obi-Wan Kenobi, Padawan Learner", "CHARACTER"),
    (2, "Qui-Gon Jinn, Jedi Master", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (2, "Padme Naberrie", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Chewie With Blaster Rifle", "CHARACTER"),
    (1, "Figrin D'an", "CHARACTER"),
    (2, "Artoo & Threepio", "CHARACTER"),
    (1, "Joh Yowza", "CHARACTER"),
    (1, "Beggar", "EFFECT"),
    (2, "Eject! Eject!", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Lightsaber Proficiency", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (2, "We're Doomed", "INTERRUPT"),
    (1, "Endor Celebration", "INTERRUPT"),
    (2, "Life Debt", "INTERRUPT"),
    (1, "Jedi Presence", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
    (1, "Blaster Deflection", "INTERRUPT"),
    (2, "Weapon Levitation", "INTERRUPT"),
    (2, "Artoo, I Have A Bad Feeling About This", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (2, "Run Luke, Run!", "INTERRUPT"),
    (3, "Thank The Maker", "INTERRUPT"),
    (2, "Strike Blocked", "INTERRUPT"),
    (1, "Outrider", "STARSHIP"),
    (1, "Millennium Falcon", "STARSHIP"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Qui-Gon's Lightsaber", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (2, "Intruder Missile", "WEAPON"),
    (1, "I Did It!", "EPIC_EVENT"),
]

# 24026 Matt "QuiGon57" Carulli Hunt Down and Revive the SCUM.
# YAML Dark / body Dark Court. Qty 60. Author Matt "QuiGon57" Carulli.
# Handle QuiGon57 is not a card. Do not dest onto Qui-Gon Jinn.
# Matt Carulli pageid 17151 dump-not-stub. General dest TITLE (no
# published finish). FIMA INSIDE Starting (9) counts toward 60.
# Named 10 Defensive Shields dest outside 60 (including original-VS
# IIFYLOFD (V) VS2). Posted Blaster Rack (V) dested Blaster Rack (V)
# (VS1). Posted Bib Fortuna (Reflections III) dested Bib Fortuna
# (Dark) File Ref3-D-bibfortuna.gif. Posted Boba Fett (CC) dested
# Cloud City Boba Fett. Posted Iggy w/ Gun dested IG-88 With Riot
# Gun. Posted Dr. Evazans Blaster dested Dr. Evazan's Sawed-off
# Blaster. Posted Naboo DB dested Naboo: Theed Palace Docking Bay.
# Posted Spaceport DB dested Spaceport Docking Bay. Posted Tatooine
# DB 94 dested Tatooine: Docking Bay 94. Posted Cantina dested
# Tatooine: Cantina. Posted Mos Eisley dested Tatooine: Mos Eisley.
# Posted Sniper/ Dark Strike dested Sniper & Dark Strike. Posted
# Jabbas Palace sites dested colon titles. Posted Court of the Vile
# Gangster dested Court Of The Vile Gangster / I Shall Enjoy
# Watching You Die. Skip GEMP (original-VS dests). Format Premiere
# - Original VS2 (19 Jun 2002; VS2 legal 1 Jun 2002).
CARULLI_DS = [
    (1, "Court Of The Vile Gangster / I Shall Enjoy Watching You Die", "OBJECTIVE"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Tatooine: Great Pit Of Carkoon", "LOCATION"),
    (1, "Jabba's Palace: Dungeon", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Blaster Rack (V)", "EFFECT"),
    (1, "All Wrapped Up", "EFFECT"),
    (1, "Power Of The Hutt", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Ephant Mon", "CHARACTER"),
    (1, "Boelo", "CHARACTER"),
    (1, "Mighty Jabba", "CHARACTER"),
    (1, "Bib Fortuna (Dark)", "CHARACTER"),
    (1, "Thok & Thug", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Boba Fett", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Snoova", "CHARACTER"),
    (1, "Dengar With Blaster Carbine", "CHARACTER"),
    (1, "Bossk With Mortar Gun", "CHARACTER"),
    (1, "Jodo Kast", "CHARACTER"),
    (1, "Aurra Sing", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Rancor", "CREATURE"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Aurra Sing's Blaster Rifle", "WEAPON"),
    (1, "Vibro-Ax", "WEAPON"),
    (1, "Dr. Evazan's Sawed-off Blaster", "WEAPON"),
    (1, "Jabba's Palace: Rancor Pit", "LOCATION"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Tatooine: Docking Bay 94", "LOCATION"),
    (1, "Tatooine: Cantina", "LOCATION"),
    (1, "Tatooine: Mos Eisley", "LOCATION"),
    (1, "Bad Feeling Have I", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Disarmed", "EFFECT"),
    (1, "We're The Bait", "EFFECT"),
    (1, "Broken Concentration", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "Hutt Bounty", "EFFECT"),
    (2, "Bounty", "EFFECT"),
    (2, "Scum And Villainy", "EFFECT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Imperial Artillery", "INTERRUPT"),
    (1, "Furry Fury", "INTERRUPT"),
    (1, "Neimoidian Advisor", "INTERRUPT"),
    (1, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Hidden Weapons", "INTERRUPT"),
    (3, "Trap Door", "INTERRUPT"),
]

CARULLI_SHIELDS = [
    (1, "Resistance", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "A Useless Gesture", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
    (1, "Secret Plans", "DEFENSIVE_SHIELD"),
    (1, "Fanfare", "DEFENSIVE_SHIELD"),
    (1, "Weapon Of A Sith", "DEFENSIVE_SHIELD"),
    (1, "There Is No Try", "DEFENSIVE_SHIELD"),
    (1, "Oppressive Enforcement", "DEFENSIVE_SHIELD"),
    (1, "I Find Your Lack Of Faith Disturbing (V)", "DEFENSIVE_SHIELD"),
]

# 24025 Chris "Fred" Davis TDIGWATT/PIDAIAF CC Dark Deal Deck.
# YAML Dark / body Dark Deal. Qty 60. Author Chris "Fred" Davis.
# Handle Fred is not a card. Do not dest onto Admiral Piett pageid 137
# (Piett is a card in the 60). Chris Davis missing — stub.
# General dest TITLE (no published finish). No FIMA. Unnamed D-shields
# dest 60 only. Posted Black 2 (V) dested Black 2 (V) (VS1)
# File VS1O-08-Black_2.png. Posted Imperial-Class Star Destroyer
# (V is possible) dested printed x2. Posted The Empire's Back without
# (V) dested printed. Posted CC slang dested colon Cloud City: titles.
# Posted This Deal.../ Pary I Don't Alter It Further dested
# This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any
# Further. Posted Lando Calrissian dested Lando Calrissian (Dark).
# Posted IG-88 dested printed Dagobah IG-88. Posted Dark Maneuvers &
# Tallon Roll dested combo. Skip GEMP (original-VS Black 2 (V) VS1).
# Format Premiere - Original VS2 (19 Jun 2002; VS2 legal 1 Jun 2002).
DAVIS_DS = [
    (1, "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further", "OBJECTIVE"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Combat Response", "EFFECT"),
    (1, "Imperial Arrest Order", "EFFECT"),
    (1, "I'm Sorry", "EFFECT"),
    (1, "All Wrapped Up", "EFFECT"),
    (1, "Cloud City: Port Town District", "LOCATION"),
    (1, "Bespin", "LOCATION"),
    (1, "Bespin: Cloud City", "LOCATION"),
    (1, "Cloud City: East Platform (Docking Bay)", "LOCATION"),
    (1, "Cloud City: Carbonite Chamber", "LOCATION"),
    (1, "Cloud City: Chasm Walkway", "LOCATION"),
    (1, "Cloud City: Casino", "LOCATION"),
    (1, "Lord Vader", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Trooper Davin Felth", "CHARACTER"),
    (1, "Sergeant Tarl", "CHARACTER"),
    (1, "Corporal Drazin", "CHARACTER"),
    (1, "DS-61-2", "CHARACTER"),
    (1, "DS-61-3", "CHARACTER"),
    (1, "DS-181-3", "CHARACTER"),
    (1, "DS-181-4", "CHARACTER"),
    (1, "Lando Calrissian", "CHARACTER"),
    (1, "Lobot", "CHARACTER"),
    (6, "Cloud City Trooper", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "IG-88", "CHARACTER"),
    (1, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Avenger", "STARSHIP"),
    (2, "Imperial-Class Star Destroyer", "STARSHIP"),
    (1, "Black 2 (V)", "STARSHIP"),
    (1, "Black 3", "STARSHIP"),
    (1, "Saber 3", "STARSHIP"),
    (1, "Saber 4", "STARSHIP"),
    (1, "OS-72-1 In Obsidian 1", "STARSHIP"),
    (1, "OS-72-2 In Obsidian 2", "STARSHIP"),
    (1, "Blizzard 2", "VEHICLE"),
    (1, "Tempest 1", "VEHICLE"),
    (1, "Blizzard Walker", "VEHICLE"),
    (1, "Combat Cloud Car", "VEHICLE"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Dark Deal", "EFFECT"),
    (1, "Cloud City Occupation", "EFFECT"),
    (1, "Expand The Empire", "EFFECT"),
    (5, "Dark Maneuvers & Tallon Roll", "INTERRUPT"),
    (2, "The Empire's Back", "INTERRUPT"),
]

# 24022 Quiet Macking of Cloud city. Author Chris "Golfercwm" McCoy.
# YAML tagged Light / body Light QMC (match). Qty 60: Starting 8 + Characters 17
# + Effects 8 + Interrupts 14 + Starships 6 + Locations 3 + Weapons 3 + AO 1.
# AUOF INSIDE Starting(8) counts. Unnamed Ten D shields dest 60 only.
# Posted Quiet Mining Colony/Independent Operation dested dual.
# Posted Cloud City Guest Quarters dested Cloud City: Guest Quarters.
# Posted Cloud City Docking Bay dested Cloud City: Platform 327 (Docking Bay).
# Posted Cloud City West Gallery / North Corridor dested colon titles.
# Posted Squadren Assignments dested Squadron Assignments.
# Posted HFTMF dested Heading For The Medical Frigate.
# Posted AUAOF dested An Unusual Amount Of Fear.
# Posted Qui Gon w/ Stick dested Qui-Gon Jinn With Lightsaber.
# Posted Qui Gon Jedi Master dested Qui-Gon Jinn, Jedi Master.
# Posted Luke w/ Stick dested Luke With Lightsaber File EP-L-lukewithlightsaber.gif
# (NOT missing Luke Skywalker With Lightsaber).
# Posted Liea Rebal Princess dested Leia, Rebel Princess.
# Posted Lando w/ Blaster pistol dested Lando With Blaster Pistol.
# Posted Lando Cal. Scoundrel dested Lando Calrissian, Scoundrel.
# Posted Chewbacca Protector dested Chewbacca, Protector.
# Posted Padme dested Padme Naberrie.
# Posted Han w/ Blaster dested Han With Heavy Blaster Pistol.
# Posted Wedge Antilies RSL dested Wedge Antilles, Red Squadron Leader.
# Posted Path of Least Resistance x2 dested printed; Path or Least
# Resistance/Reveled dested combo Path Of Least Resistance & Revealed.
# Posted Out of Commission dested printed; Out of Commission/Transmission
# Terminated dested combo.
# Posted Out of Noware dested Out Of Nowhere.
# Posted Run Luke Run dested Run Luke, Run!.
# Posted Off the Edge dested On The Edge.
# Posted Escape Pod V dested original-VS Escape Pod (V) (VS2)
# File VS2O-06-Escape_Pod.png.
# Posted Alter/Friendly Fire dested combo Alter & Friendly Fire.
# Posted Red Squad 1 dested Red Squadron 1.
# Posted Anakins Lightsaber dested Anakin's Lightsaber.
# Posted Qui Gons Lightsaber R3 dested Qui-Gon's Lightsaber.
# Posted X-Wing Laser Cannons dested X-wing Laser Cannon.
# Posted Concentrate All Fire dested Admiral's Order.
# Menace Fades / Keeping The Empire Out Forever / Squadron Assignments are
# HFTMF-deployed or extra — do not guess them as Starting Effect.
# Skip GEMP (original-VS Escape Pod (V) VS2). Format Premiere - Original VS2
# (19 Jun 2002; VS2 legal 1 Jun 2002). Do not dest onto Qui-Gon Jinn card
# pageid 6703. Distinct from Chris Davis stub 42254.
MCCOY_LS = [
    (1, "Quiet Mining Colony / Independent Operation", "OBJECTIVE"),
    (1, "Bespin", "LOCATION"),
    (1, "Cloud City: Guest Quarters", "LOCATION"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Keeping The Empire Out Forever", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (2, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Captain Panaka", "CHARACTER"),
    (1, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Qui-Gon Jinn, Jedi Master", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (1, "General Jar Jar", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Lando With Blaster Pistol", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Chewbacca, Protector", "CHARACTER"),
    (1, "Padme Naberrie", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Cloud City Celebration", "EFFECT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "Obi-Wan's Apparition", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "They Win This Round", "EFFECT"),
    (2, "Path Of Least Resistance", "INTERRUPT"),
    (1, "Path Of Least Resistance & Revealed", "INTERRUPT"),
    (1, "Out Of Commission", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Out Of Nowhere", "INTERRUPT"),
    (2, "The Signal", "INTERRUPT"),
    (1, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Run Luke, Run!", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Escape Pod (V)", "INTERRUPT"),
    (1, "Alter & Friendly Fire", "INTERRUPT"),
    (1, "Home One", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Red Leader In Red 1", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Gold Leader In Gold 1", "STARSHIP"),
    (1, "Liberty", "STARSHIP"),
    (1, "Cloud City: Platform 327 (Docking Bay)", "LOCATION"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (1, "Cloud City: North Corridor", "LOCATION"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (1, "Qui-Gon's Lightsaber", "WEAPON"),
    (1, "X-wing Laser Cannon", "WEAPON"),
    (1, "Concentrate All Fire", "ADMIRALS_ORDER"),
]

# 24020 I’m Getting Too Old For This. Author Mike "Darth Dago" Guarino.
# YAML tagged Light / body Light MBO (match). Qty 60: Starting 7 + Locations 10
# + Characters 18 + Starships 11 + Interrupts 7 + Effects 2 + Weapons 3
# + Epic 1 + AO 1. Starting Effect omitted (Get To Your Ships!, Great Shot,
# Kid!, Battle Plan & Draw Their Fire are HFTMF-deployed — do not invent
# Starting Effect). Unnamed extra dest 60 only. Do not invent Held 10.
# Posted Massassi Base Operations/OIAM dested dual.
# Posted Yavin 4 Docking Bay dested Yavin 4: Docking Bay.
# Posted Death Star Trench dested Death Star: Trench.
# Posted Yavin 4 Briefing Room / Jungle / Massassi Headquarters / Massassi
# War Room dested colon titles.
# Posted Get To Your Ships dested Get To Your Ships!.
# Posted Great Shot,Kid dested Great Shot, Kid!.
# Posted Luke w/Lightsaber dested Luke With Lightsaber.
# Posted Master Qui-Gon dested Master Qui-Gon (NOT Qui-Gon Jinn, Jedi Master).
# Posted Princess Organa dested Princess Organa (NOT Princess Leia Organa).
# Posted Whoooo dested Whoooo!.
# Posted You’re All Clear Kid dested You're All Clear Kid!.
# Posted Down With The Emperor dested Down With The Emperor!.
# Posted Traffic Control dested printed Premiere (NOT Traffic Control (V) VS3).
# Posted Qui-Gon Jinn’s Lightsaber dested Tatooine Qui-Gon Jinn's Lightsaber.
# Posted Proton Torpedoes(Ep.1) dested Proton Torpedoes (Theed Palace)
# File Theed-L-protontorpedoes.gif (NOT Premiere Proton Torpedoes).
# Posted I’ll Try Spinning dested I'll Try Spinning.
# Posted Battle Plan & Draw Their Fire dested combo without minting.
# Skip GEMP (printed-only POVS2; no original (V) cards). Format Premiere -
# Original VS2 (19 Jun 2002; VS2 legal 1 Jun 2002). Handle Darth Dago.
# Do not dest onto [[Mike]] (redirects to Mike Thomas). Do not dest onto
# Qui-Gon Jinn card pageid 6703. Do not dest onto Bravo 3 card as player.
GUARINO_LS = [
    (1, "Massassi Base Operations / One In A Million", "OBJECTIVE"),
    (1, "Yavin 4", "LOCATION"),
    (1, "Yavin 4: Docking Bay", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Get To Your Ships!", "EFFECT"),
    (1, "Great Shot, Kid!", "EFFECT"),
    (1, "Battle Plan & Draw Their Fire", "EFFECT"),
    (1, "Bothawui", "LOCATION"),
    (1, "Death Star", "LOCATION"),
    (1, "Death Star: Trench", "LOCATION"),
    (1, "Malastare", "LOCATION"),
    (1, "Naboo", "LOCATION"),
    (1, "Raithal", "LOCATION"),
    (1, "Yavin 4: Briefing Room", "LOCATION"),
    (1, "Yavin 4: Jungle", "LOCATION"),
    (1, "Yavin 4: Massassi Headquarters", "LOCATION"),
    (1, "Yavin 4: Massassi War Room", "LOCATION"),
    (1, "Captain Panaka", "CHARACTER"),
    (1, "Commander Vanden Willard", "CHARACTER"),
    (1, "Lieutenant Arven Wendik", "CHARACTER"),
    (1, "Lieutenant Chamberlyn", "CHARACTER"),
    (1, "Lieutenant Rya Kirsch", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (1, "Master Qui-Gon", "CHARACTER"),
    (5, "Naboo Fighter Pilot", "CHARACTER"),
    (1, "Officer Dolphe", "CHARACTER"),
    (1, "Officer Ellberger", "CHARACTER"),
    (1, "Princess Organa", "CHARACTER"),
    (1, "Queen Amidala", "CHARACTER"),
    (1, "Rebel Tech", "CHARACTER"),
    (1, "Ric Olie, Bravo Leader", "CHARACTER"),
    (1, "Bravo 1", "STARSHIP"),
    (1, "Bravo 2", "STARSHIP"),
    (1, "Bravo 3", "STARSHIP"),
    (1, "Bravo 4", "STARSHIP"),
    (1, "Bravo 5", "STARSHIP"),
    (1, "Bravo Fighter", "STARSHIP"),
    (5, "Naboo Defense Fighter", "STARSHIP"),
    (4, "A Few Maneuvers", "INTERRUPT"),
    (2, "Whoooo!", "INTERRUPT"),
    (1, "You're All Clear Kid!", "INTERRUPT"),
    (1, "Down With The Emperor!", "EFFECT"),
    (1, "Traffic Control", "EFFECT"),
    (1, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (2, "Proton Torpedoes (Theed Palace)", "WEAPON"),
    (1, "Attack Run", "EPIC_EVENT"),
    (1, "I'll Try Spinning", "ADMIRALS_ORDER"),
]

# 24003 What my step It’s yours I should be watching.
# Author Zach "Greedosalive" Mann. YAML tagged Light / body Light WYS (match).
# Qty 60: Starting 8 + Locations 3 + Characters 17 + Starships 3 + AO 1
# + Effects 5 + Interrupts 23. Starting Effect omitted (Menace Fades,
# Ultimatum, Squadron Assignments are HFTMF-deployed — do not invent
# Starting Effect). Unnamed extra dest 60 only. Do not invent Held 10.
# Posted WYSTPCGALR dested Watch Your Step / This Place Can Be A Little Rough.
# Posted Squadran assignments dested Squadron Assignments.
# Posted Tatooine docking bay 94 dested Tatooine: Docking Bay 94.
# Posted Tatooine cantina dested Tatooine: Cantina.
# Posted Rendezvous point dested Rendezvous Point.
# Posted Spaceport docking bay dested Spaceport Docking Bay.
# Posted Captain Han solo dested Captain Han Solo.
# Posted Chewbacca, protector dested Chewbacca, Protector.
# Posted Rattlir freighter captain dested Ralltiir Freighter Captain.
# Posted Leia, rebel princess dested Leia, Rebel Princess.
# Posted Millenium falcon dested Millennium Falcon.
# Posted Artoo in red 5 dested Artoo-Detoo In Red 5 File TA-L-artoodetooinred5.gif
# (NOT missing Artoo In Red 5).
# Posted I’ll take the leader dested I'll Take The Leader.
# Posted Projection of skywalker dested Projection Of A Skywalker.
# Posted Docking and repair facilities dested Docking And Repair Facilities.
# Posted Blast the door, kid dested Blast The Door, Kid!.
# Posted Punch it dested Punch It!.
# Posted Star destroyer dested Star Destroyer!.
# Posted It’s a trap dested It's A Trap!.
# Posted Houjix and out of nowhere combo dested Houjix & Out Of Nowhere.
# Skip GEMP (printed-only POVS2; no original (V) cards). Format Premiere -
# Original VS2 (17 Jun 2002; VS2 legal 1 Jun 2002). Handle Greedosalive.
# Do not dest onto Greedo card pageid 3689.
MANN_LS = [
    (1, "Watch Your Step / This Place Can Be A Little Rough", "OBJECTIVE"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Ultimatum", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Tatooine", "LOCATION"),
    (1, "Tatooine: Docking Bay 94", "LOCATION"),
    (1, "Tatooine: Cantina", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (1, "Rendezvous Point", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (2, "Captain Han Solo", "CHARACTER"),
    (1, "Chewbacca", "CHARACTER"),
    (1, "Chewbacca, Protector", "CHARACTER"),
    (2, "Wedge Antilles", "CHARACTER"),
    (1, "Rayc Ryjerd", "CHARACTER"),
    (1, "Mirax Terrik", "CHARACTER"),
    (1, "Talon Karrde", "CHARACTER"),
    (1, "Theron Nett", "CHARACTER"),
    (4, "Ralltiir Freighter Captain", "CHARACTER"),
    (1, "Luke Skywalker", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Ben Kenobi", "CHARACTER"),
    (1, "Millennium Falcon", "STARSHIP"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Red 2", "STARSHIP"),
    (1, "I'll Take The Leader", "ADMIRALS_ORDER"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "Beggar", "EFFECT"),
    (1, "Docking And Repair Facilities", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (4, "A Few Maneuvers", "INTERRUPT"),
    (4, "Control", "INTERRUPT"),
    (1, "Blast The Door, Kid!", "INTERRUPT"),
    (1, "Punch It!", "INTERRUPT"),
    (2, "Rebel Barrier", "INTERRUPT"),
    (1, "Star Destroyer!", "INTERRUPT"),
    (1, "Moving To Attack Position", "INTERRUPT"),
    (1, "Alternatives To Fighting", "INTERRUPT"),
    (1, "It's A Trap!", "INTERRUPT"),
    (1, "Effective Repairs", "INTERRUPT"),
    (1, "Weapon Levitation", "INTERRUPT"),
    (2, "Tunnel Vision", "INTERRUPT"),
    (1, "Dodge", "INTERRUPT"),
    (2, "Houjix & Out Of Nowhere", "INTERRUPT"),
]

# 23994 Adam "Skipray" Nelson Droid Deal v 1 0.
# YAML Dark / body Dark TDIGWATT Dark Deal (match). Qty 60: Starting 7
# + Characters 25 + Effects 5 + Interrupts 6 + Locations 5 + Starships 7
# + Weapons 5. FIMA INSIDE Starting (7) counts toward 60. Named 10
# Defensive Shields dest OUTSIDE 60. Do not invent Held 10.
# Author Adam "Skipray" Nelson. Handle Skipray. Dump-not-stub
# [[Adam Nelson]] pageid 37460. Do not dest player onto Skipray Blastboat
# (Premiere vehicle; dump API missing). [[Skipray]] MISSING.
# Posted TDIGWATT dested This Deal Is Getting Worse All The Time /
# Pray I Don't Alter It Any Further. Posted Cloud City West Gallery
# dested Cloud City: West Gallery. Posted I’m Sorry dested I'm Sorry.
# Posted 4-LOM with Concussion Rifle dested 4-LOM With Concussion Rifle.
# Posted U-3PO dested U-3PO (Yoo-Threepio) File ANH-D-u3po.gif.
# Posted IG-88 with Riot Gun dested IG-88 With Riot Gun.
# Posted There They Are dested There They Are! File Theed-D-theretheyare.gif
# pageid 7410. Posted Do They Have Code Clearance? dested Do They Have A
# Code Clearance?. Posted Bespin Cloud City dested Bespin: Cloud City.
# Posted Cloud City East Platform dested Cloud City: East Platform
# (Docking Bay). Posted Cloud City Incinerator dested Cloud City:
# Incinerator. Posted Cloud City Chasm Walkway dested Cloud City:
# Chasm Walkway. Posted Bossk in Hound’s Tooth dested Bossk In Hound's
# Tooth. Posted Boba Fett in Slave 1 dested Boba Fett In Slave I.
# Posted Imperial-class Star Destroyer(V) dested Imperial-Class Star
# Destroyer (V) (VS2) File VS2O-36. Posted Executor dested Executor
# (Dark). Posted Bespin dested Bespin (Dark). Posted OS-72-1 in
# Obsidian 1 dested OS-72-1 In Obsidian 1. Posted Death Star Sentry (V)
# dested Death Star Sentry (V) (VS2) File VS2O-29-Death_Star_Sentry.png.
# Posted IIFYLOFD (V) dested IIFYLOFD (V) (VS2). Begin Landing Your
# Troops / I'm Sorry / Mobilization Points are extra start cards, not
# Starting Effect. Skip GEMP (original-VS dests). Format Premiere -
# Original VS2 (17 Jun 2002; VS2 legal 1 Jun 2002). General dest TITLE.
NELSON_DS = [
    (1, "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further", "OBJECTIVE"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Begin Landing Your Troops", "INTERRUPT"),
    (1, "I'm Sorry", "EFFECT"),
    (1, "Mobilization Points", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (3, "Security Battle Droid", "CHARACTER"),
    (1, "SSA-1015", "CHARACTER"),
    (1, "Nute Gunray", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Rune Haako", "CHARACTER"),
    (2, "Infantry Battle Droid", "CHARACTER"),
    (1, "SSA-719", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "OWO-1 With Backup", "CHARACTER"),
    (1, "Battle Droid Officer", "CHARACTER"),
    (1, "3B3-21", "CHARACTER"),
    (1, "SSA-306", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (1, "Stormtrooper Garrison", "CHARACTER"),
    (1, "P-60", "CHARACTER"),
    (1, "U-3PO (Yoo-Threepio)", "CHARACTER"),
    (1, "Lord Vader", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "3B3-10", "CHARACTER"),
    (1, "Aurra Sing", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "EV-9D9", "CHARACTER"),
    (1, "Droid Racks", "EFFECT"),
    (1, "Cloud City Occupation", "EFFECT"),
    (1, "Forced Servitude", "EFFECT"),
    (1, "They Must Never Again Leave This City", "EFFECT"),
    (1, "Dark Deal", "EFFECT"),
    (1, "There They Are!", "INTERRUPT"),
    (2, "Twi'lek Advisor", "INTERRUPT"),
    (2, "Oh, Switch Off", "INTERRUPT"),
    (1, "Drop Your Weapons", "INTERRUPT"),
    (1, "Bespin", "LOCATION"),
    (1, "Bespin: Cloud City", "LOCATION"),
    (1, "Cloud City: East Platform (Docking Bay)", "LOCATION"),
    (1, "Cloud City: Incinerator", "LOCATION"),
    (1, "Cloud City: Chasm Walkway", "LOCATION"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Imperial-Class Star Destroyer (V)", "STARSHIP"),
    (1, "Executor", "STARSHIP"),
    (1, "Obsidian 7", "STARSHIP"),
    (1, "OS-72-1 In Obsidian 1", "STARSHIP"),
    (1, "Obsidian Squadron TIE", "STARSHIP"),
    (2, "Battle Droid Blaster Rifle", "WEAPON"),
    (1, "Maul's Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Aurra Sing's Blaster Rifle", "WEAPON"),
]

NELSON_SHIELDS = [
    (1, "You Cannot Hide Forever", "DEFENSIVE_SHIELD"),
    (1, "Secret Plans", "DEFENSIVE_SHIELD"),
    (1, "I Find Your Lack Of Faith Disturbing (V)", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Death Star Sentry (V)", "DEFENSIVE_SHIELD"),
    (1, "Resistance", "DEFENSIVE_SHIELD"),
    (1, "There Is No Try", "DEFENSIVE_SHIELD"),
    (1, "Do They Have A Code Clearance?", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
]

# 23976 James "dabora" Zajic die die die.
# YAML Light / body Light TIGIH (match). Qty 58 as published: Starting 10
# + Characters 17 listed (header 18) + Effects 4 + Starships 1 + Interrupts
# 13 + Weapons 9 + Sites 4. Do not invent an 18th character. Unnamed 10
# defensive sheilds dest 60 only (no shields section).
# Author James "dabora" Zajic. Handle dabora. [[James Zajic]] missing —
# stub. [[dabora]] / [[Dabora]] / [[James]] MISSING. Do not dest onto a card.
# Posted there is good in him dested There Is Good In Him / I Can Save Him.
# Posted i feel the conflect dested I Feel The Conflict. Posted opee sea
# killeer dested Opee Sea Killer. Posted insurrection/ aim high dested
# Insurrection & Aim High (combo wrap File; dump page MISSING — dest combo
# without minting). Posted strik planing dested Strike Planning. Posted
# heading fo the medical frigate dested Heading For The Medical Frigate.
# Posted chef churpas hut dested Endor: Chief Chirpa's Hut. Posted endor
# landing platform dested Endor: Landing Platform (Docking Bay). Posted
# lukes light saber dested Luke's Lightsaber x2 (start + weapons). Posted
# luke skywalker jedi knight dested Luke Skywalker, Jedi Knight. Posted
# qui gon with light saber dested Qui-Gon Jinn With Lightsaber. Posted
# genral solo dested General Solo. Posted jarjar binks dested Jar Jar
# Binks. Posted genreel jar jar dested General Jar Jar. Posted obi won
# konobi padwan learner dested Obi-Wan Kenobi, Padawan Learner. Posted
# leia with gun dested Leia With Blaster Rifle. Posted luke rebel scout
# dested Luke Skywalker, Rebel Scout. Posted padme dested Padme Naberrie.
# Posted han with gun dested Han With Heavy Blaster Pistol. Posted genral
# crix madien dested General Crix Madine. Posted mase windu jedi master
# dested Mace Windu, Jedi Master. Posted lando with gun dested Lando With
# Blaster Pistol. Posted daughter of sywalker dested Daughter Of Skywalker.
# Posted artoo and threepio dested Artoo & Threepio File
# Ref2-L-artoo&threepio.gif (combo wrap File; dump page MISSING — dest
# combo without minting). Posted chewie with gun dested Chewie With
# Blaster Rifle. Posted uncontroeable fury dested Uncontrollable Fury.
# Posted trafic control dested printed Traffic Control File
# Premiere-L-trafficcontrol.gif (do NOT dest Traffic Control (V) VS3).
# Posted light saber proficancey dested Lightsaber Proficiency. Posted
# artoo detoo in red 5 dested Artoo-Detoo In Red 5. Posted jedi precence
# dested Jedi Presence. Posted arto i have bad filling dested Artoo, I
# Have A Bad Feeling About This. Posted rebel artierly dested Rebel
# Artillery. Posted gift of a mentor dested Gift Of The Mentor. Posted
# houjix combo dested Houjix & Out Of Nowhere. Posted on the edge dested
# On The Edge. Posted free ride combo dested Free Ride & Endor Celebration
# (combo wrap File; dump page MISSING — dest combo without minting).
# Posted out of commision combo dested Out Of Commission & Transmission
# Terminated. Posted intruder missle dested Intruder Missile. Posted
# captain tarples electropole dested Captain Tarpals' Electropole. Posted
# ewok catupult dested Ewok Catapult. Posted jar jars electropole dested
# Jar Jar's Electropole. Posted endor hidden forest trail / dence forest /
# back door dested colon Endor: titles. Posted home one doking bay dested
# Home One: Docking Bay. I Feel The Conflict / Opee Sea Killer /
# Insurrection & Aim High are TIGIH-deployed extra start cards. Strike
# Planning is extra start, not Starting Effect. Starting Effect omitted.
# Skip GEMP (printed-only POVS2). Format Premiere - Original VS2 (16 Jun
# 2002; VS2 legal 1 Jun 2002). General dest TITLE.
ZAJIC_LS = [
    (1, "There Is Good In Him / I Can Save Him", "OBJECTIVE"),
    (1, "I Feel The Conflict", "EFFECT"),
    (1, "Opee Sea Killer", "CREATURE"),
    (1, "Insurrection & Aim High", "INTERRUPT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Endor: Chief Chirpa's Hut", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (2, "Luke's Lightsaber", "WEAPON"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Yarua", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (1, "Jar Jar Binks", "CHARACTER"),
    (1, "General Jar Jar", "CHARACTER"),
    (1, "Obi-Wan Kenobi, Padawan Learner", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (1, "Luke Skywalker, Rebel Scout", "CHARACTER"),
    (1, "Padme Naberrie", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (1, "Mace Windu, Jedi Master", "CHARACTER"),
    (1, "Lando With Blaster Pistol", "CHARACTER"),
    (1, "Daughter Of Skywalker", "CHARACTER"),
    (1, "Artoo & Threepio", "CHARACTER"),
    (1, "Chewie With Blaster Rifle", "CHARACTER"),
    (1, "Uncontrollable Fury", "EFFECT"),
    (1, "Traffic Control", "EFFECT"),
    (2, "Lightsaber Proficiency", "EFFECT"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (2, "Jedi Presence", "INTERRUPT"),
    (3, "Artoo, I Have A Bad Feeling About This", "INTERRUPT"),
    (3, "Rebel Artillery", "INTERRUPT"),
    (1, "Gift Of The Mentor", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (1, "On The Edge", "INTERRUPT"),
    (1, "Free Ride & Endor Celebration", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (5, "Intruder Missile", "WEAPON"),
    (1, "Captain Tarpals' Electropole", "WEAPON"),
    (1, "Ewok Catapult", "WEAPON"),
    (1, "Jar Jar's Electropole", "WEAPON"),
    (1, "Endor: Hidden Forest Trail", "LOCATION"),
    (1, "Endor: Dense Forest", "LOCATION"),
    (1, "Endor: Back Door", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
]

# 23975 David "Icebreath" Kangas QMC Clouds.
# YAML Light / body Light QMC (match). Qty 60: Starting 8 + Locations 5
# + Characters 14 + Weapons 4 + Starships 11 + Vehicles 6 + Admiral's
# Orders 2 + Effects 2 + Interrupts 8. AUOF inside Starting (8) counts
# toward 60. Unnamed 10 shields dest 60 only (no shields section).
# Author David "Icebreath" Kangas. Handle Icebreath. [[David Kangas]]
# missing — stub. GPN [[Icebreath]] dump-not-stub pageid 42092 — redirect
# to [[David Kangas]] (canonical legal name; same unique handle as GPN
# icebreath Wesa Gotta Beatdown Deck!). Do not dest onto a card.
# Posted QMC/Independent Ops dested Quiet Mining Colony / Independent
# Operation. Posted CC Guest Quarters dested Cloud City: Guest Quarters.
# Posted Bespin dested Light Bespin. Posted Heading for the Frigate dested
# Heading For The Medical Frigate. Posted Keeping the Empire out Forever
# dested Keeping The Empire Out Forever. Posted Sai’tor Kal Fas (V)
# dested Sai'torr Kal Fas (V) (VS1). Posted Clouds dested Clouds. Posted
# Bespin CC dested Bespin: Cloud City. Posted CC Casino dested Cloud City:
# Casino. Posted Luke, JK dested Luke Skywalker, Jedi Knight. Posted
# Master Qui-Gon dested Master Qui-Gon. Posted Leia, Rebel Princess dested
# Leia, Rebel Princess. Posted Threepio, Naked dested C-3PO (See-Threepio).
# Posted Ric Olie’ dested Ric Olie. Posted Wedge, RSL dested Wedge
# Antilles, Red Squadron Leader. Posted Obi’s saber (premiere) dested
# Obi-Wan's Lightsaber. Posted Ani’s Saber dested Anakin's Lightsaber
# (Hoth). Posted Luke’s Saber dested Luke's Lightsaber. Posted Quiggy’s
# Saber (tat) dested Qui-Gon Jinn's Lightsaber. Posted Z-95 Bespin Defense
# Fighter dested Z-95 Bespin Defense Fighter (NOT Z-95 Headhunter). Posted
# H, C, and the F dested Han, Chewie, And The Falcon. Posted Red Squad 1
# dested Red Squadron 1. Posted Cloud Car dested Cloud Car (NOT Twin-Pod
# Cloud Car). Posted CC Celebration dested Cloud City Celebration. Posted
# CC Sabaac dested Cloud City Sabacc. Posted All Wings & Darklighter Spin
# dested All Wings Report In & Darklighter Spin (combo wrap File; dump
# page MISSING — dest combo without minting). Posted Sense & Recoil in
# Fear dested Sense & Recoil In Fear. Posted OOC & TT dested Out Of
# Commission & Transmission Terminated. Posted Off The Edge dested On The
# Edge. KTEOF / Squadron Assignments / Sai'torr are extra start, not
# Starting Effect. Guest Quarters / Bespin are QMC-deployed. Starting
# Effect AUOF. Skip GEMP (original-VS Sai'torr). Format Premiere -
# Original VS2 (16 Jun 2002; VS2 legal 1 Jun 2002). General dest TITLE.
KANGAS_LS = [
    (1, "Quiet Mining Colony / Independent Operation", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Cloud City: Guest Quarters", "LOCATION"),
    (1, "Bespin", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Keeping The Empire Out Forever", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (3, "Clouds", "LOCATION"),
    (1, "Bespin: Cloud City", "LOCATION"),
    (1, "Cloud City: Casino", "LOCATION"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Master Qui-Gon", "CHARACTER"),
    (1, "Obi-Wan Kenobi", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (2, "Lando Calrissian", "CHARACTER"),
    (2, "Tibanna Gas Miner", "CHARACTER"),
    (1, "C-3PO (See-Threepio)", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Ric Olie", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Mirax Terrik", "CHARACTER"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (3, "Z-95 Bespin Defense Fighter", "STARSHIP"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Pulsar Skate", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Queen's Royal Starship", "STARSHIP"),
    (1, "Defiance", "STARSHIP"),
    (1, "Independence", "STARSHIP"),
    (1, "Liberty", "STARSHIP"),
    (6, "Cloud Car", "VEHICLE"),
    (2, "Combined Fleet Action", "ADMIRALS_ORDER"),
    (1, "Thrown Back", "EFFECT"),
    (1, "Cloud City Celebration", "EFFECT"),
    (3, "Cloud City Sabacc", "INTERRUPT"),
    (1, "All Wings Report In & Darklighter Spin", "INTERRUPT"),
    (1, "Sense & Recoil In Fear", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
]

# 23962 matt "Tasa" wehner Good PunJab Hunting.
# YAML Light / body Light Hidden Base (match). Qty 60: Starting 8
# (Hidden Base dual + Rendezvous Point + Prepared Defenses + Twilight
# + Rycar (V) + Strike Planning + Dantooine + AUOF) + Locations 4 +
# Characters 14 + Ships 2 + Interrupts 24 + Effects 8. AUOF inside
# Starting (8) counts toward 60. Unnamed shields dest 60 only.
# Author matt "Tasa" wehner. Handle Tasa. [[Matt Wehner]] dump-not-stub
# pageid 36764 last=stable=53567. [[Tasa]] / [[Wehner]] / [[Matt]] /
# [[Punjab]] MISSING. Do not dest onto Hidden Base (redirects to
# current-virtual Hidden Base (V)). Do not dest onto a card.
# Posted Hidden Base dested Hidden Base / Systems Will Slip Through
# Your Fingers. Posted Rendevous Point dested Rendezvous Point.
# Posted An Unusal Ammount Of Fear dested An Unusual Amount Of Fear.
# Posted Rycar Ryjerd (v) dested Rycar Ryjerd (V) (VS2). Posted
# Dagobah Yoda's Hutt dested Dagobah: Yoda's Hut. Posted Dejark
# Hologameboard dested Dejarik Hologameboard. Posted Qui Gon w/stick
# dested Qui-Gon Jinn With Lightsaber. Posted EPP Luke dested Luke
# With Lightsaber. Posted EPP Obi dested Obi-Wan With Lightsaber.
# Posted Lando dested Lando Calrissian. Posted Han,Chewie, Falcon
# dested Han, Chewie, And The Falcon. Posted Escape Pod (v) dested
# Escape Pod (V) (VS2). Posted Sorry About The Mess/Blaster Prof
# dested Sorry About The Mess & Blaster Proficiency (combo wrap File;
# dump page MISSING — dest combo without minting). Posted
# Control/Tunnel Vision dested Control & Tunnel Vision. Posted
# Sense/Recoil In Fear dested Sense & Recoil In Fear. Posted Bith
# Shuffle/Desperate Reach dested The Bith Shuffle & Desperate Reach.
# Posted Free Ride/Endor Celebration dested Free Ride & Endor
# Celebration (combo wrap File; dump page MISSING — dest combo
# without minting). Posted KLorSlug (v) dested K'lor'slug (V) (VS2).
# Posted The Planet Furthest From dested The Planet That It's
# Farthest From. Posted Goo Ney Tay dested Goo Nee Tay. Twilight /
# Rycar / Strike Planning / Dantooine / Rendezvous Point are extra
# start, not Starting Effect. Starting Effect AUOF. Skip GEMP
# (original-VS Rycar + Escape Pod + K'lor'slug). Format Premiere -
# Original VS2 (16 Jun 2002; VS2 legal 1 Jun 2002). General dest
# TITLE (unnamed Regional without a finish; do not invent a
# tournament row).
WEHNER_LS = [
    (1, "Hidden Base / Systems Will Slip Through Your Fingers", "OBJECTIVE"),
    (1, "Rendezvous Point", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Twilight Is Upon Me", "EFFECT"),
    (1, "Rycar Ryjerd (V)", "EFFECT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "Dantooine", "LOCATION"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Dagobah", "LOCATION"),
    (1, "Dagobah: Yoda's Hut", "LOCATION"),
    (1, "Endor", "LOCATION"),
    (1, "Dejarik Hologameboard", "LOCATION"),
    (3, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (3, "Luke With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (3, "Lando Calrissian", "CHARACTER"),
    (2, "Corran Horn", "CHARACTER"),
    (1, "Phylo Gandish", "CHARACTER"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (3, "Escape Pod (V)", "INTERRUPT"),
    (4, "A Jedi's Resilience", "INTERRUPT"),
    (3, "Glancing Blow", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (3, "Control & Tunnel Vision", "INTERRUPT"),
    (3, "Sense & Recoil In Fear", "INTERRUPT"),
    (2, "Life Debt", "INTERRUPT"),
    (2, "The Force Is Strong With This One", "INTERRUPT"),
    (2, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Free Ride & Endor Celebration", "INTERRUPT"),
    (1, "K'lor'slug (V)", "EFFECT"),
    (1, "The Planet That It's Farthest From", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Lightsaber Proficiency", "EFFECT"),
    (2, "Goo Nee Tay", "EFFECT"),
    (2, "They Win This Round", "EFFECT"),
]

MANN_DS = [
    (1, "No Bargain", "EFFECT"),
    (1, "Power Of The Hutt", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Entrance Cavern", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Jabba's Palace: Dungeon", "LOCATION"),
    (1, "Jabba's Palace: Rancor Pit", "LOCATION"),
    (1, "Jabba's Palace: Droid Workshop", "LOCATION"),
    (1, "Jabba's Sail Barge: Passenger Deck", "LOCATION"),
    (2, "Jabba The Hutt", "CHARACTER"),
    (2, "Gailid", "CHARACTER"),
    (1, "Boelo", "CHARACTER"),
    (1, "Bib Fortuna", "CHARACTER"),
    (1, "Ephant Mon", "CHARACTER"),
    (1, "J'Quille", "CHARACTER"),
    (1, "Barada", "CHARACTER"),
    (1, "Klaatu", "CHARACTER"),
    (1, "Kithaba", "CHARACTER"),
    (2, "Bane Malar", "CHARACTER"),
    (1, "Giran", "CHARACTER"),
    (1, "Nysad", "CHARACTER"),
    (1, "Salacious Crumb", "CHARACTER"),
    (1, "Ree-Yees", "CHARACTER"),
    (1, "Brangus Glee", "CHARACTER"),
    (1, "Aurra Sing", "CHARACTER"),
    (1, "Jodo Kast", "CHARACTER"),
    (1, "Chall Bekan", "CHARACTER"),
    (2, "Gamorrean Guard", "CHARACTER"),
    (1, "Dengar", "CHARACTER"),
    (1, "Dengar With Blaster Carbine", "CHARACTER"),
    (1, "Bossk", "CHARACTER"),
    (1, "Boba Fett", "CHARACTER"),
    (1, "Boba Fett With Blaster Rifle", "CHARACTER"),
    (1, "Zuckuss", "CHARACTER"),
    (1, "4-LOM", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "IG-88", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Jabba's Sail Barge", "VEHICLE"),
    (1, "Bubo", "CREATURE"),
    (1, "Double Laser Cannon", "WEAPON"),
    (1, "Scum And Villainy", "EFFECT"),
    (9, "None Shall Pass", "INTERRUPT"),
    (4, "Imperial Barrier", "INTERRUPT"),
]

BHASKER_DS = [
    (1, "Let Them Make The First Move / At Last We Will Have Revenge", "OBJECTIVE"),
    (1, "Deep Hatred", "EFFECT"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Start Your Engines!", "EFFECT"),
    (1, "Sebulba's Podracer", "PODRACER"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Conduct Your Search", "EFFECT"),
    (1, "Endor: Back Door", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Imperial Holotable", "LOCATION"),
    (3, "Lord Maul", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (3, "Darth Vader With Lightsaber", "CHARACTER"),
    (2, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Keder The Black", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (2, "Blizzard 4", "VEHICLE"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Dengar In Punishing One", "STARSHIP"),
    (2, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Imperial Barrier", "INTERRUPT"),
    (1, "Blow Parried", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (2, "Maul Strikes", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Holonet Transmission", "INTERRUPT"),
    (1, "The Circle Is Now Complete", "INTERRUPT"),
    (1, "Vader's Obsession", "INTERRUPT"),
    (2, "Control", "INTERRUPT"),
    (1, "Force Field", "INTERRUPT"),
    (1, "Alter & Collateral Damage", "INTERRUPT"),
    (1, "Sense & Uncertain Is The Future", "INTERRUPT"),
    (1, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Bad Feeling Have I", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "The Phantom Menace", "EFFECT"),
    (1, "Visage Of The Emperor", "EFFECT"),
    (1, "Drop!", "EFFECT"),
    (1, "Mournful Roar", "EFFECT"),
    (1, "Qui-Gon's End", "EFFECT"),
    (1, "Presence Of The Force", "EFFECT"),
]

# 23859 Keskic LS. YAML tagged Light; body Light Profit. General dest TITLE.
# Author Vjeko "mighty_maul" Keskic (YAML ! string tag stripped). Handle
# mighty_maul already cited from 26368. [[Vjeko Keskic]] dump-not-stub
# pageid 33155. Do not dest onto Maul card pageid 13908 / Darth Maul 6743 /
# Lord Maul 7882. Qty 60. Named 10 Defensive Shields dest outside 60.
# AUOF inside Starting counts toward 60. Starting Interrupt HFTMF.
# Sai'torr Kal Fas (V) original VS1 has no STARTING: — extra start, omit
# Starting Effect. Insurrection & Aim High / The Camp are HFTMF-deployed
# extra start. Han / Audience Chamber / Jabba's Palace are Profit-deployed
# extra start. Posted Han With Blaster Pistol dested Han With Heavy Blaster
# Pistol. Posted Master Luke dested Luke Skywalker, Jedi Knight. Posted
# Threepio With His Parts Showing dested Threepio With His Parts Showing.
# Posted Lando With Vibro Ax dested Lando With Vibro-Ax. Posted Yoda Master
# Of The Force dested Yoda, Master Of The Force. Posted Leia Rebel Princess
# dested Leia, Rebel Princess. Posted Sal'torr Kal Fas dested Sai'torr Kal
# Fas (V) (VS1). Posted Do Or Do Not dested Do, Or Do Not. Posted Dunee Ta
# dested Ounee Ta. Posted Utimatum dested Ultimatum. Posted A Tragedy Has
# Occured dested A Tragedy Has Occurred. Posted Heading For The Mediacl
# Frigate dested Heading For The Medical Frigate. Posted Run Luke,Run dested
# Run Luke, Run!. Posted You Can´t Either Profit dested You Can Either
# Profit By This.... Posted Insurrection & Aim High wrap File dump MISSING
# dest combo without minting. Posted Sorry About The Mess & Blaster
# Proficiency wrap File dump MISSING dest combo without minting. Posted
# The Bith Shuffle & Desperate Reach dump LIVE 7676. Skip GEMP (original-VS
# Sai'torr). Format Premiere - Original VS2 (10 Jun 2002; VS2 legal 1 Jun
# 2002).
KESKIC_LS = [
    (1, "You Can Either Profit By This...", "OBJECTIVE"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Tatooine: Mos Espa Docking Bay", "LOCATION"),
    (2, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Tawss Khaa", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (3, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (2, "Ben Kenobi", "CHARACTER"),
    (2, "Lando With Vibro-Ax", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (2, "Qui-Gon Jinn", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Leia's Blaster Rifle", "WEAPON"),
    (2, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Sense", "INTERRUPT"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Run Luke, Run!", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Strike Blocked", "INTERRUPT"),
    (1, "Skywalkers", "INTERRUPT"),
    (1, "Gift Of The Mentor", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (2, "Clash Of Sabers", "INTERRUPT"),
    (2, "Double Agent", "INTERRUPT"),
    (2, "Fallen Portal", "INTERRUPT"),
    (1, "Help Me Obi-Wan Kenobi", "INTERRUPT"),
    (1, "Rebel Artillery", "INTERRUPT"),
    (1, "On The Edge", "INTERRUPT"),
    (2, "You Will Take Me To Jabba Now", "INTERRUPT"),
    (1, "Were You Looking For Me?", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Insurrection & Aim High", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "The Camp", "EFFECT"),
    (1, "A Gift", "EFFECT"),
    (1, "Underworld Contacts", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Seeking An Audience", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
]
KESKIC_LS_SHIELDS = [
    (1, "Aim High", "DEFENSIVE_SHIELD"),
    (1, "Do, Or Do Not", "DEFENSIVE_SHIELD"),
    (1, "Battle Plan", "DEFENSIVE_SHIELD"),
    (1, "A Tragedy Has Occurred", "DEFENSIVE_SHIELD"),
    (1, "Wise Advice", "DEFENSIVE_SHIELD"),
    (1, "A Close Race", "DEFENSIVE_SHIELD"),
    (1, "Don't Do That Again", "DEFENSIVE_SHIELD"),
    (1, "Ultimatum", "DEFENSIVE_SHIELD"),
    (1, "Ounee Ta", "DEFENSIVE_SHIELD"),
    (1, "Let's Keep A Little Optimism Here", "DEFENSIVE_SHIELD"),
]

# 23847 Bowman DS. YAML tagged Dark; body Dark BHBM. General dest TITLE.
# Author Geoff "GG BLADE" Bowman (YAML ! string tag stripped). Handle GG BLADE
# missing as a title — cite on [[Geoff Bowman]] dump-not-stub pageid 24621.
# Do not dest onto Maul card pageid 13908 / Darth Maul 6743 / Lord Maul 7882.
# Do not dest onto Blizzard 4. Qty 60. FIMA inside Starting (9) counts toward
# 60. Unnamed shields dest 60 only. Starting Interrupt Prepared Defenses.
# Starting Effect Fear Is My Ally. Throne Room / Your Destiny /
# Insignificant Rebellion are BHBM-deployed extra start. Imperial Arrest
# Order & Secret Plans / Mobilization Points / First Strike are PD-deployed
# extra start. Posted BHBM/TYFP dested Bring Him Before Me. Posted Throne
# Room dested Death Star II: Throne Room. Posted DVDLOTS dested Darth Vader,
# Dark Lord Of The Sith. Posted Boba Fett BH dested Boba Fett, Bounty Hunter.
# Posted Janus dested Janus Greejatus. Posted Mara Jade TEH dested Mara Jade,
# The Emperor's Hand. Posted Ability Ability Ability dested Ability, Ability,
# Ability. Posted Sebulba?s dested Sebulba's Podracer. Posted Mobilization
# Points dested printed Mobilization Points. Skip GEMP (printed-only POVS2).
# Format Premiere - Original VS2 (9 Jun 2002; VS2 legal 1 Jun 2002).
# YAML title extra spaces collapsed; published curly apostrophe kept.
BOWMAN_DS = [
    (1, "Bring Him Before Me / Take Your Father's Place", "OBJECTIVE"),
    (1, "Death Star II: Throne Room", "LOCATION"),
    (1, "Your Destiny", "EFFECT"),
    (1, "Insignificant Rebellion", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Mobilization Points", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Carida", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Lord Vader", "CHARACTER"),
    (2, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "P-60", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (2, "Janus Greejatus", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (3, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "IG-88 In IG-2000", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Ability, Ability, Ability", "EFFECT"),
    (2, "The Phantom Menace", "EFFECT"),
    (1, "Emperor's Power", "EFFECT"),
    (1, "Alter & Collateral Damage", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (1, "Main Course", "INTERRUPT"),
    (2, "Masterful Move", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "Monnok", "INTERRUPT"),
    (1, "Ommni Box & It's Worse", "INTERRUPT"),
    (1, "Operational As Planned", "INTERRUPT"),
    (1, "Podracer Collision", "INTERRUPT"),
    (1, "Rise, My Friend", "INTERRUPT"),
    (1, "Sense & Uncertain Is The Future", "INTERRUPT"),
    (2, "Sense", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Sebulba's Podracer", "PODRACER"),
]

# 23843 Wehner DS. YAML tagged Dark; body Dark Court. General dest TITLE.
# Author matt "Tasa" wehner (YAML ! string tag stripped). Handle Tasa already
# cited on [[Matt Wehner]] dump-not-stub pageid 36764 last=62061 from 23962.
# Do not dest onto Court dual pageid 7559 / Rancor 5192 / Gailid 5122 /
# Stinger 7724. Qty 60. FIMA inside Starting counts toward 60. Unnamed
# "Fear is My Ally + 10 shields, including the two new ones…" dest 60 only.
# Starting Interrupt Prepared Defenses. Starting Effect Fear Is My Ally.
# Dungeon / Audience Chamber / Great Pit Of Carkoon are Court-deployed extra
# start. His Name Is Anakin / All Wrapped Up / First Strike are PD-deployed
# extra start. Posted Court of The Vile Gangeter dested Court Of The Vile
# Gangster / I Shall Enjoy Watching You Die. Posted Dungeon dested Jabba's
# Palace: Dungeon. Posted Audience Chamber dested Jabba's Palace: Audience
# Chamber. Posted Great Pit of the Sarlaac dested Tatooine: Great Pit Of
# Carkoon. Posted Rancor Pitt dested Jabba's Palace: Rancor Pit. Posted
# Galid dested Gailid. Posted Master, Destroyers dested Master, Destroyers!.
# Posted Molator (v) dested Molator (V) (VS2) File VS2O-42-Molator.png.
# Posted Destroyer Droid x3 dested as posted (non-unique). Skip GEMP
# (original-VS Molator VS2). Format Premiere - Original VS2 (9 Jun 2002;
# VS2 legal 1 Jun 2002). YAML title published casing kept (`the` not `The`).
WEHNER_DS = [
    (1, "Court Of The Vile Gangster / I Shall Enjoy Watching You Die", "OBJECTIVE"),
    (1, "Jabba's Palace: Dungeon", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Tatooine: Great Pit Of Carkoon", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "His Name Is Anakin", "EFFECT"),
    (1, "All Wrapped Up", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Jabba's Palace: Rancor Pit", "LOCATION"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Lower Passages", "LOCATION"),
    (1, "Imperial Holotable", "LOCATION"),
    (1, "Mighty Jabba", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (2, "Gailid", "CHARACTER"),
    (2, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (2, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Jodo Kast", "CHARACTER"),
    (1, "Dengar With Blaster Carbine", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (3, "Destroyer Droid", "CHARACTER"),
    (2, "P-59", "CHARACTER"),
    (2, "P-60", "CHARACTER"),
    (1, "SSA-306", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (2, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Stinger", "STARSHIP"),
    (3, "Master, Destroyers!", "INTERRUPT"),
    (2, "Rolling, Rolling, Rolling", "INTERRUPT"),
    (2, "Neimoidian Advisor", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (2, "Masterful Move", "INTERRUPT"),
    (3, "Hidden Weapons", "INTERRUPT"),
    (1, "Trap Door", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (2, "Scum And Villainy", "EFFECT"),
    (2, "Bad Feeling Have I", "EFFECT"),
    (1, "Molator (V)", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Rancor", "CREATURE"),
]

# 23830 Chris "Wedge231" Wodicka 6th place Coruscant regionals.
# YAML ! string tag stripped. Handle Wedge231. [[Wedge231]] dump-not-stub
# pageid 41975 last=62246 is the GPN handle stub — redirect to
# [[Chris Wodicka]] (informed identity ~99.9%; YAML author Chris
# "Wedge231" Wodicka; GPN dest Wedge231 Wodicka's SYCFA Mains). Do NOT
# dest onto [[Wedge Antilles]] pageid 3629. Do NOT dest onto
# [[Admiral Piett]] pageid 137. Do NOT dest onto [[Blizzard 4]] pageid
# 7846. Do NOT dest onto Darth Maul cards. Two events named → dest TITLE
# is general {Player} {Published title}; hub Tournament lists gets one
# row per published event/finish. Mint [[2002 Coruscant Regionals]]
# (6th of 36) and [[2002 NYC Mini-Open]] (2-1). Qty 60. FIMA inside
# Start (7) counts toward 60. Unnamed "Fear Is My Ally + 10 shields"
# dest 60 only. Starting Card ISB Operations. Starting Interrupt
# Prepared Defenses. Starting Effect Fear Is My Ally. Coruscant (SE),
# IAO & Secret Plans, Mobilization Points, Combat Response are extra
# start (PD / ISB). Posted Mobilization Points dested printed
# Mobilization Points (not the combo). Posted Admrial Ozzel dested
# Admiral Ozzel. Posted Darth Maul (Tat) dested Darth Maul, Young
# Apprentice. Posted Darth Vader (V) dested Darth Vader (V) (VS1) File
# VS1O-10-Darth_Vader.png. Posted 5D6-RA-7 dested 5D6-RA-7 (Fivedesix).
# Posted Executor (FREE) dested Executor (Dark). Posted SFS L-s 9.3
# Laser Cannons dested SFS L-s9.3 Laser Cannons. Posted Short Range
# Fighters & Watch Your Back dested Short Range Fighters & Watch Your
# Back! (dump MISSING dest combo without minting). Posted We Must
# Accelerate Our Plans dested printed Coruscant Dark. Skip GEMP
# (original-VS Darth Vader VS1). Format Premiere - Original VS2
# (8 Jun 2002; VS2 legal 1 Jun 2002).
WODICKA_DS = [
    (1, "ISB Operations / Imperial Siege", "OBJECTIVE"),
    (1, "Coruscant", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Mobilization Points", "EFFECT"),
    (1, "Combat Response", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Bespin", "LOCATION"),
    (1, "Naboo", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Captain Jonus", "CHARACTER"),
    (1, "General Veers", "CHARACTER"),
    (1, "Darth Maul, Young Apprentice", "CHARACTER"),
    (1, "Darth Vader (V)", "CHARACTER"),
    (1, "Baron Soontir Fel", "CHARACTER"),
    (4, "Outer Rim Scout", "CHARACTER"),
    (1, "5D6-RA-7 (Fivedesix)", "CHARACTER"),
    (1, "Executor", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Devastator", "STARSHIP"),
    (1, "Maul's Sith Infiltrator", "STARSHIP"),
    (1, "Saber 1", "STARSHIP"),
    (1, "Scimitar 2", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Blizzard 1", "VEHICLE"),
    (1, "Blizzard 2", "VEHICLE"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Tempest 1", "VEHICLE"),
    (1, "Proton Bombs", "WEAPON"),
    (1, "SFS L-s9.3 Laser Cannons", "WEAPON"),
    (2, "They Must Never Again Leave This City", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Trample", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (3, "Imperial Command", "INTERRUPT"),
    (1, "Shut Him Up Or Shut Him Down", "INTERRUPT"),
    (1, "Unsalvageable", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "Short Range Fighters & Watch Your Back!", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Ommni Box & It's Worse", "INTERRUPT"),
    (2, "Battle Deployment", "ADMIRALS_ORDER"),
]

MCCOMBIE_LS = [
    (1, "Yavin 4: Massassi Throne Room", "LOCATION"),
    (1, "Naboo: Boss Nass' Chambers", "LOCATION"),
    (1, "Naboo: Otoh Gunga Entrance", "LOCATION"),
    (1, "Naboo: Battle Plains", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Home One: War Room", "LOCATION"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (2, "Leia, Rebel Princess", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (2, "Qui-Gon Jinn", "CHARACTER"),
    (1, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Captain Han Solo", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "C-3PO (See-Threepio)", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Tycho Celchu", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Boss Nass", "CHARACTER"),
    (1, "Rep Been", "CHARACTER"),
    (1, "Captain Tarpals", "CHARACTER"),
    (1, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (1, "Leia's Blaster Rifle", "WEAPON"),
    (1, "Millennium Falcon", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Green Squadron 3", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "A Few Maneuvers", "INTERRUPT"),
    (2, "We Wish To Board At Once", "INTERRUPT"),
    (1, "Run Luke, Run!", "INTERRUPT"),
    (1, "Jedi Presence", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "Don't Get Cocky", "INTERRUPT"),
    (3, "Wesa Gotta Grand Army", "INTERRUPT"),
    (1, "Rebel Artillery", "INTERRUPT"),
]

# 23798 Stephen "Texan" Beckham Too Hot in da Hot Tub.
# YAML tagged Light; body Light We'll Handle This. Qty 61 as published.
# Author Stephen "Texan" Beckham (YAML ! string tag stripped). Handle Texan.
# MISSING Stephen Beckham / Texan / Beckham — mint stub [[Stephen Beckham]].
# Do not dest onto [[We'll Handle This]] (redirects current-virtual).
# Do not dest onto [[Qui-Gon Jinn]] pageid 6703. Do not dest onto [[Yoda]].
# Do not dest onto [[Sense]] / [[Inner Strength]] / [[Baragwin]] / [[Kessel]].
# General dest TITLE (no tournament). AUOF inside Starting counts toward 61.
# Named 10 Defensive Shields dest OUTSIDE 60. Starting Interrupt HFTMF.
# Starting Effect An Unusual Amount Of Fear. Posted the new virtual saber
# puller dested Sai'torr Kal Fas (V) (VS1). Posted we'll handle this/duel of
# the fates dested We'll Handle This / Duel Of The Fates. Posted theed palace
# generator dested Naboo: Theed Palace Generator. Posted theed palace
# generator core dested Naboo: Theed Palace Generator Core. Posted jedi
# council chamber dested Coruscant: Jedi Council Chamber. Posted obi-wan,
# jedi knight dested Obi-Wan Kenobi, Jedi Knight. Posted threepio with this
# parts showing dested C-3PO (See-Threepio). Posted lando, scoundrel dested
# Lando Calrissian, Scoundrel. Posted enraged chewie dested Chewie, Enraged.
# Posted captain han dested Captain Han Solo. Posted falcon dested
# Millennium Falcon. Posted r2 in red 5 dested Artoo-Detoo In Red 5.
# Posted jar jars electopole dested Jar Jar's Electropole. Posted qui-gons
# lightsaber dested Qui-Gon's Lightsaber. Posted obi wan's lightsaber dested
# Obi-Wan's Lightsaber. Posted shocking info/grimtaash dested Shocking
# Information & Grimtaash (dump MISSING dest combo without minting; wrap
# File LIVE). Posted free ride& endor celebration dested Free Ride & Endor
# Celebration (dump MISSING dest combo without minting; wrap File LIVE).
# Posted star destroyer dested Star Destroyer!. Posted a tragedy has occured
# dested A Tragedy Has Occurred. Posted dont do that again dested Don't Do
# That Again. Posted only jedi carry that weapon dested Only Jedi Carry That
# Weapon. Skip GEMP (original-VS Sai'torr VS1). Format Premiere - Original
# VS2 (6 Jun 2002; VS2 legal 1 Jun 2002). YAML description extra spaces
# collapsed on dest Strategy; @#$% kept (Consoli-only vulgar-off TITLE).
BECKHAM_LS = [
    (1, "We'll Handle This / Duel Of The Fates", "OBJECTIVE"),
    (1, "Inner Strength", "EPIC_EVENT"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Another Pathetic Lifeform", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Scrambled Transmission", "EFFECT"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (3, "Qui-Gon Jinn, Jedi Master", "CHARACTER"),
    (3, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (2, "Leia With Blaster Rifle", "CHARACTER"),
    (2, "Captain Han Solo", "CHARACTER"),
    (1, "C-3PO (See-Threepio)", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (2, "Baragwin", "CHARACTER"),
    (2, "Millennium Falcon", "STARSHIP"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (2, "Intruder Missile", "WEAPON"),
    (2, "Bionic Hand", "DEVICE"),
    (2, "Jar Jar's Electropole", "WEAPON"),
    (1, "Qui-Gon's Lightsaber", "WEAPON"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Thrown Back", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Shocking Information & Grimtaash", "INTERRUPT"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Free Ride & Endor Celebration", "INTERRUPT"),
    (2, "Dodge", "INTERRUPT"),
    (2, "Sense", "INTERRUPT"),
    (1, "Fall Of The Legend", "INTERRUPT"),
    (1, "Throw Me Another Charge", "INTERRUPT"),
    (2, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Star Destroyer!", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (2, "Speak With The Jedi Council", "INTERRUPT"),
    (2, "Strike Blocked", "INTERRUPT"),
]
BECKHAM_SHIELDS = [
    (1, "A Close Race", "DEFENSIVE_SHIELD"),
    (1, "A Tragedy Has Occurred", "DEFENSIVE_SHIELD"),
    (1, "Aim High", "DEFENSIVE_SHIELD"),
    (1, "Battle Plan", "DEFENSIVE_SHIELD"),
    (1, "Don't Do That Again", "DEFENSIVE_SHIELD"),
    (1, "Only Jedi Carry That Weapon", "DEFENSIVE_SHIELD"),
    (1, "Ounee Ta", "DEFENSIVE_SHIELD"),
    (1, "Ultimatum", "DEFENSIVE_SHIELD"),
    (1, "Wise Advice", "DEFENSIVE_SHIELD"),
    (1, "Do, Or Do Not", "DEFENSIVE_SHIELD"),
]

# 23661 Uriah "travler" Watkins Testing Testing 1 2 3 (4 5 6).
# YAML tagged Light; body Light MWYHL Jedi Tests. Qty 59 as published
# (Starting (7) listed 6). Author Uriah "travler" Watkins (YAML ! tag
# stripped). Handle travler. MISSING Uriah Watkins / Travler / Watkins —
# mint stub [[Uriah Watkins]]. Do not dest onto [[Yoda]] pageid 4339.
# Do not dest onto [[Jar Jar Binks]] pageid 6685. Do not dest onto
# [[Padme Naberrie]] pageid 6699. Do not dest onto [[Great Warrior]].
# Do not dest onto [[Qui-Gon Jinn With Lightsaber]] as player.
# General dest TITLE. YAML title extra spaces collapsed. AUOF inside
# Starting counts toward 59. Named 10 Defensive Shields dest OUTSIDE 60.
# Starting Interrupt HFTMF. Starting Effect An Unusual Amount Of Fear.
# Posted Sai’torr Kal Fas (Virtual) dested Sai'torr Kal Fas (V) (VS1).
# Posted Mind What You Have Learned/Save You It Can dested dual.
# Posted Dagobah dested Light Dagobah system. Posted Dagobah Swamp /
# Jungle / Training Area / Yoda’s Hut dested colon Dagobah: titles.
# Posted Obi-Wan’s Lightsaber (Premiere) dested Premiere.
# Posted Traffic Control dested printed. Posted Another Pathetic Lifeform
# in shields dested Another Pathetic Lifeform (Reflections III: A
# Collector's Bounty) File Ref3-L-anotherpatheticlifeform.gif.
# Skip GEMP (original-VS Sai'torr VS1). Format Premiere - Original VS1
# (29 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Duplicate
# posts 23658/23657/23654/23653 same title same author — dest 23661 only.
WATKINS_LS = [
    (1, "Mind What You Have Learned / Save You It Can", "OBJECTIVE"),
    (1, "Dagobah", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Wise Advice", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (2, "Jar Jar Binks", "CHARACTER"),
    (3, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Mace Windu, Jedi Master", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (1, "Yoda", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Daughter Of Skywalker", "CHARACTER"),
    (2, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (2, "Chewie, Enraged", "CHARACTER"),
    (1, "Panaka, Protector Of The Queen", "CHARACTER"),
    (1, "Padme Naberrie", "CHARACTER"),
    (3, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (1, "Luke's Backpack", "DEVICE"),
    (1, "Reflection", "EFFECT"),
    (1, "Traffic Control", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Yoda's Hope", "EFFECT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (2, "The Signal", "INTERRUPT"),
    (1, "Great Warrior", "JEDI_TEST"),
    (1, "A Jedi's Strength", "JEDI_TEST"),
    (1, "Domain Of Evil", "JEDI_TEST"),
    (1, "Size Matters Not", "JEDI_TEST"),
    (1, "It Is The Future You See", "JEDI_TEST"),
    (1, "You Must Confront Vader", "JEDI_TEST"),
    (1, "Dagobah: Swamp", "LOCATION"),
    (1, "Dagobah: Jungle", "LOCATION"),
    (1, "Dagobah: Training Area", "LOCATION"),
    (1, "Dagobah: Yoda's Hut", "LOCATION"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (3, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (2, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Amidala's Blaster", "WEAPON"),
    (1, "Panaka's Blaster", "WEAPON"),
]
WATKINS_SHIELDS = [
    (1, "Battle Plan", "DEFENSIVE_SHIELD"),
    (1, "A Tragedy Has Occurred", "DEFENSIVE_SHIELD"),
    (1, "He Can Go About His Business", "DEFENSIVE_SHIELD"),
    (1, "Let's Keep A Little Optimism Here", "DEFENSIVE_SHIELD"),
    (1, "Only Jedi Carry That Weapon", "DEFENSIVE_SHIELD"),
    (1, "Ultimatum", "DEFENSIVE_SHIELD"),
    (1, "Aim High", "DEFENSIVE_SHIELD"),
    (1, "Your Ship?", "DEFENSIVE_SHIELD"),
    (1, "A Close Race", "DEFENSIVE_SHIELD"),
    (1, "Another Pathetic Lifeform (Reflections III: A Collector's Bounty)", "DEFENSIVE_SHIELD"),
]

# 23606 Vjeko "mighty_maul" Keskic Court Likes Direct Damage aka Gailid Superstar.
# YAML ! string tag stripped. Handle mighty_maul already cited. [[Vjeko Keskic]]
# dump-not-stub pageid 33155 last=62186. Do NOT dest onto Maul card pageid 13908.
# Do NOT dest onto Darth Maul card pageid 6743. Do NOT dest onto Lord Maul
# pageid 7882. Do NOT dest onto Court Of The Vile Gangster as player. Do NOT
# dest onto Gailid as player. Tournament dest ONE event Mainz 19 May 2002
# Regional Raltiir Tournament-Germany-Switzerland-Austria. Dest TITLE
# {Event} {Player} {Published title}. Mint [[2002 Ralltiir Regionals]]
# (encyclopedia Ralltiir; published raltiir/ralltir). 3rd place 5-1 into
# final fours. B. Winkelhaus won → [[Bastian Winkelhaus]] pageid 22195.
# Qty 60. FIMA INSIDE Effects (8) counts toward 60. Named 10 Defensive
# Shields dest OUTSIDE 60. Starting Interrupt omitted. Starting Effect
# Fear Is My Ally. Posted Court Of The Ville Gangster dested Court Of The
# Vile Gangster. Posted Jabba dested Jabba The Hutt (JP Audience Chamber
# / Power Of The Hutt / Mosep / Gailid). Posted Zukuss dested Zuckuss In
# Mist Hunter. Posted We Must Accerlerate Our Plans dested printed
# Coruscant Dark. Posted Start Your Engines dested Start Your Engines!.
# Posted Scum And Villiany dested Scum And Villainy. Posted Allegation Of
# Corruption dested Allegations Of Corruption. Posted We'll Let Fate-a
# Deside,Huh? dested We'll Let Fate-a Decide, Huh?. Posted There Is No
# Try in shields dested There Is No Try & Oppressive Enforcement (dump
# MISSING dest combo without minting; wrap File LIVE
# Ref2-D-thereisnotry&oppressiveenforcement.gif). Skip GEMP (printed-only
# original-VS-era dest). Format Premiere - Original VS1 (event 19 May 2002
# / post 27 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002).
KESKIC_COURT_DS = [
    (1, "Court Of The Vile Gangster / I Shall Enjoy Watching You Die", "OBJECTIVE"),
    (1, "Jabba's Palace: Lower Passages", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Tatooine: Great Pit Of Carkoon", "LOCATION"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Dungeon", "LOCATION"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Bane Malar", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Snoova", "CHARACTER"),
    (1, "Dengar With Blaster Carbine", "CHARACTER"),
    (1, "Jabba The Hutt", "CHARACTER"),
    (1, "Ephant Mon", "CHARACTER"),
    (1, "Boelo", "CHARACTER"),
    (1, "Aurra Sing", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (2, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Boba Fett With Blaster Rifle", "CHARACTER"),
    (1, "Mosep", "CHARACTER"),
    (1, "Gailid", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Vibro-Ax", "WEAPON"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Sebulba's Podracer", "PODRACER"),
    (3, "Podracer Collision", "INTERRUPT"),
    (4, "Jabba's Through With You", "INTERRUPT"),
    (3, "Imperial Barrier", "INTERRUPT"),
    (3, "None Shall Pass", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Start Your Engines!", "INTERRUPT"),
    (2, "Twi'lek Advisor", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Scum And Villainy", "EFFECT"),
    (1, "Power Of The Hutt", "EFFECT"),
    (1, "Hutt Influence", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
]
KESKIC_COURT_SHIELDS = [
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Secret Plans", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Resistance", "DEFENSIVE_SHIELD"),
    (1, "You Cannot Hide Forever", "DEFENSIVE_SHIELD"),
    (1, "Fanfare", "DEFENSIVE_SHIELD"),
    (1, "We'll Let Fate-a Decide, Huh?", "DEFENSIVE_SHIELD"),
    (1, "There Is No Try & Oppressive Enforcement", "DEFENSIVE_SHIELD"),
]

# 23561 Vjeko "mighty_maul" Keskic All Your Damage Belongs To Watto
# YAML tagged Light; body Dark Watto. General dest TITLE (no named
# tournament). Qty dest 60 listed (posted characters heading 24 with
# 23 listed; 1+6+23+4+1+17+8=60). FIMA inside Effects (8) counts toward
# dest 60. Named 10 Defensive Shields dest OUTSIDE 60 (same names as
# 23606 KESKIC_COURT_SHIELDS; dest posted order). Starting Interrupt
# omitted. Starting Effect FIMA. Starting Card dual NMNPND. Posted
# No Money,No Parts,No Deal/You're A Slave dested
# No Money, No Parts, No Deal! / You're A Slave?. Posted Executor
# starship dested Flagship Executor. Posted Mighty Jabba dested Mighty
# Jabba (pageid 7612). Posted Ghhk dested Ghhhk. Posted Search & Destroy
# dested Search And Destroy. Posted Imperial Rest Order & Secret Plans
# dested Imperial Arrest Order & Secret Plans. Posted Twi'lek Advisior
# dested Twi'lek Advisor. Posted There Is No Try in shields dested
# There Is No Try & Oppressive Enforcement. Posted We'll Let Fate-a
# Decide,Huh? dested We'll Let Fate-a Decide, Huh?. Skip GEMP
# (printed-only original-VS-era dest). Format Premiere - Original VS1
# (25 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Canonical
# Vjeko Keskic dump-not-stub pageid 33155 — UPDATE, do not mint. Handle
# mighty_maul already cited. Do not dest onto Watto card pageid 6809.
# Do not dest onto Maul / Darth Maul / Lord Maul. Do not dest onto
# No Money, No Parts, No Deal as player. Do not dest onto 23606 Court.
KESKIC_WATTO_DS = [
    (1, "No Money, No Parts, No Deal! / You're A Slave?", "OBJECTIVE"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Imperial Holotable", "LOCATION"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Tatooine: Watto's Junkyard", "LOCATION"),
    (1, "Tatooine: Mos Espa", "LOCATION"),
    (3, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Mighty Jabba", "CHARACTER"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (4, "Watto", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (2, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Televan Koreyy", "CHARACTER"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Flagship Executor", "STARSHIP"),
    (1, "Maul's Sith Infiltrator", "STARSHIP"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Twi'lek Advisor", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Unsalvageable", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (1, "Watto's Chance Cube", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (2, "Projective Telepathy", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (2, "Neimoidian Advisor", "INTERRUPT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Bad Feeling Have I", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Search And Destroy", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
]
KESKIC_WATTO_SHIELDS = [
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "Resistance", "DEFENSIVE_SHIELD"),
    (1, "There Is No Try & Oppressive Enforcement", "DEFENSIVE_SHIELD"),
    (1, "We'll Let Fate-a Decide, Huh?", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Secret Plans", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
    (1, "You Cannot Hide Forever", "DEFENSIVE_SHIELD"),
    (1, "Fanfare", "DEFENSIVE_SHIELD"),
]

# 23520 Vjeko "mighty_maul" Keskic H-TOWN Jedis vs NRW Jedis
# YAML tagged Light; body Light We'll Handle This. YAML title extra
# spaces collapsed on dest TITLE; keep H-TOWN casing. Description
# Heidelberg Jedis vs. Nord Rhein Westfalen Jedis. General dest TITLE
# (team-matchup published title; no named event/finish). Do not mint
# H-TOWN/NRW hubs. Strategy mentions unnamed last regional with QMC —
# do not invent a QMC dest or Ralltiir Light row. Qty dest 60
# (1+4+15+9+1+3+1+19+7=60). AUOF inside Effects (7) counts toward dest
# 60. Unnamed shields dest 60 only (none posted). Starting Interrupt
# omitted. Starting Effect AUOF. Starting Card printed dual We'll
# Handle This / Duel Of The Fates (wiki We'll Handle This REDIR to
# current-virtual dual — dest printed pageid 7824 File
# Ref3-L-wellhandlethis.gif). Posted Sai’torr Kal Fas without (V)
# dested Sai'torr Kal Fas (V) (VS1). Posted Han With Blaster Rifle
# dested Han With Heavy Blaster Pistol. Posted Inner Strengh dested
# Inner Strength. Posted I Did It dested I Did It!. Posted Interuder
# Missile dested Intruder Missile. Posted Armament Dismanteld dested
# Armament Dismantled. Posted Lando,Scroundel dested Lando Calrissian,
# Scoundrel. Posted Run Luke,Run dested Run Luke, Run!. Posted Thedd
# Palace Generator Core dested Naboo: Theed Palace Generator Core.
# Skip GEMP (original-VS Sai'torr VS1). Format Premiere - Original VS1
# (23 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Canonical
# Vjeko Keskic dump-not-stub pageid 33155 — UPDATE, do not mint. Handle
# mighty_maul already cited. Do not dest onto We'll Handle This
# current-virtual. Do not dest onto Yoda / Qui-Gon / Luke / Obi-Wan /
# Han / Leia / Sai'torr as player. Do not dest onto 23606 Court.
KESKIC_HTOWN_LS = [
    (1, "We'll Handle This / Duel Of The Fates", "OBJECTIVE"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (3, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (3, "Qui-Gon Jinn, Jedi Master", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (2, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (2, "Obi-Wan's Lightsaber", "WEAPON"),
    (3, "Intruder Missile", "WEAPON"),
    (2, "Luke's Lightsaber", "WEAPON"),
    (2, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Inner Strength", "EPIC_EVENT"),
    (1, "I Did It!", "EPIC_EVENT"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Anakin's Podracer", "PODRACER"),
    (1, "Podrace Prep", "INTERRUPT"),
    (2, "Darth Maul's Demise", "INTERRUPT"),
    (3, "A Step Backward", "INTERRUPT"),
    (2, "Strike Blocked", "INTERRUPT"),
    (3, "Too Close For Comfort", "INTERRUPT"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (1, "The Force Is Strong With This One", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
    (1, "Help Me Obi-Wan Kenobi", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Run Luke, Run!", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Armament Dismantled", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
]

# 23490 Mike "Quione" Noneofyourbusiness Rebel Strike Team- Stay the hell of
# endor. YAML Light / body Light RST. Last name is a joke; [[Mike]] redirects
# to [[Mike Thomas]] — UPDATE existing stub [[Mike (Quione)]] pageid 42159.
# Handle Quione wiki missing — cite; do not mint redirect. General dest TITLE
# (no named tournament). Qty dest 60 (1+2+1+4+22+7+6+6+8+3=60). AUOF inside
# Starting counts toward dest 60. Unnamed (Pick your 10) dest 60 only (no
# shields section). Starting Interrupt Heading For The Medical Frigate.
# Starting Effect AUOF. Starting Card printed dual Rebel Strike Team /
# Garrison Destroyed (wiki Rebel Strike Team REDIR to current-virtual dual —
# dest printed pageid 6055 File Endor-L-rebelstriketeam.gif). Posted Endor
# Landing Site dested Endor: Rebel Landing Site (Forest). Posted The Shield
# is Down dested The Shield Is Down!. Posted Squadren Assignments dested
# Squadron Assignments. Posted Orimaarko dested Orrimaarko. Posted Nien Numb
# dested Nien Nunb. Posted Gold Squadren 1 dested Gold Squadron 1. Posted
# Green Squadren 3 dested Green Squadron 3. Posted Ill take the leader dested
# I'll Take The Leader. Posted Deactivate the shield generator dested
# Deactivate The Shield Generator. Posted Out of nowhere dested Out Of
# Nowhere. Posted H’nemthe dested H'nemthe. Posted Chewbacca of Kashyyyk
# dested Chewbacca Of Kashyyyk. DECK EDIT substitutions stay in strategy;
# dest published Cards 60. Skip GEMP (printed-only original-VS-era dest).
# Format Premiere - Original VS1 (22 May 2002; VS1 legal 9 Mar 2002; VS2
# legal 1 Jun 2002). Do not dest onto Rebel Strike Team as player. Do not
# dest onto Mike Thomas. Do not dest onto Endor as player. Do not dest onto
# 24089 Saber dest as this dest.
QUIONE_RST_LS = [
    (1, "Rebel Strike Team / Garrison Destroyed", "OBJECTIVE"),
    (1, "Endor", "LOCATION"),
    (1, "Endor: Rebel Landing Site (Forest)", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "The Shield Is Down!", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Admiral Ackbar", "CHARACTER"),
    (1, "Daughter Of Skywalker", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (1, "General Calrissian", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Nien Nunb", "CHARACTER"),
    (1, "Sergeant Junkin", "CHARACTER"),
    (1, "Lieutenant Blount", "CHARACTER"),
    (1, "Wuta", "CHARACTER"),
    (1, "Major Panno", "CHARACTER"),
    (1, "Corporal Midge", "CHARACTER"),
    (1, "Tycho Celchu", "CHARACTER"),
    (1, "Corporal Kensaric", "CHARACTER"),
    (1, "Lieutenant Page", "CHARACTER"),
    (1, "Chewbacca Of Kashyyyk", "CHARACTER"),
    (1, "Colonel Cracken", "CHARACTER"),
    (1, "Sergeant Brooks Carlson", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (2, "H'nemthe", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Gold Squadron 1", "STARSHIP"),
    (1, "Green Squadron 3", "STARSHIP"),
    (1, "Tala 1", "STARSHIP"),
    (1, "Tala 2", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (1, "Defiance", "STARSHIP"),
    (1, "Home One", "STARSHIP"),
    (2, "Throw Me Another Charge", "INTERRUPT"),
    (1, "I Know", "INTERRUPT"),
    (1, "Endor Celebration", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (1, "Out Of Nowhere", "INTERRUPT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Battle Plan", "EFFECT"),
    (2, "Close Air Support", "EFFECT"),
    (1, "Endor: Back Door", "LOCATION"),
    (1, "Endor: Dense Forest", "LOCATION"),
    (1, "Endor: Ewok Village", "LOCATION"),
    (1, "Endor: Bunker", "LOCATION"),
    (1, "Endor: Great Forest", "LOCATION"),
    (1, "Roche", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (1, "Kashyyyk", "LOCATION"),
    (1, "Explosive Charge", "DEVICE"),
    (1, "I'll Take The Leader", "INTERRUPT"),
    (1, "Deactivate The Shield Generator", "INTERRUPT"),
]

# 23459 Wes "SeaRaptor" Brown Imperial Blues. YAML Dark / body Dark Endor
# Ops. YAML ! stripped. Canonical [[Wes Brown]] NEW stub (wiki MISS Wes
# Brown / Wesley Brown). Handle SeaRaptor already a GPN stub pageid 41776
# last=61117 with GPN dest [[SeaRaptor Imperial Blues (EOPS)]] 41775/61116.
# Redirect [[SeaRaptor]] → [[Wes Brown]] (Wedge231/Icebreath/HuntaWarya/Kiriel
# pattern). Do NOT dest 23459 onto the GPN dest title. Cite GPN dest in See
# also. General dest TITLE (no named tournament). Qty dest 60
# (9+4+17+9+7+3+4+7=60). FIMA inside Starting (9) counts toward dest 60.
# Unnamed DEFENSIVE SHIELDS [pick 10, any 10] dest 60 only (no shields
# section). Starting Interrupt Prepared Defenses. Starting Effect Fear Is
# My Ally. Starting Card printed dual Endor Operations / Imperial Outpost
# (wiki Endor Operations MISS; printed dual HIT pageid 6161 File
# Endor-D-endoroperations.gif). Posted Darth Vader (V) dested Darth Vader
# (V) (VS1) File VS1O-10-Darth_Vader.png. Posted Executor starship dested
# Flagship Executor (wiki_card Executor dests the Dagobah system; GPN dest
# used Executor system). Posted Denegar in Punishing One dested Dengar In
# Punishing One. Posted Endor Occupation & Masterful Move dested Masterful
# Move & Endor Occupation. Posted Imperial Arrest Order dested printed
# (not combo). Posted Tempest 1 dested Tempest 1 (GPN dest used Tempest
# Scout 1). Skip GEMP (original-VS Darth Vader VS1). Format Premiere -
# Original VS1 (21 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002).
# Do not dest onto SeaRaptor Imperial Blues (EOPS). Do not dest onto
# Darth Maul. Do not dest onto Darth Vader. Do not dest onto Admiral Piett.
# Do not dest onto Blizzard 4. Do not dest onto Endor Operations as player.
BROWN_DS = [
    (1, "Endor Operations / Imperial Outpost", "OBJECTIVE"),
    (1, "Endor", "LOCATION"),
    (1, "Endor: Bunker", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Do They Have A Code Clearance?", "EFFECT"),
    (1, "Imperial Arrest Order", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Fondor", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (1, "Naboo", "LOCATION"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (1, "Admiral Motti", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Captain Godherdt", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Darth Vader (V)", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (1, "DS-61-2", "CHARACTER"),
    (1, "General Veers", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Lieutenant Cabbel", "CHARACTER"),
    (1, "Officer Evax", "CHARACTER"),
    (1, "U-3PO (Yoo-Threepio)", "CHARACTER"),
    (1, "Avenger", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Dengar In Punishing One", "STARSHIP"),
    (1, "Devastator", "STARSHIP"),
    (1, "Dominator", "STARSHIP"),
    (1, "Flagship Executor", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Blizzard 2", "VEHICLE"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Blizzard Scout 1", "VEHICLE"),
    (1, "Tempest 1", "VEHICLE"),
    (1, "Tempest Scout 3", "VEHICLE"),
    (1, "Tempest Scout 4", "VEHICLE"),
    (1, "Tempest Scout 6", "VEHICLE"),
    (2, "Battle Deployment", "ADMIRALS_ORDER"),
    (1, "We're In Attack Position Now", "ADMIRALS_ORDER"),
    (1, "Closed Door", "EFFECT"),
    (1, "Imperial Decree", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Ominous Rumors", "EFFECT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (3, "Imperial Command", "INTERRUPT"),
    (1, "Operational As Planned", "INTERRUPT"),
    (2, "Trample", "INTERRUPT"),
]

# 23458 Cody "MegaScrub" Jewell ’Saber Combat My Way V1 00(UnRevised). YAML
# Light / body Light We'll Handle This. YAML ! stripped. Keep published
# leading U+2019 and V1 00(UnRevised) spacing. Canonical [[Cody Jewell]] NEW
# stub (wiki MISS). Handle MegaScrub MISS — cite; do not mint redirect
# (joker_phreak/el-diablo/Quione pattern). Do NOT dest onto [[Mike (Quione)
# Saber combat my way]] pageid 42158 (24089 later revised dest). Do NOT dest
# onto We'll Handle This current-virtual. Do NOT dest onto Lightsaber Combat
# / Yoda / Qui-Gon / Luke / Obi-Wan / Sai'torr as player. General dest TITLE
# (names last 2 tournaments without event names; lost twice to Brian Hunter;
# beat David Jones and Chris Fanchi — mention in strategy only). Qty dest 60
# (1+1+3+1+1+1+7+3+6+12+24=60). AUOF inside Starting counts toward dest 60.
# Named 10 Defensive Shields dest OUTSIDE 60 (Watkins 23661 pattern).
# Starting Interrupt omitted. Starting Effect An Unusual Amount Of Fear.
# Starting Card printed dual We'll Handle This / Duel Of The Fates (wiki
# We'll Handle This REDIR current-virtual; dest printed pageid 7824 File
# Ref3-L-wellhandlethis.gif). Posted Sai.Torr Kal Fas dested Sai'torr Kal
# Fas (V) (VS1) File VS1O-06-Saitorr_Kal_Fas.png. Posted Goo Nee Tay OR
# Honor OR Sai.Torr dest all three in Effects(6). Posted Out of Commission
# AND Transmission Terminated dested separately. Posted Shocking
# Information/ Grimtaash dested combo wrap File (dump TITLE MISS — do not
# mint). Posted Obi-Wan Kenobi (P) dested Premiere. Posted Qui-Gon Jinn
# (Tat) dested Tatooine. Posted Obi-Wan.s Lightsaber (P) dested Premiere.
# Posted Qui-Gon.s Lightsaber (R3) dested Qui-Gon Jinn's Lightsaber.
# Posted Another Pathetic Lifeform in shields dested Reflections III
# Collector's Bounty. Skip GEMP (original-VS Sai'torr VS1). Format Premiere
# - Original VS1 (21 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002).
JEWELL_LS = [
    (1, "We'll Handle This / Duel Of The Fates", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Tatooine: Podrace Arena", "LOCATION"),
    (1, "Inner Strength", "EPIC_EVENT"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Anakin's Podracer", "PODRACER"),
    (4, "Intruder Missile", "WEAPON"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Qui-Gon Jinn's Lightsaber", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (2, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Disarmed", "EFFECT"),
    (1, "Weapon Of A Fallen Mentor", "EFFECT"),
    (1, "They Win This Round", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Luke Skywalker, Rebel Scout", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Obi-Wan Kenobi", "CHARACTER"),
    (1, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (1, "Qui-Gon Jinn", "CHARACTER"),
    (1, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (1, "Mace Windu, Jedi Master", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Artoo, Brave Little Droid", "CHARACTER"),
    (4, "Rebel Barrier", "INTERRUPT"),
    (2, "A Step Backward", "INTERRUPT"),
    (2, "Strike Blocked", "INTERRUPT"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (2, "A Jedi's Focus", "INTERRUPT"),
    (2, "Losing Track", "INTERRUPT"),
    (1, "Jedi Escape", "INTERRUPT"),
    (1, "Out Of Commission", "INTERRUPT"),
    (1, "Shocking Information & Grimtaash", "INTERRUPT"),
    (1, "Sense", "INTERRUPT"),
    (1, "Glancing Blow", "INTERRUPT"),
    (1, "Transmission Terminated", "INTERRUPT"),
    (1, "Podrace Prep", "INTERRUPT"),
    (1, "Endor Celebration", "INTERRUPT"),
    (1, "The Force Is Strong With This One", "INTERRUPT"),
    (1, "Too Close For Comfort", "INTERRUPT"),
]
JEWELL_SHIELDS = [
    (1, "Don't Do That Again", "DEFENSIVE_SHIELD"),
    (1, "A Tragedy Has Occurred", "DEFENSIVE_SHIELD"),
    (1, "Ultimatum", "DEFENSIVE_SHIELD"),
    (1, "Your Ship?", "DEFENSIVE_SHIELD"),
    (1, "Let's Keep A Little Optimism Here", "DEFENSIVE_SHIELD"),
    (1, "Battle Plan", "DEFENSIVE_SHIELD"),
    (1, "Only Jedi Carry That Weapon", "DEFENSIVE_SHIELD"),
    (1, "Another Pathetic Lifeform (Reflections III: A Collector's Bounty)", "DEFENSIVE_SHIELD"),
    (1, "A Close Race", "DEFENSIVE_SHIELD"),
    (1, "Aim High", "DEFENSIVE_SHIELD"),
]

# 23438 Clayton "TheDohMan" Atkin Atkins’ Alderaan 2nd Place TDIGWATT.
# YAML ! stripped. Keep published curly Atkins’ (U+2019). Canonical
# [[Clayton Atkin]] dump-not-stub pageid 28553 — UPDATE. Handle TheDohMan
# MISS — cite; do not mint redirect (joker_phreak/el-diablo/Quione
# pattern). Do NOT dest onto Clayton Atkins (MISS). Do NOT dest onto Atkins
# as player. Do NOT dest onto TDIGWATT / Maul / Vader / Blizzard 4 as player.
# Tournament dest TITLE {Event} {Player} {Published title}. Named event
# Alderaan regionals 2nd Place 3-1 lost final to Peter Nordstrom. Mint
# [[2002 Alderaan Regionals]]. Date dest 18 May 2002 from Saturday’s final
# duel on a 20 May 2002 (Monday) post. TFN scheduled Alderaan May 25 2002 at
# Kriers, Modesto CA — do NOT stamp May 25; site omitted. Winner
# [[Peter Nordstrom]] pageid 42522 (list unpublished). Qty dest 60
# (8+6+18+7+2+12+5+2=60). FIMA inside Starting (8) counts. Unnamed
# "(with 10 sheilds)" dest 60 only. Starting Interrupt Prepared Defenses.
# Starting Effect Fear Is My Ally. Starting Card printed dual TDIGWATT.
# Posted Executor dested Flagship Executor. Posted Black 2 dested Black 2
# (V) (VS1) from strategy “Black 2 (virtual)”. Posted Masterful Move &
# Endor Celebration dested Masterful Move & Endor Occupation (dump TITLE
# MISS — do not mint). Posted Bespin Cloud City dested Bespin: Cloud City
# File CC-D-bespincloudcity.gif. Posted Short Range Fighters & Watch your
# Back dested Short Range Fighters & Watch Your Back! File. Posted Combat
# Responce dested Combat Response. Posted Prepared Defences dested Prepared
# Defenses. Posted Dr. Evazon dested Dr. Evazan. Posted SFS Ls9.3 Lasser
# Cannons dested SFS L-s9.3 Laser Cannons. Posted I’m getting Shafted dested
# printed dual Pray I Don't Alter It Any Further. Skip GEMP (original-VS
# Prophetess VS1 + Black 2 VS1). Format Premiere - Original VS1 (18–20 May
# 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002).
ATKIN_DS = [
    (1, "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further", "OBJECTIVE"),
    (1, "Cloud City: Upper Walkway", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Combat Response", "EFFECT"),
    (1, "I'm Sorry", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Bespin", "LOCATION"),
    (1, "Bespin: Cloud City", "LOCATION"),
    (1, "Cloud City: Carbonite Chamber", "LOCATION"),
    (1, "Cloud City: Chasm Walkway", "LOCATION"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (1, "Cloud City: East Platform (Docking Bay)", "LOCATION"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Bane Malar", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Prophetess (V)", "CHARACTER"),
    (1, "Brangus Glee", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Baron Soontir Fel", "CHARACTER"),
    (1, "DS-61-2", "CHARACTER"),
    (1, "Major Turr Phennir", "CHARACTER"),
    (1, "Flagship Executor", "STARSHIP"),
    (1, "Saber 1", "STARSHIP"),
    (1, "Saber 2", "STARSHIP"),
    (1, "Black 2 (V)", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Stinger", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (2, "SFS L-s9.3 Laser Cannons", "WEAPON"),
    (1, "Twi'lek Advisor", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "Stunning Leader", "INTERRUPT"),
    (2, "Dark Maneuvers & Tallon Roll", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Short Range Fighters & Watch Your Back!", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (1, "Imperial Command", "INTERRUPT"),
    (1, "Overload", "INTERRUPT"),
    (1, "Dark Deal", "EFFECT"),
    (2, "Cloud City Occupation", "EFFECT"),
    (1, "Bad Feeling Have I", "EFFECT"),
    (1, "They Must Never Again Leave This City", "EFFECT"),
    (2, "Battle Deployment", "ADMIRALS_ORDER"),
]

# 23385 Matthew "Secret Sith" H-T Secret Siths Profit. YAML Light / body
# Light Profit. YAML ! stripped. Inventory author_guess is the description
# ("Profit deck from a beginner.") — NOT the author. Canonical
# [[Matthew Harrison-Trainor]] dump-not-stub pageid 21373 (Matt H-T /
# MatthewHT / MHT already mapped). Handle Secret Sith cited; no redirect
# (MegaScrub pattern). General dest TITLE (no named event). Qty 60.
# Starting Interrupt Heading For The Medical Frigate. Starting Effect
# omitted (posted “I do not have the starting effect”). Unnamed shields
# dest 60 only (none posted). Posted Profit dested printed dual You Can
# Either Profit By This... / Or Be Destroyed. Posted Master Luke dested
# Luke Skywalker, Jedi Knight. Posted Luke With Saber dested Luke With
# Lightsaber. Posted Chewbacca, protector dested Chewbacca, Protector.
# Posted Lando with Blaster Pistol dested Lando With Blaster Pistol.
# Posted BoShek (V) dested Bo Shek (V) (VS1) File VS1O-01-Bo Shek.png.
# Posted Orrimaako dested Orrimaarko. Posted Panaka Protector of the Queen
# dested Panaka, Protector Of The Queen. Posted Squadron Assingments dested
# Squadron Assignments. Posted Don't Get @#$%y dested Don't Get Cocky.
# Posted Swing and A Miss dested Swing-And-A-Miss. Posted Fallen portal
# dested Fallen Portal. Posted I have a Really Bad Feeling about this
# dested I Have A Really Bad Feeling About This. Posted It's a trap dested
# It's A Trap!. Posted Jedi saber dested Jedi Lightsaber. Posted Han's
# Heavy Blaster Pistol (V) dested Han's Heavy Blaster Pistol (V) (VS1)
# File VS1O-04-Hans Heavy Blaster Pistol.png. Posted Tatooine Docking Bay
# dested Tatooine: Docking Bay 94. Skip GEMP (original-VS Bo Shek VS1 +
# Han's Heavy Blaster Pistol VS1). Format Premiere - Original VS1 (16 May
# 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Do not dest onto
# Profit / You Can Either Profit By This as player. Do not dest onto
# Secret Sith as a new person. Do not dest onto BoShek. Do not dest onto
# Han's Heavy Blaster Pistol (V) current-virtual. Do not dest onto Jedi
# Lightsaber as player. Do not dest onto Bravo 2 as player. Do not dest
# onto 2002 Origins Open Ken Cross Squires Origins Profit. Do not dest
# onto CL. Do not dest age-11 private life onto the encyclopedia dest.
HT_LS = [
    (1, "You Can Either Profit By This... / Or Be Destroyed", "OBJECTIVE"),
    (1, "General Solo", "CHARACTER"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Insurrection & Aim High", "INTERRUPT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Do, Or Do Not", "EFFECT"),
    (1, "Han Solo", "CHARACTER"),
    (2, "Luke Skywalker, Rebel Scout", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Chewbacca, Protector", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Lando With Blaster Pistol", "CHARACTER"),
    (1, "Bo Shek (V)", "CHARACTER"),
    (1, "Caldera Righim", "CHARACTER"),
    (1, "Talon Karrde", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Panaka, Protector Of The Queen", "CHARACTER"),
    (1, "Master Qui-Gon", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Mirax Terrik", "CHARACTER"),
    (1, "Colonel Cracken", "CHARACTER"),
    (1, "Officer Dolphe", "CHARACTER"),
    (1, "Houjix", "INTERRUPT"),
    (1, "Dodge", "INTERRUPT"),
    (1, "Somersault", "INTERRUPT"),
    (1, "Life Debt", "INTERRUPT"),
    (1, "Smoke Screen", "INTERRUPT"),
    (1, "Warrior's Courage", "INTERRUPT"),
    (1, "Lost In The Wilderness", "INTERRUPT"),
    (1, "The Force Is Strong With This One", "INTERRUPT"),
    (1, "Don't Get Cocky", "INTERRUPT"),
    (1, "Swing-And-A-Miss", "INTERRUPT"),
    (3, "Rebel Barrier", "INTERRUPT"),
    (1, "It Could Be Worse", "INTERRUPT"),
    (1, "Fallen Portal", "INTERRUPT"),
    (1, "I Have A Really Bad Feeling About This", "INTERRUPT"),
    (2, "It's A Trap!", "INTERRUPT"),
    (1, "Blaster Proficiency", "INTERRUPT"),
    (2, "Weapon Levitation", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (2, "Jedi Lightsaber", "WEAPON"),
    (1, "Han's Heavy Blaster Pistol (V)", "WEAPON"),
    (1, "Bravo 2", "STARSHIP"),
    (1, "Tala 1", "STARSHIP"),
    (1, "Pulsar Skate", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Tatooine: Docking Bay 94", "LOCATION"),
]

# 23346 Peter "marvin" Jurcovic There Are Those Droidekas. YAML Light /
# body Dark TDIGWATT Dark Deal. YAML ! stripped. Inventory author_guess
# is the description ("And actually, they're not real men (woman), but
# hey, who cares?") — NOT the author. Canonical [[Peter Jurcovic]]
# dump-not-stub pageid 41536 last=60818. Handle marvin already cited
# from 26448; no redirect. General dest TITLE (unnamed tournament prize
# pack; do not mint a hub). Qty 60 (1+6+21+7+15+10=60). FIMA INSIDE
# Effects (10) counts. Unnamed shields dest 60 only (none posted).
# Starting Interrupt Prepared Defenses. Starting Effect Fear Is My Ally.
# Starting Card printed dual TDIGWATT. Posted Droid Manufacturing
# Platform dested printed dual Pray I Don't Alter It Any Further.
# Posted P59 (The Rep) dested P-59. Posted P60 dested P-60. Posted
# 4lom w/gun dested 4-LOM With Concussion Rifle. Posted IG88 w/gun
# dested IG-88 With Riot Gun. Posted Owo1 w/backup dested OWO-1 With
# Backup. Posted U3PO dested U-3PO (Yoo-Threepio). Posted Emperor
# dested Emperor Palpatine. Posted Darth Vader,DLOTS dested Darth
# Vader, Dark Lord Of The Sith. Posted Bossk in Buss dested Bossk In
# Hound's Tooth. Posted Boba Fett In Slave1 dested Boba Fett In Slave I.
# Posted Bespin Cloud City dested Bespin: Cloud City. Posted Cloud City
# East Platform dested Cloud City: East Platform (Docking Bay). Posted
# Cloud City Casino dested Cloud City: Casino. Posted Cloud City
# Incinerator dested Cloud City: Incinerator. Posted IAO & SP dested
# Imperial Arrest Order & Secret Plans. Posted Precision Targetting
# dested Precision Targeting. Posted Dard Deal dested Dark Deal.
# Posted Where Are Those Droidekas? dested Where Are Those Droidekas?!.
# Posted Master, Destroyers dested Master, Destroyers!. Posted Omni Box
# & It's Worse dested Ommni Box & It's Worse. Skip GEMP (no original
# (V) cards; format cell Premiere - Original VS1 by legal day 14 May
# 2002). Do not dest onto Peter Jurcovic Hold Me Thrill Me Kiss Me
# Kill Me. Do not dest onto Where Are Those Droidekas?! as player.
# Do not dest onto Maul / Darth Maul / Lord Maul as player. Do not
# dest onto Destroyer Droid as player. Do not dest onto TDIGWATT as
# player. Do not dest onto Guri as player. Do not dest onto P-59 as
# player. Do not dest onto marvin as a new person. Do not dest onto
# inventory author_guess.
JURCOVIC_WATD = [
    (1, "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further", "OBJECTIVE"),
    (1, "Bespin", "LOCATION"),
    (1, "Bespin: Cloud City", "LOCATION"),
    (1, "Cloud City: Casino", "LOCATION"),
    (1, "Cloud City: Incinerator", "LOCATION"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (1, "Cloud City: East Platform (Docking Bay)", "LOCATION"),
    (1, "P-59", "CHARACTER"),
    (1, "P-60", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (7, "Destroyer Droid", "CHARACTER"),
    (1, "OWO-1 With Backup", "CHARACTER"),
    (2, "Battle Droid Officer", "CHARACTER"),
    (1, "U-3PO (Yoo-Threepio)", "CHARACTER"),
    (2, "Darth Maul", "CHARACTER"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (2, "Maul's Sith Infiltrator", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Dengar In Punishing One", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (2, "Oh, Switch Off", "INTERRUPT"),
    (1, "Abyssin Ornament", "INTERRUPT"),
    (1, "Stunning Leader", "INTERRUPT"),
    (1, "Master, Destroyers!", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (1, "Ommni Box & It's Worse", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Combat Response", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "I'm Sorry", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (1, "Where Are Those Droidekas?!", "EFFECT"),
    (1, "Precision Targeting", "EFFECT"),
    (2, "Dark Deal", "EFFECT"),
    (1, "Cloud City Occupation", "EFFECT"),
]

# 23334 Taylor "JediMaster10" Hayward I like blowin sht up. YAML Light /
# body Light RST. YAML ! stripped. Inventory author_guess is the Light
# tag — NOT the author. Canonical [[Taylor Hayward]] NEW stub. Handle
# JediMaster10 cited; no redirect (MegaScrub pattern). General dest TITLE
# (upcoming unnamed NON-EP1 tournament; do not mint a hub). Qty 60
# (6+20+15+6+5+5+1+1+1=60). No FIMA/AUOF. Unnamed shields dest 60 only
# (none posted). Starting Interrupt Heading For The Medical Frigate.
# Starting Effect omitted. Starting Card printed dual Rebel Strike Team /
# Garrison Destroyed. Posted Endor dested Light Endor system. Posted
# Rebel Landing Platform dested Endor: Rebel Landing Site (Forest).
# Posted Back Door dested Endor: Back Door. Posted Bunker dested Endor:
# Bunker. Posted Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut.
# Posted Landing Platform dested Endor: Landing Platform (Docking Bay).
# Posted Chewbacca Of Kashyyk dested Chewbacca Of Kashyyyk. Posted
# Chewie Enraged dested Chewie, Enraged. Posted Han With Pistol dested
# Han With Heavy Blaster Pistol. Posted Luke Skywalker dested Luke
# Skywalker (V) (VS1) from strategy “Luke Skywalker is actually the
# virtual one”. Posted Luke With Sword dested Luke With Lightsaber.
# Posted Niem Numb dested Nien Nunb. Posted Obi with Sword dested
# Obi-Wan With Lightsaber. Posted Orrimarko dested Orrimaarko. Posted
# Wedge Red squad leader dested Wedge Antilles, Red Squadron Leader.
# Posted All Wing's combo dested All Wings Report In & Darklighter Spin.
# Posted It's a hit dested It's A Hit!. Posted On the edge dested On
# The Edge. Posted OOC/TT dested Out Of Commission & Transmission
# Terminated. Posted Throw me another Charge dested Throw Me Another
# Charge. Posted Weapon Lev dested Weapon Levitation. Posted The Shield
# Is Down dested The Shield Is Down!. Posted Artoo in Red 5 dested
# Artoo-Detoo In Red 5. Posted X-wing Lasor Cannon dested X-wing Laser
# Cannon. Posted I'll Take The Leader dested Admiral's Order. Posted
# Deactivate the Shield Generator dested Deactivate The Shield
# Generator. Skip GEMP (original-VS Luke Skywalker VS1). Format
# Premiere - Original VS1 (13 May 2002; VS1 legal 9 Mar 2002; VS2 legal
# 1 Jun 2002). Keep published sht on dest TITLE. Do not dest onto
# Doug Taylor. Do not dest onto Jacob Taylor. Do not dest onto Rebel
# Strike Team as player. Do not dest onto Luke Skywalker (V)
# current-virtual. Do not dest onto Mike (Quione) Rebel Strike Team-
# Stay the hell of endor. Do not dest onto JediMaster10 as a new
# person. Do not dest onto inventory author_guess Light. Strategy
# UPDATE #1/#2 stay original-post; dest 60 is the posted Cards list
# with Luke (V).
HAYWARD_LS = [
    (1, "Rebel Strike Team / Garrison Destroyed", "OBJECTIVE"),
    (1, "Endor", "LOCATION"),
    (1, "Endor: Rebel Landing Site (Forest)", "LOCATION"),
    (1, "Endor: Back Door", "LOCATION"),
    (1, "Endor: Bunker", "LOCATION"),
    (1, "Endor: Chief Chirpa's Hut", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Chewbacca Of Kashyyyk", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Daughter Of Skywalker", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (1, "General Calrissian", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (1, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Luke Skywalker (V)", "CHARACTER"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (1, "Mirax Terrik", "CHARACTER"),
    (1, "Nien Nunb", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Wuta", "CHARACTER"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (1, "All Wings Report In & Darklighter Spin", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "It Could Be Worse", "INTERRUPT"),
    (1, "It's A Hit!", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Rebel Artillery", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (3, "Throw Me Another Charge", "INTERRUPT"),
    (1, "Weapon Levitation", "INTERRUPT"),
    (1, "Battle Plan", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "The Shield Is Down!", "EFFECT"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Gold Squadron 1", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Pulsar Skate", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (3, "Explosive Charge", "WEAPON"),
    (1, "X-wing Laser Cannon", "WEAPON"),
    (1, "I'll Take The Leader", "ADMIRALS_ORDER"),
    (1, "Deactivate The Shield Generator", "EPIC_EVENT"),
]

# 23279 Lewis "Duke Devil" Blake YEEeeah I've got the Hoth (Big) Blues Baby
# YAML Dark / body Dark YMSYL walkers. General dest TITLE (no named
# event/finish). Qty 60 (6 start + 8 loc + 14 char + 7 veh + 4 ship +
# 2 ao + 6 eff + 13 int = 60). FIMA inside Starting counts. Named 8
# Defensive Shields dest outside 60. Unnamed "(2 more, thoughthey
# usually won't matter)" dest 60 only. Starting Interrupt Prepared
# Defenses. Starting Effect Fear Is My Ally. Starting Card You May
# Start Your Landing. Posted YMSYL dested You May Start Your Landing.
# Posted Ice Plains dested Hoth: Ice Plains (5th Marker). Posted Prep
# Defenses dested Prepared Defenses. Posted Prepare for a SA dested
# Prepare For A Surface Attack. Posted IAO & Secret Plans dested
# Imperial Arrest Order & Secret Plans. Posted Fear is MA dested Fear
# Is My Ally. Posted H mountains dested Hoth: Mountains (6th Marker).
# Posted H N Ridge dested Hoth: North Ridge (4th Marker). Posted H D
# Perimeter dested Hoth: Defensive Perimeter (3rd Marker). Posted H
# Echo DB dested Hoth: Echo Docking Bay. Posted D II DB dested Death
# Star II: Docking Bay. Posted Executor DB dested Executor: Docking
# Bay. Posted Ad Piet dested Admiral Piett. Posted Grnd Ad Thrawn
# dested Grand Admiral Thrawn. Posted Commander Merrijk dested
# Commander Merrejk. Posted Grnd Moff Tarkin dested Grand Moff Tarkin.
# Posted 4-LOM w/ gun dested 4-LOM With Concussion Rifle. Posted Dr. E
# and PB dested Dr. Evazan & Ponda Baba. Posted DV with saber dested
# Darth Vader With Lightsaber. Posted DM with saber dested Darth Maul
# With Lightsaber. Posted Imperial walker dested Imperial Walker.
# Posted Chimera dested Chimaera. Posted Zuckuss in MH dested Zuckuss
# In Mist Hunter. Posted Enter the Beuracrat dested Enter The
# Bureaucrat. Posted Rebel Base occ dested Rebel Base Occupation.
# Posted Imp decree dested Imperial Decree. Posted Master Move dested
# Masterful Move. Posted Twilek Advisor dested Twi'lek Advisor. Posted
# You've Never won a race? dested You've Never Won A Race?. Posted A
# Useless Guesture dested A Useless Gesture. Skip GEMP (original-VS
# pool by legal day; no (V) cards). Format Premiere - Original VS1
# (11 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Handle
# Duke Devil cited; no Duke Devil page. Do not dest onto Admiral
# Piett. Do not dest onto Grand Admiral Thrawn. Do not dest onto
# General Veers. Do not dest onto Blizzard 4 as player. Do not dest
# onto Darth Vader. Do not dest onto Darth Maul. Do not dest onto Hoth
# as player. Do not dest onto You May Start Your Landing as player.
# Do not dest onto Duke Devil as a new person. Do not dest onto
# inventory author_guess Dark.
BLAKE_DS = [
    (1, "You May Start Your Landing", "EPIC_EVENT"),
    (1, "Hoth: Ice Plains (5th Marker)", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Prepare For A Surface Attack", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Hoth", "LOCATION"),
    (1, "Hoth: Mountains (6th Marker)", "LOCATION"),
    (1, "Hoth: North Ridge (4th Marker)", "LOCATION"),
    (1, "Hoth: Defensive Perimeter (3rd Marker)", "LOCATION"),
    (1, "Hoth: Echo Docking Bay", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Naboo", "LOCATION"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "General Veers", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Commander Igar", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "Mosep", "CHARACTER"),
    (1, "Prince Xizor", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (3, "Imperial Walker", "VEHICLE"),
    (1, "Tempest 1", "VEHICLE"),
    (1, "Blizzard 2", "VEHICLE"),
    (2, "Blizzard 4", "VEHICLE"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Avenger", "STARSHIP"),
    (1, "Devastator", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (2, "Battle Deployment", "ADMIRALS_ORDER"),
    (1, "Enter The Bureaucrat", "EFFECT"),
    (2, "Presence Of The Force", "EFFECT"),
    (1, "Rebel Base Occupation", "EFFECT"),
    (1, "Imperial Decree", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (3, "Trample", "INTERRUPT"),
    (3, "Walker Garrison", "INTERRUPT"),
    (2, "Ghhhk", "INTERRUPT"),
    (2, "Masterful Move", "INTERRUPT"),
    (2, "Imperial Command", "INTERRUPT"),
    (1, "Twi'lek Advisor", "INTERRUPT"),
]
BLAKE_SHIELDS = [
    (1, "Fanfare", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
    (1, "Resistance", "DEFENSIVE_SHIELD"),
    (1, "You Cannot Hide Forever", "DEFENSIVE_SHIELD"),
    (1, "A Useless Gesture", "DEFENSIVE_SHIELD"),
]

# 23249 Jacob "Armaedes" Taylor Jacob's BHBM aka Blame Canada
# YAML Dark / body Dark BHBM sevens. General dest TITLE (no named
# event/finish). Qty 60 (6 loc + 15 char + 2 ship + 19 eff + 15 int +
# 2 weap + 1 obj = 60). FIMA inside Effects counts. Named 10 Defensive
# Shields dest outside 60. Starting Interrupt Prepared Defenses.
# Starting Effect Fear Is My Ally. Starting Card printed dual BHBM.
# Posted After Her dested After Her!. Posted Drop dested Drop!. Posted
# Rise My Friend dested Rise, My Friend. Posted This Is Some Rescue
# dested This Is Some Rescue!. Posted Cloud City East Platform dested
# Cloud City: East Platform (Docking Bay). Posted Death Star II Throne
# Room dested Death Star II: Throne Room. Posted Endor Landing Platform
# dested Endor: Landing Platform (Docking Bay). Posted Blockade Flagship
# Bridge dested Blockade Flagship: Bridge. Skip GEMP (original-VS pool
# by legal day; no (V) cards). Format Premiere - Original VS1 (9 May
# 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Handle Armaedes
# cited; no Armaedes page. Do not dest onto Bring Him Before Me as
# player. Do not dest onto Darth Maul. Do not dest onto Darth Vader.
# Do not dest onto Emperor Palpatine as player. Do not dest onto Aurra
# Sing as player. Do not dest onto Blizzard 4 as player. Do not dest
# onto Doug Taylor. Do not dest onto Taylor Hayward. Do not dest onto
# Geoff Bowman BHBM dest as player. Do not dest onto Armaedes as a new
# person. Do not dest onto inventory author_guess.
JACOB_BHBM = [
    (1, "Bring Him Before Me / Take Your Father's Place", "OBJECTIVE"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (1, "Carida", "LOCATION"),
    (1, "Cloud City: East Platform (Docking Bay)", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Death Star II: Throne Room", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Aurra Sing", "CHARACTER"),
    (5, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (2, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (2, "Zuckuss In Mist Hunter", "STARSHIP"),
    (2, "After Her!", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (2, "Drop!", "EFFECT"),
    (1, "Emperor's Power", "EFFECT"),
    (2, "Enter The Bureaucrat", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Insignificant Rebellion", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Mobilization Points", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "The Phantom Menace", "EFFECT"),
    (1, "Visage Of The Emperor", "EFFECT"),
    (1, "We're The Bait", "EFFECT"),
    (1, "Your Destiny", "EFFECT"),
    (1, "Hunting Party", "INTERRUPT"),
    (1, "I Have You Now", "INTERRUPT"),
    (1, "Imperial Artillery", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (2, "Rise, My Friend", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (2, "This Is Some Rescue!", "INTERRUPT"),
    (3, "We Must Accelerate Our Plans", "INTERRUPT"),
    (2, "You Are Beaten", "INTERRUPT"),
    (2, "Aurra Sing's Blaster Rifle", "WEAPON"),
]
JACOB_BHBM_SHIELDS = [
    (1, "A Useless Gesture", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Do They Have A Code Clearance?", "DEFENSIVE_SHIELD"),
    (1, "Fanfare", "DEFENSIVE_SHIELD"),
    (1, "Oppressive Enforcement", "DEFENSIVE_SHIELD"),
    (1, "Resistance", "DEFENSIVE_SHIELD"),
    (1, "There Is No Try", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
]

# 23127 Dunya "Hardpack" Ertan power of Rebel strike team
# YAML Light / body Light RST (match). General dest TITLE. Qty 59 as
# published (objective omitted from the list; author also forgot Endor
# system and An Unusual Amount Of Fear — do not invent). Unnamed
# Defensive shields (10) dest 60 only. Author Dunya "Hardpack" Ertan.
# Handle Hardpack cited; no Hardpack page. [[Dunya Ertan]] missing —
# stub. Inventory author_guess is the description fragment — trust
# YAML author. Do not dest onto Rebel Strike Team as player. Do not
# dest onto Hardpack as a new person. Do not dest onto inventory
# author_guess Beat down fragment. Do not dest onto Taylor Hayward
# RST dest as player. Do not dest onto Mike (Quione) RST dest as
# player. Do not dest onto Luke Skywalker / Qui-Gon Jinn / Obi-Wan
# Kenobi / Jar Jar Binks / Endor / Rep Been / Thomas Papp as players.
# Posted Endor rebel landing site dested Endor: Rebel Landing Site
# (Forest). Posted Heading for the medical frigate dested Heading For
# The Medical Frigate. Posted Squadron assignments dested Squadron
# Assignments. Posted Strike planing dested Strike Planning. Posted
# Shield is down dested The Shield Is Down!. Posted Endor back door
# dested Endor: Back Door. Posted Endor hidden forest trail dested
# Endor: Hidden Forest Trail. Posted Endor dense forest dested Endor:
# Dense Forest. Posted Luke Jedi knight dested Luke Skywalker, Jedi
# Knight. Posted General solo dested General Solo. Posted Jin with
# stick dested Qui-Gon Jinn With Lightsaber. Posted Obi with stick
# dested Obi-Wan With Lightsaber. Posted Jar jar dested Jar Jar Binks.
# Posted Sergeant junkin dested Sergeant Junkin. Posted Lieu. Blount
# dested Lieutenant Blount. Posted Cor. Midge dested Corporal Midge.
# Posted Captain yutani dested Captain Yutani. Posted Daughter of sky
# walker dested Daughter Of Skywalker. Posted Chewbacc of kashyyyk
# dested Chewbacca Of Kashyyyk. Posted Chewie with blaster dested
# Chewie With Blaster Rifle. Posted Rep ben dested Rep Been. Posted
# Wedge antilles red squadron leader dested Wedge Antilles, Red
# Squadron Leader. Posted General calrissian dested General
# Calrissian. Posted Corporal beezer dested Corporal Beezer. Posted
# General crix madine dested General Crix Madine. Posted Leit greeve
# dested Lieutenant Greeve. Posted Sergeant bruckman dested Sergeant
# Bruckman. Posted Major panno dested Major Panno. Posted Wuto dested
# Wuta. Posted Owen and brue combo dested Owen Lars & Beru Lars.
# Posted Major hassh dested Major Haash'n. Posted Cor. Janse dested
# Corporal Janse. Posted Lightsaber profiency dested Lightsaber
# Proficiency. Posted Out of commison dested Out Of Commission (not
# the combo). Posted Jedi presence dested Jedi Presence. Posted Gift
# of a mentor dested Gift Of The Mentor. Posted Nabrun leids dested
# Nabrun Leids. Posted A few maneuvers dested A Few Maneuvers. Posted
# The bith shuffle combo dested The Bith Shuffle & Desperate Reach.
# Posted Gold one (Lando ships) dested Gold Squadron 1. Posted Home
# one dested Home One. Posted Artoo in red 5 dested Artoo-Detoo In
# Red 5. Posted Intruder missile dested Intruder Missile. Starting
# Interrupt Heading For The Medical Frigate. Starting Effect omitted
# (author forgot AUOF). Starting Card printed dual RST (omitted from
# the list; identified in strategy). Skip GEMP. Format Premiere -
# Original VS1 (4 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun
# 2002). No original (V) cards posted. YAML `!` stripped. Owen Lars &
# Beru Lars wrap File OK (wiki card page missing — do not mint).
ERTAN_LS = [
    (1, "Endor: Rebel Landing Site (Forest)", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "The Shield Is Down!", "EFFECT"),
    (1, "Endor: Back Door", "LOCATION"),
    (1, "Endor: Hidden Forest Trail", "LOCATION"),
    (1, "Endor: Dense Forest", "LOCATION"),
    (2, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (2, "Jar Jar Binks", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Sergeant Junkin", "CHARACTER"),
    (1, "Lieutenant Blount", "CHARACTER"),
    (1, "Corporal Midge", "CHARACTER"),
    (1, "Captain Yutani", "CHARACTER"),
    (1, "Daughter Of Skywalker", "CHARACTER"),
    (1, "Chewbacca Of Kashyyyk", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Colonel Cracken", "CHARACTER"),
    (1, "Chewie With Blaster Rifle", "CHARACTER"),
    (1, "Rep Been", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "General Calrissian", "CHARACTER"),
    (1, "Corporal Beezer", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (1, "Lieutenant Greeve", "CHARACTER"),
    (1, "Sergeant Bruckman", "CHARACTER"),
    (1, "Major Panno", "CHARACTER"),
    (1, "Wuta", "CHARACTER"),
    (1, "Owen Lars & Beru Lars", "CHARACTER"),
    (1, "Major Haash'n", "CHARACTER"),
    (1, "Corporal Janse", "CHARACTER"),
    (1, "Traffic Control", "EFFECT"),
    (1, "Lightsaber Proficiency", "EFFECT"),
    (2, "Out Of Commission", "INTERRUPT"),
    (3, "Jedi Presence", "INTERRUPT"),
    (1, "Gift Of The Mentor", "INTERRUPT"),
    (1, "Nabrun Leids", "INTERRUPT"),
    (3, "A Few Maneuvers", "INTERRUPT"),
    (1, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Gold Squadron 1", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (2, "Home One", "STARSHIP"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (2, "Intruder Missile", "WEAPON"),
]

# 23121 Taylor "JediMaster10" Hayward Agents In The Court
# YAML Light / body Light Agents In The Court (match). General dest TITLE.
# Qty 60. AUOF inside Starting counts. Unnamed 10 shields dest 60 only.
# Starting Interrupt Heading For The Medical Frigate. Starting Effect
# An Unusual Amount Of Fear. Starting Card printed dual Agents In The
# Court. dump-not-stub Taylor Hayward 43342 (JediMaster10 already cited).
# YAML author Taylor "JediMaster10" Hayward. Inventory author_guess is
# the description fragment. Posted Uh-Oh dested Uh-oh!. Posted Nar
# shadda Wind Chimes & Out Of Somewhere dested Nar Shaddaa Wind Chimes
# & Out Of Somewhere. Posted Tatooine Mos Espa Docking Bay dested
# Tatooine: Mos Espa Docking Bay. Posted Wookie dested Wookiee.
# Posted Chewbacca (Rep) dested Premiere Chewbacca. Skip GEMP. Do not
# dest onto Agents In The Court as player (wiki card page missing —
# dest CardLink, do not mint). Do not dest onto JediMaster10 as a new
# person. Do not dest onto Dunya Ertan. Do not dest onto Rebel Strike
# Team as player. Do not dest onto inventory author_guess.
HAYWARD_AITC_LS = [
    (1, "Agents In The Court / No Love For The Empire", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Tatooine: Hutt Trade Route (Desert)", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Yarna D'al' Gargan", "CHARACTER"),
    (1, "Chewbacca", "CHARACTER"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Insurrection & Aim High", "INTERRUPT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "Uh-oh!", "INTERRUPT"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Tatooine", "LOCATION"),
    (1, "Tatooine: Cantina", "LOCATION"),
    (1, "Tatooine: Jundland Wastes", "LOCATION"),
    (1, "Tatooine: Mos Espa Docking Bay", "LOCATION"),
    (1, "Chewbacca Of Kashyyyk", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (1, "Lando With Vibro-Ax", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (5, "Palace Raider", "CHARACTER"),
    (1, "Tessek", "CHARACTER"),
    (6, "Wookiee", "CHARACTER"),
    (1, "Bargaining Table", "EFFECT"),
    (1, "Bo Shuda", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Secure Route", "EFFECT"),
    (1, "Tatooine Celebration", "EFFECT"),
    (1, "Liberty", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (1, "Red Leader In Red 1", "STARSHIP"),
    (2, "Red Squadron X-wing", "STARSHIP"),
    (1, "Don't Underestimate Our Chances", "INTERRUPT"),
    (1, "Nar Shaddaa Wind Chimes", "INTERRUPT"),
    (1, "Nar Shaddaa Wind Chimes & Out Of Somewhere", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Rebel Artillery", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (1, "Strangle", "INTERRUPT"),
    (2, "We Wish To Board At Once", "INTERRUPT"),
    (2, "You Will Take Me To Jabba Now", "INTERRUPT"),
    (4, "Patrol Craft", "VEHICLE"),
    (1, "Chewbacca's Bowcaster", "WEAPON"),
    (1, "X-Wing Laser Cannon", "WEAPON"),
]

# 23087 Jason "Mr. Black" Herrin Voice of the council solid
# YAML Light / body Light We'll Handle This (match). General dest TITLE
# (Tournament play 12-1 in strategy; unnamed events — do not mint a hub).
# Qty 60. AUOF inside Starting counts. Unnamed shields dest 60 only (none
# listed). Starting Interrupt Heading For The Medical Frigate. Starting
# Effect An Unusual Amount Of Fear. Starting Card printed dual We'll
# Handle This (wiki We'll Handle This REDIR current-virtual; dest printed
# pageid 7824 File Ref3-L-wellhandlethis.gif). Posted Saitor Kal Fass
# dested Sai'torr Kal Fas (V) (VS1). Posted We'll Handle This dested
# printed dual. Posted Theed Generator dested Naboo: Theed Palace
# Generator. Posted Theed Generator Core dested Naboo: Theed Palace
# Generator Core. Posted Jedi Council Chamber dested Coruscant: Jedi
# Council Chamber. Posted Coruscant Docking Bay dested Coruscant:
# Docking Bay. Posted Theed Docking Bay dested Naboo: Theed Palace
# Docking Bay. Posted Qui Gon Jinn, Jedi Master dested Qui-Gon Jinn,
# Jedi Master. Posted Obi Wan Kenobi, Jedi Knight dested Obi-Wan
# Kenobi, Jedi Knight. Posted Yoda Senior Council Member dested Yoda,
# Senior Council Member. Posted Depa Bilaba dested Depa Billaba.
# Posted Padme' Naberrie dested Padme Naberrie. Posted Panaka,
# Protector Of The Queen dested Panaka, Protector Of The Queen.
# Posted Threepio With His Parts Showing dested Threepio With His
# Parts Showing. Posted Chewie Enraged dested Chewie, Enraged.
# Posted Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel.
# Posted Luke Skywalker Jedi Knight dested Luke Skywalker, Jedi Knight.
# Posted Qui Gon's Lightsaber R3 dested Qui-Gon's Lightsaber.
# Posted Obi Wan's Lightsaber R3 dested Obi-Wan's Lightsaber.
# Posted Amidala's Blaster dested Amidala's Blaster. Posted Panaka's
# Blaster dested Panaka's Blaster. Posted Artoo Deetoo In Red 5 dested
# Artoo-Detoo In Red 5. Posted Obi Wan's Apparition dested Obi-Wan's
# Apparition. Posted Blast The Door Kid dested Blast The Door, Kid!.
# Posted Run Luke Run dested Run Luke, Run!. Posted Ajedi's
# Concentration dested A Jedi's Concentration. Posted Inner Strength
# dested Reflections III Epic Event. Update 4 says remove Restraining
# Bolt for Scramble — dest Restraining Bolt as published. Skip GEMP.
# Handle Mr. Black cited; no Mr. Black page. YAML author Jason
# "Mr. Black" Herrin. Inventory author_guess was the description
# fragment. [[Jason Herrin]] missing — stub. Do not dest onto We'll
# Handle This as player. Do not dest onto Lightsaber Combat as player.
# Do not dest onto Yoda / Qui-Gon Jinn / Obi-Wan Kenobi / Luke
# Skywalker / Mace Windu / Padme Naberrie / Darth Maul / Sai'torr Kal
# Fas as players. Do not dest onto Mr. Black as a new person. Do not
# dest onto Taylor Hayward Agents In The Court as player. Do not dest
# onto inventory author_guess.
HERRIN_LS = [
    (1, "We'll Handle This / Duel Of The Fates", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Inner Strength", "EPIC_EVENT"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Insurrection & Aim High", "INTERRUPT"),
    (1, "Colo Claw Fish", "CREATURE"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Coruscant: Docking Bay", "LOCATION"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
    (2, "Qui-Gon Jinn, Jedi Master", "CHARACTER"),
    (2, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (1, "Yoda, Senior Council Member", "CHARACTER"),
    (1, "Mace Windu", "CHARACTER"),
    (1, "Plo Koon", "CHARACTER"),
    (1, "Depa Billaba", "CHARACTER"),
    (2, "Padme Naberrie", "CHARACTER"),
    (2, "Panaka, Protector Of The Queen", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Boushh", "CHARACTER"),
    (1, "TK-422", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (2, "Bionic Hand", "WEAPON"),
    (1, "Qui-Gon's Lightsaber", "WEAPON"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Leia's Blaster Rifle", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Restraining Bolt", "WEAPON"),
    (1, "Amidala's Blaster", "WEAPON"),
    (1, "Panaka's Blaster", "WEAPON"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Lightsaber Proficiency", "EFFECT"),
    (1, "Obi-Wan's Apparition", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (2, "Projection Of A Skywalker", "EFFECT"),
    (1, "Armament Dismantled", "EFFECT"),
    (2, "Speak With The Jedi Council", "INTERRUPT"),
    (1, "Gift Of The Mentor", "INTERRUPT"),
    (1, "Darth Maul's Demise", "INTERRUPT"),
    (1, "Fall Of A Jedi", "INTERRUPT"),
    (1, "We Don't Have Time For This", "INTERRUPT"),
    (1, "Free Ride & Endor Celebration", "INTERRUPT"),
    (2, "Blast The Door, Kid!", "INTERRUPT"),
    (1, "Run Luke, Run!", "INTERRUPT"),
    (2, "Strike Blocked", "INTERRUPT"),
    (2, "A Jedi's Concentration", "INTERRUPT"),
]

# 23051 Dunya "Hardpack" Ertan we dont need a sticking hypergenerator.
# YAML Light / body Light The Hyperdrive Generator's Gone + Watto Profit
# sites. General dest TITLE (see u in vegas people — do not mint Vegas
# DPC hub). Qty 60. YAML ! stripped. Inventory author_guess
# is the Light tag — trust YAML author. dump-not-stub [[Dunya Ertan]]
# pageid 43557. Handle Hardpack already cited; no Hardpack page.
# Starting unnamed (effect) u can choose + defensive shields — dest 60
# only, do not invent AUOF. Starting Effect Credits Will Do Fine.
# Starting Interrupt omitted. Starting Card printed dual The Hyperdrive
# Generator's Gone / We'll Need A New One (short identity missing; dest
# CardLink dual pageid 6983 File Cor-L-thehyperdrivegeneratorsgone.gif).
# Posted hypergenerator is gone dested The Hyperdrive Generator's Gone.
# Posted boonta eve podrace dested Boonta Eve Podrace. Posted credits
# will do fine dested Credits Will Do Fine. Posted anakin podracer
# dested Anakin's Podracer. Posted podracer bay dested Tatooine:
# Podracer Bay. Posted city outshirts dested Tatooine: City Outskirts.
# Posted wattos junkyard dested Tatooine: Watto's Junkyard. Posted
# lieutnant chamberlynn dested Lieutenant Chamberlyn. Posted qui-hon
# jinn dested Qui-Gon Jinn. Posted obi one the jedi dested Obi-Wan
# Kenobi, Jedi Knight. Posted ric olie dested Ric Olie. Posted liana
# merian dested Liana Merian. Posted rio bibble dested Sio Bibble.
# Posted supreme chncellor valorum dested Supreme Chancellor Valorum.
# Posted yarun dested Yarua. Posted hurox ryyder dested Horox Ryyder.
# Posted graxol kelvyyn dested Graxol Kelvyyn. Posted debnoli dested
# Deneb Both. Posted lando with axe dested Lando With Vibro-Ax. Posted
# padme dested Padme Naberrie. Posted lieut. wlliams dested Lieutenant
# Williams. Posted jerus jannick dested Jerus Jannick. Posted freon
# orevan dested Theron Nett. Posted qui gon with stick dested Qui-Gon
# Jinn With Lightsaber. Posted jar jar dested Jar Jar Binks. Posted
# rep ben dested Rep Been. Posted tat db bay 94 dested Tatooine:
# Docking Bay 94. Posted stun blaster dested Stun Blaster. Posted
# amidale blaster dested Amidala's Blaster. Posted rebel artilery
# dested Rebel Artillery. Posted out of commison combo dested Out Of
# Commission & Transmission Terminated. Posted glaccing blow dested
# Glancing Blow. Posted alter combo dested Alter & Friendly Fire.
# Posted i've decided to go back dested I've Decided To Go Back.
# Posted yodas stew combo dested Houjix & Out Of Nowhere. Posted step
# backward dested A Step Backward. Posted pod racer prep dested
# Podrace Prep. Posted i have a really bad feeling about this dested
# I Have A Really Bad Feeling About This. Posted free ride combo dested
# Free Ride & Endor Celebration. Posted i hope she is allright dested
# I Hope She's All Right. Skip GEMP (printed Theed Palace). Format
# Premiere - Original VS1 (29 April 2002; VS1 legal 9 Mar 2002; VS2
# legal 1 Jun 2002). Do not dest onto The Hyperdrive Generator's Gone
# as player. Do not dest onto You Can Either Profit By This as player.
# Do not dest onto Hardpack as a new person. Do not dest onto Watto /
# Yoda / Qui-Gon Jinn / Obi-Wan Kenobi / Jar Jar Binks / Padme Naberrie
# / Sio Bibble / Lieutenant Chamberlyn / Ric Olie as players. Do not
# dest onto Dunya Ertan power of Rebel strike team as player. Do not
# dest onto inventory author_guess Light tag.
ERTAN_HYPER_LS = [
    (1, "The Hyperdrive Generator's Gone / We'll Need A New One", "OBJECTIVE"),
    (1, "Boonta Eve Podrace", "EPIC_EVENT"),
    (1, "Credits Will Do Fine", "EFFECT"),
    (1, "Anakin's Podracer", "PODRACER"),
    (1, "Tatooine: Podracer Bay", "LOCATION"),
    (1, "Tatooine: City Outskirts", "LOCATION"),
    (1, "Tatooine: Watto's Junkyard", "LOCATION"),
    (1, "Lieutenant Chamberlyn", "CHARACTER"),
    (1, "Talon Karrde", "CHARACTER"),
    (2, "Qui-Gon Jinn", "CHARACTER"),
    (2, "Obi-Wan Kenobi, Jedi Knight", "CHARACTER"),
    (1, "Ric Olie", "CHARACTER"),
    (1, "Liana Merian", "CHARACTER"),
    (1, "Sio Bibble", "CHARACTER"),
    (1, "Supreme Chancellor Valorum", "CHARACTER"),
    (1, "Tendau Bendon", "CHARACTER"),
    (2, "Yarua", "CHARACTER"),
    (1, "Horox Ryyder", "CHARACTER"),
    (1, "Graxol Kelvyyn", "CHARACTER"),
    (1, "Deneb Both", "CHARACTER"),
    (1, "Lando With Vibro-Ax", "CHARACTER"),
    (1, "Padme Naberrie", "CHARACTER"),
    (1, "Lieutenant Williams", "CHARACTER"),
    (1, "Corporal Rushing", "CHARACTER"),
    (1, "Jerus Jannick", "CHARACTER"),
    (1, "Theron Nett", "CHARACTER"),
    (1, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Jar Jar Binks", "CHARACTER"),
    (1, "Rep Been", "CHARACTER"),
    (1, "Tatooine: Docking Bay 94", "LOCATION"),
    (2, "Stun Blaster", "WEAPON"),
    (1, "Amidala's Blaster", "WEAPON"),
    (3, "Rebel Artillery", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Glancing Blow", "INTERRUPT"),
    (1, "Alter & Friendly Fire", "INTERRUPT"),
    (1, "Nabrun Leids", "INTERRUPT"),
    (2, "I've Decided To Go Back", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (5, "A Step Backward", "INTERRUPT"),
    (1, "Podrace Prep", "INTERRUPT"),
    (1, "Inconsequential Barriers", "INTERRUPT"),
    (1, "I Have A Really Bad Feeling About This", "INTERRUPT"),
    (2, "Free Ride & Endor Celebration", "INTERRUPT"),
    (1, "I Hope She's All Right", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
]

# 23036 Dennis "Denethor" Jeffris Rebel Strike Team - Da Non-Bomb.
# YAML Light / body Light Rebel Strike Team (match). General dest TITLE.
# Qty 60. Unnamed "play any defensive shields you want" dest 60 only.
# Starting Interrupt Heading For The Medical Frigate. Starting Effect
# An Unusual Amount Of Fear. Starting Card printed dual Rebel Strike
# Team / Garrison Destroyed. Author Dennis "Denethor" Jeffris. Handle
# Denethor cited; no Denethor page. [[Dennis Jeffris]] missing — stub.
# Inventory author_guess is the description fragment — trust YAML
# author. Posted The Shiled Is Down dested The Shield Is Down!. Posted
# I Hope She's Alright dested I Hope She's All Right. Posted Threepio
# WHPS dested Threepio With His Parts Showing. Posted Lando, Scoundrel
# dested Lando Calrissian, Scoundrel. Posted Chewbacca of Kashyyyk
# dested Chewbacca Of Kashyyyk. Posted Luke, Rebel Scout dested Luke
# Skywalker, Rebel Scout. Posted All Wings Report In combo dested All
# Wings Report In & Darklighter Spin. Posted Insurrection under Effects
# dested INTERRUPT Insurrection. Skip GEMP (printed Endor). Format
# Premiere - Original VS1 (28 April 2002; VS1 legal 9 Mar 2002; VS2
# legal 1 Jun 2002). Tournament 1st unnamed — general dest TITLE; do
# not mint a tournament hub. Do not dest onto Rebel Strike Team as
# player (current-virtual redirect). Do not dest onto Dunya Ertan
# power of Rebel strike team as player. Do not dest onto Mike (Quione)
# Rebel Strike Team- Stay the hell of endor as player. Do not dest
# onto Denethor as a new person. Do not dest onto Luke Skywalker /
# Leia Organa / Chewbacca / Han Solo / Home One / Wuta / General Crix
# Madine as players. Do not dest onto inventory author_guess
# description fragment.
JEFFRIS_RST_LS = [
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Rebel Strike Team / Garrison Destroyed", "OBJECTIVE"),
    (1, "Endor", "LOCATION"),
    (1, "Endor: Rebel Landing Site (Forest)", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "The Shield Is Down!", "EFFECT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (2, "Close Air Support", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "I Hope She's All Right", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Insurrection", "INTERRUPT"),
    (1, "Endor: Back Door", "LOCATION"),
    (1, "Endor: Dense Forest", "LOCATION"),
    (1, "Endor: Hidden Forest Trail", "LOCATION"),
    (1, "Wuta", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (1, "General Calrissian", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Corporal Beezer", "CHARACTER"),
    (1, "Lieutenant Page", "CHARACTER"),
    (1, "Chewbacca Of Kashyyyk", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Sergeant Junkin", "CHARACTER"),
    (1, "Lieutenant Blount", "CHARACTER"),
    (1, "Corporal Kensaric", "CHARACTER"),
    (1, "Corporal Midge", "CHARACTER"),
    (1, "Leia, Rebel Princess", "CHARACTER"),
    (1, "Daughter Of Skywalker", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Luke Skywalker, Rebel Scout", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Corporal Janse", "CHARACTER"),
    (1, "Corporal Delevar", "CHARACTER"),
    (1, "Colonel Cracken", "CHARACTER"),
    (1, "Under Attack", "INTERRUPT"),
    (4, "Insertion Planning", "INTERRUPT"),
    (1, "We Wish To Board At Once", "INTERRUPT"),
    (3, "On The Edge", "INTERRUPT"),
    (1, "A Jedi's Resilience", "INTERRUPT"),
    (2, "The Signal", "INTERRUPT"),
    (1, "All Wings Report In & Darklighter Spin", "INTERRUPT"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Liberty", "STARSHIP"),
    (1, "Home One", "STARSHIP"),
    (1, "Tala 1", "STARSHIP"),
    (1, "Tala 2", "STARSHIP"),
    (2, "Capital Support", "ADMIRALS_ORDER"),
]

# 23033 Taylor "JediMaster10" Hayward A Hidden Base Deck.
# YAML Light / body Light Hidden Base (match). General dest TITLE.
# Qty 59 unique as published: Locations (7) includes Hidden Base
# Indicator (Start) which is the Objective listed again as
# Hidden Base/Systems Will Slip Through Your Fingers — dest Hidden
# Base dual once. Unnamed Pick Any 10 shields dest 59 only. Starting
# Interrupt Heading For The Medical Frigate. Starting Effect An
# Unusual Amount Of Fear. Starting Card printed dual Hidden Base /
# Systems Will Slip Through Your Fingers. Author Taylor
# "JediMaster10" Hayward. Handle JediMaster10 already cited; no
# JediMaster10 page. [[Taylor Hayward]] dump-not-stub pageid 43342.
# Inventory author_guess is the description fragment — trust YAML
# author. Posted Hidden Base Indicator dested Hidden Base dual.
# Posted Kiffix dested Kiffex. Posted Niem Numb dested Nien Nunb.
# Posted Luke Skywalker (V) dested Luke Skywalker (V) (VS1) File
# VS1O-05-Luke Skywalker.png. Posted Stay Sharp dested Stay Sharp!.
# Posted X-Wing Laser Cannon dested X-wing Laser Cannon. Skip GEMP
# (original-VS Luke + qty 59). Format Premiere - Original VS1 (28
# April 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Do not dest
# onto Hidden Base as player (current-virtual redirect). Do not dest
# onto JediMaster10 as a new person. Do not dest onto Luke Skywalker
# as player. Do not dest onto Dash Rendar / Tycho Celchu / Wedge
# Antilles / Nien Nunb / Ten Numb / Outrider as players. Do not dest
# onto Taylor Hayward I like blowin sht up. Do not dest onto Taylor
# Hayward Agents In The Court as player. Do not dest onto Dennis
# Jeffris RST dest. Do not dest onto Matt Wehner Good PunJab Hunting.
# Do not dest onto Wedge231 Hidden Base - needs help!. Do not dest
# onto inventory author_guess description fragment.
HAYWARD_HB_LS = [
    (1, "Hidden Base / Systems Will Slip Through Your Fingers", "OBJECTIVE"),
    (1, "Rendezvous Point", "LOCATION"),
    (1, "Aquaris", "LOCATION"),
    (1, "Endor", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (1, "Kiffex", "LOCATION"),
    (1, "Kirdo III", "LOCATION"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Derek 'Hobbie' Klivian", "CHARACTER"),
    (1, "General Calrissian", "CHARACTER"),
    (1, "Luke Skywalker (V)", "CHARACTER"),
    (1, "Nien Nunb", "CHARACTER"),
    (1, "Ten Numb", "CHARACTER"),
    (1, "Tycho Celchu", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Blue Squadron 5", "STARSHIP"),
    (1, "Gold Squadron 1", "STARSHIP"),
    (1, "Green Squadron 3", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Red Squadron 4", "STARSHIP"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "A Few Maneuvers", "INTERRUPT"),
    (2, "All Wings Report In & Darklighter Spin", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (1, "It Could Be Worse", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (1, "Power Pivot", "INTERRUPT"),
    (1, "Rapid Fire", "INTERRUPT"),
    (1, "Rebel Artillery", "INTERRUPT"),
    (1, "Shocking Information & Grimtaash", "INTERRUPT"),
    (1, "Stay Sharp!", "INTERRUPT"),
    (1, "Steady Aim", "INTERRUPT"),
    (2, "We Wish To Board At Once", "INTERRUPT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "Your Insight Serves You Well & Staging Areas", "EFFECT"),
    (2, "Goo Nee Tay", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "Legendary Starfighter", "EFFECT"),
    (1, "Special Modifications", "EFFECT"),
    (1, "Superficial Damage", "EFFECT"),
    (1, "Traffic Control", "EFFECT"),
    (3, "Intruder Missile", "WEAPON"),
    (2, "X-wing Laser Cannon", "WEAPON"),
    (1, "Concentrate All Fire", "ADMIRALS_ORDER"),
    (2, "I'll Take The Leader", "ADMIRALS_ORDER"),
]

# 23021 chris "Putz" burnett My senate.
# YAML Dark / body Dark Senate (match). General dest TITLE (7-3 unnamed
# tournie; do not mint a tournament hub). Qty 60. Unnamed D-shields dest
# 60 only. Starting Interrupt Prepared Defenses. Starting Effect Fear Is
# My Ally. Starting Card printed dual My Lord, Is That Legal? / I Will
# Make It Legal pageid 7087 (short identity MISSING — do not mint). YAML
# author chris "Putz" burnett → dest Chris Burnett. Handle Putz cited;
# no Putz page. Inventory author_guess is the Dark tag — trust YAML
# author. Do not dest onto David Burnett pageid 41995. Do not dest onto
# lastname Burnett. Do not dest onto MLITL dual as player. Do not dest
# onto Emperor Palpatine / Lord Maul / Darth Maul / Darth Vader / Guri
# / P-59 as players. Do not dest onto Peter Jurcovic Senate dest. Do
# not dest onto Brian Hunter Vegas DPC Senate dest. Posted MLITL/IWMIL
# dested printed dual. Posted Tatooine Desert landing site dested
# Tatooine: Desert Landing Site. Posted Corusant Glactic senate dested
# Coruscant: Galactic Senate. Posted Naboo Battle plans dested Naboo:
# Battle Plains. Posted this is outrageous dested This Is Outrageous!.
# Posted vote now dested Vote Now!. Posted Oh Switch off dested Oh,
# Switch Off. Posted Do They Have A Code Clearance dested Do They Have
# A Code Clearance?. Posted ommni box & its worse dested Ommni Box &
# It's Worse. Skip GEMP. Do not dest onto inventory author_guess Dark.
BURNETT_SENATE_LS = [
    (1, "My Lord, Is That Legal? / I Will Make It Legal", "OBJECTIVE"),
    (1, "Tatooine: Desert Landing Site", "LOCATION"),
    (1, "Coruscant: Galactic Senate", "LOCATION"),
    (1, "Naboo: Battle Plains", "LOCATION"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
    (1, "Naboo: Theed Palace Courtyard", "LOCATION"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (1, "Lord Maul", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (1, "Darth Vader", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Dengar With Blaster Carbine", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "P-59", "CHARACTER"),
    (1, "P-60", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Coruscant Guard", "CHARACTER"),
    (2, "Tikkes", "CHARACTER"),
    (3, "Lott Dod", "CHARACTER"),
    (2, "Baskol Yeesrim", "CHARACTER"),
    (2, "Edcel Bar Gane", "CHARACTER"),
    (1, "Passel Argente", "CHARACTER"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (3, "The Point Is Conceded", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Oh, Switch Off", "INTERRUPT"),
    (1, "Sense & Uncertain Is The Future", "INTERRUPT"),
    (1, "Furry Fury", "INTERRUPT"),
    (2, "Squabbling Delegates", "INTERRUPT"),
    (1, "Vote Now!", "INTERRUPT"),
    (1, "Limited Resources", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (3, "Ommni Box & It's Worse", "INTERRUPT"),
    (1, "You Are Beaten", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "There Is No Try & Oppressive Enforcement", "EFFECT"),
    (1, "Do They Have A Code Clearance?", "EFFECT"),
    (1, "Senate Hovercam", "EFFECT"),
    (1, "Presence Of The Force", "EFFECT"),
    (1, "Our Blockade Is Perfectly Legal", "EFFECT"),
    (1, "This Is Outrageous!", "EFFECT"),
    (1, "Accepting Trade Federation Control", "EFFECT"),
    (1, "Image Of The Dark Lord", "EFFECT"),
    (1, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
]

# 22997 Dunya "Hardpack" Ertan beefed up profit.
# YAML Light / body Light Profit (match). General dest TITLE. Qty 62 as
# published. Unnamed all ten defensice shields dest 62 only. Starting
# Interrupt The Signal. Starting Effect omitted (Traffic Control has no
# STARTING:). Starting Card printed dual You Can Either Profit By This...
# / Or Be Destroyed pageid 7555 (short identity MISSING — do not mint).
# YAML author Dunya "Hardpack" Ertan. Handle Hardpack already cited; no
# Hardpack page. Inventory author_guess is the Light tag — trust YAML
# author. Do not dest onto You Can Either Profit By This as player. Do
# not dest onto Hardpack as a new person. Do not dest onto Han Solo /
# Lieutenant s'Too Vees / Jar Jar Binks / Luke Skywalker / Owen Lars as
# players. Do not dest onto Dunya Ertan hyper dest. Do not dest onto
# Dunya Ertan RST dest. Do not dest onto Ken Cross Origins Profit. Do
# not dest onto Matthew Harrison-Trainor Secret Siths Profit. Do not
# dest onto Chris Burnett My senate. Posted profit dested printed dual.
# Posted jabba palace dested Tatooine: Jabba's Palace. Posted jabba's
# palace dested Jabba's Palace: Audience Chamber. Posted han dested
# Premiere Han Solo. Posted jedis home dested Coruscant: Jedi Council
# Chamber. Posted tatooine farm dested Tatooine: Lars' Moisture Farm.
# Posted liet too veers dested Lieutenant s'Too Vees. Posted liet blunt
# dested Lieutenant Blount. Posted freon drevan dested Theron Nett.
# Posted are u brain dead dested Are You Brain Dead?!. Posted free ride
# dested Free Ride & Endor Celebration. Posted alter combo dested Alter
# & Friendly Fire. Posted i've got a bad feeling about this dested I
# Have A Bad Feeling About This. Skip GEMP. Do not dest onto inventory
# author_guess Light.
ERTAN_PROFIT_LS = [
    (1, "You Can Either Profit By This... / Or Be Destroyed", "OBJECTIVE"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Rendezvous Point", "LOCATION"),
    (1, "Dagobah: Yoda's Hut", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (2, "Tatooine: Lars' Moisture Farm", "LOCATION"),
    (1, "Han Solo", "CHARACTER"),
    (1, "Captain Yutani", "CHARACTER"),
    (1, "Corporal Rushing", "CHARACTER"),
    (1, "Lieutenant Greeve", "CHARACTER"),
    (1, "Padme Naberrie", "CHARACTER"),
    (1, "Lieutenant Williams", "CHARACTER"),
    (2, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Lando With Vibro-Ax", "CHARACTER"),
    (1, "Theron Nett", "CHARACTER"),
    (1, "Rep Been", "CHARACTER"),
    (2, "Jar Jar Binks", "CHARACTER"),
    (1, "Jerus Jannick", "CHARACTER"),
    (1, "Corporal Midge", "CHARACTER"),
    (2, "Owen Lars", "CHARACTER"),
    (1, "Lieutenant s'Too Vees", "CHARACTER"),
    (1, "Lieutenant Blount", "CHARACTER"),
    (1, "Yarua", "CHARACTER"),
    (2, "Chewie, Enraged", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "The Signal", "INTERRUPT"),
    (1, "I Have A Bad Feeling About This", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Nabrun Leids", "INTERRUPT"),
    (1, "Glancing Blow", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "Are You Brain Dead?!", "INTERRUPT"),
    (2, "Free Ride & Endor Celebration", "INTERRUPT"),
    (1, "Alter & Friendly Fire", "INTERRUPT"),
    (2, "Gift Of The Mentor", "INTERRUPT"),
    (3, "Harvest", "INTERRUPT"),
    (3, "Rebel Artillery", "INTERRUPT"),
    (1, "Traffic Control", "EFFECT"),
    (1, "I Hope She's All Right", "EFFECT"),
    (1, "Lightsaber Proficiency", "EFFECT"),
    (1, "Amidala's Blaster", "WEAPON"),
    (2, "Disruptor Pistol", "WEAPON"),
    (2, "Stun Blaster", "WEAPON"),
]

# 22978 Jacob "Armaedes" Taylor Jacob's Profit aka Big Trouble.
# YAML Light / body Light Profit (match). General dest TITLE. Qty 60.
# Named 10 Defensive Shields dest outside 60. Starting Interrupt Heading
# For The Medical Frigate. Starting Effect omitted (HFTMF starts Another
# Pathetic Lifeform, Insurrection & Aim High, Sai'torr Kal Fas (V)).
# Starting Card printed dual You Can Either Profit By This... / Or Be
# Destroyed pageid 7555 (short identity MISSING — do not mint). YAML
# author Jacob "Armaedes" Taylor. Handle Armaedes already cited; no
# Armaedes page. Inventory author_guess is the Light tag — trust YAML
# author. dump-not-stub Jacob Taylor pageid 43457. Do not dest onto You
# Can Either Profit By This as player. Do not dest onto Armaedes as a
# new person. Do not dest onto Sai'torr Kal Fas (V) current-virtual as
# player. Do not dest onto Ben Kenobi as player. Do not dest onto
# Obi-Wan Kenobi / Han Solo / Leia, Rebel Princess / Qui-Gon Jinn /
# Luke Skywalker as players. Do not dest onto Dunya Ertan beefed up
# profit. Do not dest onto Ken Cross Origins Profit. Do not dest onto
# Matthew Harrison-Trainor Secret Siths Profit. Do not dest onto Jacob
# Taylor Jacob's BHBM as player. Do not dest onto Doug Taylor. Do not
# dest onto Taylor Hayward. Do not dest onto Justin Warren as this
# player. Posted Sai?torr Kal Fas dested Sai'torr Kal Fas (V) original
# VS1. Posted Run Luke, Run dested Run Luke, Run!. Posted A Tragedy Has
# Occured dested A Tragedy Has Occurred. Posted Home One Docking Bay
# dested Home One: Docking Bay. Posted Ben Kenobi dested Special Edition
# Ben Kenobi. Posted Qui-Gon's Lightsaber dested Reflections III. Skip
# GEMP. Unnamed Yavin 4 Regionals 2nd in strategy — general dest TITLE.
# Do not dest onto inventory author_guess Light.
JACOB_PROFIT_LS = [
    (1, "You Can Either Profit By This... / Or Be Destroyed", "OBJECTIVE"),
    (1, "Jabba's Palace: Audience Chamber", "LOCATION"),
    (1, "Tatooine: Jabba's Palace", "LOCATION"),
    (1, "Tatooine: Mos Espa Docking Bay", "LOCATION"),
    (1, "Tatooine: Docking Bay 94", "LOCATION"),
    (1, "Hoth: Echo Docking Bay", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (3, "Ben Kenobi", "CHARACTER"),
    (2, "Chewie, Enraged", "CHARACTER"),
    (2, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (2, "Leia, Rebel Princess", "CHARACTER"),
    (3, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (2, "Qui-Gon Jinn", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Another Pathetic Lifeform", "EFFECT"),
    (2, "Goo Nee Tay", "EFFECT"),
    (1, "Insurrection & Aim High", "EFFECT"),
    (1, "Mantellian Savrip", "EFFECT"),
    (1, "Sai'torr Kal Fas (V)", "EFFECT"),
    (1, "Alter & Friendly Fire", "INTERRUPT"),
    (1, "Blaster Deflection", "INTERRUPT"),
    (1, "Clash Of Sabers", "INTERRUPT"),
    (1, "Dodge", "INTERRUPT"),
    (1, "Don't Underestimate Our Chances", "INTERRUPT"),
    (1, "Fallen Portal", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (2, "Jedi Presence", "INTERRUPT"),
    (1, "Narrow Escape", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (2, "Run Luke, Run!", "INTERRUPT"),
    (3, "Sense & Recoil In Fear", "INTERRUPT"),
    (2, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (2, "Speak With The Jedi Council", "INTERRUPT"),
    (3, "Tunnel Vision", "INTERRUPT"),
    (1, "Were You Looking For Me?", "INTERRUPT"),
    (1, "Anakin's Lightsaber", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Obi-Wan's Lightsaber", "WEAPON"),
    (1, "Qui-Gon's Lightsaber", "WEAPON"),
]
JACOB_PROFIT_SHIELDS = [
    (1, "A Close Race", "DEFENSIVE SHIELD"),
    (1, "A Tragedy Has Occurred", "DEFENSIVE SHIELD"),
    (1, "Battle Plan", "DEFENSIVE SHIELD"),
    (1, "Do, Or Do Not", "DEFENSIVE SHIELD"),
    (1, "Don't Do That Again", "DEFENSIVE SHIELD"),
    (1, "He Can Go About His Business", "DEFENSIVE SHIELD"),
    (1, "Only Jedi Carry That Weapon", "DEFENSIVE SHIELD"),
    (1, "Ounee Ta", "DEFENSIVE SHIELD"),
    (1, "Wise Advice", "DEFENSIVE SHIELD"),
    (1, "Your Insight Serves You Well", "DEFENSIVE SHIELD"),
]
# 1+7+17+7+24+4 = 60

# 22919 Kevin "KevOfCrofton" Elia 2002 Yavin 4 regional 2nd Place- I Am
# Jacks Anger. YAML Dark / body Dark YMSYL walkers. Date 21 Apr 2002
# AFTER VS1 BEFORE VS2 → Premiere - Original VS1. Unique qty 60. Named
# 10 Defensive Shields dest outside 60. Starting Interrupt Prepared
# Defenses. Starting Effect Fear Is My Ally. Starting Card You May Start
# Your Landing pageid 6817. Skip GEMP. Tournament dest TITLE. YAML
# author Kevin "KevOfCrofton" Elia. Inventory author_guess is the
# description fragment. Handle KevOfCrofton cited; KevOfCrofton MISSING.
# dump-not-stub Kevin Elia pageid 31588. NEW stub Stephen Turner. NEW
# hub 2002 Yavin 4 Regionals. Do not dest onto 2012 Yavin 4 Regionals
# 40442. Do not dest onto KevOfCrofton as a new person. Do not dest onto
# Lewis Blake YEEeeah dest. Do not dest onto Blizzard 4 / Grand Admiral
# Thrawn / Emperor Palpatine / Darth Maul / Darth Vader / Imperial
# Walker / You May Start Your Landing as players. Do not dest onto
# AT-AT Cannon. Do not dest onto Executor (Dark) Dagobah system. Posted
# YMSYL Effect dested OBJECTIVE. Posted Ice Plains dested Hoth: Ice
# Plains (5th Marker). Posted Defensive Perimeter dested Hoth:
# Defensive Perimeter (3rd Marker). Posted Hoth Docking Bay dested
# Hoth: Echo Docking Bay. Posted Naboo Docking Bay dested Naboo: Theed
# Palace Docking Bay. Posted Executor starship dested Flagship Executor.
# Posted Imperial Walker dested Imperial Walker. Posted Come Back Here
# You Big Coward dested Come Here You Big Coward. Posted A Useless
# Gestures dested A Useless Gesture. Posted Dr. Evazen and Ponda Baba
# dested Dr. Evazan & Ponda Baba. Event Dates April 2002 (do not invent
# 20 Apr). Winner Stephen Turner published. Location unpublished dest
# —. Tournament report promised later — do not invent a report dest.
ELIA_YAVIN = [
    (1, "You May Start Your Landing", "OBJECTIVE"),
    (1, "Hoth: Ice Plains (5th Marker)", "LOCATION"),
    (1, "Hoth: Defensive Perimeter (3rd Marker)", "LOCATION"),
    (1, "Hoth: Echo Docking Bay", "LOCATION"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
    (1, "Carida", "LOCATION"),
    (1, "Kashyyyk", "LOCATION"),
    (1, "Blockade Flagship: Bridge", "LOCATION"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (5, "Emperor Palpatine", "CHARACTER"),
    (1, "Captain Khurgee", "CHARACTER"),
    (2, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (2, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (2, "Chimaera", "STARSHIP"),
    (1, "Flagship Executor", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (2, "Imperial Walker", "VEHICLE"),
    (1, "Blizzard 2", "VEHICLE"),
    (1, "Blizzard Scout 1", "VEHICLE"),
    (2, "Blizzard 4", "VEHICLE"),
    (1, "Imperial Decree", "EFFECT"),
    (1, "Mobilization Points", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (4, "Imperial Command", "INTERRUPT"),
    (3, "Trample", "INTERRUPT"),
    (1, "He Hasn't Come Back Yet", "INTERRUPT"),
    (1, "Blow Parried", "INTERRUPT"),
    (2, "Sense & Uncertain Is The Future", "INTERRUPT"),
    (1, "Scanning Crew", "INTERRUPT"),
    (3, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (2, "Walker Garrison", "INTERRUPT"),
    (2, "Force Lightning", "INTERRUPT"),
]
ELIA_YAVIN_SHIELDS = [
    (1, "Oppressive Enforcement", "DEFENSIVE SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE SHIELD"),
    (1, "Come Here You Big Coward", "DEFENSIVE SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE SHIELD"),
    (1, "Battle Order", "DEFENSIVE SHIELD"),
    (1, "Fanfare", "DEFENSIVE SHIELD"),
    (1, "Resistance", "DEFENSIVE SHIELD"),
    (1, "A Useless Gesture", "DEFENSIVE SHIELD"),
    (1, "You Cannot Hide Forever", "DEFENSIVE SHIELD"),
    (1, "We'll Let Fate-a Decide, Huh?", "DEFENSIVE SHIELD"),
]
# 22886 Mike "mikezap" Stevens ls senate
# YAML Light / body Light Plead My Case To The Senate (match). General dest TITLE.
# Date 19 Apr 2002 AFTER VS1 BEFORE VS2 → Premiere - Original VS1.
# Unique qty 70. No Defensive Shields listed dest 70 only with qty note.
# Starting Interrupt HFTMF. Starting Effect omitted. Starting Card printed dual
# Plead My Case To The Senate. Skip GEMP. Inventory author_guess is Light tag.
# Posted senator valorum dested as posted (strategy oops Palpatine). Posted
# stay here where its safe dested Stay Here, Where It's Safe. Posted kin kain
# dested Kin Kian. Posted sei teria dested Sei Taria. Posted dont get @#$%y
# dested Don't Get Cocky. Posted vote now dested Vote Now!. Posted master luke
# dested Luke Skywalker, Jedi Knight. Posted x wing laser cannon dested
# X-wing Laser Cannon. Posted tantive 4 dested Tantive IV. Posted jedi
# prescence dested Jedi Presence. Do not dest onto Chris Burnett My senate.
# Do not dest onto 2002 Vegas DPC Brian Hunter LS Senate. Do not dest onto
# Yoda card. Do not dest onto Mace Windu / Admiral Ackbar / Home One /
# Coruscant Guard as players. Do not dest onto mikezap as a new person.
# Do not dest onto inventory author_guess Light. Do not dest onto Senator
# Palpatine as the posted Senator Valorum row.
STEVENS_LS = [
    (1, "Plead My Case To The Senate / Sanity And Compassion", "OBJECTIVE"),
    (1, "Coruscant: Galactic Senate", "LOCATION"),
    (1, "Coruscant", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Security Control", "EFFECT"),
    (1, "Staging Areas", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Coruscant: Docking Bay", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (1, "Ric Olie", "CHARACTER"),
    (1, "Queen's Royal Starship", "STARSHIP"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Derek 'Hobbie' Klivian", "CHARACTER"),
    (1, "Red Squadron 4", "STARSHIP"),
    (1, "Keir Santage", "CHARACTER"),
    (1, "Red Squadron 7", "STARSHIP"),
    (1, "Kin Kian", "CHARACTER"),
    (1, "Gold Squadron 1", "STARSHIP"),
    (1, "Colonel Cracken", "CHARACTER"),
    (1, "Tala 1", "STARSHIP"),
    (1, "Green Leader", "CHARACTER"),
    (1, "Green Squadron 1", "STARSHIP"),
    (1, "Admiral Ackbar", "CHARACTER"),
    (1, "Home One", "STARSHIP"),
    (1, "Tantive IV", "STARSHIP"),
    (1, "Supreme Chancellor Valorum", "CHARACTER"),
    (1, "Senator Valorum", "CHARACTER"),
    (1, "Mas Amedda", "CHARACTER"),
    (1, "Sei Taria", "CHARACTER"),
    (1, "Horox Ryyder", "CHARACTER"),
    (1, "Liana Merian", "CHARACTER"),
    (1, "Yarua", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (2, "Chewie, Enraged", "CHARACTER"),
    (1, "General Solo", "CHARACTER"),
    (1, "Boushh", "CHARACTER"),
    (1, "Orrimaarko", "CHARACTER"),
    (1, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (1, "Mace Windu", "CHARACTER"),
    (1, "Coruscant Guard", "CHARACTER"),
    (1, "Might Of The Republic", "INTERRUPT"),
    (2, "A Few Maneuvers", "INTERRUPT"),
    (1, "We Wish To Board At Once", "INTERRUPT"),
    (1, "Rebel Barrier", "INTERRUPT"),
    (2, "Fallen Portal", "INTERRUPT"),
    (1, "Jedi Presence", "INTERRUPT"),
    (1, "First Aid", "INTERRUPT"),
    (2, "Organized Attack", "INTERRUPT"),
    (1, "Don't Get Cocky", "INTERRUPT"),
    (1, "Tunnel Vision", "INTERRUPT"),
    (1, "Inconsequential Barriers", "INTERRUPT"),
    (1, "The Signal", "INTERRUPT"),
    (1, "The Force Is Strong With This One", "INTERRUPT"),
    (1, "Vote Now!", "INTERRUPT"),
    (1, "Stay Here, Where It's Safe", "INTERRUPT"),
    (1, "Narrow Escape", "INTERRUPT"),
    (1, "Senate Hovercam", "EFFECT"),
    (1, "Battle Plan", "EFFECT"),
    (1, "Projection Of A Skywalker", "EFFECT"),
    (1, "Legendary Starfighter", "EFFECT"),
    (1, "The Gravest Of Circumstances", "EFFECT"),
    (1, "I Will Not Defer", "EFFECT"),
    (1, "X-wing Laser Cannon", "WEAPON"),
]
# 7 start + 3 loc + 17 ships/pilots + 7 senators + 10 guys + 19 int + 4 eff + 2 pol + 1 weap = 70
# 22705 Casey "The Demon" Merry Celebration what
# YAML Light / body Light Cloud City Celebration (match). General dest TITLE.
# Date 9 Apr 2002 AFTER VS1 BEFORE VS2 → Premiere - Original VS1.
# Unique qty 60. No Defensive Shields listed dest 60 only. Skip GEMP.
# Starting Interrupt HFTMF. Starting Effect omitted (HFTMF 3: Another
# Pathetic Lifeform / Menace Fades / Get To Your Ships!). Starting Card
# Cloud City: Guest Quarters. Inventory author_guess is description
# fragment — trust YAML author. Posted Cloud CityCasino dested Cloud
# City: Casino. Posted Cloud CityIncinerator dested Cloud City:
# Incinerator. Posted Cloud CityGuest Quarters dested Cloud City: Guest
# Quarters. Posted Cloud CityLower Corridor dested Cloud City: Lower
# Corridor. Posted Cloud CityPlatform 327 dested Cloud City: Platform
# 327 (Docking Bay). Posted Capt. Han Solo dested Captain Han Solo.
# Posted Jerus Jannik dested Jerus Jannick. Posted Wedge Antilles, RSL
# dested Wedge Antilles, Red Squadron Leader. Posted Luke w/Lightsaber
# dested Luke With Lightsaber. Posted Luke, Rebel Scout dested Luke
# Skywalker, Rebel Scout. Posted Leia w/gun dested Leia With Blaster
# Rifle. Posted Ric Olie, BL dested Ric Olie, Bravo Leader. Posted
# Lando, Scoundrel dested Lando Calrissian, Scoundrel. Posted JJ' Pole
# dested Jar Jar's Electropole. Posted Inruder missle dested Intruder
# Missile. Posted Luke's Stick dested Luke's Lightsaber. Posted
# Chewbacca's Gun dested Chewbacca's Bowcaster. Posted Get to your Ships
# dested Get To Your Ships!. Posted Let's go Left dested Let's Go Left.
# Posted Han, Chewie, and the Falcon dested Han, Chewie, And The Falcon.
# Posted Red Leader in Red 1 dested Red Leader In Red 1. Do not dest
# onto Cloud City Limited. Do not dest onto Cloud City Celebration as
# player. Do not dest onto Cloud City: Guest Quarters as player. Do not
# dest onto Bravo 1 / Bravo 2 as players. Do not dest onto Mace Windu as
# player. Do not dest onto The Demon as a new person. Do not dest onto
# inventory author_guess. Do not dest onto David Kangas QMC Clouds. Do
# not dest onto Chris McCoy Quiet Macking of Cloud city. Do not dest
# onto Sam Diamond QMC dest. Do not dest onto Jon Manning Cloud City
# trooper deck.
MERRY_LS = [
    (1, "Cloud City: Guest Quarters", "LOCATION"),
    (1, "Kessel", "LOCATION"),
    (1, "Naboo", "LOCATION"),
    (1, "Kiffex", "LOCATION"),
    (1, "Bespin", "LOCATION"),
    (1, "Cloud City: Casino", "LOCATION"),
    (1, "Cloud City: Incinerator", "LOCATION"),
    (1, "Cloud City: Lower Corridor", "LOCATION"),
    (1, "Cloud City: Platform 327 (Docking Bay)", "LOCATION"),
    (1, "Captain Han Solo", "CHARACTER"),
    (1, "Ki-Adi-Mundi", "CHARACTER"),
    (1, "Jerus Jannick", "CHARACTER"),
    (1, "Mace Windu, Jedi Master", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Luke With Lightsaber", "CHARACTER"),
    (1, "Padme Naberrie", "CHARACTER"),
    (1, "Luke Skywalker, Rebel Scout", "CHARACTER"),
    (1, "Keir Santage", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (2, "Princess Leia", "CHARACTER"),
    (1, "Ric Olie, Bravo Leader", "CHARACTER"),
    (1, "Chewie, Enraged", "CHARACTER"),
    (1, "Officer Dolphe", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (3, "Bionic Hand", "DEVICE"),
    (1, "Jar Jar's Electropole", "WEAPON"),
    (3, "Ewok Catapult", "WEAPON"),
    (1, "Intruder Missile", "WEAPON"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (1, "Chewbacca's Bowcaster", "WEAPON"),
    (3, "Disarmed", "EFFECT"),
    (2, "Cloud City Celebration", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (2, "Mantellian Savrip", "EFFECT"),
    (1, "Another Pathetic Lifeform", "EFFECT"),
    (1, "Get To Your Ships!", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Docking And Repair Facilities", "EFFECT"),
    (1, "Reflection", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Red Leader In Red 1", "STARSHIP"),
    (1, "Red 7", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Bravo 1", "STARSHIP"),
    (1, "Bravo 2", "STARSHIP"),
    (1, "Let's Go Left", "ADMIRALS_ORDER"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Alter", "INTERRUPT"),
]
# 9 loc + 16 char + 3 device + 7 weap + 16 eff + 6 ship + 1 AO + 2 int = 60
# 1+7+16+4+6+6+20 = 60

# 22701 Darryll "217" Silva (signs Shadow32) WifeBeater- No hold barred
# YAML Light / body Dark Hoth walkers (YMSYL). General dest. Published
# title kept OFF dest TITLE (author notes readers found it offensive) —
# dest {Player} DS; original post heading still shows it. [Claude 2026-10-10]
# Date 9 Apr 2002 → Premiere - Original VS1. Qty 60 incl. FIMA. Unnamed
# "Shields" under FIMA dest 60 only. Starting Card YMSYL (posted under
# Effects; dested OBJECTIVE as Elia 22919). Starting Interrupt Prepared
# Defenses; Starting Effect Fear Is My Ally. Skip GEMP.
# Posted Emperor Palpy dested Emperor Palpatine. Posted Epp Vader dested
# Darth Vader With Lightsaber. Posted Enhanced Maul dested Darth Maul With
# Lightsaber. Posted IG with gun dested IG-88 With Riot Gun. Posted Ozzel
# dested Admiral Ozzel. Posted Janus dested Janus Greejatus. Posted Piett
# dested Admiral Piett. Posted Merrejk dested Commander Merrejk. Posted
# Thrawn dested Grand Admiral Thrawn. Posted gen veers dested General
# Veers. Posted Dre& Peanut Butter dested Dr. Evazan & Ponda Baba. Posted
# Insane in da membrane Fett dested Boba Fett, Bounty Hunter (strategy:
# "Boba Fett, BH"). Posted Igar dested Commander Igar. Posted Chiraneau
# dested Admiral Chiraneau. Posted tagge dested General Tagge. Posted 4lom
# with gun dested 4-LOM With Concussion Rifle. Posted executor dested
# Flagship Executor (as Elia 22919). Posted Dengar/Bossk/Zuck in ship
# dested Dengar In Punishing One / Bossk In Hound's Tooth / Zuckuss In
# Mist Hunter. Posted Tempest1 dested Tempest 1. Posted 2xIntro Hoth
# Walkers dested 2 Imperial Walker (ESB Introductory Two-Player). Posted
# Ice Plains / Defensive perimeter / Echo DB / Executor DB dested Hoth:
# Ice Plains (5th Marker) / Hoth: Defensive Perimeter (3rd Marker) / Hoth:
# Echo Docking Bay / Executor: Docking Bay. Posted Lat Damage dested
# Lateral Damage. Posted Rebel base Beating dested Rebel Base Occupation
# (strategy: "Rebel Base Occ."). Posted IAO&SP dested Imperial Arrest
# Order & Secret Plans (one combo card). Posted Mob points dested
# Mobilization Points. Posted imp decree dested Imperial Decree. Posted
# we mush accelerate dested We Must Accelerate Our Plans. Posted sniper
# dark strike dested Sniper & Dark Strike. Posted imp barrier dested
# Imperial Barrier. Posted prep defenses dested Prepared Defenses. Posted
# There still coming through dested They're Still Coming Through!. Posted
# ommni box combo dested Ommni Box & It's Worse. Posted Battle deployment
# dested Battle Deployment. Handles 217 / Shadow32 cited; no handle pages.
# Credits John Patchell's archetype — plain text, no person page invented.
# Do not dest onto 2002 Vegas DPC / 2002 Alderaan Regionals (only "see you
# at"). Do not dest onto inventory author_guess. Do not dest onto Elia 22919.
SILVA_DS = [
    (1, "You May Start Your Landing", "OBJECTIVE"),
    (1, "Hoth", "LOCATION"),
    (1, "Hoth: Ice Plains (5th Marker)", "LOCATION"),
    (1, "Hoth: Defensive Perimeter (3rd Marker)", "LOCATION"),
    (1, "Hoth: Echo Docking Bay", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Fondor", "LOCATION"),
    (1, "Emperor Palpatine", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "Darth Maul With Lightsaber", "CHARACTER"),
    (1, "IG-88 With Riot Gun", "CHARACTER"),
    (1, "Admiral Ozzel", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "General Veers", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "Boba Fett, Bounty Hunter", "CHARACTER"),
    (1, "Commander Igar", "CHARACTER"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (1, "General Tagge", "CHARACTER"),
    (1, "4-LOM With Concussion Rifle", "CHARACTER"),
    (1, "Flagship Executor", "STARSHIP"),
    (1, "Dengar In Punishing One", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Tempest 1", "VEHICLE"),
    (1, "Blizzard 1", "VEHICLE"),
    (1, "Blizzard 2", "VEHICLE"),
    (1, "Blizzard 4", "VEHICLE"),
    (2, "Imperial Walker", "VEHICLE"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "Rebel Base Occupation", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "Mobilization Points", "EFFECT"),
    (1, "Imperial Decree", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (3, "Trample", "INTERRUPT"),
    (2, "Walker Garrison", "INTERRUPT"),
    (4, "Imperial Command", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (1, "Imperial Barrier", "INTERRUPT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "They're Still Coming Through!", "INTERRUPT"),
    (1, "Ommni Box & It's Worse", "INTERRUPT"),
    (1, "Battle Deployment", "ADMIRALS_ORDER"),
]
# 1 obj + 6 loc + 17 char + 5 ship + 6 veh + 7 eff + 17 int + 1 AO = 60

# 23136 Thomas "Yoda TP" Papp HDADTJ aka there are no Jedi alive
# YAML Dark / body Dark Hunt Down (match). General dest TITLE. Qty 61 as
# published (Interrupts labeled 15, listed 16). FIMA inside Starting (9)
# counts. Named 10 Defensive Shields dest outside 61. Author Thomas
# "Yoda TP" Papp. Handle Yoda TP cited; no Yoda TP page. [[Thomas Papp]]
# missing — stub. Inventory author_guess is the description fragment —
# trust YAML author. Do not dest onto Yoda card pageid 4339. Do not dest
# onto Papp as a last-name-only page. Do not dest onto Hunt Down And
# Destroy The Jedi as player. Do not dest onto Darth Vader / Darth Maul
# / Emperor Palpatine / Mara Jade / Blizzard 4 / Grand Admiral Thrawn /
# Grand Moff Tarkin / Janus Greejatus as players. Do not dest onto Sam
# Diamond. Posted HDADTJ/There are no Jedi dested Hunt Down And Destroy
# The Jedi. Posted ExecutorHolotheatre dested Executor: Holotheatre.
# Posted ExecutorMed. Chamber dested Executor: Meditation Chamber.
# Posted Prep. Defenses dested Prepared Defenses. Posted They Will B No
# Match 4 U dested They Will Be No Match For You. Posted IAO/Secret
# Plans dested Imperial Arrest Order & Secret Plans. Posted Mob. Point/
# You Cannot Hide Forever dested You Cannot Hide Forever & Mobilization
# Points. Posted Lord Vader dested Lord Vader. Posted DVDLOTS dested
# Darth Vader, Dark Lord Of The Sith. Posted Vader w/ stick dested
# Darth Vader With Lightsaber. Posted Darth Maul, Young Apprentice
# dested Darth Maul, Young Apprentice. Posted Mara Jade, TEH dested
# Mara Jade, The Emperor's Hand. Posted Janus Grejatus dested Janus
# Greejatus. Posted Zuckuss In Boat dested Zuckuss In Mist Hunter.
# Posted Bossk In Bus dested Bossk In Hound's Tooth. Posted Fett In S1
# dested Boba Fett In Slave I. Posted Dengar In P1 dested Dengar In
# Punishing One. Posted Chimaera dested Chimaera. Posted DB dested
# Executor: Docking Bay. Posted Endor DB dested Endor: Landing Platform
# (Docking Bay). Posted DS DB dested Death Star II: Docking Bay. Posted
# Mara’s dested Mara Jade's Lightsaber. Posted Maul’s dested Maul's
# Double-Bladed Lightsaber. Posted Vader’s dested Vader's Lightsaber.
# Posted Darth Vader’s dested Darth Vader's Lightsaber. Posted
# Sniper/Dark Strike dested Sniper & Dark Strike. Posted Ghhhk/TRWEU
# dested Ghhhk & Those Rebels Won't Escape Us. Posted Weapon Lev.
# dested Weapon Levitation. Posted Masterful Move dested Masterful
# Move (as posted, not the Occupation combo). Posted Sec. Prec. dested
# Security Precautions. Posted The Phantom Manace dested The Phantom
# Menace. Posted You've Never Won A Podrace dested You've Never Won A
# Race?. They Will Be No Match For You / Epic Duel / Visage are extra
# start, not Starting Effect. Starting Interrupt Prepared Defenses.
# Starting Effect Fear Is My Ally. Starting Card printed dual HDADTJ.
# Skip GEMP. Format Premiere - Original VS1 (5 May 2002; VS1 legal 9
# Mar 2002; VS2 legal 1 Jun 2002). No original (V) cards posted. YAML
# `!` stripped.
PAPP_DS = [
    (1, "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", "OBJECTIVE"),
    (1, "Executor: Holotheatre", "LOCATION"),
    (1, "Executor: Meditation Chamber", "LOCATION"),
    (1, "Visage Of The Emperor", "EFFECT"),
    (1, "Epic Duel", "EFFECT"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "They Will Be No Match For You", "EFFECT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Lord Vader", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (2, "Darth Vader With Lightsaber", "CHARACTER"),
    (1, "Darth Maul", "CHARACTER"),
    (2, "Darth Maul, Young Apprentice", "CHARACTER"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (3, "Emperor Palpatine", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Grand Moff Tarkin", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Dengar In Punishing One", "STARSHIP"),
    (1, "Chimaera", "STARSHIP"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Rendili", "LOCATION"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Darth Vader's Lightsaber", "WEAPON"),
    (2, "The Circle Is Now Complete", "INTERRUPT"),
    (2, "Vader's Obsession", "INTERRUPT"),
    (3, "Maul Strikes", "INTERRUPT"),
    (2, "Masterful Move", "INTERRUPT"),
    (2, "Twi'lek Advisor", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Ghhhk & Those Rebels Won't Escape Us", "INTERRUPT"),
    (2, "Weapon Levitation", "INTERRUPT"),
    (1, "No Escape", "EFFECT"),
    (1, "Imperial Decree", "EFFECT"),
    (2, "Visage Of The Emperor", "EFFECT"),
    (1, "Security Precautions", "EFFECT"),
    (2, "The Phantom Menace", "EFFECT"),
]
PAPP_SHIELDS = [
    (1, "Come Here You Big Coward", "DEFENSIVE_SHIELD"),
    (1, "Battle Order", "DEFENSIVE_SHIELD"),
    (1, "Weapon Of A Sith", "DEFENSIVE_SHIELD"),
    (1, "You've Never Won A Race?", "DEFENSIVE_SHIELD"),
    (1, "A Useless Gesture", "DEFENSIVE_SHIELD"),
    (1, "Allegations Of Corruption", "DEFENSIVE_SHIELD"),
    (1, "Do They Have A Code Clearance?", "DEFENSIVE_SHIELD"),
    (1, "Leave Them To Me", "DEFENSIVE_SHIELD"),
    (1, "Wipe Them Out, All Of Them", "DEFENSIVE_SHIELD"),
    (1, "We'll Let Fate-a Decide, Huh?", "DEFENSIVE_SHIELD"),
]

# 23152 Sam "AgentSD" Diamond The CIA Is Trying To Kill Me
# YAML Light / body Light QMC (match). General dest TITLE. Qty 60:
# Starting 8 + Locations 3 + Characters 17 + Ships 5 + Weapons 3 +
# Interrupts 20 + Effects 2 + AO 2. AUOF inside Starting (8) counts
# toward 60. Unnamed shields dest 60 only (no shields section).
# Author Sam "AgentSD" Diamond. Handle AgentSD cited; no AgentSD page.
# [[Sam Diamond]] missing — stub. Inventory author_guess is the Non
# Phixion description fragment — trust YAML author. Do not dest onto
# CIA / Non Phixion / Quiet Mining Colony as player. Do not dest onto
# Drew Scott. Do not dest onto Luke / Obi-Wan / Qui-Gon / Leia / Dash /
# Ten Numb / Corran Horn as players. Posted QMC/Balls dested Quiet
# Mining Colony / Independent Operation. Posted Bespin dested Light
# Bespin. Posted CC Guest Quarters dested Cloud City: Guest Quarters.
# Posted An Unusual Amount of Feast (fear) dested An Unusual Amount Of
# Fear. Posted Squad A$$ dested Squadron Assignments. Posted Keeping
# the emp out forever dested Keeping The Empire Out Forever (same as
# 23975/24022). Posted Heading for the frig dested Heading For The
# Medical Frigate. Posted CC North Corridor / Carbonite Chamber / West
# Gallery dested Cloud City: …. Posted Luke EPP dested Luke With
# Lightsaber. Posted Obi EPP dested Obi-Wan With Lightsaber. Posted
# Qui Gon w/ stick dested Qui-Gon Jinn With Lightsaber. Posted Leia
# EPP dested Leia With Blaster Rifle. Posted DS2 Wedge dested Wedge
# Antilles, Red Squadron Leader. Posted Lando, Scoundrel dested Lando
# Calrissian, Scoundrel. Posted Han, Chewie, and Falcon dested Han,
# Chewie, And The Falcon. Posted Queen's Royal Starship dested Queen's
# Royal Starship. Posted Red Squad 1 dested Red Squadron 1. Posted
# Blue Squad 5 dested Blue Squadron 5. Posted We Wish To Board at
# once dested We Wish To Board At Once. Posted Path of Least
# resistance dested Path Of Least Resistance. Posted OOC/TT dested
# Out Of Commission & Transmission Terminated. Posted A Jedi's
# Reslience dested A Jedi's Resilience. Posted SATM/BP dested Sorry
# About The Mess & Blaster Proficiency. Posted Gift of the Mentor
# dested Gift Of The Mentor. Posted Off the Edge dested On The Edge.
# Posted CC Celebration dested Cloud City Celebration. Posted Capital
# Support dested Capital Support x2. KTEOF / Squadron Assignments /
# Strike Planning are extra start, not Starting Effect. Guest
# Quarters / Bespin are QMC-deployed. Starting Interrupt Heading For
# The Medical Frigate. Starting Effect An Unusual Amount Of Fear.
# Starting Card printed dual QMC. Skip GEMP. Format Premiere -
# Original VS1 (5 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun
# 2002). No original (V) cards posted. YAML `!` stripped.
DIAMOND_LS = [
    (1, "Quiet Mining Colony / Independent Operation", "OBJECTIVE"),
    (1, "Bespin", "LOCATION"),
    (1, "Cloud City: Guest Quarters", "LOCATION"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Strike Planning", "EFFECT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Keeping The Empire Out Forever", "EFFECT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Cloud City: North Corridor", "LOCATION"),
    (1, "Cloud City: Carbonite Chamber", "LOCATION"),
    (1, "Cloud City: West Gallery", "LOCATION"),
    (3, "Luke With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (1, "Leia With Blaster Rifle", "CHARACTER"),
    (1, "Ten Numb", "CHARACTER"),
    (1, "Ric Olie", "CHARACTER"),
    (1, "General Walex Blissex", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Pucumir Thryss", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "General Crix Madine", "CHARACTER"),
    (2, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Dash Rendar", "CHARACTER"),
    (1, "Outrider", "STARSHIP"),
    (1, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Queen's Royal Starship", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Blue Squadron 5", "STARSHIP"),
    (2, "Intruder Missile", "WEAPON"),
    (1, "X-Wing Laser Cannon", "WEAPON"),
    (2, "We Wish To Board At Once", "INTERRUPT"),
    (1, "Life Debt", "INTERRUPT"),
    (3, "Path Of Least Resistance", "INTERRUPT"),
    (3, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Power Pivot", "INTERRUPT"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (2, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (2, "Rebel Barrier", "INTERRUPT"),
    (2, "Rebel Artillery", "INTERRUPT"),
    (1, "Gift Of The Mentor", "INTERRUPT"),
    (1, "On The Edge", "INTERRUPT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Cloud City Celebration", "EFFECT"),
    (2, "Capital Support", "ADMIRALS_ORDER"),
]

# 23182 drew "drew man1" scott BHBM how to kill combat
# YAML Light / body Dark BHBM. General dest TITLE (4-0 at freedom con in
# strategy; do not mint Freedom Con hub; do not dest as 2001 Worlds).
# Qty 60 as posted (objective omitted from the list). FIMA inside Starting
# counts. Unnamed (you pick shields) dest 60 only. Starting Interrupt
# Prepared Defenses. Starting Effect Fear Is My Ally. Starting Card printed
# dual BHBM (title). Posted Igar dested Commander Igar. Posted Blow parred
# dested Blow Parried. Posted 4-lom dested 4-LOM. Posted twi lek dested
# Twi'lek Advisor. Posted YCHF/mob. points dested You Cannot Hide Forever
# & Mobilization Points. Posted IAO/Secret plans dested Imperial Arrest
# Order & Secret Plans. Posted ponda boba/dr. E dested Dr. Evazan & Ponda
# Baba. Posted Fett in ship dested Boba Fett In Slave I. Posted bossk in
# ship dested Bossk In Hound's Tooth. Posted zuckuss in ship dested
# Zuckuss In Mist Hunter. Posted maras sabre dested Mara Jade's Lightsaber.
# Posted naboo DB dested Naboo: Theed Palace Docking Bay. Posted rendilli
# dested Rendili. Posted sniper/ DS dested Sniper & Dark Strike. Posted
# monnok/ evader dested Evader & Monnok. Posted barrier dested Imperial
# Barrier. Skip GEMP. Handle drew man1 cited; no drew man1 page.
# [[Drew Scott]] dump-not-stub pageid 41620 (2005 World Champion).
# Do not dest onto Scott pageid 40447. Do not dest onto Bring Him Before
# Me as player. Do not dest onto Darth Maul. Do not dest onto Darth Vader.
# Do not dest onto Emperor Palpatine as player. Do not dest onto Mara Jade
# as player. Do not dest onto Blizzard 4 as player. Do not dest onto
# Jacob Taylor. Do not dest onto Geoff Bowman BHBM dest as player. Do not
# dest onto inventory author_guess Light.
SCOTT_DS = [
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Death Star II: Throne Room", "LOCATION"),
    (1, "Prepared Defenses", "INTERRUPT"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (1, "Insignificant Rebellion", "EFFECT"),
    (1, "Your Destiny", "EFFECT"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Mara Jade, The Emperor's Hand", "CHARACTER"),
    (2, "Darth Maul With Lightsaber", "CHARACTER"),
    (3, "Darth Vader With Lightsaber", "CHARACTER"),
    (3, "Janus Greejatus", "CHARACTER"),
    (1, "Commander Igar", "CHARACTER"),
    (2, "Darth Sidious", "CHARACTER"),
    (1, "DS-61-4", "CHARACTER"),
    (1, "Dr. Evazan & Ponda Baba", "CHARACTER"),
    (1, "4-LOM", "CHARACTER"),
    (1, "Blizzard 4", "VEHICLE"),
    (1, "Blizzard 2", "VEHICLE"),
    (1, "Tempest 1", "VEHICLE"),
    (1, "Boba Fett In Slave I", "STARSHIP"),
    (1, "Bossk In Hound's Tooth", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (1, "Security Precautions", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (1, "No Escape", "EFFECT"),
    (1, "First Strike", "EFFECT"),
    (1, "Search And Destroy", "EFFECT"),
    (1, "Blast Door Controls", "EFFECT"),
    (2, "Blow Parried", "INTERRUPT"),
    (2, "Twi'lek Advisor", "INTERRUPT"),
    (1, "Force Lightning", "INTERRUPT"),
    (1, "Sniper & Dark Strike", "INTERRUPT"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "Trample", "INTERRUPT"),
    (2, "Force Field", "INTERRUPT"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (2, "Young Fool", "INTERRUPT"),
    (1, "You Are Beaten", "INTERRUPT"),
    (1, "Mara Jade's Lightsaber", "WEAPON"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
    (1, "Death Star II: Docking Bay", "LOCATION"),
    (1, "Endor: Landing Platform (Docking Bay)", "LOCATION"),
    (1, "Rendili", "LOCATION"),
]

# 23407 Brian "HuntaWarya" Hunter LS Senate done RIGHT aka Ghhhks Away
# YAML Light / body Light Senate. Tournament dest TITLE (won Vegas DPC 5-0;
# Lush TR 15 May 2002 names Hunter winner; Saturday the 11th + Sunday
# tournament → 12 May 2002). Qty 60. AUOF inside Starting Effect counts.
# Unnamed (w/10 shields) dest 60 only. Starting Interrupt Heading For The
# Medical Frigate (in the 60). Posted Plead My Case to the Senate/Sanity and
# Compassion dested printed dual. Posted 3PO w/ His Parts Showing dested
# Threepio With His Parts Showing. Posted AWRI/Darklighter Spin dested All
# Wings Report In & Darklighter Spin. Posted Alter (coruscant version) dested
# Alter (Coruscant). Posted Queen Amidala, Ruler of the Naboo dested Queen
# Amidala, Ruler Of Naboo. Posted Ascertaining the Truth dested Ascertaining
# The Truth. Posted The Gravest of Circumstances dested The Gravest Of
# Circumstances. Skip GEMP. Format Premiere - Original VS1 (12 May 2002; VS1
# legal 9 Mar 2002; VS2 legal 1 Jun 2002). Handle HuntaWarya already a
# redirect to Brian Hunter dump-not-stub 36782. Do not dest onto Ghhhk /
# Senate / Plead My Case as player. Do not dest onto HUNTER_DS_TITLE.
HUNTER_LS = [
    (1, "Plead My Case To The Senate / Sanity And Compassion", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Coruscant: Jedi Council Chamber", "LOCATION"),
    (1, "Spaceport Docking Bay", "LOCATION"),
    (1, "Home One: Docking Bay", "LOCATION"),
    (1, "Naboo: Theed Palace Docking Bay", "LOCATION"),
    (1, "Coruscant: Galactic Senate", "LOCATION"),
    (3, "Horox Ryyder", "CHARACTER"),
    (1, "Tendau Bendon", "CHARACTER"),
    (3, "Queen Amidala, Ruler Of Naboo", "CHARACTER"),
    (3, "Senator Palpatine", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Luke With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Lando Calrissian, Scoundrel", "CHARACTER"),
    (1, "Yoda, Master Of The Force", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (2, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (3, "Might Of The Republic", "INTERRUPT"),
    (2, "We Wish To Board At Once", "INTERRUPT"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (3, "A Jedi's Resilience", "INTERRUPT"),
    (1, "Inconsequential Barriers", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "All Wings Report In & Darklighter Spin", "INTERRUPT"),
    (1, "Clash Of Sabers", "INTERRUPT"),
    (1, "Alter (Coruscant)", "INTERRUPT"),
    (1, "Sense", "INTERRUPT"),
    (1, "Sense & Recoil In Fear", "INTERRUPT"),
    (2, "Life Debt", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (1, "Senate Hovercam", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Docking And Repair Facilities", "EFFECT"),
    (1, "Colo Claw Fish", "EFFECT"),
    (1, "Insurrection & Aim High", "EFFECT"),
    (1, "Draw Their Fire", "EFFECT"),
    (1, "Ascertaining The Truth", "EFFECT"),
    (1, "Plea To The Court", "EFFECT"),
    (1, "The Gravest Of Circumstances", "EFFECT"),
    (1, "Don't Do That Again", "EFFECT"),
    (1, "Goo Nee Tay", "EFFECT"),
]

# 23598 Brian "HuntaWarya" Hunter Saber Combat done RIGHT aka No Mans Land
# YAML Dark / body Dark LSC. General dest TITLE (3 unnamed tournaments 8-0 then
# 11-0 after VS1; do not mint hubs; do not invent finish rows). Qty 60. FIMA
# inside Starting Effect counts. Unnamed 10 shields dest 60 only. Starting
# Interrupt Prepared Defenses (in the 60). Posted Executor starship dested
# Flagship Executor (wiki_card Executor dests the Dagobah system). Posted
# Monnok/Evader dested Evader & Monnok. Posted Prophetess (Virtual version)
# dested Prophetess (V) (VS1). Posted Blaster Rack (virtual version) dested
# Blaster Rack (V) (VS1). Posted We Must Accelerate our Plans dested printed
# Coruscant Dark. Posted Theed Palace Generator dested Naboo: Theed Palace
# Generator. Posted Let them make the first move/At last we will have our
# revenge dested dual. Admiral Ozzel amendment dest as published (60 keeps
# I Have You Now x2). Skip GEMP. Format Premiere - Original VS1 (26 May 2002;
# VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002). Handle HuntaWarya already a GPN
# stub pageid 41710 — redirect to Brian Hunter dump-not-stub 36782. Do not dest
# onto Maul / Darth Maul / Lord Maul.
HUNTER_DS = [
    (1, "Let Them Make The First Move / At Last We Will Have Revenge", "OBJECTIVE"),
    (1, "Fear Is My Ally", "EFFECT"),
    (1, "Deep Hatred", "EPIC_EVENT"),
    (1, "Naboo: Theed Palace Generator", "LOCATION"),
    (1, "Naboo: Theed Palace Generator Core", "LOCATION"),
    (1, "Executor: Docking Bay", "LOCATION"),
    (1, "Fondor", "LOCATION"),
    (1, "Endor", "LOCATION"),
    (4, "Lord Maul", "CHARACTER"),
    (1, "Lord Vader", "CHARACTER"),
    (1, "Darth Vader, Dark Lord Of The Sith", "CHARACTER"),
    (2, "Emperor Palpatine", "CHARACTER"),
    (1, "Janus Greejatus", "CHARACTER"),
    (1, "Admiral Piett", "CHARACTER"),
    (1, "Admiral Chiraneau", "CHARACTER"),
    (1, "Grand Admiral Thrawn", "CHARACTER"),
    (1, "Guri", "CHARACTER"),
    (1, "Prophetess (V)", "CHARACTER"),
    (1, "Arica", "CHARACTER"),
    (1, "Commander Merrejk", "CHARACTER"),
    (1, "Flagship Executor", "STARSHIP"),
    (2, "Chimaera", "STARSHIP"),
    (1, "Stinger", "STARSHIP"),
    (1, "Zuckuss In Mist Hunter", "STARSHIP"),
    (2, "Maul's Double-Bladed Lightsaber", "WEAPON"),
    (1, "Vader's Lightsaber", "WEAPON"),
    (1, "Imperial Arrest Order & Secret Plans", "EFFECT"),
    (1, "You Cannot Hide Forever & Mobilization Points", "EFFECT"),
    (1, "Blaster Rack (V)", "EFFECT"),
    (1, "Crush The Rebellion", "EFFECT"),
    (3, "The Phantom Menace", "EFFECT"),
    (1, "Qui-Gon's End", "EFFECT"),
    (1, "Lateral Damage", "EFFECT"),
    (3, "Imperial Command", "INTERRUPT"),
    (2, "Blow Parried", "INTERRUPT"),
    (2, "Stunning Leader", "INTERRUPT"),
    (2, "We Must Accelerate Our Plans", "INTERRUPT"),
    (1, "Masterful Move", "INTERRUPT"),
    (1, "Masterful Move & Endor Occupation", "INTERRUPT"),
    (1, "Ghhhk", "INTERRUPT"),
    (1, "Evader & Monnok", "INTERRUPT"),
    (2, "I Have You Now", "INTERRUPT"),
    (2, "Force Field", "INTERRUPT"),
    (1, "Maul Strikes", "INTERRUPT"),
    (1, "Prepared Defenses", "INTERRUPT"),
]

# 23592 Quirin "el-diablo" Fuergut Unbeatable EBO aka fun for everyone
# YAML ! string tag stripped. YAML Fuergut without umlaut; encyclopedia dest
# Fürgut. Handle el-diablo wiki missing — cite on player page; do not mint
# redirect. [[Quirin Fürgut]] dump-not-stub pageid 22639 last=47564 UPDATE.
# Do NOT dest onto Echo Base Operations card pageid 3847 as player. Do NOT
# dest onto El-diablo. General dest TITLE (no named tournament; "bigger tourny"
# without name/finish — do not invent event row). Qty 60. AUOF inside Starting
# counts. Unnamed 10 shields dest 60 only. Starting Interrupt Heading For The
# Medical Frigate. Starting Effect An Unusual Amount Of Fear. Posted Objective
# NONE; Starting Card Echo Base Operations dested dual. Posted Imperial Barrier
# dested as published Dark card in Light 60 (CROSS_SIDE); Card Choices says
# author meant Rebel Barrier — dest 60 keeps Imperial Barrier. Posted D2 Wedge
# dested Wedge Antilles, Red Squadron Leader. Posted Echo War Room dested
# Hoth: Echo Command Center (War Room). Posted Nar Shadda dested Nar Shaddaa
# Wind Chimes. Posted Han&Chewie in Falcon dested Han, Chewie, And The Falcon.
# Posted Hoth Main Power Generators dested Hoth: Main Power Generators
# (1st Marker). Posted Hoth North Ridge dested Hoth: North Ridge (4th Marker).
# Skip GEMP (printed-only original-VS-era dest). Format Premiere - Original
# VS1 (26 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002).
FURGUT_LS = [
    (1, "Echo Base Operations / Special Modifications", "OBJECTIVE"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Hoth: Main Power Generators (1st Marker)", "LOCATION"),
    (1, "Hoth: North Ridge (4th Marker)", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Battle Plan & Draw Their Fire", "INTERRUPT"),
    (1, "Insurrection & Aim High", "INTERRUPT"),
    (1, "Squadron Assignments", "EFFECT"),
    (3, "Luke Skywalker, Jedi Knight", "CHARACTER"),
    (2, "Qui-Gon Jinn With Lightsaber", "CHARACTER"),
    (2, "Obi-Wan With Lightsaber", "CHARACTER"),
    (1, "Corran Horn", "CHARACTER"),
    (1, "Kal'Falnl C'ndros", "CHARACTER"),
    (1, "Wedge Antilles, Red Squadron Leader", "CHARACTER"),
    (1, "Keir Santage", "CHARACTER"),
    (2, "Baragwin", "CHARACTER"),
    (1, "Ishi Tib", "CHARACTER"),
    (2, "Han, Chewie, And The Falcon", "STARSHIP"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Spiral", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Red Squadron 7", "STARSHIP"),
    (1, "Luke's Lightsaber", "WEAPON"),
    (2, "X-Wing Laser Cannon", "WEAPON"),
    (2, "Bionic Hand", "DEVICE"),
    (2, "Intruder Missile", "DEVICE"),
    (1, "I'll Take The Leader", "ADMIRALS_ORDER"),
    (2, "Imperial Barrier", "INTERRUPT"),
    (3, "The Signal", "INTERRUPT"),
    (2, "On The Edge", "INTERRUPT"),
    (2, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (2, "Nar Shaddaa Wind Chimes", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (1, "Hyper Escape", "INTERRUPT"),
    (1, "Ice Storm", "EFFECT"),
    (1, "Bacta Tank", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "A New Secret Base", "EFFECT"),
    (1, "Hoth: Echo Command Center (War Room)", "LOCATION"),
    (1, "Hoth: Echo Docking Bay", "LOCATION"),
    (1, "Hoth: Echo Corridor", "LOCATION"),
    (1, "Hoth", "LOCATION"),
    (1, "Kiffex", "LOCATION"),
]

# 23571 jon "joker_phreak" manning Cloud City trooper deck
# YAML ! string tag stripped. YAML lowercase jon manning; encyclopedia dest
# Jon Manning. Handle joker_phreak wiki missing — cite on player page; do not
# mint redirect. Mint [[Jon Manning]] stub. Do NOT dest onto Cloud City
# Limited pageid 19997 as player. Do NOT dest onto Cloud City Trooper as
# player. Do NOT dest onto Boba Fett as player. General dest TITLE (no named
# tournament). Qty 60. Starting Interrupt Any Methods Necessary. Starting
# Effect omitted. Posted Objective NONE; Starting Card Cloud City: Dining
# Room. Posted Cloud CityDinning Room dested Cloud City: Dining Room.
# Posted Cloud CityCarbonite Chamber dested Cloud City: Carbonite Chamber.
# Posted Lando Calrisian dested Lando Calrissian (Dark). Posted Seargean
# Merril dested Sergeant Merril. Posted Storm Trooper Cadet dested
# Stormtrooper Cadet. Posted Den of Theives dested Den Of Thieves. Posted
# 4-Lom dested 4-LOM. Posted Boba Fett dested Cloud City Boba Fett. Unnamed
# shields dest 60 only (none posted). Skip GEMP (printed-only original-VS-era
# dest). Format Premiere - Original VS1 (25 May 2002; VS1 legal 9 Mar 2002;
# VS2 legal 1 Jun 2002).
MANNING_DS = [
    (1, "Cloud City: Dining Room", "LOCATION"),
    (1, "Cloud City: Carbonite Chamber", "LOCATION"),
    (1, "Cloud City: Chasm Walkway", "LOCATION"),
    (1, "Cloud City: Lower Corridor", "LOCATION"),
    (1, "Cloud City: Security Tower", "LOCATION"),
    (1, "Cloud City: Upper Plaza Corridor", "LOCATION"),
    (1, "4-LOM", "CHARACTER"),
    (1, "Boba Fett", "CHARACTER"),
    (1, "Chokk", "CHARACTER"),
    (1, "Chyler", "CHARACTER"),
    (3, "Cloud City Engineer", "CHARACTER"),
    (5, "Cloud City Trooper", "CHARACTER"),
    (1, "Darth Sidious", "CHARACTER"),
    (1, "General Tagge", "CHARACTER"),
    (2, "Imperial Commander", "CHARACTER"),
    (1, "Imperial Squad Leader", "CHARACTER"),
    (1, "Lando Calrissian", "CHARACTER"),
    (1, "Makurth", "CHARACTER"),
    (1, "Myo", "CHARACTER"),
    (1, "Rodian", "CHARACTER"),
    (1, "Sergeant Merril", "CHARACTER"),
    (1, "Stormtrooper Cadet", "CHARACTER"),
    (10, "Stormtrooper", "CHARACTER"),
    (1, "Trooper Jerrol Blendin", "CHARACTER"),
    (1, "Ugloste", "CHARACTER"),
    (3, "Abyssin Ornament", "INTERRUPT"),
    (2, "Alter", "INTERRUPT"),
    (1, "Any Methods Necessary", "INTERRUPT"),
    (1, "Control", "INTERRUPT"),
    (1, "Release Your Anger", "INTERRUPT"),
    (1, "Sacrifice", "INTERRUPT"),
    (1, "Sense", "INTERRUPT"),
    (5, "Trooper Assault", "INTERRUPT"),
    (1, "Dark Deal", "EFFECT"),
    (1, "Den Of Thieves", "EFFECT"),
    (1, "Reactor Terminal", "EFFECT"),
    (1, "Vader's Cape", "EFFECT"),
]

# 23567 Maximilien "Kiriel" Bouchard WYS Choke BETA
# YAML ! string tag stripped. Canonical [[Maximilien Bouchard]] dump-not-stub
# pageid 41729 from 24965 — UPDATE, do not mint. Handle Kiriel already a GPN
# stub pageid 41805 last=61234 with GPN dests [[Kiriel WYS Choke BETA]]
# 41804/61152, [[Kiriel AOBS old ALPHA]] 41806/61154, [[Kiriel Ice plains
# Regional 2nd place -- Watto Podrace Alpha]] 41870/61233. Redirect [[Kiriel]]
# → [[Maximilien Bouchard]] (Wedge231/Icebreath/HuntaWarya pattern). Do NOT
# dest 23567 onto the GPN dest title. Cite GPN dests in See also. Do NOT dest
# onto Watch Your Step as player. Do NOT dest onto Talon Karrde as player.
# Do NOT dest onto Wedge Antilles as player. General dest TITLE (Tournement
# 2-0 without event name). Qty 60. AUOF inside Starting (9) counts. Unnamed
# + (10 shield) dest 60 only. Starting Interrupt Heading For The Medical
# Frigate. Starting Effect An Unusual Amount Of Fear. Posted Watch Your
# Step/This place can Be a little Rough dested printed dual. Posted Tatooine
# (PR) dested Light Tatooine. Posted TatooineDocking Bay 94 dested Tatooine:
# Docking Bay 94. Posted TatooineCantina dested Tatooine: Cantina. Posted
# Squadren Assignments dested Squadron Assignments. Posted Han With Heavey
# Blaster Pistol dested Han With Heavy Blaster Pistol. Posted Threepio with
# His Parts Showing dested Threepio With His Parts Showing. Posted Millenium
# Falcon dested Millennium Falcon. Posted Red Squadren 1 dested Red Squadron
# 1. Posted R2 in R5 dested Artoo-Detoo In Red 5. Posted Goo Ney Tay dested
# Goo Nee Tay. Posted Ill Take the Leader dested I'll Take The Leader. Posted
# X-Wing Laser Cannon dested X-wing Laser Cannon. Posted Strike bloked dested
# Strike Blocked. Posted A Jedis Resilience dested A Jedi's Resilience.
# Posted Were are you looking for me ? dested Were You Looking For Me?. Skip
# GEMP (printed-only original-VS-era dest). Format Premiere - Original VS1
# (25 May 2002; VS1 legal 9 Mar 2002; VS2 legal 1 Jun 2002).
BOUCHARD_LS = [
    (1, "Watch Your Step / This Place Can Be A Little Rough", "OBJECTIVE"),
    (1, "Tatooine", "LOCATION"),
    (1, "Tatooine: Docking Bay 94", "LOCATION"),
    (1, "Tatooine: Cantina", "LOCATION"),
    (1, "Heading For The Medical Frigate", "INTERRUPT"),
    (1, "Squadron Assignments", "EFFECT"),
    (1, "Your Insight Serves You Well & Staging Areas", "EFFECT"),
    (1, "Battle Plan & Draw Their Fire", "EFFECT"),
    (1, "An Unusual Amount Of Fear", "EFFECT"),
    (1, "Kessel", "LOCATION"),
    (2, "Dash Rendar", "CHARACTER"),
    (1, "Mirax Terrik", "CHARACTER"),
    (2, "Melas", "CHARACTER"),
    (1, "Lando With Blaster Pistol", "CHARACTER"),
    (1, "Talon Karrde", "CHARACTER"),
    (1, "Wedge Antilles", "CHARACTER"),
    (2, "Han With Heavy Blaster Pistol", "CHARACTER"),
    (3, "Luke With Lightsaber", "CHARACTER"),
    (1, "Threepio With His Parts Showing", "CHARACTER"),
    (1, "Phylo Gandish", "CHARACTER"),
    (1, "Theron Nett", "CHARACTER"),
    (2, "Chewie, Enraged", "CHARACTER"),
    (1, "Millennium Falcon", "STARSHIP"),
    (1, "Outrider", "STARSHIP"),
    (1, "Red Squadron 1", "STARSHIP"),
    (1, "Red 10", "STARSHIP"),
    (1, "Artoo-Detoo In Red 5", "STARSHIP"),
    (1, "Revolution", "EFFECT"),
    (2, "Goo Nee Tay", "EFFECT"),
    (1, "Menace Fades", "EFFECT"),
    (1, "Honor Of The Jedi", "EFFECT"),
    (1, "I'll Take The Leader", "ADMIRAL'S ORDER"),
    (1, "Combined Fleet Action", "ADMIRAL'S ORDER"),
    (1, "X-wing Laser Cannon", "WEAPON"),
    (1, "Strike Blocked", "INTERRUPT"),
    (1, "On The Edge", "INTERRUPT"),
    (1, "Out Of Commission & Transmission Terminated", "INTERRUPT"),
    (2, "Rebel Barrier", "INTERRUPT"),
    (2, "A Jedi's Resilience", "INTERRUPT"),
    (2, "Life Debt", "INTERRUPT"),
    (1, "Houjix & Out Of Nowhere", "INTERRUPT"),
    (2, "Control & Tunnel Vision", "INTERRUPT"),
    (2, "The Bith Shuffle & Desperate Reach", "INTERRUPT"),
    (1, "Were You Looking For Me?", "INTERRUPT"),
    (1, "Sorry About The Mess & Blaster Proficiency", "INTERRUPT"),
    (1, "Too Close For Comfort", "INTERRUPT"),
    (1, "Dodge", "INTERRUPT"),
    (1, "We Wish To Board At Once", "INTERRUPT"),
]

# Posted Dark combo in a Light 60 (24807) or Light combo in a Dark 60 (24905).
CROSS_SIDE = {
    "Sense & Recoil In Fear": "LIGHT",
    "Sense & Uncertain Is The Future": "DARK",
    "Prepared Defenses": "DARK",
    "Imperial Barrier": "DARK",
}


def lookup_title(title: str, side: str) -> str:
    idx = cl._load_index()
    side_n = cl.norm_side(side)
    key = cl.lookup_key(title)
    cands = idx.get((side_n, key.casefold()), [])
    if cands:
        front = cands[0].get("front") or {}
        return cl.strip_uniqueness(front.get("title") or title)
    return title


def wiki_card(title: str, side: str) -> str:
    if title == "Another Pathetic Lifeform (Reflections III: A Collector's Bounty)":
        return cl.cardlink(
            title,
            "Ref3-L-anotherpatheticlifeform.gif",
            "Another Pathetic Lifeform",
        )
    if title in {"Ommni Box & It's Worse", "Omni Box & It's Worse"}:
        dest = "Ommni Box & It's Worse"
        return cl.cardlink(dest, "Ref2-D-ommnibox&itsworse.gif", "Omni Box & It's Worse")
    if title in ORIGINAL_VS:
        dest, img = ORIGINAL_VS[title]
        return cl.cardlink(dest, img, title)
    if title in {"U-3PO", "U-3PO (Yoo-Threepio)"}:
        dest = "U-3PO (Yoo-Threepio)"
        return cl.wrap(dest, side, dest=dest, label=dest)
    if title in {"Alter (Coruscant)", "Alter (Dark) (Coruscant)"}:
        if side.upper() in {"DARK", "DS"}:
            dest = "Alter (Dark) (Coruscant)"
            return cl.cardlink(dest, "Cor-D-alter.gif", dest)
        dest = "Alter (Coruscant)"
        return cl.cardlink(dest, "Cor-L-alter.gif", dest)
    if title in {"Bib Fortuna (Dark)", "Bib Fortuna (Reflections III)"}:
        return cl.cardlink("Bib Fortuna (Dark)", "Ref3-D-bibfortuna.gif", "Bib Fortuna")
    if title in {"Proton Torpedoes (Theed Palace)", "Proton Torpedoes (EP1)"}:
        return cl.cardlink(
            "Proton Torpedoes (Theed Palace)",
            "Theed-L-protontorpedoes.gif",
            "Proton Torpedoes",
        )
    if title in CROSS_SIDE:
        dest = title
        return cl.wrap(dest, CROSS_SIDE[title], dest=dest)
    resolved = lookup_title(title, side)
    dest = resolved
    if side.upper() in {"DARK", "DS"} and title in {
        "Alter",
        "Sense",
        "Control",
        "Jawa",
        "Tatooine",
        "Hoth",
        "Dagobah",
        "Endor",
        "Coruscant",
        "Naboo",
        "Bespin",
        "Lando Calrissian",
    }:  # Executor / Death Star / Cloud City exist only as Dark cards: plain titles (no "(Dark)" page)
        dest = f"{title} (Dark)"
        return cl.wrap(title, side, dest=dest, label=title)
    if " / " in dest:
        vis = dest.split(" / ", 1)[0]
        return cl.wrap(dest, side, dest=dest, label=vis)
    return cl.wrap(title, side, dest=dest)


def table_from_rows(rows: list[tuple[int, str, str]], side: str) -> str:
    order = [
        "Objective",
        "Character",
        "Creature",
        "Device",
        "Weapon",
        "Starship",
        "Vehicle",
        "Location",
        "Effect",
        "Interrupt",
        "Jedi Test",
        "Admiral's Order",
        "Epic Event",
        "Podracer",
        "Defensive Shield",
    ]
    cat_map = {
        "OBJECTIVE": "Objective",
        "CHARACTER": "Character",
        "CREATURE": "Creature",
        "DEVICE": "Device",
        "WEAPON": "Weapon",
        "STARSHIP": "Starship",
        "VEHICLE": "Vehicle",
        "LOCATION": "Location",
        "EFFECT": "Effect",
        "INTERRUPT": "Interrupt",
        "JEDI_TEST": "Jedi Test",
        "ADMIRALS_ORDER": "Admiral's Order",
        "EPIC_EVENT": "Epic Event",
        "PODRACER": "Podracer",
        "DEFENSIVE_SHIELD": "Defensive Shield",
    }
    qty: dict[tuple[str, str], int] = {}
    keys: list[tuple[str, str]] = []
    for q, title, cat in rows:
        heading = cat_map.get(cat, cat.title())
        k = (heading, title)
        if k not in qty:
            keys.append(k)
            qty[k] = 0
        qty[k] += q
    grouped: dict[str, list[tuple[int, str]]] = {}
    for heading, title in keys:
        grouped.setdefault(heading, []).append((qty[(heading, title)], title))
    ordered = [(h, grouped[h]) for h in order if h in grouped]
    for h, rows_h in grouped.items():
        if h not in order:
            ordered.append((h, rows_h))
    mid = (len(ordered) + 1) // 2

    def col(parts: list) -> str:
        chunks = []
        for heading, items in parts:
            chunks.append(f"'''{heading}'''")
            for q, name in items:
                chunks.append(f"* {q}x {wiki_card(name, side)}")
            chunks.append("")
        return "\n".join(chunks).rstrip()

    return (
        '{| class="wikitable" style="width:100%;"\n|-\n'
        f'| style="width:50%; vertical-align:top;" |\n{col(ordered[:mid])}\n'
        f'| style="width:50%; vertical-align:top;" |\n{col(ordered[mid:])}\n|}}'
    )


def slug_file(title: str) -> str:
    t = title.replace(" ", "_").replace(":", "_")
    t = t.replace("/", "_")
    return t + ".wiki"


def write_page(title: str, body: str) -> Path:
    PAGES.mkdir(exist_ok=True)
    path = PAGES / slug_file(title)
    if not body.endswith("\n"):
        body += "\n"
    path.write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    print("WROTE", path.name)
    return path


def print_lookups(rows: list[tuple[int, str, str]], side: str) -> None:
    n = 0
    for q, title, cat in rows:
        if title == "Another Pathetic Lifeform (Reflections III: A Collector's Bounty)":
            dest = title
            img = "Ref3-L-anotherpatheticlifeform.gif"
            print(f"  OK dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in ORIGINAL_VS:
            dest, img = ORIGINAL_VS[title]
            print(f"  OK dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in {"Ommni Box & It's Worse", "Omni Box & It's Worse"}:
            dest = "Ommni Box & It's Worse"
            img = "Ref2-D-ommnibox&itsworse.gif"
            print(f"  OK dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in {"U-3PO", "U-3PO (Yoo-Threepio)"}:
            dest = "U-3PO (Yoo-Threepio)"
            img = cl.image_for(dest, side)
            mark = "OK" if img else "NOIMG"
            print(f"  {mark} dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in {"Alter (Coruscant)", "Alter (Dark) (Coruscant)"}:
            if side.upper() in {"DARK", "DS"}:
                dest = "Alter (Dark) (Coruscant)"
                img = "Cor-D-alter.gif"
            else:
                dest = "Alter (Coruscant)"
                img = "Cor-L-alter.gif"
            print(f"  OK dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in {"Bib Fortuna (Dark)", "Bib Fortuna (Reflections III)"}:
            dest = "Bib Fortuna (Dark)"
            img = "Ref3-D-bibfortuna.gif"
            print(f"  OK dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in {"Proton Torpedoes (Theed Palace)", "Proton Torpedoes (EP1)"}:
            dest = "Proton Torpedoes (Theed Palace)"
            img = "Theed-L-protontorpedoes.gif"
            print(f"  OK dest={dest} file={img} {q}x {title}")
            n += q
            continue
        if title in CROSS_SIDE:
            dest = title
            side_x = CROSS_SIDE[title]
            img = cl.image_for(dest, side_x)
            mark = "OK" if img else "NOIMG"
            print(f"  {mark} dest={dest} file={img} side={side_x} {q}x {title}")
            n += q
            continue
        resolved = lookup_title(title, side)
        img = cl.image_for(title, side) or cl.image_for(resolved, side)
        mark = "OK" if img else "NOIMG"
        if resolved != title:
            mark += f" dest={resolved}"
        print(f"  {mark} {q}x {title}")
        n += q
    print("QTY", n)


def original_post(post_id: int) -> str:
    """Dump the archived DeckTech post after the dest 60."""
    raw = (POSTS / f"{post_id}.txt").read_text(encoding="utf-8")
    if "</nowiki>" in raw:
        raw = raw.replace("</nowiki>", "&lt;/nowiki&gt;")
    return (
        "== Original post ==\n\n"
        '<div style="white-space:pre-wrap"><nowiki>\n'
        f"{raw.rstrip()}\n"
        "</nowiki></div>"
    )


def _field(raw: str, name: str) -> str:
    m = re.search(rf"^\s*{name}:\s*(.+)$", raw, re.M)
    return m.group(1).strip() if m else ""


def split_dt_post(post_id: int) -> dict[str, str]:
    raw = (POSTS / f"{post_id}.txt").read_text(encoding="utf-8")
    lower = raw.lower()
    cards_at = lower.find("cards:")
    strat_at = lower.find("strategy:")
    cards = ""
    strategy = ""
    if cards_at >= 0 and strat_at > cards_at:
        cards = raw[cards_at + len("Cards:") : strat_at]
        strategy = raw[strat_at + len("Strategy:") :]
    elif strat_at >= 0:
        strategy = raw[strat_at + len("Strategy:") :]
    cards = cards.strip().strip("'‘’`").strip()
    strategy = strategy.strip().strip("'‘’`").strip()
    return {
        "title": _field(raw, "Title"),
        "author": _field(raw, "Author"),
        "date": _field(raw, "Date"),
        "rating": _field(raw, "Rating"),
        "cards": cards,
        "strategy": strategy,
    }


def wiki_strategy(text: str) -> str:
    headings = {
        "WYS",
        "Combat",
        "QMC",
        "The Lingrell Tech",
        "Character Selection",
        "Interrupts & Effects",
        "Activation",
        "Winning",
        "Cards I would like to add",
        "Props to",
        "Props go to",
        "Senate",
        "Hunt Down",
        "Watto",
        "Dark Deal",
        "Anything Else",
        "Card Choices",
        "Fear Will Keep Them in Line",
        "Bring Him",
        "Lightsaber Combat",
        "Match-Ups",
        "Match-ups",
        "Response",
        "End Response",
        "RESPONSE TO REVIEW",
        "RESPONSE TO REVIEWS",
        "END RESPONSE",
        "END RESPONSES",
        "PRE GAME",
        "START",
        "EARLY",
        "MID",
        "END",
        "MWYHL",
        "MAINS",
        "SENATE",
        "LSC",
        "EBO",
        "Profit",
        "The Start",
        "Brief Matchups",
        "Echo Base Operations",
        "Hidden Base Flip",
        "Mains of any kind",
        "Rebel Strike Team",
        "Where is Blizzard 4?",
        "Why only two ships?",
        "Isn't that kind of a lot of effects?",
        "EDIT",
        "END EDIT",
        "Coruscant  Jedi Council Chamber",
        "Coruscant Jedi Council Chamber",
        "Naboo  Battle Plains",
        "Naboo Battle Plains",
        "Spaceport Docking Bay",
        "Jar Jar Binks",
        "Leia with Blaster Rifle",
        "Owen Lars & Beru Lars",
        "Phylo Gandish",
        "Alter (Coruscant)",
        "On the Edge",
        "A Vergence in the Force",
        "Projection of a Skywalker",
        "Sando Aqua Monster",
        "Introduction",
        "How to play it",
        "How does V3 affect this deck?",
        "Some card choices",
        "Some match-ups",
        "Some questions and answers",
        "Conclusion",
        "Interrupts",
        "Characters",
        "Effects",
        "Starships/Vehicles",
        "Locations",
        "Changes I would make",
        "Strat",
        "Card Selection",
        "Tech and other random goodness",
        "Matchups",
        "Matchups (with record vs)",
        "response to reviews",
        "Response to reviews",
        "End response to reviews",
        "Mid Game",
        "Late Game",
        "Why no space?",
        "Hunt Down And Destroy The Jedi",
        "Bring Him Before Me",
        "Big Blue of any kind",
        "No Money, No Parts, No Deal",
        "Agents Of The Black Sun",
        "Walker Garrison",
        "Dark Senate",
        "Dark Side Combat",
        "Early Game",
        "Starting setup",
        "Early game",
        "Later game",
        "Additional strategy for beating space decks",
        "Specific Card Choices",
        "Inconsequential barriers -",
        "Inconsequential barriers",
        "Coruscant Alter -",
        "Coruscant Alter",
        "Tendau bendon -",
        "Tendau bendon",
        "Horox -",
        "Horox",
        "Senator Palpatine -",
        "Senator Palpatine",
        "Queen Amidala -",
        "Queen Amidala",
        "Mid game",
        "Late game",
        "Mains",
        "Mains (1-0)",
        "QMC (1-0)",
        "Profit (0-1 with loss by 11 against Pat Ziagos)",
        "LSC (1-0)",
        "LS Senate (1-1 with loss by 15 against a Twigg)",
        "Space",
        "Why Colo Claw Fish as your 4th starting effect??",
        "LS Senate",
        "LS LSC",
        "Straight mains of any kind",
        "Space decks",
        "No Coruscant Guard?",
        "Arica instead of Keder?",
        "Sense kombo x3",
        "AAA",
        "Limited Resources",
        "Senator selection",
        "Emperor & Sidious",
        "Shut Him Up Or Shut Him Down",
        "Begin Landing Your Troops",
        "Responses to Reviews",
        "Deck Matchups",
        "Matchup",
        "WHY ??",
        "Ground deck (profit, Throne main, We have a plan)",
        "2nd 8D8",
        "No 2nd Prisoner 2187?",
        "Gold Leader",
        "First Aid",
        "Alter lost",
        "3 Too Close For Comfort and only 1 We Wish To Board?",
        "Where is Honor?",
        "Agents of Black Sun",
        "Walker Garrison/Dark Deal",
        "Court Mains or Scum",
        "LSC",
        "Bring Him Before Me and Hunt Down",
        "Updates",
        "End Updates",
        "read this amazing idea (thx alex for the genial style)",
        "Early",
        "UDDATE",
        "UDDATE.",
        "Note",
        "Easy",
        "Intricities",
        "MID/LATE game",
        "Were Doomed",
        "Leias blaster",
        "Were you looking for Me?",
        "Monk",
        "Goo Nee Tay",
        "Coruscant DB",
        "JCC/Yoda/Alter",
        "Honor",
        "Sense/UITF",
        "Non-combo TV",
        "Non-combo TV.",
        "OTE",
        "Bacta tank",
        "We Wish To Board At Once",
        "Sense & Alter",
        "Twix locations",
        "12 senators",
        "Rune Haako + Yeb Yeb x2",
        "Elis Helrot",
        "Okay, time for the matchups",
        "Quiet Mining Colony",
        "Watch Your Step",
        "Hidden Base or EBO",
        "UPDATE 8/20/02",
        "UPDATE 8/6/02",
        "UPDATE 7/30/02",
        "END UPDATE",
        "vs. Senate",
        "vs. Watch Your Step",
        "vs. Saber Combat",
        "vs. others",
        "Some card explanations",
        "How to handle different decks?",
        "LS-Combat",
        "Main & Toys",
        "Vader(V)",
        "The Empires Back(V)",
        "Malastare+Wattos Box",
        "Commander Praji(V)",
        "Sidious and Emperor",
        "vs. Combat",
        "vs. Duelling Hunt Down",
        "vs. ISB Scum",
        "vs. Dark Deal",
        "vs. Walkers",
        "UPDATE #1",
        "UPDATE #2",
        "Match ups",
        "Hunt down",
        "The Shields",
        "Characters choices",
        "Now for favorite decks types",
        "Edit 2",
        "On opponents turn",
        "1st turn",
        "2nd turn to mid game",
        "End of Mid game to Late Game",
        "Final Update",
        "End Update",
        "Update 2",
        "End Update 2",
        "Update 3",
        "Update 4",
        "BHBM",
        "Walkers",
        "Dark Combat",
        "Invasion",
        "SOme card choices",
        "First turn",
        "second turn",
        "Against some decks",
        "HUnt down",
        "Droids",
        "Hoth",
        "senate ties",
        "play any defensive shields you want",
        "Under Attack",
        "Capital Support",
        "Honor of the Jedi",
        "Close Air Support",
        "During Opponents turn",
        "2nd turn",
        "Vs Pile (yes its alive in my area)",
        "Vs WYS",
        "Vs lightsaber combat",
        "Some card choices",
        "why jedi's homes, yodas home and rendevous point?",
        "Why no other han?",
        "WHy no ships?",
        "master luke?",
        "WHy no tat. qui gon?",
        "First couple of turns",
        "Some decks vs this.",
        "Dark deal on speed",
        "senate",
        "droids",
        "Thank you",
        "Dark deal",
        "Court and Scum",
        "SYCFA or whatever",
        "OPS and stuff",
        "STARTING",
        "WHY RACING?",
        "GENERAL STRATEGY",
        "MATCHUPS",
        "AVOIDANCE",
        "NON-AVOIDANCE",
        "AGRESSIVE",
        "FEEDBACK",
        "END FEEDBACK",
        "CARD CHOICES",
        "CARD CHOICES'",
        "JEDIGAMBLER'S NOTE",
        "JEDIGAMBLER’S NOTE",
        "END OF JEDIGAMBLER'S NOTE",
        "END OF JEDIGAMBLER’S NOTE",
        "RESPONSE TO REVIEWS",
        "END OF RESPONSE",
        "STRATEGY SECTION",
        "SOME CARD CHOICES",
        "FIRST TURN",
        "Card choices",
        "The Background",
        "The Idea",
        "The Strategy",
        "The End",
        "Masterful Move, holotable",
        "P-59 x2 and wounded warrior",
        "Always Tinking With Your Stomach",
        "Omni Box & It's Worse x2",
        "Circle",
        "Maul Strikes x2",
        "Overload",
        "Shut Him up or shut him down",
        "Furry Fury",
        "Security Precautions",
        "Restraining Bolt",
        "Hyperdrive",
        "HB flip",
        "The pile",
        "Throne Room",
        "MWHL flip",
        "[EDIT #1] Respsonse to Reviews",
        "[END EDIT #1]",
        "Lets go with some card choices that may seem strange",
        "Choices",
        "Imperial Holotable",
        "P-59 x3",
        "Maul's Ship",
        "Maul’s Ship",
        "Padme",
        "Obi",
        "Joh Yowza",
        "Lightsabers",
        "Run luke, run",
        "Artoo i have a bad feeling about this",
        "Life debt",
        "Weapon levitation",
        "Blaster deflection",
        "Eject, eject",
        "Saber profiencey",
        "Early Game",
        "Starting setup",
        "Early game",
        "Later game",
        "Additional strategy for beating space decks",
        "Specific Card Choices",
        "Inconsequential barriers -",
        "Inconsequential barriers",
        "Coruscant Alter -",
        "Coruscant Alter",
        "Tendau bendon -",
        "Tendau bendon",
        "Horox -",
        "Horox",
        "Senator Palpatine -",
        "Senator Palpatine",
        "Queen Amidala -",
        "Queen Amidala",
        "Early Deploy",
        "It's a Trap-",
        "It's a Trap",
        "It’s a Trap-",
        "It’s a Trap",
        "Caldera Righim-",
        "Caldera Righim",
        "General Solo-",
        "General Solo",
        "Lost in the Wilderness-",
        "Lost in the Wilderness",
        "Don't Get @#$%y-",
        "Don't Get @#$%y",
        "Don’t Get @#$%y-",
        "Don’t Get @#$%y",
        "Do, or Do Not-",
        "Do, or Do Not",
        "Black Sun",
        "Carbon Chamber Testing",
        "SYCFA",
        "Early",
        "Mid",
        "Mid Game",
        "End Game",
        "Card Explanations",
        "Broken Concentration",
        "Were The Bait",
        "No System?",
        "Some Cards I Want to add",
        "Zuckuss + 4-LOM + Boba Fett, BH",
        "Zuckuss + 4-LOM + Boba Fett, BH =",
        "Weapon Levitation-",
        "Weapon Levitation",
        "Imperial Barrier",
        "Rancor",
        "Against . . .",
        "Hidden Base",
        "Quite Mining Colony",
        "Mind What You Have Learned",
        "Matchups",
        "HDJTJ",
        "LCS",
        "Senete",
        "Endor Ops",
        "ISB",
        "HB/EBO",
        "MWYHL",
        "Early game",
        "Mid game",
        "Late game",
        "Card choices",
        "The Background",
        "The Idea",
        "The Strategy",
        "The End",
        "UPDATE",
        "Edit",
        "vs. WYS",
        "vs. QMC",
        "vs. HB",
        "vs. EBO",
        "vs. TRM or any versoin of it.",
        "deck strat errata",
        "Turn 1.",
        "Turn 2.",
        "Turn 3.",
        "strategy",
        "here are some cards explanations",
        "why Rebel Artillery?",
        "why Double Agent?",
        "why Were You Looking For Me?",
        "why Seeking An Audience and Underworld Contacts?",
        "Starting",
        "Late Game",
        "Interupts",
        "TIEs",
        "TIEs-",
        "LSC-",
        "Dark Deal or Walkers",
        "End Edit",
        "Starting Setup",
        "Later Game",
        "Explanation of Card Choices",
        "How to play the deck...",
        "How to play the deck",
        "Force field",
        "Force Field",
        "I Have You Now",
        "Maul Strikes",
        "Qui-Gon's End",
        "Qui-Gon’s End",
        "Prophetess",
        "2 Masterful Moves, & 2 accelerates",
        "Janus/Blow Parried",
        "Possible card additions",
        "Update",
        "Destiny Layout",
        "Tournement  2-0",
        "Respond to Garion",
        "Combined fleet action",
        "Revolution This card win me many game",
        "Why Colo Claw Fish?",
        "Why Unsalvageable ?",
        "strat",
        "Why Alter?",
        "DECK EDIT",
        "DECK EDIT 2",
        "DECK EDIT 3",
        "Why Akbar?",
        "EDIT Response to reviews",
        "EDIT Why arent these cards here??",
        "Card explanations",
        "Projections of a skywalker/endor celebration/menace fades",
        "Home one/defiance",
        "roche/kashyyyk",
        "Endor great forest",
        "H’nemthe",
        "H'nemthe",
        "LS, RS",
        "Corran Horn",
        "==>Why isnt insertion planning in here?<==",
        "1st Turn",
        "Why Endor Ops as opposed to ISB?",
        "Now for some card choices",
        "Editor’s note 5/26",
        "Editor's note 5/26",
        "Editor’s note 5/20",
        "Editor's note 5/20",
        "Specifics",
        "Scanning Crew",
        "Emperor Palpatine",
        "Naboo DBay",
        "He Hasn't Come Back Yet",
        "oops senator palpatine not senator valorum",
    }
    prefix_heads = {
        "Senate",
        "Combat",
        "Hunt Down",
        "Hunt down",
        "Hunt Down-",
        "Watto",
        "Dark Deal",
        "Dark deal",
        "Dark Deal-",
        "BHBM-",
        "Walkers-",
        "Dark Combat-",
        "Invasion-",
        "Final Update",
        "End Update",
        "Update 2",
        "End Update 2",
        "Update 3",
        "Update 4",
        "SOme card choices",
        "First turn",
        "second turn",
        "Against some decks",
        "HUnt down",
        "Droids",
        "Hoth",
        "senate ties",
        "play any defensive shields you want",
        "Under Attack",
        "Under Attack -",
        "Capital Support",
        "Capital Support -",
        "Honor of the Jedi",
        "Honor of the Jedi -",
        "Close Air Support",
        "Close Air Support -",
        "During Opponents turn",
        "2nd turn",
        "Vs Pile (yes its alive in my area)",
        "Vs WYS",
        "Vs lightsaber combat",
        "Some card choices",
        "why jedi's homes, yodas home and rendevous point?",
        "Why no other han?",
        "WHy no ships?",
        "master luke?",
        "WHy no tat. qui gon?",
        "First couple of turns",
        "Some decks vs this.",
        "Dark deal on speed-",
        "Dark deal on speed",
        "Combat-",
        "senate-",
        "droids-",
        "Hunt down-",
        "senate",
        "droids",
        "Thank you",
        "Response to reviews",
        "End response to reviews",
        "Why no space?",
        "Blaster Deflection",
        "Clash Of Sabers",
        "Mantellian Savrip",
        "Tunnel Vision",
        "Hunt Down And Destroy The Jedi",
        "Bring Him Before Me",
        "Big Blue of any kind",
        "No Money, No Parts, No Deal",
        "Agents Of The Black Sun",
        "Walker Garrison",
        "Dark Senate",
        "Dark Side Combat",
        "Mid Game",
        "Late Game",
        "Match ups",
        "Court and Scum",
        "SYCFA or whatever",
        "OPS and stuff",
        "UPDATE #2",
        "Anything Else",
        "Lightsaber Combat",
        "Echo Base Operations",
        "Hidden Base Flip",
        "Mains of any kind",
        "Rebel Strike Team",
        "Jedi Luke-",
        "Two stick swing people-",
        "Endor sites-",
        "Home one-",
        "Combat (of course)-",
        "On opponents turn",
        "1st turn",
        "2nd turn to mid game",
        "End of Mid game to Late Game",
        "No combo for out of commissions? –",
        "No combo for out of commissions? -",
        "Quiet Mining Colony",
        "Watch Your Step",
        "Bring Him Before Me and Hunt Down",
        "Bring Him",
        "LS Senate -",
        "LS Senate",
        "LS LSC",
        "LS-Combat",
        "Main & Toys",
        "Vader(V)",
        "The Empires Back(V)",
        "Malastare+Wattos Box",
        "Commander Praji(V)",
        "Sidious and Emperor",
        "Blizzard 4",
        "Darth Maul",
        "Where is Put All Sections On Alert? -",
        "Others",
        "Profit",
        "Lightsaber Combat -",
        "Quiet Mining Colony -",
        "Watch Your Step -",
        "Hidden Base or EBO -",
        "LSC -",
        "LSC",
        "WYS -",
        "QMC -",
        "QMC",
        "2nd 8D8",
        "No 2nd Prisoner 2187?",
        "Gold Leader",
        "First Aid",
        "Alter lost",
        "3 Too Close For Comfort and only 1 We Wish To Board?",
        "Where is Honor?",
        "Agents of Black Sun",
        "Walker Garrison/Dark Deal",
        "Court Mains or Scum",
        "Deck Matchups",
        "Space deck",
        "Matchup",
        "Match-ups",
        "MatchUps -",
        "MatchUps",
        "Ships -",
        "Combat -",
        "UDDATE.",
        "UDDATE",
        "MID/LATE game-",
        "MID/LATE game",
        "Were Doomed -",
        "Were Doomed",
        "Note",
        "Leias blaster",
        "Were you looking for Me?",
        "Monk-",
        "Monk",
        "Goo Nee Tay....",
        "Goo Nee Tay",
        "Coruscant DB-",
        "Coruscant DB",
        "JCC/Yoda/Alter-",
        "JCC/Yoda/Alter",
        "Honor-",
        "Honor",
        "Sense/UITF",
        "Non-combo TV.",
        "Non-combo TV",
        "OTE-",
        "OTE",
        "Bacta tank-",
        "Bacta tank",
        "We Wish To Board At Once-",
        "We Wish To Board At Once",
        "Easy",
        "Intricities",
        "Early",
        "AVOIDANCE",
        "NON-AVOIDANCE",
        "AGRESSIVE",
        "Mr. Cheese",
        "Luca",
        "Bean2213",
        "Hayes",
        "FIRST TURN-",
        "-to Armaedes-",
        "-to Ithorian-",
        "-to bounty22-",
        "-Battle Deployment-",
        "-Graga-",
        "to Armaedes",
        "to Ithorian",
        "to bounty22",
        "Battle Deployment",
        "Graga",
        "---Fett Lord-",
        "---CGogolen-",
        "---Capt Paelleon-",
        "---217-",
        "--Nute Gunray and Rune Haako-",
        "--Only 1 Barrier?-",
        "--Shut Him Up Or Shut Him Down-",
        "--Unsalvageable-",
        "--QMC-",
        "--RST-",
        "--WYS-",
        "--Y4 Mains-",
        "Padme -",
        "Padme",
        "Obi -",
        "Joh Yowza -",
        "Joh Yowza",
        "Lightsabers -",
        "Lightsabers",
        "Run luke, run -",
        "Run luke, run",
        "Artoo i have a bad feeling about this -",
        "Artoo i have a bad feeling about this",
        "Life debt -",
        "Life debt",
        "Weapon levitation -",
        "Weapon levitation",
        "Blaster deflection -",
        "Blaster deflection",
        "Eject, eject -",
        "Eject, eject",
        "Saber profiencey -",
        "Saber profiencey",
        "Early Game",
        "Starting setup",
        "Early game",
        "Later game",
        "Additional strategy for beating space decks",
        "Specific Card Choices",
        "Inconsequential barriers -",
        "Inconsequential barriers",
        "Coruscant Alter -",
        "Coruscant Alter",
        "Tendau bendon -",
        "Tendau bendon",
        "Horox -",
        "Horox",
        "Senator Palpatine -",
        "Senator Palpatine",
        "Queen Amidala -",
        "Queen Amidala",
        "Early Deploy",
        "It's a Trap-",
        "It's a Trap",
        "It’s a Trap-",
        "It’s a Trap",
        "Caldera Righim-",
        "Caldera Righim",
        "General Solo-",
        "General Solo",
        "Lost in the Wilderness-",
        "Lost in the Wilderness",
        "Don't Get @#$%y-",
        "Don't Get @#$%y",
        "Don’t Get @#$%y-",
        "Don’t Get @#$%y",
        "Do, or Do Not-",
        "Do, or Do Not",
        "Black Sun",
        "Carbon Chamber Testing",
        "SYCFA",
        "Early",
        "Mid",
        "Mid Game",
        "End Game",
        "Card Explanations",
        "Broken Concentration",
        "Were The Bait",
        "No System?",
        "Some Cards I Want to add",
        "Zuckuss + 4-LOM + Boba Fett, BH",
        "Zuckuss + 4-LOM + Boba Fett, BH =",
        "Weapon Levitation-",
        "Weapon Levitation",
        "Imperial Barrier",
        "Rancor",
        "Hidden Base -",
        "Quite Mining Colony -",
        "Mind What You Have Learned -",
        "Against . . .",
        "Matchups",
        "Matchups (with record vs)",
        "response to reviews",
        "Mains (1-0)",
        "QMC (1-0)",
        "Profit (0-1 with loss by 11 against Pat Ziagos)",
        "LSC (1-0)",
        "LS Senate (1-1 with loss by 15 against a Twigg)",
        "Mains",
        "Space",
        "Unsalvageable",
        "Shut Him Up Or Shut Him Down",
        "HDJTJ-",
        "LCS-",
        "Court-",
        "Senete-",
        "Endor Ops-",
        "ISB-",
        "HB/EBO",
        "MWYHL",
        "Profit-",
        "Early game",
        "Mid game",
        "Late game",
        "Card choices",
        "The Background",
        "The Idea",
        "The Strategy",
        "The End",
        "Early game-",
        "Mid game-",
        "Late game-",
        "Card choices-",
        "Locations -",
        "Characters -",
        "Interrupts -",
        "Effects -",
        "vs. WYS",
        "vs. QMC",
        "vs. HB",
        "vs. EBO",
        "vs. TRM or any versoin of it.",
        "vs. TRM",
        "deck strat errata",
        "Turn 1.",
        "Turn 2.",
        "Turn 3.",
        "***-6/28",
        "***-6/14",
        "strategy",
        "here are some cards explanations",
        "why Rebel Artillery?",
        "why Double Agent?",
        "why Were You Looking For Me?",
        "why Seeking An Audience and Underworld Contacts?",
        "Starting",
        "Late Game",
        "Locations",
        "Characters",
        "Space",
        "Effects",
        "Interupts",
        "TIEs-",
        "LSC-",
        "Dark Deal or Walkers",
        "another pathetic lifeform-",
        "the new virtual saber puller-",
        "scrambled transmission-",
        "Kessel-",
        "obi-wan, jedi knight-",
        "luke with lightsaber-",
        "yoda, master of the force-",
        "baragwin x2-",
        "thrown back-",
        "bacta tank-",
        "fall of the legend + throw me another charge-",
        "Starting Setup",
        "Later Game",
        "Explanation of Card Choices",
        "Force field -",
        "Force Field -",
        "I Have You Now -",
        "Maul Strikes -",
        "Qui-Gon's End -",
        "Qui-Gon’s End -",
        "Prophetess -",
        "2 Masterful Moves, & 2 accelerates -",
        "Janus/Blow Parried -",
        "Possible card additions -",
        "How to play the deck...",
        "How to play the deck",
        "Respond to Garion",
        "Combined fleet action",
        "Senator Tie",
        "AOBS",
        "DECK EDIT 3",
        "DECK EDIT 2",
        "DECK EDIT",
        "Why Akbar?",
        "-Bean",
        "-Garion",
        "-Shadow 13",
        "-Hardpack",
        "Why Endor Ops as opposed to ISB?",
        "Editor’s note 5/26",
        "Editor's note 5/26",
        "Editor’s note 5/20",
        "Editor's note 5/20",
        "Now for some card choices",
        "Guri",
        "Bane Malar",
        "Prophetess (virtual)",
        "Thrawn",
        "Black 2 (virtual)",
        "Stinger",
        "Stunning Leader",
        "Dark Maneuvers & Tallon Roll",
        "MM & Endor Celebration",
        "Overload",
        "Specifics",
        "Scanning Crew-",
        "Scanning Crew",
        "Emperor Palpatine-",
        "Emperor Palpatine",
        "Naboo DBay-",
        "Naboo DBay",
        "Walker Garrison-",
        "He Hasn't Come Back Yet-",
        "He Hasn't Come Back Yet",
        "oops senator palpatine not senator valorum",
    }
    chunks = []
    buf: list[str] = []
    for line in text.splitlines():
        s = line.strip().strip("'‘’`")
        s = s.strip("*").strip()
        if s and set(s) <= set("=*-_| "):
            continue
        if not s:
            if buf:
                chunks.append(" ".join(buf))
                buf = []
            continue
        s_head = s.strip("- ").strip()
        if s_head in headings and not buf:
            chunks.append(("h", s_head))
            continue
        hit = None
        rest = ""
        for h in sorted(prefix_heads, key=len, reverse=True):
            if buf:
                break
            if s.startswith(h + " "):
                maybe = s[len(h) :].strip()
                if maybe and (
                    maybe[0].isupper()
                    or maybe[0].isdigit()
                    or h == "OPS and stuff"
                    or h == "2nd turn to mid game"
                    or h == "First turn"
                    or h == "second turn"
                    or h == "HUnt down"
                    or h == "Droids"
                    or h == "Hoth"
                    or h == "senate ties"
                    or h == "During Opponents turn"
                    or h == "Mid Game"
                    or h == "Vs lightsaber combat"
                    or h == "WHy no ships?"
                    or h == "master luke?"
                    or h == "WHy no tat. qui gon?"
                    or h == "senate"
                    or h == "droids"
                ):
                    hit = h
                    rest = maybe
                    break
            if h.endswith(("-", ".", "…")) and s.startswith(h):
                maybe = s[len(h) :].strip()
                if maybe:
                    hit = h
                    rest = maybe
                    break
        if hit:
            chunks.append(("h", hit))
            if rest:
                buf.append(rest)
            continue
        buf.append(s)
    if buf:
        chunks.append(" ".join(buf))
    out: list[str] = []
    for item in chunks:
        if isinstance(item, tuple) and item[0] == "h":
            out.append(f"==== {item[1].rstrip('-=').strip()} ====\n")
        else:
            out.append(item)
            out.append("")
    body = "\n".join(out).rstrip() + "\n"
    return body.replace("*g*", "<nowiki>*g*</nowiki>")


def formatted_original_post(post_id: int, *, description: str = "") -> str:
    """Readable original post: metadata + strategy, Cards collapsed by default."""
    p = split_dt_post(post_id)
    cards = p["cards"]
    if "</nowiki>" in cards:
        cards = cards.replace("</nowiki>", "&lt;/nowiki&gt;")
    desc = f"* '''Description:''' {description}\n" if description else ""
    return (
        "== Original post ==\n\n"
        f"'''{p['title']}'''\n"
        f"* '''Author:''' {p['author']}\n"
        f"* '''Published:''' {p['date']}\n"
        f"* '''Rating:''' {p['rating']}\n"
        f"{desc}\n"
        "=== Strategy ===\n\n"
        f"{wiki_strategy(p['strategy'])}\n"
        "=== Original card list ===\n\n"
        '{| class="wikitable mw-collapsible mw-collapsed" style="width:100%" '
        'data-expandtext="Show" data-collapsetext="Hide"\n'
        "|+ As posted on DeckTech\n"
        "|-\n"
        '| <div style="white-space:pre-wrap"><nowiki>\n'
        f"{cards}\n"
        "</nowiki></div>\n"
        "|}\n"
    )


def shaw_ds_page() -> str:
    start = wiki_card("Hunt Down And Destroy The Jedi", "DARK")
    return f"""'''{SHAW_DS_TITLE}''' is the [[Dark]] constructed list [[Greg Shaw]] posted on DeckTech after finishing 2nd at the [[2002 World Championship]].{post_ref("dt-26555", 26555, "Force Lightning is TECH", 'Greg "TychoCelchu" Shaw, 10 December 2002')}

== Deck info ==
* '''Player:''' [[Greg Shaw]]
* '''Event:''' [[2002 World Championship]]
* '''Stage:''' Published lists
* '''Finish:''' 2
* '''Published:''' 10 December 2002 (DeckTech)
* '''Published title:''' ''Force Lightning is TECH''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}

== Decklist ==

{table_from_rows(SHAW_DS, "DARK")}

{formatted_original_post(26555, description="Solid Hunt Down that took 2nd at Worlds")}

== See also ==

* [[2002 World Championship]]
* [[Greg Shaw]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26555, "Force Lightning is TECH")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:2002]]
"""


def consoli_ds_page() -> str:
    start = wiki_card("No Money, No Parts, No Deal!", "DARK")
    fima = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in CONSOLI_FIMA
    )
    return f"""'''{CONSOLI_DS_TITLE}''' is the [[Dark]] constructed list [[Angelo Consoli]] posted on DeckTech after winning the [[2002 World Championship]].{post_ref("dt-26297", 26297, "DeckTech post 26297", 'Angelo "GravShadow" Consoli, 19 November 2002')}

== Deck info ==
* '''Player:''' [[Angelo Consoli]]
* '''Event:''' [[2002 World Championship]]
* '''Stage:''' Published lists
* '''Finish:''' 1
* '''Published:''' 19 November 2002 (DeckTech)
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' Watto

== Decklist ==

{table_from_rows(CONSOLI_DS, "DARK")}

== Held by Fear Is My Ally ==

{wiki_card("Fear Is My Ally", "DARK")} holds these ten cards from outside the deck. They do not count toward the 60.

{fima}

{formatted_original_post(26297, description="This is a repost of my watto-deck that won worlds. Somehow the first post appeared in the limited section.")}

== See also ==

* [[2002 World Championship]]
* [[Angelo Consoli]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26297, "DeckTech post 26297")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:2002]]
"""


def shaw_ls_page() -> str:
    start = wiki_card("There Is Good In Him", "LIGHT")
    return f"""'''{SHAW_LS_TITLE}''' is the [[Light]] constructed list [[Greg Shaw]] posted on DeckTech after finishing 2nd at the [[2002 World Championship]].{post_ref("dt-26204", 26204, "DCon2k2 Runner Up - LS", 'Greg "TychoCelchu" Shaw, 11 November 2002')}

== Deck info ==
* '''Player:''' [[Greg Shaw]]
* '''Event:''' [[2002 World Championship]]
* '''Stage:''' Published lists
* '''Finish:''' 2
* '''Published:''' 11 November 2002 (DeckTech)
* '''Published title:''' ''DCon2k2 Runner Up - LS''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")} · {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("Merc Sunlet", "LIGHT")}
* '''Strategy:''' There Is Good In Him (variable start)

== Decklist ==

{table_from_rows(SHAW_LS, "LIGHT")}

{formatted_original_post(26204, description="Repost so more people can see it. TIGIH with some mean tech to deliver huge beats.")}

== See also ==

* [[2002 World Championship]]
* [[Greg Shaw]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26204, "DCon2k2 Runner Up - LS")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:2002]]
"""


def wata_ls_page() -> str:
    start = wiki_card("There Is Good In Him", "LIGHT")
    return f"""'''{WATA_LS_TITLE}''' is the [[Light]] constructed list [[Keith Watabayashi]] posted on DeckTech from Day 2 of the [[2002 World Championship]]. [[Brad Reinhold]] also played the list that day.{post_ref("dt-26273", 26273, "The other TIGIH at Deciphercon", 'Keith "Gen" Watabayashi, 17 November 2002')}

== Deck info ==
* '''Player:''' [[Keith Watabayashi]]
* '''Event:''' [[2002 World Championship]]
* '''Stage:''' Day 2
* '''Finish:''' Day 2
* '''Published:''' 17 November 2002 (DeckTech)
* '''Published title:''' ''The other TIGIH at Deciphercon''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")} · {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' There Is Good In Him (variable start)

== Decklist ==

{table_from_rows(WATA_LS, "LIGHT")}

{formatted_original_post(26273, description="The beats deck me and Brad Reinhold played on Day 2 of worlds. Read the my TR to see how it did.")}

== See also ==

* [[2002 World Championship]]
* [[Keith Watabayashi]] · [[Brad Reinhold]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26273, "The other TIGIH at Deciphercon")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:2002]]
"""


def krueger_ls_page() -> str:
    start = wiki_card("Coruscant: Jedi Council Chamber", "LIGHT")
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in KRUEGER_SHIELDS
    )
    return f"""'''{KRUEGER_LS_TITLE}''' is the [[Light]] constructed list [[Kyle Krueger]] posted on DeckTech from both Day 1s of the [[2002 World Championship]].{post_ref("dt-26173", 26173, "It's a Kyle deck", 'Kyle "Meto" Krueger, 8 November 2002')} He wrote that the first Day 1 went 4–2 (did not qualify) and the second Day 1 went 5–1, 2nd that Day 1.

== Deck info ==
* '''Player:''' [[Kyle Krueger]]
* '''Event:''' [[2002 World Championship]]
* '''Stage:''' Day 1
* '''Finish:''' Day 1 (2nd, 5–1)
* '''Published:''' 8 November 2002 (DeckTech)
* '''Published title:''' ''It's a Kyle deck''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Starting Effect:''' {wiki_card("Sai'torr Kal Fas (V)", "LIGHT")} · {wiki_card("Insurrection & Aim High", "LIGHT")} · {wiki_card("Your Insight Serves You Well", "LIGHT")}
* '''Strategy:''' Jedi Council Chamber (no objective)

== Decklist ==

{table_from_rows(KRUEGER_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(26173, description="This is the deck that I used in both Day 1s at DCon. It went 6-0 and I qualified on the second try.")}

== See also ==

* [[2002 World Championship]]
* [[Kyle Krueger]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26173, "It's a Kyle deck")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Championships]]
[[Category:2002]]
"""


def jurcovic_ds_page() -> str:
    start = wiki_card("My Lord, Is That Legal?", "DARK")
    fima = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in JURCOVIC_FIMA
    )
    return f"""'''{JURCOVIC_DS_TITLE}''' is the [[Dark]] constructed list [[Peter Jurcovic]] posted on DeckTech.{post_ref("dt-26448", 26448, "Hold Me Thrill Me Kiss Me Kill Me", 'Peter "marvin" Jurcovic, 2 December 2002')}

== Deck info ==
* '''Player:''' [[Peter Jurcovic]]
* '''Published:''' 2 December 2002 (DeckTech)
* '''Published title:''' ''Hold Me Thrill Me Kiss Me Kill Me''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' My Lord, Is That Legal?

== Decklist ==

{table_from_rows(JURCOVIC_DS, "DARK")}

== Held by Fear Is My Ally ==

{wiki_card("Fear Is My Ally", "DARK")} holds these ten cards from outside the deck. They do not count toward the 60.

{fima}

{formatted_original_post(26448, description="Solid DS Senate deck with space power and good drain and beatdown capabilities.")}

== See also ==

* [[Peter Jurcovic]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26448, "Hold Me Thrill Me Kiss Me Kill Me")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def wata_ds_page() -> str:
    start = wiki_card("My Kind Of Scum", "DARK")
    return f"""'''{WATA_DS_TITLE}''' is the [[Dark]] constructed list [[Keith Watabayashi]] posted on DeckTech.{post_ref("dt-26425", 26425, "G-Scum", 'Keith "Gen" Watabayashi, 29 November 2002')}

== Deck info ==
* '''Player:''' [[Keith Watabayashi]]
* '''Published:''' 29 November 2002 (DeckTech)
* '''Published title:''' ''G-Scum''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' My Kind Of Scum

== Decklist ==

{table_from_rows(WATA_DS, "DARK")}

{formatted_original_post(26425, description="Ket Maliss brokeness")}

== See also ==

* [[Keith Watabayashi]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26425, "G-Scum")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def blackford_ls_page() -> str:
    start = wiki_card("Rescue The Princess", "LIGHT")
    return f"""'''{BLACKFORD_LS_TITLE}''' is the [[Light]] constructed list [[Daniel Blackford]] posted on DeckTech.{post_ref("dt-26421", 26421, "Rock The Projects", 'Daniel "Shadow865" Blackford, 29 November 2002')}

== Deck info ==
* '''Player:''' [[Daniel Blackford]]
* '''Published:''' 29 November 2002 (DeckTech)
* '''Published title:''' ''Rock The Projects''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")} · {wiki_card("Heading For The Medical Frigate", "LIGHT")} · {wiki_card("Do, Or Do Not & Wise Advice", "LIGHT")}
* '''Starting Effect:''' {wiki_card("Cell 2187 (V)", "LIGHT")}
* '''Strategy:''' Rescue The Princess

== Decklist ==

{table_from_rows(BLACKFORD_LS, "LIGHT")}

{formatted_original_post(26421, description="RTP revived and revitalized. No gimmicky flipping strategies like lift tubes or rontos -- just solid, speedy, recurring beats that place opponents' characters out of play. The perfect meta choice, with so many decks focused around a few highpower char")}

== See also ==

* [[Daniel Blackford]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26421, "Rock The Projects")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def keskic_ds_page() -> str:
    start = wiki_card("This Deal Is Getting Worse All The Time", "DARK")
    return f"""'''{KESKIC_DS_TITLE}''' is the [[Dark]] constructed list [[Vjeko Keskic]] posted on DeckTech.{post_ref("dt-26368", 26368, "My Keskic Is This Deal Legal aka The Croatian Deal v2 1", 'Vjeko "mighty_maul" Keskic, 24 November 2002')} The post starts {wiki_card("Fear Is My Ally", "DARK")} with ten Defensive Shields from outside the 60 and names {wiki_card("Do They Have A Code Clearance?", "DARK")} and {wiki_card("Allegations Of Corruption", "DARK")}.

== Deck info ==
* '''Player:''' [[Vjeko Keskic]]
* '''Published:''' 24 November 2002 (DeckTech)
* '''Published title:''' ''My Keskic Is This Deal Legal aka The Croatian Deal v2 1''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")} · {wiki_card("I'm Sorry", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' This Deal Is Getting Worse All The Time

== Decklist ==

{table_from_rows(KESKIC_DS, "DARK")}

{formatted_original_post(26368, description="Give Your Opponent Damage With The Croatian Deal")}

== See also ==

* [[Vjeko Keskic]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26368, "My Keskic Is This Deal Legal aka The Croatian Deal v2 1")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def fiedler_ds_page() -> str:
    start = wiki_card("Let Them Make The First Move", "DARK")
    published = "we will reveal ourselves to the jedi at last we will have revenge"
    return f"""'''{FIEDLER_DS_TITLE}''' is the [[Dark]] constructed list [[Justin Fiedler]] posted on DeckTech.{post_ref("dt-25033", 25033, published, 'Justin "Black 1" Fiedler, 13 August 2002')}

== Deck info ==
* '''Player:''' [[Justin Fiedler]]
* '''Published:''' 13 August 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS3]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' Let Them Make The First Move

== Decklist ==

{table_from_rows(FIEDLER_DS, "DARK")}

{formatted_original_post(25033, description="LSC that almost guarantees to win LSC every time.")}

== See also ==

* [[Justin Fiedler]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(25033, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def zinn_ls_page() -> str:
    start = wiki_card("Rescue The Princess", "LIGHT")
    published = "Shes Virtually Back"
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in ZINN_SHIELDS
    )
    return f"""'''{ZINN_LS_TITLE}''' is the [[Light]] constructed list [[Greg Zinn]] posted on DeckTech.{post_ref("dt-25015", 25015, published, 'Greg "Gergall" Zinn, 13 August 2002')}

== Deck info ==
* '''Player:''' [[Greg Zinn]]
* '''Published:''' 13 August 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Podrace Prep", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' Rescue The Princess

== Decklist ==

{table_from_rows(ZINN_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(25015, description="It's not over yet  A fresh alternative for the light side that can reliably disrupt LSC, Dark Deal, Walker Garrison, Invasion, Senate, and especially Watto in a big way.  There are so many dark decks that rely on key characters- placing")}

== See also ==

* [[Greg Zinn]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(25015, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def povs1_page() -> str:
    return """{{Hatnote|This page is printed Decipher cards plus original Virtual Set 1 (2002 PDF slips). It is not current [[Virtual Set 1]] and not [[Premiere to Virtual Set 3]].}}
'''Premiere - Original VS1''' is the constructed pool of printed Decipher cards through [[Theed Palace]] plus original [[Players Committee]] [[Virtual Set 1 (Original)|Virtual Set 1]]. [[Virtual Set 1 (Original)|Virtual Set 1]] became tournament-legal on 9 March 2002.<ref name="vs2002">[[Virtual Sets (2002-2009)]]</ref> The short name '''POVS1''' redirects here.

[[Darryll Silva DS]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (9 April 2002). [[Casey Merry Celebration what]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (9 April 2002). [[Mike Stevens ls senate]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (19 April 2002). [[2002 Yavin 4 Regionals Kevin Elia 2002 Yavin 4 regional 2nd Place- I Am Jacks Anger]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (21 April 2002). [[Jacob Taylor Jacob's Profit aka Big Trouble]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Dunya Ertan beefed up profit]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (27 April 2002). [[Chris Burnett My senate]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (27 April 2002). [[Taylor Hayward A Hidden Base Deck]] dests [[Luke Skywalker (V) (Virtual Set 1)]]. [[Dennis Jeffris Rebel Strike Team - Da Non-Bomb]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (28 April 2002). [[Dunya Ertan we dont need a sticking hypergenerator]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (29 April 2002). [[Jason Herrin Voice of the council solid]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Taylor Hayward Agents In The Court]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (4 May 2002). [[Dunya Ertan power of Rebel strike team]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (4 May 2002). [[Thomas Papp HDADTJ aka there are no Jedi alive]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (5 May 2002). [[Sam Diamond The CIA Is Trying To Kill Me]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (5 May 2002). [[Drew Scott BHBM how to kill combat]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (6 May 2002). [[Jacob Taylor Jacob's BHBM aka Blame Canada]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (9 May 2002). [[Lewis Blake YEEeeah I've got the Hoth (Big) Blues Baby]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (11 May 2002). [[Taylor Hayward LS]] dests [[Luke Skywalker (V) (Virtual Set 1)]]. [[Peter Jurcovic There Are Those Droidekas]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (14 May 2002). [[Matthew Harrison-Trainor Secret Siths Profit]] dests [[Bo Shek (V) (Virtual Set 1)]] and [[Han's Heavy Blaster Pistol (V) (Virtual Set 1)]]. [[2002 Vegas DPC Brian Hunter LS Senate done RIGHT aka Ghhhks Away]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (12 May 2002). [[2002 Alderaan Regionals Clayton Atkin Atkins’ Alderaan 2nd Place TDIGWATT]] dests [[Prophetess (V) (Virtual Set 1)]] and [[Black 2 (V) (Virtual Set 1)]]. [[Cody Jewell ’Saber Combat My Way V1 00(UnRevised)]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Wes Brown Imperial Blues]] dests [[Darth Vader (V) (Virtual Set 1)]]. [[Mike (Quione) Rebel Strike Team- Stay the hell of endor]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (22 May 2002). [[Vjeko Keskic H-TOWN Jedis vs NRW Jedis]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Vjeko Keskic All Your Damage Belongs To Watto]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (25 May 2002). [[Maximilien Bouchard WYS Choke BETA]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (25 May 2002). [[Jon Manning Cloud City trooper deck]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (25 May 2002). [[Quirin Fürgut Unbeatable EBO aka fun for everyone]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (26 May 2002). [[Brian Hunter Saber Combat done RIGHT aka No Mans Land]] dests [[Prophetess (V) (Virtual Set 1)]] and [[Blaster Rack (V) (Virtual Set 1)]]. [[Uriah Watkins Testing Testing 1 2 3 (4 5 6)]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[2002 Ralltiir Regionals Vjeko Keskic Court Likes Direct Damage aka Gailid Superstar]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (19 May 2002). Game Players Network lists posted from that legal day dest original-era slips such as [[Blaster Rack (V) (Virtual Set 1)]], [[Darth Vader (V) (Virtual Set 1)]], [[Prophetess (V) (Virtual Set 1)]], [[Luke Skywalker (V) (Virtual Set 1)]], and [[Bo Shek (V) (Virtual Set 1)]].

== Organized play ==

* [[DeckTech decks]]
* [[Game Players Network decks]]

== See also ==

* [[Formats]]
* [[Virtual Sets (2002-2009)]]
* [[Virtual Set 1 (Original)]]
* [[Premiere - Theed Palace]]
* [[Premiere - Original VS2]]
* [[Premiere - Original VS3]]
* [[Premiere to Virtual Set 3]]

== Sources ==

* [https://web.archive.org/web/20050813215254/http://decipher.com/starwars/cardlists/virtual/VirtualCards1.pdf VirtualCards1.pdf], decipher.com (Wayback, 13 August 2005)
* [https://res.starwarsccg.org/legacyblocks/VirtualCards1a.pdf VirtualCards1a.pdf], res.starwarsccg.org/legacyblocks
* [[Virtual Sets (2002-2009)]]

{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Formats]]
[[Category:Meta]]
[[Category:2002]]
[[Category:Players Committee]]
"""


def povs2_page() -> str:
    return """{{Hatnote|This page is printed Decipher cards plus original Virtual Sets 1–2 (2002 PDF slips). It is not current [[Virtual Set 2]] and not [[Premiere to Virtual Set 3]].}}
'''Premiere - Original VS2''' is the constructed pool of printed Decipher cards through [[Theed Palace]] plus original [[Players Committee]] Virtual Sets 1–2. [[Virtual Set 2 (Original)|Virtual Set 2]] became tournament-legal on 1 June 2002.<ref name="vs2002">[[Virtual Sets (2002-2009)]]</ref> The short name '''POVS2''' redirects here.

[[Stephen Beckham Too Hot in da Hot Tub]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Chris Wodicka 6th place Coruscant regionals]] dests [[Darth Vader (V) (Virtual Set 1)]]. [[Adam McCombie Throne Room Mains So Hot Right Now]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Matt Wehner Court Of the Vile Gangsta - Limp Bizkit Style]] dests [[Molator (V) (Virtual Set 2)]]. [[Geoff Bowman DS]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (9 June 2002). [[Greg Zinn Shes Virtually Back]] dests original-era slips such as [[Leia's Back (V) (Virtual Set 2)]], [[Yavin Sentry (V) (Virtual Set 2)]], and [[Affect Mind (V) (Virtual Set 2)]]. [[Maximilien Bouchard Fear Will Keep Them In Line (V) ALPHA]] dests [[Fear Will Keep Them In Line (V) (Virtual Set 2)]] and [[Imperial-Class Star Destroyer (V) (Virtual Set 2)]]. [[John Irving 3B3-888 Superstar aka Agents of pure BS]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (7 August 2002). [[Ryan McLain The Rx Throne Room Wrex]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (4 August 2002). [[Tulsa Mini-Open Michael Sneed Subterranean Homesick Alien]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (August 2002). [[Steve Marshall Viperstyle - Keeping The Senators Out Forever]] dests [[Luke Skywalker (V) (Virtual Set 1)]]. [[2002 Origins Open Ken Cross Squires Origins Profit]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]] and [[Escape Pod (V) (Virtual Set 2)]]. [[Justin Warren Raging Bull (Hoostino's Hunt Down Hammer)]] dests [[I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)]]. [[David Burnett JediGamler's Watto aka The Unstoppable Machine]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (20 July 2002 post; [[2002 Houston DPC]] 14 July 2002). [[Kyle Krueger The Beast on the Beach]] dests [[Imperial Reinforcements (V) (Virtual Set 2)]]. [[Kyle Krueger the beast on the beach v2]] dests [[Imperial Reinforcements (V) (Virtual Set 2)]]. [[Mike (Quione) Saber combat my way]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (24 June 2002). [[Seth Van Winkle Seth's Mad Huntdown Deck]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (10 July 2002). [[Pyry Nystrom Empire is virtually back]] dests [[Darth Vader (V) (Virtual Set 1)]], [[Commander Praji (V) (Virtual Set 2)]], [[The Empire's Back (V) (Virtual Set 2)]], [[Imperial-Class Star Destroyer (V) (Virtual Set 2)]], [[Fear Will Keep Them In Line (V) (Virtual Set 2)]], and [[I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)]]. [[Bill Kafer LSC TacoBill style]] dests [[Blaster Rack (V) (Virtual Set 1)]]. [[Matt Carulli Hunt Down and Revive the SCUM]] dests [[Blaster Rack (V) (Virtual Set 1)]] and [[I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)]]. [[Chris Davis TDIGWATT/PIDAIAF CC Dark Deal Deck]] dests [[Black 2 (V) (Virtual Set 1)]]. [[Chris McCoy Quiet Macking of Cloud city]] dests [[Escape Pod (V) (Virtual Set 2)]]. [[Mike Guarino I’m Getting Too Old For This]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (19 June 2002). [[Arvind Bhasker Maul’s Combat]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (13 June 2002). [[Vjeko Keskic Rumble In The Bronx With Mains]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[Zach Mann None shall pass choke damn I guess you can]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (16 June 2002). [[Matt Wehner Good PunJab Hunting]] dests [[Rycar Ryjerd (V) (Virtual Set 2)]], [[Escape Pod (V) (Virtual Set 2)]], and [[K'lor'slug (V) (Virtual Set 2)]]. [[David Kangas QMC Clouds]] dests [[Sai'torr Kal Fas (V) (Virtual Set 1)]]. [[James Zajic die die die]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (16 June 2002). [[Adam Nelson Droid Deal v 1 0]] dests [[I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)]], [[Imperial-Class Star Destroyer (V) (Virtual Set 2)]], and [[Death Star Sentry (V) (Virtual Set 2)]]. [[Zach Mann What my step It’s yours I should be watching]] is printed Decipher through [[Theed Palace]] (no original (V) cards); the format cell is still this pool by legal day (17 June 2002).

== Organized play ==

* [[DeckTech decks]]

== See also ==

* [[Formats]]
* [[Virtual Sets (2002-2009)]]
* [[Virtual Set 2 (Original)]]
* [[Premiere - Original VS1]]
* [[Premiere - Original VS3]]
* [[Premiere - Theed Palace]]
* [[Premiere to Virtual Set 3]]

== Sources ==

* [https://web.archive.org/web/20071024153738/http://www.swccgpc.com/Resources/VirtualCards2.pdf VirtualCards2.pdf], swccgpc.com (Wayback, 24 October 2007)
* [https://res.starwarsccg.org/legacyblocks/VirtualCards2.pdf VirtualCards2.pdf], res.starwarsccg.org/legacyblocks
* [[Virtual Sets (2002-2009)]]

{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Formats]]
[[Category:Meta]]
[[Category:2002]]
[[Category:Players Committee]]
"""


def povs2_redirect() -> str:
    return "#REDIRECT [[Premiere - Original VS2]]\n"


def greg_zinn_inject() -> str:
    path = PAGES / "Greg_Zinn.wiki"
    text = path.read_text(encoding="utf-8")
    ref = post_ref(
        "dt-25015",
        25015,
        "Shes Virtually Back",
        'Greg "Gergall" Zinn, 13 August 2002',
    )
    old = "with forum handle '''Gergall''' and role contact"
    new = f"with forum handle '''Gergall'''{ref} and role contact"
    if old in text and "dt-25015" not in text:
        text = text.replace(old, new, 1)
    fact = (
        " He posted a [[Light]] "
        "[[Rescue The Princess / Sometimes I Amaze Even Myself|Rescue The Princess]] "
        "list on DeckTech (''Shes Virtually Back'')."
    )
    if "list on DeckTech" not in text:
        marker = "\n\n== Documented PC roles =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
    row = (
        "| 13 August 2002 || [[Premiere - Original VS2]] || "
        f"[[{ZINN_LS_TITLE}|Shes Virtually Back]] || [[Light]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(
        text, post_source_bullets(25015, "Shes Virtually Back") + "\n"
    )
    text = add_category(text, "2002")
    return text


def formats_inject() -> str:
    path = PAGES / "Formats.wiki"
    text = path.read_text(encoding="utf-8")
    vs2_bullet = (
        "* [[Premiere - Original VS2]] (redirect [[POVS2]]) — printed Decipher "
        "through [[Theed Palace]] plus original Virtual Sets 1–2. Legal 1 June 2002. "
        "Used on [[Greg Zinn Shes Virtually Back]].\n"
    )
    vs1_bullet = (
        "* [[Premiere - Original VS1]] (redirect [[POVS1]]) — printed Decipher "
        "through [[Theed Palace]] plus original Virtual Set 1. Legal 9 March 2002. "
        "Used on [[Game Players Network decks]] from that day.\n"
    )
    if "Premiere - Original VS2" not in text and vs1_bullet in text:
        text = text.replace(vs1_bullet, vs1_bullet + vs2_bullet, 1)
    old_later = (
        "[[Premiere - Original VS1]] (March 2002), [[Premiere - Original VS3]] (2002)"
    )
    new_later = (
        "[[Premiere - Original VS1]] (March 2002), [[Premiere - Original VS2]] "
        "(June 2002), [[Premiere - Original VS3]] (2002)"
    )
    if old_later in text:
        text = text.replace(old_later, new_later, 1)
    see = "* [[Premiere - Original VS1]] — March 2002 original-virtual constructed pool\n"
    see2 = "* [[Premiere - Original VS2]] — June 2002 original-virtual constructed pool\n"
    if see in text and see2 not in text:
        text = text.replace(see, see + see2, 1)
    return text


def worlds_2002() -> str:
    return f"""'''2002 World Championship''' was the first Players Committee Star Wars CCG World Championship, run at DecipherCon 2002 (Chesapeake Conference Center, 1–3 November 2002).<ref name="dcon-fmt">[{DCON_FORMATS} World Championship Event Formats & Prizes] (Wayback, 10 August 2002)</ref><ref name="tfn">[{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)</ref>

[[Angelo Consoli]] won. [[Greg Shaw]] finished 2nd. 3rd and 4th were [[Brian Terwilliger]] and [[Brian Fred]]. 5th–8th: [[Hayes Hunter]], [[Jonathan Chu]], Brian Rippetoe, [[Bastian Winkelhaus]].<ref name="tfn" />

The constructed pool was [[Premiere - Original VS3]]: printed sets through [[Theed Palace]] plus original virtual cards through [[Virtual Set 3 (Original)|VS3]] (legal 20 September 2002). Shaw posted a Light [[There Is Good In Him / I Can Save Him|There Is Good In Him]] list on DeckTech (DCon2k2 Runner Up - LS). [[Angelo Consoli]] posted the Dark [[2002 World Championship Angelo Consoli DS|No Money, No Parts, No Deal!]] Watto 60 that won. [[Keith Watabayashi]] posted the Day 2 Light TIGIH also played by [[Brad Reinhold]]. [[Kyle Krueger]] posted a Day 1 Light Jedi Council Chamber list (''It's a Kyle deck'').

== Format ==

* '''Environment:''' [[Premiere - Original VS3]]
* '''Dates:''' 1–3 November 2002
* '''Site:''' DecipherCon 2002, Chesapeake Conference Center

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Angelo Consoli]] || [[{CONSOLI_DS_TITLE}|No Money, No Parts, No Deal!]] || —
|-
| 2 || [[Greg Shaw]] || [[{SHAW_DS_TITLE}|Hunt Down And Destroy The Jedi]] || [[{SHAW_LS_TITLE}|There Is Good In Him]]
|-
| Day 1 (2nd, 5–1) || [[Kyle Krueger]] || — || [[{KRUEGER_LS_TITLE}|Coruscant: Jedi Council Chamber]]
|-
| Day 2 || [[Keith Watabayashi]] || — || [[{WATA_LS_TITLE}|There Is Good In Him]]
|-
| Day 2 || [[Brad Reinhold]] || — || [[{WATA_LS_TITLE}|There Is Good In Him]]
|}}

== See also ==

* [[Premiere - Original VS3]]
* [[Decklists]] · [[DeckTech decks]] · [[DeckTech tournament reports]]
* [[Championships]] · [[List of SWCCG tournaments]]
* [[DecipherCon 2002]]

== Sources ==

* [{DCON_FORMATS} World Championship Event Formats & Prizes] (Wayback)
* [{TFN_RESULTS} World Championship Results announced], theforce.net
{post_source_bullets(26297, "DeckTech post 26297", github=False)}
{post_source_bullets(26555, "Force Lightning is TECH", github=False)}
{post_source_bullets(26204, "DCon2k2 Runner Up - LS", github=False)}
{post_source_bullets(26273, "The other TIGIH at Deciphercon", github=False)}
{post_source_bullets(26173, "It's a Kyle deck", github=False)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2002]]
"""


def deciphercon_2002() -> str:
    return f"""'''DecipherCon 2002''' was held 1–3 November 2002 at the Chesapeake Conference Center. It hosted the first Players Committee [[2002 World Championship]].<ref name="dcon-fmt">[{DCON_FORMATS} World Championship Event Formats & Prizes] (Wayback, 10 August 2002)</ref><ref name="tfn">[{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)</ref>

[[Angelo Consoli]] won the Star Wars CCG World Championship. [[Greg Shaw]] finished 2nd.

== See also ==

* [[2002 World Championship]]
* [[DecipherCon 2000]] · [[DecipherCon 1999]]
* [[Championships]] · [[List of SWCCG tournaments]]
* [[Decklists]] · [[DeckTech decks]]

== Sources ==

* [{DCON_FORMATS} World Championship Event Formats & Prizes] (Wayback)
* [{TFN_RESULTS} World Championship Results announced], theforce.net

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2002]]
"""


def decktech_decks() -> str:
    return f"""'''DeckTech decks''' are constructed 60s dested from Stephen Skilton's [https://www.stephenskilton.com/decktech_archives/ SWCCG Decktech Archives] of DeckTech posts (3,923 Star Wars posts, ids 3–26555). The same catalog is also on [http://www.decktech.net/starwarsccg/decks/ decktech.net]; individual posts are at `/starwarsccg/deck/{{id}}`. The archive listing's Light/Dark tags are often wrong; dest from the post body.

Tables match [[Decipher deck designs]]: tournament rows when the post names an event and finish; general rows for the rest. Oldest-first. Title is the dest on general rows.

== Tournament lists ==

{{| class="wikitable sortable"
|-
! Date !! Format !! Event !! Finish !! Player !! Dark !! Light
|-
| 4/21/02 || [[Premiere - Original VS1]] || [[2002 Yavin 4 Regionals]] || 2 || [[Kevin Elia]] || [[{ELIA_YAVIN_TITLE}|You May Start Your Landing]] || —
|-
| 5/12/02 || [[Premiere - Original VS1]] || [[2002 Vegas DPC]] || 1 || [[Brian Hunter]] || — || [[{HUNTER_LS_TITLE}|Plead My Case To The Senate]]
|-
| 5/18/02 || [[Premiere - Original VS1]] || [[2002 Alderaan Regionals]] || 2 || [[Clayton Atkin]] || [[{ATKIN_DS_TITLE}|This Deal Is Getting Worse All The Time]] || —
|-
| 5/19/02 || [[Premiere - Original VS1]] || [[2002 Ralltiir Regionals]] || 3 || [[Vjeko Keskic]] || [[{KESKIC_COURT_TITLE}|Court Of The Vile Gangster]] || —
|-
| 6/02 || [[Premiere - Original VS2]] || [[2002 Coruscant Regionals]] || 6th || [[Chris Wodicka]] || [[{WODICKA_DS_TITLE}|ISB Operations]] || —
|-
| 6/02 || [[Premiere - Original VS2]] || [[2002 NYC Mini-Open]] || 2-1 || [[Chris Wodicka]] || [[{WODICKA_DS_TITLE}|ISB Operations]] || —
|-
| 2002 || [[Premiere - Original VS2]] || [[2002 Dantooine Regionals]] || 3-0 || [[Aaron Pawlik]] || [[{BURNETT_DS_TITLE}|No Money, No Parts, No Deal!]] || —
|-
| 7/02 || [[Premiere - Original VS2]] || [[2002 Origins Open]] || 7 || [[Ken Cross]] || — || [[{CROSS_LS_TITLE}|You Can Either Profit By This...]]
|-
| 7/02 || [[Premiere - Original VS2]] || [[2002 Houston Mini-Open]] || 1 || [[Justin Warren]] || [[{WARREN_DS_TITLE}|Hunt Down And Destroy The Jedi]] || —
|-
| 7/14/02 || [[Premiere - Original VS2]] || [[2002 Houston DPC]] || 2 || [[Justin Warren]] || [[{WARREN_DS_TITLE}|Hunt Down And Destroy The Jedi]] || —
|-
| 7/14/02 || [[Premiere - Original VS2]] || [[2002 Houston DPC]] || 2-1 || [[David Burnett]] || [[{BURNETT_DS_TITLE}|No Money, No Parts, No Deal!]] || —
|-
| 8/02 || [[Premiere - Original VS2]] || [[Tulsa Mini-Open]] || 1 || [[Michael Sneed]] || [[{SNEED_DS_TITLE}|My Lord, Is That Legal!]] || —
|-
| 11/02 || [[Premiere - Original VS3]] || [[2002 World Championship]] || 1 || [[Angelo Consoli]] || [[{CONSOLI_DS_TITLE}|No Money, No Parts, No Deal!]] || —
|-
| 11/02 || [[Premiere - Original VS3]] || [[2002 World Championship]] || 2 || [[Greg Shaw]] || [[{SHAW_DS_TITLE}|Hunt Down And Destroy The Jedi]] || [[{SHAW_LS_TITLE}|There Is Good In Him]]
|-
| 11/02 || [[Premiere - Original VS3]] || [[2002 World Championship]] || Day 1 (2nd, 5–1) || [[Kyle Krueger]] || — || [[{KRUEGER_LS_TITLE}|Coruscant: Jedi Council Chamber]]
|-
| 11/02 || [[Premiere - Original VS3]] || [[2002 World Championship]] || Day 2 || [[Keith Watabayashi]] || — || [[{WATA_LS_TITLE}|There Is Good In Him]]
|-
| 11/02 || [[Premiere - Original VS3]] || [[2002 World Championship]] || Day 2 || [[Brad Reinhold]] || — || [[{WATA_LS_TITLE}|There Is Good In Him]]
|}}

== General lists ==

{{| class="wikitable sortable"
|-
! Date !! Format !! Title !! Side !! Author
|-
| 4/9/02 || [[Premiere - Original VS1]] || [[{SILVA_DS_TITLE}]] || [[Dark]] || [[Darryll Silva]]
|-
| 4/9/02 || [[Premiere - Original VS1]] || [[{MERRY_LS_TITLE}|Celebration what]] || [[Light]] || [[Casey Merry]]
|-
| 4/19/02 || [[Premiere - Original VS1]] || [[{STEVENS_LS_TITLE}|ls senate]] || [[Light]] || [[Mike Stevens]]
|-
| 4/25/02 || [[Premiere - Original VS1]] || [[{JACOB_PROFIT_TITLE}|Jacob's Profit aka Big Trouble]] || [[Light]] || [[Jacob Taylor]]
|-
| 4/27/02 || [[Premiere - Original VS1]] || [[{ERTAN_PROFIT_TITLE}|beefed up profit]] || [[Light]] || [[Dunya Ertan]]
|-
| 4/27/02 || [[Premiere - Original VS1]] || [[{BURNETT_SENATE_TITLE}|My senate]] || [[Dark]] || [[Chris Burnett]]
|-
| 4/28/02 || [[Premiere - Original VS1]] || [[{HAYWARD_HB_TITLE}|A Hidden Base Deck]] || [[Light]] || [[Taylor Hayward]]
|-
| 4/28/02 || [[Premiere - Original VS1]] || [[{JEFFRIS_RST_TITLE}|Rebel Strike Team - Da Non-Bomb]] || [[Light]] || [[Dennis Jeffris]]
|-
| 4/29/02 || [[Premiere - Original VS1]] || [[{ERTAN_HYPER_TITLE}|we dont need a sticking hypergenerator]] || [[Light]] || [[Dunya Ertan]]
|-
| 5/2/02 || [[Premiere - Original VS1]] || [[{HERRIN_LS_TITLE}|Voice of the council solid]] || [[Light]] || [[Jason Herrin]]
|-
| 5/4/02 || [[Premiere - Original VS1]] || [[{HAYWARD_AITC_TITLE}|Agents In The Court]] || [[Light]] || [[Taylor Hayward]]
|-
| 5/4/02 || [[Premiere - Original VS1]] || [[{ERTAN_LS_TITLE}|power of Rebel strike team]] || [[Light]] || [[Dunya Ertan]]
|-
| 5/5/02 || [[Premiere - Original VS1]] || [[{PAPP_DS_TITLE}|HDADTJ aka there are no Jedi alive]] || [[Dark]] || [[Thomas Papp]]
|-
| 5/5/02 || [[Premiere - Original VS1]] || [[{DIAMOND_LS_TITLE}|The CIA Is Trying To Kill Me]] || [[Light]] || [[Sam Diamond]]
|-
| 5/6/02 || [[Premiere - Original VS1]] || [[{SCOTT_DS_TITLE}|BHBM how to kill combat]] || [[Dark]] || [[Drew Scott]]
|-
| 5/9/02 || [[Premiere - Original VS1]] || [[{JACOB_BHBM_TITLE}|Jacob's BHBM aka Blame Canada]] || [[Dark]] || [[Jacob Taylor]]
|-
| 5/11/02 || [[Premiere - Original VS1]] || [[{BLAKE_DS_TITLE}|YEEeeah I've got the Hoth (Big) Blues Baby]] || [[Dark]] || [[Lewis Blake]]
|-
| 5/13/02 || [[Premiere - Original VS1]] || [[{HAYWARD_LS_TITLE}]] || [[Light]] || [[Taylor Hayward]]
|-
| 5/14/02 || [[Premiere - Original VS1]] || [[{JURCOVIC_WATD_TITLE}|There Are Those Droidekas]] || [[Dark]] || [[Peter Jurcovic]]
|-
| 5/16/02 || [[Premiere - Original VS1]] || [[{HT_LS_TITLE}|Secret Siths Profit]] || [[Light]] || [[Matthew Harrison-Trainor]]
|-
| 5/21/02 || [[Premiere - Original VS1]] || [[{JEWELL_LS_TITLE}|’Saber Combat My Way V1 00(UnRevised)]] || [[Light]] || [[Cody Jewell]]
|-
| 5/21/02 || [[Premiere - Original VS1]] || [[{BROWN_DS_TITLE}|Imperial Blues]] || [[Dark]] || [[Wes Brown]]
|-
| 5/22/02 || [[Premiere - Original VS1]] || [[{QUIONE_RST_TITLE}|Rebel Strike Team- Stay the hell of endor]] || [[Light]] || [[Mike (Quione)]]
|-
| 5/23/02 || [[Premiere - Original VS1]] || [[{KESKIC_HTOWN_TITLE}|H-TOWN Jedis vs NRW Jedis]] || [[Light]] || [[Vjeko Keskic]]
|-
| 5/25/02 || [[Premiere - Original VS1]] || [[{KESKIC_WATTO_TITLE}|All Your Damage Belongs To Watto]] || [[Dark]] || [[Vjeko Keskic]]
|-
| 5/25/02 || [[Premiere - Original VS1]] || [[{BOUCHARD_LS_TITLE}|WYS Choke BETA]] || [[Light]] || [[Maximilien Bouchard]]
|-
| 5/25/02 || [[Premiere - Original VS1]] || [[{MANNING_DS_TITLE}|Cloud City trooper deck]] || [[Dark]] || [[Jon Manning]]
|-
| 5/26/02 || [[Premiere - Original VS1]] || [[{FURGUT_LS_TITLE}|Unbeatable EBO aka fun for everyone]] || [[Light]] || [[Quirin Fürgut]]
|-
| 5/26/02 || [[Premiere - Original VS1]] || [[{HUNTER_DS_TITLE}|Saber Combat done RIGHT aka No Mans Land]] || [[Dark]] || [[Brian Hunter]]
|-
| 5/29/02 || [[Premiere - Original VS1]] || [[{WATKINS_LS_TITLE}|Testing Testing 1 2 3 (4 5 6)]] || [[Light]] || [[Uriah Watkins]]
|-
| 6/6/02 || [[Premiere - Original VS2]] || [[{BECKHAM_LS_TITLE}|Too Hot in da Hot Tub]] || [[Light]] || [[Stephen Beckham]]
|-
| 6/8/02 || [[Premiere - Original VS2]] || [[{MCCOMBIE_LS_TITLE}|Throne Room Mains So Hot Right Now]] || [[Light]] || [[Adam McCombie]]
|-
| 6/9/02 || [[Premiere - Original VS2]] || [[{WEHNER_DS_TITLE}|Court Of the Vile Gangsta - Limp Bizkit Style]] || [[Dark]] || [[Matt Wehner]]
|-
| 6/9/02 || [[Premiere - Original VS2]] || [[{BOWMAN_DS_TITLE}]] || [[Dark]] || [[Geoff Bowman]]
|-
| 6/10/02 || [[Premiere - Original VS2]] || [[{KESKIC_LS_TITLE}|Rumble In The Bronx With Mains]] || [[Light]] || [[Vjeko Keskic]]
|-
| 6/13/02 || [[Premiere - Original VS2]] || [[{BHASKER_DS_TITLE}|Maul’s Combat]] || [[Dark]] || [[Arvind Bhasker]]
|-
| 6/16/02 || [[Premiere - Original VS2]] || [[{MANN_DS_TITLE}|None shall pass choke damn I guess you can]] || [[Dark]] || [[Zach Mann]]
|-
| 6/16/02 || [[Premiere - Original VS2]] || [[{WEHNER_LS_TITLE}|Good PunJab Hunting]] || [[Light]] || [[Matt Wehner]]
|-
| 6/16/02 || [[Premiere - Original VS2]] || [[{KANGAS_LS_TITLE}|QMC Clouds]] || [[Light]] || [[David Kangas]]
|-
| 6/16/02 || [[Premiere - Original VS2]] || [[{ZAJIC_LS_TITLE}|die die die]] || [[Light]] || [[James Zajic]]
|-
| 6/17/02 || [[Premiere - Original VS2]] || [[{NELSON_DS_TITLE}|Droid Deal v 1 0]] || [[Dark]] || [[Adam Nelson]]
|-
| 6/17/02 || [[Premiere - Original VS2]] || [[{MANN_LS_TITLE}|What my step It’s yours I should be watching]] || [[Light]] || [[Zach Mann]]
|-
| 6/19/02 || [[Premiere - Original VS2]] || [[{GUARINO_LS_TITLE}|I’m Getting Too Old For This]] || [[Light]] || [[Mike Guarino]]
|-
| 6/19/02 || [[Premiere - Original VS2]] || [[{MCCOY_LS_TITLE}|Quiet Macking of Cloud city]] || [[Light]] || [[Chris McCoy]]
|-
| 6/19/02 || [[Premiere - Original VS2]] || [[{DAVIS_DS_TITLE}|TDIGWATT/PIDAIAF CC Dark Deal Deck]] || [[Dark]] || [[Chris Davis]]
|-
| 6/19/02 || [[Premiere - Original VS2]] || [[{CARULLI_DS_TITLE}|Hunt Down and Revive the SCUM]] || [[Dark]] || [[Matt Carulli]]
|-
| 6/24/02 || [[Premiere - Original VS2]] || [[{SABER_LS_TITLE}|Saber combat my way]] || [[Light]] || [[Mike (Quione)]]
|-
| 6/24/02 || [[Premiere - Original VS2]] || [[{BEACH_V1_TITLE}|The Beast on the Beach]] || [[Dark]] || [[Kyle Krueger]]
|-
| 6/27/02 || [[Premiere - Original VS2]] || [[{KAFER_DS_TITLE}|LSC TacoBill style]] || [[Dark]] || [[Bill Kafer]]
|-
| 7/8/02 || [[Premiere - Original VS2]] || [[{NYSTROM_DS_TITLE}|Empire is virtually back]] || [[Dark]] || [[Pyry Nystrom]]
|-
| 7/10/02 || [[Premiere - Original VS2]] || [[{VAN_WINKLE_DS_TITLE}|Seth's Mad Huntdown Deck]] || [[Dark]] || [[Seth Van Winkle]]
|-
| 7/18/02 || [[Premiere - Original VS2]] || [[{KRUEGER_BEACH_TITLE}|the beast on the beach v2]] || [[Dark]] || [[Kyle Krueger]]
|-
| 7/30/02 || [[Premiere - Original VS2]] || [[{MARSHALL_LS_TITLE}|Viperstyle - Keeping The Senators Out Forever]] || [[Light]] || [[Steve Marshall]]
|-
| 8/4/02 || [[Premiere - Original VS2]] || [[{MCLAIN_LS_TITLE}|The Rx Throne Room Wrex]] || [[Light]] || [[Ryan McLain]]
|-
| 8/7/02 || [[Premiere - Original VS2]] || [[{IRVING_DS_TITLE}|3B3-888 Superstar aka Agents of pure BS]] || [[Dark]] || [[John Irving]]
|-
| 8/10/02 || [[Premiere - Original VS2]] || [[{BOUCHARD_DS_TITLE}|Fear Will Keep Them In Line (V) ALPHA]] || [[Dark]] || [[Maximilien Bouchard]]
|-
| 8/13/02 || [[Premiere - Original VS2]] || [[{ZINN_LS_TITLE}|Shes Virtually Back]] || [[Light]] || [[Greg Zinn]]
|-
| 8/13/02 || [[Premiere - Original VS3]] || [[{FIEDLER_DS_TITLE}|we will reveal ourselves to the jedi at last we will have revenge]] || [[Dark]] || [[Justin Fiedler]]
|-
| 11/24/02 || [[Premiere - Original VS3]] || [[{KESKIC_DS_TITLE}|My Keskic Is This Deal Legal aka The Croatian Deal v2 1]] || [[Dark]] || [[Vjeko Keskic]]
|-
| 11/29/02 || [[Premiere - Original VS3]] || [[{BLACKFORD_LS_TITLE}|Rock The Projects]] || [[Light]] || [[Daniel Blackford]]
|-
| 11/29/02 || [[Premiere - Original VS3]] || [[{WATA_DS_TITLE}|G-Scum]] || [[Dark]] || [[Keith Watabayashi]]
|-
| 12/02/02 || [[Premiere - Original VS3]] || [[{JURCOVIC_DS_TITLE}|Hold Me Thrill Me Kiss Me Kill Me]] || [[Dark]] || [[Peter Jurcovic]]
|}}

== See also ==

* [[Premiere - Original VS2]] · [[Premiere - Original VS3]]
* [[Decklists]] · [[DeckTech]] · [[DeckTech tournament reports]]
* [[Decipher deck designs]]
* [[List of SWCCG tournaments]]

== Sources ==

* [https://www.stephenskilton.com/decktech_archives/ SWCCG Decktech Archives], stephenskilton.com
* [https://stevetotheizz0.github.io/decktech_archives/ SWCCG Decktech Archives] (GitHub Pages)
* [http://www.decktech.net/starwarsccg/decks/ DeckTech decks], decktech.net
{post_source_bullets(24026, "Hunt Down and Revive the SCUM", github=False)}
{post_source_bullets(24089, "Saber combat my way", github=False)}
{post_source_bullets(24104, "The Beast on the Beach", github=False)}
{post_source_bullets(24142, "LSC TacoBill style", github=False)}
{post_source_bullets(24274, "Empire is virtually back", github=False)}
{post_source_bullets(24316, "Seth's Mad Huntdown Deck", github=False)}
{post_source_bullets(24467, "the beast on the beach v2", github=False)}
{post_source_bullets(24511, "JediGamler's Watto aka The Unstoppable Machine", github=False)}
{post_source_bullets(24516, "Raging Bull (Hoostino's Hunt Down Hammer)", github=False)}
{post_source_bullets(24668, "Squires Origins Profit", github=False)}
{post_source_bullets(24688, "Viperstyle - Keeping The Senators Out Forever", github=False)}
{post_source_bullets(24783, "Subterranean Homesick Alien", github=False)}
{post_source_bullets(24807, "The Rx Throne Room Wrex", github=False)}
{post_source_bullets(24905, "3B3-888 Superstar aka Agents of pure BS", github=False)}
{post_source_bullets(24965, "Fear Will Keep Them In Line (V) ALPHA", github=False)}
{post_source_bullets(25015, "Shes Virtually Back", github=False)}
{post_source_bullets(25033, "we will reveal ourselves to the jedi at last we will have revenge", github=False)}
{post_source_bullets(26297, "DeckTech post 26297", github=False)}
{post_source_bullets(26555, "Force Lightning is TECH", github=False)}
{post_source_bullets(26204, "DCon2k2 Runner Up - LS", github=False)}
{post_source_bullets(26273, "The other TIGIH at Deciphercon", github=False)}
{post_source_bullets(26173, "It's a Kyle deck", github=False)}
{post_source_bullets(26448, "Hold Me Thrill Me Kiss Me Kill Me", github=False)}
{post_source_bullets(26425, "G-Scum", github=False)}
{post_source_bullets(26421, "Rock The Projects", github=False)}
{post_source_bullets(26368, "My Keskic Is This Deal Legal aka The Croatian Deal v2 1", github=False)}

[[Category:Decklists]]
[[Category:Fan sites]]
[[Category:History]]
"""


def replace_shaw_dest_links(text: str) -> str:
    for old, new in ((SHAW_DS_OLD, SHAW_DS_TITLE), (SHAW_LS_OLD, SHAW_LS_TITLE)):
        text = text.replace(f"[[{old}|", f"[[{new}|")
        text = text.replace(f"[[{old}]]", f"[[{new}]]")
    return text


def patch_greg_shaw() -> None:
    path = PAGES / "Greg_Shaw.wiki"
    text = path.read_text(encoding="utf-8")
    old_lead = (
        "'''Greg Shaw''' (DeckTech handle '''TychoCelchu''') is a member of "
        "[[New Allies]] and the 2025 World Champion. He finished 2nd at the "
        "[[2002 World Championship]] and '''#7''' at the [[2026 Tenth Annual GEMPC]] "
        "(Lost Quarterfinals (Top 8); Challonge seed 3)."
        '<ref name="dt-26555">[http://www.decktech.net/starwarsccg/deck/26555 Force Lightning is TECH], '
        'DeckTech (Greg "TychoCelchu" Shaw, 10 December 2002)</ref>'
        '<ref name="pc-gempc">'
    )
    new_lead = (
        "'''Greg Shaw''' (DeckTech handle '''TychoCelchu''')"
        '<ref name="dt-26555">[http://www.decktech.net/starwarsccg/deck/26555 Force Lightning is TECH], '
        'DeckTech (Greg "TychoCelchu" Shaw, 10 December 2002)</ref> '
        "is a member of [[New Allies]] and the 2025 World Champion. He finished 2nd at the "
        "[[2002 World Championship]] and '''#7''' at the [[2026 Tenth Annual GEMPC]] "
        "(Lost Quarterfinals (Top 8); Challonge seed 3)."
        '<ref name="pc-gempc">'
    )
    if old_lead in text:
        text = text.replace(old_lead, new_lead, 1)
        print("PATCHED Greg Shaw cite-after-handle")
    elif "TychoCelchu''')<ref name=\"dt-26555\">" in text:
        print("Greg Shaw cite-after-handle already set")
    else:
        print("WARN Greg Shaw lead cite-after-handle missing")
    patched = replace_shaw_dest_links(text)
    if patched != text:
        print("PATCHED Greg Shaw dest links")
        text = patched
    path.write_text(text, encoding="utf-8", newline="\n")


def patch_angelo_consoli() -> None:
    path = PAGES / "Angelo_Consoli.wiki"
    text = path.read_text(encoding="utf-8")
    old_lead = (
        "'''Angelo Consoli''' (DeckTech handle '''GravShadow''') won the "
        "[[2002 World Championship]]"
        '<ref name="dt-26297">[http://www.decktech.net/starwarsccg/deck/26297 DeckTech post 26297], '
        'DeckTech (Angelo "GravShadow" Consoli, 19 November 2002)</ref>'
        '<ref name="tfn">'
    )
    new_lead = (
        "'''Angelo Consoli''' (DeckTech handle '''GravShadow''')"
        '<ref name="dt-26297">[http://www.decktech.net/starwarsccg/deck/26297 DeckTech post 26297], '
        'DeckTech (Angelo "GravShadow" Consoli, 19 November 2002)</ref> '
        "won the [[2002 World Championship]]"
        '<ref name="tfn">'
    )
    if old_lead in text:
        text = text.replace(old_lead, new_lead, 1)
        print("PATCHED Angelo Consoli cite-after-handle")
    elif "GravShadow''')<ref name=\"dt-26297\">" in text:
        print("Angelo Consoli cite-after-handle already set")
    else:
        print("WARN Angelo Consoli lead cite-after-handle missing")
    path.write_text(text, encoding="utf-8", newline="\n")


def _insert_live_before_skilton(text: str, pid: int, label: str) -> str:
    live_line = f"* [{live_deck(pid)} {label}], decktech.net"
    skill_line = f"* [{skilton_deck(pid)} {label}], stephenskilton.com"
    if live_line in text:
        return text
    if skill_line in text:
        return text.replace(skill_line, live_line + "\n" + skill_line, 1)
    return text


def patch_player_sources() -> None:
    shaw = PAGES / "Greg_Shaw.wiki"
    text = shaw.read_text(encoding="utf-8")
    text = _insert_live_before_skilton(text, 26555, "Force Lightning is TECH")
    ls_live = f"* [{live_deck(26204)} DCon2k2 Runner Up - LS], decktech.net"
    ls_sk = f"* [{skilton_deck(26204)} DCon2k2 Runner Up - LS], stephenskilton.com"
    if ls_sk not in text:
        needle = f"* [{skilton_deck(26555)} Force Lightning is TECH], stephenskilton.com"
        if needle in text:
            text = text.replace(
                needle,
                needle + "\n" + ls_live + "\n" + ls_sk,
                1,
            )
    else:
        text = _insert_live_before_skilton(text, 26204, "DCon2k2 Runner Up - LS")
    shaw.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Greg Shaw Sources")

    consoli = PAGES / "Angelo_Consoli.wiki"
    ctext = consoli.read_text(encoding="utf-8")
    ctext = _insert_live_before_skilton(ctext, 26297, "DeckTech post 26297")
    consoli.write_text(ctext, encoding="utf-8", newline="\n")
    print("PATCHED Angelo Consoli Sources")


def patch_decktech_hub() -> None:
    path = PAGES / "DeckTech.wiki"
    text = path.read_text(encoding="utf-8")
    old = (
        "Live [http://www.decktech.net/starwarsccg/decks/ decktech.net/starwarsccg/decks] "
        "and [http://www.decktech.net/starwarsccg/tournament-reports/ tournament-reports] "
        "are a later shell. They do not list the old posts in static HTML. "
        "The Skilton dump is the working copy of the DeckTech 60s and reports. "
        "Listing Light/Dark tags on the archive index are often wrong "
        "(a Hunt Down post tagged Light); dest from the post body."
    )
    new = (
        "The same 3,923 posts are also hosted at "
        "[http://www.decktech.net/starwarsccg/decks/ decktech.net]; individual posts "
        "are at `/starwarsccg/deck/{id}`. Title, author, handle, side, and rating "
        "letter indexes on that host 404. Listing Light/Dark tags on the archive "
        "index are often wrong (a Hunt Down post tagged Light)."
    )
    if old in text:
        text = text.replace(old, new, 1)
        print("PATCHED DeckTech later-shell lead")
    elif "/starwarsccg/deck/{id}" in text:
        print("DeckTech hub already updated")
    else:
        print("WARN DeckTech hub later-shell paragraph missing")
    extra = (
        "* [http://www.decktech.net/starwarsccg/deck/26555 Force Lightning is TECH], decktech.net\n"
        "* [http://www.decktech.net/starwarsccg/deck/26297 DeckTech post 26297], decktech.net\n"
        "* [http://www.decktech.net/starwarsccg/deck/26204 DCon2k2 Runner Up - LS], decktech.net"
    )
    listing = "* [http://www.decktech.net/starwarsccg/decks/ DeckTech decks], decktech.net"
    if "starwarsccg/deck/26555" not in text and listing in text:
        text = text.replace(listing, listing + "\n" + extra, 1)
        print("PATCHED DeckTech Sources live posts")
    path.write_text(text, encoding="utf-8", newline="\n")


def add_misc_row(text: str, row: str) -> str:
    if row in text:
        return text
    if "== Miscellaneous decklists ==" not in text:
        table = (
            "== Miscellaneous decklists ==\n\n"
            '{| class="wikitable"\n'
            "|-\n"
            "! Date !! Format !! Title !! Side\n"
            "|-\n"
            f"{row}\n"
            "|}\n\n"
        )
        see = text.find("== See also ==")
        if see >= 0:
            return text[:see] + table + text[see:]
        return text
    idx = text.find("== Miscellaneous decklists ==")
    close = text.find("\n|}", idx)
    if close < 0:
        return text
    return text[:close] + "\n|-\n" + row + text[close:]


def add_result_row(text: str, row: str) -> str:
    if row in text:
        return text
    idx = text.find("== Tournament Results ==")
    if idx < 0:
        return text
    close = text.find("\n|}", idx)
    if close < 0:
        return text
    return text[:close] + "\n|- \n" + row + text[close:]


def add_source_line(text: str, line: str) -> str:
    if line in text:
        return text
    src = text.find("== Sources ==")
    if src < 0:
        return text
    if_pos = text.find("\n{{#if:", src)
    cat = text.find("\n[[Category:", src)
    candidates = [p for p in (if_pos, cat) if p >= 0]
    if not candidates:
        return text
    insert_at = min(candidates)
    insert = line if line.endswith("\n") else line + "\n"
    return text[:insert_at] + insert + text[insert_at:]


def add_see_also(text: str, line: str) -> str:
    if line in text:
        return text
    see = text.find("== See also ==")
    if see < 0:
        return text
    src = text.find("\n== Sources ==", see)
    if src < 0:
        return text
    return text[:src] + "\n" + line.rstrip() + "\n" + text[src:]


def add_category(text: str, cat: str) -> str:
    line = f"[[Category:{cat}]]"
    if line in text:
        return text
    return text.rstrip() + "\n" + line + "\n"


def keith_stub() -> str:
    ref = post_ref(
        "dt-26273",
        26273,
        "The other TIGIH at Deciphercon",
        'Keith "Gen" Watabayashi, 17 November 2002',
    )
    row = (
        "| 1–3 November 2002 || [[2002 World Championship]] (Day 2) || "
        "[[Premiere - Original VS3]] || Day 2 || — || "
        f"[[{WATA_LS_TITLE}|There Is Good In Him]]"
    )
    return f"""'''Keith Watabayashi''' (DeckTech handle '''Gen'''){ref} posted a [[Light]] [[There Is Good In Him / I Can Save Him|There Is Good In Him]] list from Day 2 of the [[2002 World Championship]], which he and [[Brad Reinhold]] played.

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{row}
|}}

== See also ==

* [[2002 World Championship]]
* [[Brad Reinhold]]
* [[DeckTech decks]]
* [[Championships]]
* [[List of SWCCG tournaments]]

== Sources ==

{post_source_bullets(26273, "The other TIGIH at Deciphercon")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def patch_kyle_krueger() -> None:
    path = PAGES / "Kyle_Krueger.wiki"
    text = path.read_text(encoding="utf-8")
    old_lead = "'''Kyle Krueger''' is a member of [[Team 5]]"
    new_lead = (
        "'''Kyle Krueger''' (DeckTech handle '''Meto''')"
        '<ref name="dt-26173">[http://www.decktech.net/starwarsccg/deck/26173 It\'s a Kyle deck], '
        'DeckTech (Kyle "Meto" Krueger, 8 November 2002)</ref> '
        "is a member of [[Team 5]]"
    )
    if old_lead in text:
        text = text.replace(old_lead, new_lead, 1)
        print("PATCHED Kyle Krueger cite-after-handle")
    elif "Meto''')<ref name=\"dt-26173\">" in text:
        print("Kyle Krueger cite-after-handle already set")
    else:
        print("WARN Kyle Krueger lead cite-after-handle missing")
    row = (
        "| 1–3 November 2002 || [[2002 World Championship]] (Day 1) || "
        "[[Premiere - Original VS3]] || Day 1 (2nd, 5–1) || — || "
        f"[[{KRUEGER_LS_TITLE}|Coruscant: Jedi Council Chamber]]"
    )
    text = add_result_row(text, row)
    text = add_see_also(text, "* [[2002 World Championship]]")
    text = add_source_line(
        text,
        "* [http://www.decktech.net/starwarsccg/deck/26173 It's a Kyle deck], decktech.net\n"
        "* [https://www.stephenskilton.com/decktech_archives/26173/ It's a Kyle deck], stephenskilton.com\n",
    )
    wb = WAYBACK.get(("live", 26173))
    if wb:
        text = add_source_line(
            text, f"* [{wb} It's a Kyle deck] (Wayback of decktech.net)\n"
        )
    text = add_category(text, "2002")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Kyle Krueger")


def patch_brad_reinhold() -> None:
    path = PAGES / "Brad_Reinhold.wiki"
    text = path.read_text(encoding="utf-8")
    old_lead = (
        "'''Brad Reinhold''' finished '''#7''' at the [[2025 Las Vegas Grand Prix]]."
    )
    new_lead = (
        "'''Brad Reinhold''' played a [[Light]] [[There Is Good In Him / I Can Save Him|There Is Good In Him]] list on Day 2 of the "
        "[[2002 World Championship]] with [[Keith Watabayashi]]."
        '<ref name="dt-26273">[http://www.decktech.net/starwarsccg/deck/26273 The other TIGIH at Deciphercon], '
        'DeckTech (Keith "Gen" Watabayashi, 17 November 2002)</ref> '
        "He finished '''#7''' at the [[2025 Las Vegas Grand Prix]]."
    )
    if old_lead in text:
        text = text.replace(old_lead, new_lead, 1)
        print("PATCHED Brad Reinhold 2002 lead")
    elif "dt-26273" in text[:400]:
        print("Brad Reinhold 2002 lead already set")
    else:
        print("WARN Brad Reinhold lead missing")
    text = text.replace(
        "[[Light]] [[There Is Good In Him]] list",
        "[[Light]] [[There Is Good In Him / I Can Save Him|There Is Good In Him]] list",
    )
    row = (
        "| 1–3 November 2002 || [[2002 World Championship]] (Day 2) || "
        "[[Premiere - Original VS3]] || Day 2 || — || "
        f"[[{WATA_LS_TITLE}|There Is Good In Him]]"
    )
    text = add_result_row(text, row)
    text = add_see_also(text, "* [[2002 World Championship]]")
    text = add_source_line(
        text,
        "* [http://www.decktech.net/starwarsccg/deck/26273 The other TIGIH at Deciphercon], decktech.net\n"
        "* [https://www.stephenskilton.com/decktech_archives/26273/ The other TIGIH at Deciphercon], stephenskilton.com\n",
    )
    wb = WAYBACK.get(("live", 26273))
    if wb:
        text = add_source_line(
            text,
            f"* [{wb} The other TIGIH at Deciphercon] (Wayback of decktech.net)\n",
        )
    text = add_category(text, "2002")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Brad Reinhold")


def peter_stub() -> str:
    ref = post_ref(
        "dt-26448",
        26448,
        "Hold Me Thrill Me Kiss Me Kill Me",
        'Peter "marvin" Jurcovic, 2 December 2002',
    )
    row = (
        "| 2 December 2002 || [[Premiere - Original VS3]] || "
        f"[[{JURCOVIC_DS_TITLE}|Hold Me Thrill Me Kiss Me Kill Me]] || [[Dark]]"
    )
    return f"""'''Peter Jurcovic''' (DeckTech handle '''marvin'''){ref} posted a [[Dark]] [[My Lord, Is That Legal? / I Will Make It Legal|My Lord, Is That Legal?]] list on DeckTech (''Hold Me Thrill Me Kiss Me Kill Me'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26448, "Hold Me Thrill Me Kiss Me Kill Me")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def daniel_stub() -> str:
    ref = post_ref(
        "dt-26421",
        26421,
        "Rock The Projects",
        'Daniel "Shadow865" Blackford, 29 November 2002',
    )
    row = (
        "| 29 November 2002 || [[Premiere - Original VS3]] || "
        f"[[{BLACKFORD_LS_TITLE}|Rock The Projects]] || [[Light]]"
    )
    return f"""'''Daniel Blackford''' (DeckTech handle '''Shadow865'''){ref} posted a [[Light]] [[Rescue The Princess / Sometimes I Amaze Even Myself|Rescue The Princess]] list on DeckTech (''Rock The Projects'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(26421, "Rock The Projects")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def keith_page() -> str:
    ref = post_ref(
        "dt-26273",
        26273,
        "The other TIGIH at Deciphercon",
        'Keith "Gen" Watabayashi, 17 November 2002',
    )
    trow = (
        "| 1–3 November 2002 || [[2002 World Championship]] (Day 2) || "
        "[[Premiere - Original VS3]] || Day 2 || — || "
        f"[[{WATA_LS_TITLE}|There Is Good In Him]]"
    )
    mrow = (
        "| 29 November 2002 || [[Premiere - Original VS3]] || "
        f"[[{WATA_DS_TITLE}|G-Scum]] || [[Dark]]"
    )
    return f"""'''Keith Watabayashi''' (DeckTech handle '''Gen'''){ref} posted a [[Light]] [[There Is Good In Him / I Can Save Him|There Is Good In Him]] list from Day 2 of the [[2002 World Championship]], which he and [[Brad Reinhold]] played. He also posted a [[Dark]] [[My Kind Of Scum / Fearless And Inventive|My Kind Of Scum]] list (''G-Scum'').{post_ref("dt-26425", 26425, "G-Scum", 'Keith "Gen" Watabayashi, 29 November 2002')}

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{trow}
|}}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{mrow}
|}}

== See also ==

* [[2002 World Championship]]
* [[Brad Reinhold]]
* [[DeckTech decks]]
* [[Championships]]
* [[List of SWCCG tournaments]]

== Sources ==

{post_source_bullets(26273, "The other TIGIH at Deciphercon")}
{post_source_bullets(26425, "G-Scum")}
* [{TFN_RESULTS} World Championship Results announced], theforce.net (3 November 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def vjeko_page() -> str:
    ref = post_ref(
        "dt-26368",
        26368,
        "My Keskic Is This Deal Legal aka The Croatian Deal v2 1",
        'Vjeko "mighty_maul" Keskic, 24 November 2002',
    )
    ref2 = post_ref(
        "dt-23859",
        23859,
        "Rumble In The Bronx With Mains",
        'Vjeko "mighty_maul" Keskic, 10 June 2002',
    )
    mrow_ls = (
        "| 10 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{KESKIC_LS_TITLE}|Rumble In The Bronx With Mains]] || [[Light]]"
    )
    mrow_ds = (
        "| 24 November 2002 || [[Premiere - Original VS3]] || "
        f"[[{KESKIC_DS_TITLE}|My Keskic Is This Deal Legal aka The Croatian Deal v2 1]] || [[Dark]]"
    )
    ref3 = post_ref(
        "dt-23606",
        23606,
        "Court Likes Direct Damage aka Gailid Superstar",
        'Vjeko "mighty_maul" Keskic, 27 May 2002',
    )
    ref4 = post_ref(
        "dt-23561",
        23561,
        "All Your Damage Belongs To Watto",
        'Vjeko "mighty_maul" Keskic, 25 May 2002',
    )
    ref5 = post_ref(
        "dt-23520",
        23520,
        "H-TOWN Jedis vs NRW Jedis",
        'Vjeko "mighty_maul" Keskic, 23 May 2002',
    )
    trow_ralltiir = (
        "| 19 May 2002 || [[2002 Ralltiir Regionals]] || [[Premiere - Original VS1]] || 3 || "
        f"[[{KESKIC_COURT_TITLE}|Court Of The Vile Gangster]] || —"
    )
    mrow_watto = (
        "| 25 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{KESKIC_WATTO_TITLE}|All Your Damage Belongs To Watto]] || [[Dark]]"
    )
    mrow_htown = (
        "| 23 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{KESKIC_HTOWN_TITLE}|H-TOWN Jedis vs NRW Jedis]] || [[Light]]"
    )
    return f"""'''Vjeko Keskic''' (DeckTech handle '''mighty_maul'''){ref} posted a [[Light]] [[You Can Either Profit By This... / Or Be Destroyed|You Can Either Profit By This...]] list on DeckTech (''Rumble In The Bronx With Mains''){ref2} and finished 3rd at [[2002 Ralltiir Regionals]] with a [[Dark]] [[Court Of The Vile Gangster / I Shall Enjoy Watching You Die|Court Of The Vile Gangster]] list (''Court Likes Direct Damage aka Gailid Superstar'').{ref3} He posted a [[Dark]] [[No Money, No Parts, No Deal! / You're A Slave?|No Money, No Parts, No Deal!]] list (''All Your Damage Belongs To Watto'').{ref4} He posted a [[Light]] [[We'll Handle This / Duel Of The Fates|We'll Handle This]] list (''H-TOWN Jedis vs NRW Jedis'').{ref5} He played the [[2019 European Championship]].<ref name="pc-rem">[https://www.starwarsccg.org/2019-european-championships/ 2019 European Championship], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
| 12–14 July 2019 || [[2019 European Championship]] (Day 2) || [[Open]] || — || [[2019 European Championship Day 2 Vjeko Keskic DS Court Of The Vile Gangster|Court Of The Vile Gangster]] || [[2019 European Championship Day 2 Vjeko Keskic LS Old Allies|Old Allies]]
|-
{trow_ralltiir}
|}}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{mrow_ds}
|-
{mrow_ls}
|-
{mrow_watto}
|-
{mrow_htown}
|}}

== See also ==

* [[{KESKIC_COURT_TITLE}]]
* [[{KESKIC_WATTO_TITLE}]]
* [[{KESKIC_HTOWN_TITLE}]]
* [[{KESKIC_LS_TITLE}]]
* [[{KESKIC_DS_TITLE}]]
* [[2002 Ralltiir Regionals]]
* [[2019 European Championship]]
* [[DeckTech decks]]
* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [https://www.starwarsccg.org/2019-european-championships/ 2019 European Championship], starwarsccg.org
{post_source_bullets(23520, "H-TOWN Jedis vs NRW Jedis")}
{post_source_bullets(23561, "All Your Damage Belongs To Watto")}
{post_source_bullets(23606, "Court Likes Direct Damage aka Gailid Superstar")}
{post_source_bullets(23859, "Rumble In The Bronx With Mains")}
{post_source_bullets(26368, "My Keskic Is This Deal Legal aka The Croatian Deal v2 1")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2019]]
[[Category:2002]]
"""


def bouchard_ds_page() -> str:
    start = wiki_card("Set Your Course For Alderaan", "DARK")
    published = "Fear Will Keep Them In Line (V) ALPHA"
    return f"""'''{BOUCHARD_DS_TITLE}''' is the [[Dark]] constructed list [[Maximilien Bouchard]] posted on DeckTech.{post_ref("dt-24965", 24965, published, 'Maximilien "Kiriel" Bouchard, 10 August 2002')} The published list has 61 cards.

== Deck info ==
* '''Player:''' [[Maximilien Bouchard]]
* '''Published:''' 10 August 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' Set Your Course For Alderaan

== Decklist ==

{table_from_rows(BOUCHARD_DS, "DARK")}

{formatted_original_post(24965, description="This deck ROCK, I know there are a lot of FWKTIL deck but this one is a little different. I try to make it the best it could be.")}

== See also ==

* [[Maximilien Bouchard]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24965, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def maximilien_stub_OLD24965() -> str:
    published = "Fear Will Keep Them In Line (V) ALPHA"
    ref = post_ref(
        "dt-24965",
        24965,
        published,
        'Maximilien "Kiriel" Bouchard, 10 August 2002',
    )
    row = (
        "| 10 August 2002 || [[Premiere - Original VS2]] || "
        f"[[{BOUCHARD_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Maximilien Bouchard''' (DeckTech handle '''Kiriel'''){ref} posted a [[Dark]] [[Set Your Course For Alderaan / The Ultimate Power In The Universe|Set Your Course For Alderaan]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24965, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def irving_ds_page() -> str:
    start = wiki_card("Agents Of Black Sun", "DARK")
    published = "3B3-888 Superstar aka Agents of pure BS"
    return f"""'''{IRVING_DS_TITLE}''' is the [[Dark]] constructed list [[John Irving]] posted on DeckTech.{post_ref("dt-24905", 24905, published, 'John "Jirving00" Irving, 7 August 2002')}

== Deck info ==
* '''Player:''' [[John Irving]]
* '''Published:''' 7 August 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' Agents Of Black Sun

== Decklist ==

{table_from_rows(IRVING_DS, "DARK")}

{formatted_original_post(24905, description="Jedi sure are easy to kill when they have no defence value.")}

== See also ==

* [[John Irving]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24905, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def john_irving_page() -> str:
    published = "3B3-888 Superstar aka Agents of pure BS"
    ref = post_ref(
        "dt-24905",
        24905,
        published,
        'John "Jirving00" Irving, 7 August 2002',
    )
    row = (
        "| 7 August 2002 || [[Premiere - Original VS2]] || "
        f"[[{IRVING_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''John Irving''' (DeckTech and Game Players Network handle '''Jirving00'''){ref} posted a [[Dark]] [[Agents Of Black Sun / Vengeance Of The Dark Prince|Agents Of Black Sun]] list on DeckTech (''{published}'') and published constructed lists on [[Game Players Network]].

== Decklists ==

* [[Jirving00 TDIGWATT - The Big Nasty]] (DS, 7 December 2001)

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[Game Players Network decks]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24905, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def jirving00_redirect() -> str:
    return "#REDIRECT [[John Irving]]\n"


def mclain_ls_page() -> str:
    start = wiki_card("Yavin 4: Massassi Throne Room", "LIGHT")
    published = "The Rx Throne Room Wrex"
    return f"""'''{MCLAIN_LS_TITLE}''' is the [[Light]] constructed list [[Ryan McLain]] posted on DeckTech.{post_ref("dt-24807", 24807, published, 'Ryan "_Rx_" McLain, 4 August 2002')} The published list has 59 cards.

== Deck info ==
* '''Player:''' [[Ryan McLain]]
* '''Published:''' 4 August 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' Yavin 4: Massassi Throne Room

== Decklist ==

{table_from_rows(MCLAIN_LS, "LIGHT")}

{formatted_original_post(24807, description="High destiny, power characters, and total darkside acrivation hate.")}

== See also ==

* [[Ryan McLain]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24807, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def ryan_mclain_stub() -> str:
    published = "The Rx Throne Room Wrex"
    ref = post_ref(
        "dt-24807",
        24807,
        published,
        'Ryan "_Rx_" McLain, 4 August 2002',
    )
    row = (
        "| 4 August 2002 || [[Premiere - Original VS2]] || "
        f"[[{MCLAIN_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Ryan McLain''' (DeckTech handle '''_Rx_'''){ref} posted a [[Light]] [[Yavin 4: Massassi Throne Room]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24807, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def sneed_ds_page() -> str:
    start = wiki_card("My Lord, Is That Legal?", "DARK")
    published = "Subterranean Homesick Alien"
    return f"""'''{SNEED_DS_TITLE}''' is the [[Dark]] constructed list [[Michael Sneed]] posted on DeckTech after winning the [[Tulsa Mini-Open]].{post_ref("dt-24783", 24783, published, 'Michael "admiralpiett" Sneed, 2 August 2002')}

== Deck info ==
* '''Player:''' [[Michael Sneed]]
* '''Event:''' [[Tulsa Mini-Open]]
* '''Finish:''' 1
* '''Published:''' 2 August 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' My Lord, Is That Legal!

== Decklist ==

{table_from_rows(SNEED_DS, "DARK")}

{formatted_original_post(24783, description="This is the deck that has served me and my brother quite well, and the deck I used to win the Tulsa Mini-Open.")}

== See also ==

* [[Tulsa Mini-Open]]
* [[Michael Sneed]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24783, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def michael_sneed_stub() -> str:
    published = "Subterranean Homesick Alien"
    ref = post_ref(
        "dt-24783",
        24783,
        published,
        'Michael "admiralpiett" Sneed, 2 August 2002',
    )
    row = (
        "| August 2002 || [[Tulsa Mini-Open]] || [[Premiere - Original VS2]] || 1 || "
        f"[[{SNEED_DS_TITLE}|My Lord, Is That Legal!]] || —"
    )
    return f"""'''Michael Sneed''' (DeckTech handle '''admiralpiett'''){ref} won the [[Tulsa Mini-Open]] with a [[Dark]] [[My Lord, Is That Legal? / I Will Make It Legal|My Lord, Is That Legal!]] list (''{published}'').

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{row}
|}}

== See also ==

* [[Tulsa Mini-Open]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24783, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def tulsa_mini_open() -> str:
    published = "Subterranean Homesick Alien"
    ref = post_ref(
        "dt-24783",
        24783,
        published,
        'Michael "admiralpiett" Sneed, 2 August 2002',
    )
    return f"""'''Tulsa Mini-Open''' was a constructed Star Wars CCG tournament in Tulsa in August 2002. [[Michael Sneed]] won with a [[Dark]] [[My Lord, Is That Legal? / I Will Make It Legal|My Lord, Is That Legal!]] list (''{published}'').{ref}

* '''Dates:''' August 2002
* '''Site:''' Tulsa
* '''Format:''' [[Premiere - Original VS2]]
* '''Winner:''' [[Michael Sneed]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Michael Sneed]] || [[{SNEED_DS_TITLE}|My Lord, Is That Legal!]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Michael Sneed]]

== Sources ==

{post_source_bullets(24783, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def patch_list() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "2002 Dantooine Regionals" in text:
        print("List already has 2002 Dantooine Regionals")
        return
    origins = (
        "| 2002-07 || [[2002 Origins Open]] || 4–7 July 2002 || Columbus, Ohio || "
        "[[Premiere - Original VS2]] || —\n"
    )
    row = (
        "| 2002 || [[2002 Dantooine Regionals]] || 2002 || — || "
        "[[Premiere - Original VS2]] || —\n"
    )
    if origins not in text:
        print("WARN List Origins row not found")
        return
    path.write_text(
        text.replace(origins, origins + "|-\n" + row, 1),
        encoding="utf-8",
        newline="\n",
    )
    print("patched List Dantooine")


def justin_stub() -> str:
    published = "we will reveal ourselves to the jedi at last we will have revenge"
    ref = post_ref(
        "dt-25033",
        25033,
        published,
        'Justin "Black 1" Fiedler, 13 August 2002',
    )
    row = (
        "| 13 August 2002 || [[Premiere - Original VS3]] || "
        f"[[{FIEDLER_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Justin Fiedler''' (DeckTech handle '''Black 1'''){ref} posted a [[Dark]] [[Let Them Make The First Move / At Last We Will Have Revenge|Let Them Make The First Move]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(25033, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def marshall_ls_page() -> str:
    start = wiki_card("Quiet Mining Colony", "LIGHT")
    published = "Viperstyle - Keeping The Senators Out Forever"
    return f"""'''{MARSHALL_LS_TITLE}''' is the [[Light]] constructed list [[Steve Marshall]] posted on DeckTech.{post_ref("dt-24688", 24688, published, 'Steve "BlackViper" Marshall, 30 July 2002')}

== Deck info ==
* '''Player:''' [[Steve Marshall]]
* '''Published:''' 30 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' Quiet Mining Colony

== Decklist ==

{table_from_rows(MARSHALL_LS, "LIGHT")}

{formatted_original_post(24688, description="Viper's way of defeating Senate and Combat, as well as most everything else. Light side is bleeding right now - this is its band-aid")}

== See also ==

* [[Steve Marshall]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24688, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def steve_marshall_stub() -> str:
    published = "Viperstyle - Keeping The Senators Out Forever"
    ref = post_ref(
        "dt-24688",
        24688,
        published,
        'Steve "BlackViper" Marshall, 30 July 2002',
    )
    row = (
        "| 30 July 2002 || [[Premiere - Original VS2]] || "
        f"[[{MARSHALL_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Steve Marshall''' (DeckTech handle '''BlackViper'''){ref} posted a [[Light]] [[Quiet Mining Colony / Independent Operation|Quiet Mining Colony]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24688, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def cross_ls_page() -> str:
    start = wiki_card("You Can Either Profit By This...", "LIGHT")
    published = "Squires Origins Profit"
    return f"""'''{CROSS_LS_TITLE}''' is the [[Light]] constructed list [[Ken Cross]] posted on DeckTech after finishing 7th at the [[2002 Origins Open]].{post_ref("dt-24668", 24668, published, 'Ken "Squires" Cross, 29 July 2002')}

== Deck info ==
* '''Player:''' [[Ken Cross]]
* '''Event:''' [[2002 Origins Open]]
* '''Finish:''' 7
* '''Published:''' 29 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Podrace Prep", "LIGHT")}
* '''Strategy:''' You Can Either Profit By This...

== Decklist ==

{table_from_rows(CROSS_LS, "LIGHT")}

{formatted_original_post(24668, description="Origins wasd a while ago, but here is my Profit deck that went 3-0 in the open and got me 7th place.")}

== See also ==

* [[2002 Origins Open]]
* [[Ken Cross]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24668, published)}
* [{ORIGINS_2002_WB} Origins 2002], decipher.com (Wayback, 2 August 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def ken_cross_inject() -> str:
    path = PAGES / "Ken_Cross.wiki"
    text = path.read_text(encoding="utf-8")
    published = "Squires Origins Profit"
    ref = post_ref(
        "dt-24668",
        24668,
        published,
        'Ken "Squires" Cross, 29 July 2002',
    )
    old = "'''Ken Cross''' played the"
    new = f"'''Ken Cross''' (DeckTech handle '''Squires'''){ref} played the"
    if old in text and "dt-24668" not in text:
        text = text.replace(old, new, 1)
    fact = (
        " He finished 7th at the [[2002 Origins Open]] with a [[Light]] "
        "[[You Can Either Profit By This... / Or Be Destroyed|You Can Either Profit By This...]] "
        f"list (''{published}'')."
    )
    if "2002 Origins Open" not in text.split("== Tournament Results ==")[0]:
        marker = "\n\n== Tournament Results =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
    row = (
        "| 4–7 July 2002 || [[2002 Origins Open]] || [[Premiere - Original VS2]] || 7 || "
        f"— || [[{CROSS_LS_TITLE}|You Can Either Profit By This...]]"
    )
    text = add_result_row(text, row)
    text = add_see_also(text, "* [[2002 Origins Open]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(24668, published) + "\n")
    text = add_category(text, "2002")
    return text


def origins_2002_open() -> str:
    published = "Squires Origins Profit"
    ref = post_ref(
        "dt-24668",
        24668,
        published,
        'Ken "Squires" Cross, 29 July 2002',
    )
    return f"""'''2002 Origins Open''' was a constructed Star Wars CCG tournament at Origins 2002 (4–7 July 2002) in Columbus, Ohio. [[Ken Cross]] finished 7th in the open with a [[Light]] [[You Can Either Profit By This... / Or Be Destroyed|You Can Either Profit By This...]] list (''{published}'', 3–0 as posted).{ref}<ref name="origins-2002">[{ORIGINS_2002_WB} Origins 2002], decipher.com (Wayback, 2 August 2002)</ref>

* '''Dates:''' 4–7 July 2002
* '''Site:''' Columbus, Ohio
* '''Format:''' [[Premiere - Original VS2]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 7 || [[Ken Cross]] || — || [[{CROSS_LS_TITLE}|You Can Either Profit By This...]]
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Ken Cross]]
* [[1999 Origins Open]]

== Sources ==

{post_source_bullets(24668, published)}
* [{ORIGINS_2002_WB} Origins 2002], decipher.com (Wayback, 2 August 2002)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def warren_ds_page() -> str:
    start = wiki_card("Hunt Down And Destroy The Jedi", "DARK")
    published = "Raging Bull (Hoostino's Hunt Down Hammer)"
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in WARREN_SHIELDS
    )
    return f"""'''{WARREN_DS_TITLE}''' is the [[Dark]] constructed list [[Justin Warren]] posted on DeckTech after finishing 1st at the [[2002 Houston Mini-Open]] and 2nd at the [[2002 Houston DPC]].{post_ref("dt-24516", 24516, published, 'Justin "hoostino" Warren, 20 July 2002')}

== Deck info ==
* '''Player:''' [[Justin Warren]]
* '''Published:''' 20 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Strategy:''' Hunt Down And Destroy The Jedi

== Decklist ==

{table_from_rows(WARREN_DS, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(24516, description="This deck went 6-0 in the sanctioned games at the Houston Mini-Open and the Houston DPC. I took first and second at those events respectively, and have this deck to thank for it.")}

== See also ==

* [[2002 Houston Mini-Open]]
* [[2002 Houston DPC]]
* [[Justin Warren]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24516, published)}
* [{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], Stephen Skilton
* [{HOUSTON_DPC_TR_GH} houston-texas-07-14-02-dpc-houston] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def justin_warren_stub() -> str:
    published = "Raging Bull (Hoostino's Hunt Down Hammer)"
    ref = post_ref(
        "dt-24516",
        24516,
        published,
        'Justin "hoostino" Warren, 20 July 2002',
    )
    row_dpc = (
        "| 14 July 2002 || [[2002 Houston DPC]] || [[Premiere - Original VS2]] || 2 || "
        f"[[{WARREN_DS_TITLE}|Hunt Down And Destroy The Jedi]] || —"
    )
    row_mini = (
        "| July 2002 || [[2002 Houston Mini-Open]] || [[Premiere - Original VS2]] || 1 || "
        f"[[{WARREN_DS_TITLE}|Hunt Down And Destroy The Jedi]] || —"
    )
    return f"""'''Justin Warren''' (DeckTech handle '''hoostino'''){ref} won the [[2002 Houston Mini-Open]] and finished 2nd at the [[2002 Houston DPC]] with a [[Dark]] [[Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe|Hunt Down And Destroy The Jedi]] list (''{published}'').

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{row_dpc}
|-
{row_mini}
|}}

== See also ==

* [[2002 Houston DPC]]
* [[2002 Houston Mini-Open]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24516, published)}
* [{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], Stephen Skilton
* [{HOUSTON_DPC_TR_GH} houston-texas-07-14-02-dpc-houston] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def houston_mini_open() -> str:
    published = "Raging Bull (Hoostino's Hunt Down Hammer)"
    ref = post_ref(
        "dt-24516",
        24516,
        published,
        'Justin "hoostino" Warren, 20 July 2002',
    )
    return f"""'''2002 Houston Mini-Open''' was a constructed Star Wars CCG tournament in Houston, Texas in July 2002. [[Justin Warren]] won with a [[Dark]] [[Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe|Hunt Down And Destroy The Jedi]] list (''{published}'').{ref}

* '''Dates:''' July 2002
* '''Site:''' Houston, Texas
* '''Format:''' [[Premiere - Original VS2]]
* '''Winner:''' [[Justin Warren]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Justin Warren]] || [[{WARREN_DS_TITLE}|Hunt Down And Destroy The Jedi]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[2002 Houston DPC]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Justin Warren]]

== Sources ==

{post_source_bullets(24516, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def houston_dpc() -> str:
    published = "Raging Bull (Hoostino's Hunt Down Hammer)"
    burnett_published = "JediGamler's Watto aka The Unstoppable Machine"
    ref = post_ref(
        "dt-24516",
        24516,
        published,
        'Justin "hoostino" Warren, 20 July 2002',
    )
    burnett_ref = post_ref(
        "dt-24511",
        24511,
        burnett_published,
        'David "JediGambler" Burnett, 20 July 2002',
    )
    tr = (
        f'<ref name="dpc-houston-tr">[{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], '
        f'Jacob "Armaedes" Taylor, DeckTech (16 July 2002). Preservation copy: '
        f"[{HOUSTON_DPC_TR_GH} GitHub Pages].</ref>"
    )
    return f"""'''2002 Houston DPC''' was a constructed Star Wars CCG Decipher Player Championship on 14 July 2002 in Houston, Texas. [[Brian Hunter]] won. [[Justin Warren]] finished 2nd with a [[Dark]] [[Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe|Hunt Down And Destroy The Jedi]] list (''{published}'').{ref} [[David Burnett]] went 2-1 with a [[Dark]] [[No Money, No Parts, No Deal! / You're A Slave?|No Money, No Parts, No Deal!]] list (''{burnett_published}'').{burnett_ref}{tr}

* '''Dates:''' 14 July 2002
* '''Site:''' Houston, Texas
* '''Format:''' [[Premiere - Original VS2]]
* '''Winner:''' [[Brian Hunter]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Brian Hunter]] || — || —
|-
| 2 || [[Justin Warren]] || [[{WARREN_DS_TITLE}|Hunt Down And Destroy The Jedi]] || —
|-
| 2-1 || [[David Burnett]] || [[{BURNETT_DS_TITLE}|No Money, No Parts, No Deal!]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[2002 Houston Mini-Open]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Justin Warren]]
* [[Brian Hunter]]
* [[David Burnett]]

== Sources ==

{post_source_bullets(24516, published)}
{post_source_bullets(24511, burnett_published)}
* [{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], Stephen Skilton
* [{HOUSTON_DPC_TR_GH} houston-texas-07-14-02-dpc-houston] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def burnett_ds_page() -> str:
    start = wiki_card("No Money, No Parts, No Deal!", "DARK")
    published = "JediGamler's Watto aka The Unstoppable Machine"
    return f"""'''{BURNETT_DS_TITLE}''' is the [[Dark]] constructed list [[David Burnett]] posted on DeckTech. [[Aaron Pawlik]] went 3-0 with it at the [[2002 Dantooine Regionals]]. Burnett went 2-1 with it at the [[2002 Houston DPC]].{post_ref("dt-24511", 24511, published, 'David "JediGambler" Burnett, 20 July 2002')}

== Deck info ==
* '''Player:''' [[David Burnett]]
* '''Published:''' 20 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' No Money, No Parts, No Deal!

== Decklist ==

{table_from_rows(BURNETT_DS, "DARK")}

{formatted_original_post(24511, description="Went 3-0 at Dantooine regional in the hands of Aaron Pawlik with 20 or higher dif each game. Went 2-1 at DPC Houston for me (the maker) with only a timed loss to Matt Lush (luck). As Aaron calls it a Machine.")}

== See also ==

* [[2002 Dantooine Regionals]]
* [[2002 Houston DPC]]
* [[David Burnett]]
* [[Aaron Pawlik]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24511, published)}
* [{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], Stephen Skilton
* [{HOUSTON_DPC_TR_GH} houston-texas-07-14-02-dpc-houston] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def david_burnett_stub() -> str:
    published = "JediGamler's Watto aka The Unstoppable Machine"
    ref = post_ref(
        "dt-24511",
        24511,
        published,
        'David "JediGambler" Burnett, 20 July 2002',
    )
    row = (
        "| 14 July 2002 || [[2002 Houston DPC]] || [[Premiere - Original VS2]] || 2-1 || "
        f"[[{BURNETT_DS_TITLE}|No Money, No Parts, No Deal!]] || —"
    )
    return f"""'''David Burnett''' (DeckTech handle '''JediGambler'''){ref} posted a [[Dark]] [[No Money, No Parts, No Deal! / You're A Slave?|No Money, No Parts, No Deal!]] list on DeckTech (''{published}''). He went 2-1 with it at the [[2002 Houston DPC]].

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{row}
|}}

== See also ==

* [[2002 Houston DPC]]
* [[2002 Dantooine Regionals]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24511, published)}
* [{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], Stephen Skilton
* [{HOUSTON_DPC_TR_GH} houston-texas-07-14-02-dpc-houston] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def aaron_pawlik_stub() -> str:
    published = "JediGamler's Watto aka The Unstoppable Machine"
    ref = post_ref(
        "dt-24511",
        24511,
        published,
        'David "JediGambler" Burnett, 20 July 2002',
    )
    row = (
        "| 2002 || [[2002 Dantooine Regionals]] || [[Premiere - Original VS2]] || 3-0 || "
        f"[[{BURNETT_DS_TITLE}|No Money, No Parts, No Deal!]] || —"
    )
    return f"""'''Aaron Pawlik''' went 3-0 at the [[2002 Dantooine Regionals]] with [[David Burnett]]'s [[Dark]] [[No Money, No Parts, No Deal! / You're A Slave?|No Money, No Parts, No Deal!]] list (''{published}'').{ref}

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{row}
|}}

== See also ==

* [[2002 Dantooine Regionals]]
* [[David Burnett]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24511, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def dantooine_regionals() -> str:
    published = "JediGamler's Watto aka The Unstoppable Machine"
    ref = post_ref(
        "dt-24511",
        24511,
        published,
        'David "JediGambler" Burnett, 20 July 2002',
    )
    return f"""'''2002 Dantooine Regionals''' was a constructed Star Wars CCG regional in 2002. [[Aaron Pawlik]] went 3-0 with [[David Burnett]]'s [[Dark]] [[No Money, No Parts, No Deal! / You're A Slave?|No Money, No Parts, No Deal!]] list (''{published}'').{ref}

* '''Dates:''' 2002
* '''Format:''' [[Premiere - Original VS2]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 3-0 || [[Aaron Pawlik]] || [[{BURNETT_DS_TITLE}|No Money, No Parts, No Deal!]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[2002 Houston DPC]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Aaron Pawlik]]
* [[David Burnett]]

== Sources ==

{post_source_bullets(24511, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def brian_hunter_inject() -> str:
    path = PAGES / "Brian_Hunter.wiki"
    text = path.read_text(encoding="utf-8")
    published = "Raging Bull (Hoostino's Hunt Down Hammer)"
    ref = (
        f'<ref name="dpc-houston-tr">[{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], '
        f'Jacob "Armaedes" Taylor, DeckTech (16 July 2002). Preservation copy: '
        f"[{HOUSTON_DPC_TR_GH} GitHub Pages].</ref>"
    )
    old = "'''Brian Hunter''' finished 2nd"
    new = f"'''Brian Hunter''' won the [[2002 Houston DPC]].{ref} He finished 2nd"
    if old in text and "2002 Houston DPC" not in text.split("== Tournament Results ==")[0]:
        text = text.replace(old, new, 1)
    row = (
        "| 14 July 2002 || [[2002 Houston DPC]] || [[Premiere - Original VS2]] || 1 || "
        "— || —"
    )
    text = add_result_row(text, row)
    text = add_see_also(text, "* [[2002 Houston DPC]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    src = (
        f"* [{HOUSTON_DPC_TR} houston-texas-07-14-02-dpc-houston], Stephen Skilton\n"
        f"* [{HOUSTON_DPC_TR_GH} houston-texas-07-14-02-dpc-houston] (GitHub Pages)\n"
        + post_source_bullets(24516, published)
        + "\n"
    )
    text = add_source_line(text, src)
    text = add_category(text, "2002")
    return text


def nystrom_ds_page() -> str:
    start = wiki_card("Set Your Course For Alderaan", "DARK")
    published = "Empire is virtually back"
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in NYSTROM_SHIELDS
    )
    return f"""'''{NYSTROM_DS_TITLE}''' is the [[Dark]] constructed list [[Pyry Nystrom]] posted on DeckTech.{post_ref("dt-24274", 24274, published, 'Pyry "Blizzard" Nystrom, 8 July 2002')}

== Deck info ==
* '''Player:''' [[Pyry Nystrom]]
* '''Published:''' 8 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Start Your Engines!", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' Special SYCFA that will not flip, instead it wins games... Uses many (V)-cards for advantage

== Decklist ==

{table_from_rows(NYSTROM_DS, "DARK")}

== Defensive Shields ==

These five named cards were posted as Defensive Shields outside the 60 (plus unnamed others). They do not count toward the 60.

{shields}

{formatted_original_post(24274, description="Special SYCFA that will not flip, instead it wins games... Uses many (V)-cards for advantage")}

== See also ==

* [[Pyry Nystrom]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24274, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def pyry_nystrom_stub() -> str:
    published = "Empire is virtually back"
    ref = post_ref(
        "dt-24274",
        24274,
        published,
        'Pyry "Blizzard" Nystrom, 8 July 2002',
    )
    row = (
        "| 8 July 2002 || [[Premiere - Original VS2]] || "
        f"[[{NYSTROM_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Pyry Nystrom''' (DeckTech handle '''Blizzard'''){ref} posted a [[Dark]] [[Set Your Course For Alderaan / The Ultimate Power In The Universe|Set Your Course For Alderaan]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24274, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def van_winkle_ds_page() -> str:
    start = wiki_card("Hunt Down And Destroy The Jedi", "DARK")
    published = "Seth's Mad Huntdown Deck"
    return f"""'''{VAN_WINKLE_DS_TITLE}''' is the [[Dark]] constructed list [[Seth Van Winkle]] posted on DeckTech.{post_ref("dt-24316", 24316, published, 'Seth "Ooryl" Van Winkle, 10 July 2002')}

== Deck info ==
* '''Player:''' [[Seth Van Winkle]]
* '''Published:''' 10 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' huntdown

== Decklist ==

{table_from_rows(VAN_WINKLE_DS, "DARK")}

{formatted_original_post(24316, description="Its a huntdown deck.")}

== See also ==

* [[Seth Van Winkle]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24316, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def seth_van_winkle_stub() -> str:
    published = "Seth's Mad Huntdown Deck"
    ref = post_ref(
        "dt-24316",
        24316,
        published,
        'Seth "Ooryl" Van Winkle, 10 July 2002',
    )
    row = (
        "| 10 July 2002 || [[Premiere - Original VS2]] || "
        f"[[{VAN_WINKLE_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Seth Van Winkle''' (DeckTech handle '''Ooryl'''){ref} posted a [[Dark]] [[Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe|Hunt Down And Destroy The Jedi]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24316, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def krueger_beach_page() -> str:
    start = wiki_card("Tatooine: Desert Landing Site", "DARK")
    published = "the beast on the beach v2"
    return f"""'''{KRUEGER_BEACH_TITLE}''' is the [[Dark]] constructed list [[Kyle Krueger]] posted on DeckTech. He wrote that it was 12-0 in four tournaments (two locals, the Endor Regionals, and RebelCon).{post_ref("dt-24467", 24467, published, 'Kyle "Meto" Krueger, 18 July 2002')}

== Deck info ==
* '''Player:''' [[Kyle Krueger]]
* '''Published:''' 18 July 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Combat Readiness", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' mains beatdown

== Decklist ==

{table_from_rows(KRUEGER_BEACH_DS, "DARK")}

{formatted_original_post(24467, description="mains beatdown.  undefeated in tourney play.  wins by a lot.")}

== See also ==

* [[Kyle Krueger]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24467, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def patch_kyle_krueger_24467() -> None:
    path = PAGES / "Kyle_Krueger.wiki"
    text = path.read_text(encoding="utf-8")
    published = "the beast on the beach v2"
    ref = post_ref(
        "dt-24467",
        24467,
        published,
        'Kyle "Meto" Krueger, 18 July 2002',
    )
    fact = (
        f" He posted a [[Dark]] [[Tatooine: Desert Landing Site]] list on DeckTech "
        f"(''{published}'').{ref}"
    )
    if published not in text.split("== Tournament Results ==")[0]:
        marker = "\n\n== Tournament Results =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
            print("PATCHED Kyle Krueger 24467 lead")
        else:
            print("WARN Kyle Krueger Tournament Results marker missing")
    row = (
        "| 18 July 2002 || [[Premiere - Original VS2]] || "
        f"[[{KRUEGER_BEACH_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{KRUEGER_BEACH_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(24467, published) + "\n")
    text = add_category(text, "2002")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Kyle Krueger 24467")


def kafer_ds_page() -> str:
    start = wiki_card("Let Them Make The First Move", "DARK")
    published = "LSC TacoBill style"
    return f"""'''{KAFER_DS_TITLE}''' is the [[Dark]] constructed list [[Bill Kafer]] posted on DeckTech.{post_ref("dt-24142", 24142, published, 'Bill "TacoBill" Kafer, 27 June 2002')}

== Deck info ==
* '''Player:''' [[Bill Kafer]]
* '''Published:''' 27 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' A very solid LSC deck that wins and can win really big. High destiny, big drains, what more do you want?

== Decklist ==

{table_from_rows(KAFER_DS, "DARK")}

{formatted_original_post(24142, description="A very solid LSC deck that wins and can win really big. High destiny, big drains, what more do you want?")}

== See also ==

* [[Bill Kafer]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24142, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def patch_bill_kafer_24142() -> None:
    path = PAGES / "Bill_Kafer.wiki"
    text = path.read_text(encoding="utf-8")
    published = "LSC TacoBill style"
    ref = post_ref(
        "dt-24142",
        24142,
        published,
        'Bill "TacoBill" Kafer, 27 June 2002',
    )
    old = "'''Bill Kafer''' (forum TacoBill)"
    new = f"'''Bill Kafer''' (forum TacoBill; DeckTech handle '''TacoBill'''){ref}"
    if old in text and "dt-24142" not in text:
        text = text.replace(old, new, 1)
        print("PATCHED Bill Kafer 24142 handle")
    fact = (
        " He posted a [[Dark]] "
        "[[Let Them Make The First Move / At Last We Will Have Revenge|Let Them Make The First Move]] "
        f"list on DeckTech (''{published}'')."
    )
    lead = text.split("== Tournament Results ==")[0]
    if "list on DeckTech" not in lead:
        marker = "\n\n== Tournament Results =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
            print("PATCHED Bill Kafer 24142 lead")
        else:
            print("WARN Bill Kafer Tournament Results marker missing")
    row = (
        "| 27 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{KAFER_DS_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{KAFER_DS_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(24142, published) + "\n")
    text = add_category(text, "2002")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Bill Kafer 24142")


def beach_v1_page() -> str:
    start = wiki_card("Tatooine: Desert Landing Site", "DARK")
    published = "The Beast on the Beach"
    return f"""'''{BEACH_V1_TITLE}''' is the [[Dark]] constructed list [[Kyle Krueger]] posted on DeckTech. He wrote that it was undefeated in three tournaments (two locals and the Endor Regionals) and beat John Hawkins by 24.{post_ref("dt-24104", 24104, published, 'Kyle "Meto" Krueger, 24 June 2002')}

== Deck info ==
* '''Player:''' [[Kyle Krueger]]
* '''Published:''' 24 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Combat Readiness", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' An efficient deck, with mains and high destiny.  Has some sweet tech and good counters for most decks.

== Decklist ==

{table_from_rows(BEACH_V1_DS, "DARK")}

{formatted_original_post(24104, description="An efficient deck, with mains and high destiny.  Has some sweet tech and good counters for most decks.")}

== See also ==

* [[Kyle Krueger]]
* [[Kyle Krueger the beast on the beach v2]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24104, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def patch_kyle_krueger_24104() -> None:
    path = PAGES / "Kyle_Krueger.wiki"
    text = path.read_text(encoding="utf-8")
    published = "The Beast on the Beach"
    ref = post_ref(
        "dt-24104",
        24104,
        published,
        'Kyle "Meto" Krueger, 24 June 2002',
    )
    fact = (
        " He also posted an earlier [[Dark]] [[Tatooine: Desert Landing Site]] list "
        f"on DeckTech (''{published}'').{ref}"
    )
    lead = text.split("== Tournament Results ==")[0]
    if published not in lead:
        marker = "\n\n== Tournament Results =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
            print("PATCHED Kyle Krueger 24104 lead")
        else:
            print("WARN Kyle Krueger Tournament Results marker missing")
    row = (
        "| 24 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{BEACH_V1_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{BEACH_V1_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(24104, published) + "\n")
    text = add_category(text, "2002")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Kyle Krueger 24104")


def saber_ls_page() -> str:
    start = wiki_card("We'll Handle This / Duel Of The Fates", "LIGHT")
    published = "Saber combat my way"
    return f"""'''{SABER_LS_TITLE}''' is the [[Light]] constructed list [[Mike (Quione)]] posted on DeckTech.{post_ref("dt-24089", 24089, published, 'Mike "Quione" Noneofyourbusiness, 24 June 2002')}

== Deck info ==
* '''Player:''' [[Mike (Quione)]]
* '''Published:''' 24 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Podrace Prep", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' LS combat with a unique twist

== Decklist ==

{table_from_rows(SABER_LS, "LIGHT")}

{formatted_original_post(24089, description="LS combat with a unique twist")}

== See also ==

* [[Mike (Quione)]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24089, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def mike_quione_stub() -> str:
    published = "Saber combat my way"
    published_rst = "Rebel Strike Team- Stay the hell of endor"
    ref = post_ref(
        "dt-24089",
        24089,
        published,
        'Mike "Quione" Noneofyourbusiness, 24 June 2002',
    )
    ref_rst = post_ref(
        "dt-23490",
        23490,
        published_rst,
        'Mike "Quione" Noneofyourbusiness, 22 May 2002',
    )
    row = (
        "| 24 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{SABER_LS_TITLE}|{published}]] || [[Light]]"
    )
    row_rst = (
        "| 22 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{QUIONE_RST_TITLE}|{published_rst}]] || [[Light]]"
    )
    hat = "{{" + "Hatnote|[[Mike]] redirects to [[Mike Thomas]]." + "}}"
    return f"""{hat}
'''Mike''' (DeckTech handle '''Quione'''){ref} posted a [[Light]] [[We'll Handle This / Duel Of The Fates|We'll Handle This]] list on DeckTech (''{published}'') and a [[Light]] [[Rebel Strike Team / Garrison Destroyed|Rebel Strike Team]] list (''{published_rst}'').{ref_rst}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|-
{row_rst}
|}}

== See also ==

* [[{SABER_LS_TITLE}]]
* [[{QUIONE_RST_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23490, published_rst)}
{post_source_bullets(24089, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def carulli_ds_page() -> str:
    start = wiki_card(
        "Court Of The Vile Gangster / I Shall Enjoy Watching You Die", "DARK"
    )
    published = "Hunt Down and Revive the SCUM"
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in CARULLI_SHIELDS
    )
    return f"""'''{CARULLI_DS_TITLE}''' is the [[Dark]] constructed list [[Matt Carulli]] posted on DeckTech.{post_ref("dt-24026", 24026, published, 'Matt "QuiGon57" Carulli, 19 June 2002')}

== Deck info ==
* '''Player:''' [[Matt Carulli]]
* '''Published:''' 19 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' This Court deck does a few things most other Court decks dont: Capture cards and win But it still needs help so please review

== Decklist ==

{table_from_rows(CARULLI_DS, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(24026, description="This Court deck does a few things most other Court decks dont: Capture cards and win But it still needs help so please review")}

== See also ==

* [[Matt Carulli]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24026, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def patch_matt_carulli_24026() -> None:
    path = PAGES / "Matt_Carulli.wiki"
    text = path.read_text(encoding="utf-8")
    published = "Hunt Down and Revive the SCUM"
    ref = post_ref(
        "dt-24026",
        24026,
        published,
        'Matt "QuiGon57" Carulli, 19 June 2002',
    )
    old = "'''Matt Carulli''' is listed as"
    new = f"'''Matt Carulli''' (DeckTech handle '''QuiGon57'''){ref} is listed as"
    if old in text and "QuiGon57" not in text:
        text = text.replace(old, new, 1)
        print("PATCHED Matt Carulli handle")
    fact = (
        " He posted a [[Dark]] "
        "[[Court Of The Vile Gangster / I Shall Enjoy Watching You Die|Court Of The Vile Gangster]] "
        f"list on DeckTech (''{published}'')."
    )
    if "list on DeckTech" not in text:
        marker = "\n\n== Documented PC roles =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
            print("PATCHED Matt Carulli 24026 lead")
        else:
            print("WARN Matt Carulli Documented PC roles marker missing")
    row = (
        "| 19 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{CARULLI_DS_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{CARULLI_DS_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(24026, published) + "\n")
    text = add_category(text, "2002")
    see = text.find("== See also ==")
    src = text.find("\n== Sources ==", see)
    if see >= 0 and src > see:
        kept: list[str] = []
        for line in text[see:src].splitlines(True):
            if line.strip() == "" and kept and kept[-1].lstrip().startswith("*"):
                continue
            kept.append(line)
        text = text[:see] + "".join(kept) + text[src:]
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Matt Carulli 24026")


def davis_ds_page() -> str:
    start = wiki_card(
        "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further",
        "DARK",
    )
    published = "TDIGWATT/PIDAIAF CC Dark Deal Deck"
    return f"""'''{DAVIS_DS_TITLE}''' is the [[Dark]] constructed list [[Chris Davis]] posted on DeckTech.{post_ref("dt-24025", 24025, published, 'Chris "Fred" Davis, 19 June 2002')}

== Deck info ==
* '''Player:''' [[Chris Davis]]
* '''Published:''' 19 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Strategy:''' Fast Dark Deal deck.

== Decklist ==

{table_from_rows(DAVIS_DS, "DARK")}

{formatted_original_post(24025, description="Fast Dark Deal deck.")}

== See also ==

* [[Chris Davis]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24025, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def chris_davis_stub() -> str:
    published = "TDIGWATT/PIDAIAF CC Dark Deal Deck"
    ref = post_ref(
        "dt-24025",
        24025,
        published,
        'Chris "Fred" Davis, 19 June 2002',
    )
    row = (
        "| 19 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{DAVIS_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Chris Davis''' (DeckTech handle '''Fred'''){ref} posted a [[Dark]] [[This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further|This Deal Is Getting Worse All The Time]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{DAVIS_DS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24025, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def mann_ls_page() -> str:
    start = wiki_card(
        "Watch Your Step / This Place Can Be A Little Rough", "LIGHT"
    )
    published = "What my step It’s yours I should be watching"
    desc = "My first WYS deck: heavy strategy and tech, meant for fighting ground and space. I would really appreciate any advice"
    return f"""'''{MANN_LS_TITLE}''' is the [[Light]] constructed list [[Zach Mann]] posted on DeckTech.{post_ref("dt-24003", 24003, published, 'Zach "Greedosalive" Mann, 17 June 2002')}

== Deck info ==
* '''Player:''' [[Zach Mann]]
* '''Published:''' 17 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(MANN_LS, "LIGHT")}

{formatted_original_post(24003, description=desc)}

== See also ==

* [[Zach Mann]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24003, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def zach_mann_stub() -> str:
    published = "What my step It’s yours I should be watching"
    ref = post_ref(
        "dt-24003",
        24003,
        published,
        'Zach "Greedosalive" Mann, 17 June 2002',
    )
    row = (
        "| 17 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{MANN_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Zach Mann''' (DeckTech handle '''Greedosalive'''){ref} posted a [[Light]] [[Watch Your Step / This Place Can Be A Little Rough|Watch Your Step]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{MANN_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24003, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def nelson_ds_page() -> str:
    start = wiki_card(
        "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further",
        "DARK",
    )
    published = "Droid Deal v 1 0"
    desc = "Battle Droids on Cloud City."
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in NELSON_SHIELDS
    )
    return f"""'''{NELSON_DS_TITLE}''' is the [[Dark]] constructed list [[Adam Nelson]] posted on DeckTech.{post_ref("dt-23994", 23994, published, 'Adam "Skipray" Nelson, 17 June 2002')}

== Deck info ==
* '''Player:''' [[Adam Nelson]]
* '''Published:''' 17 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(NELSON_DS, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23994, description=desc)}

== See also ==

* [[Adam Nelson]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23994, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def patch_adam_nelson() -> None:
    path = PAGES / "Adam_Nelson.wiki"
    text = path.read_text(encoding="utf-8")
    published = "Droid Deal v 1 0"
    ref = post_ref(
        "dt-23994",
        23994,
        published,
        'Adam "Skipray" Nelson, 17 June 2002',
    )
    old = "'''Adam Nelson''' is a Star Wars"
    new = f"'''Adam Nelson''' (DeckTech handle '''Skipray'''){ref} is a Star Wars"
    if old in text and "Skipray" not in text:
        text = text.replace(old, new, 1)
        print("PATCHED Adam Nelson handle")
    fact = (
        " He posted a [[Dark]] "
        "[[This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further|This Deal Is Getting Worse All The Time]] "
        f"list on DeckTech (''{published}'')."
    )
    if "list on DeckTech" not in text:
        marker = "\n\n== Tournament Results =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
            print("PATCHED Adam Nelson 23994 lead")
        else:
            print("WARN Adam Nelson Tournament Results marker missing")
    row = (
        "| 17 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{NELSON_DS_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    if "== Sources ==" not in text:
        cat = text.find("\n[[Category:")
        sources = (
            "\n== Sources ==\n\n"
            f"{post_source_bullets(23994, published)}\n\n"
            "{{#if:1|<nowiki />\n"
            "<h2>References</h2>\n"
            "<references />}}\n"
        )
        if cat >= 0:
            text = text[:cat] + "\n" + sources + text[cat:]
        else:
            text = text.rstrip() + "\n" + sources
        print("PATCHED Adam Nelson Sources")
    text = add_see_also(text, f"* [[{NELSON_DS_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(23994, published) + "\n")
    text = add_category(text, "2002")
    see = text.find("== See also ==")
    src = text.find("\n== Sources ==", see)
    if see >= 0 and src > see:
        kept: list[str] = []
        for line in text[see:src].splitlines(True):
            if line.strip() == "" and kept and kept[-1].lstrip().startswith("*"):
                continue
            kept.append(line)
        text = text[:see] + "".join(kept) + text[src:]
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Adam Nelson 23994")


def guarino_ls_page() -> str:
    start = wiki_card("Massassi Base Operations / One In A Million", "LIGHT")
    published = "I’m Getting Too Old For This"
    desc = "Ric Olie and the rest of the Bravo Squadron come out of retirement to take out the death star."
    return f"""'''{GUARINO_LS_TITLE}''' is the [[Light]] constructed list [[Mike Guarino]] posted on DeckTech.{post_ref("dt-24020", 24020, published, 'Mike "Darth Dago" Guarino, 19 June 2002')}

== Deck info ==
* '''Player:''' [[Mike Guarino]]
* '''Published:''' 19 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(GUARINO_LS, "LIGHT")}

{formatted_original_post(24020, description=desc)}

== See also ==

* [[Mike Guarino]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24020, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def mike_guarino_stub() -> str:
    published = "I’m Getting Too Old For This"
    ref = post_ref(
        "dt-24020",
        24020,
        published,
        'Mike "Darth Dago" Guarino, 19 June 2002',
    )
    row = (
        "| 19 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{GUARINO_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Mike Guarino''' (DeckTech handle '''Darth Dago'''){ref} posted a [[Light]] [[Massassi Base Operations / One In A Million|Massassi Base Operations]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{GUARINO_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24020, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def mccoy_ls_page() -> str:
    start = wiki_card("Quiet Mining Colony / Independent Operation", "LIGHT")
    published = "Quiet Macking of Cloud city"
    desc = "Nothing special.  Short a couple cards i need to make the deck better"
    return f"""'''{MCCOY_LS_TITLE}''' is the [[Light]] constructed list [[Chris McCoy]] posted on DeckTech.{post_ref("dt-24022", 24022, published, 'Chris "Golfercwm" McCoy, 19 June 2002')}

== Deck info ==
* '''Player:''' [[Chris McCoy]]
* '''Published:''' 19 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(MCCOY_LS, "LIGHT")}

{formatted_original_post(24022, description=desc)}

== See also ==

* [[Chris McCoy]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(24022, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def chris_mccoy_stub() -> str:
    published = "Quiet Macking of Cloud city"
    ref = post_ref(
        "dt-24022",
        24022,
        published,
        'Chris "Golfercwm" McCoy, 19 June 2002',
    )
    row = (
        "| 19 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{MCCOY_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Chris McCoy''' (DeckTech handle '''Golfercwm'''){ref} posted a [[Light]] [[Quiet Mining Colony / Independent Operation|Quiet Mining Colony]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{MCCOY_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(24022, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def zajic_ls_page() -> str:
    start = wiki_card("There Is Good In Him / I Can Save Him", "LIGHT")
    published = "die die die"
    desc = "to drain opponet and tkae out vader."
    return f"""'''{ZAJIC_LS_TITLE}''' is the [[Light]] constructed list [[James Zajic]] posted on DeckTech.{post_ref("dt-23976", 23976, published, 'James "dabora" Zajic, 16 June 2002')} The published list has 58 cards.

== Deck info ==
* '''Player:''' [[James Zajic]]
* '''Published:''' 16 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(ZAJIC_LS, "LIGHT")}

{formatted_original_post(23976, description=desc)}

== See also ==

* [[James Zajic]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23976, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def james_zajic_stub() -> str:
    published = "die die die"
    ref = post_ref(
        "dt-23976",
        23976,
        published,
        'James "dabora" Zajic, 16 June 2002',
    )
    row = (
        "| 16 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{ZAJIC_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''James Zajic''' (DeckTech handle '''dabora'''){ref} posted a [[Light]] [[There Is Good In Him / I Can Save Him|There Is Good In Him]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{ZAJIC_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23976, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def kangas_ls_page() -> str:
    start = wiki_card("Quiet Mining Colony / Independent Operation", "LIGHT")
    published = "QMC Clouds"
    desc = "Get as much as 17 Force damage per turn from drains alone, and massive retrieval"
    return f"""'''{KANGAS_LS_TITLE}''' is the [[Light]] constructed list [[David Kangas]] posted on DeckTech.{post_ref("dt-23975", 23975, published, 'David "Icebreath" Kangas, 16 June 2002')}

== Deck info ==
* '''Player:''' [[David Kangas]]
* '''Published:''' 16 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(KANGAS_LS, "LIGHT")}

{formatted_original_post(23975, description=desc)}

== See also ==

* [[David Kangas]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23975, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def david_kangas_stub() -> str:
    published = "QMC Clouds"
    ref = post_ref(
        "dt-23975",
        23975,
        published,
        'David "Icebreath" Kangas, 16 June 2002',
    )
    row = (
        "| 16 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{KANGAS_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''David Kangas''' (DeckTech and Game Players Network handle '''Icebreath'''){ref} posted a [[Light]] [[Quiet Mining Colony / Independent Operation|Quiet Mining Colony]] list on DeckTech (''{published}'') and published constructed lists on [[Game Players Network]].

== Decklists ==

* [[icebreath Wesa Gotta Beatdown Deck!]] (LS, 21 October 2002)

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{KANGAS_LS_TITLE}]]
* [[Game Players Network decks]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23975, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def icebreath_redirect() -> str:
    return "#REDIRECT [[David Kangas]]\n"


def keskic_ls_page() -> str:
    start = wiki_card("You Can Either Profit By This...", "LIGHT")
    published = "Rumble In The Bronx With Mains"
    desc = "mains,battles,force retrieval,beat downswhat do you need more?"
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in KESKIC_LS_SHIELDS
    )
    return f"""'''{KESKIC_LS_TITLE}''' is the [[Light]] constructed list [[Vjeko Keskic]] posted on DeckTech.{post_ref("dt-23859", 23859, published, 'Vjeko "mighty_maul" Keskic, 10 June 2002')}

== Deck info ==
* '''Player:''' [[Vjeko Keskic]]
* '''Published:''' 10 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(KESKIC_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23859, description=desc)}

== See also ==

* [[Vjeko Keskic]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23859, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def bhasker_ds_page() -> str:
    start = wiki_card(
        "Let Them Make The First Move / At Last We Will Have Revenge", "DARK"
    )
    published = "Maul’s Combat"
    desc = "A dark side lightsaber combat that went 3-0 in the May World Qualifiers."
    return f"""'''{BHASKER_DS_TITLE}''' is the [[Dark]] constructed list [[Arvind Bhasker]] posted on DeckTech after going 3–0 in the May World Qualifiers.{post_ref("dt-23914", 23914, published, 'Arvind "Master Chief" Bhasker, 13 June 2002')}

== Deck info ==
* '''Player:''' [[Arvind Bhasker]]
* '''Published:''' 13 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BHASKER_DS, "DARK")}

{formatted_original_post(23914, description=desc)}

== See also ==

* [[Arvind Bhasker]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23914, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def arvind_bhasker_stub() -> str:
    published = "Maul’s Combat"
    ref = post_ref(
        "dt-23914",
        23914,
        published,
        'Arvind "Master Chief" Bhasker, 13 June 2002',
    )
    row = (
        "| 13 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{BHASKER_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Arvind Bhasker''' (DeckTech handle '''Master Chief'''){ref} posted a [[Dark]] [[Let Them Make The First Move / At Last We Will Have Revenge|Let Them Make The First Move]] list on DeckTech that went 3–0 in the May World Qualifiers (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{BHASKER_DS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23914, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def mann_ds_page() -> str:
    start = wiki_card("Tatooine: Jabba's Palace", "DARK")
    published = "None shall pass choke damn I guess you can"
    desc = "A palace deck, Gailid and the gang."
    return f"""'''{MANN_DS_TITLE}''' is the [[Dark]] constructed list [[Zach Mann]] posted on DeckTech.{post_ref("dt-23958", 23958, published, 'Zach "Greedosalive" Mann, 16 June 2002')}

== Deck info ==
* '''Player:''' [[Zach Mann]]
* '''Published:''' 16 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(MANN_DS, "DARK")}

{formatted_original_post(23958, description=desc)}

== See also ==

* [[Zach Mann]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23958, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def patch_zach_mann() -> None:
    path = PAGES / "Zach_Mann.wiki"
    text = path.read_text(encoding="utf-8")
    published = "None shall pass choke damn I guess you can"
    ref = post_ref(
        "dt-23958",
        23958,
        published,
        'Zach "Greedosalive" Mann, 16 June 2002',
    )
    fact = (
        " He posted a [[Dark]] [[Tatooine: Jabba's Palace]] list on DeckTech "
        f"(''{published}'').{ref}"
    )
    if "dt-23958" not in text:
        marker = "\n\n== Miscellaneous decklists =="
        if marker in text:
            text = text.replace(marker, fact + marker, 1)
            print("PATCHED Zach Mann 23958 lead")
        else:
            print("WARN Zach Mann Miscellaneous marker missing")
    row = (
        "| 16 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{MANN_DS_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{MANN_DS_TITLE}]]")
    text = add_source_line(text, post_source_bullets(23958, published) + "\n")
    text = add_category(text, "2002")
    see = text.find("== See also ==")
    src = text.find("\n== Sources ==", see)
    if see >= 0 and src > see:
        kept: list[str] = []
        for line in text[see:src].splitlines(True):
            if line.strip() == "" and kept and kept[-1].lstrip().startswith("*"):
                continue
            kept.append(line)
        text = text[:see] + "".join(kept) + text[src:]
    path.write_text(text, encoding="utf-8", newline="\n")
    print("PATCHED Zach Mann 23958")


def wehner_ls_page() -> str:
    start = wiki_card(
        "Hidden Base / Systems Will Slip Through Your Fingers", "LIGHT"
    )
    published = "Good PunJab Hunting"
    desc = (
        "The title comes from our Regional.  It was held in a mall with an "
        "indian/american restaurant and Sher-e-Punjab was the name.  I don’t "
        "care who you are, the word punjab is funny as hell.  So, anyway, we "
        "made a fun game of just"
    )
    return f"""'''{WEHNER_LS_TITLE}''' is the [[Light]] constructed list [[Matt Wehner]] posted on DeckTech.{post_ref("dt-23962", 23962, published, 'matt "Tasa" wehner, 16 June 2002')}

== Deck info ==
* '''Player:''' [[Matt Wehner]]
* '''Published:''' 16 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(WEHNER_LS, "LIGHT")}

{formatted_original_post(23962, description=desc)}

== See also ==

* [[Matt Wehner]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23962, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def wehner_ds_page() -> str:
    start = wiki_card(
        "Court Of The Vile Gangster / I Shall Enjoy Watching You Die", "DARK"
    )
    published = "Court Of the Vile Gangsta - Limp Bizkit Style"
    desc = "Now you know you’ll be lovin this sh$t right here....."
    return f"""'''{WEHNER_DS_TITLE}''' is the [[Dark]] constructed list [[Matt Wehner]] posted on DeckTech.{post_ref("dt-23843", 23843, published, 'matt "Tasa" wehner, 9 June 2002')}

== Deck info ==
* '''Player:''' [[Matt Wehner]]
* '''Published:''' 9 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(WEHNER_DS, "DARK")}

{formatted_original_post(23843, description=desc)}

== See also ==

* [[Matt Wehner]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23843, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def wehner_page() -> str:
    ls_published = "Good PunJab Hunting"
    ds_published = "Court Of the Vile Gangsta - Limp Bizkit Style"
    ref_ls = post_ref(
        "dt-23962",
        23962,
        ls_published,
        'matt "Tasa" wehner, 16 June 2002',
    )
    ref_ds = post_ref(
        "dt-23843",
        23843,
        ds_published,
        'matt "Tasa" wehner, 9 June 2002',
    )
    row_ls = (
        "| 16 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{WEHNER_LS_TITLE}|{ls_published}]] || [[Light]]"
    )
    row_ds = (
        "| 9 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{WEHNER_DS_TITLE}|{ds_published}]] || [[Dark]]"
    )
    return f"""'''Matt Wehner''' (DeckTech handle '''Tasa'''){ref_ls} played the [[2013 Texas Mini Worlds]].<ref name="pc-rem">[https://starwarsccg.org/phocadownload/2013/2013TMWDay1.pdf 2013 Texas Mini Worlds], starwarsccg.org</ref> He posted a [[Light]] [[Hidden Base / Systems Will Slip Through Your Fingers|Hidden Base]] list on DeckTech (''{ls_published}'') and a [[Dark]] [[Court Of The Vile Gangster / I Shall Enjoy Watching You Die|Court Of The Vile Gangster]] list (''{ds_published}'').{ref_ds}

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
| 19–21 April 2013 || [[2013 Texas Mini Worlds]] (Day 1) || [[Legacy Open]] || — || [[2013 Texas Mini Worlds Day 1 Matt Wehner DS Set Your Course For Alderaan|Set Your Course For Alderaan]] || [[2013 Texas Mini Worlds Day 1 Matt Wehner LS Mind What You Have Learned|Mind What You Have Learned]]
|}}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row_ls}
|-
{row_ds}
|}}

== See also ==

* [[2013 Texas Mini Worlds]]
* [[List of SWCCG tournaments]]
* [[Championships]]
* [[{WEHNER_DS_TITLE}]]
* [[{WEHNER_LS_TITLE}]]
* [[DeckTech decks]]

== Sources ==

* [https://starwarsccg.org/phocadownload/2013/2013TMWDay1.pdf 2013 Texas Mini Worlds], starwarsccg.org
{post_source_bullets(23843, ds_published)}
{post_source_bullets(23962, ls_published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2013]]
[[Category:2002]]
"""


def bowman_ds_page() -> str:
    start = wiki_card("Bring Him Before Me / Take Your Father's Place", "DARK")
    published = "BHBM - Bastard He Bit Me - Well that’s cuz you won"
    desc = "Classic Ghetto BMBM Deck with tons of battle damage potential."
    return f"""'''{BOWMAN_DS_TITLE}''' is the [[Dark]] constructed list [[Geoff Bowman]] posted on DeckTech. The published title is not used as the page title; it is kept in the original post below.{post_ref("dt-23847", 23847, published, 'Geoff "GG BLADE" Bowman, 9 June 2002')}

== Deck info ==
* '''Player:''' [[Geoff Bowman]]
* '''Published:''' 9 June 2002 (DeckTech)
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BOWMAN_DS, "DARK")}

{formatted_original_post(23847, description=desc)}

== See also ==

* [[Geoff Bowman]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23847, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def geoff_page() -> str:
    published = "BHBM - Bastard He Bit Me - Well that’s cuz you won"
    ref = post_ref(
        "dt-23847",
        23847,
        published,
        'Geoff "GG BLADE" Bowman, 9 June 2002',
    )
    row = (
        "| 9 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{BOWMAN_DS_TITLE}]] || [[Dark]]"
    )
    return f"""'''Geoff Bowman''' (DeckTech handle '''GG BLADE'''){ref} posted a [[Dark]] [[Bring Him Before Me / Take Your Father's Place|Bring Him Before Me]] list on DeckTech and played in 2025 Players Committee constructed events.<ref name="pc-2025">[https://www.starwarsccg.org/2025-01-las-vegas-grand-prix-las-vegas-nevada-jan-11-12-2025/ 2025 Las Vegas Grand Prix], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
| 11–12 January 2025 || [[2025 Las Vegas Grand Prix]] (Day 1) || [[Open]] || #26 || [[2025 LVGP Geoff Bowman DS AOBS|Agents Of Black Sun]] || [[2025 LVGP Geoff Bowman LS HITCO|He Is The Chosen One]]
|}}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{BOWMAN_DS_TITLE}]]
* [[2025 Las Vegas Grand Prix]]
* [[DeckTech decks]]
* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [https://www.starwarsccg.org/2025-01-las-vegas-grand-prix-las-vegas-nevada-jan-11-12-2025/ 2025 Las Vegas Grand Prix], starwarsccg.org
{post_source_bullets(23847, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2025]]
[[Category:2002]]
"""


def wodicka_ds_page() -> str:
    start = wiki_card("ISB Operations / Imperial Siege", "DARK")
    published = "6th place Coruscant regionals"
    desc = "The deck I used to finish 6th (out of 36) at Coruscant regionals. It is fairly consistent."
    return f"""'''{WODICKA_DS_TITLE}''' is the [[Dark]] constructed list [[Chris Wodicka]] posted on DeckTech.{post_ref("dt-23830", 23830, published, 'Chris "Wedge231" Wodicka, 8 June 2002')} He finished 6th (out of 36) at [[2002 Coruscant Regionals]] and went 2-1 at the [[2002 NYC Mini-Open]] with it.

== Deck info ==
* '''Player:''' [[Chris Wodicka]]
* '''Published:''' 8 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(WODICKA_DS, "DARK")}

{formatted_original_post(23830, description=desc)}

== See also ==

* [[Chris Wodicka]]
* [[2002 Coruscant Regionals]]
* [[2002 NYC Mini-Open]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23830, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def chris_wodicka_page() -> str:
    published = "6th place Coruscant regionals"
    ref = post_ref(
        "dt-23830",
        23830,
        published,
        'Chris "Wedge231" Wodicka, 8 June 2002',
    )
    return f"""'''Chris Wodicka''' (DeckTech and Game Players Network handle '''Wedge231'''){ref} finished 6th (out of 36) at [[2002 Coruscant Regionals]] and went 2-1 at the [[2002 NYC Mini-Open]] with a [[Dark]] [[ISB Operations / Imperial Siege|ISB Operations]] list (''{published}''). He published constructed lists on [[Game Players Network]].

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
| June 2002 || [[2002 NYC Mini-Open]] || [[Premiere - Original VS2]] || 2-1 || [[{WODICKA_DS_TITLE}|ISB Operations]] || —
|-
| June 2002 || [[2002 Coruscant Regionals]] || [[Premiere - Original VS2]] || 6th || [[{WODICKA_DS_TITLE}|ISB Operations]] || —
|}}

== Decklists ==

* [[Wedge231 Wodicka's SYCFA Mains]] (DS, 29 August 2002)
* [[Wedge231 ISB Done WRONG]] (DS, 19 January 2003)
* [[Wedge231 Hidden Base - needs help!]] (LS, 17 February 2003)

== See also ==

* [[{WODICKA_DS_TITLE}]]
* [[2002 Coruscant Regionals]]
* [[2002 NYC Mini-Open]]
* [[Game Players Network decks]]
* [[DeckTech decks]]
* [[Decklists]]
* [[List of SWCCG tournaments]]

== Sources ==

{post_source_bullets(23830, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def wedge231_redirect() -> str:
    return "#REDIRECT [[Chris Wodicka]]\n"


def coruscant_regionals() -> str:
    published = "6th place Coruscant regionals"
    ref = post_ref(
        "dt-23830",
        23830,
        published,
        'Chris "Wedge231" Wodicka, 8 June 2002',
    )
    return f"""'''2002 Coruscant Regionals''' was a constructed Star Wars CCG regional in 2002. [[Chris Wodicka]] finished 6th (out of 36) with a [[Dark]] [[ISB Operations / Imperial Siege|ISB Operations]] list (''{published}'').{ref}

* '''Dates:''' June 2002
* '''Format:''' [[Premiere - Original VS2]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 6th || [[Chris Wodicka]] || [[{WODICKA_DS_TITLE}|ISB Operations]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[2002 NYC Mini-Open]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Chris Wodicka]]

== Sources ==

{post_source_bullets(23830, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def nyc_mini_open() -> str:
    published = "6th place Coruscant regionals"
    ref = post_ref(
        "dt-23830",
        23830,
        published,
        'Chris "Wedge231" Wodicka, 8 June 2002',
    )
    return f"""'''2002 NYC Mini-Open''' was a constructed Star Wars CCG tournament in New York City in 2002. [[Chris Wodicka]] went 2-1 with a [[Dark]] [[ISB Operations / Imperial Siege|ISB Operations]] list (''{published}''), with a loss by 15 to [[Brian Terwilliger]]'s Senate.{ref}

* '''Dates:''' June 2002
* '''Site:''' New York City
* '''Format:''' [[Premiere - Original VS2]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 2-1 || [[Chris Wodicka]] || [[{WODICKA_DS_TITLE}|ISB Operations]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[2002 Coruscant Regionals]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]
* [[Chris Wodicka]]
* [[Brian Terwilliger]]

== Sources ==

{post_source_bullets(23830, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def patch_list_23830() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "2002 Coruscant Regionals" in text:
        print("List already has 2002 Coruscant Regionals")
        return
    origins = (
        "| 2002-07 || [[2002 Origins Open]] || 4–7 July 2002 || Columbus, Ohio || "
        "[[Premiere - Original VS2]] || —\n"
    )
    rows = (
        "| 2002-06 || [[2002 NYC Mini-Open]] || June 2002 || New York City || "
        "[[Premiere - Original VS2]] || —\n"
        "|-\n"
        "| 2002-06 || [[2002 Coruscant Regionals]] || June 2002 || — || "
        "[[Premiere - Original VS2]] || —\n"
    )
    if origins not in text:
        print("WARN List Origins row not found")
        return
    path.write_text(
        text.replace(origins, origins + "|-\n" + rows, 1),
        encoding="utf-8",
        newline="\n",
    )
    print("patched List Coruscant Regionals and NYC Mini-Open")


def patch_gpn_wodicka() -> None:
    dests = [
        PAGES / "Wedge231_Wodicka's_SYCFA_Mains.wiki",
        PAGES / "Wedge231_ISB_Done_WRONG.wiki",
        PAGES / "Wedge231_Hidden_Base_-_needs_help!.wiki",
    ]
    for path in dests:
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "* '''Player:''' [[Wedge231]]",
            "* '''Player:''' [[Chris Wodicka|Wedge231]]",
        )
        text = text.replace("* [[Wedge231]]\n", "* [[Chris Wodicka]]\n")
        path.write_text(text, encoding="utf-8", newline="\n")
        print("patched GPN dest", path.name)
    hub = PAGES / "Game_Players_Network_decks.wiki"
    text = hub.read_text(encoding="utf-8")
    n = text.count("| [[Wedge231]]\n")
    text = text.replace("| [[Wedge231]]\n", "| [[Chris Wodicka|Wedge231]]\n")
    hub.write_text(text, encoding="utf-8", newline="\n")
    print("patched GPN hub Wedge231 author n=", n)


def mccombie_ls_page() -> str:
    start = wiki_card("Yavin 4: Massassi Throne Room", "LIGHT")
    published = "Throne Room Mains So Hot Right Now"
    desc = "Throne Room Mains with a little Gungan side dish for flavor"
    return f"""'''{MCCOMBIE_LS_TITLE}''' is the [[Light]] constructed list [[Adam McCombie]] posted on DeckTech.{post_ref("dt-23820", 23820, published, 'Adam "kida117" McCombie, 8 June 2002')}

== Deck info ==
* '''Player:''' [[Adam McCombie]]
* '''Published:''' 8 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(MCCOMBIE_LS, "LIGHT")}

{formatted_original_post(23820, description=desc)}

== See also ==

* [[Adam McCombie]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23820, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def adam_mccombie_stub() -> str:
    published = "Throne Room Mains So Hot Right Now"
    ref = post_ref(
        "dt-23820",
        23820,
        published,
        'Adam "kida117" McCombie, 8 June 2002',
    )
    row = (
        "| 8 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{MCCOMBIE_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Adam McCombie''' (DeckTech handle '''kida117'''){ref} posted a [[Light]] [[Yavin 4: Massassi Throne Room]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{MCCOMBIE_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23820, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def beckham_ls_page() -> str:
    start = wiki_card("We'll Handle This / Duel Of The Fates", "LIGHT")
    published = "Too Hot in da Hot Tub"
    desc = (
        "My friend used to always say that and then I saw Ricky Williams "
        "say it on cribs. Funny @#$%."
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in BECKHAM_SHIELDS
    )
    return f"""'''{BECKHAM_LS_TITLE}''' is the [[Light]] constructed list [[Stephen Beckham]] posted on DeckTech.{post_ref("dt-23798", 23798, published, 'Stephen "Texan" Beckham, 6 June 2002')} The published list has 61 cards.

== Deck info ==
* '''Player:''' [[Stephen Beckham]]
* '''Published:''' 6 June 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS2]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BECKHAM_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23798, description=desc)}

== See also ==

* [[Stephen Beckham]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS2]]

== Sources ==

{post_source_bullets(23798, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def stephen_beckham_stub() -> str:
    published = "Too Hot in da Hot Tub"
    ref = post_ref(
        "dt-23798",
        23798,
        published,
        'Stephen "Texan" Beckham, 6 June 2002',
    )
    row = (
        "| 6 June 2002 || [[Premiere - Original VS2]] || "
        f"[[{BECKHAM_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Stephen Beckham''' (DeckTech handle '''Texan'''){ref} posted a [[Light]] [[We'll Handle This / Duel Of The Fates|We'll Handle This]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{BECKHAM_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23798, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def watkins_ls_page() -> str:
    start = wiki_card("Mind What You Have Learned / Save You It Can", "LIGHT")
    published = "Testing Testing 1 2 3 (4 5 6)"
    desc = (
        "Uses mains and Jedi Tests to make a lot of battle damage for the Dark "
        "Side. This deck needs work, but I’ve done okay with it."
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in WATKINS_SHIELDS
    )
    return f"""'''{WATKINS_LS_TITLE}''' is the [[Light]] constructed list [[Uriah Watkins]] posted on DeckTech.{post_ref("dt-23661", 23661, published, 'Uriah "travler" Watkins, 29 May 2002')} The published list has 59 cards.

== Deck info ==
* '''Player:''' [[Uriah Watkins]]
* '''Published:''' 29 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(WATKINS_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23661, description=desc)}

== See also ==

* [[Uriah Watkins]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23661, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def uriah_watkins_stub() -> str:
    published = "Testing Testing 1 2 3 (4 5 6)"
    ref = post_ref(
        "dt-23661",
        23661,
        published,
        'Uriah "travler" Watkins, 29 May 2002',
    )
    row = (
        "| 29 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{WATKINS_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Uriah Watkins''' (DeckTech handle '''travler'''){ref} posted a [[Light]] [[Mind What You Have Learned / Save You It Can|Mind What You Have Learned]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{WATKINS_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23661, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def keskic_court_ds_page() -> str:
    start = wiki_card(
        "Court Of The Vile Gangster / I Shall Enjoy Watching You Die", "DARK"
    )
    published = "Court Likes Direct Damage aka Gailid Superstar"
    desc = (
        "i got the 3rd place at the raltiir regionals this year with this deck, "
        "it went 5:1 into the finlal fours"
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in KESKIC_COURT_SHIELDS
    )
    return f"""'''{KESKIC_COURT_TITLE}''' is the [[Dark]] constructed list [[Vjeko Keskic]] posted on DeckTech after finishing 3rd at [[2002 Ralltiir Regionals]].{post_ref("dt-23606", 23606, published, 'Vjeko "mighty_maul" Keskic, 27 May 2002')}

== Deck info ==
* '''Player:''' [[Vjeko Keskic]]
* '''Event:''' [[2002 Ralltiir Regionals]]
* '''Finish:''' 3
* '''Published:''' 27 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(KESKIC_COURT_DS, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23606, description=desc)}

== See also ==

* [[2002 Ralltiir Regionals]]
* [[Vjeko Keskic]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23606, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def ralltiir_regionals_2002() -> str:
    published = "Court Likes Direct Damage aka Gailid Superstar"
    ref = post_ref(
        "dt-23606",
        23606,
        published,
        'Vjeko "mighty_maul" Keskic, 27 May 2002',
    )
    return f"""'''2002 Ralltiir Regionals''' was a constructed Star Wars CCG regional in Mainz on 19 May 2002 (Germany–Switzerland–Austria). [[Bastian Winkelhaus]] won. [[Vjeko Keskic]] finished 3rd (5–1 into the final four) with a [[Dark]] [[Court Of The Vile Gangster / I Shall Enjoy Watching You Die|Court Of The Vile Gangster]] list (''{published}'').{ref}

* '''Dates:''' 19 May 2002
* '''Site:''' Mainz
* '''Format:''' [[Premiere - Original VS1]]
* '''Winner:''' [[Bastian Winkelhaus]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 3 || [[Vjeko Keskic]] || [[{KESKIC_COURT_TITLE}|Court Of The Vile Gangster]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]
* [[Vjeko Keskic]]
* [[Bastian Winkelhaus]]

== Sources ==

{post_source_bullets(23606, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def patch_list_23606() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "2002 Ralltiir Regionals" in text:
        print("List already has 2002 Ralltiir Regionals")
        return
    coruscant = (
        "| 2002-06 || [[2002 Coruscant Regionals]] || June 2002 || — || "
        "[[Premiere - Original VS2]] || —\n"
    )
    row = (
        "| 2002-05 || [[2002 Ralltiir Regionals]] || 19 May 2002 || Mainz || "
        "[[Premiere - Original VS1]] || [[Bastian Winkelhaus]]\n"
    )
    if coruscant not in text:
        print("WARN List Coruscant row not found")
        return
    path.write_text(
        text.replace(coruscant, coruscant + "|-\n" + row, 1),
        encoding="utf-8",
        newline="\n",
    )
    print("patched List 2002 Ralltiir Regionals")


def hunter_ds_page() -> str:
    start = wiki_card(
        "Let Them Make The First Move / At Last We Will Have Revenge", "DARK"
    )
    published = "Saber Combat done RIGHT aka No Mans Land"
    desc = (
        "This is dark-side saber combat, the way God intended it.  (no really, I asked him)  "
        "This deck was originally posted to the GPN, and I decided to put it up here too, "
        "since so many people kept asking why I hadn’t."
    )
    return f"""'''{HUNTER_DS_TITLE}''' is the [[Dark]] constructed list [[Brian Hunter]] posted on DeckTech.{post_ref("dt-23598", 23598, published, 'Brian "HuntaWarya" Hunter, 26 May 2002')}

== Deck info ==
* '''Player:''' [[Brian Hunter]]
* '''Published:''' 26 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HUNTER_DS, "DARK")}

{formatted_original_post(23598, description=desc)}

== See also ==

* [[Brian Hunter]]
* [[HuntaWarya No Man's Land (VSC!) (DLSC)]]
* [[DeckTech decks]]
* [[Game Players Network decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23598, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def brian_hunter_page() -> str:
    published = "Saber Combat done RIGHT aka No Mans Land"
    ref = post_ref(
        "dt-23598",
        23598,
        published,
        'Brian "HuntaWarya" Hunter, 26 May 2002',
    )
    mrow = (
        "| 26 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{HUNTER_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Brian Hunter''' (GPN / DeckTech handle '''HuntaWarya'''){ref} won the [[2002 Houston DPC]].<ref name="dpc-houston-tr">[https://www.stephenskilton.com/decktech_archives/reports/2002-07-16-houston-texas-07-14-02-dpc-houstond3841/ houston-texas-07-14-02-dpc-houston], Jacob "Armaedes" Taylor, DeckTech (16 July 2002). Preservation copy: [https://stevetotheizz0.github.io/decktech_archives/reports/2002-07-16-houston-texas-07-14-02-dpc-houstond3841/ GitHub Pages].</ref> He finished 2nd at the [[2006 World Championship]] in Chicago, losing to [[Nate Meeker]].<ref name="awards">[https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org; Wayback [https://web.archive.org/web/20230817222457/https://www.starwarsccg.org/community/awards/ 17 August 2023]</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
| '''5-7 October 2007''' || [[2007 World Championship]] (Team) || [[Premiere - Original VS13]] || — || — || [[2007 Worlds Team Brian Hunter LS Mind What You Have Learned|Mind What You Have Learned]]
|-
| '''5-7 October 2007''' || [[2007 World Championship]] (Day 3) || [[Premiere - Original VS13]] || — || [[2007 Worlds Day 3 Brian Hunter DS Ralltiir Operations|Ralltiir Operations]] || [[2007 Worlds Day 3 Brian Hunter LS Echo Base Operations|Echo Base Operations]]
|-
| '''5-7 October 2007''' || [[2007 World Championship]] (Day 2) || [[Premiere - Original VS13]] || — || [[2007 Worlds Day 2 Brian Hunter DS Set Your Course For Alderaan|Set Your Course For Alderaan]] || [[2007 Worlds Day 2 Brian Hunter LS We'll Handle This|We'll Handle This]]
|-
| 2006 || [[2006 World Championship]] || [[Virtual Sets (2002-2009)]] || 2 || — || —
|-
| 14 July 2002 || [[2002 Houston DPC]] || [[Premiere - Original VS2]] || 1 || — || —
|}}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{mrow}
|}}

== See also ==

* [[{HUNTER_DS_TITLE}]]
* [[HuntaWarya No Man's Land (VSC!) (DLSC)]]
* [[HuntaWarya How to Hide a Rebel Base (VSC!) (HB)]]
* [[2007 World Championship]]
* [[2006 World Championship]]
* [[2002 Houston DPC]]
* [[DeckTech decks]]
* [[Game Players Network decks]]
* [[List of SWCCG tournaments]]

== Sources ==

* [https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org
* [https://web.archive.org/web/20230817222457/https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame] (Wayback 17 August 2023)
* [https://www.starwarsccg.org/2007-decklists/ 2007 Decklists], starwarsccg.org
* [https://www.stephenskilton.com/decktech_archives/reports/2002-07-16-houston-texas-07-14-02-dpc-houstond3841/ houston-texas-07-14-02-dpc-houston], Stephen Skilton
* [https://stevetotheizz0.github.io/decktech_archives/reports/2002-07-16-houston-texas-07-14-02-dpc-houstond3841/ houston-texas-07-14-02-dpc-houston] (GitHub Pages)
* [http://www.decktech.net/starwarsccg/deck/24516 Raging Bull (Hoostino's Hunt Down Hammer)], decktech.net
* [https://www.stephenskilton.com/decktech_archives/24516/ Raging Bull (Hoostino's Hunt Down Hammer)], stephenskilton.com
* [https://stevetotheizz0.github.io/decktech_archives/24516/ Raging Bull (Hoostino's Hunt Down Hammer)] (GitHub Pages)
* [https://web.archive.org/web/20261009044330/http://www.decktech.net/starwarsccg/deck/24516/ Raging Bull (Hoostino's Hunt Down Hammer)] (Wayback of decktech.net)
{post_source_bullets(23598, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2006]]
[[Category:2007]]
[[Category:2002]]
"""


def hunta_redirect() -> str:
    return "#REDIRECT [[Brian Hunter]]\n"


def furgut_ls_page() -> str:
    start = wiki_card("Echo Base Operations / Special Modifications", "LIGHT")
    published = "Unbeatable EBO aka fun for everyone"
    desc = (
        "well not really but it’s hard to get someones attention these days.So "
        "just look at the deck and you’ll know what I mean."
    )
    return f"""'''{FURGUT_LS_TITLE}''' is the [[Light]] constructed list [[Quirin Fürgut]] posted on DeckTech.{post_ref("dt-23592", 23592, published, 'Quirin "el-diablo" Fuergut, 26 May 2002')}

== Deck info ==
* '''Player:''' [[Quirin Fürgut]]
* '''Published:''' 26 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(FURGUT_LS, "LIGHT")}

{formatted_original_post(23592, description=desc)}

== See also ==

* [[Quirin Fürgut]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23592, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def quirin_furgut_page() -> str:
    published = "Unbeatable EBO aka fun for everyone"
    ref = post_ref(
        "dt-23592",
        23592,
        published,
        'Quirin "el-diablo" Fuergut, 26 May 2002',
    )
    mrow = (
        "| 26 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{FURGUT_LS_TITLE}|{published}]] || [[Light]]"
    )
    live = (ROOT / "_live_Quirin_Furgut.wiki").read_text(encoding="utf-8")
    rest = live.split("== Tournament Results ==", 1)[1]
    tourney, after = rest.split("== See also ==", 1)
    see_src = after.split("== Sources ==", 1)
    see = see_src[0]
    sources = see_src[1]
    lead = (
        f"'''Quirin Fürgut''' (DeckTech handle '''el-diablo'''){ref} played "
        "the [[2026 European Championship]].<ref name=\"pc-euro\">"
        "[https://www.starwarsccg.org/2026-10-european-championship-bochum-germany-sept-19-20-2026/ "
        "2026-10 European Championship], starwarsccg.org</ref>\n"
    )
    misc = (
        "== Miscellaneous decklists ==\n\n"
        '{| class="wikitable"\n'
        "|-\n"
        "! Date !! Format !! Title !! Side\n"
        "|-\n"
        f"{mrow}\n"
        "|}\n\n"
    )
    see_out = (
        "== See also ==\n\n"
        f"* [[{FURGUT_LS_TITLE}]]\n"
        + see.lstrip("\n")
    )
    if "* [[DeckTech decks]]" not in see_out:
        see_out = see_out.replace(
            "* [[List of SWCCG tournaments]]",
            "* [[DeckTech decks]]\n* [[List of SWCCG tournaments]]",
        )
    marker = "{{#if:1|"
    if marker in sources:
        src_bullets, tail = sources.split(marker, 1)
        src_out = (
            "== Sources ==\n"
            + src_bullets.rstrip()
            + "\n"
            + post_source_bullets(23592, published)
            + "\n\n"
            + marker
            + tail
        )
    else:
        src_out = "== Sources ==\n" + sources.rstrip() + "\n" + post_source_bullets(23592, published) + "\n"
    if "[[Category:2002]]" not in src_out:
        src_out = src_out.replace("[[Category:Players]]", "[[Category:Players]]\n[[Category:2002]]")
    return (
        lead
        + "\n== Tournament Results ==\n"
        + tourney
        + misc
        + see_out
        + src_out
    )


def manning_ds_page() -> str:
    start = wiki_card("Cloud City: Dining Room", "DARK")
    published = "Cloud City trooper deck"
    desc = (
        "people go to cloud city and kill other people while forcedraining "
        "and troopering against others"
    )
    return f"""'''{MANNING_DS_TITLE}''' is the [[Dark]] constructed list [[Jon Manning]] posted on DeckTech.{post_ref("dt-23571", 23571, published, 'jon "joker_phreak" manning, 25 May 2002')}

== Deck info ==
* '''Player:''' [[Jon Manning]]
* '''Published:''' 25 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Any Methods Necessary", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(MANNING_DS, "DARK")}

{formatted_original_post(23571, description=desc)}

== See also ==

* [[Jon Manning]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23571, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def jon_manning_stub() -> str:
    published = "Cloud City trooper deck"
    ref = post_ref(
        "dt-23571",
        23571,
        published,
        'jon "joker_phreak" manning, 25 May 2002',
    )
    row = (
        "| 25 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{MANNING_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Jon Manning''' (DeckTech handle '''joker_phreak'''){ref} posted a [[Dark]] [[Cloud City: Dining Room]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{MANNING_DS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23571, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def bouchard_ls_page() -> str:
    start = wiki_card(
        "Watch Your Step / This Place Can Be A Little Rough", "LIGHT"
    )
    published = "WYS Choke BETA"
    desc = "CHOKE + BEAT + thek"
    return f"""'''{BOUCHARD_LS_TITLE}''' is the [[Light]] constructed list [[Maximilien Bouchard]] posted on DeckTech.{post_ref("dt-23567", 23567, published, 'Maximilien "Kiriel" Bouchard, 25 May 2002')}

== Deck info ==
* '''Player:''' [[Maximilien Bouchard]]
* '''Published:''' 25 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BOUCHARD_LS, "LIGHT")}

{formatted_original_post(23567, description=desc)}

== See also ==

* [[Maximilien Bouchard]]
* [[Kiriel WYS Choke BETA]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23567, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def maximilien_stub() -> str:
    published_ls = "WYS Choke BETA"
    published_ds = "Fear Will Keep Them In Line (V) ALPHA"
    ref_ls = post_ref(
        "dt-23567",
        23567,
        published_ls,
        'Maximilien "Kiriel" Bouchard, 25 May 2002',
    )
    ref_ds = post_ref(
        "dt-24965",
        24965,
        published_ds,
        'Maximilien "Kiriel" Bouchard, 10 August 2002',
    )
    row_ds = (
        "| 10 August 2002 || [[Premiere - Original VS2]] || "
        f"[[{BOUCHARD_DS_TITLE}|{published_ds}]] || [[Dark]]"
    )
    row_ls = (
        "| 25 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{BOUCHARD_LS_TITLE}|{published_ls}]] || [[Light]]"
    )
    return f"""'''Maximilien Bouchard''' (DeckTech handle '''Kiriel'''){ref_ls} posted a [[Light]] [[Watch Your Step / This Place Can Be A Little Rough|Watch Your Step]] list on DeckTech (''{published_ls}'') and a [[Dark]] [[Set Your Course For Alderaan / The Ultimate Power In The Universe|Set Your Course For Alderaan]] list (''{published_ds}''){ref_ds}.

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row_ds}
|-
{row_ls}
|}}

== See also ==

* [[{BOUCHARD_LS_TITLE}]]
* [[{BOUCHARD_DS_TITLE}]]
* [[Kiriel WYS Choke BETA]]
* [[Kiriel AOBS old ALPHA]]
* [[Kiriel Ice plains Regional 2nd place -- Watto Podrace Alpha]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23567, published_ls)}
{post_source_bullets(24965, published_ds)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def kiriel_redirect() -> str:
    return "#REDIRECT [[Maximilien Bouchard]]\n"


def keskic_watto_page() -> str:
    start = wiki_card(
        "No Money, No Parts, No Deal! / You're A Slave?", "DARK"
    )
    published = "All Your Damage Belongs To Watto"
    desc = "Watto likes Direct Damage"
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in KESKIC_WATTO_SHIELDS
    )
    return f"""'''{KESKIC_WATTO_TITLE}''' is the [[Dark]] constructed list [[Vjeko Keskic]] posted on DeckTech.{post_ref("dt-23561", 23561, published, 'Vjeko "mighty_maul" Keskic, 25 May 2002')}

== Deck info ==
* '''Player:''' [[Vjeko Keskic]]
* '''Published:''' 25 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(KESKIC_WATTO_DS, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23561, description=desc)}

== See also ==

* [[Vjeko Keskic]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23561, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def keskic_htown_page() -> str:
    start = wiki_card("We'll Handle This / Duel Of The Fates", "LIGHT")
    published = "H-TOWN Jedis vs NRW Jedis"
    desc = "Heidelberg Jedis vs. Nord Rhein Westfalen Jedis"
    return f"""'''{KESKIC_HTOWN_TITLE}''' is the [[Light]] constructed list [[Vjeko Keskic]] posted on DeckTech.{post_ref("dt-23520", 23520, published, 'Vjeko "mighty_maul" Keskic, 23 May 2002')}

== Deck info ==
* '''Player:''' [[Vjeko Keskic]]
* '''Published:''' 23 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(KESKIC_HTOWN_LS, "LIGHT")}

{formatted_original_post(23520, description=desc)}

== See also ==

* [[Vjeko Keskic]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23520, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def quione_rst_page() -> str:
    start = wiki_card("Rebel Strike Team / Garrison Destroyed", "LIGHT")
    published = "Rebel Strike Team- Stay the hell of endor"
    desc = "RST with space to maximize drains and help keep endor clear"
    return f"""'''{QUIONE_RST_TITLE}''' is the [[Light]] constructed list [[Mike (Quione)]] posted on DeckTech.{post_ref("dt-23490", 23490, published, 'Mike "Quione" Noneofyourbusiness, 22 May 2002')}

== Deck info ==
* '''Player:''' [[Mike (Quione)]]
* '''Published:''' 22 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(QUIONE_RST_LS, "LIGHT")}

{formatted_original_post(23490, description=desc)}

== See also ==

* [[Mike (Quione)]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23490, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def brown_ds_page() -> str:
    start = wiki_card("Endor Operations / Imperial Outpost", "DARK")
    published = "Imperial Blues"
    desc = (
        "Outlast your opponent in space and on the ground while draining "
        "him away with big bonuses in the air."
    )
    return f"""'''{BROWN_DS_TITLE}''' is the [[Dark]] constructed list [[Wes Brown]] posted on DeckTech.{post_ref("dt-23459", 23459, published, 'Wes "SeaRaptor" Brown, 21 May 2002')}

== Deck info ==
* '''Player:''' [[Wes Brown]]
* '''Published:''' 21 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BROWN_DS, "DARK")}

{formatted_original_post(23459, description=desc)}

== See also ==

* [[Wes Brown]]
* [[SeaRaptor Imperial Blues (EOPS)]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23459, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def wes_brown_stub() -> str:
    published = "Imperial Blues"
    ref = post_ref(
        "dt-23459",
        23459,
        published,
        'Wes "SeaRaptor" Brown, 21 May 2002',
    )
    row = (
        "| 21 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{BROWN_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Wes Brown''' (DeckTech handle '''SeaRaptor'''){ref} posted a [[Dark]] [[Endor Operations / Imperial Outpost|Endor Operations]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{BROWN_DS_TITLE}]]
* [[SeaRaptor Imperial Blues (EOPS)]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23459, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def searaptor_redirect() -> str:
    return "#REDIRECT [[Wes Brown]]\n"


def jewell_ls_page() -> str:
    start = wiki_card("We'll Handle This / Duel Of The Fates", "LIGHT")
    published = "’Saber Combat My Way V1 00(UnRevised)"
    desc = (
        "Saber Combat that has not sucked. I like it alot, and It has beaten "
        "alot of deck types including Watto, HDADTJ, TDIGWATT, and Invasion. "
        "Check it out."
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in JEWELL_SHIELDS
    )
    return f"""'''{JEWELL_LS_TITLE}''' is the [[Light]] constructed list [[Cody Jewell]] posted on DeckTech.{post_ref("dt-23458", 23458, published, 'Cody "MegaScrub" Jewell, 21 May 2002')}

== Deck info ==
* '''Player:''' [[Cody Jewell]]
* '''Published:''' 21 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(JEWELL_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23458, description=desc)}

== See also ==

* [[Cody Jewell]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23458, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def cody_jewell_stub() -> str:
    published = "’Saber Combat My Way V1 00(UnRevised)"
    ref = post_ref(
        "dt-23458",
        23458,
        published,
        'Cody "MegaScrub" Jewell, 21 May 2002',
    )
    row = (
        "| 21 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{JEWELL_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Cody Jewell''' (DeckTech handle '''MegaScrub'''){ref} posted a [[Light]] [[We'll Handle This / Duel Of The Fates|We'll Handle This]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{JEWELL_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23458, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def atkin_ds_page() -> str:
    start = wiki_card(
        "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further",
        "DARK",
    )
    published = "Atkins’ Alderaan 2nd Place TDIGWATT"
    desc = (
        "This is my version of The Deal that went 3-1 in the Alderaan regionals, "
        "losing only in the final duel to Peter Nordstroms Light Senate Beats "
        "(Hunter style....don’t you know who he is?)"
    )
    return f"""'''{ATKIN_DS_TITLE}''' is the [[Dark]] constructed list [[Clayton Atkin]] posted on DeckTech after finishing 2nd at [[2002 Alderaan Regionals]].{post_ref("dt-23438", 23438, published, 'Clayton "TheDohMan" Atkin, 20 May 2002')}

== Deck info ==
* '''Player:''' [[Clayton Atkin]]
* '''Event:''' [[2002 Alderaan Regionals]]
* '''Finish:''' 2
* '''Published:''' 20 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(ATKIN_DS, "DARK")}

{formatted_original_post(23438, description=desc)}

== See also ==

* [[2002 Alderaan Regionals]]
* [[Clayton Atkin]]
* [[Peter Nordstrom]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23438, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def alderaan_regionals_2002() -> str:
    published = "Atkins’ Alderaan 2nd Place TDIGWATT"
    ref = post_ref(
        "dt-23438",
        23438,
        published,
        'Clayton "TheDohMan" Atkin, 20 May 2002',
    )
    return f"""'''2002 Alderaan Regionals''' was a constructed Star Wars CCG regional on 18 May 2002. [[Peter Nordstrom]] won. [[Clayton Atkin]] finished 2nd (3–1, lost the final duel) with a [[Dark]] [[This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further|This Deal Is Getting Worse All The Time]] list (''{published}'').{ref}

* '''Dates:''' 18 May 2002
* '''Format:''' [[Premiere - Original VS1]]
* '''Winner:''' [[Peter Nordstrom]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 2 || [[Clayton Atkin]] || [[{ATKIN_DS_TITLE}|This Deal Is Getting Worse All The Time]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]
* [[Clayton Atkin]]
* [[Peter Nordstrom]]

== Sources ==

{post_source_bullets(23438, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def patch_list_23438() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "2002 Alderaan Regionals" in text:
        print("List already has 2002 Alderaan Regionals")
        return
    ralltiir = (
        "| 2002-05 || [[2002 Ralltiir Regionals]] || 19 May 2002 || Mainz || "
        "[[Premiere - Original VS1]] || [[Bastian Winkelhaus]]\n"
    )
    row = (
        "| 2002-05 || [[2002 Alderaan Regionals]] || 18 May 2002 || — || "
        "[[Premiere - Original VS1]] || [[Peter Nordstrom]]\n"
    )
    if ralltiir not in text:
        print("WARN List Ralltiir row not found")
        return
    path.write_text(
        text.replace(ralltiir, ralltiir + "|-\n" + row, 1),
        encoding="utf-8",
        newline="\n",
    )
    print("patched List 2002 Alderaan Regionals")


def clayton_atkin_update() -> str:
    published = "Atkins’ Alderaan 2nd Place TDIGWATT"
    ref = post_ref(
        "dt-23438",
        23438,
        published,
        'Clayton "TheDohMan" Atkin, 20 May 2002',
    )
    text = (ROOT / "_live_Clayton_Atkin.wiki").read_text(encoding="utf-8")
    old = "'''Clayton Atkin''' played the [[2022 Endor Grand Prix]]."
    new = (
        f"'''Clayton Atkin''' (DeckTech handle '''TheDohMan'''){ref} "
        "finished 2nd at [[2002 Alderaan Regionals]] with a [[Dark]] "
        "[[This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further|"
        "This Deal Is Getting Worse All The Time]] list (''Atkins’ Alderaan 2nd Place TDIGWATT''). "
        "He played the [[2022 Endor Grand Prix]]."
    )
    if old in text and "TheDohMan" not in text:
        text = text.replace(old, new, 1)
    row = (
        "| 18 May 2002 || [[2002 Alderaan Regionals]] || "
        "[[Premiere - Original VS1]] || 2 || "
        f"[[{ATKIN_DS_TITLE}|This Deal Is Getting Worse All The Time]] || —"
    )
    text = add_result_row(text, row)
    text = add_see_also(text, f"* [[{ATKIN_DS_TITLE}]]")
    text = add_see_also(text, "* [[2002 Alderaan Regionals]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_see_also(text, "* [[Peter Nordstrom]]")
    text = add_source_line(text, post_source_bullets(23438, published) + "\n")
    text = add_category(text, "2002")
    return text


def hunter_ls_page() -> str:
    start = wiki_card("Plead My Case To The Senate / Sanity And Compassion", "LIGHT")
    published = "LS Senate done RIGHT aka Ghhhks Away"
    desc = (
        "The Senate deck that stormed through the Vegas DPC, going 5-0 in the process."
    )
    return f"""'''{HUNTER_LS_TITLE}''' is the [[Light]] constructed list [[Brian Hunter]] posted on DeckTech after winning [[2002 Vegas DPC]] 5–0.{post_ref("dt-23407", 23407, published, 'Brian "HuntaWarya" Hunter, 18 May 2002')}

== Deck info ==
* '''Player:''' [[Brian Hunter]]
* '''Event:''' [[2002 Vegas DPC]]
* '''Finish:''' 1
* '''Published:''' 18 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HUNTER_LS, "LIGHT")}

{formatted_original_post(23407, description=desc)}

== See also ==

* [[2002 Vegas DPC]]
* [[Brian Hunter]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23407, published)}
* [{VEGAS_DPC_TR} vegas-baby-lush-at-the-vegas-dpc], Stephen Skilton
* [{VEGAS_DPC_TR_GH} vegas-baby-lush-at-the-vegas-dpc] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def vegas_dpc_2002() -> str:
    published = "LS Senate done RIGHT aka Ghhhks Away"
    ref = post_ref(
        "dt-23407",
        23407,
        published,
        'Brian "HuntaWarya" Hunter, 18 May 2002',
    )
    tr = (
        f'<ref name="dpc-vegas-tr">[{VEGAS_DPC_TR} vegas-baby-lush-at-the-vegas-dpc], '
        f'Matt "Old Skooler" Lush, DeckTech (15 May 2002). Preservation copy: '
        f"[{VEGAS_DPC_TR_GH} GitHub Pages].</ref>"
    )
    return f"""'''2002 Vegas DPC''' was a constructed Star Wars CCG Decipher Player Championship on 12 May 2002 in Las Vegas, Nevada. [[Brian Hunter]] won 5–0 with a [[Light]] [[Plead My Case To The Senate / Sanity And Compassion|Plead My Case To The Senate]] list (''{published}'').{ref}{tr}

* '''Dates:''' 12 May 2002
* '''Site:''' Las Vegas, Nevada
* '''Format:''' [[Premiere - Original VS1]]
* '''Winner:''' [[Brian Hunter]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Brian Hunter]] || — || [[{HUNTER_LS_TITLE}|Plead My Case To The Senate]]
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]
* [[Brian Hunter]]
* [[2002 Houston DPC]]

== Sources ==

{post_source_bullets(23407, published)}
* [{VEGAS_DPC_TR} vegas-baby-lush-at-the-vegas-dpc], Stephen Skilton
* [{VEGAS_DPC_TR_GH} vegas-baby-lush-at-the-vegas-dpc] (GitHub Pages)

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def patch_list_23407() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "2002 Vegas DPC" in text:
        print("List already has 2002 Vegas DPC")
        return
    alderaan = (
        "| 2002-05 || [[2002 Alderaan Regionals]] || 18 May 2002 || — || "
        "[[Premiere - Original VS1]] || [[Peter Nordstrom]]\n"
    )
    row = (
        "| 2002-05 || [[2002 Vegas DPC]] || 12 May 2002 || Las Vegas, Nevada || "
        "[[Premiere - Original VS1]] || [[Brian Hunter]]\n"
    )
    if alderaan not in text:
        print("WARN List Alderaan row not found")
        return
    path.write_text(
        text.replace(alderaan, alderaan + "|-\n" + row, 1),
        encoding="utf-8",
        newline="\n",
    )
    print("patched List 2002 Vegas DPC")


def brian_hunter_update() -> str:
    published = "LS Senate done RIGHT aka Ghhhks Away"
    ref = post_ref(
        "dt-23407",
        23407,
        published,
        'Brian "HuntaWarya" Hunter, 18 May 2002',
    )
    tr = (
        f'<ref name="dpc-vegas-tr">[{VEGAS_DPC_TR} vegas-baby-lush-at-the-vegas-dpc], '
        f'Matt "Old Skooler" Lush, DeckTech (15 May 2002). Preservation copy: '
        f"[{VEGAS_DPC_TR_GH} GitHub Pages].</ref>"
    )
    text = (ROOT / "_live_Brian_Hunter.wiki").read_text(encoding="utf-8")
    old = "won the [[2002 Houston DPC]]."
    new = (
        "won the [[2002 Vegas DPC]] 5–0 with a [[Light]] "
        "[[Plead My Case To The Senate / Sanity And Compassion|"
        "Plead My Case To The Senate]] list "
        f"(''{published}'').{ref}{tr} He won the [[2002 Houston DPC]]."
    )
    if old in text and "2002 Vegas DPC" not in text:
        text = text.replace(old, new, 1)
    row = (
        "| 12 May 2002 || [[2002 Vegas DPC]] || "
        "[[Premiere - Original VS1]] || 1 || — || "
        f"[[{HUNTER_LS_TITLE}|Plead My Case To The Senate]]"
    )
    text = add_result_row(text, row)
    text = add_see_also(text, f"* [[{HUNTER_LS_TITLE}]]")
    text = add_see_also(text, "* [[2002 Vegas DPC]]")
    text = add_source_line(text, post_source_bullets(23407, published) + "\n")
    text = add_source_line(
        text,
        f"* [{VEGAS_DPC_TR} vegas-baby-lush-at-the-vegas-dpc], Stephen Skilton\n",
    )
    text = add_source_line(
        text,
        f"* [{VEGAS_DPC_TR_GH} vegas-baby-lush-at-the-vegas-dpc] (GitHub Pages)\n",
    )
    return text


def jacob_bhbm_page() -> str:
    start = wiki_card("Bring Him Before Me / Take Your Father's Place", "DARK")
    published = "Jacob's BHBM aka Blame Canada"
    desc = (
        "A Bring Him Before Me sevens deck that can turn Luke and/or beatdown "
        "quickly and easily."
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in JACOB_BHBM_SHIELDS
    )
    return f"""'''{JACOB_BHBM_TITLE}''' is the [[Dark]] constructed list [[Jacob Taylor]] posted on DeckTech.{post_ref("dt-23249", 23249, published, 'Jacob "Armaedes" Taylor, 9 May 2002')}

== Deck info ==
* '''Player:''' [[Jacob Taylor]]
* '''Published:''' 9 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(JACOB_BHBM, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23249, description=desc)}

== See also ==

* [[Jacob Taylor]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23249, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def jacob_taylor_stub() -> str:
    published = "Jacob's BHBM aka Blame Canada"
    ref = post_ref(
        "dt-23249",
        23249,
        published,
        'Jacob "Armaedes" Taylor, 9 May 2002',
    )
    row = (
        "| 9 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{JACOB_BHBM_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Jacob Taylor''' (DeckTech handle '''Armaedes'''){ref} posted a [[Dark]] [[Bring Him Before Me / Take Your Father's Place|Bring Him Before Me]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{JACOB_BHBM_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23249, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def blake_ds_page() -> str:
    start = wiki_card("You May Start Your Landing", "DARK")
    published = "YEEeeah I've got the Hoth (Big) Blues Baby"
    desc = (
        "I'll put the theme song somewhere randomly in the strat section... "
        "that way you'll have to read at least some of it if you wanna read "
        "the jamming jingle of the Hoth Big Blues"
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in BLAKE_SHIELDS
    )
    return f"""'''{BLAKE_DS_TITLE}''' is the [[Dark]] constructed list [[Lewis Blake]] posted on DeckTech.{post_ref("dt-23279", 23279, published, 'Lewis "Duke Devil" Blake, 11 May 2002')}

== Deck info ==
* '''Player:''' [[Lewis Blake]]
* '''Published:''' 11 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BLAKE_DS, "DARK")}

== Defensive Shields ==

These eight cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23279, description=desc)}

== See also ==

* [[Lewis Blake]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23279, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def lewis_blake_stub() -> str:
    published = "YEEeeah I've got the Hoth (Big) Blues Baby"
    ref = post_ref(
        "dt-23279",
        23279,
        published,
        'Lewis "Duke Devil" Blake, 11 May 2002',
    )
    row = (
        "| 11 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{BLAKE_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Lewis Blake''' (DeckTech handle '''Duke Devil'''){ref} posted a [[Dark]] [[You May Start Your Landing]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{BLAKE_DS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23279, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def hayward_ls_page() -> str:
    start = wiki_card("Rebel Strike Team / Garrison Destroyed", "LIGHT")
    published = "I like blowin sht up"
    desc = (
        "NON-EP1...AKA NO EPISODE 1 CARDS...AKA NO CARDS WITH AN EPISODE 1 "
        "ICON...other than that a rebel strike team deck"
    )
    return f"""'''{HAYWARD_LS_TITLE}''' is the [[Light]] constructed list [[Taylor Hayward]] posted on DeckTech. The published title is not used as the page title; it is kept in the original post below.{post_ref("dt-23334", 23334, published, 'Taylor "JediMaster10" Hayward, 13 May 2002')}

== Deck info ==
* '''Player:''' [[Taylor Hayward]]
* '''Published:''' 13 May 2002 (DeckTech)
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HAYWARD_LS, "LIGHT")}

{formatted_original_post(23334, description=desc)}

== See also ==

* [[Taylor Hayward]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23334, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def taylor_hayward_stub() -> str:
    published = "I like blowin sht up"
    ref = post_ref(
        "dt-23334",
        23334,
        published,
        'Taylor "JediMaster10" Hayward, 13 May 2002',
    )
    row = (
        "| 13 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{HAYWARD_LS_TITLE}]] || [[Light]]"
    )
    return f"""'''Taylor Hayward''' (DeckTech handle '''JediMaster10'''){ref} posted a [[Light]] [[Rebel Strike Team / Garrison Destroyed|Rebel Strike Team]] list on DeckTech.

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{HAYWARD_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23334, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2002]]
"""


def jurcovic_watd_page() -> str:
    start = wiki_card(
        "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further",
        "DARK",
    )
    published = "There Are Those Droidekas"
    desc = (
        "Here they are Here come the men in white uniforms. I mean, in metal "
        "frames. And actually, they're not real men (woman), but hey, who cares?"
    )
    return f"""'''{JURCOVIC_WATD_TITLE}''' is the [[Dark]] constructed list [[Peter Jurcovic]] posted on DeckTech.{post_ref("dt-23346", 23346, published, 'Peter "marvin" Jurcovic, 14 May 2002')}

== Deck info ==
* '''Player:''' [[Peter Jurcovic]]
* '''Published:''' 14 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(JURCOVIC_WATD, "DARK")}

{formatted_original_post(23346, description=desc)}

== See also ==

* [[Peter Jurcovic]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23346, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def peter_jurcovic_update() -> str:
    published = "There Are Those Droidekas"
    ref = post_ref(
        "dt-23346",
        23346,
        published,
        'Peter "marvin" Jurcovic, 14 May 2002',
    )
    text = (ROOT / "_live_Peter_Jurcovic.wiki").read_text(encoding="utf-8")
    old = (
        "posted a [[Dark]] [[My Lord, Is That Legal? / I Will Make It Legal|"
        "My Lord, Is That Legal?]] list on DeckTech "
        "(''Hold Me Thrill Me Kiss Me Kill Me'')."
    )
    new = (
        old
        + " He posted a [[Dark]] "
        "[[This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further|"
        "This Deal Is Getting Worse All The Time]] list on DeckTech "
        f"(''{published}'').{ref}"
    )
    if old in text and JURCOVIC_WATD_TITLE not in text:
        text = text.replace(old, new, 1)
    row = (
        "| 14 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{JURCOVIC_WATD_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{JURCOVIC_WATD_TITLE}]]")
    text = add_source_line(text, post_source_bullets(23346, published) + "\n")
    text = add_category(text, "2002")
    return text


def ht_ls_page() -> str:
    start = wiki_card(
        "You Can Either Profit By This... / Or Be Destroyed", "LIGHT"
    )
    published = "Secret Siths Profit"
    desc = "A Profit deck from a beginner."
    return f"""'''{HT_LS_TITLE}''' is the [[Light]] constructed list [[Matthew Harrison-Trainor]] posted on DeckTech.{post_ref("dt-23385", 23385, published, 'Matthew "Secret Sith" H-T, 16 May 2002')}

== Deck info ==
* '''Player:''' [[Matthew Harrison-Trainor]]
* '''Published:''' 16 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HT_LS, "LIGHT")}

{formatted_original_post(23385, description=desc)}

== See also ==

* [[Matthew Harrison-Trainor]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23385, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def matthew_ht_update() -> str:
    published = "Secret Siths Profit"
    ref = post_ref(
        "dt-23385",
        23385,
        published,
        'Matthew "Secret Sith" H-T, 16 May 2002',
    )
    text = (ROOT / "_live_Matthew_Harrison-Trainor.wiki").read_text(encoding="utf-8")
    old = (
        "'''Matthew Harrison-Trainor''' (GEMP handles '''MHT''' and "
        "'''MatthewHT''') is a member of [[Team 5]]"
    )
    new = (
        "'''Matthew Harrison-Trainor''' (GEMP handles '''MHT''' and "
        "'''MatthewHT'''; DeckTech handle '''Secret Sith''')"
        f"{ref} is a member of [[Team 5]]"
    )
    if old in text and "Secret Sith" not in text:
        text = text.replace(old, new, 1)
    fact = (
        " He posted a [[Light]] "
        "[[You Can Either Profit By This... / Or Be Destroyed|"
        "You Can Either Profit By This...]] list on DeckTech "
        f"(''{published}'')."
    )
    marker = "\n\n== Tournament Results =="
    if "list on DeckTech" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    row = (
        "| 16 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{HT_LS_TITLE}|{published}]] || [[Light]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{HT_LS_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(23385, published) + "\n")
    text = add_category(text, "2002")
    return text


def scott_ds_page() -> str:
    start = wiki_card("Bring Him Before Me / Take Your Father's Place", "DARK")
    published = "BHBM how to kill combat"
    desc = "all around good combat deck that as little weaknesses"
    return f"""'''{SCOTT_DS_TITLE}''' is the [[Dark]] constructed list [[Drew Scott]] posted on DeckTech.{post_ref("dt-23182", 23182, published, 'drew "drew man1" scott, 6 May 2002')}

== Deck info ==
* '''Player:''' [[Drew Scott]]
* '''Published:''' 6 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(SCOTT_DS, "DARK")}

{formatted_original_post(23182, description=desc)}

== See also ==

* [[Drew Scott]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23182, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def drew_scott_update() -> str:
    published = "BHBM how to kill combat"
    ref = post_ref(
        "dt-23182",
        23182,
        published,
        'drew "drew man1" scott, 6 May 2002',
    )
    text = (ROOT / "_live_Drew_Scott.wiki").read_text(encoding="utf-8")
    old = "'''Drew Scott''' won the [[2005 World Championship]]"
    new = (
        "'''Drew Scott''' (DeckTech handle '''drew man1''')"
        f"{ref} won the [[2005 World Championship]]"
    )
    if old in text and "drew man1" not in text:
        text = text.replace(old, new, 1)
    fact = (
        " He posted a [[Dark]] "
        "[[Bring Him Before Me / Take Your Father's Place|"
        "Bring Him Before Me]] list on DeckTech "
        f"(''{published}'')."
    )
    marker = "\n\n== Tournament Results =="
    if "list on DeckTech" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    row = (
        "| 6 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{SCOTT_DS_TITLE}|{published}]] || [[Dark]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{SCOTT_DS_TITLE}]]")
    text = add_see_also(text, "* [[DeckTech decks]]")
    text = add_source_line(text, post_source_bullets(23182, published) + "\n")
    text = add_category(text, "2002")
    return text


def diamond_ls_page() -> str:
    start = wiki_card("Quiet Mining Colony / Independent Operation", "LIGHT")
    published = "The CIA Is Trying To Kill Me"
    desc = (
        "Solid QMC, that I've been using for a while.  Title comes from a "
        "song by the underground rap group, Non Phixion, you may have seen "
        "their commercial on MTV2."
    )
    return f"""'''{DIAMOND_LS_TITLE}''' is the [[Light]] constructed list [[Sam Diamond]] posted on DeckTech.{post_ref("dt-23152", 23152, published, 'Sam "AgentSD" Diamond, 5 May 2002')}

== Deck info ==
* '''Player:''' [[Sam Diamond]]
* '''Published:''' 5 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(DIAMOND_LS, "LIGHT")}

{formatted_original_post(23152, description=desc)}

== See also ==

* [[Sam Diamond]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23152, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def sam_diamond_stub() -> str:
    published = "The CIA Is Trying To Kill Me"
    ref = post_ref(
        "dt-23152",
        23152,
        published,
        'Sam "AgentSD" Diamond, 5 May 2002',
    )
    row = (
        "| 5 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{DIAMOND_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Sam Diamond''' (DeckTech handle '''AgentSD'''){ref} posted a [[Light]] [[Quiet Mining Colony / Independent Operation|Quiet Mining Colony]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{DIAMOND_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23152, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def hayward_hb_page() -> str:
    start = wiki_card("Hidden Base / Systems Will Slip Through Your Fingers", "LIGHT")
    published = "A Hidden Base Deck"
    desc = "My first hidden base deck..."
    return f"""'''{HAYWARD_HB_TITLE}''' is the [[Light]] constructed list [[Taylor Hayward]] posted on DeckTech.{post_ref("dt-23033", 23033, published, 'Taylor "JediMaster10" Hayward, 28 April 2002')} The published list has 59 cards.

== Deck info ==
* '''Player:''' [[Taylor Hayward]]
* '''Published:''' 28 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HAYWARD_HB_LS, "LIGHT")}

{formatted_original_post(23033, description=desc)}

== See also ==

* [[Taylor Hayward]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23033, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def hayward_hb_update() -> str:
    published = "A Hidden Base Deck"
    ref = post_ref(
        "dt-23033",
        23033,
        published,
        'Taylor "JediMaster10" Hayward, 28 April 2002',
    )
    text = (ROOT / "_live_Taylor_Hayward.wiki").read_text(encoding="utf-8")
    fact = (
        " He posted a [[Light]] "
        "[[Hidden Base / Systems Will Slip Through Your Fingers|"
        "Hidden Base]] list on DeckTech "
        f"(''{published}''){ref}."
    )
    marker = "\n\n== Miscellaneous decklists =="
    if "Hidden Base / Systems Will Slip Through Your Fingers" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    row = (
        "| 28 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{HAYWARD_HB_TITLE}|{published}]] || [[Light]]"
    )
    text = add_misc_row(text, row)
    see_aitc = "* [[Taylor Hayward Agents In The Court]]"
    see_new = f"* [[{HAYWARD_HB_TITLE}]]"
    if see_aitc in text and see_new not in text:
        text = text.replace(see_aitc, see_new + "\n" + see_aitc, 1)
    else:
        text = add_see_also(text, see_new)
    text = add_source_line(text, post_source_bullets(23033, published) + "\n")
    text = add_category(text, "2002")
    return text


def burnett_senate_page() -> str:
    start = wiki_card("My Lord, Is That Legal? / I Will Make It Legal", "DARK")
    published = "My senate"
    desc = "my senate deck that has help me win a tournie and is 7-3 in tournie play"
    return f"""'''{BURNETT_SENATE_TITLE}''' is the [[Dark]] constructed list [[Chris Burnett]] posted on DeckTech.{post_ref("dt-23021", 23021, published, 'chris "Putz" burnett, 27 April 2002')}

== Deck info ==
* '''Player:''' [[Chris Burnett]]
* '''Published:''' 27 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(BURNETT_SENATE_LS, "DARK")}

{formatted_original_post(23021, description=desc)}

== See also ==

* [[Chris Burnett]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23021, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def chris_burnett_stub() -> str:
    published = "My senate"
    ref = post_ref(
        "dt-23021",
        23021,
        published,
        'chris "Putz" burnett, 27 April 2002',
    )
    row = (
        "| 27 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{BURNETT_SENATE_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Chris Burnett''' (DeckTech handle '''Putz'''){ref} posted a [[Dark]] [[My Lord, Is That Legal? / I Will Make It Legal|My Lord, Is That Legal?]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{BURNETT_SENATE_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23021, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def ertan_profit_page() -> str:
    start = wiki_card("You Can Either Profit By This... / Or Be Destroyed", "LIGHT")
    published = "beefed up profit"
    desc = "kill and retive and force lost what u waiting for"
    return f"""'''{ERTAN_PROFIT_TITLE}''' is the [[Light]] constructed list [[Dunya Ertan]] posted on DeckTech.{post_ref("dt-22997", 22997, published, 'Dunya "Hardpack" Ertan, 27 April 2002')} The published list has 62 cards.

== Deck info ==
* '''Player:''' [[Dunya Ertan]]
* '''Published:''' 27 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("The Signal", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(ERTAN_PROFIT_LS, "LIGHT")}

{formatted_original_post(22997, description=desc)}

== See also ==

* [[Dunya Ertan]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(22997, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def dunya_ertan_profit_update() -> str:
    published = "beefed up profit"
    ref = post_ref(
        "dt-22997",
        22997,
        published,
        'Dunya "Hardpack" Ertan, 27 April 2002',
    )
    text = (ROOT / "_live_Dunya_Ertan.wiki").read_text(encoding="utf-8")
    fact = (
        " Dunya posted a [[Light]] "
        "[[You Can Either Profit By This... / Or Be Destroyed|"
        "You Can Either Profit By This...]] list on DeckTech "
        f"(''{published}''){ref}."
    )
    marker = "\n\n== Miscellaneous decklists =="
    if "You Can Either Profit By This... / Or Be Destroyed" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    old_row = (
        "| 29 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{ERTAN_HYPER_TITLE}|we dont need a sticking hypergenerator]] || [[Light]]"
    )
    new_first = (
        "| 27 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{ERTAN_PROFIT_TITLE}|{published}]] || [[Light]]"
    )
    if old_row in text and new_first not in text:
        text = text.replace(old_row, new_first + "\n|-\n" + old_row, 1)
    else:
        text = add_misc_row(text, new_first)
    see_hyper = f"* [[{ERTAN_HYPER_TITLE}]]"
    see_new = f"* [[{ERTAN_PROFIT_TITLE}]]"
    if see_hyper in text and see_new not in text:
        text = text.replace(see_hyper, see_new + "\n" + see_hyper, 1)
    else:
        text = add_see_also(text, see_new)
    text = add_source_line(text, post_source_bullets(22997, published) + "\n")
    text = add_category(text, "2002")
    return text


def jacob_profit_page() -> str:
    start = wiki_card("You Can Either Profit By This... / Or Be Destroyed", "LIGHT")
    published = "Jacob's Profit aka Big Trouble"
    desc = "A defensive profit that can bring the beats."
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'LIGHT')}" for _, title, _ in JACOB_PROFIT_SHIELDS
    )
    return f"""'''{JACOB_PROFIT_TITLE}''' is the [[Light]] constructed list [[Jacob Taylor]] posted on DeckTech.{post_ref("dt-22978", 22978, published, 'Jacob "Armaedes" Taylor, 25 April 2002')}

== Deck info ==
* '''Player:''' [[Jacob Taylor]]
* '''Published:''' 25 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(JACOB_PROFIT_LS, "LIGHT")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(22978, description=desc)}

== See also ==

* [[Jacob Taylor]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(22978, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def jacob_taylor_profit_update() -> str:
    published = "Jacob's Profit aka Big Trouble"
    ref = post_ref(
        "dt-22978",
        22978,
        published,
        'Jacob "Armaedes" Taylor, 25 April 2002',
    )
    text = (ROOT / "_live_Jacob_Taylor.wiki").read_text(encoding="utf-8")
    fact = (
        " Jacob posted a [[Light]] "
        "[[You Can Either Profit By This... / Or Be Destroyed|"
        "You Can Either Profit By This...]] list on DeckTech "
        f"(''{published}''){ref}."
    )
    marker = "\n\n== Miscellaneous decklists =="
    if "You Can Either Profit By This... / Or Be Destroyed" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    old_row = (
        "| 9 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{JACOB_BHBM_TITLE}|Jacob's BHBM aka Blame Canada]] || [[Dark]]"
    )
    new_first = (
        "| 25 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{JACOB_PROFIT_TITLE}|{published}]] || [[Light]]"
    )
    if old_row in text and new_first not in text:
        text = text.replace(old_row, new_first + "\n|-\n" + old_row, 1)
    else:
        text = add_misc_row(text, new_first)
    see_bhbm = f"* [[{JACOB_BHBM_TITLE}]]"
    see_new = f"* [[{JACOB_PROFIT_TITLE}]]"
    if see_bhbm in text and see_new not in text:
        text = text.replace(see_bhbm, see_new + "\n" + see_bhbm, 1)
    else:
        text = add_see_also(text, see_new)
    text = add_source_line(text, post_source_bullets(22978, published) + "\n")
    text = add_category(text, "2002")
    return text


def elia_yavin_page() -> str:
    start = wiki_card("You May Start Your Landing", "DARK")
    published = "2002 Yavin 4 regional 2nd Place- I Am Jacks Anger"
    desc = (
        "Hoth with walkers, but its just really powerful. I don't think I "
        "would have finished second without it. By the way, it only lost 1 "
        "game in the final to Stephen Turner."
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in ELIA_YAVIN_SHIELDS
    )
    return f"""'''{ELIA_YAVIN_TITLE}''' is the [[Dark]] constructed list [[Kevin Elia]] posted on DeckTech after finishing 2nd at [[2002 Yavin 4 Regionals]].{post_ref("dt-22919", 22919, published, 'Kevin "KevOfCrofton" Elia, 21 April 2002')}

== Deck info ==
* '''Player:''' [[Kevin Elia]]
* '''Event:''' [[2002 Yavin 4 Regionals]]
* '''Finish:''' 2
* '''Published:''' 21 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(ELIA_YAVIN, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(22919, description=desc)}

== See also ==

* [[2002 Yavin 4 Regionals]]
* [[Kevin Elia]]
* [[Stephen Turner]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(22919, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:2002]]
"""


def yavin4_regionals_2002() -> str:
    published = "2002 Yavin 4 regional 2nd Place- I Am Jacks Anger"
    ref = post_ref(
        "dt-22919",
        22919,
        published,
        'Kevin "KevOfCrofton" Elia, 21 April 2002',
    )
    return f"""'''2002 Yavin 4 Regionals''' was a constructed Star Wars CCG regional in April 2002. [[Stephen Turner]] won. [[Kevin Elia]] finished 2nd with a [[Dark]] [[You May Start Your Landing]] list (''{published}'').{ref}

* '''Dates:''' April 2002
* '''Format:''' [[Premiere - Original VS1]]
* '''Winner:''' [[Stephen Turner]]

== Published lists ==

{{| class="wikitable"
|-
! Finish !! Player !! Dark !! Light
|-
| 2 || [[Kevin Elia]] || [[{ELIA_YAVIN_TITLE}|You May Start Your Landing]] || —
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]
* [[Kevin Elia]]
* [[Stephen Turner]]

== Sources ==

{post_source_bullets(22919, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:2002]]
[[Category:Decklists]]
"""


def patch_list_22919() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "2002 Yavin 4 Regionals" in text:
        print("List already has 2002 Yavin 4 Regionals")
        return
    vegas = (
        "| 2002-05 || [[2002 Vegas DPC]] || 12 May 2002 || Las Vegas, Nevada || "
        "[[Premiere - Original VS1]] || [[Brian Hunter]]\n"
    )
    row = (
        "| 2002-04 || [[2002 Yavin 4 Regionals]] || April 2002 || — || "
        "[[Premiere - Original VS1]] || [[Stephen Turner]]\n"
    )
    if vegas not in text:
        print("WARN List Vegas DPC row not found")
        return
    path.write_text(
        text.replace(vegas, vegas + "|-\n" + row, 1),
        encoding="utf-8",
        newline="\n",
    )
    print("patched List 2002 Yavin 4 Regionals")


def kevin_elia_update() -> str:
    published = "2002 Yavin 4 regional 2nd Place- I Am Jacks Anger"
    ref = post_ref(
        "dt-22919",
        22919,
        published,
        'Kevin "KevOfCrofton" Elia, 21 April 2002',
    )
    text = (ROOT / "_live_Kevin_Elia.wiki").read_text(encoding="utf-8")
    old = "'''Kevin Elia''' played the"
    new = (
        f"'''Kevin Elia''' (DeckTech handle '''KevOfCrofton'''){ref} "
        "finished 2nd at [[2002 Yavin 4 Regionals]] with a [[Dark]] "
        "[[You May Start Your Landing]] list "
        f"(''{published}''). He played the"
    )
    if old in text and "KevOfCrofton" not in text:
        text = text.replace(old, new, 1)
    row = (
        "| April 2002 || [[2002 Yavin 4 Regionals]] || "
        "[[Premiere - Original VS1]] || 2 || "
        f"[[{ELIA_YAVIN_TITLE}|You May Start Your Landing]] || —"
    )
    text = add_result_row(text, row)
    see_block = (
        "* [[Championships]]\n"
        f"* [[{ELIA_YAVIN_TITLE}]]\n"
        "* [[2002 Yavin 4 Regionals]]\n"
        "* [[Stephen Turner]]\n"
        "* [[DeckTech decks]]"
    )
    if "* [[Championships]]" in text and f"* [[{ELIA_YAVIN_TITLE}]]" not in text:
        text = text.replace("* [[Championships]]", see_block, 1)
    text = add_source_line(text, post_source_bullets(22919, published) + "\n")
    text = add_category(text, "2002")
    return text


def stephen_turner_stub() -> str:
    published = "2002 Yavin 4 regional 2nd Place- I Am Jacks Anger"
    ref = post_ref(
        "dt-22919",
        22919,
        published,
        'Kevin "KevOfCrofton" Elia, 21 April 2002',
    )
    return f"""'''Stephen Turner''' won [[2002 Yavin 4 Regionals]].{ref}

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
| April 2002 || [[2002 Yavin 4 Regionals]] || [[Premiere - Original VS1]] || 1 || — || —
|}}

== See also ==

* [[2002 Yavin 4 Regionals]]
* [[Kevin Elia]]
* [[List of SWCCG tournaments]]
* [[DeckTech decks]]

== Sources ==

{post_source_bullets(22919, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def jeffris_rst_page() -> str:
    start = wiki_card("Rebel Strike Team / Garrison Destroyed", "LIGHT")
    published = "Rebel Strike Team - Da Non-Bomb"
    desc = "This RST doesn't blow up the bunker.  Fancy that?"
    return f"""'''{JEFFRIS_RST_TITLE}''' is the [[Light]] constructed list [[Dennis Jeffris]] posted on DeckTech.{post_ref("dt-23036", 23036, published, 'Dennis "Denethor" Jeffris, 28 April 2002')}

== Deck info ==
* '''Player:''' [[Dennis Jeffris]]
* '''Published:''' 28 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(JEFFRIS_RST_LS, "LIGHT")}

{formatted_original_post(23036, description=desc)}

== See also ==

* [[Dennis Jeffris]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23036, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def dennis_jeffris_stub() -> str:
    published = "Rebel Strike Team - Da Non-Bomb"
    ref = post_ref(
        "dt-23036",
        23036,
        published,
        'Dennis "Denethor" Jeffris, 28 April 2002',
    )
    row = (
        "| 28 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{JEFFRIS_RST_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Dennis Jeffris''' (DeckTech handle '''Denethor'''){ref} posted a [[Light]] [[Rebel Strike Team / Garrison Destroyed|Rebel Strike Team]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{JEFFRIS_RST_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23036, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def ertan_hyper_page() -> str:
    start = wiki_card("The Hyperdrive Generator's Gone / We'll Need A New One", "LIGHT")
    published = "we dont need a sticking hypergenerator"
    desc = "stack cards"
    return f"""'''{ERTAN_HYPER_TITLE}''' is the [[Light]] constructed list [[Dunya Ertan]] posted on DeckTech.{post_ref("dt-23051", 23051, published, 'Dunya "Hardpack" Ertan, 29 April 2002')}

== Deck info ==
* '''Player:''' [[Dunya Ertan]]
* '''Published:''' 29 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Effect:''' {wiki_card("Credits Will Do Fine", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(ERTAN_HYPER_LS, "LIGHT")}

{formatted_original_post(23051, description=desc)}

== See also ==

* [[Dunya Ertan]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23051, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def dunya_ertan_update() -> str:
    published = "we dont need a sticking hypergenerator"
    ref = post_ref(
        "dt-23051",
        23051,
        published,
        'Dunya "Hardpack" Ertan, 29 April 2002',
    )
    text = (ROOT / "_live_Dunya_Ertan.wiki").read_text(encoding="utf-8")
    fact = (
        " Dunya posted a [[Light]] "
        "[[The Hyperdrive Generator's Gone / We'll Need A New One|"
        "The Hyperdrive Generator's Gone]] list on DeckTech "
        f"(''{published}''){ref}."
    )
    marker = "\n\n== Miscellaneous decklists =="
    if "The Hyperdrive Generator's Gone / We'll Need A New One" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    old_row = (
        "| 4 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{ERTAN_LS_TITLE}|power of Rebel strike team]] || [[Light]]"
    )
    new_first = (
        "| 29 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{ERTAN_HYPER_TITLE}|{published}]] || [[Light]]"
    )
    if old_row in text and new_first not in text:
        text = text.replace(old_row, new_first + "\n|-\n" + old_row, 1)
    else:
        text = add_misc_row(text, new_first)
    see_rst = f"* [[{ERTAN_LS_TITLE}]]"
    see_new = f"* [[{ERTAN_HYPER_TITLE}]]"
    if see_rst in text and see_new not in text:
        text = text.replace(see_rst, see_new + "\n" + see_rst, 1)
    else:
        text = add_see_also(text, see_new)
    text = add_source_line(text, post_source_bullets(23051, published) + "\n")
    text = add_category(text, "2002")
    return text


def herrin_ls_page() -> str:
    start = wiki_card("We'll Handle This / Duel Of The Fates", "LIGHT")
    published = "Voice of the council solid"
    desc = "Lightsaber combat that screws with the opponent."
    return f"""'''{HERRIN_LS_TITLE}''' is the [[Light]] constructed list [[Jason Herrin]] posted on DeckTech.{post_ref("dt-23087", 23087, published, 'Jason "Mr. Black" Herrin, 2 May 2002')}

== Deck info ==
* '''Player:''' [[Jason Herrin]]
* '''Published:''' 2 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HERRIN_LS, "LIGHT")}

{formatted_original_post(23087, description=desc)}

== See also ==

* [[Jason Herrin]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23087, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def jason_herrin_stub() -> str:
    published = "Voice of the council solid"
    ref = post_ref(
        "dt-23087",
        23087,
        published,
        'Jason "Mr. Black" Herrin, 2 May 2002',
    )
    row = (
        "| 2 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{HERRIN_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Jason Herrin''' (DeckTech handle '''Mr. Black'''){ref} posted a [[Light]] [[We'll Handle This / Duel Of The Fates|We'll Handle This]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{HERRIN_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23087, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def hayward_aitc_page() -> str:
    start = wiki_card("Agents In The Court / No Love For The Empire", "LIGHT")
    published = "Agents In The Court"
    desc = "My try at an Agents In The Court Deck."
    return f"""'''{HAYWARD_AITC_TITLE}''' is the [[Light]] constructed list [[Taylor Hayward]] posted on DeckTech.{post_ref("dt-23121", 23121, published, 'Taylor "JediMaster10" Hayward, 4 May 2002')}

== Deck info ==
* '''Player:''' [[Taylor Hayward]]
* '''Published:''' 4 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Starting Effect:''' {wiki_card("An Unusual Amount Of Fear", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(HAYWARD_AITC_LS, "LIGHT")}

{formatted_original_post(23121, description=desc)}

== See also ==

* [[Taylor Hayward]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23121, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def taylor_hayward_update() -> str:
    published = "Agents In The Court"
    ref = post_ref(
        "dt-23121",
        23121,
        published,
        'Taylor "JediMaster10" Hayward, 4 May 2002',
    )
    text = (ROOT / "_live_Taylor_Hayward.wiki").read_text(encoding="utf-8")
    fact = (
        " He posted a [[Light]] "
        "[[Agents In The Court / No Love For The Empire|"
        "Agents In The Court]] list on DeckTech "
        f"(''{published}''){ref}."
    )
    marker = "\n\n== Miscellaneous decklists =="
    if "Agents In The Court / No Love For The Empire" not in text and marker in text:
        text = text.replace(marker, fact + marker, 1)
    row = (
        "| 4 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{HAYWARD_AITC_TITLE}|{published}]] || [[Light]]"
    )
    text = add_misc_row(text, row)
    text = add_see_also(text, f"* [[{HAYWARD_AITC_TITLE}]]")
    text = add_source_line(text, post_source_bullets(23121, published) + "\n")
    text = add_category(text, "2002")
    return text


def ertan_ls_page() -> str:
    start = wiki_card("Rebel Strike Team / Garrison Destroyed", "LIGHT")
    published = "power of Rebel strike team"
    desc = "Beat down and out drain"
    return f"""'''{ERTAN_LS_TITLE}''' is the [[Light]] constructed list [[Dunya Ertan]] posted on DeckTech.{post_ref("dt-23127", 23127, published, 'Dunya "Hardpack" Ertan, 4 May 2002')} The published list has 59 cards.

== Deck info ==
* '''Player:''' [[Dunya Ertan]]
* '''Published:''' 4 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(ERTAN_LS, "LIGHT")}

{formatted_original_post(23127, description=desc)}

== See also ==

* [[Dunya Ertan]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23127, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def dunya_ertan_stub() -> str:
    published = "power of Rebel strike team"
    ref = post_ref(
        "dt-23127",
        23127,
        published,
        'Dunya "Hardpack" Ertan, 4 May 2002',
    )
    row = (
        "| 4 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{ERTAN_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Dunya Ertan''' (DeckTech handle '''Hardpack'''){ref} posted a [[Light]] [[Rebel Strike Team / Garrison Destroyed|Rebel Strike Team]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{ERTAN_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23127, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def papp_ds_page() -> str:
    start = wiki_card(
        "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe",
        "DARK",
    )
    published = "HDADTJ aka there are no Jedi alive"
    desc = (
        "This deck has only one loss(only by one card). It uses the Dark "
        "Jedi to take revenge on the Jedi."
    )
    shields = "\n".join(
        f"* 1x {wiki_card(title, 'DARK')}" for _, title, _ in PAPP_SHIELDS
    )
    return f"""'''{PAPP_DS_TITLE}''' is the [[Dark]] constructed list [[Thomas Papp]] posted on DeckTech.{post_ref("dt-23136", 23136, published, 'Thomas "Yoda TP" Papp, 5 May 2002')} The published list has 61 cards.

== Deck info ==
* '''Player:''' [[Thomas Papp]]
* '''Published:''' 5 May 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(PAPP_DS, "DARK")}

== Defensive Shields ==

These ten cards were posted as Defensive Shields outside the 60. They do not count toward the 60.

{shields}

{formatted_original_post(23136, description=desc)}

== See also ==

* [[Thomas Papp]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(23136, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def thomas_papp_stub() -> str:
    published = "HDADTJ aka there are no Jedi alive"
    ref = post_ref(
        "dt-23136",
        23136,
        published,
        'Thomas "Yoda TP" Papp, 5 May 2002',
    )
    row = (
        "| 5 May 2002 || [[Premiere - Original VS1]] || "
        f"[[{PAPP_DS_TITLE}|{published}]] || [[Dark]]"
    )
    return f"""'''Thomas Papp''' (DeckTech handle '''Yoda TP'''){ref} posted a [[Dark]] [[Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe|Hunt Down And Destroy The Jedi]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{PAPP_DS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(23136, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def mike_stevens_ls_page() -> str:
    start = wiki_card("Plead My Case To The Senate / Sanity And Compassion", "LIGHT")
    published = "ls senate"
    desc = "an experiment using the ls senate design refiews are very helpful"
    return f"""'''{STEVENS_LS_TITLE}''' is the [[Light]] constructed list [[Mike Stevens]] posted on DeckTech.{post_ref("dt-22886", 22886, published, 'Mike "mikezap" Stevens, 19 April 2002')} The published list has 70 cards.

== Deck info ==
* '''Player:''' [[Mike Stevens]]
* '''Published:''' 19 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(STEVENS_LS, "LIGHT")}

{formatted_original_post(22886, description=desc)}

== See also ==

* [[Mike Stevens]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(22886, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def mike_stevens_stub() -> str:
    published = "ls senate"
    ref = post_ref(
        "dt-22886",
        22886,
        published,
        'Mike "mikezap" Stevens, 19 April 2002',
    )
    row = (
        "| 19 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{STEVENS_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Mike Stevens''' (DeckTech handle '''mikezap'''){ref} posted a [[Light]] [[Plead My Case To The Senate / Sanity And Compassion|Plead My Case To The Senate]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{STEVENS_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(22886, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def casey_merry_ls_page() -> str:
    start = wiki_card("Cloud City: Guest Quarters", "LIGHT")
    published = "Celebration what"
    desc = "This is a Cloud City Celebration deck that usually gets the job done."
    return f"""'''{MERRY_LS_TITLE}''' is the [[Light]] constructed list [[Casey Merry]] posted on DeckTech.{post_ref("dt-22705", 22705, published, 'Casey "The Demon" Merry, 9 April 2002')}

== Deck info ==
* '''Player:''' [[Casey Merry]]
* '''Published:''' 9 April 2002 (DeckTech)
* '''Published title:''' ''{published}''
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Light]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Heading For The Medical Frigate", "LIGHT")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(MERRY_LS, "LIGHT")}

{formatted_original_post(22705, description=desc)}

== See also ==

* [[Casey Merry]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(22705, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def casey_merry_stub() -> str:
    published = "Celebration what"
    ref = post_ref(
        "dt-22705",
        22705,
        published,
        'Casey "The Demon" Merry, 9 April 2002',
    )
    row = (
        "| 9 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{MERRY_LS_TITLE}|{published}]] || [[Light]]"
    )
    return f"""'''Casey Merry''' (DeckTech handle '''The Demon'''){ref} posted a [[Light]] [[Cloud City Celebration]] list on DeckTech (''{published}'').

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{MERRY_LS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(22705, published)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def silva_ds_page() -> str:
    start = wiki_card("You May Start Your Landing", "DARK")
    desc = "Walkers...the unbeatable style."
    return f"""'''{SILVA_DS_TITLE}''' is the [[Dark]] constructed list [[Darryll Silva]] posted on DeckTech. The published title is not used as the page title; it appears in the original post below.{post_ref("dt-22701", 22701, "DeckTech post 22701", 'Darryll "217" Silva, 9 April 2002')}

== Deck info ==
* '''Player:''' [[Darryll Silva]]
* '''Published:''' 9 April 2002 (DeckTech)
* '''Format:''' [[Premiere - Original VS1]]
* '''Side:''' [[Dark]]
* '''Starting Card:''' {start}
* '''Starting Interrupt:''' {wiki_card("Prepared Defenses", "DARK")}
* '''Starting Effect:''' {wiki_card("Fear Is My Ally", "DARK")}
* '''Strategy:''' {desc}

== Decklist ==

{table_from_rows(SILVA_DS, "DARK")}

The post lists Defensive Shields under Fear Is My Ally without naming them; none are dested.

{formatted_original_post(22701, description=desc)}

== See also ==

* [[Darryll Silva]]
* [[DeckTech decks]]
* [[Decklists]]
* [[Premiere - Original VS1]]

== Sources ==

{post_source_bullets(22701, "DeckTech post 22701")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2002]]
"""


def darryll_silva_stub() -> str:
    ref = post_ref("dt-22701", 22701, "DeckTech post 22701", 'Darryll "217" Silva, 9 April 2002')
    row = (
        "| 9 April 2002 || [[Premiere - Original VS1]] || "
        f"[[{SILVA_DS_TITLE}]] || [[Dark]]"
    )
    return f"""'''Darryll Silva''' (DeckTech author handle '''217'''; signs the post '''Shadow32'''){ref} posted a [[Dark]] Hoth walker list on DeckTech in April 2002, crediting John Patchell's deck archetype.

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{row}
|}}

== See also ==

* [[{SILVA_DS_TITLE}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{post_source_bullets(22701, "DeckTech post 22701")}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:2002]]
"""


def main() -> None:
    print("LOOKUP SILVA DS")
    print_lookups(SILVA_DS, "DARK")
    write_page(SILVA_DS_TITLE, silva_ds_page())
    write_page("Darryll Silva", darryll_silva_stub())
    write_page("DeckTech decks", decktech_decks())
    write_page("Premiere - Original VS1", povs1_page())
    titles = [
        (SILVA_DS_TITLE, f"pages/{slug_file(SILVA_DS_TITLE)}"),
        ("Darryll Silva", "pages/Darryll_Silva.wiki"),
        ("DeckTech decks", "pages/DeckTech_decks.wiki"),
        ("Premiere - Original VS1", "pages/Premiere_-_Original_VS1.wiki"),
    ]
    tsv = ROOT / "y-dt-22701-delta.tsv"
    lines = [f"{t}\t{rel}" for t, rel in titles if (ROOT / rel).exists()]
    tsv.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("TSV", tsv, "n", len(lines))


def main_22705() -> None:
    print("LOOKUP MERRY LS")
    print_lookups(MERRY_LS, "LIGHT")
    write_page(MERRY_LS_TITLE, casey_merry_ls_page())
    write_page("Casey Merry", casey_merry_stub())
    write_page("DeckTech decks", decktech_decks())
    write_page("Premiere - Original VS1", povs1_page())
    titles = [
        (MERRY_LS_TITLE, f"pages/{slug_file(MERRY_LS_TITLE)}"),
        ("Casey Merry", "pages/Casey_Merry.wiki"),
        ("DeckTech decks", "pages/DeckTech_decks.wiki"),
        ("Premiere - Original VS1", "pages/Premiere_-_Original_VS1.wiki"),
    ]
    tsv = ROOT / "y-dt-22705-delta.tsv"
    seen: set[str] = set()
    lines = []
    for title, rel in titles:
        if title in seen:
            continue
        if (ROOT / rel).exists():
            seen.add(title)
            lines.append(f"{title}\t{rel}")
    tsv.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("TSV", tsv, "n", len(lines))


if __name__ == "__main__":
    raise SystemExit(main())
