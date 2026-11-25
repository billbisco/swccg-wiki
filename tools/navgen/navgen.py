#!/usr/bin/env python3
"""navgen.py - draft shared Versions navigators for card families that have none.

swccg-guild/work#1342 (child of #1325). Reusable for #1343 (VS 10-19), #1344 (VS 20-27, P, D,
Premium), #1345 (Reflections Gold playtest/Remastered) and #1346 (Virtual Legacy).

DRAFTS ONLY: reads the live wiki (read-only API, < 2 requests/second) and the #1325 census; writes a
draft folder in the standard apply format. It never saves a wiki page and never writes to GitHub.

House pattern followed (most recent closed rollout, Theed Palace #1303, 2026-11-22; e.g.
Template:Card versions/Droid Racks (Theed Palace), diff
https://swccg.com/wiki/index.php?diff=353139&oldid=297907 and ...?diff=353072&oldid=340155):

  * template  Template:Card versions/<base article title> (<origin set>)
  * body      <includeonly><div class="card-family-versions" data-card-family="<name>"> one
              card-family-era div per era (Decipher, Virtual Original, Virtual Legacy, Virtual Modern),
              each with card-family-edition headings ([[Set|Set]]); entries
              {{Card version link|page=..|label=..|current={{{current|{{FULLPAGENAME}}}}}}} joined by " · ",
              oldest to newest; then the "Edit versions · Help" line; <noinclude> editing note +
              [[Category:Templates]].
  * members   |versions={{Card versions/<name>}}: replaces an existing |versions= value in place,
              otherwise is inserted as the first infobox line (right after "{{Card");
              an inline |printings= list is replaced by the same transclusion. Nothing else changes
              (hatnotes, errata_history, sources ... are kept byte for byte).

Usage:
  navgen.py --ticket 1342 --out /home/claude/pc601/drafts/nav1342
  navgen.py --owner "Virtual Sets 10-19" --out DIR
  navgen.py --family "Coarse And Rough And Irritating [Dark effect]" --out DIR
Options: --census DIR (default /home/claude/census1325), --status "no navigator" (repeatable),
         --era "Virtual Modern", --origin-set REGEX, --limit N, --cache-only (no live fetch; testing).

Output (DIR): one .wiki per page ("/" in a title is written as %2F in the file name), apply.tsv
(title<TAB>drafts/<dir>/<file>), base_revids.json (0 for new templates), families.tsv (drafted
families: template, order, labels), refused.tsv (family, reason), diff_summary.txt (dry-run diff of
every page), navgen.log.
"""
import argparse, collections, csv, datetime, difflib, json, os, re, sys, time, urllib.parse, urllib.request

API = "https://swccg.com/wiki/api.php"
UA = "swccg-navgen/1.0 (read-only draft generator; swccg-guild/work#1342)"
MIN_INTERVAL = 0.55

TICKETS = {  # ticket -> census owner-label substrings (labels were assigned before the tickets)
    "1342": ["Virtual Modern-origin families: Virtual Sets 0-9"],
    "1343": ["Virtual Modern-origin families: Virtual Sets 10-19"],
    "1344": ["Virtual Modern-origin families: Virtual Sets 20-27",
             "Virtual Modern-origin families: Sets P, D, Premium and undated"],
    "1345": ["Reflections Gold playtest/Remastered pairs"],
    "1346": ["Virtual Legacy-origin families (Blocks 1-9 / Virtual Shields)"],
}

ERA_ORDER = ["Decipher", "Virtual Original", "Virtual Legacy", "Virtual Modern"]
ERA_HEAD = {"Decipher": "[[Decipher era|Decipher Era]]",
            "Virtual Original": "[[Virtual Original|Virtual Original Era]]",
            "Virtual Legacy": "[[Virtual Legacy|Virtual Legacy Era]]",
            "Virtual Modern": "[[Virtual Modern|Virtual Modern Era]]"}

AI_MARK = re.compile(r"\s*\((?:AI|ALT|Holo AI|Holo ALT)\)\s*$", re.I)
# trailing article-title qualifiers that name a version (not part of the family name)
VQ = re.compile(r"\s*\((?:Errata(?: \d+)?|PC Errata(?: \d+)?|ALT|AI|Holo AI|Holo ALT|Remastered|"
                r"Playtest|Reflections Gold|Reflections Gold Remastered|Virtual Block \d+|Virtual Shields|"
                r"Virtual Set \d+: [^()]+|Virtual Set [0-9A-Z]+)\)\s*$")
MON = "January|February|March|April|May|June|July|August|September|October|November|December"
MONTHS = {m: i + 1 for i, m in enumerate(MON.split("|"))}


# ------------------------------------------------------------------ census helpers (import)
def load_census_module(cdir):
    sys.path.insert(0, cdir)
    import census  # noqa: E402  (stdlib-only; defines parse helpers; main() not run on import)
    sys.path.pop(0)
    return census


