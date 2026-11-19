<?php
declare( strict_types = 1 );

/**
 * Pure, source-preserving image-description layout normalization.
 *
 * No MediaWiki services, hooks, source lookups, publication or Python dependency.
 * This is the PHP equivalent of authoring/image_description_standard.py.
 */
final class SwccgImageDescriptionStandard {
    private const HEADING = '~^(?P<marks>={2,6})[ \t]*(?P<label>.*?)[ \t]*(?P=marks)[ \t]*$~m';
    private const CATEGORY = '~\[\[Category:[^\]]*\]\]~i';
    private const PROTECTED = '~<!--[\s\S]*?-->|<(nowiki|pre|syntaxhighlight|source)\b[^>]*>[\s\S]*?</\1\s*>|<nowiki\s*/>~i';
    private const SOURCE_PREFIX = <<<'REGEX'
(?:Source(?:[ \t]+and[ \t]+credit)?[ \t]*:|'''Source(?:[ \t]+and[ \t]+credit)?[ \t]*(?::'''|'''[ \t]*:))
REGEX;
    private const SOURCE_BOUNDARY = '~(*UCP)^[ \t]*(?:\*[ \t]*)?(?:' . self::SOURCE_PREFIX . '[ \t]*\S|Photo provided by[ \t]+\S)~imu';
    private const RENAMES = [
        'summary' => 'Description',
        'source' => 'Source and credit',
        'sources' => 'Source and credit',
    ];

    /** Retain byte offsets and line boundaries while masking protected text. */
    private static function blank( string $text ): string {
        return preg_replace( '~[^\r\n]~', ' ', $text );
    }

    private static function masked( string $text ): string {
        $masked = preg_replace_callback(
            self::PROTECTED,
            static fn ( array $match ): string => self::blank( $match[0] ),
            $text
        );
        preg_match_all( '~\{\{|\}\}~', $masked, $tokens, PREG_OFFSET_CAPTURE );
        $depth = 0;
        $start = 0;
        $ranges = [];
        foreach ( $tokens[0] as [ $token, $offset ] ) {
            if ( $token === '{{' ) {
                if ( $depth === 0 ) {
                    $start = $offset;
                }
                $depth++;
            } elseif ( $depth > 0 ) {
                $depth--;
                if ( $depth === 0 ) {
                    $ranges[] = [ $start, $offset + 2 ];
                }
            }
        }
        if ( $depth > 0 ) {
            $ranges[] = [ $start, strlen( $masked ) ];
        }
        foreach ( array_reverse( $ranges ) as [ $start, $end ] ) {
            $masked = substr_replace( $masked, self::blank( substr( $masked, $start, $end - $start ) ), $start, $end - $start );
        }
        return $masked;
    }

    private static function stripped( string $text ): string {
        // Python str.strip also regards the four ASCII information separators as whitespace.
        return preg_replace( '~(*UCP)\A[\s\x{1c}-\x{1f}]+|[\s\x{1c}-\x{1f}]+\z~u', '', $text );
    }

    private static function folded( string $text ): string {
        return mb_convert_case( self::stripped( $text ), MB_CASE_FOLD, 'UTF-8' );
    }

    /** @return array<int,array{start:int,end:int,label:string}> */
    private static function headings( string $text ): array {
        preg_match_all( self::HEADING, self::masked( $text ), $matches, PREG_SET_ORDER | PREG_OFFSET_CAPTURE );
        $headings = [];
        foreach ( $matches as $match ) {
            if ( strlen( $match['marks'][0] ) === 2 ) {
                $headings[] = [
                    'start' => $match[0][1],
                    'end' => $match[0][1] + strlen( $match[0][0] ),
                    'label' => $match['label'][0],
                ];
            }
        }
        return $headings;
    }

    private static function substantive( string $text ): bool {
        return self::stripped( preg_replace( self::CATEGORY, '', self::masked( $text ) ) ) !== '';
    }

    private static function sectionContent( string $text, array $heading ): string {
        $found = preg_match( self::HEADING, self::masked( $text ), $following, PREG_OFFSET_CAPTURE, $heading['end'] );
        $end = $found ? $following[0][1] : strlen( $text );
        return substr( $text, $heading['end'], $end - $heading['end'] );
    }

    /** Structural observations; this does not replace editorial/source validation. */
    public static function structuralIssues( string $text ): array {
        $headings = self::headings( $text );
        $names = array_map( static fn ( array $h ): string => self::folded( $h['label'] ), $headings );
        $issues = [];
        if ( !in_array( 'description', $names, true ) ) {
            $issues[] = 'missing_description_section';
        }
        if ( !in_array( 'source and credit', $names, true ) ) {
            $issues[] = 'missing_source_and_credit_section';
        }
        foreach ( $names as $name ) {
            if ( isset( self::RENAMES[$name] ) ) {
                $issues[] = 'legacy_section_heading';
                break;
            }
        }
        $counts = array_count_values( $names );
        if ( ( $counts['description'] ?? 0 ) > 1 || ( $counts['source and credit'] ?? 0 ) > 1 ) {
            $issues[] = 'duplicate_standard_heading';
        }
        foreach ( $headings as $heading ) {
            if ( !self::substantive( self::sectionContent( $text, $heading ) ) ) {
                $issues[] = 'empty_section';
                break;
            }
        }
        if ( strpos( $text, '{{' ) !== false && !self::substantive( $text ) ) {
            $issues[] = 'opaque_template_description';
        }
        return $issues;
    }

    private static function payload( string $text ): string {
        foreach ( array_reverse( self::headings( $text ) ) as $heading ) {
            $length = $heading['end'] - $heading['start'];
            $text = substr_replace( $text, str_repeat( ' ', $length ), $heading['start'], $length );
        }
        return preg_replace( '~(*UCP)[\s\x{1c}-\x{1f}]~u', '', $text );
    }

    private static function urls( string $text ): array {
        preg_match_all( "~(*UCP)https?://[^\\s<>\\]\"']+~u", $text, $matches );
        return $matches[0];
    }

    /** @return array<string,mixed> */
    public static function normalize( string $text ): array {
        $original = $text;
        $before = self::structuralIssues( $text );
        if ( preg_match( '~(*UCP)\A\s*#redirect\b~iu', $text ) ) {
            return [
                'text' => $text, 'changed' => false, 'operations' => [],
                'issues_before' => $before, 'issues_after' => $before, 'new_issues' => [],
                'all_payload_characters_retained' => true, 'all_urls_retained_in_order' => true,
                'source_disposition' => 'file_redirect_not_a_description',
            ];
        }
        $operations = [];
        $headings = self::headings( $text );
        $names = array_map( static fn ( array $h ): string => self::folded( $h['label'] ), $headings );
        $replacements = [];
        foreach ( $headings as $heading ) {
            $target = self::RENAMES[self::folded( $heading['label'] )] ?? null;
            if ( $target === null ) {
                continue;
            }
            $aliases = array_filter( $names, static fn ( string $name ): bool => self::folded( self::RENAMES[$name] ?? $name ) === self::folded( $target ) );
            if ( count( $aliases ) !== 1 || !self::substantive( self::sectionContent( $text, $heading ) ) ) {
                continue;
            }
            $replacements[] = [ $heading['start'], $heading['end'], '== ' . $target . ' ==' ];
            $operations[] = 'rename_heading:' . self::stripped( $heading['label'] ) . '->' . $target;
        }
        foreach ( array_reverse( $replacements ) as [ $start, $end, $replacement ] ) {
            $text = substr_replace( $text, $replacement, $start, $end - $start );
        }

        $headings = self::headings( $text );
        $names = array_map( static fn ( array $h ): string => self::folded( $h['label'] ), $headings );
        $descriptions = array_values( array_filter( $headings, static fn ( array $h ): bool => self::folded( $h['label'] ) === 'description' ) );
        if ( count( $descriptions ) === 1 && !in_array( 'source and credit', $names, true ) ) {
            $description = $descriptions[0];
            $body = self::sectionContent( $text, $description );
            $found = preg_match( self::SOURCE_BOUNDARY, self::masked( $body ), $boundary, PREG_OFFSET_CAPTURE );
            if ( $found && self::substantive( substr( $body, 0, $boundary[0][1] ) ) ) {
                $index = $description['end'] + $boundary[0][1];
                $text = substr_replace( $text, "== Source and credit ==\n\n", $index, 0 );
                $operations[] = 'insert_source_heading_at_explicit_boundary';
                $headings = self::headings( $text );
                $names = array_map( static fn ( array $h ): string => self::folded( $h['label'] ), $headings );
            }
        }
        $first = $headings[0]['start'] ?? strlen( $text );
        $prelude = substr( $text, 0, $first );
        $found = preg_match( self::SOURCE_BOUNDARY, self::masked( $prelude ), $boundary, PREG_OFFSET_CAPTURE );
        if ( $found && !in_array( 'source and credit', $names, true ) ) {
            $index = $boundary[0][1];
            $source = substr( $prelude, $index );
            if ( self::substantive( $source ) ) {
                $prefix = substr( $prelude, 0, $index );
                $text = $prefix . "== Source and credit ==\n\n" . substr( $text, $index );
                $operations[] = 'insert_source_heading_at_explicit_boundary';
                $prelude = $prefix;
            }
        }
        if ( !in_array( 'description', $names, true ) && self::substantive( $prelude ) ) {
            $visible = self::stripped( preg_replace( self::CATEGORY, '', self::masked( $prelude ) ) );
            if ( !preg_match( '~(*UCP)\A(?:https?://|(?:\*[ \t]*)?' . self::SOURCE_PREFIX . '|Photo provided by\b)~iu', $visible ) ) {
                $text = "== Description ==\n\n" . $text;
                $operations[] = 'insert_description_heading_over_existing_subject';
            }
        }

        $after = self::structuralIssues( $text );
        if ( self::payload( $original ) !== self::payload( $text ) ) {
            throw new RuntimeException( 'Substantive payload changed; hold the draft' );
        }
        if ( self::urls( $original ) !== self::urls( $text ) ) {
            throw new RuntimeException( 'Source URL sequence changed; hold the draft' );
        }
        $newIssues = array_values( array_diff( $after, $before ) );
        sort( $newIssues );
        return [
            'text' => $text, 'changed' => $text !== $original, 'operations' => $operations,
            'issues_before' => $before, 'issues_after' => $after, 'new_issues' => $newIssues,
            'all_payload_characters_retained' => true, 'all_urls_retained_in_order' => true,
            'source_disposition' => in_array( 'missing_source_and_credit_section', $after, true ) ? 'source_boundary_or_missing_information_needs_review' : 'standard_section_present',
        ];
    }
}
