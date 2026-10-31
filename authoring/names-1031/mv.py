import sys, time, json
from pathlib import Path
import wiki_api_apply as w
wk = w.Wiki(); t0 = time.time()
done = set(Path("moves.done").read_text().splitlines()) if Path("moves.done").exists() else set()
log = open("moves.done", "a")
for line in open(sys.argv[2]):
    if not line.strip(): continue
    a, b = line.rstrip("\n").split("\t")
    if a in done: continue
    if time.time() - t0 > 140: print("PARTIAL"); sys.exit()
    r = wk.post(action="move", **{"from": a}, to=b, movetalk="1", reason=sys.argv[1], token=wk.csrf)
    if "move" in r:
        print("MOVED", a, "->", b); log.write(a + "\n"); log.flush()
    else:
        print("ERR", a, json.dumps(r)[:300])
print("DONE")
