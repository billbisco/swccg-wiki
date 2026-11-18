<?php
/** Standard presentation for explicitly categorized bitmap photographs. */
class SwccgPhotographPresentation {
    public static function addStyles( $out ): void {
        $title = $out->getTitle();
        if ( $title && self::appliesTo( $title ) ) {
            $out->addInlineStyle( '.mw-filepage-resolutioninfo,.fullMedia{display:none!important;}' );
        }
    }

    public static function appliesTo( $title ): bool {
        if ( !$title->inNamespace( NS_FILE ) ) {
            return false;
        }
        $services = \MediaWiki\MediaWikiServices::getInstance();
        $file = $services->getRepoGroup()->findFile( $title );
        if ( !$file || $file->getMediaType() !== MEDIATYPE_BITMAP ) {
            return false;
        }
        $photographCategories = self::categoryKeys();
        foreach ( array_keys( $title->getParentCategories() ) as $name ) {
            $category = Title::newFromText( $name );
            if ( $category && isset( $photographCategories[$category->getDBkey()] ) ) {
                return true;
            }
        }
        return false;
    }

    /** Cached category subtree; also used by bounded maintenance inventories. */
    public static function categoryKeys(): array {
        $services = \MediaWiki\MediaWikiServices::getInstance();
        $cache = $services->getMainWANObjectCache();
        return $cache->getWithSetCallback(
            $cache->makeKey( 'swccg-photograph-categories', 'v1' ),
            300,
            static function () use ( $services ) {
                $db = $services->getConnectionProvider()->getReplicaDatabase();
                $seen = [ 'Photographs' => true ];
                $pending = [ 'Photographs' ];
                while ( $pending ) {
                    $rows = $db->newSelectQueryBuilder()
                        ->select( 'page_title' )
                        ->from( 'categorylinks' )
                        ->join( 'page', null, 'page_id = cl_from' )
                        ->where( [ 'cl_to' => $pending, 'page_namespace' => NS_CATEGORY ] )
                        ->caller( __METHOD__ )
                        ->fetchResultSet();
                    $pending = [];
                    foreach ( $rows as $row ) {
                        $key = $row->page_title;
                        if ( !isset( $seen[$key] ) ) {
                            $seen[$key] = true;
                            $pending[] = $key;
                        }
                    }
                }
                return $seen;
            }
        );
    }
}
