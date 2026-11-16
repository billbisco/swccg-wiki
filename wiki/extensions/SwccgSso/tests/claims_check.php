<?php
// Run inside the wiki container: echo 'require "extensions/SwccgSso/tests/claims_check.php";' | php maintenance/run.php eval
require __DIR__ . '/../src/OidcKeys.php';
require __DIR__ . '/../src/BackchannelLogoutHandler.php';
use MediaWiki\Extension\SwccgSso\BackchannelLogoutHandler as B;
$now = time(); $iss = 'https://swccg.com/login';
$ok = [ 'iss' => $iss, 'aud' => 'wiki', 'iat' => $now, 'exp' => $now + 120, 'jti' => 'j1', 'sub' => '3901', 'sid' => 's1',
	'events' => [ B::EVENT => [] ] ];
$cases = [
	'ok' => [ $ok, null ],
	'aud string' => [ [ 'aud' => [ 'wiki' ] ] + $ok, null ],
	'no sid' => [ array_diff_key( $ok, [ 'sid' => 1 ] ), null ],
	'wrong aud' => [ [ 'aud' => 'forum' ] + $ok, 'wrong audience' ],
	'wrong iss' => [ [ 'iss' => 'https://evil' ] + $ok, 'wrong issuer' ],
	'nonce' => [ $ok + [ 'nonce' => 'x' ], 'nonce present' ],
	'no events' => [ array_diff_key( $ok, [ 'events' => 1 ] ), 'no back-channel event' ],
	'expired' => [ [ 'exp' => $now - 3600 ] + $ok, 'expired' ],
	'no jti' => [ array_diff_key( $ok, [ 'jti' => 1 ] ), 'no jti' ],
	'no sub/sid' => [ array_diff_key( $ok, [ 'sub' => 1, 'sid' => 1 ] ), 'no sub or sid' ],
	'bad sub' => [ [ 'sub' => '1 OR 1' ] + $ok, 'bad sub' ],
];
$fail = 0;
foreach ( $cases as $n => [ $c, $want ] ) {
	$got = B::claimsProblem( $c, $iss, 'wiki', $now );
	$r = $got === $want ? 'PASS' : 'FAIL';
	if ( $r === 'FAIL' ) { $fail++; }
	echo "$r $n => " . var_export( $got, true ) . "\n";
}
echo $fail ? "FAILURES $fail\n" : "ALL PASS\n";
