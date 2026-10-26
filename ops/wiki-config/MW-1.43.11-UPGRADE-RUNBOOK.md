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

## Rehearsal

Rehearsed on the staging copy at `test.swccg.com/wiki/` (a copy of the production DB in its own DB
server, see `staging/STAGING.md`): `update.php --quick` from 1.43.9 data on the 1.43.11 image.

## Steps (≈ 10 minutes, one short outage)

0. **Prerequisite (Alpha3 owns wiki + GEMP backups):** get a fresh backup path and its sha256 from Alpha3
   and agree the window with Alpha3 so the nightly backup (`swccg-backup.timer`, 07:15 UTC) does not overlap it.
   Do not start step 2 until both the path and the sha256 are recorded in the change note.
1. Backups (only if Alpha3's backup above is not used): `docker exec swccg_wiki_db mariadb-dump --single-transaction -u root -p… wiki > wiki-$(date +%F).sql`
   (password from `/opt/swccg-wiki/.env` via env var, never typed on the command line); copy `/opt/swccg-wiki/*.php`.
2. `docker pull mediawiki:1.43.11`
3. `cd /opt/swccg-wiki && docker compose -f docker-compose.yml -f docker-compose.localsettings.yml -f ops/wiki-config/docker-compose.mw-1.43.11.yml up -d wiki`
   (sessions are in MariaDB, so this does not log anyone out; never `--force-recreate` the `db` service).
4. `docker exec swccg_wiki php maintenance/run.php update --quick`
5. Verify: `curl -s 'https://wiki.swccg.com/api.php?action=query&meta=siteinfo&format=json' | grep -o '"generator":"[^"]*"'` → `MediaWiki 1.43.11`;
   `python3 /opt/swccg-wiki/verify-admin-login.py` → `LOGIN_OK`; open Main Page, a card page, Special:Version; edit + review one page as a bot.
6. Bump `$wgCacheEpoch` in `extra-settings.php` if CSS looks stale; `apachectl graceful`.

## After EVERY image or extension update (caching phase 1, deployed 2026-10-21)

Since 2026-10-21 the wiki runs self-built images (`swccg/mediawiki:1.43.9-php8.3.36-live-cache1` live,
`swccg/mediawiki:1.43.11-php8.3.36-cache1` staging; build context `/root/php2shell-build-20261021/cache1/`,
`ARG BASE=<previous image>`) and nginx serves static files from copies on the host. After any image,
MediaWiki point release or extension change (including a FlaggedRevs `git pull`), in the same window:

1. Rebuild the image on top of the new base so `zz-caching.ini` (APCu 128M, opcache 256/20000/16) is kept:
   `docker build --build-arg BASE=<new base image> -t <new tag>-cache1 /root/php2shell-build-20261021/cache1`
2. Localisation cache (CDB files in the `wiki_cache` volume, `$wgCacheDirectory=/var/www/cache/l10n`):
   `docker exec -u www-data swccg_wiki php maintenance/run.php rebuildLocalisationCache --force`
   (≈50 s, 526 languages; staging: same with `swccg_wiki_staging`).
3. Static copy used by nginx for `/skins/`, `/resources/`, `/extensions/` (CSS/JS/images/fonts):
   `bash /root/wiki-caching-20261021/scripts/refresh-static-live.sh`
   (staging: `refresh-static-staging.sh`). Missing files fall back to Apache, but stale ones are served for 30 days.
4. Check the read-only image mounts nginx serves `/images/` from (they must show `ro` and point at the volume data):
   `systemctl is-active srv-wikistatic-live-images.mount` and `findmnt /srv/wikistatic/live/images`
   (staging: `srv-wikistatic-staging-w-images.mount`, `srv-wikistatic-staging-w-staging\x2dthumbs.mount`).
   If the images volume was recreated or moved, re-enable: `systemctl restart srv-wikistatic-live-images.mount`.
5. Verify: `curl -sI https://wiki.swccg.com/images/<any file>` → `Cache-Control: max-age=86400`, `X-Content-Type-Options: nosniff`,
   `X-Wiki-Static: nginx`; `curl -sI https://wiki.swccg.com/skins/Vector/resources/skins.vector.styles.legacy/images/bullet-icon.svg`
   → `X-Wiki-Static: nginx`; an article twice logged out → `X-Cache-Status: MISS` then `HIT`.
6. Optional: if pages look stale for logged-out readers, the nginx microcache expires on its own after 2 minutes, and the
   MediaWiki file cache (`/var/www/cache/html`) is invalidated by `$wgCacheEpoch` bumps; to clear it at once:
   `docker exec swccg_wiki sh -c 'rm -rf /var/www/cache/html/*'`.

Full details and rollback scripts: `/root/wiki-caching-20261021/LIVE-PLAN.md`, `/root/wiki-caching-20261021/live/rollback-live-*.sh`.

## Rollback

`image: <previous tag>` and `up -d wiki` (then steps 2–4 above for the previous image). 1.43.x point releases have no schema changes, so the DB needs no
restore; restore the dump only if `update.php` reported errors.
