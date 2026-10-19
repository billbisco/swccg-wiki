<?php
/**
 * Live end-to-end driver: real GempAuth + real GEMP private listener (see run-e2e.sh).
 * One case per process, so each case gets its own request with its own forwarded client IP.
 *
 * php maintenance/run.php --conf <e2e-settings.php> <this file> --case ok --ip 203.0.113.50 \
 *     --seed seed.json --gemp-log gemp.log
 */

use MediaWiki\Auth\AuthenticationResponse;
use MediaWiki\Auth\AuthManager;
use MediaWiki\Auth\PasswordAuthenticationRequest;
use MediaWiki\Context\RequestContext;
use MediaWiki\Extension\GempAuth\GempPrimaryAuthenticationProvider;
use MediaWiki\Maintenance\Maintenance;
use MediaWiki\Request\FauxRequest;

// phpcs:ignore MediaWiki.Files.ClassMatchesFilename
class GempAuthE2EProxyRequest extends FauxRequest {
	/** The TCP peer is the docker bridge gateway (host nginx); the end user is in X-Forwarded-For. */
	protected function getRawIP() {
		return '172.18.0.1';
	}
}

class GempAuthE2E extends Maintenance {
	private const PASSWORD = 'Correct-Horse-9';
	private int $failures = 0;
	private array $seed = [];
	private string $gempLog = '';
	private string $ip = '';

	public function __construct() {
		parent::__construct();
		$this->addOption( 'case', 'Case name', true, true );
		$this->addOption( 'ip', 'End-user IP to forward through the trusted proxy', true, true );
		$this->addOption( 'seed', 'Seed JSON written by WikiAuthE2EServer', true, true );
		$this->addOption( 'gemp-log', 'GEMP listener log file', true, true );
	}

	private function check( bool $ok, string $what ): void {
		$this->output( ( $ok ? '  PASS ' : '  FAIL ' ) . $what . "\n" );
		if ( !$ok ) {
			$this->failures++;
		}
	}

	private function login( string $name, string $password ): AuthenticationResponse {
		$req = new PasswordAuthenticationRequest();
		$req->action = AuthManager::ACTION_LOGIN;
		$req->username = $name;
		$req->password = $password;
		return $this->getServiceContainer()->getAuthManager()->beginAuthentication( [ $req ], 'http://localhost/' );
	}

	private function expectFail( AuthenticationResponse $res, string $key, string $what ): void {
		$got = $res->message ? $res->message->getKey() : '(none)';
		$this->check( $res->status === AuthenticationResponse::FAIL && $got === $key,
			"$what -> FAIL $key (got {$res->status} $got)" );
	}

	private function registered( string $name ): bool {
		$u = $this->getServiceContainer()->getUserIdentityLookup()->getUserIdentityByName( $name );
		return $u !== null && $u->isRegistered();
	}

	private function linkedId( string $name ): ?string {
		$u = $this->getServiceContainer()->getUserFactory()->newFromName( $name );
		$v = $this->getServiceContainer()->getUserOptionsLookup()->getOption( $u, GempPrimaryAuthenticationProvider::LINK_OPTION );
		return ( $v === null || $v === '' ) ? null : (string)$v;
	}

	/** GEMP decision lines ("wiki-auth: ...") currently in the listener log. */
	private function gempLines(): array {
		clearstatcache();
		$lines = file( $this->gempLog, FILE_IGNORE_NEW_LINES ) ?: [];
		return array_values( array_filter( $lines, static fn ( $l ) => str_contains( $l, 'wiki-auth: ' ) ) );
	}

	private function lastGempLineFor( string $user ): string {
		usleep( 200000 );
		$hits = array_filter( $this->gempLines(), static fn ( $l ) => str_contains( $l, "user=$user " ) );
		return $hits ? end( $hits ) : '';
	}

	private function expectGemp( string $user, string $result ): void {
		$line = $this->lastGempLineFor( $user );
		$this->check( str_contains( $line, "ip={$this->ip} " ) || str_ends_with( $line, "ip={$this->ip}" ),
			"GEMP saw client_ip={$this->ip} for $user (not the peer 127.0.0.1 / 172.18.0.1)" );
		$this->check( $result === '' || str_contains( $line, "result=$result" ) || str_contains( $line, $result ),
			"GEMP decision for $user: $result [" . trim( preg_replace( '/^.*wiki-auth: /', '', $line ) ) . ']' );
	}

