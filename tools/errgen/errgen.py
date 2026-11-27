#!/usr/bin/env python3
"""DRAFTS-ONLY generator for SWCCG wiki Errata comparison tables (swccg-guild/work#697, Epic #638).

Reads the live wiki API (no login, < 2 req/s, 50 titles per query), never saves a page and never
pushes anywhere. Writes drafts for the parent session to apply:

  OUT/apply.tsv          Title<TAB>drafts/<outname>/<file>   (templates first, then members)
  OUT/base_revids.json   {title: live revid}  (0 for new templates)
  OUT/*.wiki             one draft per page ("/" -> "%2F")
  OUT/families.tsv       family/chain, owner template, columns (label/date), folded members, notes
  OUT/refused.tsv        chain + reason for anything not done safely
  OUT/diff_summary.txt   per page: what changed; self-check results

Scope: every version chain (pages linked by the |errata_history= "version N of M" bullets) whose
earliest member has |set= == --origin-set and whose pages are of --era, and that is not already
covered by a Card errata table on every member. Seeds come from the census page cache
(--cards-cache) plus the census families (--families), then everything is re-read live.

Usage:
  python3 errgen.py --origin-set "Virtual Set 10" --era "Virtual Modern" --out vs10
  python3 errgen.py --origin-set "Virtual Set 10" --family "Mustafar [Dark location]" --out t
  add --no-selfcheck to skip the action=parse render checks; --keep-stamp-only to make a change of the
  printed errata mark alone (same words/stats/uniqueness/title) a column. Default folds it: the Style guide
  defines Errata as changed game text, stats or uniqueness, and Virtual Set remasters relabel E -> E1.
"""
import argparse, csv, difflib, html, json, os, re, sys, time, urllib.parse, urllib.request

API = "https://swccg.com/wiki/api.php"
_last = [0.0]
NREQ = [0]


def q(**p):
    p.update(format="json", formatversion=2)
    err = None
    for i in range(5):
        dt = time.time() - _last[0]
        if dt < 0.6:
            time.sleep(0.6 - dt)
        _last[0] = time.time()
        NREQ[0] += 1
        try:
            req = urllib.request.Request(API, urllib.parse.urlencode(p).encode(),
                                         headers={"User-Agent": "errgen-drafts/1.0 (read-only)"})
            return json.load(urllib.request.urlopen(req, timeout=120))
        except Exception as e:  # noqa
            err = e
            time.sleep(3 + 3 * i)
    raise RuntimeError("API failed: %s" % err)


def fetch(titles):
    """{title: (revid, text)}; missing -> (0, None). Redirects are NOT followed (a redirect is reported)."""
    out = {}
    titles = list(dict.fromkeys(titles))
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = q(action="query", titles="|".join(chunk), prop="revisions", rvprop="ids|content", rvslots="main")
        norm = {x["from"]: x["to"] for x in d["query"].get("normalized", [])}
        got = {}
        for p in d["query"]["pages"]:
            if p.get("missing") or "revisions" not in p:
                got[p["title"]] = (0, None)
            else:
                r = p["revisions"][0]
                got[p["title"]] = (r["revid"], r["slots"]["main"]["content"])
        for t in chunk:
            out[t] = got.get(norm.get(t, t), (0, None))
            ov = os.environ.get("ERRGEN_OVERLAY")
            if ov and os.path.exists(os.path.join(ov, fname(t))):
                out[t] = (out[t][0], open(os.path.join(ov, fname(t))).read())
    return out


def exists(titles):
    res = {}
    titles = list(dict.fromkeys(titles))
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = q(action="query", titles="|".join(chunk))
        norm = {x["from"]: x["to"] for x in d["query"].get("normalized", [])}
        st = {p["title"]: not p.get("missing") for p in d["query"]["pages"]}
        for t in chunk:
            res[t] = st.get(norm.get(t, t), False)
    return res


# ---------------------------------------------------------------- Card template parsing
def card_params(text):
    """Top-level params of the first {{Card ...}}: {name: (value_start, value_end)} in text offsets."""
    s = text.find("{{Card\n")
    if s < 0:
        s = text.find("{{Card|")
    if s < 0:
        return None
    i = s + 2
    depth_t, depth_l = 1, 0
    params = {}
    cur = None  # start of current param (index after "|")
    n = len(text)
    while i < n:
        two = text[i:i + 2]
        if two == "{{":
            depth_t += 1; i += 2; continue
        if two == "}}":
            depth_t -= 1
            if depth_t == 0:
                if cur is not None:
                    _addp(params, text, cur, i)
                params["__end__"] = (i, i)
                return params
            i += 2; continue
        if text[i] == "<":
            # extension tags protect their pipes from template-argument splitting (MediaWiki preprocessor)
            mt = re.match(r"<(gallery|ref|nowiki|pre|math|poem)\b[^>]*?(/?)>", text[i:i + 300], re.I)
            if mt:
                if mt.group(2) == "/":
                    i += mt.end(); continue
                close = text.lower().find("</%s>" % mt.group(1).lower(), i + mt.end())
                if close > 0:
                    i = close + len(mt.group(1)) + 3; continue
        if two == "[[":
            depth_l += 1; i += 2; continue
        if two == "]]" and depth_l:
            depth_l -= 1; i += 2; continue
        if text[i] == "|" and depth_t == 1 and depth_l == 0:
            if cur is not None:
                _addp(params, text, cur, i)
            cur = i + 1
        i += 1
    return None


def _addp(params, text, a, b):
    seg = text[a:b]
    if "=" in seg:
        k = seg.split("=", 1)[0]
        if "\n" not in k and k.strip():
            vs = a + len(k) + 1
            params.setdefault(k.strip(), (vs, b))


def pval(text, params, k):
    if k not in params:
        return None
    a, b = params[k]
    v = text[a:b]
    return v.rstrip("\n").strip()


# ---------------------------------------------------------------- errata_history prose
DATE = r"\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4}"
BUL = re.compile(r"^\* '''([^'\n]+?)''' \((this page|\[\[([^\]|]+)(?:\|[^\]]*)?\]\])", re.M)


