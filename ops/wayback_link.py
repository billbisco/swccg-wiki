#!/usr/bin/env python3
"""Add verified Wayback captures to the wiki pages that need them (Story swccg-guild/work#1320).

Runs after each normal `wayback_worker.py` run (and by hand). Reads only `status: verified`
entries of ops/wayback/done.json and edits as the Archive Droid bot account:

  (a) original upload  https://swccg.com/wiki/images/x/xy/<Name>
      -> File:<Name>, a line under "== Preservation ==".
  (b) forum post/thread snapshot  https://swccg.com/snapshots/forum/p<N>.html  (or t<N>.html)
      -> every main or File page whose external links cite viewtopic.php?...p=<N>
         (t<N>: cites of t=<N> with no p=). " Preserved copy: [<capture> Internet Archive]"
         goes inside that <ref> (before </ref>), or right after the link outside a ref,
         or replaces a "(Thread snapshot not yet archived ...)" placeholder.
  (c) ops/wayback/link-extra.json: other posts/threads a snapshot also holds.

Idempotent: a page that already carries a Wayback copy of the same original or snapshot is
skipped. Never raises into the worker: run_safe() catches everything.

Credentials: /root/.config/swccg-wayback/wiki-bot.env (WIKI_BOT_USER / WIKI_BOT_PASS),
root-only, never logged or committed.
"""
from __future__ import annotations

import argparse
import http.cookiejar
import json
import os
import re
import subprocess
import sys
import time
import traceback
import urllib.parse
import urllib.request
from pathlib import Path

API = os.environ.get("SWCCG_WIKI_API", "https://swccg.com/wiki/api.php")
ENV_FILE = Path(os.environ.get("SWCCG_LINK_ENV", "/root/.config/swccg-wayback/wiki-bot.env"))
STATE_FILE = Path(os.environ.get("SWCCG_LINK_STATE", "/root/.local/state/swccg-wayback/linker.json"))
DB_CONTAINER = os.environ.get("SWCCG_WIKI_DB_CONTAINER", "swccg_wiki_db")
DONE = "ops/wayback/done.json"
EXTRA = "ops/wayback/link-extra.json"
UA = "swccg-wayback-linker/1.0 (https://github.com/billbisco/swccg-wiki; Archive Droid)"
SUMMARY = "#1320: add verified Wayback copy"
PACE = float(os.environ.get("SWCCG_LINK_PACE", "0.5"))

IMAGE = re.compile(r"^https?://(?:www\.)?swccg\.com/wiki/images/[0-9a-f]/[0-9a-f]{2}/([^/?#]+)$")
FORUM_SNAP = re.compile(r"^https?://(?:www\.)?swccg\.com/snapshots/forum/([pt])(\d+)\.html$")
PLACEHOLDER = re.compile(r"\(Thread snapshot not yet archived[^)]*\)")
PRESERVATION_PENDING = "A Wayback copy of this upload is pending the central wiki-original preservation queue."
ORIGINAL_LINE = ("Wayback copy of this exact original (SHA-256 verified by the central preservation owner): "
                 "[%s Internet Archive].")
FORUM_SQL = """
SELECT p.page_namespace, p.page_title, CONCAT(e.el_to_domain_index, e.el_to_path)
FROM externallinks e JOIN page p ON p.page_id = e.el_from
WHERE p.page_namespace IN (0, 6)
  AND e.el_to_domain_index LIKE '%starwarsccg.%'
  AND e.el_to_path LIKE '%viewtopic%'
"""


# ---------------------------------------------------------------- pure helpers (tested)

def file_title(original: str) -> str | None:
    m = IMAGE.match(original)
    if not m:
        return None
    return "File:" + urllib.parse.unquote(m.group(1)).replace("_", " ")


def forum_key(url: str) -> tuple[str, str] | None:
    """('p', '123') for a post link, ('t', '45') for a thread link with no p=; else None."""
    if "viewtopic" not in url:
        return None
    query = url.split("?", 1)[1] if "?" in url else ""
    q = urllib.parse.parse_qs(query.split("#", 1)[0])
    if q.get("p") and q["p"][0].isdigit():
        return ("p", q["p"][0])
    if q.get("t") and q["t"][0].isdigit():
        return ("t", q["t"][0])
    return None


def page_name(ns: int, title: str) -> str:
    t = title.replace("_", " ")
    return "File:" + t if int(ns) == 6 else t


