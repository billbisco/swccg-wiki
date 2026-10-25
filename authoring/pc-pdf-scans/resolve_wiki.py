"""Resolve (GEMP title, v, side, ep1) -> wiki card page + image + type, side-aware. Caches to card_cache.json."""
import json, re, os, time, urllib.request, urllib.parse
API = "https://wiki.swccg.com/api.php"
CACHE = os.path.join(os.path.dirname(__file__), "card_cache.json")
_c = json.load(open(CACHE)) if os.path.exists(CACHE) else {"pages": {}, "prefix": {}}
def _q(**k):
    k.update(format="json", formatversion=2)
    for a in range(5):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(API, data=urllib.parse.urlencode(k).encode(),
                   headers={"User-Agent": "HolocronClaude-pdfres"}), timeout=90))
        except Exception:
            time.sleep(3)
_last = [0.0]
def save(force=False):
    if not force and time.time() - _last[0] < 30: return
    _last[0] = time.time()
    tmp = CACHE + ".tmp%d" % os.getpid(); json.dump(_c, open(tmp, "w")); os.replace(tmp, CACHE)
import atexit; atexit.register(lambda: save(True))
def fetch(titles):
    need = [t for t in titles if t not in _c["pages"]]
    for i in range(0, len(need), 50):
        r = _q(action="query", titles="|".join(need[i:i+50]), prop="revisions", rvprop="content", rvslots="main", redirects=1)
        red = {x["from"]: x["to"] for x in r["query"].get("redirects", [])}
        norm = {x["from"]: x["to"] for x in r["query"].get("normalized", [])}
        got = {}
        for p in r["query"]["pages"]:
            txt = p["revisions"][0]["slots"]["main"]["content"] if p.get("revisions") else None
            got[p["title"]] = (p["title"], txt)
        for t in need[i:i+50]:
            t2 = norm.get(t, t); t3 = red.get(t2, t2)
            title, txt = got.get(t3, (t3, None))
            info = None
            if txt is not None:
                m = lambda f: (re.search(r"\|\s*" + f + r"\s*=\s*([^\n|]*)", txt) or [None, None])[1]
                dis = bool(re.search(r"\{\{\s*(disambig|Disambiguation|dab)", txt, re.I)) or "may refer to" in txt[:600]
                info = {"title": title, "side": (m("side") or "").strip(), "type": (m("type") or "").strip(),
                        "image": (m("image") or "").strip(), "dis": dis, "card": "{{Card" in txt}
            _c["pages"][t] = info
    save()
def prefix(t):
    if t not in _c["prefix"]:
        r = _q(action="query", list="prefixsearch", pssearch=t + " (", pslimit=60)
        _c["prefix"][t] = [p["title"] for p in r["query"]["prefixsearch"]]
    return _c["prefix"][t]
def resolve(name, v, side, ep1=False):
    """side 'Light'/'Dark'. Returns info dict or None."""
    cands = []
    rx = re.compile(re.escape(name) + r"( \([^()]+\))*$")
    pre = [t for t in prefix(name) if rx.match(t)]
    base = [name] + pre
    fetch(base); save()
    ok = []
    for t in base:
        i = _c["pages"].get(t)
        if not i or not i["card"] or i["dis"] or i["side"] != side: continue
        isv = "(V)" in i["title"]
        if isv != bool(v): continue
        ok.append(i)
    if ep1:
        e = [i for i in ok if "(Coruscant)" in i["title"] or "(Episode I)" in i["title"] or "(Theed Palace)" in i["title"]]
        if e: ok = e
    else:
        e = [i for i in ok if "(Coruscant)" not in i["title"]] if any("(Coruscant)" not in i["title"] for i in ok) else ok
        ok = e
    # dedupe by final title
    seen = {}
    for i in ok: seen.setdefault(i["title"], i)
    ok = list(seen.values())
    if len(ok) == 1: return ok[0]
    if not ok: return None
    # prefer shortest title (default printing), then Premiere
    ok.sort(key=lambda i: (len(i["title"]), i["title"]))
    return ok[0]

def resolve_shield(name, v, side):
    rx = re.compile(re.escape(name) + r"( \([^()]+\))*$")
    base = [name] + [t for t in prefix(name) if rx.match(t)]
    fetch(base)
    ok = {}
    for t in base:
        i = _c["pages"].get(t)
        if i and i["card"] and not i["dis"] and i["side"] == side and i["type"] == "Defensive Shield":
            ok.setdefault(i["title"], i)
    ok = list(ok.values())
    if not ok: return None
    ok.sort(key=lambda i: (("(V)" in i["title"]) != bool(v), "Premium" in i["title"], len(i["title"]), i["title"]))
    return ok[0]

_resolve1 = resolve
def resolve(name, v, side, ep1=False):
    r = _resolve1(name, v, side, ep1)
    if r or not name: return r
    front = name.split(" / ")[0].strip()
    if front != name:
        r = _resolve1(front, v, side, ep1)
        if r: return r
    key = front + " /"
    if key not in _c["prefix"]:
        q = _q(action="query", list="prefixsearch", pssearch=key, pslimit=30)
        _c["prefix"][key] = [p["title"] for p in q["query"]["prefixsearch"]]
    cands = [t for t in _c["prefix"][key] if t.split(" / ")[0] == front]
    fetch(cands)
    ok = [i for t in cands for i in [_c["pages"].get(t)] if i and i["card"] and i["side"] == side and ("(V)" in i["title"]) == bool(v)]
    if not ok:
        ok = [i for t in cands for i in [_c["pages"].get(t)] if i and i["card"] and i["side"] == side]
    if not ok: return None
    ok.sort(key=lambda i: ("(AI)" in i["title"], "•" in i["title"], len(i["title"])))
    return ok[0]
