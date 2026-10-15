#!/usr/bin/env python3
"""Run a list of wiki operations as Holocron Claude, safely re-runnable in time-boxed chunks.

    python3 wiki_api_ops.py ops.jsonl [--summary "..."] [--budget 160]

ops.jsonl, one JSON object per line, applied in order:
    {"op": "move", "from": "Jawa", "to": "Jawa (Light) (Premiere)"}
    {"op": "edit", "title": "Jawa", "file": "pages/Jawa.wiki"}
    {"op": "purge", "titles": ["A", "B"]}

A move is skipped when it is already done (source is a redirect to the target, or the target exists and the
source does not). An edit with unchanged text is a no-op. Progress is written to <ops>.done (line numbers), so a
call that hits the time budget resumes where it stopped. Credentials: WIKI_BOT_USER / WIKI_BOT_PASS, as
wiki_api_apply.py.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki_api_apply import Wiki as _Wiki  # noqa: E402
import urllib.error  # noqa: E402


class Wiki(_Wiki):
    """Short request timeout: a hung request costs 30 s, not the whole time-boxed call."""

    def _open(self, req, tries: int = 4) -> dict:
        for i in range(tries):
            try:
                with self.op.open(req, timeout=30) as r:
                    d = json.loads(r.read().decode("utf-8"))
                if d.get("error", {}).get("code") == "maxlag":
                    time.sleep(5 * (i + 1))
                    continue
                return d
            except (urllib.error.URLError, TimeoutError, OSError):
                if i == tries - 1:
                    raise
                time.sleep(3 * (i + 1))
        raise RuntimeError("API retries exhausted")


def page_info(w: Wiki, title: str) -> dict:
    p = w.get(action="query", titles=title, prop="info|revisions", rvprop="content", rvslots="main")["query"]["pages"][0]
    if p.get("missing"):
        return {"missing": True}
    text = p["revisions"][0]["slots"]["main"]["content"]
    return {"missing": False, "redirect": p.get("redirect", False), "text": text}


def do_move(w: Wiki, src: str, dst: str, reason: str) -> str:
    s, d = page_info(w, src), page_info(w, dst)
    if not d["missing"] and (s["missing"] or (s.get("redirect") and f"[[{dst}]]" in s["text"])):
        return "already"
    if s["missing"]:
        return "ERROR source missing"
    if not d["missing"] and not d.get("redirect"):
        return "ERROR target exists"
    for wait in (0, 20, 40, 60):
        time.sleep(wait)
        r = w.post(action="move", **{"from": src}, to=dst, reason=reason, movetalk="1", ignorewarnings="1",
                   token=w.csrf)
        if r.get("error", {}).get("code") != "ratelimited":
            break
    if "error" in r:
        return f"ERROR {r['error'].get('code')}: {r['error'].get('info', '')[:120]}"
    return "moved" + w.review(dst)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ops", type=Path)
    ap.add_argument("--summary", default="Disambiguation rollout (Holocron Claude)")
    ap.add_argument("--budget", type=float, default=160.0, help="seconds before stopping cleanly")
    ap.add_argument("--pause", type=float, default=1.0, help="seconds between operations (spare the server)")
    a = ap.parse_args()
    start = time.time()
    done_f = a.ops.with_suffix(a.ops.suffix + ".done")
    done = set(int(x) for x in done_f.read_text().split()) if done_f.exists() else set()
    lines = [l for l in a.ops.read_text(encoding="utf-8").splitlines()]
    w = Wiki()
    errors = 0
    for i, line in enumerate(lines):
        if i in done or not line.strip():
            continue
        if time.time() - start > a.budget:
            print(f"BUDGET stop at op {i}/{len(lines)}")
            break
        op = json.loads(line)
        time.sleep(a.pause)
        try:
            res, label = run_op(w, op, a)
        except Exception as e:  # server trouble (502/timeouts): stop cleanly, resume next call
            print(f"SERVER ERROR at op {i}: {e}; stopping")
            break
        print(f"{label}: {res}")
        if res.startswith("ERROR"):
            errors += 1
        else:
            done.add(i)
            done_f.write_text(" ".join(map(str, sorted(done))))
    left = len([i for i, l in enumerate(lines) if l.strip() and i not in done])
    print(f"DONE errors {errors} remaining {left}")
    return 1 if errors else 0


def run_op(w: Wiki, op: dict, a) -> tuple[str, str]:
    if True:
        if op["op"] == "move":
            res = do_move(w, op["from"], op["to"], a.summary)
            label = f"MOVE {op['from']} -> {op['to']}"
        elif op["op"] == "edit":
            text = (a.ops.parent / op["file"]).read_text(encoding="utf-8")
            res = w.edit(op["title"], text, op.get("summary", a.summary))
            label = f"EDIT {op['title']}"
        elif op["op"] == "purge":
            w.purge(*op["titles"])
            res, label = "ok", f"PURGE {len(op['titles'])}"
        else:
            res, label = "ERROR unknown op", str(op)
        return res, label


if __name__ == "__main__":
    raise SystemExit(main())
