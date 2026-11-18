<?php
# WP-W1/W2 extras. Required from LocalSettings.php. No secrets.

wfLoadExtension( 'ParserFunctions' );
wfLoadExtension( 'Cite' );
wfLoadExtension( 'TemplateData' );
wfLoadExtension( 'WikiEditor' );
wfLoadExtension( 'ConfirmEdit' );
wfLoadExtension( 'ConfirmEdit/QuestyCaptcha' );
wfLoadExtension( 'AbuseFilter' );
wfLoadExtension( 'TitleBlacklist' );
wfLoadExtension( 'SpamBlacklist' );

$wgCaptchaClass = 'QuestyCaptcha';
$wgCaptchaQuestions = [
	'What card game is this wiki about? (answer: SWCCG or Star Wars CCG)' => [
		'SWCCG', 'swccg', 'Star Wars CCG', 'star wars ccg', 'Star Wars Customizable Card Game',
	],
];
$wgCaptchaTriggers['createaccount'] = true;
$wgCaptchaTriggers['addurl'] = true;
$wgCaptchaTriggers['edit'] = false;
$wgCaptchaTriggers['create'] = false;

# Captcha on account creation; still no anon edits.
$wgGroupPermissions['*']['createaccount'] = false; // #586: accounts are made at swccg.com/login (2026-11-17)
$wgGroupPermissions['*']['edit'] = false;

if ( !defined( 'NS_CARD' ) ) {
	define( 'NS_CARD', 3000 );
	define( 'NS_CARD_TALK', 3001 );
}
$wgExtraNamespaces[NS_CARD] = 'Card';
$wgExtraNamespaces[NS_CARD_TALK] = 'Card_talk';
$wgContentNamespaces[] = NS_CARD;
$wgNamespacesToBeSearchedDefault[NS_CARD] = true;
$wgNamespacesWithSubpages[NS_CARD] = true;

$wgFlaggedRevsNamespaces = [ NS_MAIN, NS_PROJECT, NS_TEMPLATE, NS_HELP, NS_CARD ];

$wgArticlePath = '/wiki/$1';
$wgUsePathInfo = true;

# LOTR-wiki-style left sidebar (Vector legacy, not Vector 2022)
$wgDefaultSkin = 'vector';
$wgVectorUseWvuiSearch = false;
# Vector legacy: keep skin.json responsive:false (viewport width=1120).
# Phone dual-Objective stack uses Common.js screen.width -> html.card-device-narrow
# (do NOT force device-width site-wide — wrecks Vector chrome on phone).

$wgEnableUploads = true;
$wgGroupPermissions['sysop']['upload'] = true;
$wgGroupPermissions['sysop']['reupload'] = true;
$wgFileExtensions[] = 'gif';
$wgFileExtensions[] = 'png';
$wgFileExtensions[] = 'jpg';
$wgFileExtensions[] = 'jpeg';
$wgFileExtensions[] = 'webp';
$wgFileExtensions[] = 'txt';
$wgFileExtensions[] = 'pdf';
# html GEMP dumps are stored as .txt (importImages); championship sheet scans are PDF
$wgMaxUploadSize = 80 * 1024 * 1024;
$wgUseImageMagick = true;
$wgImageMagickConvertCommand = '/usr/bin/convert';

$wgLogo = '/wiki/resources/assets/swccg-wiki-logo.png';
$wgLogos = [
	'1x' => '/wiki/resources/assets/swccg-wiki-logo.png',
	'icon' => '/wiki/resources/assets/swccg-wiki-logo.png',
];

# Never show the "Powered by MediaWiki" footer icon.
unset( $wgFooterIcons['poweredby'] );
$wgFooterIcons['poweredby'] = [];

# Bust ResourceLoader so Common.css/js edits go live.
$wgCacheEpoch = '20261117123600';  # #267: refresh every page for the sidebar Play link (Bill 2026-11-15); was 20261115141257

