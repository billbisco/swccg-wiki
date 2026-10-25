"""render.py <out_dir_reviewed_jsons> <final_dir>
For each reviewed deck JSON: fetch the live page, replace the Decklist section with a grouped list (side-aware card
pages), set the Starting Card CardLink. Writes final/pages/*.wiki, final/titles.tsv, final/decks-canon.json, report."""
import json, re, sys, pathlib, collections, urllib.request, urllib.parse, time
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import resolve_wiki as R
src, final = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
(final / "pages").mkdir(parents=True, exist_ok=True)
API = "https://wiki.swccg.com/api.php"
def live(title):
    r = R._q(action="query", titles=title, prop="revisions", rvprop="content", rvslots="main")
    p = r["query"]["pages"][0]
    return p["revisions"][0]["slots"]["main"]["content"] if p.get("revisions") else None
LEFT = ["Objective", "Character", "Effect", "Interrupt", "Epic Event", "Admiral's Order", "Jedi Test", "Podracer"]
RIGHT = ["Location", "Starship", "Vehicle", "Weapon", "Device", "Creature", "Defensive Shield", "Not identified"]
def norm_type(t):
    t = (t or "").strip()
    if t.lower().startswith("admiral"): return "Admiral's Order"
    return t if t in LEFT + RIGHT else (t or "Not identified")
def cardlink(i):
    t = i["title"]; lab = t.replace("•", "")
    # strip side/set qualifiers from label
    lab2 = re.sub(r"( \((?!V\))[^()]*\))+$", "", lab)
    s = "{{CardLink|" + t + "|" + i["image"]
    if lab2 != t: s += "|label=" + lab2
    return s + "}}"
rows, canon, report = [], [], []
for f in sorted(src.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    side = "Dark" if d["side"] == "DS" else "Light"
    groups = collections.OrderedDict(); n_unres = 0; cards = []; shields = []
    def add(line, is_shield):
        global n_unres
        name = (line.get("card") or "").strip()
        info = None
        if name and is_shield:
            info = R.resolve_shield(name, line.get("v"), side)
        elif name:
            for vv in ([bool(line.get("v")), not line.get("v")]):
                i = R.resolve(name, vv, side, line.get("ep1"))
                if i and (not is_shield or i["type"] == "Defensive Shield"):
                    info = i; break
                if not is_shield and not line.get("v"):
                    break   # printed card asked for: don't silently swap in a (V) page
        if info is None:
            key = ("Not identified", "TEXT:" + (line.get("text") or name or "?"))
            report.append(f"UNRESOLVED {d['title']} line {line.get('n')}: text={line.get('text')!r} card={name!r}")
        else:
            typ = "Defensive Shield" if is_shield else norm_type(info["type"])
            key = (typ, info["title"])
            (shields if is_shield else cards).append((name, bool(line.get("v")) and "(V)" in info["title"]))
        groups.setdefault(key[0], collections.OrderedDict())
        g = groups[key[0]]; g[key[1]] = (g.get(key[1], (0, info))[0] + 1, info)
    for l in d["lines"]: add(l, False)
    for l in d.get("shield_lines", []): add(l, True)
    def col(names):
        out = []
        for h in names:
            if h not in groups: continue
            out.append(f"'''{h}'''")
            for k, (q, info) in groups[h].items():
                pre = f"{q}x " if q > 1 else ""
                out.append("* " + pre + (cardlink(info) if info else k[5:].replace("[", "&#91;")))
            out.append("")
        return "\n".join(out).rstrip("\n")
    note = ""
    if "Not identified" in groups:
        note = "Lines the transcription could not identify are printed as written under '''Not identified'''.\n\n"
    body = (note + '{| class="wikitable" style="width:100%;"\n|-\n| style="width:50%; vertical-align:top;" |\n'
            + col(LEFT) + '\n| style="width:50%; vertical-align:top;" |\n' + col(RIGHT) + "\n|}\n")
    txt = live(d["title"])
    if txt is None:
        report.append(f"NOPAGE {d['title']}"); continue
    m = re.search(r"(== Decklist ==\n)(.*?)(\n\n== )", txt, re.S)
    if not m:
        report.append(f"NOSECTION {d['title']}"); continue
    new = txt[:m.start(2)] + "\n" + body + txt[m.end(2):]
    # starting card
    st = d.get("start") or ""
    si = R.resolve(st, False, side) if st else None
    if si:
        new = re.sub(r"^\* '''Starting Card:''' .*$", "* '''Starting Card:''' " + cardlink(si), new, count=1, flags=re.M)
    fn = re.sub(r"[^\w.-]+", "_", d["title"]) + ".wiki"
    (final / "pages" / fn).write_text(new, encoding="utf-8")
    rows.append(f"{d['title']}\tpages/{fn}")
    canon.append({**{k: d[k] for k in ("title", "player", "side", "event", "stage")},
                  "cards": [[1, n, v] for n, v in cards], "shields": [[1, n, v] for n, v in shields],
                  "unresolved": sum(1 for r in report if r.startswith("UNRESOLVED " + d["title"] + " "))})
    report.append(f"OK {d['title']} cards={len(cards)} shields={len(shields)}")
(final / "titles.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
json.dump(canon, open(final / "decks-canon.json", "w"), indent=1, ensure_ascii=False)
(final / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print(len(rows), "pages;", sum(r.startswith("UNRESOLVED") for r in report), "unresolved lines")
