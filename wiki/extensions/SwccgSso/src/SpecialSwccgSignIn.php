<?php
/**
 * Special:SwccgSignIn — OIDC client for the SWCCG sign-in service (#267, #249).
 * The wiki account is found by the ID token's sub, which is the membership id and the wiki user_id
 * (the sign-in service creates the wiki row at the same id). Never by name or email.
 * Local wiki passwords, BotPasswords and API logins are untouched.
 */
namespace MediaWiki\Extension\SwccgSso;

use MediaWiki\Auth\AuthManager;
use MediaWiki\Http\HttpRequestFactory;
use MediaWiki\Logger\LoggerFactory;
use MediaWiki\SpecialPage\SpecialPage;
use MediaWiki\Title\Title;
use MediaWiki\User\UserFactory;
use WANObjectCache;
use Wikimedia\Rdbms\IDBAccessObject;

class SpecialSwccgSignIn extends SpecialPage {
	private const SESSION_KEY = 'swccgsso-flow';
	private const FAIL_KEY = 'swccgsso-failed';
	private const NOROW_ERROR = 'swccgsso_norow';

	/** returnto of the flow being finished, for the failure page. */
	private string $failReturnto = '';

	public function __construct(
		private UserFactory $userFactory,
		private AuthManager $authManager,
		private HttpRequestFactory $http,
		private WANObjectCache $cache
	) {
		parent::__construct( 'SwccgSignIn' );
	}

	public function doesWrites() {
		return true;
	}

	protected function getGroupName() {
		return 'login';
	}

	public function execute( $par ) {
		$this->setHeaders();
		$out = $this->getOutput();
		$out->disallowUserJs();
		$cfg = $this->getConfig();
		$issuer = rtrim( (string)$cfg->get( 'SwccgSsoIssuer' ), '/' );
		if ( $issuer === '' || $cfg->get( 'SwccgSsoClientSecret' ) === '' || $cfg->get( 'SwccgSsoRedirectUri' ) === '' ) {
			$out->addWikiMsg( 'swccgsso-disabled' );
			return;
		}
		$req = $this->getRequest();
		if ( $req->getVal( 'failed' ) !== null ) {
			$this->showFailure();
			return;
		}
		if ( $req->getVal( 'error' ) === self::NOROW_ERROR && $req->getVal( 'code' ) === null ) {
			// #516: landing after a sign-in that found no wiki row. Coming through here with an error
			// lets nginx set its 10-minute "checked" marker, so silent sign-in doesn't loop.
			$out->redirect( $this->returnUrl( (string)$req->getVal( 'returnto', '' ) ) );
			return;
		}
		if ( $req->getVal( 'code' ) !== null || $req->getVal( 'error' ) !== null ) {
			$this->callback( $issuer );
			return;
		}
		if ( $this->getUser()->isRegistered() ) {
			$out->redirect( $this->returnUrl( $req->getVal( 'returnto', '' ) ) );
			return;
		}
		$this->start( $issuer );
	}

	private function start( string $issuer ): void {
		$req = $this->getRequest();
		$disc = $this->discovery( $issuer );
		if ( !$disc ) {
			$this->fail( 'the sign-in service is unavailable' );
			return;
		}
		$state = self::b64u( random_bytes( 24 ) );
		$nonce = self::b64u( random_bytes( 24 ) );
		$verifier = self::b64u( random_bytes( 48 ) );
		$session = $req->getSession();
		$session->persist();
		$session->set( self::SESSION_KEY, [
			'state' => $state, 'nonce' => $nonce, 'verifier' => $verifier,
			'returnto' => (string)$req->getVal( 'returnto', '' ), 'at' => time(),
		] );
		$session->save();
		$q = [
			'response_type' => 'code',
			'client_id' => $this->getConfig()->get( 'SwccgSsoClientId' ),
			'redirect_uri' => $this->getConfig()->get( 'SwccgSsoRedirectUri' ),
			'scope' => 'openid profile',
			'state' => $state,
			'nonce' => $nonce,
			'code_challenge' => self::b64u( hash( 'sha256', $verifier, true ) ),
			'code_challenge_method' => 'S256',
		];
		$this->getOutput()->redirect( $disc['authorization_endpoint'] . '?' . http_build_query( $q, '', '&', PHP_QUERY_RFC3986 ) );
	}

