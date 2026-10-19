# GempAuth

MediaWiki 1.43 extension for wiki.swccg.com: log in with a GEMP (play.swccg.com) account.

- `GempPrimaryAuthenticationProvider` — non-authoritative password provider (sort 50, before LocalPassword). Calls GEMP's private `POST /internal/v1/verify` (HMAC-signed, contract in `docs/wiki-auth-api.md`), auto-creates and links the wiki user on first login, refuses unlinked name collisions, blocks wiki password changes/resets for linked users.
- `Hooks::onGetUserPermissionsErrors` — content namespaces need `editcontent` (granted by the `emailconfirmed` autopromote group); talk pages stay open. Replaces `$wgEmailConfirmToEdit`, which would also block talk.
- `maintenance/linkGempAccount.php` — admin link/unlink.

Config: `$wgGempAuthEndpoint`, `$wgGempAuthSecret` (untracked file), `$wgGempAuthTimeout`, `$wgGempAuthAccountUrl`, `$wgGempAuthEmailGateNamespaces`.

Tests (from a MediaWiki 1.43 checkout with dev dependencies, extension at `extensions/GempAuth`):
```
php vendor/bin/phpunit extensions/GempAuth/tests/phpunit
```
The integration tests need the site config from `ops/wiki-config/login-security.php` loaded in LocalSettings.
