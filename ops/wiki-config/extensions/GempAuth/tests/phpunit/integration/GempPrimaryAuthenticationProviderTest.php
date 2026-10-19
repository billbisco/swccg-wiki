<?php

namespace MediaWiki\Extension\GempAuth\Tests\Integration;

use MediaWiki\Auth\AuthenticationResponse;
use MediaWiki\Auth\AuthManager;
use MediaWiki\Auth\PasswordAuthenticationRequest;
use MediaWiki\Extension\GempAuth\GempPrimaryAuthenticationProvider;
use MediaWiki\Request\FauxRequest;
use MediaWiki\Context\RequestContext;
use MediaWikiIntegrationTestCase;

/**
 * @group Database
 * @covers \MediaWiki\Extension\GempAuth\GempPrimaryAuthenticationProvider
 */
class GempPrimaryAuthenticationProviderTest extends MediaWikiIntegrationTestCase {
	private FakeGempClient $gemp;

	protected function setUp(): void {
		parent::setUp();
		require_once __DIR__ . '/FakeGempClient.php';
		$this->gemp = new FakeGempClient();
		$this->setService( 'GempAuth.Client', $this->gemp );
		// The core test bootstrap replaces $wgAuthManagerConfig with core-only providers; put the
		// shipped extension.json GempAuth spec back between TemporaryPassword and LocalPassword.
		$auto = $this->getConfVar( 'AuthManagerAutoConfig' );
		$gempSpec = $auto['primaryauth'][GempPrimaryAuthenticationProvider::class];
		$core = $this->getConfVar( 'AuthManagerConfig' );
		$core['primaryauth'][0]['sort'] = 0;
		$core['primaryauth'][1]['sort'] = 100;
		$core['primaryauth'][] = $gempSpec;
		$this->overrideConfigValues( [
			'AuthManagerConfig' => $core,
			'CaptchaTriggers' => [],          // ConfirmEdit's badlogin captcha is tested separately
			'PasswordAttemptThrottle' => [],
			'AccountCreationThrottle' => [],
		] );
		RequestContext::getMain()->setRequest( new FauxRequest() );
		$this->resetServices();
		$this->setService( 'GempAuth.Client', $this->gemp );
	}

	private function login( string $name, string $password ): AuthenticationResponse {
		$manager = $this->getServiceContainer()->getAuthManager();
		$req = new PasswordAuthenticationRequest();
		$req->action = AuthManager::ACTION_LOGIN;
		$req->username = $name;
		$req->password = $password;
		return $manager->beginAuthentication( [ $req ], 'http://localhost/' );
	}

	private function linkedId( string $name ): ?string {
		$user = $this->getServiceContainer()->getUserFactory()->newFromName( $name );
		$v = $this->getServiceContainer()->getUserOptionsLookup()->getOption( $user, GempPrimaryAuthenticationProvider::LINK_OPTION );
		return $v === null || $v === '' ? null : (string)$v;
	}

	public function testFirstGempLoginAutoCreatesAndLinks() {
		$this->gemp->answers['gempnewbie'] = [ 'status' => 'ok', 'user' => [ 'id' => 77, 'name' => 'gempnewbie', 'admin' => false ] ];
		$res = $this->login( 'gempnewbie', 'right-password' );
		$this->assertSame( AuthenticationResponse::PASS, $res->status, (string)( $res->message ? $res->message->plain() : '' ) );
		$this->assertSame( 'Gempnewbie', $res->username );
		$user = $this->getServiceContainer()->getUserFactory()->newFromName( 'Gempnewbie' );
		$this->assertTrue( $user->isRegistered(), 'auto-created' );
		$this->assertSame( '77', $this->linkedId( 'Gempnewbie' ) );
		$this->assertSame( '127.0.0.1', $this->gemp->calls[0][2] );

		// second login: same id -> pass
		$this->assertSame( AuthenticationResponse::PASS, $this->login( 'gempnewbie', 'right-password' )->status );
	}

	public function testLocalAccountsNeverConsultGemp() {
		$testUser = $this->getMutableTestUser();
		$name = $testUser->getUser()->getName();
		$this->assertSame( AuthenticationResponse::PASS, $this->login( $name, $testUser->getPassword() )->status );
		$this->assertSame( AuthenticationResponse::FAIL, $this->login( $name, 'not-the-password' )->status );
		$this->assertSame( [], $this->gemp->calls, 'local account passwords must not be sent to GEMP' );
	}