	private function callback( string $issuer ): void {
		$req = $this->getRequest();
		$session = $req->getSession();
		$flow = $session->get( self::SESSION_KEY );
		$session->remove( self::SESSION_KEY );
		$this->failReturnto = is_array( $flow ) ? (string)( $flow['returnto'] ?? '' ) : '';
		if ( !is_array( $flow ) || !hash_equals( (string)$flow['state'], (string)$req->getVal( 'state', '' ) )
			|| time() - (int)$flow['at'] > 900 ) {
			$this->logRefused( 'bad_state' );
			$this->fail( 'the sign-in request expired or did not match' );
			return;
		}
		if ( $req->getVal( 'error' ) !== null ) {
			$silent = in_array( $req->getVal( 'error' ), [ 'login_required', 'interaction_required', 'consent_required', 'account_selection_required' ], true );
			$this->logRefused( ( $silent ? 'silent:' : 'error:' ) . (string)$req->getVal( 'error' ) );
			if ( in_array( $req->getVal( 'error' ), [ 'login_required', 'interaction_required', 'consent_required', 'account_selection_required' ], true ) ) {
				// silent (prompt=none) check found no usable site session: go back quietly
				$this->getOutput()->redirect( $this->returnUrl( (string)$flow['returnto'] ) );
				return;
			}
			$this->fail( 'the sign-in was cancelled' );
			return;
		}
		$iss = $req->getVal( 'iss' );
		if ( $iss !== null && rtrim( $iss, '/' ) !== $issuer ) {
			$this->logRefused( 'iss_mismatch' );
			$this->fail( 'unexpected issuer' );
			return;
		}
		$disc = $this->discovery( $issuer );
		if ( !$disc ) {
			$this->logRefused( 'discovery' );
			$this->fail( 'the sign-in service is unavailable' );
			return;
		}
		$cfg = $this->getConfig();
		$cid = (string)$cfg->get( 'SwccgSsoClientId' );
		$tr = $this->http->create( $disc['token_endpoint'], [
			'method' => 'POST', 'timeout' => 10,
			'postData' => http_build_query( [
				'grant_type' => 'authorization_code',
				'code' => (string)$req->getVal( 'code' ),
				'redirect_uri' => (string)$cfg->get( 'SwccgSsoRedirectUri' ),
				'code_verifier' => (string)$flow['verifier'],
			] ),
		], __METHOD__ );
		$tr->setHeader( 'Authorization', 'Basic ' . base64_encode( rawurlencode( $cid ) . ':' . rawurlencode( (string)$cfg->get( 'SwccgSsoClientSecret' ) ) ) );
		$tr->setHeader( 'Content-Type', 'application/x-www-form-urlencoded' );
		$st = $tr->execute();
		$tok = json_decode( (string)$tr->getContent(), true );
		if ( !$st->isOK() || !is_array( $tok ) || empty( $tok['id_token'] ) ) {
			$this->log()->warning( 'token exchange failed: {status}', [ 'status' => $tr->getStatus() ] );
			$this->logRefused( 'token_exchange' );
			$this->fail( 'the code could not be exchanged' );
			return;
		}
		$claims = $this->verifyIdToken( (string)$tok['id_token'], $disc, $issuer, $cid, (string)$flow['nonce'] );
		if ( !$claims ) {
			$this->logRefused( 'id_token' );
			$this->fail( 'the sign-in token was not valid' );
			return;
		}
		$id = (int)$claims['sub'];
		$user = $this->userFactory->newFromId( $id );
		$user->load();
		if ( !$user->isRegistered() ) {
			// #516: the sign-in service may have just made the row; the shared user cache can still
			// hold "no such user" from an earlier try, so read the database and drop the stale entry.
			$user = $this->userFactory->newFromId( $id );
			$user->load( IDBAccessObject::READ_LATEST );
			if ( $user->isRegistered() ) {
				$user->clearSharedCache( 'refresh' );
			}
		}
		if ( self::faultNoRow( $id ) ) {
			$user = $this->userFactory->newAnonymous(); // #516 test-only fault switch (off unless the file exists)
		}
		if ( !$user->isRegistered() || $user->getId() !== $id ) {
			// #516: the sign-in service makes the missing wiki row when the wiki asks for a token.
			// If there is still none, go back quietly to the page asked for, signed out.
			$this->log()->warning( 'no wiki row for membership {id} after sign-in; returned signed out', [ 'id' => $id ] );
			$this->logRefused( 'no_wiki_row', $claims['swccg_tid'] ?? null );
			$q = [ 'error' => self::NOROW_ERROR ];
			if ( (string)$flow['returnto'] !== '' ) {
				$q['returnto'] = (string)$flow['returnto'];
			}
			// the pretty path (not index.php?title=) so nginx's Special:SwccgSignIn location sets the marker
			$this->getOutput()->redirect( $this->getPageTitle()->getFullURL() . '?' . http_build_query( $q, '', '&', PHP_QUERY_RFC3986 ) );
			return;
		}
		if ( isset( $claims['preferred_username'] ) && $claims['preferred_username'] !== $user->getName() ) {
			$this->log()->info( 'membership {id}: site name differs from wiki name', [ 'id' => $id ] );
		}
		$this->logIn( $user );
		$session = $this->getRequest()->getSession();
		$session->set( 'swccgsso-sid-tail', Hooks::siteSessionTail( $this->getRequest() ) );
		$session->set( 'swccgsso-id-token', (string)$tok['id_token'] );
		if ( isset( $claims['sid'] ) && is_string( $claims['sid'] ) && $claims['sid'] !== '' ) {
			$session->set( 'swccgsso-sid', $claims['sid'] ); // #507 back-channel match
		}
		$session->save();
		$this->log()->info( 'membership {id} signed in to the wiki', [ 'id' => $id ] );
		// #631: the tracking id from swccg-login and this request's id from nginx.
		SigninLog::ok( $id, $claims['swccg_tid'] ?? null, (string)$req->getVal( 'state', '' ), (string)$req->getHeader( 'X-Request-Id' ) );
		$this->getOutput()->redirect( $this->returnUrl( (string)$flow['returnto'] ) );
	}

