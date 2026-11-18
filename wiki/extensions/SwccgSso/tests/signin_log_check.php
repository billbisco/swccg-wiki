<?php
// #631. Run inside the wiki container: php extensions/SwccgSso/tests/signin_log_check.php
require __DIR__ . '/../src/SigninLog.php';
use MediaWiki\Extension\SwccgSso\SigninLog as L;
$fail = 0;
function t( $n, $ok ) { global $fail; echo ( $ok ? 'PASS ' : 'FAIL ' ) . $n . "\n"; if ( !$ok ) { $fail++; } }
$d = sys_get_temp_dir() . '/wiki-sso-test-' . getmypid(); @mkdir( $d, 0700 );
$now = gmmktime( 12, 0, 0, 11, 18, 2026 );
file_put_contents( "$d/sso-signin-2026-10-01.log", "old\n" );
file_put_contents( "$d/sso-signin-2026-10-20.log", "kept\n" );
t( 'ok line written', L::ok( 3841, '0123456789abcdef0123456789abcdef', 'abc', 'name@example.org', $d, $now ) );
t( 'refused line written', L::refused( 'bad_state', null, 'abc', 'fedcba9876543210fedcba9876543210', $d, $now ) );
$lines = file( "$d/sso-signin-2026-11-18.log" );
$a = json_decode( $lines[0], true ); $b = json_decode( $lines[1], true );
t( 'ok: ids only, bad rid dropped', $a['event'] === 'wiki_signin' && $a['gemp_id'] === 3841 && $a['tid'] === '0123456789abcdef0123456789abcdef' && $a['sfp'] === 'ba7816bf8f01cfea' && $a['rid'] === '-' && count( $a ) === 6 );
t( 'refused: reason, sfp, rid; never the state', $b['event'] === 'wiki_signin_refused' && $b['reason'] === 'bad_state' && $b['sfp'] === 'ba7816bf8f01cfea' && $b['tid'] === '-' && strpos( implode( '', $lines ), '"abc"' ) === false );
t( 'reason key fixed shape', L::reason( 'error:access_denied' ) === 'error:access_denied' && L::reason( 'a b' ) === 'other' );
t( 'old days pruned (30 days)', !file_exists( "$d/sso-signin-2026-10-01.log" ) && file_exists( "$d/sso-signin-2026-10-20.log" ) );
array_map( 'unlink', glob( "$d/*" ) ); @rmdir( $d );
echo $fail ? "FAILURES $fail\n" : "ALL PASS\n";
exit( $fail ? 1 : 0 );
