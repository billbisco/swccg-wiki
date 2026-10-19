<?php
/**
 * While real email delivery is not live, put existing editors who have no confirmed email into
 * 'confirmed-editor' (grants editcontent only) so the email gate does not lock them out.
 * Runbook query: user_email_authenticated IS NULL AND user_editcount > 0.
 * Skips system users and anyone who already has editcontent (sysop, bot, editor, confirmed-editor).
 * Each addition is written to Special:Log/rights. Safe to re-run.
 *
 *   php maintenance/run.php ./extensions/GempAuth/maintenance/grantConfirmedEditor.php --dry-run
 *   php maintenance/run.php ./extensions/GempAuth/maintenance/grantConfirmedEditor.php
 */

use MediaWiki\Maintenance\Maintenance;
use MediaWiki\User\User;

$IP = getenv( 'MW_INSTALL_PATH' ) ?: __DIR__ . '/../../..';
require_once "$IP/maintenance/Maintenance.php";

class GrantConfirmedEditor extends Maintenance {
	public const GROUP = 'confirmed-editor';

	public function __construct() {
		parent::__construct();
		$this->requireExtension( 'GempAuth' );
		$this->addDescription( 'Add existing editors without a confirmed email to the confirmed-editor group' );
		$this->addOption( 'dry-run', 'List who would be added; change nothing' );
		$this->addOption( 'reason', 'Rights log reason', false, true );
	}

	public function execute() {
		$services = $this->getServiceContainer();
		$dbr = $services->getConnectionProvider()->getReplicaDatabase();
		$ids = $dbr->newSelectQueryBuilder()
			->select( 'user_id' )
			->from( 'user' )
			->where( [ 'user_email_authenticated' => null, $dbr->expr( 'user_editcount', '>', 0 ) ] )
			->orderBy( 'user_id' )
			->caller( __METHOD__ )
			->fetchFieldValues();
		$ugm = $services->getUserGroupManager();
		$pm = $services->getPermissionManager();
		$dry = $this->hasOption( 'dry-run' );
		$reason = $this->getOption( 'reason', 'Existing editor; real email delivery is not live yet (GempAuth email gate)' );
		$performer = User::newSystemUser( User::MAINTENANCE_SCRIPT_USER, [ 'steal' => true ] );
		$added = 0;
		foreach ( $ids as $id ) {
			$user = $services->getUserFactory()->newFromId( (int)$id );
			$user->load();
			$name = $user->getName();
			if ( $user->isSystemUser() ) {
				$this->output( "skip  $name (system user)\n" );
				continue;
			}
			if ( $pm->userHasRight( $user, 'editcontent' ) ) {
				$this->output( "skip  $name (already has editcontent: " . implode( ',', $ugm->getUserGroups( $user ) ) . ")\n" );
				continue;
			}
			if ( $dry ) {
				$this->output( "would add $name\n" );
				$added++;
				continue;
			}
			$old = $ugm->getUserGroups( $user );
			if ( $ugm->addUserToGroup( $user, self::GROUP ) ) {
				$log = new ManualLogEntry( 'rights', 'rights' );
				$log->setPerformer( $performer );
				$log->setTarget( $user->getUserPage() );
				$log->setComment( $reason );
				$log->setParameters( [ '4::oldgroups' => $old, '5::newgroups' => $ugm->getUserGroups( $user ) ] );
				$log->insert();
				$this->output( "added $name\n" );
				$added++;
			}
		}
		$this->output( ( $dry ? 'would add' : 'added' ) . " $added user(s) to " . self::GROUP . "\n" );
	}
}

$maintClass = GrantConfirmedEditor::class;
require_once RUN_MAINTENANCE_IF_MAIN;
