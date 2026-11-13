<?php

namespace MediaWiki\Extension\GempAuth\Tests\Integration;

use MediaWiki\Extension\GempAuth\GempClient;
use MediaWiki\MediaWikiServices;

/** Test double: canned GEMP answers, records calls (password included, test-only). */
class FakeGempClient extends GempClient {
	/** @var array<string,array> username => result */
	public array $answers = [];
	public array $calls = [];

	public function __construct() {
		parent::__construct( MediaWikiServices::getInstance()->getHttpRequestFactory(), 'http://gemp.invalid/internal/v1/verify', str_repeat( 's', 32 ) );
	}

	public function verify( string $username, string $password, string $clientIp ): array {
		$this->calls[] = [ $username, $password, $clientIp ];
		return $this->answers[$username] ?? [ 'status' => self::INVALID ];
	}
}
