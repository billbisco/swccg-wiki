# Unified login (V1 piece 3b) — wiki side runbook

**Status: prepared, NOT deployed.** Every step below that touches the VPS needs Bill's go-ahead.
Owner: Alpha4 (wiki side). GEMP endpoint: same PR family in `billbisco/swccg-gemp`. Email delivery
(`$wgSMTP`, Brevo/SES) belongs to Primary Bot and is not touched here.

Contract: [`docs/wiki-auth-api.md`](../../docs/wiki-auth-api.md). Plan: `/workspace/reports/swccg-security-login-assessment.md` ("Approved login plan").

## What ships

| File (repo `ops/wiki-config/`) | Lands at (VPS) | Does |
|---|---|---|
| `extensions/GempAuth/` | `/opt/swccg-wiki/extensions/GempAuth` (ro mount → `$IP/extensions/GempAuth`) | AuthManager primary provider (GEMP login, auto-create, link), email-to-edit permission hook, password-reset block for GEMP accounts, `linkGempAccount.php` |
| `login-security.php` | `/opt/swccg-wiki/login-security.php` (ro mount) | Levels 2–4 config, anti-spam, rate limits, real client IP |
| `LocalSettings.unified-login.patch` | `/opt/swccg-wiki/LocalSettings.php` | one `require_once` after `extra-settings.php` |
| `docker-compose.unified-login.yml` | `/opt/swccg-wiki/` | mounts + `swccg-auth` network + `GEMP_AUTH_ENDPOINT` |
| `nginx-wiki-realip.patch` | `/etc/nginx/sites-enabled/wiki.swccg.com` | `X-Forwarded-For $remote_addr`; POST burst limit on account pages |
| `dev-mail-logonly.php` | **staging only** | captures outgoing mail (SES not live yet) |
| (untracked) `secrets/gempauth-secret.php` | `/opt/swccg-wiki/secrets/` mode 0640 | `$wgGempAuthSecret = '…';` |

## Behaviour after deploy

- **Login:** GEMP name + password on Special:UserLogin. First login auto-creates the wiki user (`autocreateaccount`), links it to the GEMP id. Wiki signup is closed (`*` `createaccount` = false); sysops can still create local accounts.
- **Local accounts keep working** and never touch GEMP: Admin, Holocron Claude, Datacard Grok, Comlink Cursor, Abuse filter.
- **Editing:** content namespaces (Main, Card, Template, Help, Category, File, Project) need `editcontent`, granted by the implicit group `emailconfirmed` (APCOND_EMAILCONFIRMED) and to sysop/bot/editor. Talk pages, user pages and user talk stay open to any logged-in user. FlaggedRevs review is unchanged.
  - **Until SES works, nobody new can confirm an email**, so new GEMP users can talk but not edit content. Existing editors are unaffected only if they are in `editor`/`bot`/`sysop` or already have a confirmed email. Check before deploy: `SELECT user_name FROM user WHERE user_email_authenticated IS NULL AND user_editcount > 0;` and decide (Bill) whether to add those people to `editor` or wait.
- **2FA:** `$wgOATHRequiredForGroups = sysop, bureaucrat, interface-admin`. Members without 2FA **lose those groups' rights** until they enrol at Special:OATHManage. Only `Admin` is affected today (it holds all three). See "Admin 2FA order" below.
- **Anti-spam:** captcha after 3 bad logins per IP / 10 per account; `$wgPasswordAttemptThrottle` 5/5 min per IP+name, 50/day per name; `$wgAccountCreationThrottle` 5/h, 10/day per IP (covers auto-creation); `$wgRateLimits` for `mailpassword`, `confirmemail`, `changeemail`, `sendemail` (the 1.43 name of `emailuser`), `badcaptcha`, newbie `edit`/`create`. AbuseFilter, SpamBlacklist, TitleBlacklist stay as they are. GEMP adds 10 failures/15 min per account, 30/5 min per IP.
- **Real IPs:** `$wgCdnServersNoPurge = ['172.18.0.1']` (the `swccg-wiki_default` gateway, checked read-only). Without it every throttle above is site-wide. **Re-check the gateway if the wiki network is ever recreated** (`docker network inspect swccg-wiki_default`).