	public function testWrongGempPasswordFails() {
		$res = $this->login( 'nosuchgemp', 'whatever-pw' );
		$this->assertSame( AuthenticationResponse::FAIL, $res->status );
		$this->assertCount( 1, $this->gemp->calls );
		$this->assertFalse( $this->getServiceContainer()->getUserFactory()->newFromName( 'Nosuchgemp' )->isRegistered() );
	}

	public static function provideGempRefusals() {
		return [
			'INVALID' => [ [ 'status' => 'invalid_credentials' ], 'wrongpassword' ],
			'BANNED' => [ [ 'status' => 'banned' ], 'gempauth-banned' ],
			'TEMP_BANNED' => [ [ 'status' => 'temp_banned', 'until' => 1900000000 ], 'gempauth-temp-banned' ],
			'RESET_REQUIRED' => [ [ 'status' => 'reset_required' ], 'gempauth-reset-required' ],
			'DEACTIVATED' => [ [ 'status' => 'deactivated' ], 'gempauth-deactivated' ],
			'THROTTLED' => [ [ 'status' => 'throttled', 'retry_after' => 300 ], 'gempauth-throttled' ],
			'unavailable' => [ [ 'status' => 'unavailable' ], 'gempauth-unavailable' ],
		];
	}

	/** @dataProvider provideGempRefusals */
	public function testGempRefusals( array $answer, string $msg ) {
		$this->gemp->answers['refused'] = $answer;
		$res = $this->login( 'refused', 'pw-12345678' );
		$this->assertSame( AuthenticationResponse::FAIL, $res->status );
		$this->assertSame( $msg, $res->message->getKey() );
		$this->assertFalse( $this->getServiceContainer()->getUserFactory()->newFromName( 'Refused' )->isRegistered(),
			'no account is created for a refused login' );
	}

	public function testResetRequiredTellsUserToFinishOnGempAndNeverLogsIn() {
		$this->gemp->answers['resetme'] = [ 'status' => 'reset_required' ];
		$res = $this->login( 'resetme', 'ABCD-EFGH-JKLM' );
		$this->assertSame( AuthenticationResponse::FAIL, $res->status );
		$this->assertSame( 'gempauth-reset-required', $res->message->getKey() );
		$this->assertStringContainsString( 'Finish the reset on', $res->message->inLanguage( 'en' )->plain() );
		$this->assertFalse( $this->getServiceContainer()->getUserFactory()->newFromName( 'Resetme' )->isRegistered() );
	}

	public function testTempBanShowsDate() {
		$this->gemp->answers['suspended'] = [ 'status' => 'temp_banned', 'until' => 1900000000 ];
		$res = $this->login( 'suspended', 'pw-12345678' );
		$this->assertSame( 'gempauth-temp-banned', $res->message->getKey() );
		$this->assertStringContainsString( '2030', $res->message->inLanguage( 'en' )->text() );
	}

	public function testSendsRealClientIpFromTrustedProxy() {
		$this->overrideConfigValue( 'CdnServersNoPurge', [ '172.18.0.1' ] );
		// TCP peer is the docker bridge gateway (nginx on the host); nginx sets X-Forwarded-For
		$req = new class extends FauxRequest {
			protected function getRawIP() {
				return '172.18.0.1';
			}
		};
		$req->setHeader( 'X-Forwarded-For', '203.0.113.50' );
		RequestContext::getMain()->setRequest( $req );
		$this->resetServices();
		$this->setService( 'GempAuth.Client', $this->gemp );
		$this->login( 'whoever', 'pw-12345678' );
		$this->assertSame( '203.0.113.50', $this->gemp->calls[0][2], 'end-user IP, not the docker gateway' );
	}

