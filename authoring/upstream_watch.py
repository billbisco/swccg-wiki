#!/usr/bin/env python3
"""GEMP upstream watch: diff the Players Committee's public repos against our ledger and write a report.

    python3 upstream_watch.py <ledger.json> <report.wiki> [--update]

Sources (public, unauthenticated): PlayersCommittee/gemp-swccg-public commits + releases, swccgpc/swccg-card-json
Dark/Light(.json|Legacy.json) card text. See ai-team-skills shared/gemp-upstream-watch/SKILL.md for what to do
with each class of change. --update writes the new SHAs/hashes back to the ledger (do this after the report
is posted and the items are filed).
"""
from __future__ import annotations
import hashlib, json, sys, urllib.request, datetime
from pathlib import Path

GH = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
UA = {"User-Agent": "swccg-upstream-watch/1.0 (billbisco)"}


def get(url, binary=False):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)
    return r.read() if binary else json.loads(r.read().decode("utf-8"))


def gh_commits(repo, since_sha, branch):
    out = []
    page = 1
    while True:
        d = get(f"{GH}/repos/{repo}/commits?sha={branch}&per_page=100&page={page}")
        for c in d:
            if c["sha"] == since_sha:
                return out
            out.append({"sha": c["sha"][:10], "date": c["commit"]["author"]["date"][:10], "msg": c["commit"]["message"].splitlines()[0][:140]})
        if len(d) < 100 or page > 10:
            return out
        page += 1


def card_text_hashes(repo="swccgpc/swccg-card-json", branch="main"):
    h, titles = {}, {}
    for f in ("Dark.json", "Light.json", "DarkLegacy.json", "LightLegacy.json"):
        d = get(f"{RAW}/{repo}/{branch}/{f}")
        for c in d.get("cards", d if isinstance(d, list) else []):
            gid = c.get("gempId")
            if not gid:
                continue
            fr = c.get("front", {})
            key = json.dumps({k: fr.get(k) for k in ("gametext", "power", "ability", "deploy", "forfeit", "destiny", "armor", "maneuver", "hyperspeed", "icons", "lore")}, sort_keys=True)
            h[gid] = hashlib.sha1(key.encode()).hexdigest()[:12]
            titles[gid] = fr.get("title", "")
    return h, titles


def main():
    ledger_p, report_p = Path(sys.argv[1]), Path(sys.argv[2])
    update = "--update" in sys.argv
    L = json.loads(ledger_p.read_text(encoding="utf-8"))
    today = datetime.date.today().isoformat()
    lines = [f"== Upstream watch {today} ==", ""]
    # 1. engine repo
    repo = "PlayersCommittee/gemp-swccg-public"
    info = get(f"{GH}/repos/{repo}")
    branch = info.get("default_branch", "master")
    head = get(f"{GH}/repos/{repo}/commits/{branch}")["sha"]
    rels = get(f"{GH}/repos/{repo}/releases?per_page=5")
    last_tag = rels[0]["tag_name"] if rels else None
    commits = gh_commits(repo, L[repo.split('/')[1]]["last_sha"], branch) if L[repo.split('/')[1]]["last_sha"] else []
    lines.append(f"=== {repo} ===")
    lines.append(f"Branch {branch} head {head[:10]}; latest release {last_tag or '—'}" + (f" ({rels[0]['published_at'][:10]})" if rels else ""))
    if commits:
        lines.append(f"{len(commits)} new commits since last check:")
        for c in commits:
            lines += [f"* {c['date']} {c['sha']} — {c['msg']}"]
    else:
        lines.append("No new commits (or first run — baseline recorded)." if update else "No new commits.")
    # 2. card text
    hashes, titles = card_text_hashes()
    old = L["swccg-card-json"]["text_hashes"]
    changed = [g for g in hashes if g in old and old[g] != hashes[g]]
    new = [g for g in hashes if g not in old]
    gone = [g for g in old if g not in hashes]
    lines += ["", "=== swccgpc/swccg-card-json ==="]
    if old:
        lines.append(f"Changed card text/stats: {len(changed)}; new cards: {len(new)}; removed: {len(gone)}")
        for g in changed[:200]:
            lines.append(f"* CHANGED {g} {titles.get(g, '')} → new dated state (old text becomes o<n>)")
        for g in new[:200]:
            lines.append(f"* NEW {g} {titles.get(g, '')}")
        for g in gone[:50]:
            lines.append(f"* REMOVED {g} — ids are append-only here; flag")
    else:
        lines.append(f"Baseline recorded: {len(hashes)} cards.")
    report_p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12]))
    if update:
        L["gemp-swccg-public"] = {"last_sha": head, "last_tag": last_tag}
        L["swccg-card-json"]["text_hashes"] = hashes
        L["swccg-card-json"]["checked"] = today
        ledger_p.write_text(json.dumps(L, indent=0), encoding="utf-8")


if __name__ == "__main__":
    main()
