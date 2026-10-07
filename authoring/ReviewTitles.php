<?php
require_once __DIR__ . '/Maintenance.php';

class ReviewTitles extends Maintenance {
	public function execute() {
		$raw = [];
		for ( $i = 0; ; $i++ ) {
			$a = $this->getArg( $i );
			if ( $a === false || $a === null || $a === '' ) {
				break;
			}
			$raw[] = $a;
		}
		if ( !$raw ) {
			$stdin = stream_get_contents( STDIN );
			$raw = preg_split( '/\r?\n/', $stdin );
		}
		$dbw = $this->getServiceContainer()->getConnectionProvider()->getPrimaryDatabase();
		$n = 0;
		foreach ( $raw as $name ) {
			$name = trim( $name );
			if ( $name === '' ) {
				continue;
			}
			$title = Title::newFromText( $name );
			if ( !$title || !$title->exists() ) {
				$this->output( "MISSING $name\n" );
				continue;
			}
			$pageId = $title->getId();
			$latest = $title->getLatestRevID();
			$exists = $dbw->selectField(
				'flaggedpages',
				'fp_page_id',
				[ 'fp_page_id' => $pageId ],
				__METHOD__
			);
			$fields = [
				'fp_stable' => $latest,
				'fp_reviewed' => 1,
				'fp_pending_since' => null,
			];
			if ( $exists ) {
				$dbw->update(
					'flaggedpages',
					$fields,
					[ 'fp_page_id' => $pageId ],
					__METHOD__
				);
				$this->output( "updated $name id=$pageId stable=$latest\n" );
			} else {
				$fields['fp_page_id'] = $pageId;
				$dbw->insert( 'flaggedpages', $fields, __METHOD__ );
				$this->output( "inserted $name id=$pageId stable=$latest\n" );
			}
			$n++;
		}
		$this->output( "DONE n=$n\n" );
	}
}

$maintClass = ReviewTitles::class;
require_once RUN_MAINTENANCE_IF_MAIN;
