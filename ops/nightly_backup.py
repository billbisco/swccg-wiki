#!/usr/bin/env python3
"""Nightly preservation backup, run on the VPS by a systemd timer.

Finds every page edited/created/moved and every file uploaded on wiki.swccg.com since the last
successful run (anyone's edits), then:
  * page text  -> billbisco/swccg-wiki        pages/ (+ pages/INDEX.tsv)
  * file bytes -> billbisco/swccg-wiki-files  files/ (+ files/INDEX.tsv, files/USAGE.tsv)
and pushes both. Deleted pages/files are NOT removed from the backups (preservation).

Usage: nightly_backup.py PAGES_REPO FILES_REPO [--state /var/lib/swccg-ops/backup-state.json]
       [--since 2026-10-09T00:00:00Z]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gitsync import commit_and_push, reset_to_origin  # noqa: E402

API = "https://wiki.swccg.com/api.php"
UA = "swccg-wiki-preservation/1.0 (https://github.com/billbisco/swccg-wiki; nightly backup)"


def api(params: dict) -> dict:
    q = {"format": "json", "formatversion": "2", **params}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(q), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def paged(params: dict, key: str) -> list[dict]:
    out, cont = [], {}
    while True:
        d = api({**params, **cont})
        out += d.get("query", {}).get(key, [])
        if "continue" not in d:
            return out
        cont = d["continue"]


def changed_since(since: str) -> tuple[set[str], set[str]]:
    """(page titles, file titles) touched since `since`."""
    pages, files = set(), set()
    rc = paged({"action": "query", "list": "recentchanges", "rcend": since, "rcdir": "older",
                "rcprop": "title|loginfo", "rctype": "edit|new|log", "rclimit": "max"}, "recentchanges")
    for r in rc:
        t = r.get("title", "")
        if r.get("type") == "log":
            if r.get("logtype") == "upload":
                files.add(t)
                continue
            if r.get("logtype") == "move":
                target = (r.get("logparams") or {}).get("target_title")
                if target and ns_of(target) in KEEP_NS:
                    pages.add(target)
                continue
            continue
        if r.get("ns") == 6:
            files.add(t)   # file description edit: re-check the file too (cheap if unchanged)
        if r.get("ns") in KEEP_NS:
            pages.add(t)
    return pages, files


KEEP_NS = (0, 4, 8, 10, 12, 14, 3000)  # the namespaces tools/dump_live.py backs up


# ---------------------------------------------------------------- pages

def backup_pages(repo: Path, titles: set[str]) -> int:
    sys.path.insert(0, str(repo / "tools"))
    import dump_live as dl  # the repo's own dumper: same file layout as every other backup
    keep = sorted(titles)
    if not keep:
        return 0

    def write() -> list[str]:
        existing = dl.index_existing()
        idx = {}
        if dl.INDEX.exists():
            for line in dl.INDEX.read_text(encoding="utf-8").splitlines():
                if "\t" in line:
                    a, b = line.split("\t", 1)
                    idx[a] = b
        tsv = repo / ".nightly-titles.tsv"
        tsv.write_text("".join(f"{t}\t{idx.get(t, '')}\n" for t in sorted(keep)), encoding="utf-8")
        written: list[tuple[str, str]] = []
        dl.dump_from_tsv(tsv, existing, written)   # deleted pages come back "missing": skipped, old copy kept
        tsv.unlink()
        dl.write_index(dl._merge_index(written, keep_old=True))
        return sorted({rel for _, rel in written} | {"pages/INDEX.tsv"})

    paths = write()
    n = len(paths) - 1
    commit_and_push(repo, paths, f"nightly backup: {n} pages from wiki.swccg.com", write)
    return n


_NS: dict[str, int] | None = None


def ns_of(title: str) -> int:
    """Namespace id of a title, from the wiki's own namespace names."""
    global _NS
    if _NS is None:
        d = api({"action": "query", "meta": "siteinfo", "siprop": "namespaces|namespacealiases"})
        _NS = {v["name"]: int(v["id"]) for v in d["query"]["namespaces"].values() if v.get("name")}
        _NS.update({v["alias"]: int(v["id"]) for v in d["query"].get("namespacealiases", [])})
    pre = title.split(":", 1)[0] if ":" in title else ""
    return _NS.get(pre, 0)


