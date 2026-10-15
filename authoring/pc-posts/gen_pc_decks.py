#!/usr/bin/env python3
"""Generate deck pages for PC-sourced decklists (typed posts or transcriptions) with the 2015 EC machinery.

Run from the Windows worktree's wiki/ folder (Linux shell), via:
    python3 gen_pc_decks.py <decks.json> <out_dir>
decks.json: list of {title, player, side: "DS"|"LS", event, stage, format_link, start, cards:[[q,name,v]], shields:[[q,name,v]]}
Writes <out_dir>/<file>.wiki and <out_dir>/titles.tsv. Uses current-virtual Open lookups (never Virtual Block).
"""
import json, os, pathlib, re, sys

W = pathlib.Path(os.environ.get("WIKI_WT", ".")).resolve()
sys.path.insert(0, str(W)); os.chdir(W)
import update_gempc_start_fields as ug
ug.BP_PATH = pathlib.Path(os.environ["BP_PATH"])
import generate_2014_mpc as mpc
mpc.TYPE_OVERRIDE.setdefault("combined attack", "Interrupt")
mpc.TYPE_OVERRIDE.setdefault("tatooine (dark) (coruscant)", "Location")
mpc.TYPE_OVERRIDE.setdefault("tatooine (coruscant)", "Location")
import generate_2014_worlds as w14
import generate_2015_ec as ec           # builds the Open index; install_open_lookup()
from generate_2026_sdso import load_bp_simple

decks = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
ec.install_open_lookup()
_by_id, by_title = load_bp_simple()
rows = []
for d in decks:
    side = "Light" if d["side"] == "LS" else "Dark"
    cards = [(q, n, v, False) for q, n, v in d["cards"]]
    shields = [(q, n, v, True) for q, n, v in d.get("shields", [])]
    groups = mpc.group_cards(cards + shields, by_title)
    unknown = [n for h, rs in groups if h == "Unknown" for _q, n, *_ in rs]
    if unknown:
        print("WARN Unknown types", d["title"], unknown)
    body = mpc.render_groups(groups, side)
    n_obj, is_v, prefer_sh, _label = mpc.starting_from_groups(groups, side)
    if d.get("start"):
        n_obj, is_v = d["start"], False
        head = n_obj.split(" / ")[0].strip()
        for _q, n, v in d["cards"]:
            if n == n_obj or n.startswith(head):
                is_v = v
                if " / " in n:
                    n_obj = n
                break
    start_link = w14.wikilink(n_obj, side, is_v, prefer_sh=prefer_sh)
    w14.EVENT = d["event"]
    w14.CAT = f"[[Category:{d['event'][:4]}]]"
    txt = w14.deck_page(d["title"], d["player"], f"{side} Side", start_link, d["stage"], body, [],
                        player_page=None)
    txt = txt.replace("* '''Format:''' [[Legacy Open]]", f"* '''Format:''' {d.get('format_link', '[[Open]]')}")
    fn = re.sub(r"[^\w.-]+", "_", d["title"]) + ".wiki"
    (out / fn).write_text(txt, encoding="utf-8")
    rows.append(f"{d['title']}\t{fn}")
    n = sum(q for q, *_ in d["cards"])
    if n != 60:
        print("WARN count", d["title"], n)
(out / "titles.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print("generated", len(rows))
