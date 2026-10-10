<?php
# Copy of the block appended to /opt/swccg-wiki/extra-settings.php on 2026-10-10 (backup: extra-settings.php.bak-20261010-gemp).
# Also live: nginx `location /images/` adds X-Content-Type-Options: nosniff (backup /root/wiki.swccg.com.nginx.bak-20261010).

# --- GEMP Importable decklists (Bill 2026-10-10) ------------------------------------------
# GEMP decklist .txt files are XML inside, and MediaWiki blocks XML uploads by default.
# Allow them ONLY when the file is a GEMP deck: a .txt file under 512 KB whose root element is
# <deck> holding only <card>/<cardOutsideDeck> elements, with no DOCTYPE, entities, stylesheet
# instructions, namespaces or script. Any other XML upload is still refused.
$wgMimeTypeExclusions = array_values( array_diff( $wgMimeTypeExclusions, [ 'application/xml', 'text/xml' ] ) );
# Let a .txt name carry XML content (the GEMP format); the UploadVerifyFile check below then
# decides whether that XML is really a GEMP deck.
$wgHooks['MimeMagicInit'][] = static function ( $mimeAnalyzer ) {
	$mimeAnalyzer->addExtraTypes( 'application/xml txt' );
};
$wgHooks['UploadVerifyFile'][] = static function ( $upload, $mime, &$error ) {
	if ( $mime !== 'application/xml' && $mime !== 'text/xml' ) {
		return true;
	}
	$title = $upload->getTitle();
	$path = $upload->getTempPath();
	$ok = $title && preg_match( '/\.txt$/i', $title->getText() ) && $path && filesize( $path ) <= 512 * 1024;
	if ( $ok ) {
		$xml = file_get_contents( $path );
		$ok = !preg_match( '/<!DOCTYPE|<!ENTITY|<\?xml-stylesheet|xmlns|<script|javascript:/i', $xml );
	}
	if ( $ok ) {
		$prev = libxml_use_internal_errors( true );
		$doc = simplexml_load_string( $xml, 'SimpleXMLElement', LIBXML_NONET );
		libxml_use_internal_errors( $prev );
		$ok = $doc !== false && $doc->getName() === 'deck';
		if ( $ok ) {
			foreach ( $doc->children() as $child ) {
				if ( !in_array( $child->getName(), [ 'card', 'cardOutsideDeck' ], true ) ) {
					$ok = false;
					break;
				}
			}
		}
	}
	if ( !$ok ) {
		$error = [ 'filetype-badmime', $mime ];
		return false;
	}
	return true;
};
