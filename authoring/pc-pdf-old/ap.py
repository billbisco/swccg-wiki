#!/usr/bin/env python3
"""Time-boxed, re-runnable apply for the old-PDF decklist batches (Holocron Claude).

python3 ap.py files "<summary>" media/* pdf/*   # upload files whose wiki SHA-1 differs (chunked when > 4 MB)
python3 ap.py pages "<summary>" all.tsv         # edit pages not yet in done.log
Prints DONE or PARTIAL; run again until DONE.
"""
import hashlib, json, sys, time, uuid, urllib.request
from pathlib import Path
import wiki_api_apply as w

mode, summary, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
budget = 150; t0 = time.time(); wk = w.Wiki(); left = 0


def remote_sha1(name):
    p = wk.get(action="query", titles=f"File:{name}", prop="imageinfo", iiprop="sha1")["query"]["pages"]
    p = p[0] if isinstance(p, list) else list(p.values())[0]
    ii = p.get("imageinfo")
    return ii[0]["sha1"] if ii else None


def chunked(path):
    data = path.read_bytes(); size = 1024 * 1024; filekey = None
    def mp(fields, chunk=None):
        b = uuid.uuid4().hex
        body = b"".join(f"--{b}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode() for k, v in fields.items())
        if chunk is not None:
            body += (f"--{b}\r\nContent-Disposition: form-data; name=\"chunk\"; filename=\"{path.name}\"\r\n"
                     "Content-Type: application/octet-stream\r\n\r\n").encode() + chunk + b"\r\n"
        body += f"--{b}--\r\n".encode()
        return wk._open(urllib.request.Request(w.API, body, {"Content-Type": f"multipart/form-data; boundary={b}"}))
    for off in range(0, len(data), size):
        f = {"action": "upload", "format": "json", "formatversion": "2", "stash": "1", "filename": path.name,
             "filesize": str(len(data)), "offset": str(off), "ignorewarnings": "1", "token": wk.csrf}
        if filekey: f["filekey"] = filekey
        d = mp(f, data[off:off + size])
        if "error" in d: return "ERROR " + json.dumps(d["error"])[:200]
        filekey = d["upload"]["filekey"]
    d = mp({"action": "upload", "format": "json", "formatversion": "2", "filename": path.name, "filekey": filekey,
            "comment": summary, "ignorewarnings": "1", "token": wk.csrf})
    return d.get("upload", {}).get("result", "ERROR " + json.dumps(d)[:200])


if mode == "files":
    for f in map(Path, rest):
        if time.time() - t0 > budget: left += 1; continue
        local = hashlib.sha1(f.read_bytes()).hexdigest()
        if remote_sha1(f.name) == local:
            print("SKIP", f.name, flush=True); continue
        for attempt in range(3):
            try:
                r = chunked(f) if f.stat().st_size > 4 * 1024 * 1024 else wk.upload(f, summary)
                print("FILE", f.name, r, flush=True); break
            except Exception as e:
                time.sleep(3)
                if remote_sha1(f.name) == local:
                    print("FILE", f.name, "Success (confirmed)", flush=True); break
        else:
            print("FAIL", f.name, flush=True)
elif mode == "pages":
    tsv = Path(rest[0]); base = tsv.resolve().parent; log = base / "done.log"
    since = (base / "since.txt").read_text().strip() if (base / "since.txt").exists() else ""
    done = set()
    if log.exists():
        done = {l.split("\t")[1] for l in log.read_text(encoding="utf-8").splitlines() if l.startswith("OK\t")}
    with open(log, "a", encoding="utf-8") as lg:
        for line in tsv.read_text(encoding="utf-8").splitlines():
            if "\t" not in line: continue
            title, rel = line.split("\t", 1)
            if title in done: continue
            if time.time() - t0 > budget: left += 1; continue
            if since:
                pg = wk.get(action="query", titles=title, prop="revisions", rvprop="timestamp|user")["query"]["pages"]
                pg = pg[0] if isinstance(pg, list) else list(pg.values())[0]
                rv = (pg.get("revisions") or [{}])[0]
                if rv and rv["timestamp"] > since and rv["user"] != "Holocron Claude":
                    print("PAGE", title, "CONFLICT edited by", rv["user"], flush=True)
                    lg.write(f"ERR\t{title}\tCONFLICT {rv['user']}\n"); continue
            for attempt in range(3):
                try:
                    r = wk.edit(title, (base / rel).read_text(encoding="utf-8"), summary)
                    print("PAGE", title, r, flush=True)
                    lg.write(("OK" if not r.startswith("ERROR") else "ERR") + "\t" + title + "\t" + r + "\n"); lg.flush(); break
                except Exception as e:
                    print("RETRY", title, type(e).__name__, flush=True); time.sleep(3)
            else:
                print("FAIL", title, flush=True)
print(f"PARTIAL left {left}" if left else "DONE", flush=True)