# ------------------------------------------------------------------ live API (read-only)
_last = [0.0]
NREQ = [0]


def api(params):
    params = dict(params, format="json", formatversion="2")
    data = urllib.parse.urlencode(params).encode()
    for attempt in range(6):
        wait = _last[0] + MIN_INTERVAL - time.time()
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time(); NREQ[0] += 1
        try:
            req = urllib.request.Request(API, data=data, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print(f"  retry {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("API failed")


def live_pages(titles):
    """title -> {'text','revid','missing','redirect_to'} (redirects not followed for content)."""
    out = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = api(dict(action="query", titles="|".join(chunk), prop="revisions|info",
                     rvprop="content|ids", rvslots="main"))
        q = d.get("query", {})
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        pages = {p["title"]: p for p in q.get("pages", [])}
        for t in chunk:
            p = pages.get(norm.get(t, t), {})
            if not p or p.get("missing") or p.get("invalid"):
                out[t] = {"missing": True, "text": None, "revid": 0, "redirect": False}
                continue
            r = (p.get("revisions") or [{}])[0]
            out[t] = {"missing": False, "text": r.get("slots", {}).get("main", {}).get("content", ""),
                      "revid": r.get("revid", 0), "redirect": bool(p.get("redirect"))}
    return out


def live_resolve(titles):
    """title -> (exists, final title after redirects)."""
    res = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = api(dict(action="query", titles="|".join(chunk), redirects="1"))
        q = d.get("query", {})
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        redir = {r["from"]: r["to"] for r in q.get("redirects", [])}
        pages = {p["title"]: p for p in q.get("pages", [])}
        for t in chunk:
            t2 = norm.get(t, t); n = 0
            while t2 in redir and n < 5:
                t2 = redir[t2]; n += 1
            p = pages.get(t2.split("#")[0], {})
            res[t] = (bool(p) and not p.get("missing") and not p.get("invalid"), t2)
    return res


# ------------------------------------------------------------------ wikitext helpers
def top_param_span(text, name):
    """(start of value, end of value) of top-level |name= in the {{Card ...}} infobox, or None.
    The value ends at the next top-level '\\n|' or at the infobox's closing '}}'."""
    off = card_offset(text)
    if off is None:
        return None
    depth_b = depth_l = 0
    i, n = off + 2, len(text)
    cur_name, val_start = None, None
    hit = None
    while i < n:
        if text.startswith("{{", i):
            depth_b += 1; i += 2; continue
        if text.startswith("}}", i):
            if depth_b == 0:
                if cur_name == name:
                    hit = (val_start, i - 1 if text[i - 1] == "\n" else i)
                return hit
            depth_b -= 1; i += 2; continue
        if text.startswith("[[", i):
            depth_l += 1; i += 2; continue
        if text.startswith("]]", i):
            depth_l = max(0, depth_l - 1); i += 2; continue
        if text[i] == "|" and depth_b == 0 and depth_l == 0 and text[i - 1] == "\n":
            if cur_name == name and hit is None:
                hit = (val_start, i - 1)
            m = re.match(r"\|\s*([a-z_0-9]+)\s*=", text[i:])
            cur_name = m.group(1) if m else None
            val_start = i + (m.end() if m else 1)
        i += 1
    return hit


def card_offset(text):
    """Index of the '{{Card' line that opens the infobox (first line, or after leading hatnote lines)."""
    if text.startswith("{{Card\n"):
        return 0
    i = text.find("\n{{Card\n")
    if i < 0:
        return None
    head = text[:i + 1]
    # only whole-line templates (hatnotes) may precede the infobox
    if all(re.fullmatch(r"\{\{(?:Hatnote|hatnote|DISPLAYTITLE:[^{}]*)[^\n]*\}\}", ln) for ln in head.strip().split("\n")):
        return i + 1
    return None


def get_param(text, name):
    s = top_param_span(text, name)
    return None if s is None else text[s[0]:s[1]]


def set_param(text, name, value):
    s = top_param_span(text, name)
    return text[:s[0]] + value + text[s[1]:]


def parse_inline_list(val):
    """Entries of an old inline Versions/printings list, split on <br />. Returns (entries, ok);
    entry = ('self', None) | ('link', title). Accepted entry shapes (all seen on the wiki):
      bold label — bold or plain "this page" ...                     -> self
      bold label — [[Page]] (<code>id</code>), [[Set]], date          -> first link is the page
      Decipher — [[Page|label]] ...  /  [[Page|label]] (<code>id</code>)  -> first link is the page
      [Decipher — ] bold label [(<code>id</code>)]  (no link)           -> self (the current page)
    Anything else (templates, multi-line values, free text) is unexpected."""
    ents = []
    if "\n" in val.strip():
        return ents, False
    for part in re.split(r"<br\s*/?>", val.strip()):
        part = part.strip()
        if not part:
            continue
        if "{{" in part.replace("{{!}}", ""):
            return ents, False
        if re.search(r"(?:—|–|-)\s*(?:''')?this page(?:''')?", part):
            ents.append(("self", None)); continue
        m = re.match(r"(?:'''[^']+'''|[A-Za-z][A-Za-z ()]*?)?\s*(?:—|–|-)?\s*\[\[([^\]|#]+)[^\]]*\]\]", part)
        if m:
            ents.append(("link", m.group(1).strip().replace("_", " "))); continue
        if re.fullmatch(r"(?:[A-Za-z][A-Za-z ]*\s*(?:—|–|-)\s*)?'''[^'\[\]]+'''(?:\s*\(<code>[^<]*</code>\))?", part):
            ents.append(("self", None)); continue
        return ents, False
    return ents, True


def parse_date_tokens(s):
    """[((y,m,d), precision, position)] in order of position; d=0 for month precision."""
    out = []
    for m in re.finditer(r"(\d{1,2}) (" + MON + r") (\d{4})", s):
        out.append(((int(m.group(3)), MONTHS[m.group(2)], int(m.group(1))), 3, m.start()))
    for m in re.finditer(r"(\d{4})-(\d{2})-(\d{2})(?:T|\b)", s):
        out.append(((int(m.group(1)), int(m.group(2)), int(m.group(3))), 3, m.start()))
    for m in re.finditer(r"(?<![0-9] )\b(" + MON + r") (\d{4})", s):
        out.append(((int(m.group(2)), MONTHS[m.group(1)], 0), 2, m.start()))
    return sorted(out, key=lambda t: t[2])


def bullet_dates(eh, self_title):
    """{title: (y,m,d)} first-publication date of each version-history bullet of |errata_history=.
    Prefers the date after 'First published', then after 'uploaded'/'published'/'import'/'committed'/
    'archived', then the first date in the bullet (by position)."""
    res = {}
    for line in (eh or "").split("\n"):
        if not line.startswith("*"):
            continue
        head = re.sub(r"<ref[^>]*>.*?</ref>|<ref[^>]*/>", "", line)
        # rulings/decision stamps such as "(Bill, 12 Nov 2026)" are not publication dates
        head = re.sub(r"\([^()]*\b(?:Bill|ALT-PNG|Chief)\b[^()]*\)", "", head)
        m = re.match(r"\*\s*'''[^']*'''\s*\((this page|\[\[([^\]|#]+)[^\]]*\]\])\)", head)
        if not m:
            continue
        tgt = self_title if m.group(1) == "this page" else m.group(2).strip()
        body = head[m.end():]
        d = None
        for kw in (r"First published", r"uploaded|published|import|committed|archived"):
            k = re.search(r"\b(?:" + kw + r")\b", body)
            if k:
                toks = parse_date_tokens(body[k.end():k.end() + 60])
                if toks:
                    d = toks[0][0]
                    break
        if d is None:
            toks = parse_date_tokens(body)
            if toks:
                d = toks[0][0]
        if d:
            res[tgt] = d
    return res


def cmp_dates(a, b):
    """-1 a<b, 1 a>b, 0 same/uncomparable (month precision vs same month)."""
    if a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    if a[1] != b[1]:
        return -1 if a[1] < b[1] else 1
    if a[2] and b[2] and a[2] != b[2]:
        return -1 if a[2] < b[2] else 1
    return 0


# ------------------------------------------------------------------ labels
def version_parts(title, stem):
    """('lineage', errata_no, extra) from the qualifiers after the family stem."""
    rest = title[len(stem):] if title.startswith(stem) else None
    if rest is None:
        return None
    quals = re.findall(r"\s*\(([^()]*)\)", rest)
    if re.sub(r"\s*\([^()]*\)", "", rest).strip():
        return None
    lineage, errata, extra = "", 0, []
    for q in quals:
        if q in ("ALT", "AI", "Holo AI", "Holo ALT"):
            if lineage or errata:
                return None
            lineage = "ALT" if q in ("ALT", "AI") else "Holo AI"
        elif re.fullmatch(r"Errata(?: \d+)?", q):
            if errata:
                return None
            errata = int(q.split()[1]) if " " in q else 1
        elif q == "Remastered":
            extra.append("PC Remastered")
        elif q == "Playtest":
            extra.append("Playtest")
        elif q == "Reflections Gold":
            extra.append("Original playtest")
        elif q == "Reflections Gold Remastered":
            extra.append("Remastered")
        elif re.fullmatch(r"Virtual Block \d+|Virtual Shields|Virtual Set \d+: .+|Virtual Set [0-9A-Z]+", q):
            continue  # set qualifier: the edition heading already says it
        else:
            return None
    return lineage, errata, extra


def make_label(vp):
    lineage, errata, extra = vp
    bits = []
    if lineage:
        bits.append(lineage)
    if errata:
        bits.append("Errata" if errata == 1 else f"Errata {errata}")
    bits += extra
    if not bits:
        return "Original"
    return " ".join(bits)


# ------------------------------------------------------------------ template text
def render_template(tname, members_by_era):
    full = "Template:Card versions/" + tname
    parts = [f'<includeonly><div class="card-family-versions" data-card-family="{tname}">']
    for era in ERA_ORDER:
        ms = members_by_era.get(era)
        if not ms:
            continue
        parts.append(f'<div class="card-family-era" style="margin:0 0 0.55em;"><strong><u>{ERA_HEAD[era]}</u>'
                     f'</strong><div class="card-family-indent" style="margin-left:6px;">')
        cur_ed, first = None, True
        for m in ms:
            if m["edition"] != cur_ed:
                if not first:
                    parts.append("<br />")
                parts.append(f'<strong class="card-family-edition" style="font-size:95%;"><u>'
                             f'[[{m["edition"]}|{m["edition"]}]]</u></strong><br />')
                cur_ed, first = m["edition"], True
            if not first:
                parts.append(" · ")
            parts.append("{{Card version link|page=%s|label=%s|current={{{current|{{FULLPAGENAME}}}}}}}"
                         % (m["title"], m["label"]))
            first = False
        parts.append("</div></div>")
    parts.append(f'<div class="card-family-edit" style="font-size:90%;">[{{{{fullurl:{full}|action=edit}}}} '
                 f'Edit versions] · [[{full}#Editing the family navigator|Help]]</div></div></includeonly>\n'
                 "<noinclude>\n== Editing the family navigator ==\nEach publication article includes this "
                 "template in its Versions field. List canonical publication articles in order.\n\n"
                 "[[Category:Templates]]\n</noinclude>")
    return "".join(parts)


def member_edit(text, tname):
    """New wikitext for a member page, or (None, reason)."""
    tr = "{{Card versions/%s}}" % tname
    off = card_offset(text)
    if off is None:
        return None, "unexpected text before the infobox"
    out = text
    if top_param_span(out, "versions") is not None:
        out = set_param(out, "versions", tr)
    else:
        k = off + len("{{Card\n")
        out = out[:k] + "|versions=" + tr + "\n" + out[k:]
    if top_param_span(out, "printings") is not None:
        out = set_param(out, "printings", tr)
    return out, None


def fname(title):
    return title.replace("/", "%2F") + ".wiki"


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--census", default="/home/claude/census1325")
    ap.add_argument("--ticket", choices=sorted(TICKETS))
    ap.add_argument("--owner", action="append", default=[], help="census owner-label substring")
    ap.add_argument("--family", action="append", default=[], help="exact census family label")
    ap.add_argument("--status", action="append", default=[], help="census status filter (default: any)")
    ap.add_argument("--era", action="append", default=[])
    ap.add_argument("--origin-set", default=None, help="regex on census origin_set")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cache-only", action="store_true", help="use census cache text, no live fetch (testing only)")
    a = ap.parse_args()

    C = load_census_module(a.census)
    cards = json.load(open(os.path.join(a.census, "cache", "cards.json")))
    tpls = json.load(open(os.path.join(a.census, "cache", "templates.json")))
    fams = list(csv.DictReader(open(os.path.join(a.census, "families.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
    gaps = list(csv.DictReader(open(os.path.join(a.census, "gaps.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
    gaps_by_fam = collections.defaultdict(list)
    for g in gaps:
        gaps_by_fam[g["family"]].append(g)

    owners = list(a.owner) + (TICKETS[a.ticket] if a.ticket else [])

    def selected(f):
        if a.family and f["family"] not in a.family:
            return False
        if owners and not any(o in f["owner"] for o in owners):
            return False
        if a.status and f["status"] not in a.status:
            return False
        if a.era and f["era"] not in a.era:
            return False
        if a.origin_set and not re.search(a.origin_set, f["origin_set"]):
            return False
        return bool(a.family or owners or a.status or a.era or a.origin_set)

    # ---- family keys (side, type, name) from member infoboxes
    info_of = {}

    def info(t):
        if t not in info_of:
            info_of[t] = C.parse_infobox(cards[t]["text"]) if t in cards else None
        return info_of[t]

    def key_of(t, inf=None):
        inf = inf or info(t)
        return (C.norm_side(inf.get("side", "")), C.norm_type(inf.get("type", "")), C.name_key(inf, t))

    def loose(k):
        s, ty, n = k
        n = re.sub(r"\s*\([^()]*\)", "", n).strip()
        return (s, ty, n)

    fam_rows = {f["family"]: f for f in fams}
    fam_members = {f["family"]: [m.strip() for m in f["members"].split(" | ") if m.strip()] for f in fams}
    fam_keys = {}
    by_key = collections.defaultdict(list)
    by_loose = collections.defaultdict(set)
    for f in fams:
        ks = {key_of(m) for m in fam_members[f["family"]] if m in cards and info(m)}
        fam_keys[f["family"]] = ks
        for k in ks:
            by_key[k].append(f["family"])
    page_family = {}
    for fn_, ms in fam_members.items():
        for m in ms:
            page_family[m] = fn_
    for t in cards:
        if cards[t].get("redirect") or not info(t):
            continue
        by_loose[loose(key_of(t))].add(t)

    # ---- AI/ALT families join the family of the original artwork (Style guide: Official AI and ALT)
    parent = {}
    parent_problem = {}
    for f in fams:
        ks = fam_keys[f["family"]]
        if len(ks) != 1:
            continue
        s, ty, n = next(iter(ks))
        b = AI_MARK.sub("", n)
        if b == n:
            continue
        cands = sorted(set(by_key.get((s, ty, b), [])))
        if len(cands) == 1:
            parent[f["family"]] = cands[0]
        elif len(cands) > 1:
            parent_problem[f["family"]] = "AI/ALT family matches several parent families: " + "; ".join(cands)
    children = collections.defaultdict(list)
    for ch, p in parent.items():
        children[p].append(ch)

    def root_of(fn_):
        seen = 0
        while fn_ in parent and seen < 3:
            fn_ = parent[fn_]; seen += 1
        return fn_

    sel = [f["family"] for f in fams if selected(f)]
    os.makedirs(a.out, exist_ok=True)
    log = open(os.path.join(a.out, "navgen.log"), "w")
    refused, deferred, groups = [], [], []
    seen_roots = set()
    for fn_ in sel:
        r = root_of(fn_)
        if fn_ in parent_problem:
            refused.append((fn_, parent_problem[fn_])); continue
        if r != fn_ and not selected(fam_rows[r]):
            pr = fam_rows[r]
            if pr["navigators"]:
                refused.append((fn_, f"official AI/ALT of [{r}], which already has {pr['navigators']} "
                                     f"(owner {pr['owner']}): add these pages to that navigator instead"))
            else:
                deferred.append((fn_, f"official AI/ALT of [{r}] (origin {pr['origin_set']}, owner "
                                      f"{pr['owner']}): drafted with that family's ticket"))
            continue
        if r in seen_roots:
            continue
        seen_roots.add(r)
        groups.append(r)
    if a.limit:
        groups = groups[:a.limit]

    # ---- live fetch of every member page, the would-be template titles and the edition pages
    group_members = {}
    for r in groups:
        fl = [r] + sorted(children.get(r, []))
        group_members[r] = (fl, [m for x in fl for m in fam_members[x]])
    all_members = sorted({m for _, ms in group_members.values() for m in ms})
    live = {} if a.cache_only else live_pages(all_members)

    def text_of(t):
        if a.cache_only:
            return cards[t]["text"], 0
        lv = live.get(t) or {}
        return (None, 0) if lv.get("missing") else (lv["text"], lv["revid"])

    drafts = {}   # title -> (text, base_revid)
    out_fams = []
    plans = []
    link_targets = set()
    for r in groups:
        fl, mem = group_members[r]
        reason = None
        # census-flagged problems other than "no navigator"
        for x in fl:
            fr = fam_rows[x]
            if fr["navigators"]:
                reason = f"[{x}] already has a navigator ({fr['navigators']})"; break
            probs = [g["problem"] for g in gaps_by_fam.get(x, []) if g["problem"] != "no navigator"]
            if probs:
                reason = f"census flags [{x}]: " + "; ".join(sorted(set(probs))); break
            if fr["status"] not in ("no navigator", "OK (single printing)"):
                reason = f"[{x}] census status is '{fr['status']}', not 'no navigator'"; break
        if not reason and len(mem) < 2:
            reason = "single printing (no navigator needed)"
        texts = {}
        if not reason:
            for m in mem:
                tx, rev = text_of(m)
                if tx is None:
                    reason = f"member [{m}] no longer exists"; break
                if a.cache_only is False and live[m]["redirect"]:
                    reason = f"member [{m}] is now a redirect"; break
                if re.search(r"\{\{\s*(?:[Tt]emplate:)?[Cc]ard[ _]versions/", tx):
                    reason = f"member [{m}] already transcludes a Card versions navigator"; break
                inf = C.parse_infobox(tx)
                if not inf:
                    reason = f"member [{m}] has no Card infobox"; break
                if card_offset(tx) is None:
                    reason = f"member [{m}]: unexpected text before the infobox"; break
                texts[m] = (tx, rev, inf)
        if not reason:
            ks = {(C.norm_side(i_.get("side", "")), C.norm_type(i_.get("type", ""))) for _, _, i_ in texts.values()}
            if len(ks) != 1:
                reason = "members span sides/types: " + ", ".join(sorted("/".join(k) for k in ks))
        if not reason:
            eras = {m: C.era_of(i_, m) for m, (_, _, i_) in texts.items()}
            rg = [m for m, e in eras.items() if e == "Reflections Gold / independent"]
            if rg and len(rg) != len(mem):
                reason = ("picture check: Reflections Gold page(s) in a family with other printings: "
                          + ", ".join(rg))
            elif any(e not in ERA_ORDER and e != "Reflections Gold / independent" for e in eras.values()):
                reason = "unknown era on a member"
        if not reason:
            # family stem = earliest-origin article title without version qualifiers
            stems = {}
            for m in mem:
                s = m
                while True:
                    s2 = VQ.sub("", s)
                    if s2 == s:
                        break
                    s = s2
                stems[m] = s
            root_mem = fam_members[r]
            root_stems = {stems[m] for m in root_mem}
            # the root family's own stem (AI children carry an extra (ALT)/(AI)/(Holo AI) handled by VQ)
            if len(root_stems) != 1:
                reason = "root family members do not share one base title: " + ", ".join(sorted(root_stems))
        if not reason:
            stem = next(iter(root_stems))
            vparts = {}
            for m in mem:
                if stems[m] != stem:
                    reason = f"member [{m}] does not share the family base title '{stem}'"; break
                vp = version_parts(m, stem)
                if vp is None:
                    reason = f"unrecognised title qualifier on [{m}] (family base '{stem}')"; break
                vparts[m] = vp
        if not reason:
            labels = {m: make_label(vparts[m]) for m in mem}
            # editions
            eds = {}
            for m, (_, _, i_) in texts.items():
                ed = C.strip_markup(i_.get("set") or "")
                if not ed:
                    reason = f"member [{m}] has no |set="; break
                eds[m] = ed
        if not reason:
            origin = fam_rows[r]["origin_set"]
            if origin.startswith("Reflections Gold"):
                origin = "Reflections Gold"   # the playtest set is the origin of a playtest/Remastered pair
            # Reflections Gold labels follow the Theed Palace precedent (Open Fire!): the 2001 playtest
            # printing is "Original playtest", the Reflections Gold Remastered printing "Remastered"
            for m in mem:
                if vparts[m][0] == "" and vparts[m][1] == 0:
                    if eds[m] == "Reflections Gold":
                        labels[m] = "Original playtest"
                    elif eds[m] == "Reflections Gold Remastered":
                        labels[m] = "Remastered"
            tname = f"{stem} ({origin})"
            # inline lists: format + order + out-of-family links
            lists = {}
            for m, (tx, _, _) in texts.items():
                for fld in ("printings", "versions"):
                    v = get_param(tx, fld)
                    if v is None or not v.strip():
                        continue
                    ents, ok = parse_inline_list(v)
                    if not ok:
                        reason = f"unexpected inline-list format in |{fld}= on [{m}]"; break
                    lists.setdefault(m, []).append(ents)
                    for kind, t in ents:
                        if kind == "link":
                            link_targets.add(t)
                if reason:
                    break
        if not reason:
            plans.append(dict(root=r, fams=fl, mem=mem, texts=texts, labels=labels, eras=eras, eds=eds,
                              tname=tname, lists=lists, vparts=vparts, stem=stem))
        else:
            refused.append((r, reason))

    # resolve inline-list link targets (redirects) once
    res = {} if a.cache_only else live_resolve(sorted(t for t in link_targets if t not in cards))
    tnames = ["Template:Card versions/" + p["tname"] for p in plans]
    edition_pages = sorted({e for p in plans for e in p["eds"].values()})
    tlive = {} if a.cache_only else live_resolve(tnames + edition_pages)

    for p in plans:
        r, mem, texts = p["root"], p["mem"], p["texts"]
        memset = set(mem)
        reason = None
        tfull = "Template:Card versions/" + p["tname"]
        if (tlive.get(tfull, (False,))[0]) or tfull in tpls:
            reason = f"{tfull} already exists"
        bad_ed = [e for e in set(p["eds"].values()) if not a.cache_only and not tlive.get(e, (False,))[0]]
        if not reason and bad_ed:
            reason = "edition page missing: " + ", ".join(bad_ed)
        # out-of-family links in the old inline lists
        dropped = set()
        order_lists = []
        if not reason:
            fkey = (C.norm_side(texts[mem[0]][2].get("side", "")), C.norm_type(texts[mem[0]][2].get("type", "")))
            lk = loose((fkey[0], fkey[1], C.name_key(texts[mem[0]][2], mem[0])))
            lk = (lk[0], lk[1], AI_MARK.sub("", lk[2]))
            fam_slugs = {img_slug(i_) for _, _, i_ in texts.values()} - {None}
            for m, lsts in p["lists"].items():
                for ents in lsts:
                    seq = []
                    for kind, t in ents:
                        if kind == "self":
                            seq.append(m); continue
                        tt = t[:1].upper() + t[1:]
                        if tt not in cards and tt in res:
                            ex, tt2 = res[tt]
                            tt = tt2 if ex else tt
                        if tt in memset:
                            seq.append(tt); continue
                        dropped.add(tt)
                        if tt in cards and info(tt):
                            k2 = loose(key_of(tt)); k2 = (k2[0], k2[1], AI_MARK.sub("", k2[2]))
                            if k2 == lk:
                                reason = (f"picture check: [{m}] lists [{tt}] (same side, type and name, "
                                          f"outside this family; census family [{page_family.get(tt, '?')}])")
                                break
                            if (k2[0], k2[2]) == (lk[0], lk[2]):
                                reason = (f"type-rule check: [{m}] lists [{tt}] (same side and name, card type "
                                          f"{k2[1]} vs {lk[1]}; census family [{page_family.get(tt, '?')}])")
                                break
                            if k2[0] == lk[0] and img_slug(info(tt)) and img_slug(info(tt)) in fam_slugs:
                                reason = (f"retitle check: [{m}] lists [{tt}], a different title with the same "
                                          f"card image name ({img_slug(info(tt))}); possibly an earlier title "
                                          f"of this card (census family [{page_family.get(tt, '?')}])")
                                break
                    if reason:
                        break
                    order_lists.append(seq)
                if reason:
                    break
        # chronology
        order = None
        if not reason:
            dates = {}
            for m, (tx, _, _) in texts.items():
                for t, d in bullet_dates(get_param(tx, "errata_history"), m).items():
                    if t in memset:
                        dates.setdefault(t, d)
            for m, (_, _, i_) in texts.items():
                if m not in dates:
                    toks = parse_date_tokens(re.sub(r"<ref[^>]*>.*?</ref>", "", i_.get("released") or ""))
                    if toks:
                        dates[m] = toks[0][0]
            order, why, cnotes = chronology(mem, p["vparts"], p["eras"], order_lists, dates)
            if order is None:
                reason = why
        if reason:
            refused.append((r, reason)); continue
        by_era = collections.OrderedDict()
        for m in order:
            era = p["eras"][m]
            era = "Decipher" if era == "Reflections Gold / independent" else era
            by_era.setdefault(era, []).append(dict(title=m, label=p["labels"][m], edition=p["eds"][m]))
        ttext = render_template(p["tname"], by_era)
        drafts[tfull] = (ttext, 0)
        for m in mem:
            nt, why = member_edit(texts[m][0], p["tname"])
            if nt is None:
                reason = why; break
            drafts[m] = (nt, texts[m][1])
        if reason:
            drafts.pop(tfull, None)
            for m in mem:
                drafts.pop(m, None)
            refused.append((r, reason)); continue
        out_fams.append(dict(root=r, fams=p["fams"], template=tfull, order=order,
                             labels=[p["labels"][m] for m in order], dropped=sorted(dropped),
                             notes=cnotes, dates={m: dates.get(m) for m in order}))

    # ---- write the draft folder
    base = {}
    rows = []
    rel = os.path.basename(os.path.normpath(a.out))
    for t in sorted(drafts, key=lambda x: (not x.startswith("Template:"), x)):
        tx, rev = drafts[t]
        with open(os.path.join(a.out, fname(t)), "w") as fh:
            fh.write(tx)
        base[t] = rev
        rows.append(f"{t}\tdrafts/{rel}/{fname(t)}")
    open(os.path.join(a.out, "apply.tsv"), "w").write("\n".join(rows) + "\n")
    json.dump(base, open(os.path.join(a.out, "base_revids.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(a.out, "families.tsv"), "w") as fh:
        fh.write("family\tjoined_ai_alt_families\ttemplate\tn_members\torder (label, version-history date)\t"
                 "dropped_inline_links\torder_notes\n")
        for f in out_fams:
            fh.write("\t".join([f["root"], " | ".join(f["fams"][1:]), f["template"], str(len(f["order"])),
                                " · ".join(f"{m} ({l}, {fmt_d(f['dates'][m])})" for m, l in zip(f["order"], f["labels"])),
                                " | ".join(f["dropped"]), " | ".join(f["notes"])]) + "\n")
    with open(os.path.join(a.out, "refused.tsv"), "w") as fh:
        fh.write("family\tdisposition\treason\n")
        for fn_, why in refused:
            kids = sorted(children.get(fn_, [])) if fn_ in groups else []
            extra = f" [joined AI/ALT families also not drafted: {'; '.join(kids)}]" if kids else ""
            fh.write(f"{fn_}\trefused\t{why}{extra}\n")
        for fn_, why in deferred:
            fh.write(f"{fn_}\tdeferred\t{why}\n")
    # dry-run diff summary
    with open(os.path.join(a.out, "diff_summary.txt"), "w") as fh:
        fh.write(f"navgen dry run {datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M} UTC  selection={owners or a.family}\n")
        fh.write(f"families selected {len(sel)}; groups {len(groups)}; drafted {len(out_fams)}; "
                 f"refused {len(refused)}; deferred {len(deferred)}\n")
        fh.write(f"templates created {sum(1 for t in drafts if t.startswith('Template:'))}; member pages edited "
                 f"{sum(1 for t in drafts if not t.startswith('Template:'))}; API requests {NREQ[0]}\n\n")
        for f in out_fams:
            fh.write(f"=== {f['root']}  ->  {f['template']} (NEW)\n")
            for m, l in zip(f["order"], f["labels"]):
                old = texts_cache_get(m, live, cards, a.cache_only)
                fh.write(f"  [{l}] {m}\n")
                for ln in difflib.unified_diff(old.splitlines(), drafts[m][0].splitlines(), lineterm="", n=0):
                    if ln.startswith(("---", "+++", "@@")):
                        continue
                    fh.write("      " + (ln if len(ln) < 220 else ln[:217] + "...") + "\n")
            for nt in f["notes"]:
                fh.write("  order note: " + nt + "\n")
            if f["dropped"]:
                fh.write("  dropped inline links (outside the family): " + " | ".join(f["dropped"]) + "\n")
            fh.write("\n")
    msg = (f"selected {len(sel)} families -> {len(groups)} groups; drafted {len(out_fams)}, refused {len(refused)}, "
           f"deferred {len(deferred)}; templates {sum(1 for t in drafts if t.startswith('Template:'))}, "
           f"member pages {sum(1 for t in drafts if not t.startswith('Template:'))}; API requests {NREQ[0]}")
    print(msg); log.write(msg + "\n")
    for fn_, why in refused:
        log.write(f"REFUSED {fn_}: {why}\n")
    for fn_, why in deferred:
        log.write(f"DEFERRED {fn_}: {why}\n")
    log.close()


def img_slug(inf):
    """Card-name part of a Holotable-style image file name: V4-L-imgettingprettygoodatthis-2018-07-08.gif
    -> imgettingprettygoodatthis (AI/ALT suffixes dropped)."""
    f = (inf or {}).get("image") or ""
    m = re.match(r"\s*(?:\[\[)?(?:File:)?[A-Za-z0-9]+-[LD0]-([a-z0-9]+?)(?:_ai|_alt)?(?:[-_.]|$)", f)
    return m.group(1) if m else None


def fmt_d(d):
    if not d:
        return "undated"
    return "%04d-%02d" % d[:2] + ("-%02d" % d[2] if d[2] else "")


def texts_cache_get(m, live, cards, cache_only):
    if cache_only:
        return cards[m]["text"]
    return live[m]["text"]


def chronology(mem, vparts, eras, lists, dates):
    """Order members oldest to newest within each era (Style guide: chronology within an edition; official
    AI/ALT at their own publication dates). Strong constraints: errata numbering within one lineage
    (Original < Errata < Errata 2 ...) and the dated version-history entries; a contradiction between them
    refuses the family. Weak constraints: the old curated inline lists, used only where numbering and dates
    say nothing (an inline list that disagrees with the dates is overridden and reported).
    Returns (order, None, notes) or (None, reason, notes)."""
    before = collections.defaultdict(set)   # a -> {b}: a before b
    src = {}
    notes = []

    def reach(a_, b_):
        stack, seen = [a_], set()
        while stack:
            x = stack.pop()
            if x == b_:
                return True
            for y in before[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        return False

    def add(a_, b_, why, strong=True):
        if a_ == b_ or b_ in before[a_]:
            return None
        if reach(b_, a_):
            if strong:
                return f"chronology conflict: {why} puts [{a_}] before [{b_}], but numbering/dates put it after"
            notes.append(f"dates override the old inline list order of [{a_}] before [{b_}]")
            return None
        before[a_].add(b_); src[(a_, b_)] = why
        return None

    for x in mem:
        for y in mem:
            if x != y and eras[x] == eras[y] and vparts[x][0] == vparts[y][0] and vparts[x][2] == vparts[y][2] \
                    and vparts[x][1] < vparts[y][1]:
                e = add(x, y, "errata numbering")
                if e:
                    return None, e, notes
    for x in mem:
        for y in mem:
            if x != y and x in dates and y in dates and eras[x] == eras[y] and cmp_dates(dates[x], dates[y]) < 0:
                e = add(x, y, "version-history dates (%04d-%02d-%02d < %04d-%02d-%02d)" % (dates[x] + dates[y]))
                if e:
                    return None, e, notes
    for seq in lists:
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                if eras[seq[i]] == eras[seq[j]]:
                    add(seq[i], seq[j], "an inline Versions list", strong=False)
    order = []
    for era in ERA_ORDER + ["Reflections Gold / independent"]:
        rest = [m for m in mem if eras[m] == era]
        while rest:
            free = [m for m in rest if not any(m in before[o] for o in rest if o != m)]
            if len(free) != 1:
                if not free:
                    return None, "chronology cycle among " + ", ".join(rest), notes
                return None, ("cannot order " + " vs ".join(f"[{m}]" for m in free)
                              + " (no inline-list order, errata numbering or dates)"), notes
            order.append(free[0]); rest.remove(free[0])
    return order, None, sorted(set(notes))


if __name__ == "__main__":
    main()