# Login sessions must survive docker restart / compose up. The official
# mediawiki:1.43 image defaults sessions to CACHE_ACCEL (APCu inside
# swccg_wiki); that store dies with the container and logs everyone out.
# MariaDB objectcache lives on volume wiki_db.
$wgSessionCacheType = CACHE_DB;
# Server-side session blob TTL. #632 (Bill 2026-11-18 "proceed with your 1-3", Alpha12):
# a browser that is signed in (sends a wikiUserID cookie) gets 400 days, renewed on use like the
# swccg.com sign-in service; anonymous sessions (bots on Special:UserLogin, the SSO state that
# Special:SwccgSignIn keeps for ~10 minutes) expire after 1 hour. Was 180 days for every session.
# Rollback: /mnt/HC_Volume_107153504/work/alpha12-wikiperf/sessions/rollback.sh
# Agent accounts (Bill 2026-11-18 10:31 "Yes, go ahead with all three session fixes") get 1-day
# sessions; decided from the request's wikiUserName cookie, so no session lookup is needed here.
# Rollback of this rule only: rollback-632b.sh.
$wgSwccgAgentAccounts = [ 'datacardgrok', 'comlinkcursor', 'memorycorechatgpt', 'holocronclaude' ]; # #632 user_name without spaces, lower case
$wgObjectCacheSessionExpiry = ( isset( $_COOKIE['wikiUserID'] ) && preg_match( '/^[1-9][0-9]*$/', (string)$_COOKIE['wikiUserID'] ) )
	? ( in_array( strtolower( str_replace( [ '_', ' ' ], '', (string)( $_COOKIE['wikiUserName'] ?? '' ) ) ), $wgSwccgAgentAccounts, true )
		? 24 * 3600 : 400 * 24 * 3600 )
	: 3600; # #632
$wgExtendedLoginCookieExpiration = 400 * 24 * 3600; # #632 was 180 days
$wgCookieExpiration = 400 * 24 * 3600; # #632 was 30 days
# #632: core sends wiki_session as a browser-session cookie; for a signed-in session make it last
# 400 days (renewed whenever MediaWiki renews the session). Anonymous sessions are unchanged.
$wgHooks['WebResponseSetCookie'][] = static function ( &$name, &$value, &$expire, &$options ) { # #632
	if ( $name !== 'wiki_session' || (int)$expire !== 0 ) {
		return true;
	}
	try {
		$s = \MediaWiki\Session\SessionManager::getGlobalSession();
		if ( $s->getId() === (string)$value && $s->getUser()->isRegistered() ) {
			$expire = time() + 400 * 24 * 3600;
		}
	} catch ( \Throwable $e ) {
		// keep the browser-session cookie
	}
	return true;
}; # #632 end
$wgPHPSessionHandling = 'disable';

# --- GEMP Importable decklists (Bill 2026-10-10) ------------------------------------------
# GEMP decklist .txt files are XML inside, and MediaWiki blocks XML uploads by default.
# Allow them ONLY when the file is a GEMP deck: a .txt file under 512 KB whose root element is
# <deck> holding only <card>/<cardOutsideDeck> elements, with no DOCTYPE, entities, stylesheet
# instructions, namespaces or script. Any other XML upload is still refused.
$wgMimeTypeExclusions = array_values( array_diff( $wgMimeTypeExclusions, [ 'application/xml', 'text/xml' ] ) );
# Let a .txt name carry XML content (the GEMP format); the UploadVerifyFile check below then
# decides whether that XML is really a GEMP deck.
$wgHooks['MimeMagicInit'][] = static function ( $mimeAnalyzer ) {
	$mimeAnalyzer->addExtraTypes( 'application/xml txt' );
};
$wgHooks['UploadVerifyFile'][] = static function ( $upload, $mime, &$error ) {
	if ( $mime !== 'application/xml' && $mime !== 'text/xml' ) {
		return true;
	}
	$title = $upload->getTitle();
	$path = $upload->getTempPath();
	$ok = $title && preg_match( '/\.txt$/i', $title->getText() ) && $path && filesize( $path ) <= 512 * 1024;
	if ( $ok ) {
		$xml = file_get_contents( $path );
		$ok = !preg_match( '/<!DOCTYPE|<!ENTITY|<\?xml-stylesheet|xmlns|<script|javascript:/i', $xml );
	}
	if ( $ok ) {
		$prev = libxml_use_internal_errors( true );
		$doc = simplexml_load_string( $xml, 'SimpleXMLElement', LIBXML_NONET );
		libxml_use_internal_errors( $prev );
		$ok = $doc !== false && $doc->getName() === 'deck';
		if ( $ok ) {
			foreach ( $doc->children() as $child ) {
				if ( !in_array( $child->getName(), [ 'card', 'cardOutsideDeck' ], true ) ) {
					$ok = false;
					break;
				}
			}
		}
	}
	if ( !$ok ) {
		$error = [ 'filetype-badmime', $mime ];
		return false;
	}
	return true;
};
$wgGroupPermissions['bot']['noratelimit'] = true;
$wgJobRunRate = 0;