	public function execute() {
		$this->seed = json_decode( file_get_contents( $this->getOption( 'seed' ) ), true );
		$this->gempLog = $this->getOption( 'gemp-log' );
		$this->ip = $this->getOption( 'ip' );
		$req = new GempAuthE2EProxyRequest();
		$req->setHeader( 'X-Forwarded-For', $this->ip );
		RequestContext::getMain()->setRequest( $req );
		$this->check( RequestContext::getMain()->getRequest()->getIP() === $this->ip,
			"wiki resolves client IP {$this->ip} through trusted proxy 172.18.0.1" );

		$case = $this->getOption( 'case' );
		$this->output( "case $case\n" );
		switch ( $case ) {
			case 'setup':
				// A second local-only wiki account (no GEMP link), next to the installer's Admin.
				$u = \MediaWiki\User\User::createNew( 'Lobot' );
				$this->check( $u !== null && $u->isRegistered(), 'created local-only wiki account Lobot' );
				break;
			case 'ok':
				$res = $this->login( 'E2ECANON', self::PASSWORD );
				$this->check( $res->status === AuthenticationResponse::PASS && $res->username === 'E2eCanon',
					"OK login typed E2ECANON -> PASS as E2eCanon (got {$res->status} {$res->username})" );
				$this->check( $this->registered( 'E2eCanon' ), 'wiki account E2eCanon auto-created' );
				$this->check( $this->linkedId( 'E2eCanon' ) === (string)$this->seed['canon_id'],
					'linked gempauth-id=' . $this->seed['canon_id'] . ' (got ' . var_export( $this->linkedId( 'E2eCanon' ), true ) . ')' );
				$this->check( !$this->registered( 'E2ECANON' ), 'no account under the typed name E2ECANON' );
				$this->expectGemp( 'E2ECANON', 'ok' );
				break;
			case 'ok-again':
				$res = $this->login( 'e2eCanon', self::PASSWORD );
				$this->check( $res->status === AuthenticationResponse::PASS && $res->username === 'E2eCanon',
					"second login (linked) -> PASS as E2eCanon (got {$res->status})" );
				$this->expectGemp( 'e2eCanon', 'ok' );
				break;
			case 'wrong':
				$this->expectFail( $this->login( 'e2eCanon', 'Wrong-Horse-9' ), 'wrongpassword', 'wrong password' );
				$this->expectGemp( 'e2eCanon', 'invalid_credentials' );
				break;
			case 'blank':
				$this->expectFail( $this->login( 'e2eblank', self::PASSWORD ), 'wrongpassword', 'blank stored hash, old password' );
				$this->expectGemp( 'e2eblank', 'invalid_credentials' );
				$this->expectFail( $this->login( 'e2eblank', 'anything-at-all' ), 'wrongpassword', 'blank stored hash, any password' );
				$this->expectGemp( 'e2eblank', 'invalid_credentials' );
				$this->check( !$this->registered( 'E2eblank' ), 'no wiki account for e2eblank' );
				break;
			case 'reset':
				$res = $this->login( 'e2ereset', $this->seed['reset_code'] );
				$this->expectFail( $res, 'gempauth-reset-required', 'one-time reset code' );
				$text = $res->message ? $res->message->inLanguage( 'en' )->text() : '';
				$this->check( str_contains( $text, 'Finish the reset on' ), "message: \"$text\"" );
				$this->expectGemp( 'e2ereset', 'reset_required' );
				$this->check( !$this->registered( 'E2ereset' ), 'no login and no wiki account for e2ereset' );
				$this->expectFail( $this->login( 'e2ereset', self::PASSWORD ), 'wrongpassword', 'old password after admin reset' );
				$this->expectGemp( 'e2ereset', 'invalid_credentials' );
				break;
			case 'admin-variant':
				$before = count( $this->gempLines() );
				$this->expectFail( $this->login( 'ADMIN', 'admin-local-pw' ), 'gempauth-local-case-variant', 'typed ADMIN (local-only Admin)' );
				$this->expectFail( $this->login( 'aDMIN', 'admin-local-pw' ), 'gempauth-local-case-variant', 'typed aDMIN' );
				// GEMP really has LOBOT with this password, so only the wiki-side check stops it.
				$this->expectFail( $this->login( 'LOBOT', 'Gemp-Admin-pw1' ), 'gempauth-local-case-variant',
					'typed LOBOT (local-only Lobot; GEMP account LOBOT would accept this password)' );
				usleep( 300000 );
				$after = $this->gempLines();
				$this->check( count( $after ) === $before, "no GEMP call (GEMP decision lines $before -> " . count( $after ) . ')' );
				$this->check( $this->linkedId( 'Admin' ) === null && $this->linkedId( 'Lobot' ) === null, 'local Admin and Lobot still unlinked' );
				$this->check( !$this->registered( 'ADMIN' ) && !$this->registered( 'LOBOT' ), 'no ADMIN/LOBOT wiki accounts created' );
				break;
			case 'throttle-authservice':
				$this->expectFail( $this->login( 'e2ethrot', self::PASSWORD ), 'gempauth-throttled',
					'correct password on an account locked by 10 failed game logins (AuthService THROTTLED)' );
				$this->expectGemp( 'e2ethrot', 'throttled' );
				break;
			case 'throttle-endpoint':
				for ( $i = 0; $i < 10; $i++ ) {
					$r = $this->login( 'e2eburst', "Wrong-pass-$i" );
					if ( $r->status !== AuthenticationResponse::FAIL ) {
						$this->check( false, "burst attempt $i should fail" );
					}
				}
				$this->expectFail( $this->login( 'e2eburst', self::PASSWORD ), 'gempauth-throttled',
					'11th attempt (correct password) after 10 failures: endpoint 429' );
				$this->expectGemp( 'e2eburst', 'rate limited' );
				break;
			case 'legacy':
				$res = $this->login( 'e2elegacy', self::PASSWORD );
				$this->check( $res->status === AuthenticationResponse::PASS && $res->username === 'E2elegacy',
					"legacy SHA-256 account -> PASS as E2elegacy (got {$res->status})" );
				$this->expectGemp( 'e2elegacy', 'ok' );
				break;
			default:
				$this->fatalError( "unknown case $case" );
		}
		if ( $this->failures > 0 ) {
			$this->fatalError( "case $case: {$this->failures} check(s) failed" );
		}
	}
}

$maintClass = GempAuthE2E::class;
return $maintClass;
