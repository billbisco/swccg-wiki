# Story 414: fresh central-owner result

Read-only inspection on 14 November 2026. No save submissions, queue writes, staging, timer/service controls, credential changes, registry writes or Wiki edits were performed by this task.

## Actual current owner

- At 16:49:00 UTC, durable control and health reported `auth_blocked`, HTTP 401, `authentication rejected`.
- Latest real systemd invocation ran 16:48:27–16:48:28 UTC and returned success with health `outcome: paused`. The timer is active/waiting; the service is inactive with MainPID 0. A successful process exit does not mean a capture occurred.
- Last actual submission attempt remains 13:35:03.964539 UTC. `next_eligible_attempt_at` is null; no recovery canary is awaiting verification. Durable repair issue 407 remains open.
- No credential value or fingerprint was read into the report. The sanitized control/health/repair receipt is `fresh-owner-control.json`.

## Scoped registrations and queue

All 58 exact requested objects exist: 56 source/context mappings and two A Brave Resistance public original versions. There are 39 distinct source/original URLs, with 21 object rows ready and 37 awaiting stage. Thirty-three distinct URLs are in the existing legacy queue. Thirty-eight URLs have no existing owner-ledger entry; one metadata source has a byte-verified capture receipt.

The metadata receipt is sets.json, capture `https://web.archive.org/web/20261017142326/https://raw.githubusercontent.com/swccgpc/swccg-card-json/main/sets.json`, SHA256 `c0f16e65bbbc809a80e5dd2fe6a570344362664b582c3ffbe16d2e0c020501f5`, 15094 bytes. The separate existing-capture agent has this receipt and is comparing it to the retained source before reuse. It is not a new save or full Story 414 completion.

The six currently unqueued distinct URLs comprise the two ABR originals, the private demo snapshot target, the demo premium PDF, sets.json (already verified, do not blindly resubmit), and the old virtual-slips snapshot target. Source objects marked awaiting stage remain pending; registration does not prove a public stage or accepted capture job.

## Existing supported production entrypoint

At 16:51:53 UTC, the unit's actual ExecStart was `/usr/bin/python3 /opt/swccg-ops/repos/swccg-wiki/ops/wayback_worker.py /opt/swccg-ops/repos/swccg-wiki --minutes 12`. There is no outer staging/promoting wrapper. Inspection of deployed ops/tools code finds `promote_ready` only at its definition in `ops/preservation_registry.py`; `wayback_worker.py` does not import or call the registry. The library has an integration function requiring the existing owner's lock, public-byte checks, pinned approval checks and queue receipt callbacks, but no supported production staging/promotion caller was found.

A client calling that library and passing the string `server-wayback-owner` would not establish genuine owner coordination. This task did not do that, create a second saver, bulk-stage sources or append queue entries directly.

## Exact continuation

1. Resolve the existing Archive.org account-context dependency on [Bug 407](https://github.com/swccg-guild/work/issues/407), following its pending signed-in-account question and documented repair route. Do not reset/rotate keys, clear the circuit, retry anonymously or change hosts to evade the stop. A genuine confirmed repair must pass the existing single-canary strict replay verification before backlog submissions resume.
2. Complete the existing owner's registry staging/promotion integration through its tested/deployed change process. Keep the owner's global lock, stage budget, exact source restore/public-byte checks, existing-queue deduplication and pinned approval checks. No configuration or scheduler change is implied by Story 414's capture request.
3. Reconcile existing checked captures before queuing duplicates. The independent source/image capture agents own those bounded read-only checks now.
4. Once the real owner route is available, promote/submit the remaining exact Story 414 jobs through it and verify actual replays. Then root can add honest citation/File preservation links and close the original preservation AC.

No active job is owned by this diagnostic task. The existing systemd timer remains active/waiting and paused by its durable control. Other agents' existing-capture checks are independent active work, not capture submissions.
