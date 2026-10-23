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
  - **Until SES works, nobody new can confirm an email**, so new GEMP users can talk but not edit content. Existing editors are unaffected only if they are in `editor`/`bot`/`sysop`/`confirmed-editor` or already have a confirmed email.
  - **Decided (Bill, 2026-10-19):** existing editors without a confirmed email go into `confirmed-editor`, a group that grants **only** `editcontent` (FlaggedRevs' `editor` would also grant review rights). Sysops can add/remove it at Special:UserRights. The script selects exactly the runbook query `SELECT user_name FROM user WHERE user_email_authenticated IS NULL AND user_editcount > 0;`, skips system users and anyone who already has `editcontent`, and writes a normal rights-log entry:
    ```
    docker exec swccg_wiki php maintenance/run.php ./extensions/GempAuth/maintenance/grantConfirmedEditor.php --dry-run
    docker exec swccg_wiki php maintenance/run.php ./extensions/GempAuth/maintenance/grantConfirmedEditor.php
    ```
    Re-running is harmless (idempotent).
- **2FA (two phases, decided by Bill 2026-10-19):** OATHAuth is loaded with the requirement **off** (`$swccgRequireAdmin2FA = false;` in `login-security.php`). After Bill has enrolled, the requirement goes on: `$wgOATHRequiredForGroups = sysop, bureaucrat, interface-admin`, and members without 2FA **lose those groups' rights** until they enrol at Special:OATHManage. Only `Admin` holds them today. See "Admin 2FA" below.
- **Anti-spam:** captcha after 3 bad logins per IP / 10 per account; `$wgPasswordAttemptThrottle` 5/5 min per IP+name, 50/day per name; `$wgAccountCreationThrottle` 5/h, 10/day per IP (covers auto-creation); `$wgRateLimits` for `mailpassword`, `confirmemail`, `changeemail`, `sendemail` (the 1.43 name of `emailuser`), `badcaptcha`, newbie `edit`/`create`. AbuseFilter, SpamBlacklist, TitleBlacklist stay as they are. GEMP adds 10 failures/15 min per account, 30/5 min per IP.
- **Real IPs:** `$wgCdnServersNoPurge = ['172.18.0.1']` (the `swccg-wiki_default` gateway, checked read-only). Without it every throttle above is site-wide. **Re-check the gateway if the wiki network is ever recreated** (`docker network inspect swccg-wiki_default`).

## Deploy order (each step needs Bill's OK)

0. Prerequisites: GEMP #284–#286 are merged into master; swccg-gemp PR #287 is now based on master. Deploy #284's `update_password_hashing.sql` migration before or with #287. The GEMP endpoint calls `AuthService.verifyCredentials`, so blank stored hashes never verify and reset codes return `reset_required`, never a login. MediaWiki 1.43.11 upgrade (separate runbook) can go first. **Backups are Alpha3's:** get a fresh backup path + sha256 from Alpha3 and agree the window so the nightly backup does not overlap.
1. **Backups**: `mysqldump --single-transaction` of `swccg_wiki_db` (and copy `/opt/swccg-wiki/*.php`, compose files, nginx vhost).
2. **Admin 2FA**: deployed in phase 1 (requirement off). Bill enrols (see "Admin 2FA" below), then the phase 2 flip is a separate, explicit step.
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

## Admin 2FA

**Phase 1 (shipped):** `wfLoadExtension( 'OATHAuth' )` and `$swccgRequireAdmin2FA = false;`. Nobody loses rights.

**Bill's enrolment** (on staging first, then again on production after the production deploy; the two are separate accounts/databases):
1. Install a TOTP authenticator app on your phone: Aegis (Android), Raivo or 2FAS (iOS), Google Authenticator or Microsoft Authenticator (either), or the TOTP field of 1Password/Bitwarden. Any RFC 6238 app works (6 digits, 30 s).
2. Log in as **Admin** at `https://test.swccg.com/wiki/Special:UserLogin` (production later: `https://wiki.swccg.com/wiki/Special:UserLogin`). Admin is a local wiki account, not a GEMP one: use its wiki password.
3. Open `https://test.swccg.com/wiki/Special:OATHManage` (production: `https://wiki.swccg.com/wiki/Special:OATHManage`). If asked to re-enter the password (security re-check), do so.
4. Click **Enable** next to "Time-based one-time password (TOTP)".
5. Scan the QR code with the app (or type the shown secret key manually, type "time-based"). The account shows as "SWCCG Wiki (staging):Admin" or "SWCCG Wiki:Admin".
6. **Scratch codes:** the page lists 10 one-time recovery codes. Write them on paper or save them in your password manager **before** continuing; they are shown only once. Each works once instead of an app code if the phone is lost.
7. Type the current 6-digit code from the app into "Enter a verification code" and click **Continue**. The page now says two-factor authentication is enabled.
8. **Confirm:** log out, log in again as Admin: after the password, the wiki asks for a "Verification code"; enter the app code. `Special:OATHManage` shows TOTP as enabled with a **Disable** button. Tell the operator "Admin 2FA enrolled on <staging|production>".

**Phase 2 (only after Bill confirms step 8), the exact flip:**
```
# staging
F=/opt/swccg-wiki-staging/wiki-config/login-security.php C=swccg_wiki_staging
# production (after the production deploy):  F=/opt/swccg-wiki/login-security.php C=swccg_wiki
sudo cp -a "$F" "$F.bak-2fa-$(date +%F)" \
  && sudo sh -c 'sed "s/^\$swccgRequireAdmin2FA = false;\$/\$swccgRequireAdmin2FA = true;/" "$1" > "$1.new" && cat "$1.new" > "$1" && rm "$1.new"' _ "$F" \
  && grep -n '^\$swccgRequireAdmin2FA' "$F" \
  && docker exec "$C" apachectl -k graceful \
  && docker exec "$C" php maintenance/run.php getConfiguration --settings=wgOATHRequiredForGroups --format=json
```
Do **not** use `sed -i`: it replaces the file, and a single-file bind mount keeps showing the old file to the container. `cat new > file` rewrites it in place (same inode); the `.bak` copy is the safety net. `grep` must print `$swccgRequireAdmin2FA = true;` and the last command `{"wgOATHRequiredForGroups":["sysop","bureaucrat","interface-admin"]}` (phase 1 prints `[]`). Then Admin (enrolled) still has its rights; check Special:UserRights/Admin and that Special:Block loads. Commit the same one-line change in git (the PHPUnit test `testPhase2FlipLineIsExactlyAsDocumented` guards that the `false` line exists exactly once before the flip).
**Undo phase 2:** `sudo sh -c 'cat "$1" > "$2"' _ "$F.bak-2fa-<date>" "$F" && docker exec "$C" apachectl -k graceful` (in place, same reason as above).

## Staging (test.swccg.com)

Approved by Bill 2026-10-19: wiki staging on `test.swccg.com` only. Files in `staging/` (`STAGING.md`, compose, settings, nginx snippet, deploy/rollback scripts). Isolated from production: own wiki DB server and volume, own (empty) images volume, own copies of chrome and settings, own GEMP auth listener + GEMP DB. Production is only read (file copies + a `--single-transaction` dump).

## Future work

- **Email sending (SES), when it is built:** the change must subscribe to the SES **bounce and complaint SNS topics** and disable email on matching wiki user accounts (unset `user_email_authenticated` / turn off email for that address). This is a commitment made to AWS for SES production access; do not enable real sending without it. `dev-mail-logonly.php` stays the mailer until then.

## Decisions for Bill

1. ~~Staging~~ decided: test.swccg.com only (see "Staging").
2. ~~Editors without a confirmed email~~ decided: `confirmed-editor` group (see "Editing").
3. Leave `$wgEnableUserEmail = true` (user-to-user email, rate-limited now) or turn it off as the assessment suggests? Not changed here because it touches email behaviour.
4. Captcha: keep QuestyCaptcha (answer is in the question) for the bad-login trigger, or add hCaptcha/Turnstile (needs a site key Bill creates)?
5. Remember-me is 180 days for everyone including admins; shorten for admins? (Not changed.)
6. Restrict OATH to sysop/bureaucrat/interface-admin only (as shipped), or also `editor` reviewers?
