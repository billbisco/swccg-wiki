#!/usr/bin/env python3
"""check_nav.py - independent line-level checker for a navgen draft folder (read-only).

    cd /home/claude/pc601/drafts && python3 /home/claude/navgen/check_nav.py nav1342

For every member page it fetches the BASE revision (base_revids.json) and compares line by line:
the only permitted differences are
  A  one inserted line  |versions={{Card versions/T}}  directly after the "{{Card" line (page had no |versions=)
  B  the |versions=... line replaced by  |versions={{Card versions/T}}
  C  the |printings=... line replaced by |printings={{Card versions/T}}
where T is a template drafted in the same folder that lists this page. Any other added, removed or changed
line is an error. For every template: the title is still free on the wiki; every entry is an existing,
non-redirect page in Category:Cards; no duplicates; every entry is a page drafted to transclude it and vice
versa; the highlight parameter is exactly current={{{current|{{FULLPAGENAME}}}}}; all members have one side
and one card type. It also runs style_lint.lint() on base and draft of every member and reports any flag
present on the draft but not on the base. Requests are spaced >= 0.55 s (< 2 req/s).
"""
import collections, difflib, json, os, re, sys, time, urllib.parse, urllib.request
sys.path.insert(0, "/home/claude/swtools")
import style_lint  # noqa: E402

API = "https://swccg.com/wiki/api.php"
UA = "swccg-navgen-check/1.0 (read-only)"
_last = [0.0]