# 2026-11-10 Bill: mass dest/purge — skip throttle; dest rights on bot/editor
$wgGroupPermissions['editor']['noratelimit'] = true;
$wgGroupPermissions['reviewer']['noratelimit'] = true;

$swccgDestRights = [
	'noratelimit',
	'apihighlimits',
	'skipcaptcha',
	'autoconfirmed',
	'editsemiprotected',
	'editprotected',
	'patrol',
	'review',
	'autoreview',
	'validate',
	'unreviewedpages',
	'suppressredirect',
	'reupload',
	'upload',
	'movefile',
];
foreach ( [ 'bot', 'editor' ] as $swccgGroup ) {
	foreach ( $swccgDestRights as $swccgRight ) {
		$wgGroupPermissions[$swccgGroup][$swccgRight] = true;
	}
}

$swccgUnlimited = [ 100000000, 60 ];
$swccgBuckets = [ 'ip', 'ip-all', 'newbie', 'user', 'bot' ];
$swccgExtraActions = [
	'edit', 'move', 'upload', 'rollback', 'mailpassword', 'emailuser',
	'changeemail', 'confirmemail', 'purge', 'linkpurge', 'renderfile',
	'renderfile-nonstandard', 'stashedit', 'stashbasehtml', 'changetags',
	'editcontentmodel', 'review', 'thanks', 'patrol', 'sendemail',
];
$swccgActions = array_unique( array_merge( array_keys( $wgRateLimits ?? [] ), $swccgExtraActions ) );
foreach ( $swccgActions as $swccgAction ) {
	foreach ( $swccgBuckets as $swccgBucket ) {
		$wgRateLimits[$swccgAction][$swccgBucket] = $swccgUnlimited;
	}
}

# Bill approved 2026-11-11: allow steam:// Workshop links
$wgUrlProtocols[] = 'steam://';

# SWCCG #266 — account-name rules (Unicode 15.0; no auto-capitalisation; space and underscore distinct). Article text is unrestricted.
wfLoadExtension( "SWCCGAccountNames" );
$wgCapitalLinkOverrides[NS_USER] = false;
$wgCapitalLinkOverrides[NS_USER_TALK] = false;


# #267 one host (Alpha11 2026-11-15): wiki at https://swccg.com/wiki; its cookies stay under /wiki, host-only.
$wgCookieDomain = "";
$wgCookiePath = "/wiki";
$wgCookieSecure = true;
$wgCookieHttpOnly = true;

# #267 wiki SSO (Alpha11, 2026-11-15, Bill go-ahead): sign in with the site account at the same membership id.
# Since #266 AC8 (2026-11-17) the wiki has no password sign-in of its own (block below). Rollback: delete this block.
if ( is_dir( "$IP/extensions/SwccgSso" ) && is_readable( "$IP/sso-settings.php" ) ) {
	wfLoadExtension( 'SwccgSso' );
	$wgSwccgSsoIssuer = 'https://swccg.com/login';
	$wgSwccgSsoClientId = 'wiki';
	$wgSwccgSsoRedirectUri = 'https://swccg.com/wiki/Special:SwccgSignIn';
	require_once "$IP/sso-settings.php";
	$wgDebugLogGroups['SwccgSso'] = '/var/www/cache/swccgsso.log';
}

