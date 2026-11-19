<?php
declare( strict_types = 1 );

require_once dirname( __DIR__ ) . '/chrome/image-description-normalizer.php';
$fixturePath = $argv[1] ?? __DIR__ . '/fixtures/image-description-standard.json';
$fixtures = json_decode( file_get_contents( $fixturePath ), true, 512, JSON_THROW_ON_ERROR );
$passed = 0;
foreach ( $fixtures as $fixture ) {
    $actual = SwccgImageDescriptionStandard::normalize( $fixture['text'] );
    $text = $actual['text'];
    unset( $actual['text'] );
    if ( hash( 'sha256', $text ) !== $fixture['expected_sha256'] || $actual !== $fixture['expected_meta'] ) {
        throw new RuntimeException( 'Normalization regression: ' . $fixture['title'] );
    }
    if ( SwccgImageDescriptionStandard::normalize( $text )['changed'] ) {
        throw new RuntimeException( 'Normalization is not idempotent: ' . $fixture['title'] );
    }
    $passed++;
}
echo $passed, " source-preserving image-description regression cases PASS\n";
