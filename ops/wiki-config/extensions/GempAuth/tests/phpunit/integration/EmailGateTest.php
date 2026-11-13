<?php

namespace MediaWiki\Extension\GempAuth\Tests\Integration;

use MediaWiki\Context\RequestContext;
use MediaWiki\Title\Title;
use MediaWiki\User\User;
use MediaWikiIntegrationTestCase;

/**
 * Level 3: content edits need a confirmed email; talk pages do not.
 * Mail goes through a capture hook (SES not live yet): the test follows the emailed link.
 *
 * @group Database
 * @covers \MediaWiki\Extension\GempAuth\Hooks
 */
class EmailGateTest extends MediaWikiIntegrationTestCase {
	private array $mail = [];

	protected function setUp(): void {
		parent::setUp();
		$this->overrideConfigValues( [ 'EnableEmail' => true, 'EmailAuthentication' => true ] );
		$this->setTemporaryHook( 'AlternateUserMailer', function ( $headers, $to, $from, $subject, $body ) {
			$this->mail[] = [ 'to' => $to, 'subject' => $subject, 'body' => is_array( $body ) ? $body['text'] : $body ];
			return false;
		} );
	}

	private function can( User $user, string $action, string $page ): bool {
		$pm = $this->getServiceContainer()->getPermissionManager();
		return $pm->userCan( $action, $user, Title::newFromText( $page ), $pm::RIGOR_SECURE );
	}

	private function freshUser(): User {
		$user = $this->getMutableTestUser()->getUser();
		$user->setEmail( '' );
		$user->saveSettings();
		return $user;
	}

	public function testUnconfirmedUserCanTalkButNotEditContent() {
		$user = $this->freshUser();
		$this->assertFalse( $user->isEmailConfirmed() );
		foreach ( [ 'Talk:Luke Skywalker', 'User talk:Someone', 'Card talk:Han', 'Project talk:Rules', 'User:' . $user->getName() ] as $p ) {
			$this->assertTrue( $this->can( $user, 'edit', $p ), "edit $p" );
		}
		foreach ( [ 'Luke Skywalker', 'Card:Han', 'Template:Card', 'Help:Editing', 'Category:Cards', 'Project:Rules' ] as $p ) {
			$this->assertFalse( $this->can( $user, 'edit', $p ), "edit $p" );
			$this->assertFalse( $this->can( $user, 'create', $p ), "create $p" );
		}
		$this->assertFalse( $this->can( $user, 'move', 'Luke Skywalker' ) );
		$errors = $this->getServiceContainer()->getPermissionManager()
			->getPermissionErrors( 'edit', $user, Title::newFromText( 'Luke Skywalker' ) );
		$this->assertContains( 'gempauth-confirm-email-to-edit', array_map( static fn ( $e ) => $e[0], $errors ) );
	}

	public function testConfirmedEditorGroupCanEditContentWithoutEmail() {
		$user = $this->freshUser();
		$this->assertFalse( $this->can( $user, 'edit', 'Luke Skywalker' ) );
		$this->getServiceContainer()->getUserGroupManager()->addUserToGroup( $user, 'confirmed-editor' );
		$this->getServiceContainer()->getPermissionManager()->invalidateUsersRightsCache( $user );
		$this->assertFalse( $user->isEmailConfirmed() );
		$this->assertTrue( $this->can( $user, 'edit', 'Luke Skywalker' ) );
		$this->assertTrue( $this->can( $user, 'edit', 'Talk:Luke Skywalker' ) );
		$this->assertFalse( $this->getServiceContainer()->getPermissionManager()->userHasRight( $user, 'review' ), 'no FlaggedRevs review rights' );
	}

	public function testConfirmationMailLinkUnlocksEditing() {
		$user = $this->freshUser();
		RequestContext::getMain()->setUser( $user );
		$user->setEmail( 'player@example.org' );
		$user->saveSettings();
		$status = $user->sendConfirmationMail();
		$this->assertStatusGood( $status );
		$this->assertCount( 1, $this->mail, 'one message captured, none sent' );
		$this->assertMatchesRegularExpression( '#Special:ConfirmEmail/([0-9a-f]{32})#', $this->mail[0]['body'] );
		preg_match( '#Special:ConfirmEmail/([0-9a-f]{32})#', $this->mail[0]['body'], $m );

		// What Special:ConfirmEmail does with the code from the link
		$fromCode = $this->getServiceContainer()->getUserFactory()->newFromConfirmationCode( $m[1], 0 );
		$this->assertNotNull( $fromCode );
		$this->assertSame( $user->getId(), $fromCode->getId() );
		$fromCode->confirmEmail();
		$fromCode->saveSettings();

		$confirmed = $this->getServiceContainer()->getUserFactory()->newFromId( $user->getId() );
		$confirmed->load( User::READ_LATEST );
		$this->assertTrue( $confirmed->isEmailConfirmed() );
		$this->assertContains( 'emailconfirmed', $this->getServiceContainer()->getUserGroupManager()->getUserEffectiveGroups( $confirmed ) );
		$this->assertTrue( $this->can( $confirmed, 'edit', 'Luke Skywalker' ) );
		$this->assertTrue( $this->can( $confirmed, 'edit', 'Card:Han' ) );
	}

	public function testTrustedGroupsBypassTheGate() {
		foreach ( [ 'bot', 'sysop' ] as $group ) {
			$user = $this->getMutableTestUser( [ $group ] )->getUser();
			$user->setEmail( '' );
			$user->saveSettings();
			$this->assertTrue( $this->can( $user, 'edit', 'Luke Skywalker' ), $group );
		}
	}
}
