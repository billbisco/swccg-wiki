<?php
/**
 * Link (or unlink) an existing wiki account to a GEMP player id, e.g. for a person who had a
 * local wiki account before GEMP login, or to resolve a case collision (GEMP "bill" vs "Bill").
 * Linked accounts cannot set a wiki password; any old local password keeps working until
 * an admin removes it (see the runbook).
 *
 *   php maintenance/run.php ./extensions/GempAuth/maintenance/linkGempAccount.php --user "Name" --gemp-id 123
 *   php maintenance/run.php ./extensions/GempAuth/maintenance/linkGempAccount.php --user "Name" --unlink
 */

use MediaWiki\Extension\GempAuth\GempPrimaryAuthenticationProvider;
use MediaWiki\Maintenance\Maintenance;

$IP = getenv( 'MW_INSTALL_PATH' ) ?: __DIR__ . '/../../..';
require_once "$IP/maintenance/Maintenance.php";

class LinkGempAccount extends Maintenance {
	public function __construct() {
		parent::__construct();
		$this->requireExtension( 'GempAuth' );
		$this->addDescription( 'Link or unlink a wiki account and a GEMP player id' );
		$this->addOption( 'user', 'Wiki user name', true, true );
		$this->addOption( 'gemp-id', 'GEMP player id (from GEMP admin)', false, true );
		$this->addOption( 'unlink', 'Remove the link' );
	}

	public function execute() {
		$services = $this->getServiceContainer();
		$user = $services->getUserFactory()->newFromName( $this->getOption( 'user' ) );
		if ( !$user || !$user->isRegistered() ) {
			$this->fatalError( 'No such wiki user' );
		}
		$opts = $services->getUserOptionsManager();
		if ( $this->hasOption( 'unlink' ) ) {
			$opts->setOption( $user, GempPrimaryAuthenticationProvider::LINK_OPTION, null );
		} else {
			$id = (int)$this->getOption( 'gemp-id', 0 );
			if ( $id <= 0 ) {
				$this->fatalError( '--gemp-id must be a positive integer' );
			}
			$opts->setOption( $user, GempPrimaryAuthenticationProvider::LINK_OPTION, (string)$id );
		}
		$opts->saveOptions( $user );
		$this->output( $user->getName() . ' gempauth-id=' . ( $opts->getOption( $user, GempPrimaryAuthenticationProvider::LINK_OPTION ) ?? '(none)' ) . "\n" );
	}
}

$maintClass = LinkGempAccount::class;
require_once RUN_MAINTENANCE_IF_MAIN;
