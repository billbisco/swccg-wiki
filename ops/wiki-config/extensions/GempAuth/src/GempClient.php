<?php

namespace MediaWiki\Extension\GempAuth;

use MediaWiki\Http\HttpRequestFactory;
use MediaWiki\Logger\LoggerFactory;

/**
 * Client for GEMP's private POST /internal/v1/verify (contract: docs/wiki-auth-api.md, "GEMP-AUTH-V1").
 * Signs every request with HMAC-SHA256 and checks GEMP's signed response. Never logs the password.
 */
class GempClient {
	public const OK = 'ok';
	public const INVALID = 'invalid_credentials';
	/** The password was a valid GEMP one-time reset code: finish the reset on GEMP. Never a login. */
	public const RESET = 'reset_required';
	public const BANNED = 'banned';
	public const TEMP_BANNED = 'temp_banned';
	public const DEACTIVATED = 'deactivated';
	/** GEMP's AuthService throttle (200) or this endpoint's second-layer limit (429). */
	public const THROTTLED = 'throttled';
	public const UNAVAILABLE = 'unavailable';

	/** @var callable():int */
	private $clock;
	/** @var callable():string */
	private $nonceFactory;

	public function __construct(
		private HttpRequestFactory $http,
		private string $endpoint,
		private string $secret,
		private int $timeout = 5,
		?callable $clock = null,
		?callable $nonceFactory = null
	) {
		$this->clock = $clock ?? 'time';
		$this->nonceFactory = $nonceFactory ?? static fn () => bin2hex( random_bytes( 16 ) );
	}

	public function isConfigured(): bool {
		return $this->endpoint !== '' && strlen( $this->secret ) >= 32;
	}

	public static function requestCanonical( string $ts, string $nonce, string $method, string $path, string $body ): string {
		return "GEMP-AUTH-V1\n$ts\n$nonce\n$method\n$path\n" . hash( 'sha256', $body );
	}

	public static function responseCanonical( string $nonce, int $status, string $body ): string {
		return "GEMP-AUTH-V1-RESP\n$nonce\n$status\n" . hash( 'sha256', $body );
	}

	public function sign( string $canonical ): string {
		return 'v1=' . hash_hmac( 'sha256', $canonical, $this->secret );
	}

	/**
	 * @param string $clientIp the end user's IP as MediaWiki resolved it through the trusted proxy
	 *   ($wgCdnServersNoPurge). Sent inside the signed body, so it is covered by the HMAC; GEMP uses it
	 *   for its login throttle instead of the docker peer address.
	 * @return array{status:string, user?:array{id:int,name:string,admin:bool}, until?:int, retry_after?:int}
	 */
	public function verify( string $username, string $password, string $clientIp ): array {
		$log = LoggerFactory::getInstance( 'GempAuth' );
		if ( !$this->isConfigured() || $clientIp === '' ) {
			return [ 'status' => self::UNAVAILABLE ];
		}
		$payload = [ 'username' => $username, 'password' => $password, 'client_ip' => $clientIp ];
		$body = json_encode( $payload, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
		$path = (string)parse_url( $this->endpoint, PHP_URL_PATH );
		$ts = (string)( $this->clock )();
		$nonce = ( $this->nonceFactory )();

		$req = $this->http->create( $this->endpoint, [
			'method' => 'POST',
			'postData' => $body,
			'timeout' => $this->timeout,
			'connectTimeout' => 2,
			'followRedirects' => false,
			'proxy' => false,
		], __METHOD__ );
		$req->setHeader( 'Content-Type', 'application/json' );
		$req->setHeader( 'X-Gemp-Timestamp', $ts );
		$req->setHeader( 'X-Gemp-Nonce', $nonce );
		$req->setHeader( 'X-Gemp-Signature', $this->sign( self::requestCanonical( $ts, $nonce, 'POST', $path, $body ) ) );
		$req->execute();

		$code = (int)$req->getStatus();
		$content = (string)$req->getContent();
		$sig = (string)$req->getResponseHeader( 'x-gemp-signature' );
		if ( !hash_equals( $this->sign( self::responseCanonical( $nonce, $code, $content ) ), $sig ) ) {
			$log->warning( 'GEMP verify: unsigned or badly signed response (HTTP {code})', [ 'code' => $code ] );
			return [ 'status' => self::UNAVAILABLE ];
		}
		$data = json_decode( $content, true );
		if ( !is_array( $data ) ) {
			return [ 'status' => self::UNAVAILABLE ];
		}
		if ( $code === 429 ) {
			return [ 'status' => self::THROTTLED, 'retry_after' => (int)( $data['retry_after'] ?? 300 ) ];
		}
		if ( $code !== 200 ) {
			$log->warning( 'GEMP verify: HTTP {code} {error}', [ 'code' => $code, 'error' => $data['error'] ?? '' ] );
			return [ 'status' => self::UNAVAILABLE ];
		}
		if ( ( $data['ok'] ?? false ) === true && isset( $data['user']['id'], $data['user']['name'] ) ) {
			return [ 'status' => self::OK, 'user' => [
				'id' => (int)$data['user']['id'],
				'name' => (string)$data['user']['name'],
				'admin' => (bool)( $data['user']['admin'] ?? false ),
			] ];
		}
		$error = (string)( $data['error'] ?? '' );
		// Anything that is not ok:true is a refusal; unknown codes are treated as unavailable.
		$known = [ self::INVALID, self::RESET, self::BANNED, self::TEMP_BANNED, self::DEACTIVATED, self::THROTTLED ];
		$out = [ 'status' => in_array( $error, $known, true ) ? $error : self::UNAVAILABLE ];
		if ( $error === self::TEMP_BANNED && isset( $data['until'] ) ) {
			$out['until'] = (int)$data['until'];
		}
		if ( $error === self::THROTTLED ) {
			$out['retry_after'] = (int)( $data['retry_after'] ?? 300 );
		}
		return $out;
	}
}
