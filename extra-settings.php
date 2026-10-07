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
$wgGroupPermissions['*']['createaccount'] = true;
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

$wgLogo = '/resources/assets/swccg-wiki-logo.png';
$wgLogos = [
	'1x' => '/resources/assets/swccg-wiki-logo.png',
	'icon' => '/resources/assets/swccg-wiki-logo.png',
];

# Never show the "Powered by MediaWiki" footer icon.
unset( $wgFooterIcons['poweredby'] );
$wgFooterIcons['poweredby'] = [];

# Bust ResourceLoader so Common.css/js edits go live.
$wgCacheEpoch = '20260930050000';

# Login sessions must survive docker restart / compose up. The official
# mediawiki:1.43 image defaults sessions to CACHE_ACCEL (APCu inside
# swccg_wiki); that store dies with the container and logs everyone out.
# MariaDB objectcache lives on volume wiki_db.
$wgSessionCacheType = CACHE_DB;
# Server-side session blob TTL. Default 3600s logs editors out after an
# hour of idle even when the Remember-me cookie is still valid.
$wgObjectCacheSessionExpiry = 180 * 24 * 3600;
$wgExtendedLoginCookieExpiration = 180 * 24 * 3600;
$wgCookieExpiration = 30 * 24 * 3600;
$wgPHPSessionHandling = 'disable';
