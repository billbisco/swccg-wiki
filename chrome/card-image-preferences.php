<?php
/** Existing chrome application hooks; no installation or database migration. */
class SwccgCardImages {
    public static function onGetPreferences( $user, &$preferences ): void {
        $preferences['swccg-card-images'] = [
            'type' => 'radio',
            'label-message' => 'swccg-card-images-setting',
            'section' => 'rendering/files',
            'options-messages' => [
                'swccg-card-images-original' => 'original',
                'swccg-card-images-remastered' => 'remastered',
            ],
            'default' => 'original',
        ];
    }
    public static function onUserGetDefaultOptions( &$options ): void {
        $options['swccg-card-images'] = 'original';
    }
    public static function addPilot( $out ): void {
        if ( !is_readable( '/swccg-chrome/card-image-pilot.json' ) ) {
            return;
        }
        $manifest = json_decode( file_get_contents( '/swccg-chrome/card-image-pilot.json' ), true );
        $title = $out->getTitle();
        if ( !$title || !isset( $manifest['pages'][$title->getPrefixedText()] ) ) {
            return;
        }
        $messages = [];
        foreach ( [ 'original','remastered','group','setting','save','saved','failed' ] as $key ) {
            $messages[$key] = wfMessage( 'swccg-card-images-' . $key )
                ->inLanguage( $out->getLanguage() )->text();
        }
        // Only public rendition metadata and localized labels enter the page cache.
        $out->addJsConfigVars( 'swccgCardImagePilot', [ 'cards' => $manifest['cards'], 'messages' => $messages ] );
        $out->addInlineStyle( file_get_contents( '/swccg-chrome/card-image-viewer.css' ) );
        $out->addInlineScript( file_get_contents( '/swccg-chrome/card-image-viewer.js' ) );
    }
}
$wgMessagesDirs['SwccgCardImages'] = '/swccg-chrome/i18n';
$wgHooks['GetPreferences'][] = 'SwccgCardImages::onGetPreferences';
$wgHooks['UserGetDefaultOptions'][] = 'SwccgCardImages::onUserGetDefaultOptions';
