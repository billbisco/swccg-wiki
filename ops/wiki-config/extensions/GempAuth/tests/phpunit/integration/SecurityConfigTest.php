<?php

namespace MediaWiki\Extension\GempAuth\Tests\Integration;

use MediaWiki\Context\RequestContext;
use MediaWiki\Request\WebRequest;
use MediaWikiIntegrationTestCase;

/**
 * Checks the shipped ops/wiki-config/login-security.php values as loaded by the test wiki.
 *
 * @group Database
 * @coversNothing
 */
class SecurityConfigTest extends MediaWikiIntegrationTestCase {
	public function testSignupMovedToGempAndAutocreateKept() {
		$perms = $this->getConfVar( 'GroupPermissions' );
		$this->assertFalse( $perms['*']['createaccount'] );
		$this->assertTrue( $perms['*']['autocreateaccount'] );
		$this->assertFalse( $this->getConfVar( 'EmailConfirmToEdit' ), 'must not block talk pages' );
	}

	public function testRealClientIpBehindHostNginx() {
		$this->overrideConfigValue( 'CdnServersNoPurge', [ '172.18.0.1' ] );
		$this->resetServices();
		$get = function ( string $remote, ?string $xff ) {
			$_SERVER['REMOTE_ADDR'] = $remote;
			if ( $xff === null ) {
				unset( $_SERVER['HTTP_X_FORWARDED_FOR'] );
			} else {
				$_SERVER['HTTP_X_FORWARDED_FOR'] = $xff;
			}
			return ( new WebRequest() )->getIP();
		};
		$this->assertSame( '203.0.113.9', $get( '172.18.0.1', '203.0.113.9' ) );
		// Client-supplied XFF is kept by $proxy_add_x_forwarded_for; MW still takes nginx's entry.
		$this->assertSame( '203.0.113.9', $get( '172.18.0.1', '6.6.6.6, 203.0.113.9' ) );
		// Anyone else cannot spoof
		$this->assertSame( '198.51.100.4', $get( '198.51.100.4', '203.0.113.9' ) );
		unset( $_SERVER['HTTP_X_FORWARDED_FOR'] );
	}

	public function testAdminsWithout2faLoseAdminRights() {
		$this->assertSame( [ 'sysop', 'bureaucrat', 'interface-admin' ], $this->getConfVar( 'OATHRequiredForGroups' ) );
		$admin = $this->getMutableTestUser( [ 'sysop', 'bureaucrat' ] )->getUser();
		RequestContext::getMain()->setUser( $admin );
		$ugm = $this->getServiceContainer()->getUserGroupManager();
		$ugm->clearCache( $admin );
		$effective = $ugm->getUserEffectiveGroups( $admin );
		$this->assertNotContains( 'sysop', $effective );
		$this->assertNotContains( 'bureaucrat', $effective );
		$this->assertTrue( $this->getServiceContainer()->getPermissionManager()->userHasRight( $admin, 'oathauth-enable' ) );
	}

	public function testRateLimitsPresent() {
		$rl = $this->getConfVar( 'RateLimits' );
		foreach ( [ 'mailpassword', 'confirmemail', 'changeemail', 'sendemail', 'badcaptcha' ] as $k ) {
			$this->assertArrayHasKey( $k, $rl );
		}
		$this->assertTrue( $this->getConfVar( 'CaptchaTriggers' )['badlogin'] );
	}
}