# ---------------------------------------------------------------- files

def safe_name(title: str) -> str:
    name = title.replace(" ", "_").replace(":", "_").replace("/", "_")
    for ch in '?*"<>|':
        name = name.replace(ch, "")
    return name


def backup_files(repo: Path, titles: set[str]) -> int:
    names = sorted({t.split(":", 1)[1] for t in titles if ":" in t})
    info: dict[str, dict] = {}
    for i in range(0, len(names), 50):
        chunk = names[i:i + 50]
        d = api({"action": "query", "titles": "|".join("File:" + n for n in chunk),
                 "prop": "imageinfo|fileusage", "iiprop": "url|size|mime|sha1", "fulimit": "max"})
        for p in d["query"].get("pages", []):
            if p.get("missing") or not p.get("imageinfo"):
                continue
            info[p["title"].split(":", 1)[1]] = p
    if not info:
        return 0
    blobs: dict[str, bytes] = {}
    for nm, p in info.items():
        ii = p["imageinfo"][0]
        req = urllib.request.Request(ii["url"], headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=300) as r:
            data = r.read()
        if hashlib.sha1(data).hexdigest() != ii["sha1"]:
            print("SKIP sha1 mismatch", nm)
            continue
        blobs[nm] = data

    def write() -> list[str]:
        fdir = repo / "files"
        idx_p, use_p = fdir / "INDEX.tsv", fdir / "USAGE.tsv"
        idx = idx_p.read_text(encoding="utf-8").splitlines() if idx_p.exists() else []
        use = use_p.read_text(encoding="utf-8").splitlines() if use_p.exists() else []
        have = {l.split("\t")[0] for l in idx}
        paths = ["files/INDEX.tsv", "files/USAGE.tsv"]
        for nm, data in blobs.items():
            ii = info[nm]["imageinfo"][0]
            (fdir / safe_name(nm)).write_bytes(data)
            paths.append("files/" + safe_name(nm))
            if nm not in have:
                idx.append(f"{nm}\t{safe_name(nm)}\t{ii.get('mime', '')}\t{ii.get('size', '')}")
            for u in info[nm].get("fileusage", []):
                use.append(f"{nm}\t{u['title']}")
        idx_p.write_text("\n".join(sorted(set(idx))) + "\n", encoding="utf-8")
        use_p.write_text("\n".join(sorted(set(use))) + "\n", encoding="utf-8")
        return paths

    paths = write()
    commit_and_push(repo, paths, f"nightly backup: {len(blobs)} files from wiki.swccg.com", write)
    return len(blobs)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pages_repo", type=Path)
    ap.add_argument("files_repo", type=Path)
    ap.add_argument("--state", type=Path, default=Path("/var/lib/swccg-ops/backup-state.json"))
    ap.add_argument("--since")
    a = ap.parse_args()
    started = datetime.now(timezone.utc).replace(microsecond=0)
    state = json.loads(a.state.read_text()) if a.state.exists() else {}
    since = a.since or state.get("last") or (started - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    pages, files = changed_since(since)
    print(f"since {since}: {len(pages)} pages, {len(files)} files changed")
    for repo in (a.pages_repo, a.files_repo):
        reset_to_origin(repo)
    np_ = backup_pages(a.pages_repo.resolve(), pages)
    nf = backup_files(a.files_repo.resolve(), files)
    a.state.parent.mkdir(parents=True, exist_ok=True)
    a.state.write_text(json.dumps({"last": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
                                   "pages": np_, "files": nf}) + "\n")
    print(f"backed up {np_} pages, {nf} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
