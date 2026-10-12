#!/usr/bin/env python3
"""Roll the card-identity naming scheme (shared/swccg-card-identity) to the Original Virtual Sets 1,2,4-17.

    python3 rename_ovs.py fetch OUT     # pull wikitext of every page involved into OUT/src.json (read-only)
    python3 rename_ovs.py build OUT     # write OUT/moves.txt + OUT/y-ovs-rename.tsv + OUT/report.txt

Set pages  `Virtual Set N (Original)`  -> `Virtual Set N: Subtitle`  (+ Talk: if it exists)
Card stubs `Title (V) (Virtual Set N)` -> `Title (V) (Virtual Set N: Subtitle)`   (only the 636 stubs listed in
original-vs-index.json; modern cards that happen to carry a `(Virtual Set N)` suffix are untouched)
Stub fields: set, printings, prev/next, card_uid = GEMP id 11NN_slip, hatnote in the VS3 style, boilerplate
game_text_note / notes dropped. Every other page that links an old title gets the link target rewritten.
"""
from __future__ import annotations
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
ROOT = Path(__file__).resolve().parent
SUBTITLES = {1: "Legacy", 2: "Our Most Desperate Hour", 3: "Revolution", 4: "Battle Of Hoth", 5: "A Dark Time", 6: "City In The Clouds",
             7: "Shadows Of The Empire", 8: "Jabba's Court", 9: "Sanctuary Moon", 10: "Fourth Anthology", 11: "Gathering Storm",
             12: "Martyrs & Magistrates", 13: "Remote Outpost", 14: "Armed & Operational", 15: "Galactic Frontier",
             16: "Revenge Of The Sith", 17: "The Force Unleashed"}
SETS = [n for n in SUBTITLES if n != 3]
BOILER_GTN = re.compile(r"^\s*Game text transcribed from VirtualCards\d+\.pdf (?:Legacy )?slip.*?named from the printed slip where readable\.\s*")
BOILER_NOTES = re.compile(r"^\s*Virtual Original-era printable slip \(Virtual Set \d+ / [^)]*\)\. Overlay for the cited [^.]*where applicable\. Not valid for current Standard / Modern Virtual play\.\s*")


def api(**p):
    p["format"] = "json"
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(API + "?" + urllib.parse.urlencode(p), timeout=90))
        except Exception as e:  # noqa
            time.sleep(3 * (i + 1))
    raise SystemExit(f"API failed: {p}")


def get_pages(titles):
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        r = api(action="query", prop="revisions", rvprop="content", rvslots="main", titles="|".join(chunk))
        for pg in r["query"]["pages"].values():
            if "missing" in pg:
                continue
            out[pg["title"]] = pg["revisions"][0]["slots"]["main"]["*"]
    return out


def backlinks(title):
    out, cont = [], {}
    while True:
        r = api(action="query", list="backlinks", bltitle=title, bllimit=500, blfilterredir="nonredirects", **cont)
        out += [b["title"] for b in r["query"]["backlinks"]]
        if "continue" in r:
            cont = r["continue"]
        else:
            return out


def old_new():
    idx = json.loads((ROOT / "original-vs-index.json").read_text(encoding="utf-8"))
    m = {}
    for pages in idx.values():
        for p in pages:
            mo = re.search(r" \(Virtual Set (\d+)\)$", p)
            if mo and int(mo.group(1)) in SETS:
                n = int(mo.group(1))
                m[p] = p[: -len(mo.group(0))] + f" (Virtual Set {n}: {SUBTITLES[n]})"
    for n in SETS:
        m[f"Virtual Set {n} (Original)"] = f"Virtual Set {n}: {SUBTITLES[n]}"
    return m


