<?php
# Unified login + account security for wiki.swccg.com (V1 piece 3b).
# required from LocalSettings.php AFTER extra-settings.php (it overrides createaccount there).
# Approved plan: /workspace/reports/swccg-security-login-assessment.md ("Approved login plan").
# No secrets in this file. Email delivery ($wgSMTP, $wgPasswordSender) is NOT set here; Primary Bot owns it.

# --- Level 2: log in with the GEMP account (GempAuth) -------------------------------------
wfLoadExtension( 'GempAuth' );   # mounted at $IP/extensions/GempAuth
# Private listener on the GEMP container, reached over the attachable GEMP docker network.
# Never a public hostname: the port is not published on the host and nginx never proxies it.
$wgGempAuthEndpoint = getenv( 'GEMP_AUTH_ENDPOINT' ) ?: '';
$wgGempAuthAccountUrl = 'https://play.swccg.com/';
# Untracked, mode 0640 root:www-data. Defines $wgGempAuthSecret. Absent = GEMP login disabled.
if ( is_readable( "$IP/secrets/gempauth-secret.php" ) ) {
	require_once "$IP/secrets/gempauth-secret.php";
}

# New people sign up on GEMP; the wiki account is auto-created at first GEMP login.
$wgGroupPermissions['*']['createaccount'] = false;
$wgGroupPermissions['*']['autocreateaccount'] = true;
$wgGroupPermissions['sysop']['createaccount'] = true;   # admins can still make local accounts (bots)

# --- Level 3: content edits need a confirmed email (talk pages do not) ----------------------
# Not $wgEmailConfirmToEdit: that blocks talk pages too. GempAuth's getUserPermissionsErrors hook
# denies edit/create/move/upload in content namespaces unless the user has 'editcontent'.
$wgEmailAuthentication = true;
$wgAutopromote['emailconfirmed'] = APCOND_EMAILCONFIRMED;
$wgImplicitGroups[] = 'emailconfirmed';
$wgGroupPermissions['emailconfirmed']['editcontent'] = true;
$wgGroupPermissions['sysop']['editcontent'] = true;
$wgGroupPermissions['bot']['editcontent'] = true;
$wgGroupPermissions['editor']['editcontent'] = true;
# While real email is not live (SES pending), existing editors without a confirmed email go into
# this group instead (maintenance/grantConfirmedEditor.php). It grants editcontent only; unlike
# FlaggedRevs' 'editor' it carries no review rights.
$wgGroupPermissions['confirmed-editor']['editcontent'] = true;
$wgAddGroups['sysop'][] = 'confirmed-editor';
$wgRemoveGroups['sysop'][] = 'confirmed-editor';
$wgGroupPermissions['user']['edit'] = true;            # talk / user pages stay open to logged-in users
# FlaggedRevs unchanged: 'user' has autoreview=false, so Level 3 edits still queue for review.

# --- Level 4: 2FA for admins ---------------------------------------------------------------
wfLoadExtension( 'OATHAuth' );   # bundled in the mediawiki:1.43 image
# Two phases (Bill, 2026-10-19), see UNIFIED-LOGIN-RUNBOOK.md "Admin 2FA":
#   1. OATHAuth loaded, requirement OFF: admins enrol at Special:OATHManage.
#   2. After Bill confirms his enrolment, flip the next line to true and reload Apache.
# While required, members of these groups lose the group's rights until they enrol.
$swccgRequireAdmin2FA = false;
$wgOATHRequiredForGroups = $swccgRequireAdmin2FA ? [ 'sysop', 'bureaucrat', 'interface-admin' ] : [];
$wgGroupPermissions['user']['oathauth-enable'] = true;
# 2FA protects the session; keep "remember me" for admins shorter than the 180-day default.
# (Applies to everyone; leave at 180 days until Bill decides. See runbook "Decisions".)

# --- Anti-spam: signup, login, password reset, resend-confirmation ---------------------------
# ConfirmEdit/QuestyCaptcha + AbuseFilter + SpamBlacklist + TitleBlacklist are already loaded in
# extra-settings.php. Add a captcha after repeated bad logins (per IP and per account).
$wgCaptchaTriggers['badlogin'] = true;
$wgCaptchaTriggers['badloginperuser'] = true;
$wgCaptchaBadLoginAttempts = 3;
$wgCaptchaBadLoginPerUserAttempts = 10;
$wgCaptchaTriggers['createaccount'] = true;   # local accounts only (sysop) after the change above

# Wiki-side password throttle (local accounts; GEMP accounts are also limited inside GEMP).
$wgPasswordAttemptThrottle = [
	[ 'count' => 5, 'seconds' => 300 ],                          # per IP + username
	[ 'count' => 50, 'seconds' => 86400, 'allIPs' => true ],     # per username from anywhere
];
# Auto-creation counts against this too; real client IPs (below) make it per person, not site-wide.
$wgAccountCreationThrottle = [
	[ 'count' => 5, 'seconds' => 3600 ],
	[ 'count' => 10, 'seconds' => 86400 ],
];
$wgRateLimits['mailpassword'] = [ 'ip' => [ 3, 3600 ], 'user' => [ 3, 3600 ] ];
$wgRateLimits['confirmemail'] = [ 'ip' => [ 5, 86400 ], 'user' => [ 3, 86400 ], 'newbie' => [ 3, 86400 ] ];
$wgRateLimits['changeemail'] = [ 'ip' => [ 5, 86400 ], 'user' => [ 4, 86400 ], 'newbie' => [ 2, 86400 ] ];
$wgRateLimits['sendemail'] = [ 'ip' => [ 5, 86400 ], 'user' => [ 10, 86400 ], 'newbie' => [ 1, 86400 ] ];   # 'emailuser' was renamed 'sendemail' (1.43 config validation rejects the old key)
$wgRateLimits['edit']['newbie'] = [ 8, 60 ];
$wgRateLimits['create']['newbie'] = [ 4, 60 ];
$wgRateLimits['badcaptcha'] = [ 'ip' => [ 15, 3600 ], 'user' => [ 30, 86400 ] ];
# Rate-limit counters need a shared cache that survives requests. CACHE_ACCEL (APCu) is per
# container and fine for this single-container wiki.
$wgGroupPermissions['bot']['noratelimit'] = true;

# --- Real client IPs (M5): host nginx -> docker-proxy -> container --------------------------
# Every request arrives from the swccg-wiki_default bridge gateway. Trust X-Forwarded-For from it
# only. NoPurge: there is no cache to send PURGEs to (plain $wgCdnServers would PURGE the gateway).
$wgCdnServersNoPurge = [ '172.18.0.1' ];
$wgUsePrivateIPs = false;
