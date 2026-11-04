#!/usr/bin/env python3
"""Wave 6 step 2: decide which candidate PC deck posts are really missing from the wiki.

python3 compare.py pcrest.json decklists.json out.json
For each post: render it (resolved card titles), find the player's decklist pages of that year/side
(any event), read their Decklist sections, and compare card multisets. A post is COVERED when a page of
the same event has >= 85% of the same cards; DUP-OTHER-EVENT when only another event's page matches.
"""
import json, re, sys, pathlib, collections, html as H, unicodedata, difflib, urllib.request, urllib.parse, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import render as RD   # noqa: E402

API = "https://wiki.swccg.com/api.php"
CACHE = HERE / "page_cache.json"
pc = json.load(open(CACHE)) if CACHE.exists() else {}


def wikitext(titles):
    need = [t for t in titles if t not in pc]
    for i in range(0, len(need), 40):
        q = dict(action="query", prop="revisions", rvprop="content", rvslots="main", titles="|".join(need[i:i + 40]),
                 format="json", formatversion=2)
        for a in range(5):
            try:
                r = json.load(urllib.request.urlopen(API + "?" + urllib.parse.urlencode(q), timeout=90)); break
            except Exception:
                time.sleep(5)
        norm = {n["from"]: n["to"] for n in r["query"].get("normalized", [])}
        got = {p["title"]: (p["revisions"][0]["slots"]["main"]["content"] if "revisions" in p else "") for p in r["query"]["pages"]}
        for t in need[i:i + 40]:
            pc[t] = got.get(norm.get(t, t), "")
    json.dump(pc, open(CACHE, "w"))
    return {t: pc[t] for t in titles}


def page_cards(txt):
    i = txt.find("== Decklist ==")
    if i < 0: return collections.Counter()
    sec = txt[i:]
    j = sec.find("\n== ", 5)
    sec = sec[:j] if j > 0 else sec
    c = collections.Counter()
    for line in sec.splitlines():
        m = re.match(r"\*\s*(?:(\d+)\s*x\s*)?(?:\{\{CardLink\|([^|}]+)|\[\[([^|\]]+))", line)
        if m:
            c[(m.group(2) or m.group(3)).strip()] += int(m.group(1) or 1)
    return c


def overlap(a, b):
    if not a or not b: return 0.0
    inter = sum((a & b).values())
    return inter / max(sum(a.values()), sum(b.values()))


def norm(s): return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", urllib.parse.unquote(s)).encode("ascii", "ignore").decode().lower())


NICK = {'matthew': 'matt', 'michael': 'mike', 'samuel': 'sam', 'jeffrey': 'jeff', 'christopher': 'chris', 'stephen': 'steve',
        'jonathan': 'jon', 'joseph': 'joe', 'bryan': 'brian', 'andrew': 'andy', 'patrick': 'pat', 'steven': 'steve',
        'daniel': 'dan', 'thomas': 'tom', 'robert': 'rob', 'nicholas': 'nick', 'william': 'bill'}


def tm(a, b):
    if a == b or NICK.get(a, a) == NICK.get(b, b): return True
    return len(a) >= 4 and len(b) >= 4 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.8


if __name__ == "__main__":
    rest = json.load(open(sys.argv[1])); titles = json.load(open(sys.argv[2])); out = sys.argv[3]
    by = collections.defaultdict(list)
    for t in titles:
        m = re.match(r"(\d{4}) .*? (DS|LS)\b", t)
        if m: by[(m.group(1), m.group(2))].append((t, norm(t).split()))
    tmp = HERE / "posts_html"; tmp.mkdir(exist_ok=True)
    res = {}
    done = json.load(open(out)) if pathlib.Path(out).exists() else {}
    for slug, p in rest.items():
        if slug in done: res[slug] = done[slug]; continue
        if not p:
            res[slug] = {"verdict": "NOT-ON-SITE"}; continue
        title = H.unescape(p["title"]["rendered"])
        f = tmp / f"{slug}.html"
        f.write_text(f"<title>{H.escape(title)} | x</title><div class=\"entry-content\">{p['content']['rendered']}</div><footer>",
                     encoding="utf-8")
        st = norm(slug.replace("-", " ") + " " + title).split()
        sd = "DS" if "ds" in st else ("LS" if "ls" in st else None)
        yr = (re.search(r"\b(20\d\d)\b", p.get("date", "")) or re.search(r"\b(20\d\d)\b", " ".join(st)))
        yr = next((x for x in st if re.match(r"20\d\d$", x)), yr.group(1) if yr else None)
        if not sd:
            res[slug] = {"verdict": "NO-SIDE", "post_title": title}; continue
        try:
            r = RD.render(f, sd)
            other = "LS" if sd == "DS" else "DS"
            if len(r["unresolved"]) > 0.25 * max(1, len(r["cardlist"])):
                r2 = RD.render(f, other)
                if len(r2["unresolved"]) < len(r["unresolved"]):
                    r, sd = r2, other
        except Exception as e:
            res[slug] = {"verdict": "RENDER-ERROR", "err": str(e)[:200], "post_title": title}; continue
        toks = [x for x in st if len(x) > 2 and not x.isdigit()]
        cands = [t for t, tt in by.get((yr, sd), []) if sum(any(tm(a, b) for b in tt) for a in toks) >= 2]
        res_side = sd
        pages = wikitext(cands)
        scores = sorted(((round(overlap(r["titles"], page_cards(pages[t])), 3), t) for t in cands), reverse=True)
        best = scores[0] if scores else (0, None)
        res[slug] = {"post_title": title, "date": p.get("date"), "link": p.get("link"), "side": sd, "start_loc": r.get("start_loc") and r["start_loc"]["title"], "year": yr,
                     "total": r["total"], "shields": r["shields"], "unresolved": r["unresolved"],
                     "objective": r["objective"] and r["objective"]["title"], "start_int": r["start_int"] and r["start_int"]["title"],
                     "best": best, "scores": scores[:12], "verdict": "COVERED?" if best[0] >= 0.85 else "MISSING"}
        if len(res) % 10 == 0:
            json.dump(res, open(out, "w"), indent=0); print(len(res), flush=True)
    json.dump(res, open(out, "w"), indent=0)
    print(collections.Counter(v["verdict"] for v in res.values()))
