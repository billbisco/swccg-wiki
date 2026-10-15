#!/usr/bin/env python3
"""Normalize posted card names to official titles before generation.

python3 canon.py <decks.json> <out.json>
Order: strip notes -> edition tags -> explicit map -> high-confidence fuzzy (same side). Else keep as written.
Each change is logged in deck["fixes"] as "Posted X dested Y" (stays off the article).
"""
import difflib, json, re, sys, unicodedata

DB = "/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"
EP1 = r"\((?:ep\.?\s*(?:1|i)|ep1|e1|episode\s*(?:1|i))\)"
NOTE = r"\s*\((?:[^)]*(?:card start|card hand|starting hand|\d+ starting|alternate|not a legal|indicator|start\b)[^)]*)\)"
EXPLICIT = {
    "dr. chelli aphra": "Dr. Chelli Lona Aphra", "i'm getting kind of good at this": "I'm Getting Pretty Good At This",
    "corran in rogue 9": "Corran Horn In Rogue 9", "stolen first order tie": "Stolen First Order TIE Fighter",
    "jedha city": "Jedha: Jedha City", "taunal villager": "Tuanul Villager", "fn-2199 'nines'": "FN-2199 (Nines)",
    "k2so": "K-2SO (Kay-Tuesso)", "mara jade in vt-49": "Mara Jade In VT-49 Decimator",
    "mara jade in decimator vt-49": "Mara Jade In VT-49 Decimator", "mara jade in decimater vt-49": "Mara Jade In VT-49 Decimator",
    "le-b0209 (leebo)": "LE-BO2D9 (Leebo)", "lando's not a system": "Lando's Not A System, He's A Man",
    "tatooine epi": "Tatooine (Coruscant)", "masterful move and endor occupation": "Masterful Move & Endor Occupation",
    "you can either profit by this...": "You Can Either Profit By This... / Or Be Destroyed",
    "you can either profit by this": "You Can Either Profit By This... / Or Be Destroyed",
    "i've got a bad feeling about...": "I've Got A Bad Feeling About This",
    "colonel jendon in ony": "Colonel Jendon In Onyx 1", "colonel jendon in onyx": "Colonel Jendon In Onyx 1",
    "ony": "Onyx 1",
    "marek steele, the emperor's reach": "Maarek Stele, The Emperor's Reach",
    "maraca stele, the emperor's reach": "Maarek Stele, The Emperor's Reach",
    "owen & beru lars": "Owen Lars & Beru Lars",
    "han, chewie & the falcon": "Han, Chewie, And The Falcon", "han, chewie, & the falcon": "Han, Chewie, And The Falcon",
    "visage of the empire": "Visage Of The Emperor",
    "vibro axe": "Vibro-Ax", "galid": "Gailid", "dorme'": "Dorme",
    "sfs 7.2 tie cannon": "SFS L-s7.2 TIE Cannon",
    "sfs 9.3 laser cannons": "SFS L-s9.3 Laser Cannons", "sfs ls-9.3 laser cannons": "SFS L-s9.3 Laser Cannons",
    "sfs-s9.3 laser cannons": "SFS L-s9.3 Laser Cannons",
    "artoo in red 5": "Artoo-Detoo In Red 5", "maul with lightsaber": "Darth Maul With Lightsaber",
    "ysanne siard": "Ysanne Isard", "dengar with blaster cannon": "Dengar With Blaster Carbine",
    "enter the beurocrat": "Enter The Bureaucrat", "scimitar squadron tie bomber": "Scimitar Squadron TIE",
    "balst door controls": "Blast Door Controls", "endor celebration & free ride": "Free Ride & Endor Celebration",
    "free ride & endor occupation": "Free Ride & Endor Celebration",
    "knowledge & defense": "Knowledge And Defense", "search & destroy": "Search And Destroy",
    "scum & villainy": "Scum And Villainy",
    "u-3p0": "U-3PO", "r-3p0": "R-3PO",
    "no money, no parts, no deal": "No Money, No Parts, No Deal! / You're A Slave?",
    "golenrod": "Goldenrod", "hoth: echo war room": "Hoth: Echo Command Center (War Room)",
    "qui-gon with lightsaber": "Qui-Gon Jinn With Lightsaber",
    "you can either profit by this / or be destroyed": "You Can Either Profit By This... / Or Be Destroyed",
    "hoth: north rdige": "Hoth: North Ridge", "hoth: ice plans": "Hoth: Ice Plains",
    "lieutentant tarn mison": "Lieutenant Tarn Mison",
    "our of commission & transmission terminated": "Out Of Commission & Transmission Terminated",
    "x-wing laser cannon": "X-wing Laser Cannon", "anger, fear, agression": "Anger, Fear, Aggression",
    "secret place": "Secret Plans", "we'll let fate decide": "We'll Let Fate-a Decide, Huh?",
    "we'll let-a fate decide": "We'll Let Fate-a Decide, Huh?", "simple tricks & nonsense": "Simple Tricks And Nonsense",
    "a pathetic lifeform": "Another Pathetic Lifeform",
    "darth maul's lightsaber": "Maul's Lightsaber",
    "turn it off! turn it off!!!": "Turn It Off! Turn It Off!", "turn it off!": "Turn It Off! Turn It Off!",
    "mace's lightsaber": "Mace Windu's Lightsaber", "sith proid droid": "Sith Probe Droid",
    "blast the door kid": "Blast The Door, Kid!", "obi-wan in radiant 7": "Obi-Wan In Radiant VII",
    "obi-wan in radian vii": "Obi-Wan In Radiant VII", "antiles anouever": "Antilles Maneuver",
    "wilde kaarde": "Wild Karrde", "set for stun & control": "Control & Set For Stun",
    "han with heavy blaster": "Han With Heavy Blaster Pistol", "padme": "Padme Naberrie",
    "anakin, padawan learner": "Anakin Skywalker, Padawan Learner",
    'derek "hobbie" klivian': "Derek 'Hobbie' Klivian", "5d6-ra7": "5D6-RA-7 (Fivedesix)",
    "green leader in green 1": "Green Leader In Green Squadron 1",
    "wedge antilles in red squadron 1": "Wedge In Red Squadron 1", "closer!?": "Closer?!",
    "slayn and korpil facilities": "Slayn & Korpil Facilities", "bb-8": "BB-8 (Beebee-Ate)",
    "captain rex": "Captain Rex, 501st Legion", "ct-5555": "CT-5555 (Fives)",
    "dreadnaught": "Dreadnaught-Class Heavy Cruiser",
    "mareek steele, the emperor's hand": "Maarek Stele, The Emperor's Reach",
    "wedge, red squadron leader": "Wedge Antilles, Red Squadron Leader",
    "4-lom with concussion": "4-LOM With Concussion Rifle", "han chewie & the falcon": "Han, Chewie, And The Falcon",
    "kal fal cenedros": "Kal'Falnl C'ndros", "dr. evazan and ponda baba": "Dr. Evazan & Ponda Baba",
    "dormé": "Dorme", "imperial entanglements": "Imperial Entanglements / No One To Stop Us This Time",
    "agents of the black sun / vengeance of the dark prince": "Agents Of Black Sun / Vengeance Of The Dark Prince",
    "yavin 4: throne room": "Yavin 4: Massassi Throne Room", "yavin 4: war room": "Yavin 4: Massassi War Room",
    "masterful move & endor celebration": "Masterful Move & Endor Occupation",
    "hoth: echo base command center": "Hoth: Echo Command Center (War Room)",
    "hoth: echo base war room": "Hoth: Echo Command Center (War Room)", "hoth: echo base corridor": "Hoth: Echo Corridor",
    "we'll hand this / duel of the fates": "We'll Handle This / Duel Of The Fates",
    "you can profit by this / or be destroyed": "You Can Either Profit By This... / Or Be Destroyed",
    "naboo: generator core": "Naboo: Theed Palace Generator Core", "tatooine: episode 1": "Tatooine (Coruscant)",
    "tatooine : lars moisture farm": "Tatooine: Lars' Moisture Farm", "clout city: upper plaza": "Cloud City: Upper Plaza Corridor",
    "sprial": "Spiral", "chewie, protector": "Chewbacca, Protector",
    "lieutenant pol triedam": "Lt. Pol Treidum", "lieutenant pol treidum": "Lt. Pol Treidum",
}


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("•", "").replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