# #564 real client IP (Alpha6, 2026-11-16, Bill: no account-wide lock a stranger can trigger).
# nginx on the host reaches the wiki through the docker gateway; trust it for X-Forwarded-For so
# password throttles, rate limits and blocks use the visitor's IP, not one shared address.
# Rollback: delete this block.
# The live value (the docker network gateway on the wiki host) is set on the server only.
$wgCdnServersNoPurge = [ '<docker-gateway-ip>' ];

# swccg-guild/work#570 (2026-11-16): keep AbuseFilter log IPs 30 days, site-wide IP rule.
$wgAbuseFilterLogIPMaxAge = 30 * 86400;

# #266 AC8 one sign-in (Alpha11, 2026-11-17, Bill: "One sign in for everyone. No wiki only sign in.").
# The wiki has no password sign-in of its own: everyone, staff and bots included, signs in at
# swccg.com/login through Special:SwccgSignIn. Bots script that same sign-in
# (billbisco/swccg-wiki authoring/swccg_signin.py). Rollback: delete this block.
$wgAuthManagerAutoConfig['primaryauth'] = [];
$wgEnableBotPasswords = true;
$wgPasswordResetRoutes = [ 'username' => false, 'email' => false ];
# #597 / dest'd #266 AC8: bots use MediaWiki BotPasswords via action=login; humans stay on swccg.com/login.
foreach ( [ 'clientlogin', 'createaccount', 'linkaccount', 'unlinkaccount',
	'changeauthenticationdata', 'removeauthenticationdata', 'resetpassword' ] as $swccgOff ) {
	$wgAPIModules[$swccgOff] = 'ApiDisabled';
}
$wgHooks['SpecialPageBeforeExecute'][] = static function ( $special, $subPage ) {
	$name = $special->getName();
	if ( in_array( $name, [ 'Userlogin', 'CreateAccount' ], true ) ) {
		$q = [];
		$rt = $special->getRequest()->getVal( 'returnto' );
		if ( $rt !== null && $rt !== '' ) {
			$q['returnto'] = $rt;
		}
		$url = \MediaWiki\SpecialPage\SpecialPage::getTitleFor( 'SwccgSignIn' )->getLocalURL( $q );
		$out = $special->getOutput();
		if ( $special->getUser()->isRegistered() ) {
			$out->redirect( wfExpandUrl( $url, PROTO_CANONICAL ) );
			return false;
		}
		// A light page with only the site sign-in (no wiki password form). Not a redirect: crawlers
		// follow Special:UserLogin links in bulk, and each redirect would start a sign-in at swccg.com.
		$out->setPageTitleMsg( $special->msg( 'login' ) );
		$out->setRobotPolicy( 'noindex,nofollow' );
		$out->addHTML( Html::rawElement( 'div', [ 'class' => 'swccgsso-box', 'style' => 'max-width:290px;margin:0 0 1.5em' ],
			Html::element( 'a', [ 'href' => $url, 'rel' => 'nofollow', 'class' => 'cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--action-progressive cdx-button--weight-primary', 'style' => 'width:100%;justify-content:center' ],
				$special->msg( 'swccgsso-button' )->text() ) .
			Html::element( 'p', [ 'style' => 'font-size:90%;margin:.5em 0' ], $special->msg( 'swccgsso-button-help' )->text() ) ) );
		return false;
	}
	if ( in_array( $name, [ 'PasswordReset', 'ChangePassword', 'ChangeCredentials', 'RemoveCredentials',
		'BotPasswords', 'LinkAccounts', 'UnlinkAccounts' ], true ) ) {
		$special->getOutput()->redirect( 'https://swccg.com/login/account' );
		return false;
	}
};