def fetch(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    m = old_new()
    titles = list(m) + [f"Talk:{t}" for t in m if t.startswith("Virtual Set")] + [f"Virtual Set {n}" for n in SETS]
    titles += ["Sets", "Main Page", "Virtual Sets (2002-2009)"] + [f"Premiere - Original VS{n}" for n in SETS]
    src = get_pages(titles)
    print("pages fetched", len(src))
    linkers = set()
    for i, t in enumerate(m):
        linkers.update(backlinks(t))
        if i % 100 == 0:
            print("backlinks", i, len(linkers))
    linkers -= set(src)
    src.update(get_pages(sorted(linkers)))
    print("with linkers", len(src))
    (out / "src.json").write_text(json.dumps({"map": m, "src": src}, ensure_ascii=False), encoding="utf-8")


def relink(text: str, m: dict) -> str:
    # link targets [[Old]] [[Old|..]] [[Old#..]] and file link=Old ; also bold-printings '''Virtual Set N (Original)'''
    def sub_link(mo):
        t = mo.group(2).strip()
        key = t[0].upper() + t[1:] if t else t
        return mo.group(1) + m.get(key, t) + mo.group(3)
    text = re.sub(r"(\[\[)([^\[\]|#]+)([|#\]])", sub_link, text)
    text = re.sub(r"(link=)([^|\]]+)([|\]])", sub_link, text)
    for n in SETS:
        text = text.replace(f"Virtual Set {n} (Original)", f"Virtual Set {n}: {SUBTITLES[n]}")
    return text


GTN_DROP = re.compile(r"^(Game text transcribed from VirtualCards|Official text as of|Triangles|ICON KEY letters|Cover has no separate ICON KEY|"
                      r"Uniqueness bullet shown as|Other (slip|sheet) icons named|Cover also defines|Where the slip footer Decipher base differs|IA CDX for )")


def gtn_strip(v: str) -> str:
    if not v.startswith("Game text transcribed from VirtualCards"):
        return f"|game_text_note={v}\n"
    keep = [s for s in re.split(r"(?<=\.) (?![^()]*\))", v.strip()) if s and not GTN_DROP.match(s)]
    return f"|game_text_note={' '.join(keep)}\n" if keep else ""


def fix_stub(title: str, text: str, m: dict, n: int) -> str:
    slip = re.search(r"\|image=VS\d+O-(\d+)-", text)
    if not slip:
        raise ValueError(f"no slip number in {title}")
    uid = f"11{n:02d}_{int(slip.group(1))}"
    text = relink(text, m)
    text = re.sub(r"\|card_uid=[^\n]*", f"|card_uid={uid}", text, count=1)
    if "|card_uid=" not in text:
        text = text.replace("|image=", f"|card_uid={uid}\n|image=", 1)
    def strip(field, rx):
        def f(mo):
            tail = rx.sub("", mo.group(1), count=1).strip()
            return f"|{field}={tail}\n" if tail else ""
        return re.sub(rf"\|{field}=([^\n]*)\n", f, text)
    text = strip("game_text_note", BOILER_GTN)
    text = re.sub(r"\|game_text_note=([^\n]*)\n", lambda mo: gtn_strip(mo.group(1)), text)
    text = strip("notes", BOILER_NOTES)
    for k in ("prev", "next"):
        mo = re.search(rf"\|{k}=([^\n]*)", text)
        if mo and mo.group(1).strip() in m:
            text = text.replace(mo.group(0), f"|{k}={m[mo.group(1).strip()]}")
    code = f"Code OVS{n} · GEMP id {uid}."
    base = re.search(r"\|hatnote=Decipher printing: (\[\[[^\]]+\]\])", text)
    carrier = re.search(r"\|hatnote=Sleeve carrier / prior printing: (\[\[[^\]]+\]\])", text)
    vtitle = re.search(r"\|hatnote=Virtual title (\[\[[^\]]+\]\]); slip footer directs sleeve with (\[\[[^\]]+\]\])", text)
    if base:
        hat = f"For the Decipher card this slip modifies, see {base.group(1)}. {code}"
    elif carrier:
        hat = f"Sleeve this slip over {carrier.group(1)}. {code}"
    elif vtitle:
        hat = f"Sleeve this slip over {vtitle.group(2)}. Modern Players Committee card of the same name: {vtitle.group(1)}. {code}"
    elif "|hatnote=" in text:
        hat = re.search(r"\|hatnote=([^\n]*)", text).group(1).rstrip() + " " + code
    else:
        hat = None
    if hat:
        text = re.sub(r"\|hatnote=[^\n]*", lambda _: "|hatnote=" + hat, text, count=1)
    return text


def build(out: Path):
    d = json.loads((out / "src.json").read_text(encoding="utf-8"))
    m, src = d["map"], d["src"]
    moves, rows, rep = [], [], []
    for n in SETS:
        o, nw = f"Virtual Set {n} (Original)", f"Virtual Set {n}: {SUBTITLES[n]}"
        moves.append(f"{o}|{nw}")
        if f"Talk:{o}" in src:
            moves.append(f"Talk:{o}|Talk:{nw}")
    stubs = {t: v for t, v in m.items() if not t.startswith("Virtual Set")}
    missing = [t for t in stubs if t not in src]
    for t, nw in stubs.items():
        if t in src:
            moves.append(f"{t}|{nw}")
    rep.append(f"moves {len(moves)}; stubs missing on wiki: {len(missing)} {missing[:10]}")
    done = set()
    # stubs (written at their NEW titles, after moveBatch)
    bad = []
    for t, nw in stubs.items():
        if t not in src:
            continue
        n = int(re.search(r"\(Virtual Set (\d+)\)$", t).group(1))
        if f"|set=Virtual Set {n} (Original)" not in src[t]:
            bad.append(t)
            continue
        rows.append((nw, fix_stub(t, src[t], m, n)))
        done.add(t)
    rep.append(f"stubs whose |set= is not 'Virtual Set N (Original)' (skipped): {len(bad)} {bad[:10]}")
    # set pages + talk
    for n in SETS:
        o, nw = f"Virtual Set {n} (Original)", f"Virtual Set {n}: {SUBTITLES[n]}"
        if o in src:
            rows.append((nw, relink(src[o], m)))
            done.add(o)
        if f"Talk:{o}" in src:
            rows.append((f"Talk:{nw}", relink(src[f"Talk:{o}"], m)))
            done.add(f"Talk:{o}")
        # modern hub hatnote
        mod = src.get(f"Virtual Set {n}")
        if mod is not None:
            hat = f"{{{{Hatnote|1=This is the post-2014 Players Committee set. For the pre-2009 Players Committee set also numbered {n} see [[{nw}]].}}}}\n"
            if nw not in mod:
                mod2 = re.sub(r"^\{\{Hatnote\|[^\n]*\n", "", mod) if o in mod.split("\n", 1)[0] else mod
                rows.append((f"Virtual Set {n}", hat + mod2))
            done.add(f"Virtual Set {n}")
    # Main Page tiles: full titles, file links fixed (VS3 included)
    mp = relink(src["Main Page"], m)
    for n, sub in SUBTITLES.items():
        mp = re.sub(rf"\[\[Virtual Set {n}: {re.escape(sub)}\|VS{n} [^\]]*\]\]", f"[[Virtual Set {n}: {sub}]]", mp)
    mp = mp.replace("link=Virtual Set 3 (Original)", "link=Virtual Set 3: Revolution")
    rows.append(("Main Page", mp)); done.add("Main Page")
    sets = relink(src["Sets"], m)
    for n, sub in SUBTITLES.items():
        sets = re.sub(rf"\[\[Virtual Set {n}: {re.escape(sub)}\|Virtual Set {n} &mdash; [^\]]*\]\]", f"[[Virtual Set {n}: {sub}]]", sets)
    rows.append(("Sets", sets)); done.add("Sets")
    # everything else that links an old title
    others = 0
    for t, text in src.items():
        if t in done or t in m or t.startswith("Talk:Virtual Set") or re.fullmatch(r"Virtual Set \d+", t):
            continue
        new = relink(text, m)
        if new != text:
            rows.append((t, new)); others += 1
    rep.append(f"other linking pages rewritten: {others}; total rows {len(rows)}")
    (out / "moves.txt").write_text("\n".join(moves) + "\n", encoding="utf-8")
    (out / "pages").mkdir(exist_ok=True)
    with open(out / "y-ovs-rename.tsv", "w", encoding="utf-8") as f:
        for i, (t, text) in enumerate(rows):
            fn = f"pages/{i:04d}_{re.sub(r'[^A-Za-z0-9]+', '_', t)[:60]}.wiki"
            (out / fn).write_text(text, encoding="utf-8")
            f.write(f"{t}\t{out.name}/{fn}\n")
    (out / "report.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep))


if __name__ == "__main__":
    {"fetch": fetch, "build": build}[sys.argv[1]](Path(sys.argv[2]))
