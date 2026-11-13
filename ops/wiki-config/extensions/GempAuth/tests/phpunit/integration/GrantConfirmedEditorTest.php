<?php

namespace MediaWiki\Extension\GempAuth\Tests\Integration;

use GrantConfirmedEditor;
use MediaWiki\Tests\Maintenance\MaintenanceBaseTestCase;
use MediaWiki\User\User;

/**
 * @group Database
 * @covers \GrantConfirmedEditor
 */
class GrantConfirmedEditorTest extends MaintenanceBaseTestCase {
	protected function getMaintenanceClass() {
		require_once dirname( __DIR__, 3 ) . '/maintenance/grantConfirmedEditor.php';
		return GrantConfirmedEditor::class;
	}

	private function user( int $edits, bool $confirmed, array $groups = [] ): User {
		$user = $this->getMutableTestUser( $groups )->getUser();
		$user->setEmail( $confirmed ? 'x@example.org' : '' );
		if ( $confirmed ) {
			$user->confirmEmail();
		}
		$user->saveSettings();
		$this->getDb()->newUpdateQueryBuilder()->update( 'user' )
			->set( [ 'user_editcount' => $edits, 'user_email_authenticated' => $confirmed ? $this->getDb()->timestamp() : null ] )
			->where( [ 'user_id' => $user->getId() ] )->caller( __METHOD__ )->execute();
		return $user;
	}

	private function groups( User $u ): array {
		$ugm = $this->getServiceContainer()->getUserGroupManager();
		$ugm->clearCache( $u );
		return $ugm->getUserGroups( $u );
	}

	public function testAddsOnlyUnconfirmedEditorsWithoutEditcontent() {
		$editor = $this->user( 26, false );
		$confirmed = $this->user( 10, true );
		$noEdits = $this->user( 0, false );
		$sysop = $this->user( 500, false, [ 'sysop' ] );
		$bot = $this->user( 900, false, [ 'bot' ] );
		$system = User::newSystemUser( 'Redirect system', [ 'steal' => true ] );

		$this->maintenance->loadWithArgv( [ '--dry-run' ] );
		$this->maintenance->execute();
		$this->assertNotContains( 'confirmed-editor', $this->groups( $editor ), 'dry run changes nothing' );

		$this->maintenance->loadWithArgv( [] );
		$this->maintenance->execute();
		$out = $this->getActualOutputForAssertion();
		$this->assertStringContainsString( 'would add ' . $editor->getName(), $out );
		$this->assertStringContainsString( 'added ' . $editor->getName(), $out );
		$this->assertContains( 'confirmed-editor', $this->groups( $editor ) );
		foreach ( [ $confirmed, $noEdits, $sysop, $bot ] as $u ) {
			$this->assertNotContains( 'confirmed-editor', $this->groups( $u ), $u->getName() );
		}
		$this->assertNotContains( 'confirmed-editor', $this->groups( $system ) );
		$this->assertSame( 1, (int)$this->getDb()->newSelectQueryBuilder()->select( 'COUNT(*)' )->from( 'logging' )
			->where( [ 'log_type' => 'rights', 'log_title' => str_replace( ' ', '_', $editor->getName() ) ] )
			->caller( __METHOD__ )->fetchField(), 'rights log entry' );
	}

	public function testIdempotent() {
		$editor = $this->user( 3, false );
		$this->maintenance->loadWithArgv( [] );
		$this->maintenance->execute();
		$this->maintenance->loadWithArgv( [] );
		$this->maintenance->execute();
		$this->assertStringContainsString( 'already has editcontent', $this->getActualOutputForAssertion() );
		$this->assertContains( 'confirmed-editor', $this->groups( $editor ) );
	}
}
