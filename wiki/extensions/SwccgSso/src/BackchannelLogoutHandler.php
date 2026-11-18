<?php
namespace MediaWiki\Extension\SwccgSso;

use MediaWiki\Config\Config;
use MediaWiki\Http\HttpRequestFactory;
use MediaWiki\Logger\LoggerFactory;
use MediaWiki\Rest\Handler;
use MediaWiki\Rest\RequestInterface;
use MediaWiki\Rest\Response;
use MediaWiki\Session\SessionManager;
use MediaWiki\User\UserFactory;
use WANObjectCache;
use Wikimedia\ObjectCache\BagOStuff;

/**
 * POST rest.php/swccgsso/v1/backchannel-logout (#507): OpenID Connect Back-Channel Logout 1.0.
 * The sign-in service posts logout_token here when a site session ends (sign-out, reset, block,
 * close). A token with sid ends the wiki sessions started from that site session; a token without
 * sid ends every wiki session of the account. Anything that doesn't check out gets 400 and ends nothing.
 */
class BackchannelLogoutHandler extends Handler {
	public const EVENT = 'http://schemas.openid.net/event/backchannel-logout';
	/** How long a revoked sid is remembered: as long as a wiki session can live. */
	private const SID_TTL = 400 * 86400; // #632 was 180 days (Alpha7 OK)

	public function __construct(
		private Config $config,
		private HttpRequestFactory $http,
		private WANObjectCache $cache,
		private BagOStuff $stash,
		private UserFactory $userFactory
	) {
	}

	public function needsWriteAccess() {
		return false; // no wiki content is written
	}

	public function getSupportedRequestTypes(): array {
		return [ RequestInterface::FORM_URLENCODED_CONTENT_TYPE ];
	}

	public function execute() {
		$issuer = rtrim( (string)$this->config->get( 'SwccgSsoIssuer' ), '/' );
		if ( $issuer === '' ) {
			return $this->reply( 400, 'disabled' );
		}
		$tok = $this->getRequest()->getPostParams()['logout_token'] ?? null;
		if ( !is_string( $tok ) || $tok === '' ) {
			return $this->reply( 400, 'missing logout_token' );
		}
		$v = ( new OidcKeys( $this->http, $this->cache ) )->verifySignature( $tok, $issuer );
		if ( !$v ) {
			return $this->reply( 400, 'bad signature' );
		}
		[ , $c ] = $v;
		$why = self::claimsProblem( $c, $issuer, (string)$this->config->get( 'SwccgSsoClientId' ), time() );
		if ( $why !== null ) {
			return $this->reply( 400, $why );
		}
		// jti seen before? add() is atomic and fails when the key exists.
		$exp = (int)$c['exp'];
		$jtiKey = $this->stash->makeKey( 'swccgsso-bcl-jti', hash( 'sha256', (string)$c['jti'] ) );
		if ( !$this->stash->add( $jtiKey, 1, max( 300, $exp - time() + 600 ) ) ) {
			return $this->reply( 400, 'replayed' );
		}
		$sub = isset( $c['sub'] ) ? (string)$c['sub'] : '';
		$sid = isset( $c['sid'] ) ? (string)$c['sid'] : '';
		if ( $sid !== '' ) {
			$this->stash->set( self::sidKey( $this->stash, $sid ), $sub === '' ? '?' : $sub, self::SID_TTL );
			$this->log()->info( 'back-channel sign-out of site session for {id}', [ 'id' => $sub ] );
		} else {
			$user = $this->userFactory->newFromId( (int)$sub );
			$user->load();
			if ( $user->isRegistered() ) {
				SessionManager::singleton()->invalidateSessionsForUser( $user );
			}
			$this->log()->info( 'back-channel sign-out everywhere for {id}', [ 'id' => $sub ] );
		}
		$r = $this->getResponseFactory()->create();
		$r->setStatus( 200 );
		$r->setHeader( 'Cache-Control', 'no-store' );
		return $r;
	}

	/** Stash key for a revoked site session; Hooks checks it on every signed-in request. */
	public static function sidKey( BagOStuff $stash, string $sid ): string {
		return $stash->makeKey( 'swccgsso-bcl-sid', hash( 'sha256', $sid ) );
	}

	/**
	 * Back-Channel Logout 1.0 section 2.6 checks (signature already checked). Returns why the
	 * token is refused, or null when it is fine.
	 */
	public static function claimsProblem( array $c, string $issuer, string $clientId, int $now ): ?string {
		if ( rtrim( (string)( $c['iss'] ?? '' ), '/' ) !== $issuer ) {
			return 'wrong issuer';
		}
		if ( !in_array( $clientId, (array)( $c['aud'] ?? [] ), true ) ) {
			return 'wrong audience';
		}
		if ( !isset( $c['iat'] ) || !is_int( $c['iat'] ) || $c['iat'] > $now + 300 || $c['iat'] < $now - 600 ) {
			return 'bad iat';
		}
		if ( !isset( $c['exp'] ) || !is_int( $c['exp'] ) || $c['exp'] < $now - 60 ) {
			return 'expired';
		}
		if ( !isset( $c['events'] ) || !is_array( $c['events'] ) || !array_key_exists( self::EVENT, $c['events'] )
			|| !is_array( $c['events'][self::EVENT] ) ) {
			return 'no back-channel event';
		}
		if ( array_key_exists( 'nonce', $c ) ) {
			return 'nonce present';
		}
		if ( !isset( $c['jti'] ) || !is_string( $c['jti'] ) || $c['jti'] === '' ) {
			return 'no jti';
		}
		$sub = $c['sub'] ?? null;
		$sid = $c['sid'] ?? null;
		if ( $sub !== null && !preg_match( '/^[1-9][0-9]{0,9}$/', (string)$sub ) ) {
			return 'bad sub';
		}
		if ( $sid !== null && ( !is_string( $sid ) || $sid === '' || strlen( $sid ) > 255 ) ) {
			return 'bad sid';
		}
		if ( $sub === null && $sid === null ) {
			return 'no sub or sid';
		}
		return null;
	}

	private function reply( int $status, string $why ) {
		$this->log()->info( 'back-channel token refused: {why}', [ 'why' => $why ] );
		$r = $this->getResponseFactory()->createJson( [ 'error' => 'invalid_request' ] );
		$r->setStatus( $status );
		$r->setHeader( 'Cache-Control', 'no-store' );
		return $r;
	}

	private function log() {
		return LoggerFactory::getInstance( 'SwccgSso' );
	}
}
