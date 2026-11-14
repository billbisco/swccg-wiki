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

## Persistent preservation owner and failures (Story #407)

All producers add approved public URLs to the existing queue. They do not run
independent Save Page Now fallbacks on their own PCs or accounts. The worker
holds an OS advisory lock for its full run and keeps its circuit, acknowledged-job
journal and health outside the Git working tree. Git resets cannot erase a pause.

The default control directory is `~/.local/state/swccg-wayback`, for the operating
system account running the existing service. `WAYBACK_CONTROL_DIR` can point to
an explicitly coordinated directory. Every instance must use the same account
and directory. A filesystem lock does **not** coordinate other hosts, users, or
programs that ignore this owner; those clients must enqueue work here.

* A rejected credential pauses authenticated submissions; the worker never
  automatically retries anonymously. Subsequent timer starts make no Archive.org
  request with the same rejected credential. An authorized credential change
  allows one recovery canary. The opaque credential fingerprint stays only in
  the private control file, never health, Git, logs or reports.
* Provider throttling, service failures and transport errors open a persistent
  circuit. `Retry-After` is honored; otherwise the conservative starting pause is
  15 minutes, doubling on repeated failures up to 24 hours. These are local safety
  choices, not a claimed official Archive.org allowance. A later timer invocation
  exits without network work while the cooldown remains active.
* Recovery submits at most one canary, retaining its job identity across runs.
  A submission acknowledgment or HTTP200 cannot close the circuit; the existing
  strict replay/content verifier must mark that canary verified first. Source
  failures remain distinct from a provider/account failure.
* Accepted jobs and partial ledger updates are checkpointed atomically before
  waiting. After interruption they are reconciled against the fresh Git ledger.
  A different newer receipt causes a guarded stop, never an overwrite. Unknown
  request outcomes before an acknowledgment are still subject to SPN2's existing
  `if_not_archived_within` behavior; this does not claim transactional exactly-once
  delivery across an HTTP connection failure.

`control.json` and `pending-updates.json` are private runtime state, not repository
files. `health.json` exposes the actual mode, pause reason, next eligible attempt,
ledger counts, oldest pending activity and last newly verified progress.
`repair.json` records a deduplicated open/recovered incident, owning account and
repair issue407. Service exit0 is explicitly **not** proof of a new capture.
No new notification destination, systemd unit, credential or timer is installed.

Read health without contacting Git or Archive.org:

```sh
python3 ops/wayback_worker.py /path/to/job/repo --health
```

Do not delete the control directory to bypass throttling. A corrupt control or
conflicting pending-job journal fails closed and needs reconciliation. Capture
verification and the existing snapshot citation/age/delete checks are unchanged.
Content publication and independent backup may continue under the approved
publication policy while external preservation remains pending; a queue or a
healthy process is never a verified archive receipt.

Offline regressions run with fixture credentials and loopback-only sockets:

```sh
python3 ops/tests/run_offline.py --temp-root /path/to/isolated/test-temp
```

This lock protects the archive owner, not another service's Git index. The
installer historically points the nightly backup and archive jobs at the same
checkout; deployments must verify their working-copy isolation/coordination
separately. Do not infer that this change serializes unrelated backup writers.

Rollback of the verify change: `/opt/swccg-backups/wayback-worker-<date>/rollback.sh` on the VPS (pins the previous worker with a systemd drop-in and maps verified/unverified back to ok), or revert the merge commit on GitHub.