## Deploy order (each step needs Bill's OK)

0. Prerequisites: GEMP must-fix items 2–5 merged and live (Alpha3) — otherwise the wiki inherits the blank-password and SHA-256 issues. (GempAuth already refuses blank-password accounts.) MediaWiki upgrade (separate runbook) can go first.
1. **Backups**: `mysqldump --single-transaction` of `swccg_wiki_db` (and copy `/opt/swccg-wiki/*.php`, compose files, nginx vhost).
2. **Admin 2FA order**: enrolment needs OATHAuth loaded, and once `$wgOATHRequiredForGroups` is live, Admin has no sysop until enrolled. So in step 5 first deploy with `$wgOATHRequiredForGroups = [];`, let Bill enrol Admin at Special:OATHManage (keep the scratch codes offline), then restore the three groups and `apachectl graceful`. (If it is done in one go, Admin can still log in and enrol; it just has no admin rights for those minutes.)
3. **Network + secret**: `docker network create --internal swccg-auth`; generate the secret once (`openssl rand -base64 48`), write it to GEMP `.env` (`GEMP_INTERNAL_AUTH_SECRET`, `INTERNAL_AUTH_PORT=8090`) and to `/opt/swccg-wiki/secrets/gempauth-secret.php`. Never echo it to a terminal log or chat.
4. **GEMP**: deploy the endpoint build with `-f docker-compose.wiki-auth.yml`; check the log line `wiki-auth internal listener on port 8090`; confirm from the host that 8090 is **not** listening on any host address (`ss -ltn | grep 8090` → nothing).
5. **Wiki**: copy files, apply the LocalSettings patch, `docker compose ... -f docker-compose.unified-login.yml up -d wiki` (sessions are in DB, nobody is logged out), then `docker exec swccg_wiki php maintenance/run.php update --quick` (OATHAuth tables).
6. **nginx**: apply `nginx-wiki-realip.patch`, `nginx -t && systemctl reload nginx`.
7. **Smoke test** (staging first if possible, with `dev-mail-logonly.php`):
   - `python3 /opt/swccg-wiki/verify-admin-login.py` → `LOGIN_OK` (local account path).
   - Log in with a test GEMP account → wiki user auto-created; `linkGempAccount.php --user … ` shows the id.
   - As that user: edit a Talk page (works); edit a content page (blocked with the confirm-email message).
   - Wrong password 4× → captcha appears.
   - Check Special:RecentChanges / CheckUser-style IPs are real (Special:Log/newusers shows varied IPs; `docker logs` access lines still show 172.18.0.1 — Apache's own log is unaffected, MediaWiki is).
8. **Rollback**: remove the `require_once` line (or the compose override), `apachectl graceful`; GEMP: drop the override file / unset `INTERNAL_AUTH_PORT`. Auto-created users and links stay; harmless.

## Decisions for Bill

1. Staging: test on `test.swccg.com` GEMP (`gemp_swccg_app_2`) + a wiki copy before production? (Recommended.)
2. Editors without a confirmed email while SES is pending: add them to `editor`, or accept that they cannot edit content until mail works?
3. Leave `$wgEnableUserEmail = true` (user-to-user email, rate-limited now) or turn it off as the assessment suggests? Not changed here because it touches email behaviour.
4. Captcha: keep QuestyCaptcha (answer is in the question) for the bad-login trigger, or add hCaptcha/Turnstile (needs a site key Bill creates)?
5. Remember-me is 180 days for everyone including admins; shorten for admins? (Not changed.)
6. Restrict OATH to sysop/bureaucrat/interface-admin only (as shipped), or also `editor` reviewers?