def api(**p):
    p.update(format="json", formatversion="2")
    data = urllib.parse.urlencode(p).encode()
    for a in range(5):
        w = _last[0] + 0.55 - time.time()
        if w > 0:
            time.sleep(w)
        _last[0] = time.time()
        try:
            req = urllib.request.Request(API, data=data, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print("retry", e, file=sys.stderr); time.sleep(3 * (a + 1))
    raise RuntimeError("api")


def by_revids(revids):
    out = {}
    revids = sorted(set(revids))
    for i in range(0, len(revids), 50):
        d = api(action="query", revids="|".join(map(str, revids[i:i + 50])), prop="revisions",
                rvprop="content|ids", rvslots="main")
        for p in d["query"]["pages"]:
            for r in p.get("revisions", []):
                out[r["revid"]] = (p["title"], r["slots"]["main"]["content"])
    return out


def page_info(titles):
    out = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        d = api(action="query", titles="|".join(titles[i:i + 50]), prop="info|categories",
                clcategories="Category:Cards", cllimit="max")
        q = d["query"]
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        pages = {p["title"]: p for p in q["pages"]}
        for t in titles[i:i + 50]:
            p = pages.get(norm.get(t, t), {})
            out[t] = dict(exists=bool(p) and not p.get("missing"), redirect=bool(p.get("redirect")),
                          card=bool(p.get("categories")), lastrev=p.get("lastrevid", 0))
    return out


def cats_of(titles):
    out = collections.defaultdict(set)
    titles = sorted(set(titles))
    for i in range(0, len(titles), 50):
        cont = {}
        while True:
            d = api(action="query", titles="|".join(titles[i:i + 50]), prop="categories", cllimit="max", **cont)
            for p in d["query"]["pages"]:
                for c in p.get("categories", []):
                    out[p["title"]].add(c["title"])
            if "continue" in d:
                cont = d["continue"]
            else:
                break
    return out


LINK_RE = re.compile(r"\{\{Card version link\|page=([^|]*)\|label=([^|]*)\|current=([^}]*\}\}\}\}\})\}\}")


def main(g):
    base = json.load(open(os.path.join(g, "base_revids.json")))
    rows = [l.split("\t") for l in open(os.path.join(g, "apply.tsv")).read().splitlines() if l.strip()]
    draft = {t: open(os.path.join(g, os.path.basename(rel))).read() for t, rel in rows}
    tpl = {t: d for t, d in draft.items() if t.startswith("Template:Card versions/")}
    mem = {t: d for t, d in draft.items() if t not in tpl}
    errors, cat = [], collections.Counter()
    # templates
    listed = collections.defaultdict(list)
    tinfo = page_info(list(tpl))
    for t, d in tpl.items():
        if tinfo[t]["exists"]:
            errors.append(f"{t}: template already exists on the wiki")
        if base.get(t) != 0:
            errors.append(f"{t}: base revid should be 0")
        ents = LINK_RE.findall(d)
        if len(ents) != d.count("{{Card version link"):
            errors.append(f"{t}: unparsed Card version link entry")
        pages = [e[0] for e in ents]
        if len(pages) != len(set(pages)):
            errors.append(f"{t}: duplicate entry")
        for p, lab, cur in ents:
            if cur != "{{{current|{{FULLPAGENAME}}}}}":
                errors.append(f"{t}: wrong highlight parameter on {p}")
            listed[p].append(t)
        name = t.split("/", 1)[1]
        if f'data-card-family="{name}"' not in d or f"{{{{fullurl:{t}|action=edit}}}}" not in d:
            errors.append(f"{t}: family name / edit link mismatch")
    pinfo = page_info([p for p in listed])
    for p, ts in listed.items():
        i = pinfo[p]
        if not i["exists"] or i["redirect"] or not i["card"]:
            errors.append(f"{p}: listed in {ts} but exists={i['exists']} redirect={i['redirect']} card={i['card']}")
        if len(ts) != 1:
            errors.append(f"{p}: listed in {len(ts)} templates")
        if p not in mem:
            errors.append(f"{p}: listed in {ts[0]} but no member draft")
    # members
    revs = by_revids([base[t] for t in mem])
    minfo = page_info(list(mem))
    cats = cats_of(list(mem))
    side_type = collections.defaultdict(set)
    new_flags = 0
    for t, d in sorted(mem.items()):
        if minfo[t]["lastrev"] != base[t]:
            errors.append(f"{t}: live revision {minfo[t]['lastrev']} != base {base[t]} (re-run navgen)")
        bt, old = revs.get(base[t], (None, None))
        if old is None or bt != t:
            errors.append(f"{t}: base revision not found"); continue
        trs = re.findall(r"\{\{Card versions/([^{}]*)\}\}", d)
        tn = set(trs)
        if len(tn) != 1:
            errors.append(f"{t}: transcludes {len(tn)} navigators"); continue
        T = "Template:Card versions/" + next(iter(tn))
        if T not in tpl or listed.get(t) != [T]:
            errors.append(f"{t}: transcludes {T}, which does not list it exactly once")
        tr = "{{Card versions/%s}}" % next(iter(tn))
        ol, nl = old.split("\n"), d.split("\n")
        ok = True
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ol, nl, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            a_, b_ = ol[i1:i2], nl[j1:j2]
            if op == "insert" and b_ == ["|versions=" + tr] and i1 > 0 and ol[i1 - 1] == "{{Card" \
                    and not any(l.startswith("|versions=") for l in ol):
                cat["A insert |versions= after {{Card"] += 1; continue
            if op == "replace" and len(a_) == len(b_):
                good = True
                for x, y in zip(a_, b_):
                    if x.startswith("|versions=") and y == "|versions=" + tr:
                        cat["B replace inline |versions= list"] += 1
                    elif x.startswith("|printings=") and y == "|printings=" + tr:
                        cat["C replace inline |printings= list"] += 1
                    else:
                        good = False
                if good:
                    continue
            ok = False
            errors.append(f"{t}: unexpected {op} {a_[:2]!r} -> {b_[:2]!r}")
        if ok:
            cat["member pages: all differences are pattern changes"] += 1
        # one infobox |versions= and side/type
        inf = re.search(r"^\|side=(.*)$", d, re.M), re.search(r"^\|type=(.*)$", d, re.M)
        side_type[T].add((inf[0].group(1).strip() if inf[0] else "?", inf[1].group(1).strip() if inf[1] else "?"))
        if d.count("|versions=") != 1:
            errors.append(f"{t}: {d.count('|versions=')} |versions= lines")
        # style lint: no new flags
        c = cats.get(t, set())
        fo = set(style_lint.lint(old, t, c)[0]); fn = set(style_lint.lint(d, t, c)[0])
        for f in sorted(fn - fo):
            new_flags += 1; errors.append(f"{t}: NEW style_lint flag {f}")
        if fo:
            cat["member pages with pre-existing style_lint flags (unchanged)"] += 1
    for T, st in side_type.items():
        if len(st) != 1:
            errors.append(f"{T}: members span side/type {st}")
    for t in tpl:
        if not any(listed.get(p) == [t] for p in mem):
            errors.append(f"{t}: no member transcludes it")
    print(f"{g}: {len(tpl)} templates, {len(mem)} member pages")
    for k, v in sorted(cat.items()):
        print(f"  {v:5d}  {k}")
    print(f"  new style_lint flags: {new_flags}")
    print(f"  errors: {len(errors)}")
    for e in errors[:200]:
        print("   ", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(max(main(g) for g in sys.argv[1:]))
