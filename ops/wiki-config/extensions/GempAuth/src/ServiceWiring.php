<?php

use MediaWiki\Extension\GempAuth\GempClient;
use MediaWiki\MediaWikiServices;

return [
	'GempAuth.Client' => static function ( MediaWikiServices $services ): GempClient {
		$config = $services->getMainConfig();
		return new GempClient(
			$services->getHttpRequestFactory(),
			(string)$config->get( 'GempAuthEndpoint' ),
			(string)$config->get( 'GempAuthSecret' ),
			(int)$config->get( 'GempAuthTimeout' )
		);
	},
];
