# #414 existing source-capture verification

Read-only verification completed for all 37 registered source targets, plus 37 distinct primary HTML citation contexts. Five existing source captures were fetched and checked; their exact payloads are retained locally. Three were already cited. Two new preserved-copy additions are ready: the Fall 2019 errata PDF and July 2022 errata PDF.

The exact verified mapping is `verified-citation-map.json`. It includes timestamped replay URLs, original/source URLs, actual bytes/hashes, verification method, existing-citation status and local fetched payloads. These are real replay checks, not ledger acceptance or a successful availability lookup. All five resolved on web.archive.org.

Thirty-two source targets remain unverified. Some CDX lookups returned no successful indexed capture; others became unavailable through connection refusals. The documented VPS read-only fallback was attempted. It discovered eight primary-page capture candidates, but replay connections were refused, so none of those candidates is approved for citation. Their separate file is explicitly labelled unverified.

The final single read-side probe received HTTP 429 and an explicit Wayback suspected-bot-traffic block. No further archive requests followed. There were no saves, staging changes, worker-control changes, account changes or attempts to bypass the stop. The parent's owner-health task separately found the existing central submission worker auth-blocked with HTTP 401. Those two external conditions prevent honest full preservation completion in this turn.

No active job remains from this source-verification subtask. Root owns article edits, durable evidence publication and the #414 handoff. Do not mark pending or merely discovered captures verified, and do not delete the backed source payloads.

Verified: 5; new citation additions: 2; remaining source targets: 32; unverified primary candidates: 8.
