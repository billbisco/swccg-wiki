#!/usr/bin/env python3
"""Resilient wrapper around wiki_api_apply.Wiki for chunked runs (time-boxed, idempotent).

python3 apply_resilient.py files media/*        # upload files not already present with the same SHA-1
python3 apply_resilient.py pages titles.tsv     # edit pages (skips unchanged); reviews via Wiki.edit
Stops before --budget seconds (default 150) and prints DONE or PARTIAL so it can be re-run.
"""
import hashlib, sys, time
from pathlib import Path
import wiki_api_apply as w

SUMMARY = "2015 European Championship Day 2 decklists from the PC Xerox PDFs (Holocron Claude)"
budget = 150
args = sys.argv[1:]
if "--budget" in args:
    i = args.index("--budget"); budget = int(args[i + 1]); del args[i:i + 2]
mode, rest = args[0], args[1:]
t0 = time.time()
wk = w.Wiki()


def remote_sha1(name):
    r = wk.get(action="query", titles=f"File:{name}", prop="imageinfo", iiprop="sha1")
    pages = r["query"]["pages"]
    p = pages[0] if isinstance(pages, list) else list(pages.values())[0]
    ii = p.get("imageinfo")
    return ii[0]["sha1"] if ii else None


left = 0
if mode == "files":
    for f in map(Path, rest):
        if time.time() - t0 > budget:
            left += 1; continue
        local = hashlib.sha1(f.read_bytes()).hexdigest()
        if remote_sha1(f.name) == local:
            print("SKIP", f.name, flush=True); continue
        for attempt in range(3):
            try:
                print("FILE", f.name, wk.upload(f, SUMMARY), flush=True); break
            except Exception as e:  # dropped connection: check whether it landed
                time.sleep(3)
                if remote_sha1(f.name) == local:
                    print("FILE", f.name, "Success (confirmed after", type(e).__name__ + ")", flush=True); break
        else:
            print("FAIL", f.name, flush=True)
elif mode == "pages":
    tsv = Path(rest[0]); base = tsv.resolve().parent
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if "\t" not in line:
            continue
        title, rel = line.split("\t", 1)
        if time.time() - t0 > budget:
            left += 1; continue
        for attempt in range(3):
            try:
                print("PAGE", title, wk.edit(title, (base / rel).read_text(encoding="utf-8"), SUMMARY), flush=True); break
            except Exception as e:
                print("RETRY", title, type(e).__name__, flush=True); time.sleep(3)
        else:
            print("FAIL", title, flush=True)
print("PARTIAL left", left if left else "", flush=True) if left else print("DONE", flush=True)