def bullets(eh, self_title):
    """[(label, page, bullet_text)] in prose order."""
    out = []
    ms = list(BUL.finditer(eh))
    for j, m in enumerate(ms):
        end = ms[j + 1].start() if j + 1 < len(ms) else len(eh)
        body = eh[m.start():end]
        # drop "*:" continuation lines (images) from the bullet text
        body = "\n".join(l for l in body.split("\n") if not l.startswith("*:"))
        page = self_title if m.group(2) == "this page" else m.group(3).strip()
        # playtest printings are not published text states: no column, and the pages' own
        # "version N of M" counts only published versions
        if re.search(r"\(Playtest(?: \d+)?\)$", page) or re.match(r"(?i)playtest", m.group(1).strip()):
            continue
        if out and out[-1][1] == page:
            continue  # a later publication bullet on the same article (same-words re-made image): same column
        out.append((m.group(1).strip(), page, body))
    return out


def bullet_date(b):
    for pat in (r"First published (%s)" % DATE, r"(?:this page|\]\]), (%s)\)" % DATE,
                r"(?:published|uploaded) (%s)" % DATE):
        m = re.search(pat, b)
        if m:
            return m.group(1)
    return ""


def bullet_ref(b, date, slug, idx):
    """Citation for a column: the bullet's own first <ref> (verbatim, same name), else built from its
    first Holotable link. Returns (ref_wikitext, has_preserved_copy, url)."""
    m = re.search(r"<ref name=\"([^\"]+)\">(.*?)</ref>", b, re.S)
    if m:
        # renamed: member pages define the same ref name with slightly different text, so a shared
        # table must never reuse a page's ref name (cite error "defined multiple times")
        return '<ref name="errgen-%s-%d">%s</ref>' % (slug, idx, m.group(2)), ("web.archive.org" in m.group(2)), (re.search(r"https?://\S+", m.group(2)) or [None])[0]
    m = re.search(r"\[(https://(?:github\.com|raw\.githubusercontent\.com)/swccgpc/holotable/\S+) ([^\]]*)\]", b)
    if m:
        url, lab = m.group(1), m.group(2)
        sha = re.search(r"/(?:blob|commit)/([0-9a-f]{7,40})|holotable/([0-9a-f]{7,40})/", url)
        sha = (sha.group(1) or sha.group(2)) if sha else ""
        lab = lab.strip() or ("Holotable commit " + sha[:7])
        name = "errgen-%s-%d" % (slug, idx)
        txt = "Players Committee card image, [%s %s]%s." % (url, lab, (" (%s)" % date) if date else "")
        return '<ref name="%s">%s</ref>' % (name, txt), False, url
    return "", False, None


# ---------------------------------------------------------------- normalisation & diff
_NOWIKI_EMPTY = re.compile(r"<nowiki\s*/>", re.I)
_NOWIKI_WRAP = re.compile(r"<nowiki>(.*?)</nowiki>", re.I | re.S)


def strip_wiki_quotes(s):
    """Plain text of a wikitext value without its italic/bold marks ('' ''' ''''') or <nowiki/>
    separators, e.g. "''Executor''<nowiki/>'s" -> "Executor's", "''Executor'''s" -> "Executor's".
    Card |title=, |model= and |subtype= carry italics as printed since swccg-guild/work#1379; strip
    them before comparing or exporting (swccg-guild/work#1380). Apostrophe runs are read as
    MediaWiki's doQuotes reads them; text inside <nowiki>...</nowiki> is kept as written."""
    kept = []

    def keep(m):
        kept.append(m.group(1))
        return "\x01%d\x02" % (len(kept) - 1)

    s = _NOWIKI_WRAP.sub(keep, _NOWIKI_EMPTY.sub("", s or ""))
    lines = []
    for line in s.split("\n"):
        parts = re.split(r"('{2,})", line)
        n_it = n_b = 0
        for i in range(1, len(parts), 2):
            n = len(parts[i])
            if n == 4:  # ' + bold
                parts[i - 1] += "'"
                n = 3
            elif n > 5:  # extra apostrophes + bold italic
                parts[i - 1] += "'" * (n - 5)
                n = 5
            parts[i] = "'" * n
            n_it += n in (2, 5)
            n_b += n in (3, 5)
        if n_it % 2 and n_b % 2:
            # one ''' is really an apostrophe + '' (MediaWiki: after a one-letter word, else after a
            # longer word, else after a space)
            single = multi = space = None
            for i in range(1, len(parts), 2):
                if len(parts[i]) != 3:
                    continue
                x1, x2 = parts[i - 1][-1:], parts[i - 1][-2:-1]
                if x1 == " ":
                    space = space or i
                elif x2 == " ":
                    single = i
                    break
                else:
                    multi = multi or i
            pick = single or multi or space
            if pick:
                parts[pick - 1] += "'"
                parts[pick] = "''"
        lines.append("".join(parts[0::2]))
    return re.sub("\x01(\\d+)\x02", lambda m: kept[int(m.group(1))], "\n".join(lines))


# swccg-guild/work#1382 (Bill, Option B): |game_text= and |lore= keep apostrophes and quote marks as the
# card prints them, curly (’ ‘ “ ”) or straight. Comparisons treat the two styles as one character; the
# drafts always show each page's own text. A quote-style-only difference is real but cosmetic: never a
# column and never an Errata hl, only a table note (quote_note).
QUOTE_FOLD = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})


def fold_quotes(s):
    """Comparison key only: ’ ‘ -> ', “ ” -> " (never written to a page)."""
    return (s or "").translate(QUOTE_FOLD)


def plain(s):
    s = (s or "").replace("{{!}}", "|")
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)
    s = strip_wiki_quotes(s)  # #1380: also drops <nowiki/> (was a space) and keeps the ' of ''X'''s
    s = re.sub(r"</?[A-Za-z][^<>]*>", " ", s)  # PATCH-A only real tags: card text has "< 4", prose "--->"
    s = html.unescape(s)
    s = fold_quotes(s).translate(str.maketrans({"–": "-", "—": "-"}))
    return s