	/** Same steps as AuthManager::setSessionDataForUser() (private in 1.43). */
	private function logIn( $user ): void {
		$session = $this->getRequest()->getSession();
		$delay = $session->delaySave();
		$session->resetId();
		$session->resetAllTokens();
		if ( $session->canSetUser() ) {
			$session->setUser( $user );
		}
		$session->setRememberUser( false );
		$session->set( 'AuthManager:lastAuthId', $user->getId() );
		$session->set( 'AuthManager:lastAuthTimestamp', time() );
		$session->persist();
		\Wikimedia\ScopedCallback::consume( $delay );
		$this->getHookContainer()->run( 'UserLoggedIn', [ $user ] );
	}

	/** @return array|null claims */
	private function verifyIdToken( string $jwt, array $disc, string $issuer, string $cid, string $nonce ): ?array {
		$parts = explode( '.', $jwt );
		if ( count( $parts ) !== 3 ) {
			return null;
		}
		$h = json_decode( self::b64ud( $parts[0] ), true );
		$c = json_decode( self::b64ud( $parts[1] ), true );
		if ( !is_array( $h ) || !is_array( $c ) || ( $h['alg'] ?? '' ) !== 'RS256' ) {
			return null;
		}
		$pem = $this->jwkPem( $disc['jwks_uri'], (string)( $h['kid'] ?? '' ) );
		if ( !$pem || openssl_verify( $parts[0] . '.' . $parts[1], self::b64ud( $parts[2] ), $pem, OPENSSL_ALGO_SHA256 ) !== 1 ) {
			return null;
		}
		$aud = (array)( $c['aud'] ?? [] );
		$now = time();
		if ( rtrim( (string)( $c['iss'] ?? '' ), '/' ) !== $issuer || !in_array( $cid, $aud, true )
			|| (int)( $c['exp'] ?? 0 ) < $now - 60 || (int)( $c['iat'] ?? 0 ) > $now + 300
			|| !hash_equals( $nonce, (string)( $c['nonce'] ?? '' ) )
			|| !preg_match( '/^[1-9][0-9]{0,9}$/', (string)( $c['sub'] ?? '' ) ) ) {
			return null;
		}
		return $c;
	}

