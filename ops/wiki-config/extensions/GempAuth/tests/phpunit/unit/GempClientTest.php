<?php

namespace MediaWiki\Extension\GempAuth\Tests\Unit;

use MediaWiki\Extension\GempAuth\GempClient;
use MediaWiki\Http\HttpRequestFactory;
use MediaWikiUnitTestCase;
use MWHttpRequest;

/**
 * @covers \MediaWiki\Extension\GempAuth\GempClient
 */
class GempClientTest extends MediaWikiUnitTestCase {
	private const SECRET = '0123456789abcdef0123456789abcdef';
	private const ENDPOINT = 'http://gemp_swccg_app_1:8090/internal/v1/verify';
	private const NONCE = 'abcdefghijklmnop';

	/** Same vector as GEMP's InternalAuthSignerTest: both sides must produce identical bytes. */
	public function testKnownAnswerVectors() {
		$c = new GempClient( $this->createMock( HttpRequestFactory::class ), self::ENDPOINT, self::SECRET );
		$body = '{"username":"Bill","password":"hunter22","client_ip":"203.0.113.7"}';
		$this->assertSame( 'v1=46e1e96f0b78c038fe19bbe9c6fd7214d328d11f5261711b99876c3f7e22abf1',
			$c->sign( GempClient::requestCanonical( '1760000000', self::NONCE, 'POST', '/internal/v1/verify', $body ) ) );
		$this->assertSame( 'v1=bdc04e5d3a97a420aa22a9394c66ae2a5408d52ff1c6aded80ce6bae78c1486a',
			$c->sign( GempClient::responseCanonical( self::NONCE, 200, '{"ok":false,"error":"invalid_credentials"}' ) ) );
	}

	private function client( int $status, string $body, ?string $sig = null, ?array &$sent = null, ?string $secret = null ): GempClient {
		$signer = new GempClient( $this->createMock( HttpRequestFactory::class ), self::ENDPOINT, $secret ?? self::SECRET );
		$sig ??= $signer->sign( GempClient::responseCanonical( self::NONCE, $status, $body ) );
		$req = $this->createMock( MWHttpRequest::class );
		$headers = [];
		$req->method( 'setHeader' )->willReturnCallback( static function ( $k, $v ) use ( &$headers ) {
			$headers[$k] = $v;
		} );
		$req->method( 'getStatus' )->willReturn( $status );
		$req->method( 'getContent' )->willReturn( $body );
		$req->method( 'getResponseHeader' )->willReturn( $sig );
		$factory = $this->createMock( HttpRequestFactory::class );
		$factory->method( 'create' )->willReturnCallback(
			static function ( $url, $options ) use ( $req, &$sent, &$headers ) {
				$sent = [ 'url' => $url, 'options' => $options, 'headers' => &$headers ];
				return $req;
			} );
		return new GempClient( $factory, self::ENDPOINT, self::SECRET, 5,
			static fn () => 1760000000, static fn () => self::NONCE );
	}

	public function testSuccessAndSignedRequest() {
		$sent = null;
		$c = $this->client( 200, '{"ok":true,"user":{"id":42,"name":"bill","admin":false}}', null, $sent );
		$r = $c->verify( 'bill', 'pw-123456', '203.0.113.7' );
		$this->assertSame( 'ok', $r['status'] );
		$this->assertSame( [ 'id' => 42, 'name' => 'bill', 'admin' => false ], $r['user'] );

		$this->assertSame( self::ENDPOINT, $sent['url'] );
		$this->assertSame( 'POST', $sent['options']['method'] );
		$this->assertFalse( $sent['options']['followRedirects'] );
		$body = $sent['options']['postData'];
		$this->assertSame( [ 'username' => 'bill', 'password' => 'pw-123456', 'client_ip' => '203.0.113.7' ], json_decode( $body, true ) );
		$h = $sent['headers'];
		$this->assertSame( '1760000000', $h['X-Gemp-Timestamp'] );
		$this->assertSame( self::NONCE, $h['X-Gemp-Nonce'] );
		$this->assertSame( $c->sign( GempClient::requestCanonical( '1760000000', self::NONCE, 'POST', '/internal/v1/verify', $body ) ),
			$h['X-Gemp-Signature'] );
	}

	public static function provideOutcomes() {
		return [
			'wrong password' => [ 200, '{"ok":false,"error":"invalid_credentials"}', 'invalid_credentials' ],
			'reset' => [ 200, '{"ok":false,"error":"password_reset_required"}', 'password_reset_required' ],
			'banned' => [ 200, '{"ok":false,"error":"banned"}', 'banned' ],
			'temp banned' => [ 200, '{"ok":false,"error":"temp_banned","until":1760003600}', 'temp_banned' ],
			'rate limited' => [ 429, '{"ok":false,"error":"rate_limited","retry_after":30}', 'rate_limited' ],
			'unknown error code' => [ 200, '{"ok":false,"error":"weird"}', 'unavailable' ],
			'server error' => [ 503, '{"ok":false,"error":"unavailable"}', 'unavailable' ],
			'ok without user' => [ 200, '{"ok":true}', 'unavailable' ],
			'not json' => [ 200, '<html>', 'unavailable' ],
		];
	}

	/** @dataProvider provideOutcomes */
	public function testOutcomes( $status, $body, $expected ) {
		$this->assertSame( $expected, $this->client( $status, $body )->verify( 'bill', 'x', null )['status'] );
	}

	public function testRateLimitAndBanDetails() {
		$this->assertSame( 30, $this->client( 429, '{"ok":false,"error":"rate_limited","retry_after":30}' )
			->verify( 'bill', 'x', null )['retry_after'] );
		$this->assertSame( 1760003600, $this->client( 200, '{"ok":false,"error":"temp_banned","until":1760003600}' )
			->verify( 'bill', 'x', null )['until'] );
	}

	public function testRejectsUnsignedOrForgedResponses() {
		$ok = '{"ok":true,"user":{"id":1,"name":"bill"}}';
		$this->assertSame( 'unavailable', $this->client( 200, $ok, '' )->verify( 'bill', 'x', null )['status'] );
		$forged = ( new GempClient( $this->createMock( HttpRequestFactory::class ), self::ENDPOINT, str_repeat( 'z', 32 ) ) )
			->sign( GempClient::responseCanonical( self::NONCE, 200, $ok ) );
		$this->assertSame( 'unavailable', $this->client( 200, $ok, $forged )->verify( 'bill', 'x', null )['status'] );
	}

	public function testNotConfigured() {
		$factory = $this->createNoOpMock( HttpRequestFactory::class );
		$this->assertFalse( ( new GempClient( $factory, '', self::SECRET ) )->isConfigured() );
		$this->assertFalse( ( new GempClient( $factory, self::ENDPOINT, 'short' ) )->isConfigured() );
		$this->assertSame( 'unavailable', ( new GempClient( $factory, self::ENDPOINT, 'short' ) )->verify( 'a', 'b', null )['status'] );
	}
}