def snapshot_keys(snap: str, extra: dict) -> list[tuple[str, str]]:
    m = FORUM_SNAP.match(snap)
    keys = [(m.group(1), m.group(2))] if m else []
    e = extra.get(snap) or {}
    keys += [("p", str(p)) for p in e.get("posts", [])]
    keys += [("t", str(t)) for t in e.get("topics", [])]
    return keys


def live_link_re(kind: str, num: str) -> re.Pattern:
    """A starwarsccg.org forum viewtopic URL citing post p=<num> (or thread t=<num>, no p=)."""
    base = r"https?://(?:forum\.|www\.)?starwarsccg\.org/(?:forum/)?viewtopic\.php\?[^\s\]|<}]*"
    if kind == "p":
        return re.compile(base + r"(?<![\w])p=" + num + r"(?!\d)[^\s\]|<}]*")
    return re.compile(r"https?://(?:forum\.|www\.)?starwarsccg\.org/(?:forum/)?viewtopic\.php\?"
                      r"(?:(?!p=)[^\s\]|<}])*(?<![\w])t=" + num + r"(?!\d)(?:(?!p=)[^\s\]|<}])*(?=[\s\]|<}]|$)")


def has_capture_of(text: str, original: str) -> bool:
    """True if text already links any Wayback capture of this original URL."""
    tail = re.sub(r"^https?://(?:www\.)?", "", original)
    variants = {tail, urllib.parse.unquote(tail), urllib.parse.quote(urllib.parse.unquote(tail), safe="/:")}
    for v in variants:
        if re.search(r"web\.archive\.org/web/\d{14}[a-z_]*/(?:https?://)?(?:www\.)?" + re.escape(v), text):
            return True
    return False


def add_original_line(text: str, capture: str, original: str) -> str | None:
    """File page: add the Preservation line. None = already there."""
    if capture in text or has_capture_of(text, original):
        return None
    line = ORIGINAL_LINE % capture
    if PRESERVATION_PENDING in text:
        return text.replace(PRESERVATION_PENDING, line, 1)
    if "== Preservation ==" in text:
        return text.replace("== Preservation ==", "== Preservation ==\n" + line, 1)
    m = re.search(r"\n(\[\[Category:)", text)
    if m:
        return text[:m.start()] + "\n== Preservation ==\n" + line + "\n" + text[m.start():]
    return text.rstrip() + "\n\n== Preservation ==\n" + line + "\n"


def _ref_span(text: str, pos: int) -> tuple[int, int] | None:
    """(start of ref content, index of </ref>) if pos sits inside <ref ...>...</ref>."""
    start = text.rfind("<ref", 0, pos)
    if start < 0:
        return None
    gt = text.find(">", start)
    if gt < 0 or gt > pos or text[gt - 1] == "/":
        return None
    close_before = text.rfind("</ref>", start, pos)
    if close_before >= 0:
        return None
    end = text.find("</ref>", pos)
    return (gt + 1, end) if end >= 0 else None


def _link_end(text: str, m: re.Match) -> int:
    """End of the external link containing the match: after ']' if bracketed, else after URL."""
    open_b = text.rfind("[", 0, m.start())
    if open_b >= 0 and open_b == m.start() - 1:
        close_b = text.find("]", m.end())
        nl = text.find("\n", m.end())
        if close_b >= 0 and (nl < 0 or close_b < nl):
            return close_b + 1
    return m.end()


def _sep(before: str) -> str:
    """House style: '... source. Preserved copy: [...]'."""
    return " " if before.endswith((".", "!", "?")) or not before else ". "


