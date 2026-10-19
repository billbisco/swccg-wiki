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
$wgEnableUploads = false;

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
