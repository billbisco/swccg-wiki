"""Card name (as transcribed) -> (section, wiki target) for 2008-2009 era decklists."""
import json, re, urllib.request, urllib.parse, functools
L = json.load(open('/tmp/claude-0/ltm/build/labels.json'))
API = "https://wiki.swccg.com/api.php"
def q(**p):
    p.update(format='json', formatversion='2')
    r = urllib.request.Request(API, data=urllib.parse.urlencode(p).encode(), headers={"User-Agent": "x"})
    return json.load(urllib.request.urlopen(r, timeout=90))
CACHE = {}
def info(titles):
    need = [t for t in titles if t not in CACHE]
    for i in range(0, len(need), 40):
        r = q(action='query', titles='|'.join(need[i:i+40]), prop='revisions', rvprop='content', rvslots='main')
        for p in r['query']['pages']:
            if p.get('missing') or 'revisions' not in p: CACHE[p['title']] = None; continue
            c = p['revisions'][0]['slots']['main']['content']
            if c.lstrip().upper().startswith('#REDIRECT'):
                m = re.search(r'\[\[([^\]|#]+)', c); CACHE[p['title']] = ('REDIRECT', m.group(1).strip() if m else None); continue
            if 'isambiguation' in c[:3000] and '{{Card' not in c: CACHE[p['title']] = ('DAB', None); continue
            g = lambda k: (re.search(r'^\|' + k + r'=([^\n]*)', c, re.M) or [0, ''])[1].strip()
            CACHE[p['title']] = (g('type'), g('side'))
    return {t: CACHE.get(t) for t in titles}
SECT = {"Objective": "Objective", "Location": "Location", "Character": "Character", "Starship": "Starship", "Vehicle": "Vehicle",
        "Weapon": "Weapon", "Device": "Device", "Effect": "Effect", "Interrupt": "Interrupt", "Defensive Shield": "Defensive Shield",
        "Epic Event": "Effect", "Admiral's Order": "Effect", "Creature": "Creature", "Jedi Test": "Effect", "Podracer": "Vehicle"}
def variants(name, side):
    v = [f"{name} ({side})", name]
    if " & " in name:
        a, b = name.split(" & ", 1); v += [f"{a} & •{b}", f"{a} & •{b} ({side})", f"•{a} & •{b}"]
    if name.endswith(" (V)"):
        v += [f"{name[:-4]} (V) ({side})"]
    return v
def resolve(name, side, label_ok=True):
    """returns (section, target) or None"""
    if label_ok and name in L:
        sec, tgt = L[name]
        i = info([tgt])[tgt]
        if i and i[0] not in ('REDIRECT', 'DAB') and (not i[1] or i[1] == side):
            return SECT.get(i[0], sec), tgt
    vs = variants(name, side); I = info(vs)
    for t in vs:
        i = I[t]
        if not i: continue
        if i[0] == 'REDIRECT' and i[1]:
            j = info([i[1]])[i[1]]
            if j and j[0] not in ('REDIRECT', 'DAB') and (not j[1] or j[1] == side): return SECT.get(j[0], j[0]), i[1]
            continue
        if i[0] == 'DAB': continue
        if i[1] and i[1] != side: continue
        return SECT.get(i[0], i[0]), t
    return None