def add_preserved_copy(text: str, keys: list[tuple[str, str]], capture: str, snap: str) -> tuple[str, int]:
    """Add the capture next to every cite of the keys that has no Wayback copy yet.
    Returns (new_text, number_of_places_changed)."""
    if capture in text or has_capture_of(text, snap):
        return text, 0
    pc = "Preserved copy: [%s Internet Archive]" % capture
    edits: list[tuple[int, int, str]] = []
    seen_spans: set[tuple[int, int]] = set()
    for kind, num in keys:
        for m in live_link_re(kind, num).finditer(text):
            span = _ref_span(text, m.start())
            if span:
                if span in seen_spans:
                    continue
                seen_spans.add(span)
                seg = text[span[0]:span[1]]
                if "web.archive.org" in seg:
                    continue
                ph = PLACEHOLDER.search(seg)
                if ph:
                    edits.append((span[0] + ph.start(), span[0] + ph.end(), pc))
                else:
                    body = seg.rstrip()
                    body_end = span[0] + len(body)
                    edits.append((body_end, body_end, _sep(body) + pc))
            else:
                end = _link_end(text, m)
                nl = text.find("\n", end)
                eol = nl if nl >= 0 else len(text)
                bol = text.rfind("\n", 0, m.start()) + 1
                line = text[bol:eol]
                table = line.lstrip().startswith(("|", "!")) or "||" in line
                # Table cell: right after the link. Other lines: end of line (house style).
                rest = text[end:eol]
                if "web.archive.org" in (rest if table else line):
                    continue
                ph = PLACEHOLDER.search(rest)
                if ph:
                    edits.append((end + ph.start(), end + ph.end(), pc))
                elif table:
                    edits.append((end, end, " " + pc))
                else:
                    stop = bol + len(line.rstrip())
                    edits.append((stop, stop, _sep(line.rstrip()) + pc))
    if not edits:
        return text, 0
    out = text
    for a, b, s in sorted(set(edits), reverse=True):
        out = out[:a] + s + out[b:]
    return out, len(set(edits))


def plan_jobs(done: dict, cites: dict, extra: dict) -> list[dict]:
    """Jobs from verified done.json entries. cites: {(kind, num): set(page names)}."""
    jobs = []
    for url, e in done.items():
        if e.get("status") != "verified" or not e.get("capture"):
            continue
        cap = e["capture"]
        t = file_title(url)
        if t:
            jobs.append({"kind": "original", "title": t, "url": url, "capture": cap})
            continue
        keys = snapshot_keys(url, extra)
        if not keys:
            continue
        pages = set()
        for k in keys:
            pages |= cites.get(k, set())
        for p in sorted(pages):
            jobs.append({"kind": "snapshot", "title": p, "url": url, "capture": cap, "keys": keys})
    return jobs


# ---------------------------------------------------------------- I/O

def forum_cites_from_db(run=subprocess.run) -> dict:
    proc = run(
        ["docker", "exec", "-i", DB_CONTAINER, "sh", "-c",
         'export MYSQL_PWD="$MYSQL_PASSWORD"; mysql -N -u"$MYSQL_USER" "$MYSQL_DATABASE"'],
        input=FORUM_SQL.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, check=False)
    if proc.returncode != 0:
        raise RuntimeError("forum cite query failed rc=%s" % proc.returncode)
    cites: dict = {}
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        k = forum_key(parts[2])
        if k:
            cites.setdefault(k, set()).add(page_name(int(parts[0]), parts[1]))
    return cites


class Wiki:
    def __init__(self, api: str = API):
        self.api = api
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        self.csrf = None

    def call(self, params: dict, post: bool = False) -> dict:
        params = dict(params, format="json", formatversion="2")
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(self.api if post else self.api + "?" + data.decode(),
                                     data=data if post else None, headers={"User-Agent": UA})
        with self.op.open(req, timeout=60) as r:
            return json.load(r)

    def login(self, env_file: Path = ENV_FILE) -> str:
        env = {}
        for line in env_file.read_text().splitlines():
            k, _, v = line.strip().partition("=")
            env[k] = v
        tok = self.call({"action": "query", "meta": "tokens", "type": "login"})["query"]["tokens"]["logintoken"]
        r = self.call({"action": "login", "lgname": env["WIKI_BOT_USER"], "lgpassword": env["WIKI_BOT_PASS"],
                       "lgtoken": tok}, post=True)["login"]
        if r.get("result") != "Success":
            raise RuntimeError("wiki login: %s" % r.get("result"))
        self.csrf = self.call({"action": "query", "meta": "tokens"})["query"]["tokens"]["csrftoken"]
        return r.get("lgusername", "")

    def page(self, title: str):
        p = self.call({"action": "query", "titles": title, "prop": "revisions",
                       "rvprop": "content|timestamp", "rvslots": "main", "curtimestamp": 1})
        cur = p.get("curtimestamp")
        pg = p["query"]["pages"][0]
        if pg.get("missing") or "revisions" not in pg:
            return None, None, cur
        rev = pg["revisions"][0]
        return rev["slots"]["main"]["content"], rev["timestamp"], cur

    def edit(self, title: str, text: str, base: str, start: str, summary: str) -> str:
        r = self.call({"action": "edit", "title": title, "text": text, "summary": summary, "bot": 1,
                       "nocreate": 1, "basetimestamp": base, "starttimestamp": start,
                       "token": self.csrf}, post=True)
        if "error" in r:
            return "error:" + r["error"].get("code", "?")
        return "edited" if r.get("edit", {}).get("result") == "Success" else "error:" + json.dumps(r)[:80]