	public function testCaseCollisionOnlyFirstLinkedAccountGetsIn() {
		$this->gemp->answers['bill'] = [ 'status' => 'ok', 'user' => [ 'id' => 1, 'name' => 'bill', 'admin' => false ] ];
		$this->assertSame( AuthenticationResponse::PASS, $this->login( 'bill', 'pw-aaaaaaaa' )->status );
		// A different GEMP account "Bill" maps to the same wiki name "Bill"
		$this->gemp->answers['Bill'] = [ 'status' => 'ok', 'user' => [ 'id' => 2, 'name' => 'Bill', 'admin' => false ] ];
		$res = $this->login( 'Bill', 'pw-bbbbbbbb' );
		$this->assertSame( AuthenticationResponse::FAIL, $res->status );
		$this->assertSame( 'gempauth-link-mismatch', $res->message->getKey() );
		$this->assertSame( '1', $this->linkedId( 'Bill' ) );
	}

	public function testCanonicalGempNameIsTheWikiName() {
		// GEMP matches "SKYWALKER" case-insensitively and returns the stored name "Skywalker"
		$this->gemp->answers['SKYWALKER'] = [ 'status' => 'ok', 'user' => [ 'id' => 5, 'name' => 'Skywalker', 'admin' => false ] ];
		$res = $this->login( 'SKYWALKER', 'pw-12345678' );
		$this->assertSame( AuthenticationResponse::PASS, $res->status );
		$this->assertSame( 'Skywalker', $res->username );
		$this->assertSame( '5', $this->linkedId( 'Skywalker' ) );
		$this->assertFalse( $this->getServiceContainer()->getUserFactory()->newFromName( 'SKYWALKER' )->isRegistered() );
	}

	public function testCanonicalNameCannotTakeOverLocalAccount() {
		$local = $this->getMutableTestUser()->getUser()->getName();
		$typed = strtoupper( $local );
		$this->assertNotSame( $local, $typed );
		$this->gemp->answers[$typed] = [ 'status' => 'ok', 'user' => [ 'id' => 6, 'name' => $local, 'admin' => false ] ];
		$res = $this->login( $typed, 'pw-12345678' );
		$this->assertSame( AuthenticationResponse::FAIL, $res->status );
		$this->assertSame( 'gempauth-link-mismatch', $res->message->getKey() );
		$this->assertNull( $this->linkedId( $local ) );
	}

	public function testLinkedAccountsCannotSetWikiPasswordOrReset() {
		$this->gemp->answers['linkeduser'] = [ 'status' => 'ok', 'user' => [ 'id' => 9, 'name' => 'linkeduser', 'admin' => false ] ];
		$this->assertSame( AuthenticationResponse::PASS, $this->login( 'linkeduser', 'pw-12345678' )->status );
		$req = new PasswordAuthenticationRequest();
		$req->action = AuthManager::ACTION_CHANGE;
		$req->username = 'Linkeduser';
		$req->password = $req->retype = 'new-wiki-password-1';
		$status = $this->getServiceContainer()->getAuthManager()->allowsAuthenticationDataChange( $req );
		$this->assertFalse( $status->isGood() );
		$this->assertTrue( $status->hasMessage( 'gempauth-password-on-gemp' ) );

		// local (unlinked) users can still change their password
		$local = $this->getMutableTestUser()->getUser();
		$req2 = clone $req;
		$req2->username = $local->getName();
		$this->assertTrue( $this->getServiceContainer()->getAuthManager()->allowsAuthenticationDataChange( $req2 )->isGood() );

		$linked = $this->getServiceContainer()->getUserFactory()->newFromName( 'Linkeduser' );
		$linked->setEmail( 'linked@example.org' );
		$linked->confirmEmail();
		$linked->saveSettings();
		$mailed = [];
		$this->setTemporaryHook( 'AlternateUserMailer', static function () use ( &$mailed ) {
			$mailed[] = func_get_args();
			return false;
		} );
		$this->overrideConfigValue( 'PasswordResetRoutes', [ 'username' => true, 'email' => true ] );
		$anon = $this->getServiceContainer()->getUserFactory()->newAnonymous( '127.0.0.1' );
		$st = $this->getServiceContainer()->getPasswordReset()->execute( $anon, 'Linkeduser', null );
		$this->assertFalse( $st->isOK(), 'wiki password reset refused for GEMP-linked accounts' );
		$this->assertTrue( $st->hasMessage( 'gempauth-password-on-gemp' ) );
		$this->assertSame( [], $mailed, 'no reset mail' );
	}
}