def words(s):
    import html as _h
    return re.findall(r"[A-Za-z0-9▼▲\[\]<>]+", _h.unescape(plain(s)).lower())


def contained(needle, hay):
    n, h = words(needle), words(hay)
    if not n:
        return True
    L = len(n)
    return any(h[i:i + L] == n for i in range(len(h) - L + 1))


# A word may hold a single ' (opponent's, Lars') but never a run of 2+: '' and ''' are italic/bold marks, so
# "scout'''" is the word "scout" and a bold mark (otherwise the mark lands inside an Errata hl).
TOK = re.compile(r"\s+|\[\[.*?\]\]|\{\{.*?\}\}|<[^>]*>|'{2,5}|&[a-z#0-9]+;|(?:[\w\[\]▲▼’‘\-+=]|(?<!')'(?!'))+|[^\s\w]")


def toks(s):
    return TOK.findall(s)


def hl(s):
    return "{{Errata hl|1=%s}}" % s


def _ismark(t):
    return bool(re.fullmatch(r"'{2,5}", t)) or t.startswith("<")


def diff_hl(old, new):
    """Word-level diff: wrap only the changed/inserted words of `new` (vs `old`) in Errata hl. Runs of
    changed words separated only by whitespace become one highlight; bold/italic markers and tags are
    never inside a highlight. Words that differ only by curly vs straight quote marks are the same word
    (#1382); the output keeps `new`'s own marks. Returns (wikitext, n_highlights, deleted_only)."""
    a = [fold_quotes(t) for t in toks(old) if not t.isspace()]
    bt = toks(new)
    bi = [i for i, t in enumerate(bt) if not t.isspace()]
    b = [fold_quotes(bt[i]) for i in bi]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    changed, dels = set(), False
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("replace", "insert"):
            changed.update(bi[j] for j in range(j1, j2) if not _ismark(bt[bi[j]]))
        elif op == "delete":
            dels = True
    return _wrap(bt, changed), len(_runs(bt, changed)), dels


def deleted_hl(old, new):
    """Old text with only its purely deleted words highlighted (for a column whose successor removed words)."""
    at = toks(old)
    ai = [i for i, t in enumerate(at) if not t.isspace()]
    a = [fold_quotes(at[i]) for i in ai]
    b = [fold_quotes(t) for t in toks(new) if not t.isspace()]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    gone = set()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "delete":
            gone.update(ai[i] for i in range(i1, i2) if not _ismark(at[ai[i]]))
    return _wrap(at, gone), len(_runs(at, gone))


def quote_swaps(old, new):
    """Quote marks that differ only in style between two texts whose words otherwise match (#1382), as
    sorted (old_mark, new_mark) pairs, e.g. [("'", "’")]. Only aligned (unchanged) words are looked at, so
    a real wording change elsewhere does not hide or fake a swap."""
    at = [t for t in toks(old) if not t.isspace()]
    bt = [t for t in toks(new) if not t.isspace()]
    sm = difflib.SequenceMatcher(None, [fold_quotes(t) for t in at], [fold_quotes(t) for t in bt], autojunk=False)
    swaps = set()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            continue
        for x, y in zip(at[i1:i2], bt[j1:j2]):
            if x != y:
                swaps.update((c, d) for c, d in zip(x, y) if c != d)
    return sorted(swaps)


QUOTE_FIELDS = ("game_text", "lore")


def straight_quote_fields(v):
    """Fields a card page records as printing straight ' or " (Template:Card |straight_quotes=, #1382):
    "yes" = game_text and lore; otherwise a comma/space list of game_text, lore. Same rule as style_lint."""
    v = re.sub(r"<!--.*?-->", "", v or "", flags=re.S).strip().lower()
    if v in ("yes", "y", "1", "true", "all", "both"):
        return set(QUOTE_FIELDS)
    return {w for w in re.split(r"[\s,;]+", v) if w in QUOTE_FIELDS}


def quote_verified(field, old_vals, new_vals, swaps):
    """A straight mark in a quote-style swap counts as printed only if its page records it (#1382);
    otherwise it may be an old transcription and gets no table note. Curly marks are typed on purpose."""
    for c, d in swaps:
        if c in "'\"" and field not in old_vals.get("__sq", ()):
            return False
        if d in "'\"" and field not in new_vals.get("__sq", ()):
            return False
    return True


def quote_note(lab, old_label, new_label, swaps):
    """One table-note sentence for a quote-style-only difference (#1382)."""
    what = ", ".join("%s where %s prints %s" % (d, old_label, c) for c, d in swaps)
    return "%s: %s prints %s; quote style only, not a text change." % (lab, new_label, what)


def _runs(bt, changed):
    runs, cur = [], []
    for i, t in enumerate(bt):
        if i in changed:
            cur.append(i)
        elif t.isspace() and cur:
            continue
        elif cur:
            runs.append(cur); cur = []
    if cur:
        runs.append(cur)
    return runs


def _wrap(bt, changed):
    out, run, n = [], [], [0]

    def flush():
        if not run:
            return
        k = len(run)
        while k and run[k - 1].isspace():
            k -= 1
        out.append(hl("".join(run[:k])))
        out.extend(run[k:])
        n[0] += 1
        run.clear()

    for i, t in enumerate(bt):
        if i in changed:
            run.append(t)
        elif t.isspace() and run:
            run.append(t)
        else:
            flush()
            out.append(t)
    flush()
    return "".join(out)


def cell(s):
    s = (s or "").strip()
    s = re.sub(r"\n\s*\n", "<br />", s)
    s = s.replace("\n", "<br />")
    return s


# ---------------------------------------------------------------- fields
STAT_FIELDS = [("uniqueness", "Uniqueness"), ("destiny", "Destiny"), ("power", "Power"), ("ability", "Ability"),
               ("politics", "Politics"), ("armor", "Armor"), ("maneuver", "Maneuver"), ("hyperspeed", "Hyperspeed"),
               ("landspeed", "Landspeed"), ("ferocity", "Ferocity"), ("parsec", "Parsec"), ("deploy", "Deploy"),
               ("forfeit", "Forfeit"), ("subtype", "Subtype"), ("model", "Model"), ("icons", "Icons"),
               ("light_icons", "Light Side icons"), ("dark_icons", "Dark Side icons")]