def load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text())
    except (OSError, ValueError):
        return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, sort_keys=True))
    os.replace(tmp, STATE_FILE)


RETRY = {"error:editconflict", "error:ratelimited", "error:badtoken", "exception"}


def link(repo: Path, *, seconds: float = 90, limit: int = 200, dry_run: bool = False,
         only: set | None = None, wiki: Wiki | None = None, cites: dict | None = None) -> dict:
    t0 = time.time()
    done = json.loads((repo / DONE).read_text())
    extra_p = repo / EXTRA
    extra = json.loads(extra_p.read_text()) if extra_p.exists() else {}
    if cites is None:
        cites = forum_cites_from_db()
    state = load_state()
    jobs = plan_jobs(done, cites, extra)
    if only:
        jobs = [j for j in jobs if j["title"] in only]
    todo = [j for j in jobs if state.get(j["title"] + "|" + j["capture"]) in (None, *RETRY)]
    counts = {"jobs": len(jobs), "todo": len(todo), "edited": 0, "already": 0, "missing": 0,
              "no-anchor": 0, "error": 0, "dry": 0}
    print("WAYBACK-LINK plan", json.dumps({k: counts[k] for k in ("jobs", "todo")}), flush=True)
    if not todo:
        return counts
    if wiki is None:
        wiki = Wiki()
        if not dry_run:
            wiki.login()
    edits = 0
    for j in todo:
        if time.time() - t0 > seconds or edits >= limit:
            break
        key = j["title"] + "|" + j["capture"]
        try:
            text, base, start = wiki.page(j["title"])
            if text is None:
                res = "missing"
            else:
                if j["kind"] == "original":
                    new = add_original_line(text, j["capture"], j["url"])
                    new = new if new is not None else text
                else:
                    new, _n = add_preserved_copy(text, j["keys"], j["capture"], j["url"])
                if new == text:
                    # Original: line already there. Snapshot: this capture is there, or every
                    # cite already carries some Wayback copy; no cite found = no-anchor.
                    found = j["kind"] == "original" or any(
                        live_link_re(k, n).search(text) for k, n in j["keys"])
                    res = "already" if found or has_capture_of(text, j["url"]) else "no-anchor"
                elif dry_run:
                    res = "dry"
                    print("WAYBACK-LINK dry", j["title"], j["capture"], flush=True)
                else:
                    res = wiki.edit(j["title"], new, base, start, SUMMARY)
                    edits += 1
                    print("WAYBACK-LINK", res, j["title"], flush=True)
                    time.sleep(PACE)
        except Exception as ex:  # one page never stops the run
            res = "exception"
            print("WAYBACK-LINK-ERR", j["title"], type(ex).__name__, str(ex)[:120], flush=True)
        counts[res if res in counts else "error"] += 1
        if not dry_run:
            state[key] = res
    if not dry_run:
        save_state(state)
    print("WAYBACK-LINK done", json.dumps(counts, sort_keys=True), flush=True)
    return counts


def run_safe(repo: Path, **kw) -> None:
    """Called by wayback_worker.main(); never raises."""
    if not ENV_FILE.exists():
        print("WAYBACK-LINK skipped: no bot credential file", flush=True)
        return
    try:
        import fcntl
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(STATE_FILE.with_suffix(".lock"), "w") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                print("WAYBACK-LINK skipped: another linker is running", flush=True)
                return
            link(repo, **kw)
    except Exception as ex:
        print("WAYBACK-LINK-ERR", type(ex).__name__, str(ex)[:160], flush=True)
        traceback.print_exc(limit=3)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("repo", type=Path)
    ap.add_argument("--dry-run", action="store_true", help="print what would change; no edits, no state")
    ap.add_argument("--limit", type=int, default=200, help="max edits this run")
    ap.add_argument("--seconds", type=float, default=90)
    ap.add_argument("--only", action="append", help="limit to this page title (repeatable)")
    a = ap.parse_args()
    link(a.repo.resolve(), seconds=a.seconds, limit=a.limit, dry_run=a.dry_run,
         only=set(a.only) if a.only else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
