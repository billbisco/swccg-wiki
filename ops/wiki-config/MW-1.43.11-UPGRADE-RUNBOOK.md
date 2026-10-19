# MediaWiki 1.43.9 → 1.43.10+ upgrade runbook (prepared, NOT run)

**Waits for Bill's go-ahead.** Finding M6: 1.43.9 lacks the 1.43.10 security release (11 CVEs, 2026-10-01).

## Target version: 1.43.11 (not 1.43.10)

Docker Hub never published a `mediawiki:1.43.10` image; the tags are `1.43.9` (2026-09-25) and then
`1.43.11` / `1.43` (2026-10-06). 1.43.11 contains all 1.43.10 security fixes plus maintenance fixes.
The tarball 1.43.10 exists at releases.wikimedia.org but the deployment uses the official image, so the
image path is **1.43.11**. (If Bill specifically wants 1.43.10, it would mean building our own image from
the tarball — not recommended.)

Tested on the box (not the VPS): fresh 1.43.9 and 1.43.11 installs with the production `extra-settings.php`
+ `login-security.php`; `update.php` clean on both; GempAuth PHPUnit suite 36/36 on both.

## Change in git

`docker-compose.yml` (wiki): pin the image instead of the moving `1.43` tag:
```diff
-    image: mediawiki:1.43
+    image: mediawiki:1.43.11
```
(Shipped as `ops/wiki-config/docker-compose.mw-1.43.11.yml` override so nothing changes until used.)
No composer changes: the official image ships core + bundled extensions with their vendor libraries
(OATHAuth's QR/HOTP libs and AbuseFilter's Equivset are in core `vendor/`). Do not run composer in the container.

FlaggedRevs is **not** bundled; it is bind-mounted from `/opt/swccg-wiki/extensions/FlaggedRevs`.
Before upgrading, record its version (`git -C /opt/swccg-wiki/extensions/FlaggedRevs log -1` or extension.json)
and, if it is a REL1_43 checkout, `git pull` the REL1_43 branch in the same window.

## Steps (≈ 10 minutes, one short outage)

1. Backups: `docker exec swccg_wiki_db mariadb-dump --single-transaction -u root -p… wiki > wiki-$(date +%F).sql`
   (password from `/opt/swccg-wiki/.env` via env var, never typed on the command line); copy `/opt/swccg-wiki/*.php`.
2. `docker pull mediawiki:1.43.11`
3. `cd /opt/swccg-wiki && docker compose -f docker-compose.yml -f docker-compose.localsettings.yml -f ops/wiki-config/docker-compose.mw-1.43.11.yml up -d wiki`
   (sessions are in MariaDB, so this does not log anyone out; never `--force-recreate` the `db` service).
4. `docker exec swccg_wiki php maintenance/run.php update --quick`
5. Verify: `curl -s 'https://wiki.swccg.com/api.php?action=query&meta=siteinfo&format=json' | grep -o '"generator":"[^"]*"'` → `MediaWiki 1.43.11`;
   `python3 /opt/swccg-wiki/verify-admin-login.py` → `LOGIN_OK`; open Main Page, a card page, Special:Version; edit + review one page as a bot.
6. Bump `$wgCacheEpoch` in `extra-settings.php` if CSS looks stale; `apachectl graceful`.

## Rollback

`image: mediawiki:1.43.9` and `up -d wiki`. 1.43.x point releases have no schema changes, so the DB needs no
restore; restore the dump only if `update.php` reported errors.
