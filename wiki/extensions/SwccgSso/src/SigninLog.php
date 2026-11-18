<?php
/**
 * Wiki sign-in log (#631): one line per sign-in callback through swccg.com, so a
 * wiki sign-in can be followed from nginx through swccg-login to the wiki by its
 * tracking id (swccg_tid in the ID token). A refused callback has no ID token; it
 * is logged with a reason key and the state fingerprint (sfp: first 16 hex of
 * SHA-256 of the state, as swccg-login logs it), never the state itself.
 * Account number and ids only: no name, email or address. Daily files in
 * /var/log/wiki-sso (the data volume), deleted after 30 days.
 */
namespace MediaWiki\Extension\SwccgSso;

class SigninLog {
	public const DIR = '/var/log/wiki-sso';
	public const DAYS = 30;

	/** Hex ids only (16-64), anything else is logged as "-". */
	public static function clean( $id ): string {
		return ( is_string( $id ) && preg_match( '/^[0-9a-f]{16,64}$/', $id ) ) ? $id : '-';
	}

	public static function sfp( $state ): string {
		return ( is_string( $state ) && $state !== '' ) ? substr( hash( 'sha256', $state ), 0, 16 ) : '-';
	}

	public static function reason( $r ): string {
		$r = strtolower( (string)$r );
		return preg_match( '/^[a-z0-9_:]{1,64}$/', $r ) ? $r : 'other';
	}

	public static function okLine( int $id, $tid, $state, $rid, int $now ): string {
		return json_encode( [
			'time' => gmdate( 'Y-m-d\TH:i:s\Z', $now ), 'event' => 'wiki_signin', 'gemp_id' => $id,
			'tid' => self::clean( $tid ), 'sfp' => self::sfp( $state ), 'rid' => self::clean( $rid ),
		] ) . "\n";
	}

	public static function refusedLine( $reason, $tid, $state, $rid, int $now ): string {
		return json_encode( [
			'time' => gmdate( 'Y-m-d\TH:i:s\Z', $now ), 'event' => 'wiki_signin_refused', 'reason' => self::reason( $reason ),
			'tid' => self::clean( $tid ), 'sfp' => self::sfp( $state ), 'rid' => self::clean( $rid ),
		] ) . "\n";
	}

	public static function ok( int $id, $tid, $state, $rid, string $dir = self::DIR, ?int $now = null ): bool {
		$now = $now ?? time();
		return self::append( self::okLine( $id, $tid, $state, $rid, $now ), $dir, $now );
	}

	public static function refused( $reason, $tid, $state, $rid, string $dir = self::DIR, ?int $now = null ): bool {
		$now = $now ?? time();
		return self::append( self::refusedLine( $reason, $tid, $state, $rid, $now ), $dir, $now );
	}

	private static function append( string $line, string $dir, int $now ): bool {
		if ( !is_dir( $dir ) || !is_writable( $dir ) ) {
			return false;
		}
		$file = $dir . '/sso-signin-' . gmdate( 'Y-m-d', $now ) . '.log';
		$newDay = !file_exists( $file );
		$ok = @file_put_contents( $file, $line, FILE_APPEND | LOCK_EX ) !== false;
		if ( $newDay ) {
			self::prune( $dir, $now );
		}
		return $ok;
	}

	/** Keeps today and the DAYS-1 days before it; returns how many files it deleted. */
	public static function prune( string $dir = self::DIR, ?int $now = null, int $days = self::DAYS ): int {
		$now = $now ?? time();
		$cut = gmdate( 'Y-m-d', $now - ( $days - 1 ) * 86400 );
		$n = 0;
		foreach ( (array)@scandir( $dir ) as $f ) {
			if ( preg_match( '/^sso-signin-(\d{4}-\d{2}-\d{2})\.log$/', (string)$f, $m ) && $m[1] < $cut && @unlink( $dir . '/' . $f ) ) {
				$n++;
			}
		}
		return $n;
	}
}
