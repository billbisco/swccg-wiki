# ops — unattended jobs on the wiki VPS

Both run on the VPS (`gemp`) from `/opt/swccg-ops/repos/swccg-wiki/ops`, under systemd timers
(`systemctl list-timers 'swccg-*'`). They push with per-repo GitHub deploy keys in
`/opt/swccg-ops/keys/` (write access to one repo each; revoke under the repo's
Settings → Deploy keys). Logs: `journalctl -u swccg-wayback` / `journalctl -u swccg-backup`.

| Job | Timer | What it does |
| --- | --- | --- |
| `wayback_worker.py` | every 15 min, ≤10 min per run | Saves URLs from `wayback/queue.txt` to archive.org one at a time, confirms captures, records them in `wayback/done.json`. |
| `nightly_backup.py` | 07:15 UTC daily | Backs up every page edited/created/moved and every file uploaded since the last run (anyone's edits) to `swccg-wiki` `pages/` and `swccg-wiki-files` `files/`. Never deletes old copies. |

Setup/repair: `ops/install-vps.sh` (idempotent; run as root on the VPS).