NUMERIC = {"destiny", "power", "ability", "politics", "armor", "maneuver", "hyperspeed", "landspeed", "ferocity",
           "parsec", "deploy", "forfeit"}
QUAL = re.compile(r"\s+\((?:V|ALT|AI|Holo AI)\)")


def printed_title(t, p):
    v = pval(t, p, "display_title") or pval(t, p, "title") or ""
    # uniqueness dots are compared in the Uniqueness row, not as title words
    return QUAL.sub("", v).replace("•", "").replace("&bull;", "").strip()


def row_order(use_stamp):
    rows = [("__title", "Title")] + STAT_FIELDS + [("lore", "Lore"), ("game_text", "Game text")]
    if use_stamp:
        rows.append(("errata_mark", "Stamp"))
    return rows


# ---------------------------------------------------------------- main logic
def fname(title):
    return title.replace("/", "%2F") + ".wiki"


def era_of(t, p):
    e = pval(t, p, "era") or ""
    return plain(e).strip()


def label_of(page):
    m = re.search(r"\((Errata(?: \d+)?)\)$", page)
    return m.group(1) if m else "Original"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin-set", required=True)
    ap.add_argument("--era", default="Virtual Modern")
    ap.add_argument("--family", action="append", help="census family name(s) to restrict to")
    ap.add_argument("--out", required=True)
    ap.add_argument("--families", default="/home/claude/census1325/families.tsv")
    ap.add_argument("--cards-cache", default="/home/claude/census1325/cache/cards.json")
    ap.add_argument("--keep-stamp-only", action="store_true", help="treat a change of the printed errata mark alone as a new column")
    ap.add_argument("--no-selfcheck", action="store_true")
    a = ap.parse_args()
    use_stamp = a.keep_stamp_only
    out = a.out
    os.makedirs(out, exist_ok=True)
    rel = "drafts/%s" % os.path.basename(os.path.normpath(out))

    fams = list(csv.DictReader(open(a.families), delimiter="\t"))
    mem2fam = {}
    for f in fams:
        for m in f["members"].split(" | "):
            if m.strip():
                mem2fam[m.strip()] = f["family"]
    fammembers = {f["family"]: [m.strip() for m in f["members"].split(" | ") if m.strip()] for f in fams}

    # seeds: census families with this origin set + families holding a cached page of this set
    seedfams = {f["family"] for f in fams if f["origin_set"] == a.origin_set}
    loose = set()
    try:
        cache = json.load(open(a.cards_cache))
        for t, v in cache.items():
            m = re.search(r"^\|set=(.*)$", v.get("text") or "", re.M)
            if m and m.group(1).strip() == a.origin_set:
                if t in mem2fam:
                    seedfams.add(mem2fam[t])
                else:
                    loose.add(t)
    except FileNotFoundError:
        pass
    if a.family:
        seedfams &= set(a.family)
        loose = set()
    seedpages = sorted({m for fm in seedfams for m in fammembers[fm]} | loose)
    print("seed families %d, pages %d" % (len(seedfams), len(seedpages)), file=sys.stderr)
    live = fetch(seedpages)

    # chains from live errata_history prose
    P = {}
    for t, (rv, x) in live.items():
        if x is None:
            continue
        p = card_params(x)
        if p is None:
            continue
        P[t] = p
    # extra chain pages not in the seed
    extra = set()
    for t, p in P.items():
        eh = pval(live[t][1], p, "errata_history") or ""
        for _, pg, _ in bullets(eh, t):
            if pg not in live:
                extra.add(pg)
    if extra:
        live.update(fetch(sorted(extra)))
        for t in extra:
            if live[t][1] is not None:
                pp = card_params(live[t][1])
                if pp:
                    P[t] = pp

    chains = {}  # key = tuple(chain pages)
    pagechain = {}
    for t, p in P.items():
        x = live[t][1]
        if era_of(x, p) and a.era not in era_of(x, p):
            continue
        eh = pval(x, p, "errata_history") or ""
        bl = bullets(eh, t)
        if not bl:
            continue
        key = tuple(pg for _, pg, _ in bl)
        pagechain[t] = key
        chains.setdefault(key, []).append(t)

    fam_rows, refused, applies, templates, members_out, summary = [], [], [], [], [], []
    base = {}
    done_chains = set()
    allerr = set()
    cont = {}
    while True:
        d = q(action="query", list="allpages", apnamespace=10, apprefix="Card errata/", aplimit="max", **cont)
        allerr |= {x["title"] for x in d["query"]["allpages"]}
        if "continue" in d:
            cont = d["continue"]
        else:
            break

    scoped = set()

    def refuse(key, fam, why):
        refused.append((fam, " | ".join(key), why))

    for key in sorted(chains, key=lambda k: k[0]):
        if key in done_chains:
            continue
        done_chains.add(key)
        first = key[0]
        fam = mem2fam.get(first, first)
        # chain must start in the origin set
        if first not in P:
            refuse(key, fam, "first chain page %s missing or not a Card page" % first); continue
        fx = live[first][1]
        if (pval(fx, P[first], "set") or "").strip() != a.origin_set:
            continue  # out of scope (not first published in this set)
        scoped.update(key)
        # every page of the chain must exist, be of this era and carry the same chain
        bad = []
        for pg in key:
            if pg not in P:
                bad.append("%s: missing/redirect/not a Card page" % pg); continue
            e = era_of(live[pg][1], P[pg])
            if e and a.era not in e:
                bad.append("%s: era %s" % (pg, e))
            if pagechain.get(pg) != key:
                bad.append("%s: its errata_history lists a different version chain (%s)" % (pg, " | ".join(pagechain.get(pg) or ["none"])))
        if bad:
            refuse(key, fam, "conflicting/unsourced order: " + "; ".join(bad)); continue
        if len(key) == 1:
            fam_rows.append((fam, "", "", "", "page %s: single printing in this era: no table" % key[0])); continue
        # version N of M must agree with the chain length and position; when no page states it,
        # the chain order (from the dated errata_history bullets) must agree with the errata numbering
        vbad = []; nabsent = 0; offs = set()
        for i, pg in enumerate(key):
            eh = pval(live[pg][1], P[pg], "errata_history") or ""
            m = re.search(r"version (\d+) of (\d+)", eh)
            if not m:
                nabsent += 1
            # a page may count unpublished playtests too (constant leading offset): accept when the
            # distance to the newest version and the offset agree
            if m and int(m.group(2)) - len(key) >= 0 and int(m.group(1)) - (i + 1) == int(m.group(2)) - len(key):
                offs.add(int(m.group(2)) - len(key)); continue
            if not m or int(m.group(1)) != i + 1 or int(m.group(2)) != len(key):
                vbad.append("%s: 'version N of M' %s vs position %d of %d" % (pg, m.group(0) if m else "absent", i + 1, len(key)))
        if len(offs) > 1:
            vbad.append("pages count earlier unpublished versions differently (%s)" % sorted(offs))
        if vbad and all("absent" in v for v in vbad):  # every stated position agrees; only some pages lack the line
            def enum(t):
                mm = re.search(r"\(Errata(?: (\d+))?\)$", t)
                return (int(mm.group(1) or 1) if mm else 0)
            lines = {}
            for pg in key:
                b = re.sub(r"\s+\(Errata(?: \d+)?\)$", "", pg); lines.setdefault(b, []).append(enum(pg))
            if all(v == sorted(v) and len(set(v)) == len(v) for v in lines.values()):
                vbad = []
        if vbad:
            refuse(key, fam, "unsourced order: " + "; ".join(vbad)); continue
        # members outside the chain in the same census family part of this era (e.g. a fake or loose page)
        famm = [m for m in fammembers.get(fam, []) if m in P and m not in key
                and a.era in (era_of(live[m][1], P[m]) or a.era)
                and (pval(live[m][1], P[m], "set") or "") == a.origin_set and pagechain.get(m) is None]
        # existing Card errata transclusions
        existing = set()
        for pg in key:
            existing |= set(re.findall(r"\{\{\s*Card errata/([^}|]+)\}\}", live[pg][1]))
        owner = first
        tpl = "Template:Card errata/" + owner
        if existing - {owner}:
            refuse(key, fam, "members already transclude another Card errata table: %s" % ", ".join(sorted(existing))); continue
        if all(re.search(r"\{\{\s*Card errata/" + re.escape(owner) + r"\s*\}\}", live[pg][1]) for pg in key) and tpl in allerr:
            fam_rows.append((fam, tpl, "", "", "table already on every member (skipped)")); continue

        # version data + prose/page consistency
        vers, cbad, notes = [], [], []
        if famm:
            notes.append("census family also has same-set pages outside this chain: " + ", ".join(famm))
        slug = re.sub(r"[^a-z0-9]+", "", owner.lower())[:24]
        for i, pg in enumerate(key):
            x, p = live[pg][1], P[pg]
            eh = pval(x, p, "errata_history") or ""
            bl = bullets(eh, pg)
            b = bl[i][2]
            gt = pval(x, p, "game_text")
            if not gt:
                cbad.append("%s: no game_text" % pg); continue
            # prose check: the page's game text must be the text the prose quotes for this version
            seg = b
            if "Text:" in b:
                seg = b[b.find("Text:"):]
                k = seg.find("'''What changed")
                if k > 0:
                    seg = seg[:k]
            else:
                k = b.find("'''What changed")
                if k > 0:
                    k2 = b.find("Document:", k)
                    seg = b[:k] + (b[k2:] if k2 > 0 else "")
            quoted = re.findall(r"“((?:[^“”]|“[^“”]*”){15,})”", seg)
            quoted = [re.sub(r"<s>.*?</s>", "", qq) for qq in quoted]
            sides = [re.sub(r"^\s*'''[^'\n]{1,40}:'''\s*", "", s) for s in re.split(r"\n\s*\n", gt)
                     if s.strip() and not re.fullmatch(r"\s*'''[^'\n]+'''\s*", s)]
            if quoted and re.search(r"drops icons|spelling of the [^.]{0,40}icon", b):
                # PATCH-B: the prose says the card list wrote icons as words and the page restored the slip's icons
                sides = [re.sub(r"\[(Immune to [A-Za-z ]+)\]", r"\1", s_) for s_ in sides]
            # PATCH-C: prose says the quote differs from the page only in notation and nothing changed
            notation_only = bool(re.search(r"which is notation|notation only", b)) and "What changed:''' nothing" in b
            if quoted and notation_only:
                notes.append("%s: prose says its quote differs only in notation; page game_text used" % pg)
            elif quoted:
                qhay = " \u00a6 ".join(quoted)
                miss = [s for s in sides if not contained(s, qhay)]
                # a side the prose does not quote at all is a partial quote, not a conflict:
                # conflict = some quote starts like this side (first 4 words) but is not the same text
                def _conflicts(side):
                    w = words(side)[:4]
                    return any(words(qq)[:4] == w and not contained(side, qq) and not contained(qq, side) for qq in quoted) or \
                        any(len(words(qq)) >= 6 and words(qq)[:4] == w for qq in quoted) and not contained(side, qhay)
                partial = [s for s in miss if not _conflicts(s)]
                if partial:
                    notes.append("%s: prose quotes only part of the game text for %s; page game_text used" % (pg, bl[i][0]))
                miss = [s for s in miss if _conflicts(s)]
                if miss:
                    cbad.append("%s: page game_text differs from the text its errata_history quotes for %s (%r...)"
                                % (pg, bl[i][0], plain(miss[0])[:70]))
            else:
                notes.append("%s: prose quotes no text for this version; page game_text used" % pg)
            date = bullet_date(b)
            ref, preserved, url = bullet_ref(b, date, slug, i)
            vals = {"__title": printed_title(x, p), "__sq": straight_quote_fields(pval(x, p, "straight_quotes"))}
            for f, _ in STAT_FIELDS + [("lore", ""), ("game_text", ""), ("errata_mark", "")]:
                vals[f] = pval(x, p, f)
            vers.append(dict(page=pg, label=(bl[i][0] if (i > 0 and label_of(pg) == "Original") else label_of(pg)), vlabel=bl[i][0], date=date, ref=ref,
                             preserved=preserved, url=url, vals=vals))
        if cbad:
            refuse(key, fam, "conflicting text sources: " + "; ".join(cbad)); continue
        # fields present on some members only -> unknown
        rows = row_order(use_stamp)
        partial = []
        for f, lab in rows:
            pres = [v["vals"].get(f) not in (None, "") for v in vers]
            if any(pres) and not all(pres):
                if f in ("errata_mark",):
                    continue  # absent mark = no mark printed
                partial.append("%s (%s)" % (lab, ", ".join(v["page"] for v, pr in zip(vers, pres) if not pr)))
        _ok = set(z.strip() for z in os.environ.get("ERRGEN_ABSENT_OK", "").split(";") if z.strip())  # PATCH-D
        partial = [pp for pp in partial if "%s|%s" % (fam, pp.split(" (")[0]) not in _ok]
        if partial:
            refuse(key, fam, "field present on some members only (cannot tell if it changed): " + "; ".join(partial)); continue

        def comp(v):
            return tuple(re.sub(r"\s+", " ", plain(v["vals"].get(f) or "")).strip() for f, _ in rows)

        # fold consecutive identical states
        states = []
        for v in vers:
            if states and comp(states[-1][0]) == comp(v):
                states[-1].append(v)
            else:
                states.append([v])
        folded = ["%s→%s" % (v["page"], s[0]["page"]) for s in states for v in s[1:]]
        # prose cross-check: a fold must not hide a described wording change, a column must not
        # contradict prose that says the words are unchanged
        SAME = re.compile(r"words are unchanged|same words|[Ww]ords unchanged|words and mark are unchanged|words (?:of the game text )?are the same")
        pbad = []
        for j, s in enumerate(states):
            for k, v in enumerate(s):
                if j == 0 and k == 0:
                    continue
                eh = pval(live[v["page"]][1], P[v["page"]], "errata_history") or ""
                b = [x for x in bullets(eh, v["page"]) if x[1] == v["page"]]
                wc = b[0][2] if b else ""
                wc = wc[wc.find("What changed"):] if "What changed" in wc else ""
                wc = re.sub(r"<ref[^>]*?/>|<ref[^>]*>.*?</ref>", "", wc, flags=re.S)  # citation text is not prose about the words
                if k > 0 and "became" in wc and not SAME.search(wc):
                    pbad.append("%s folded but its prose says text 'became' something else" % v["page"])
                if k == 0 and SAME.search(wc) and not re.search(r"became|→|\(was |is gone|are gone|[Nn]ew: |removed|added", wc):
                    prev = states[j - 1][0]
                    if fold_quotes(prev["vals"].get("game_text") or "") != fold_quotes(v["vals"].get("game_text") or ""):
                        pbad.append("%s: game_text differs from the previous state but its prose says the words are unchanged" % v["page"])
        if pbad:
            refuse(key, fam, "conflicting text sources: " + "; ".join(pbad)); continue
        if len(states) < 2:
            fam_rows.append((fam, "", "", "; ".join(folded), "no real errata (one text state)" + ("; " + "; ".join(notes) if notes else "")))
            continue
        if tpl in allerr and not existing:
            refuse(key, fam, "%s already exists but no member transcludes it; extend by hand" % tpl); continue
        if tpl in allerr and existing:
            refuse(key, fam, "%s exists on some members; extending an existing table is not automated in this pilot" % tpl); continue

        # rows to keep
        keep = []
        for f, lab in rows:
            vs = [comp(s[0])[rows.index((f, lab))] for s in states]
            if f == "game_text" or len(set(vs)) > 1:
                keep.append((f, lab))
        stamp_only = []
        for j in range(1, len(states)):
            ch = [lab for f, lab in rows if comp(states[j][0])[rows.index((f, lab))] != comp(states[j - 1][0])[rows.index((f, lab))]]
            if ch == ["Stamp"]:
                stamp_only.append(states[j][0]["page"])
        if stamp_only:
            notes.append("stamp-only column(s) kept (--keep-stamp-only): %s" % ", ".join(stamp_only))
        if not use_stamp:
            # show the printed mark as a row only when it is constant inside every column and differs between columns
            marks = [{(w["vals"].get("errata_mark") or "none") for w in s} for s in states]
            if all(len(m) == 1 for m in marks) and len({next(iter(m)) for m in marks}) > 1:
                keep.append(("errata_mark", "Stamp"))
            elif any(len(m) > 1 for m in marks):
                notes.append("Stamp row omitted: a column's same-words members print different marks (%s)" % "; ".join(
                    "%s: %s" % (s[0]["label"], "/".join(sorted(m))) for s, m in zip(states, marks) if len(m) > 1))

        # #1382: quote-style-only differences (adjacent columns, and members folded into one column) go in
        # a table note, never in a highlight
        # A straight mark counts only where the page records it as printed (|straight_quotes=); an
        # unrecorded one may be an old transcription, so it is listed in families.tsv, not on the table.
        qnotes, qunver = [], []

        def _q(f, lab, ov, nv, old_label, new_label, new_page):
            sw = quote_swaps(ov["vals"].get(f) or "", nv["vals"].get(f) or "")
            if not sw:
                return
            if f in QUOTE_FIELDS and quote_verified(f, ov["vals"], nv["vals"], sw):
                qnotes.append(quote_note(lab, old_label, new_label, sw))
            else:
                qunver.append("%s %s vs %s (%s)" % (lab, new_page, ov["page"], ", ".join("%s/%s" % x for x in sw)))

        for f, lab in rows:
            if f == "errata_mark":
                continue
            for j, s in enumerate(states):
                if j > 0:
                    _q(f, lab, states[j - 1][0], s[0], states[j - 1][0]["label"], s[0]["label"], s[0]["page"])
                for w in s[1:]:
                    _q(f, lab, s[0], w, s[0]["label"], "[[%s]] (same column)" % w["page"], w["page"])

        # header
        def colhdr(s):
            v = s[0]
            cur = ""
            if len(s) > 1:
                cur = "|current={{#switch:{{FULLPAGENAME}}|%s=%s|#default={{FULLPAGENAME}}}}" % (
                    "|".join(w["page"] for w in s[1:]), v["page"])
            return "{{Errata col|page=%s%s|label=%s|date=%s|ref=%s}}" % (v["page"], cur, v["label"], v["date"], v["ref"])

        L = ['<includeonly><div class="errata-compare" style="overflow-x:auto;max-width:100%">',
             '{| class="wikitable"',
             "! !! " + " !! ".join(colhdr(s) for s in states)]
        delnotes = []
        for f, lab in keep:
            cells, own = [], []
            for j, s in enumerate(states):
                own.append(False)
                cur = s[0]["vals"].get(f) or ""
                if f == "errata_mark" and not cur:
                    cur = "none"
                if j == 0:
                    cells.append(cell(cur) if cur else "—")
                    continue
                prev = states[j - 1][0]["vals"].get(f) or ""
                if f == "errata_mark" and not prev:
                    prev = "none"
                if re.sub(r"\s+", " ", plain(prev)).strip() == re.sub(r"\s+", " ", plain(cur)).strip():
                    cells.append("—")
                elif not cur and f != "errata_mark":
                    cells.append(hl("none"))  # PATCH-D: field printed before, absent now (approved via ERRGEN_ABSENT_OK)
                    own[j] = True
                elif f in NUMERIC or f in ("uniqueness", "errata_mark", "subtype", "model"):
                    cells.append(hl(cell(cur)) if cur else "—")
                    own[j] = True
                else:
                    w, n, dl = diff_hl(cell(prev), cell(cur))
                    cells.append(w)
                    own[j] = n > 0
                    if dl:
                        # removed words: highlight them in the previous column (as Template:Card errata/First Order
                        # Stormtrooper does), unless that cell already carries its own highlights
                        if not own[j - 1]:
                            ow, on = deleted_hl(cell(prev), cell(cur))
                            if on:
                                cells[j - 1] = ow
                                own[j - 1] = True
                                delnotes.append("%s %s: removed words highlighted in the previous column" % (s[0]["page"], lab))
                        else:
                            delnotes.append("%s %s: words removed, previous column already highlighted; removal not shown" % (s[0]["page"], lab))
            L.append("|-")
            L.append("! " + lab)
            L.append("| " + " || ".join(cells))
        L.append("|}")
        L.append("</div>")
        if qnotes:
            L.append('<div class="errata-note" style="font-size:90%%;">Quote marks: %s</div>' % " ".join(qnotes))
        L.append('<div class="card-family-edit" style="font-size:90%%;">[{{fullurl:%s|action=edit}} Edit errata] · [[%s#Editing|Help]]</div></includeonly><noinclude>' % (tpl, tpl))
        L.append("== Editing ==")
        foldtxt = ""
        if folded:
            foldtxt = " Same-words image changes are not columns: " + "; ".join(
                "[[%s]] shares the [[%s]] column" % tuple(x.split("→")) for x in folded) + "."
        L.append("This shared table is the '''Errata''' section on every %s [[%s]] article. Use '''Edit errata''' on a member page. "
                 "One column per published text state; {{tl|Errata hl}} only the words or values that changed; an em dash if that field "
                 "is unchanged from the previous column.%s%s See [[SWCCG Wiki:Style guide#Errata comparison table]]." % (
                     a.era, owner, " Words a later column removed are highlighted in the column before it." if any(
                         "previous column" in d and "highlighted in" in d for d in delnotes) else "", foldtxt))
        L.append("</noinclude>")
        twiki = "\n".join(L)
        notes += delnotes
        notes += ["quote style only (table note): " + qq for qq in qnotes]
        if qunver:
            notes.append("quote style differs, straight marks not recorded as printed (no table note; check the card, "
                         "then set |straight_quotes= or curl the marks): " + "; ".join(qunver))
        unpres = [s[0]["page"] for s in states if not s[0]["preserved"]]
        if unpres:
            notes.append("ARCHIVE pending: column ref without Preserved copy for " + ", ".join(unpres))
        templates.append((tpl, twiki, owner, key))
        base[tpl] = 0
        cols = "; ".join("%s=%s (%s)" % (s[0]["label"], s[0]["page"], s[0]["date"] or "no date") for s in states)
        fam_rows.append((fam, tpl, cols, "; ".join(folded), "; ".join(notes)))

        # member edits
        for pg in key:
            rv, x = live[pg]
            p = P[pg]
            trans = "{{Card errata/%s}}" % owner
            if "errata_history" in p:
                va, vb = p["errata_history"]
                cur = x[va:vb]
                if cur.lstrip().startswith(trans):
                    summary.append("%s: already transcludes %s (no edit)" % (pg, trans)); continue
                new = x[:va] + trans + "\n" + cur + x[vb:]
                what = "prepended %s to |errata_history=" % trans
            elif "sources" in p:
                sa, _ = p["sources"]
                k = x.rfind("|sources=", 0, sa)
                new = x[:k] + "|errata_history=" + trans + "\n" + x[k:]
                what = "inserted |errata_history=%s before |sources=" % trans
            else:
                refuse(key, fam, "%s: no errata_history and no sources param; member edit skipped" % pg); continue
            members_out.append((pg, new, x, what, twiki, owner))
            base[pg] = rv

    # in-set pages of this era that belong to no in-scope chain
    loosegrp = {}
    for t in sorted(P):
        x = live[t][1]
        if (pval(x, P[t], "set") or "").strip() != a.origin_set or t in scoped:
            continue
        e = era_of(x, P[t])
        if e and a.era not in e:
            continue
        if t in pagechain:
            fam_rows.append((mem2fam.get(t, t), "", "", "", "page %s: its version chain starts outside %s" % (t, a.origin_set)))
            continue
        base_t = re.sub(r"\s+\((?:Errata(?: \d+)?|Remastered(?: \d{4})?)\)$", "", t)
        loosegrp.setdefault((mem2fam.get(t, t), base_t), []).append(t)
    for (fam, base_t), pages in sorted(loosegrp.items()):
        if len(pages) == 1:
            fam_rows.append((fam, "", "", "", "page %s: single printing in this era (no errata_history version list): no table" % pages[0]))
            continue
        flds = [f for f, _ in row_order(use_stamp) if f != "__title"]
        sig = {tuple(re.sub(r"\s+", " ", plain(pval(live[t][1], P[t], f) or "")).strip() for f in flds) for t in pages}
        if len(sig) == 1:
            fam_rows.append((fam, "", "", " | ".join(pages), "no real errata (no errata_history version list; the %d pages carry identical text/stats)" % len(pages)))
        else:
            refused.append((fam, " | ".join(pages), "unsourced order: pages differ in text/stats but carry no errata_history version list with dates"))

    # write drafts
    # page refs copied into table cells (e.g. a lore field's <ref>) must not reuse a member page's ref name
    def _renref(t):
        return re.sub(r'<ref name="(?!errgen-)([^"]+)"(\s*/?)>', r'<ref name="errgen-\1"\2>', t)
    templates = [(tpl, _renref(twiki), owner, key) for tpl, twiki, owner, key in templates]
    for tpl, twiki, owner, key in templates:
        fn = fname(tpl)
        open(os.path.join(out, fn), "w").write(twiki + "\n" if not twiki.endswith("\n") else twiki)
        applies.append((tpl, "%s/%s" % (rel, fn)))
    for pg, new, old, what, twiki, owner in members_out:
        fn = fname(pg)
        open(os.path.join(out, fn), "w").write(new)
        applies.append((pg, "%s/%s" % (rel, fn)))
        summary.append("%s: %s" % (pg, what))

    with open(os.path.join(out, "apply.tsv"), "w") as fh:
        for t, f in applies:
            fh.write("%s\t%s\n" % (t, f))
    json.dump(base, open(os.path.join(out, "base_revids.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(out, "families.tsv"), "w") as fh:
        fh.write("family\towner_template\tcolumns (label=page (date))\tfolded members\tnotes\n")
        for r in fam_rows:
            fh.write("\t".join(r) + "\n")
    with open(os.path.join(out, "refused.tsv"), "w") as fh:
        fh.write("family\tchain\treason\n")
        for r in refused:
            fh.write("\t".join(r) + "\n")

    # self-check
    checks = []
    if not a.no_selfcheck:
        for tpl, twiki, owner, key in templates:
            body = re.search(r"<includeonly>(.*)</includeonly>", twiki, re.S).group(1)
            r = q(action="parse", title=owner, text=body + "\n<references />", contentmodel="wikitext",
                  prop="text|links|templates", disablelimitreport=1)
            h = r["parse"]["text"]
            red = [l["title"] for l in r["parse"]["links"] if not l.get("exists") and l["title"] != tpl]
            redt = [l["title"] for l in r["parse"]["templates"] if not l.get("exists")]
            cite = ("cite_error" in h) or ("mw-ext-cite-error" in h)
            ok = not red and not redt and not cite
            checks.append("TEMPLATE %s: %s%s%s%s" % (tpl, "OK" if ok else "FAIL", " cite_error" if cite else "",
                                                     (" redlinks=" + ", ".join(red)) if red else "",
                                                     (" missing templates=" + ", ".join(redt)) if redt else ""))
        for pg, new, old, what, twiki, owner in members_out:
            # byte check: only errata_history changed
            po, pn = card_params(old), card_params(new)
            same = all(pval(old, po, k) == pval(new, pn, k) for k in po if k not in ("errata_history", "__end__"))
            extra = set(pn) - set(po) - {"errata_history"}
            ehn = pval(new, pn, "errata_history") or ""
            eho = pval(old, po, "errata_history") or ""
            trans = "{{Card errata/%s}}" % owner
            okb = same and not extra and (ehn == trans + "\n" + eho or (not eho and ehn == trans))
            sa, sb = pn["errata_history"]
            outside = new[:sa] + new[sb:] == old[:po["errata_history"][0]] + old[po["errata_history"][1]:] if "errata_history" in po else None
            body = re.search(r"<includeonly>(.*)</includeonly>", twiki, re.S).group(1)
            # no TemplateSandbox on this wiki: render the draft page with the transclusion removed and the
            # table body appended at top level, titled as the member (exercises the current-column marker and
            # any <ref name> collision between the table and the page's own references)
            render = new.replace(trans + "\n", "", 1) + "\n" + body + "\n<references />"
            r = q(action="parse", title=pg, text=render, contentmodel="wikitext", prop="text", disablelimitreport=1)
            h = r["parse"]["text"]
            cite = ("cite_error" in h) or ("mw-ext-cite-error" in h)
            hasbold = "<strong>This (" in h
            checks.append("MEMBER %s: bytes %s%s; parse %s%s" % (
                pg, "OK" if okb else "FAIL", "" if outside in (True, None) else " (outside-errata bytes differ!)",
                "cite_error" if cite else "no cite errors", "; current column bold" if hasbold else "; NO bold current column"))
    with open(os.path.join(out, "diff_summary.txt"), "w") as fh:
        fh.write("errgen drafts — origin set %s, era %s — %d API requests\n" % (a.origin_set, a.era, NREQ[0]))
        nre = sum(1 for r in fam_rows if r[4].startswith("no real errata"))
        fh.write("chains/families: %d tables drafted, %d no real errata, %d single printings/out-of-set chains, "
                 "%d already tabled, %d refused; %d member drafts\n\n" % (
                     len(templates), nre, sum(1 for r in fam_rows if r[4].startswith("page ")),
                     sum(1 for r in fam_rows if "already on every member" in r[4]), len(refused), len(members_out)))
        fh.write("== Member edits ==\n" + "\n".join(summary) + "\n\n== Self-check ==\n" + "\n".join(checks) + "\n")
    print("templates %d, member drafts %d, families rows %d, refused %d, requests %d" % (
        len(templates), len(members_out), len(fam_rows), len(refused), NREQ[0]), file=sys.stderr)


if __name__ == "__main__":
    main()