titles = {"DS": {}, "LS": {}}
for r in json.load(open(DB)):
    sd = {"DARK": "DS", "LIGHT": "LS"}.get(r.get("side"))
    if sd:
        titles[sd].setdefault(norm(r["title"]), r["title"])


import os, time, urllib.parse, urllib.request
WCACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wiki-exists.json")
_wx = json.load(open(WCACHE)) if os.path.exists(WCACHE) else {}


def wiki_has(titles_):
    todo = [t for t in dict.fromkeys(titles_) if t and t not in _wx and not re.search(r"[#<>\[\]|{}]", t)]
    for i in range(0, len(todo), 45):
        ch = todo[i:i + 45]
        q = json.load(urllib.request.urlopen("https://wiki.swccg.com/api.php?" + urllib.parse.urlencode(
            {"action": "query", "titles": "|".join(ch), "redirects": 1, "format": "json"}), timeout=60))["query"]
        norm_ = {n["from"]: n["to"] for n in q.get("normalized", [])}
        red = {n["from"]: n["to"] for n in q.get("redirects", [])}
        ok = {p["title"] for p in q["pages"].values() if "missing" not in p and "invalid" not in p}
        for t in ch:
            t2 = norm_.get(t, t)
            _wx[t] = red.get(t2, t2) in ok
        time.sleep(0.25)
    json.dump(_wx, open(WCACHE, "w"))
    return {t: _wx.get(t, False) for t in titles_}


