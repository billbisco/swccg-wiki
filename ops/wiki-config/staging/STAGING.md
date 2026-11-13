# Wiki staging on test.swccg.com

Approved by Bill (2026-10-19): **test.swccg.com only**. No production wiki, production GEMP or DNS change.

URL: `https://test.swccg.com/wiki/Main_Page` (scripts under `/w/`). The test GEMP site keeps `/`,
`/gemp-swccg/` and `/gemp-swccg-server/`; staging adds only `/w/`, `/wiki/`, `/chrome/`.

## What runs (docker project `swccg-wiki-staging`, dir `/opt/swccg-wiki-staging`)

| Service | Image | Notes |
|---|---|---|
| `wiki` (`swccg_wiki_staging`) | `mediawiki:1.43.11` | `127.0.0.1:17013`; production `LocalSettings.php` copy + `login-security.php` + `dev-mail-logonly.php` + `staging-settings.php` |
| `db` (`swccg_wiki_staging_db`) | `mariadb:10.11` | own server + volume, loaded from a `--single-transaction` dump of production (no `objectcache` rows, so no production sessions) |
| `gempauth` (`swccg_gempauth_staging`) | `gemp_app` (Java runtime only) | PR #287 build: real `AuthService` + `DbPlayerDAO`, private listener only, internal networks, no host port |
| `gempdb` (`swccg_gemp_staging_db`) | `mariadb:10.11` | fresh GEMP schema (pre-#284) + `update_password_hashing.sql`; one test player `wikistage` |

Nothing writable is shared with production: separate DB servers, volumes, networks, secrets (`$wgSecretKey`,
cookie prefix `swccgstaging`). **Images:** production's image files are bind-mounted **read-only**
(`/var/lib/docker/volumes/swccg-wiki_wiki_images/_data` → `/var/www/html/images:ro`); thumbnails, temp files and
locks go to staging's own volume (`staging_images` at `/var/www/html/staging-thumbs`, served as `/w/staging-thumbs/`).
Uploads stay off (`$wgEnableUploads = false`).
Mail: `dev-mail-logonly.php` writes to `/tmp/gempauth-mail.log` in the wiki container; nothing is sent.

Why not the test GEMP (`gemp_swccg_app_2`): it runs a pre-#284 build with local changes and is shared;
redeploying it is not part of this approval. The staging listener uses the same code path
(`AuthService.verifyCredentials` behind `InternalAuthServer`) against its own GEMP DB.

## Deploy / rollback

```
# box: build bundle (wiki-config/ + gempauth/) and copy it with a player password file to the VPS
sudo ./deploy-staging.sh /tmp/swccg-wiki-staging-bundle.tgz /tmp/wikistage-pw
sudo /opt/swccg-wiki-staging/wiki-config/staging/rollback-staging.sh
```
`deploy-staging.sh` refuses to run if the dir, port 17013, subnet 172.31.13.0/24 or the vhost markers already
exist, or if a dump is running on the production wiki DB. It checks that the wiki's `db` host is the staging DB
container before `update.php`. Rollback removes only the marked vhost blocks, the project's containers,
volumes and networks, and the directory.