	private function jwkPem( string $uri, string $kid ): ?string {
		foreach ( [ false, true ] as $fresh ) {
			$key = $this->cache->makeKey( 'swccgsso-jwks', md5( $uri ) );
			if ( $fresh ) {
				$this->cache->delete( $key );
			}
			$jwks = $this->cache->getWithSetCallback( $key, 3600, function () use ( $uri ) {
				$j = json_decode( (string)$this->http->get( $uri, [ 'timeout' => 10 ], __METHOD__ ), true );
				return is_array( $j ) && isset( $j['keys'] ) ? $j : false;
			} );
			foreach ( ( $jwks['keys'] ?? [] ) as $k ) {
				if ( ( $k['kty'] ?? '' ) === 'RSA' && ( $kid === '' || ( $k['kid'] ?? '' ) === $kid ) ) {
					return self::rsaPem( self::b64ud( $k['n'] ), self::b64ud( $k['e'] ) );
				}
			}
		}
		return null;
	}

	private function discovery( string $issuer ): ?array {
		$d = $this->cache->getWithSetCallback(
			$this->cache->makeKey( 'swccgsso-disco', md5( $issuer ) ), 600,
			function () use ( $issuer ) {
				$j = json_decode( (string)$this->http->get( $issuer . '/.well-known/openid-configuration', [ 'timeout' => 10 ], __METHOD__ ), true );
				return is_array( $j ) && rtrim( (string)( $j['issuer'] ?? '' ), '/' ) === $issuer ? $j : false;
			}
		);
		foreach ( [ 'authorization_endpoint', 'token_endpoint', 'jwks_uri' ] as $k ) {
			if ( !is_array( $d ) || !str_starts_with( (string)( $d[$k] ?? '' ), $issuer . '/' ) ) {
				return null;
			}
		}
		return $d;
	}

	private function returnUrl( string $returnto ): string {
		$t = $returnto !== '' ? Title::newFromText( $returnto ) : null;
		if ( !$t || $t->isExternal() || $t->isSpecial( 'Userlogout' ) || $t->isSpecial( 'SwccgSignIn' ) ) {
			$t = Title::newMainPage();
		}
		return $t->getFullURL();
	}

	/**
	 * #516 test-only fault switch, off by default: membership ids listed one per line in
	 * extensions/SwccgSso/.fault-no-row are treated as having no wiki row. Delete the file to turn it off.
	 */
	private static function faultNoRow( int $id ): bool {
		$f = dirname( __DIR__ ) . '/.fault-no-row';
		if ( !is_file( $f ) ) {
			return false;
		}
		$ids = preg_split( '/\s+/', trim( (string)file_get_contents( $f ) ) );
		return in_array( (string)$id, $ids, true );
	}