def fix(name, v, side):
    orig = name
    name = re.sub(NOTE, "", name, flags=re.I).strip()
    name = re.sub(r"^<>\s*", "", name)
    name = re.sub(r"\s*/\s*$", "", name)
    m = re.search(r"\s+v$", name, re.I)
    if m:
        v, name = True, name[: m.start()].strip()
    m = re.search(r"\s*\((v)\)\s*$", name, re.I)
    if m:
        v, name = True, name[: m.start()].strip()
    ep1 = re.search(r"\s*" + EP1 + r"\s*$", name, re.I)
    if ep1:
        base = name[: ep1.start()].strip()
        if base.lower() in ("tatooine", "coruscant", "alter", "sense"):
            name = f"{base.title()} (Coruscant)" if side == "LS" else f"{base.title()} (Dark) (Coruscant)"
            if name == "Coruscant (Coruscant)":
                name = "Coruscant"
        else:
            name = base
    pm = re.search(r"\s*\((premiere)\)\s*$", name, re.I)
    if pm and v and _wx.get(name + " (V)"):
        pm = None
    if pm:
        base = name[: pm.start()].strip()
        if base.lower() in ("tatooine", "sense") and side == "LS":
            name = f"{base.title()} (Premiere)"
        elif base.lower() in ("tatooine", "sense"):
            name = f"{base.title()} (Dark)"
        else:
            name = base
    name = re.sub(r"\s*\((?:special edition|se)\)\s*$", "", name, flags=re.I).strip()
    key = name.lower().strip()
    tc = re.sub(r"\b(in|of|the|and|to|with|on|at|for|from|by|a)\b", lambda m: m.group(1).title(), name)
    if key not in EXPLICIT and not ep1 and not pm and (_wx.get(tc) or (v and _wx.get(tc + " (V)"))):
        name = tc
    if key not in EXPLICIT and not ep1 and not pm and (_wx.get(name) or (v and _wx.get(name + " (V)"))):
        return name, v, (None if name == orig else f"Posted {orig} dested {name}{' (V)' if v else ''}.")
    if key in EXPLICIT:
        name = EXPLICIT[key]
    elif norm(name) not in titles[side] and not re.search(r"\((?:coruscant|premiere|dark)\)", name, re.I):
        cand = difflib.get_close_matches(norm(name), list(titles[side]), n=2, cutoff=0.88)
        if cand and (len(cand) == 1 or difflib.SequenceMatcher(None, norm(name), cand[0]).ratio()
                     - difflib.SequenceMatcher(None, norm(name), cand[1]).ratio() > 0.03):
            name = titles[side][cand[0]]
    return name, v, (None if name == orig else f"Posted {orig} dested {name}{' (V)' if v else ''}.")


def objective_fix(name, v):
    """Two-sided objective typed with a variant back: resolve by the wiki page whose front matches;
    unmarked = original (skip (V) pages unless the list marks V)."""
    if " / " not in name or _wx.get(name):
        return name
    front = name.split(" / ")[0].strip()
    alias = {"imperial security bureau": "ISB Operations"}
    front = alias.get(front.lower(), front)
    r = json.load(urllib.request.urlopen("https://wiki.swccg.com/api.php?" + urllib.parse.urlencode(
        {"action": "query", "list": "allpages", "apprefix": front.split(" ")[0], "aplimit": 500, "format": "json"}), timeout=60))
    cands = [x["title"] for x in r["query"]["allpages"] if " / " in x["title"]
             and norm(x["title"].split(" / ")[0].replace("(V)", "")) == norm(front.replace("(V)", ""))]
    if not v:
        cands = [c for c in cands if "(V)" not in c] or cands
    cands = [c for c in cands if not re.search(r"\((?:Virtual|Dark|AI)", c)] or cands
    return sorted(cands, key=len)[0] if cands else name


decks = json.load(open(sys.argv[1]))
pre = set()
for d in decks:
    for q, n, v in d["cards"] + d["shields"]:
        c = re.sub(NOTE, "", n, flags=re.I).strip()
        c = re.sub(r"\s+v$", "", c, flags=re.I)
        tc = re.sub(r"\b(in|of|the|and|to|with|on|at|for|from|by|a)\b", lambda m: m.group(1).title(), c)
        pre.update({c, c + " (V)", tc, tc + " (V)"})
wiki_has(sorted(pre))
changed = 0
for d in decks:
    d.setdefault("fixes", [])
    for key in ("cards", "shields"):
        new = []
        for q, n, v in d[key]:
            n2, v2, note = fix(n, v, d["side"])
            if " / " in n2:
                n3 = objective_fix(n2, v2)
                if n3 != n2:
                    note = f"Posted {n} dested {n3}."; n2 = n3
            if note:
                d["fixes"].append(note); changed += 1
            new.append([q, n2, v2])
        d[key] = new
    if d.get("start"):
        d["start"], _, _ = fix(d["start"], False, d["side"])
json.dump(decks, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
print("decks", len(decks), "names fixed", changed)
