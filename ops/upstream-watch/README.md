# GEMP upstream watch (VPS)
Lives at `/opt/swccg-wiki/ops/upstream-watch/` on gemp: `upstream_watch.py`, `ledger.json` (last SHAs + card-text
hashes), `run-weekly.sh` (diff → post `GEMP upstream watch/YYYY-MM-DD` + hub line → update ledger).
Weekly crontab line (Bill installs): `15 7 * * 1 /opt/swccg-wiki/ops/upstream-watch/run-weekly.sh >> /var/log/swccg-upstream-watch.log 2>&1`
Rules for acting on the report: ai-team-skills `shared/gemp-upstream-watch/SKILL.md`.
