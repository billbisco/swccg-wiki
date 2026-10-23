<?php
# Wiki staging overrides (test.swccg.com). Required at the END of the staging LocalSettings.php,
# after extra-settings.php, login-security.php and dev-mail-logonly.php. No secrets in this file.
$wgSitename = 'SWCCG Wiki (staging)';
$wgServer = 'https://test.swccg.com';
$wgCanonicalServer = 'https://test.swccg.com';
$wgScriptPath = '/w';
$wgArticlePath = '/wiki/$1';
$wgResourceBasePath = '/w';
foreach ( $wgLogos ?? [] as $k => $v ) {
	if ( is_string( $v ) && str_starts_with( $v, '/' ) && !str_starts_with( $v, '/w/' ) ) {
		$wgLogos[$k] = '/w' . $v;
	}
}
$wgCookiePrefix = 'swccgstaging';
$wgCookieSecure = true;
$wgDefaultRobotPolicy = 'noindex,nofollow';
$wgEnableUploads = false;   # production's extra-settings.php turns uploads on; staging keeps them off

# Images: production's originals are bind-mounted READ-ONLY at $IP/images (see docker-compose.staging.yml).
# Thumbnails, temp files and deletions go to staging's own volume at $IP/staging-thumbs, and the
# backend uses no lock files (lockdir would be inside the read-only mount).
$wgFileBackends[] = [
	'name' => 'staging-local-backend',
	'class' => FSFileBackend::class,
	'lockManager' => 'nullLockManager',
	'containerPaths' => [
		'local-public' => "$IP/images",
		'local-thumb' => "$IP/staging-thumbs/thumb",
		'local-transcoded' => "$IP/staging-thumbs/transcoded",
		'local-temp' => "$IP/staging-thumbs/temp",
		'local-deleted' => "$IP/staging-thumbs/deleted",
	],
	'fileMode' => 0644,
	'directoryMode' => 0755,
];
$wgLocalFileRepo = [
	'class' => LocalRepo::class,
	'name' => 'local',
	'backend' => 'staging-local-backend',
	'url' => '/w/images',
	'thumbUrl' => '/w/staging-thumbs/thumb',
	'transcodedUrl' => '/w/staging-thumbs/transcoded',
	'hashLevels' => 2,
	'deletedHashLevels' => 3,
	'thumbScriptUrl' => false,
	'transformVia404' => false,
	'abbrvThreshold' => 255,
	'isPrivate' => false,
	'updateCompatibleMetadata' => false,
	'reserializeMetadata' => false,
];
$wgUploadDirectory = "$IP/staging-thumbs";   # lockdir, temp and anything else written under the upload dir
$wgDeletedDirectory = "$IP/staging-thumbs/deleted";

# Own DB server (docker service "db"), own secrets: DB password, $wgSecretKey, $wgUpgradeKey.
$wgDBserver = 'db';
$wgDBname = 'wiki';
$wgDBuser = 'wiki';
require_once "$IP/secrets/staging-secrets.php";

# Staging GEMP auth listener on the internal "auth" network.
$wgGempAuthEndpoint = 'http://gempauth:8090/internal/v1/verify';

# Real client IP: requests arrive from the staging "web" network gateway.
$wgCdnServersNoPurge = [ '172.31.13.1' ];

# Logs used by the staging checks (container-local, /tmp).
$wgDebugLogGroups['authentication'] = '/tmp/mw-authentication.log';
$wgDebugLogGroups['GempAuth'] = '/tmp/mw-gempauth.log';
$wgDebugLogGroups['ratelimit'] = '/tmp/mw-ratelimit.log';
