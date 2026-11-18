<?php
/**
 * Shared swccg.com header/footer inside MediaWiki.
 * Also emits Open Graph tags so Discord/Slack previews show the card image.
 */

require_once '/swccg-chrome/card-image-preferences.php';
require_once '/swccg-chrome/photograph-presentation.php';

class SwccgChrome {

	public static function onBeforePageDisplay( $out, $skin ): void {
		# ResourceLoader site.styles can lag behind MediaWiki:Common.css.
		# Inline so portrait+Info stay left even when load.php is stale.
		$out->addInlineStyle(
			'.card-rail{float:left!important;clear:left!important;margin:0 1em 1em 0!important;}'
			. '.card-rail-right{float:right!important;clear:right!important;margin:0 0 1em 1em!important;}'
		);
		// Foil photograph framing and intrinsic inline-symbol sizes (work#436).
		$out->addInlineStyle( '.mw-parser-output table.card-thumbs td:not(:first-child) img{width:auto;height:auto;max-width:none;vertical-align:middle;} .mw-parser-output .card-photo-source img{width:100%!important;max-width:none!important;height:auto;display:block;} .mw-parser-output .card-photo-source a,.mw-parser-output .card-photo-source>span{display:block;width:100%;}' );
		SwccgCardImages::addPilot( $out );
		SwccgPhotographPresentation::addStyles( $out );
		// Bounded review pilot: no resources or behavior on ordinary card pages.
		$title = $out->getTitle();
        // Bounded public shared-search pilot449; ordinary Wiki pages load no resources.
        if ( $title && $title->getPrefixedText() === 'SWCCG Wiki:Samples/Shared search pilot' ) {
            $out->addInlineStyle( file_get_contents( '/swccg-chrome/shared-search-449.ef40c6e80858.css' ) );
            $out->addInlineScript( file_get_contents( '/swccg-chrome/shared-search-449.eaab1776ae20.js' ) );
        }

		if ( $title && in_array( $title->getPrefixedText(), [
			'SWCCG Wiki:Samples/Original Virtual Darth Vader image viewer',
			'SWCCG Wiki:Samples/Original Virtual Luke Skywalker image viewer',
		], true ) ) {
			$assets = '/swccg-chrome/';
			if ( is_readable( $assets . 'vader-image-viewer.css' ) && is_readable( $assets . 'vader-image-viewer.js' ) ) {
				$out->addInlineStyle( file_get_contents( $assets . 'vader-image-viewer.css' ) );
				$out->addInlineScript( file_get_contents( $assets . 'vader-image-viewer.js' ) );
			}
		}
		try {
			self::addOpenGraph( $out );
		} catch ( Throwable $e ) {
			wfLogWarning( 'SwccgChrome OG: ' . $e->getMessage() );
		}
	}

	public static function onSiteNoticeAfter( &$siteNotice, $skin ): void {
	}

	public static function onSkinAfterContent( &$data, $skin ): void {
	}

	private static function addOpenGraph( $out ): void {
		$title = $out->getTitle();
		if ( !$title || $title->isSpecialPage() ) {
			return;
		}
		$pageTitle = $title->getPrefixedText() . ' - SWCCG Wiki';
		$canonical = $title->getFullURL();
		self::prop( $out, 'og:type', 'website' );
		self::prop( $out, 'og:site_name', 'SWCCG Wiki' );
		self::prop( $out, 'og:title', $pageTitle );
		self::prop( $out, 'og:url', $canonical );
		$out->addHeadItem(
			'twitter:card',
			'<meta name="twitter:card" content="summary_large_image" />'
		);

		$desc = self::pageDescription( $title );
		if ( $desc !== '' ) {
			self::prop( $out, 'og:description', $desc );
			$out->addHeadItem(
				'twitter:description',
				'<meta name="twitter:description" content="' . htmlspecialchars( $desc, ENT_QUOTES ) . '" />'
			);
		}

		$img = self::cardImage( $title );
		if ( $img ) {
			self::prop( $out, 'og:image', $img['url'] );
			if ( !empty( $img['width'] ) ) {
				self::prop( $out, 'og:image:width', (string)$img['width'] );
			}
			if ( !empty( $img['height'] ) ) {
				self::prop( $out, 'og:image:height', (string)$img['height'] );
			}
			$out->addHeadItem(
				'twitter:image',
				'<meta name="twitter:image" content="' . htmlspecialchars( $img['url'], ENT_QUOTES ) . '" />'
			);
		}
	}

	private static function prop( $out, string $property, string $content ): void {
		$out->addHeadItem(
			$property,
			'<meta property="' . htmlspecialchars( $property, ENT_QUOTES ) . '" content="' . htmlspecialchars( $content, ENT_QUOTES ) . '" />'
		);
	}

	private static function pageDescription( $title ): string {
		$text = self::wikitext( $title );
		if ( $text !== '' && preg_match( '/\|lore=([^\n]+)/', $text, $m ) ) {
			$lore = trim( $m[1] );
			$lore = preg_replace( '/\[\[([^|\]]+)\|([^\]]+)\]\]/', '$2', $lore );
			$lore = preg_replace( '/\[\[([^\]]+)\]\]/', '$1', $lore );
			$lore = preg_replace( "/''+/", '', $lore );
			$lore = trim( $lore );
			if ( $lore !== '' ) {
				if ( strlen( $lore ) > 240 ) {
					$lore = substr( $lore, 0, 237 ) . '...';
				}
				return $lore;
			}
		}
		return $title->getText() . ' â€” Star Wars CCG card on SWCCG Wiki.';
	}

	private static function cardImage( $title ): ?array {
		$text = self::wikitext( $title );
		if ( $text === '' || !preg_match( '/\|image=([^\n|]+)/', $text, $m ) ) {
			return null;
		}
		$name = trim( $m[1] );
		if ( $name === '' ) {
			return null;
		}
		$services = MediaWiki\MediaWikiServices::getInstance();
		$file = $services->getRepoGroup()->findFile( $name );
		if ( !$file || !$file->exists() ) {
			return null;
		}
		$url = $file->getUrl();
		if ( function_exists( 'wfExpandUrl' ) ) {
			$url = wfExpandUrl( $url, PROTO_CANONICAL );
		}
		return [
			'url' => $url,
			'width' => $file->getWidth() ?: 0,
			'height' => $file->getHeight() ?: 0,
		];
	}

	private static function wikitext( $title ): string {
		try {
			$services = MediaWiki\MediaWikiServices::getInstance();
			$page = $services->getWikiPageFactory()->newFromTitle( $title );
			$content = $page->getContent();
			if ( !$content || !method_exists( $content, 'getText' ) ) {
				return '';
			}
			return $content->getText();
		} catch ( Throwable $e ) {
			return '';
		}
	}
}
