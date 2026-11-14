<?php
/** Existing chrome application hooks; no installation or database migration. */
class SwccgCardImages {
    private static function manifestForTitle( $title ): ?array {
        if ( !$title || !is_readable( '/swccg-chrome/card-image-pilot.json' ) ) {
            return null;
        }
        $manifest = json_decode( file_get_contents( '/swccg-chrome/card-image-pilot.json' ), true );
        return is_array( $manifest ) && isset( $manifest['pages'][$title->getPrefixedText()] )
            ? $manifest : null;
    }
    public static function onNavigation( $skin, &$links ): void {
        $title = $skin->getTitle();
        $manifest = self::manifestForTitle( $title );
        $settingsTitle = $manifest && isset( $manifest['settingsPage'] )
            ? Title::newFromText( $manifest['settingsPage'] ) : null;
        if ( !$settingsTitle || !isset( $links['namespaces'] ) ) {
            return;
        }
        $selected = $title->equals( $settingsTitle );
        $tab = [
            'text' => wfMessage( 'swccg-card-images-settings-tab' )
                ->inLanguage( $skin->getLanguage() )->text(),
            'href' => $settingsTitle->getLocalURL(),
            'class' => $selected ? 'selected' : '',
        ];
        $tabs = [];
        foreach ( $links['namespaces'] as $key => $link ) {
            if ( $selected && isset( $link['class'] ) ) {
                $link['class'] = trim( preg_replace( '/\bselected\b/', '', $link['class'] ) );
            }
            $tabs[$key] = $link;
            if ( $key === 'talk' ) {
                $tabs['card-image-settings'] = $tab;
            }
        }
        if ( !isset( $tabs['card-image-settings'] ) ) {
            $tabs['card-image-settings'] = $tab;
        }
        $links['namespaces'] = $tabs;
    }
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
        $title = $out->getTitle();
        $manifest = self::manifestForTitle( $title );
        if ( !$manifest ) {
            return;
        }
        $messages = [];
        foreach ( [ 'original','remastered','group','setting','save','saved','failed' ] as $key ) {
            $messages[$key] = wfMessage( 'swccg-card-images-' . $key )
                ->inLanguage( $out->getLanguage() )->text();
        }
        // Only public rendition metadata and localized labels enter the page cache.
        $out->addJsConfigVars( 'swccgCardImagePilot', [
            'cards' => $manifest['cards'],
            'messages' => $messages,
            'settingsPage' => $title->getPrefixedText() === ( $manifest['settingsPage'] ?? '' ),
        ] );
        $out->addInlineStyle( file_get_contents( '/swccg-chrome/card-image-viewer.css' ) );
        $out->addInlineScript( file_get_contents( '/swccg-chrome/card-image-viewer.js' ) );
    }
}
$wgMessagesDirs['SwccgCardImages'] = '/swccg-chrome/i18n';
$wgHooks['GetPreferences'][] = 'SwccgCardImages::onGetPreferences';
$wgHooks['UserGetDefaultOptions'][] = 'SwccgCardImages::onUserGetDefaultOptions';
$wgHooks['SkinTemplateNavigation::Universal'][] = 'SwccgCardImages::onNavigation';
