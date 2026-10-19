<?php

namespace MediaWiki\Extension\GempAuth;

use MediaWiki\Auth\AbstractPasswordPrimaryAuthenticationProvider;
use MediaWiki\Auth\AuthenticationRequest;
use MediaWiki\Auth\AuthenticationResponse;
use MediaWiki\Auth\PasswordAuthenticationRequest;
use MediaWiki\Auth\TemporaryPasswordAuthenticationRequest;
use MediaWiki\Message\Message;
use MediaWiki\User\Options\UserOptionsManager;
use MediaWiki\User\UserIdentity;
use MediaWiki\User\UserIdentityLookup;
use MediaWiki\User\UserRigorOptions;
use StatusValue;

/**
 * Log in to the wiki with a GEMP (play.swccg.com) name and password.
 *
 * - Runs before LocalPassword (sort 50 < 100) and is non-authoritative: it ABSTAINS for every
 *   existing wiki account that is not linked to GEMP (Admin and the bot accounts keep their
 *   local passwords, and their passwords are never sent to GEMP).
 * - A GEMP login whose name maps to no wiki account auto-creates it and links it to the GEMP
 *   player id (user option gempauth-id; deliberately not a registered preference, so a user
 *   cannot set it through the API).
 * - Linked accounts have no wiki password: changes and resets happen on GEMP.
 */
class GempPrimaryAuthenticationProvider extends AbstractPasswordPrimaryAuthenticationProvider {
	public const LINK_OPTION = 'gempauth-id';
	private const SESSION_KEY = 'GempAuth:pendingLink';

	public function __construct(
		private GempClient $client,
		private UserIdentityLookup $userIdentityLookup,
		private UserOptionsManager $userOptionsManager,
		array $params = []
	) {
		parent::__construct( $params + [ 'authoritative' => false ] );
	}

	/** GEMP player id linked to this wiki user, or null. */
	public function getLinkedGempId( UserIdentity $user ): ?int {
		$v = $this->userOptionsManager->getOption( $user, self::LINK_OPTION );
		return ( $v === null || $v === '' ) ? null : (int)$v;
	}

	public function beginPrimaryAuthentication( array $reqs ) {
		$req = AuthenticationRequest::getRequestByClass( $reqs, PasswordAuthenticationRequest::class );
		if ( !$req || $req->username === null || $req->password === null || !$this->client->isConfigured() ) {
			return AuthenticationResponse::newAbstain();
		}
		$typed = trim( $req->username );
		$wikiName = $this->userNameUtils->getCanonical( $typed, UserRigorOptions::RIGOR_CREATABLE );
		if ( $wikiName === false ) {
			return AuthenticationResponse::newAbstain();
		}
		$existing = $this->userIdentityLookup->getUserIdentityByName( $wikiName );
		$linkedId = ( $existing && $existing->isRegistered() ) ? $this->getLinkedGempId( $existing ) : null;
		if ( $existing && $existing->isRegistered() && $linkedId === null ) {
			// Local-only wiki account: let LocalPassword handle it; never send its password to GEMP.
			return AuthenticationResponse::newAbstain();
		}

		$ip = $this->manager->getRequest()->getIP();
		$result = $this->client->verify( $typed, $req->password, $ip );
		switch ( $result['status'] ) {
			case GempClient::OK:
				break;
			case GempClient::INVALID:
				return $this->failResponse( $req );
			case GempClient::RESET:
				return AuthenticationResponse::newFail( wfMessage( 'gempauth-reset-required', $this->accountUrl() ) );
			case GempClient::BANNED:
				return AuthenticationResponse::newFail( wfMessage( 'gempauth-banned' ) );
			case GempClient::TEMP_BANNED:
				return AuthenticationResponse::newFail( wfMessage( 'gempauth-temp-banned',
					Message::dateTimeParam( wfTimestamp( TS_MW, $result['until'] ?? 0 ) ) ) );
			case GempClient::RATE_LIMITED:
				return AuthenticationResponse::newFail( wfMessage( 'gempauth-rate-limited',
					Message::durationParam( $result['retry_after'] ?? 60 ) ) );
			default:
				return AuthenticationResponse::newFail( wfMessage( 'gempauth-unavailable' ) );
		}

		// GEMP is case-sensitive; map its canonical name (not what was typed) to the wiki name.
		$gempId = $result['user']['id'];
		$mapped = $this->userNameUtils->getCanonical( $result['user']['name'], UserRigorOptions::RIGOR_CREATABLE );
		if ( $mapped !== $wikiName ) {
			return AuthenticationResponse::newFail( wfMessage( 'gempauth-name-mismatch' ) );
		}
		if ( $linkedId !== null && $linkedId !== $gempId ) {
			// e.g. GEMP "bill" and "Bill" both map to wiki "Bill": only the first linked one gets in.
			$this->logger->warning( 'GempAuth: {name} is linked to GEMP id {linked}, refused id {id}',
				[ 'name' => $wikiName, 'linked' => $linkedId, 'id' => $gempId ] );
			return AuthenticationResponse::newFail( wfMessage( 'gempauth-link-mismatch' ) );
		}
		if ( $linkedId === null ) {
			$this->manager->setAuthenticationSessionData( self::SESSION_KEY, [ 'name' => $wikiName, 'id' => $gempId ] );
		}
		return AuthenticationResponse::newPass( $wikiName );
	}

	public function autoCreatedAccount( $user, $source ) {
		$pending = $this->manager->getAuthenticationSessionData( self::SESSION_KEY );
		if ( $source !== $this->getUniqueId() || !is_array( $pending ) || $pending['name'] !== $user->getName() ) {
			return;
		}
		$this->userOptionsManager->setOption( $user, self::LINK_OPTION, (string)$pending['id'] );
		$this->userOptionsManager->saveOptions( $user );
		$this->manager->removeAuthenticationSessionData( self::SESSION_KEY );
		$this->logger->info( 'GempAuth: auto-created {name} linked to GEMP id {id}', $pending );
	}

	public function testUserExists( $username, $flags = 0 ) {
		// We never enumerate GEMP accounts from the wiki.
		return false;
	}

	public function providerAllowsAuthenticationDataChange( AuthenticationRequest $req, $checkData = true ) {
		if ( ( $req instanceof PasswordAuthenticationRequest || $req instanceof TemporaryPasswordAuthenticationRequest )
			&& $req->username !== null
		) {
			$user = $this->userIdentityLookup->getUserIdentityByName( $req->username );
			if ( $user && $user->isRegistered() && $this->getLinkedGempId( $user ) !== null ) {
				return StatusValue::newFatal( wfMessage( 'gempauth-password-on-gemp', $this->accountUrl() ) );
			}
		}
		return StatusValue::newGood( 'ignored' );
	}

	public function providerChangeAuthenticationData( AuthenticationRequest $req ) {
		// GEMP owns GEMP passwords; nothing is stored on the wiki.
	}

	public function accountCreationType() {
		return self::TYPE_NONE;
	}

	public function beginPrimaryAccountCreation( $user, $creator, array $reqs ) {
		return AuthenticationResponse::newAbstain();
	}

	private function accountUrl(): string {
		return (string)$this->config->get( 'GempAuthAccountUrl' );
	}
}
