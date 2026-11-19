<?php
declare( strict_types = 1 );

use MediaWiki\Content\Renderer\ContentParseParams;
use MediaWiki\Content\WikitextContent;
use MediaWiki\MediaWikiServices;
use MediaWiki\Parser\ParserOutputFlags;
use MediaWiki\Parser\Sanitizer;

require_once __DIR__ . '/image-description-normalizer.php';

/** Render image descriptions consistently without changing their saved source. */
final class SwccgImageFileDescription {
    public const CACHE_VERSION = '816-v1';
    public const CACHE_KEY = 'swccg-image-description-layout';
    private const FULL_EDIT = 'swccg-image-layout-full-page';

    public static function isImage( $title ): bool {
        if ( !$title || $title->getNamespace() !== NS_FILE ) {
            return false;
        }
        $file = MediaWikiServices::getInstance()->getRepoGroup()->findFile( $title );
        return $file && $file->exists()
            && ( in_array( $file->getMediaType(), [ MEDIATYPE_BITMAP, MEDIATYPE_DRAWING ], true )
                || strpos( (string)$file->getMimeType(), 'image/' ) === 0 );
    }

    /** ContentGetParserOutput: normalize only the actual outer content object. */
    public static function render( $content, $title, $revId, $options, $generateHtml, &$output ): bool {
        if ( !$generateHtml || !$content instanceof WikitextContent
            || $content->isRedirect() || !self::isImage( $title )
        ) {
            return true;
        }

        $normalized = SwccgImageDescriptionStandard::normalize( $content->getText() );
        $display = new WikitextContent( $normalized['text'] );
        $display->setPreSaveTransformFlags( $content->getPreSaveTransformFlags() );
        $params = new ContentParseParams( $title, $revId, $options, true );

        // Use the installed content handler's rendering path, preserving its parser
        // selection, redirect/signature handling and ParserOutput dependency data.
        // This public bridge avoids re-entering ContentGetParserOutput recursively.
        $content->getContentHandler()->fillParserOutputInternal( $display, $params, $output );
        $output->setExtensionData( self::CACHE_KEY, self::CACHE_VERSION );

        if ( $normalized['changed'] ) {
            $html = $output->getRawText();
            if ( $options->getUseParsoid() ) {
                // Virtual offsets do not describe the saved source. The page's
                // ordinary Edit action remains available; never point a section
                // editor at an unrelated stored section.
                $output->setOutputFlag( ParserOutputFlags::NO_SECTION_EDIT_LINKS );
            } else {
                $html = self::fullPageEditMarkers( $html, $title->getPrefixedText() );
            }
            $output->setRawText( self::legacyAnchors( $html, $normalized['operations'], $options->getUseParsoid() ) );
        }
        return false;
    }

    /** Reject only old image-description cache values, once per layout version. */
    public static function acceptCached( $output, $wikiPage, $options ): bool {
        return $wikiPage->isRedirect() || $wikiPage->getContentModel() !== CONTENT_MODEL_WIKITEXT
            || !self::isImage( $wikiPage->getTitle() )
            || $output->getExtensionData( self::CACHE_KEY ) === self::CACHE_VERSION;
    }

    /** SkinEditSectionLinks: a virtual section edits the real full File source. */
    public static function editLinks( $skin, $title, $section, $sectionTitle, &$links, $lang ): void {
        if ( $section !== self::FULL_EDIT || $title->getNamespace() !== NS_FILE ) {
            return;
        }
        foreach ( $links as &$link ) {
            unset( $link['query']['section'] );
        }
    }

    private static function fullPageEditMarkers( string $html, string $title ): string {
        return preg_replace_callback(
            '~<mw:editsection page="([^"]*)" section="([^"]*)">~',
            static function ( array $match ) use ( $title ): string {
                if ( htmlspecialchars_decode( $match[1], ENT_QUOTES ) !== $title ) {
                    return $match[0];
                }
                return '<mw:editsection page="' . $match[1] . '" section="' . self::FULL_EDIT . '">';
            },
            $html
        );
    }

    /** Keep external #Summary/#Source links usable, without duplicate IDs. */
    private static function legacyAnchors( string $html, array $operations, bool $parsoid ): string {
        preg_match_all( '~(?:\bid|data-mw-anchor)="([^"]+)"~', $html, $existing );
        $used = array_fill_keys( array_map( 'htmlspecialchars_decode', $existing[1] ), true );
        $aliases = [];
        foreach ( $operations as $operation ) {
            if ( !preg_match( '~^rename_heading:(.+)->(Description|Source and credit)$~u', $operation, $match ) ) {
                continue;
            }
            $alias = Sanitizer::escapeIdForAttribute( $match[1] );
            if ( !isset( $used[$alias] ) ) {
                $target = Sanitizer::escapeIdForAttribute( $match[2] );
                $aliases[$target][] = $alias;
                $used[$alias] = true;
            }
        }
        if ( !$aliases ) {
            return $html;
        }
        return preg_replace_callback(
            '~<h([1-6])\b[^>]*>[\s\S]*?</h\1>~i',
            static function ( array $match ) use ( &$aliases, $parsoid ): string {
                if ( !$parsoid && strpos( $match[0], 'section="' . self::FULL_EDIT . '"' ) === false ) {
                    return $match[0];
                }
                foreach ( $aliases as $target => $names ) {
                    $attribute = htmlspecialchars( $target, ENT_QUOTES );
                    if ( !preg_match( '~(?:\bid|data-mw-anchor)="' . preg_quote( $attribute, '~' ) . '"~', $match[0] ) ) {
                        continue;
                    }
                    $markers = '';
                    foreach ( $names as $name ) {
                        $markers .= '<span id="' . htmlspecialchars( $name, ENT_QUOTES ) . '"></span>';
                    }
                    unset( $aliases[$target] );
                    return $markers . $match[0];
                }
                return $match[0];
            },
            $html
        );
    }
}
