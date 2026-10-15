#!/usr/bin/env python3
"""Validate transcribe_2015_ec_*.py files: counts and card names vs GEMP titles.

python3 validate.py out/transcribe_2015_ec_x.py [more files...]
"""
import importlib.util, json, re, sys, unicodedata, difflib
from pathlib import Path

DB = "/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("•", "").replace("’", "'").lower()
    s = re.sub(r"\s*\(v\)\s*$", "", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


titles = {"LIGHT": {}, "DARK": {}}
for r in json.load(open(DB)):
    t = r.get("title", "")
    side = r.get("side")
    if side in titles:
        titles[side].setdefault(norm(t), t)
        # also index each half of combo/objective titles
        for part in re.split(r"\s*/\s*", t):
            titles[side].setdefault(norm(part), t)
        bare = re.sub(r"\s*\([^)]*\)", "", t)
        titles[side].setdefault(norm(bare), t)


def known(side, name):
    k = norm(name)
    if k in titles[side] or norm(re.sub(r"\s*\([^)]*\)", "", name)) in titles[side]:
        return True
    if all(norm(p) in titles[side] for p in re.split(r"\s*/\s*", name)):
        return True
    return any(t.startswith(k + " ") or k.startswith(t + " ") for t in titles[side] if len(t) > 6)


def check(path: str) -> int:
    spec = importlib.util.spec_from_file_location("m", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    bad = 0
    print(f"== {Path(path).name}  PLAYER={m.PLAYER!r}")
    for side, pre in (("LIGHT", "LS"), ("DARK", "DS")):
        cards = getattr(m, f"{pre}_CARDS", [])
        sh = getattr(m, f"{pre}_SHIELDS", [])
        add = getattr(m, f"{pre}_ADD", [])
        n = sum(q for q, *_ in cards)
        print(f"  {pre}: main={n} shields={sum(q for q,*_ in sh)} add={len(add)} start={getattr(m, pre+'_START', '')!r}")
        if not cards:
            print(f"  {pre}: NO CARDS"); bad += 1
        elif n != 60:
            print(f"  {pre}: WARN main != 60 (ok only if the sheet really says so; explain in {pre}_NOTE)")
        for q, name, v in cards + sh + add:
            if not known(side, name):
                sug = difflib.get_close_matches(norm(name), list(titles[side]), n=3, cutoff=0.6)
                print(f"    UNKNOWN {pre} {name!r}  suggest: {[titles[side][s] for s in sug]}")
                bad += 1
    return bad


if __name__ == "__main__":
    total = sum(check(p) for p in sys.argv[1:])
    print("PROBLEMS", total)
