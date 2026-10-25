# ops — unattended jobs on the wiki VPS

Both run on the VPS (`gemp`) from `/opt/swccg-ops/repos/swccg-wiki/ops`, under systemd timers
(`systemctl list-timers 'swccg-*'`). They push with per-repo GitHub deploy keys in
`/opt/swccg-ops/keys/` (write access to one repo each; revoke under the repo's
Settings → Deploy keys). Logs: `journalctl -u swccg-wayback` / `journalctl -u swccg-backup`.

| Job | Timer | What it does |
| --- | --- | --- |
| `wayback_worker.py` | systemd timer, one run at a time | Saves URLs from `wayback/queue.txt` to archive.org one at a time, confirms captures, then **verifies** each capture against its source (fetches the `id_` URL; sha256 for files, page text for HTML) and records `status: verified` + `capture` in `wayback/done.json`. Pending confirm polls at most 40 jobs whose `last` is within 2 hours (newest first) and stops that walk on connection refused / 429 so new submits still run. For verified `https://swccg.com/snapshots/…` URLs it **deletes** the staging file only when a main-namespace wiki article already cites a Wayback URL of that snapshot path (log: `DELETED-after-wayback.log`). |
| `nightly_backup.py` | 07:15 UTC daily | Backs up every page edited/created/moved and every file uploaded since the last run (anyone's edits) to `swccg-wiki` `pages/` and `swccg-wiki-files` `files/`. Never deletes old copies. |

Setup/repair: `ops/install-vps.sh` (idempotent; run as root on the VPS).

## Wayback queue: what a bot does (2026-10-20)

1. Add the live URL (or the swccg.com snapshot URL for Cloudflare hosts) to `wayback/queue.txt`, commit, push.
2. Read `wayback/done.json` on a later pull. `status: verified` means the worker fetched the capture's `id_` URL and it matched the source (`verify.method` `sha256` for files, `text` with `verify.text_match` for HTML). That counts as opened and checked: cite `capture` on the wiki article. For a `swccg.com/snapshots/` URL the worker deletes the VPS staging file only after a main-namespace article already cites that Wayback URL.
3. `unverified` has a `verify.reason` (Cloudflare page, file differs, text differs, source could not be fetched): look at it before citing. `ok` = loaded, not verified yet (the worker verifies these each run, newest first). `pending`/`retry`/`failed` as before. Do not delete unverified or uncaptured snapshot files.

No Wayback access is needed from the bot's own machine.

Rollback of the verify change: `/opt/swccg-backups/wayback-worker-<date>/rollback.sh` on the VPS (pins the previous worker with a systemd drop-in and maps verified/unverified back to ok), or revert the merge commit on GitHub.
