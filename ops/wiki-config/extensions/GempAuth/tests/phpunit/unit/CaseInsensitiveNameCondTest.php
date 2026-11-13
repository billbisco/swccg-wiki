<?php

namespace MediaWiki\Extension\GempAuth\Tests\Unit;

use MediaWiki\Extension\GempAuth\GempPrimaryAuthenticationProvider;
use MediaWikiUnitTestCase;
use Wikimedia\Rdbms\IReadableDatabase;

/** @covers \MediaWiki\Extension\GempAuth\GempPrimaryAuthenticationProvider::caseInsensitiveNameCond */
class CaseInsensitiveNameCondTest extends MediaWikiUnitTestCase {
	private function db( string $type ): IReadableDatabase {
		$db = $this->createMock( IReadableDatabase::class );
		$db->method( 'getType' )->willReturn( $type );
		$db->method( 'addQuotes' )->willReturnCallback( static fn ( $v ) => "'" . str_replace( "'", "''", $v ) . "'" );
		return $db;
	}

	public function testMysqlConvertsBinaryColumnAndQuotes() {
		$this->assertSame( "LOWER(CONVERT(user_name USING utf8mb4)) = 'admin'",
			GempPrimaryAuthenticationProvider::caseInsensitiveNameCond( $this->db( 'mysql' ), 'ADMIN' ) );
		$this->assertSame( "LOWER(CONVERT(user_name USING utf8mb4)) = 'ölaf'",
			GempPrimaryAuthenticationProvider::caseInsensitiveNameCond( $this->db( 'mysql' ), 'ÖLAF' ) );
		$this->assertSame( "LOWER(CONVERT(user_name USING utf8mb4)) = 'o''brien'' or 1=1 --'",
			GempPrimaryAuthenticationProvider::caseInsensitiveNameCond( $this->db( 'mysql' ), "O'Brien' OR 1=1 --" ) );
	}

	public function testSqlite() {
		$this->assertSame( "LOWER(user_name) = 'admin'",
			GempPrimaryAuthenticationProvider::caseInsensitiveNameCond( $this->db( 'sqlite' ), 'ADMIN' ) );
	}
}
