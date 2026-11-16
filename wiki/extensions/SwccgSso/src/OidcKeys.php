<?php
namespace MediaWiki\Extension\SwccgSso;

use MediaWiki\Http\HttpRequestFactory;
use WANObjectCache;

/**
 * Discovery, signing keys and RS256 checks for tokens from the sign-in service (#507).
 * Same rules as Special:SwccgSignIn: endpoints must sit under the issuer; keys come from its jwks_uri.
 */
class OidcKeys {
	public function __construct(
		private HttpRequestFactory $http,
		private WANObjectCache $cache
	) {
	}

	public function discovery( string $issuer ): ?array {
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

	/**
	 * Checks an RS256 JWT's signature against the issuer's published keys (refetched once
	 * for an unknown kid). Returns [header, claims] or null. Claims are not checked here.
	 */
	public function verifySignature( string $jwt, string $issuer ): ?array {
		$parts = explode( '.', $jwt );
		if ( count( $parts ) !== 3 || strlen( $jwt ) > 16384 ) {
			return null;
		}
		$h = json_decode( self::b64ud( $parts[0] ), true );
		$c = json_decode( self::b64ud( $parts[1] ), true );
		if ( !is_array( $h ) || !is_array( $c ) || ( $h['alg'] ?? '' ) !== 'RS256' ) {
			return null;
		}
		$disc = $this->discovery( $issuer );
		if ( !$disc ) {
			return null;
		}
		$pem = $this->jwkPem( $disc['jwks_uri'], (string)( $h['kid'] ?? '' ) );
		if ( !$pem || openssl_verify( $parts[0] . '.' . $parts[1], self::b64ud( $parts[2] ), $pem, OPENSSL_ALGO_SHA256 ) !== 1 ) {
			return null;
		}
		return [ $h, $c ];
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

	public static function b64ud( string $s ): string {
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
