#!/usr/bin/env python3
"""Chunked MediaWiki upload (stash chunks, then commit) using wiki_api_apply.Wiki's session.

python3 chunk_upload.py <file> [chunk_mb]
"""
import json, sys, uuid, urllib.request
from pathlib import Path
import wiki_api_apply as w

path = Path(sys.argv[1])
size_chunk = int(float(sys.argv[2] if len(sys.argv) > 2 else 1) * 1024 * 1024)
SUMMARY = "2015 European Championship Day 2 decklist PDF from the Players Committee (Holocron Claude)"
wk = w.Wiki()
data = path.read_bytes()


def multipart(fields, chunk=None):
    b = uuid.uuid4().hex
    body = b"".join(f"--{b}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode() for k, v in fields.items())
    if chunk is not None:
        body += (f"--{b}\r\nContent-Disposition: form-data; name=\"chunk\"; filename=\"{path.name}\"\r\n"
                 "Content-Type: application/octet-stream\r\n\r\n").encode() + chunk + b"\r\n"
    body += f"--{b}--\r\n".encode()
    req = urllib.request.Request(w.API, body, {"Content-Type": f"multipart/form-data; boundary={b}"})
    return wk._open(req)


filekey = None
for off in range(0, len(data), size_chunk):
    f = {"action": "upload", "format": "json", "formatversion": "2", "stash": "1", "filename": path.name,
         "filesize": str(len(data)), "offset": str(off), "ignorewarnings": "1", "token": wk.csrf}
    if filekey:
        f["filekey"] = filekey
    d = multipart(f, data[off:off + size_chunk])
    if "error" in d:
        raise SystemExit(f"chunk {off}: {d['error']}")
    filekey = d["upload"]["filekey"]
    print("chunk", off, d["upload"]["result"], flush=True)

d = multipart({"action": "upload", "format": "json", "formatversion": "2", "filename": path.name, "filekey": filekey,
               "comment": SUMMARY, "ignorewarnings": "1", "token": wk.csrf})
print("COMMIT", json.dumps(d)[:300], flush=True)
