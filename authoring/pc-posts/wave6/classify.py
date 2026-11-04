#!/usr/bin/env python3
"""Wave 6 step 3: final verdict per PC deck post from compare.py output.

python3 classify.py decklists.json cmp*.json -> verdicts.json + summary
COVERED  : a decklist page of the same event (all event words of its title appear in the post slug/title) and the
           same player (surname matches) has >= 85% of the cards, or >= 70% at the same stage.
MISSING  : otherwise (built in step 4). Posts whose list did not parse (< 30 cards) are PARSE-CHECK.
"""
import json, re, sys, collections, unicodedata, urllib.parse, difflib

AL = [(r'world championships?', 'worlds'), (r'\bworld\b', 'worlds'), (r'endor grand prix', 'egp'),
      (r'european championships?|\beuros?\b|\bec\b', 'ec'), (r'north american continental(?:s)?(?: championships?)?|\bnacs?\b', 'nac'),
      (r'texas mini worlds?|tx mini worlds?|\btmw\b', 'tmw'), (r'match play championships?', 'mpc'), (r'las vegas grand prix', 'lvgp'),
      (r'san diego super open', 'sdso'), (r'san diego grand prix', 'sdgp'), (r'\bus nationals\b|\bnationals\b', 'nationals'),
      (r'regionals?', 'regionals'), (r'final 4|final four', 'final4'), (r'final confrontation|\bfinals?\b', 'final'),
      (r'sweet 16|round of 16', 'r16'), (r'elite 8', 'top8'), (r'\btop (\d+)\b', r'top\1'), (r'\bday (\d)\b', r'day\1'),
      (r'semifinals?', 'semi'), (r'\bendor\b(?! regionals)', 'egp'), (r'\bseattle\b', 'egp'), (r'\btournament\b', ' '), (r'quarterfinals?', 'quarter'), (r'\bpc 20\b|\bpc20\b', 'pc20')]
NICK = {'matthew': 'matt', 'michael': 'mike', 'samuel': 'sam', 'jeffrey': 'jeff', 'christopher': 'chris', 'stephen': 'steve',
        'jonathan': 'jon', 'joseph': 'joe', 'bryan': 'brian', 'andrew': 'andy', 'patrick': 'pat', 'steven': 'steve',
        'daniel': 'dan', 'thomas': 'tom', 'robert': 'rob', 'nicholas': 'nick', 'william': 'bill', 'erik': 'eric'}
STAGEW = re.compile(r'day\d|top\d+|r16|final4?|semi|quarter|pods|round')


def norm(s): return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", urllib.parse.unquote(s)).encode("ascii", "ignore").decode().lower())


def canon(s):
    s = " " + norm(s) + " "
    for a, b in AL: s = re.sub(a, " " + b + " ", s)
    return s.split()


def tm(a, b):
    if a == b or NICK.get(a, a) == NICK.get(b, b): return True
    return len(a) >= 4 and len(b) >= 4 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.8


def hit(a, st):
    return any(tm(a, b) or (len(a) >= 2 and len(b) >= 4 and a in b) for b in st)


def event_player_match(core, st):
    """All event + name words of a page title appear in the post; one miss allowed only for a first/middle
    name, and then the surname must match exactly (or inside a slug word, e.g. 'de vos' in 'devos')."""
    if len(core) < 2: return False
    miss = [i for i, a in enumerate(core) if not hit(a, st)]
    if not miss: return True
    if len(miss) > 1 or miss[0] != len(core) - 2: return False
    sur = core[-1]
    return any(sur == b or (len(b) >= 4 and sur in b) or (len(sur) >= 6 and len(b) >= 6 and (b in sur)) for b in st)


def main():
    titles = json.load(open(sys.argv[1]))
    res = {}
    for f in sys.argv[2:]:
        res.update(json.load(open(f)))
    # event words = tokens that recur across many page titles of a year (names are rare)
    freq = collections.Counter()
    pre = {}
    for t in titles:
        m = re.match(r"(\d{4}) (.*?) (DS|LS)\b", t)
        if not m: continue
        toks = [x for x in canon(m.group(2)) if not x.isdigit()]
        pre[t] = (m.group(1), toks)
        for x in set(toks): freq[(m.group(1), x)] += 1
    out = {}
    for slug, v in res.items():
        if v.get("verdict") not in ("MISSING", "COVERED?"):
            out[slug] = dict(v, final=v.get("verdict")); continue
        if (v.get("total") or 0) < 30:
            out[slug] = dict(v, final="PARSE-CHECK"); continue
        st = canon(slug.replace("-", " ") + " " + v.get("post_title", ""))
        sstage = {x for x in st if STAGEW.match(x)}
        final, why = "MISSING", None
        for score, page in v.get("scores", []):
            if page not in pre: continue
            y, toks = pre[page]
            core = [x for x in toks if not STAGEW.match(x) and len(x) > 1]
            if not event_player_match(core, st): continue
            pstage = {x for x in toks if STAGEW.match(x)}
            same_stage = bool(pstage & sstage) or not pstage or not sstage
            if score >= 0.85 or (score >= 0.7 and same_stage):
                final, why = "COVERED", page; break
        out[slug] = dict(v, final=final, covered_by=why)
    json.dump(out, open("verdicts.json", "w"), indent=0)
    c = collections.Counter(v["final"] for v in out.values())
    print(c)
    ev = collections.Counter(re.sub(r'-(day-\d|top|sweet|elite|round|pods|playoff|\d+(st|nd|rd|th)).*', '', s)[:32]
                             for s, v in out.items() if v["final"] == "MISSING")
    for k, n in ev.most_common(80): print(n, k)


if __name__ == "__main__":
    main()
