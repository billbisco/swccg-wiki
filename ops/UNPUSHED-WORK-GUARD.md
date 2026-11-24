# Unpushed local wiki-backup work guard

Refs swccg-guild/work#1323. This is a plain scheduled job, not an AI model.

## Why it exists

Same-sitting dumps on manpc used to leave work that never reached GitHub:

- `tools/dump_images.py` wrote files into the manpc `swccg-wiki-files` clone and did not commit or push.
- `tools/sync_delta.py` committed always, but pushed only when `--push` was passed.
- There was no job to report ahead commits or untracked files, or to copy them to a safety branch.

The nightly VPS job (`swccg-backup.timer`) and the nightly GitHub Action (`sync-from-live.yml`) are the source of truth. manpc clones are working copies, not an off-site backup.

## What the guard does

`ops/unpushed_work_guard.py` looks at known clones (or `UNPUSHED_GUARD_CLONES`). It:

- reports ahead / behind / untracked / dirty counts
- pushes already-made ahead commits to `safety/unpushed-YYYYMMDD-HHMMSS` (never to `main`, never force-push)
- commits untracked `files/` backup data on a new safety branch, pushes that branch, and returns to the original branch
- leaves dirty tracked files alone (Windows case-fold collisions must not be auto-committed)
- does nothing to a checkout already on a `safety/*` branch or holding a git lock (so an in-flight safety push is not interrupted)
- opens or comments on a `Unpushed local wiki backup work (auto)` issue in billbisco/swccg-wiki if unpushed work older than 24 hours remains

On manpc it is installed as the scheduled task `SWCCG Unpushed Wiki Backup Guard`, twice a day at 09:00 and 21:00 America/Caracas, by `ops/install-unpushed-guard-manpc.ps1`. Logs go to `C:\Users\gythe\.grok\swccg-ops\logs`.

## Same-sitting dumps

- Pages: `python tools/sync_delta.py --from-tsv <apply.tsv>` now pushes by default. Use `--no-push` only when the commit must stay local.
- Images: `python tools/dump_images.py --out <swccg-wiki-files>/files --merge --push`, or skip the local dump and leave new uploads to the nightly VPS job.