	/**
	 * A failed sign-in (#511): when the request carries the service's answer (code, state or error),
	 * keep the reason in the session and redirect to a clean URL, so no used code or state stays in
	 * the address bar, the history or the page's links. The clean page shows what happened and what to do.
	 */
	private function fail( string $why ): void {
		$req = $this->getRequest();
		if ( $req->getVal( 'code' ) === null && $req->getVal( 'state' ) === null && $req->getVal( 'error' ) === null ) {
			$this->getOutput()->addWikiMsg( 'swccgsso-error', $why );
			$this->addNextSteps( '' );
			return;
		}
		$session = $req->getSession();
		$session->persist();
		$session->set( self::FAIL_KEY, [ 'why' => $why, 'returnto' => $this->failReturnto ] );
		$session->save();
		$this->getOutput()->redirect( $this->getPageTitle()->getFullURL( [ 'failed' => 1 ] ) );
	}

	/** The clean page a failed sign-in lands on. */
	private function showFailure(): void {
		$session = $this->getRequest()->getSession();
		$f = $session->get( self::FAIL_KEY );
		$session->remove( self::FAIL_KEY );
		$why = is_array( $f ) && is_string( $f['why'] ?? null ) ? $f['why'] : 'the sign-in did not finish';
		$returnto = is_array( $f ) && is_string( $f['returnto'] ?? null ) ? $f['returnto'] : '';
		$this->getOutput()->addWikiMsg( 'swccgsso-error', $why );
		$this->addNextSteps( $returnto );
	}

	/** "Try again" (a fresh sign-in back to the same page) and a link back to that page. */
	private function addNextSteps( string $returnto ): void {
		$q = [];
		$t = $returnto !== '' ? Title::newFromText( $returnto ) : null;
		if ( $t && !$t->isExternal() && !$t->isSpecial( 'Userlogout' ) && !$t->isSpecial( 'SwccgSignIn' ) ) {
			$q['returnto'] = $t->getPrefixedText();
		}
		$this->getOutput()->addWikiMsg( 'swccgsso-error-next',
			$this->getPageTitle()->getFullURL( $q ), $this->returnUrl( $returnto ) );
	}

	/** #631: why a callback was refused, with the state fingerprint and nginx's request id (no personal data). */
	private function logRefused( string $reason, $tid = null ): void {
		$req = $this->getRequest();
		SigninLog::refused( $reason, $tid, (string)$req->getVal( 'state', '' ), (string)$req->getHeader( 'X-Request-Id' ) );
	}

	private function log() {
		return LoggerFactory::getInstance( 'SwccgSso' );
	}

	private static function b64u( string $b ): string {
		return rtrim( strtr( base64_encode( $b ), '+/', '-_' ), '=' );
	}

	private static function b64ud( string $s ): string {
		return (string)base64_decode( strtr( $s, '-_', '+/' ) . str_repeat( '=', ( 4 - strlen( $s ) % 4 ) % 4 ) );
	}

	private static function derLen( int $n ): string {
		if ( $n < 128 ) {
			return chr( $n );
		}
		$b = ltrim( pack( 'N', $n ), "\0" );
		return chr( 0x80 | strlen( $b ) ) . $b;
	}

	private static function derInt( string $x ): string {
		$x = ltrim( $x, "\0" );
		if ( $x === '' || ord( $x[0] ) > 0x7f ) {
			$x = "\0" . $x;
		}
		return "\x02" . self::derLen( strlen( $x ) ) . $x;
	}

	private static function rsaPem( string $n, string $e ): string {
		$rsa = self::derInt( $n ) . self::derInt( $e );
		$rsa = "\x30" . self::derLen( strlen( $rsa ) ) . $rsa;
		$bit = "\x03" . self::derLen( strlen( $rsa ) + 1 ) . "\0" . $rsa;
		$alg = "\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01\x01\x01\x05\x00";
		$spki = "\x30" . self::derLen( strlen( $alg . $bit ) ) . $alg . $bit;
		return "-----BEGIN PUBLIC KEY-----\n" . chunk_split( base64_encode( $spki ), 64, "\n" ) . "-----END PUBLIC KEY-----\n";
	}
}
