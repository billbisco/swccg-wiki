<?php

namespace MediaWiki\Extension\GempAuth;

use MediaWiki\Config\Config;
use MediaWiki\Permissions\Hook\GetUserPermissionsErrorsHook;
use MediaWiki\User\Hook\SpecialPasswordResetOnSubmitHook;
use MediaWiki\User\Options\UserOptionsLookup;

/**
 * Level 3 of the approved login plan: editing content pages needs the editcontent right,
 * which the implicit autopromote group "emailconfirmed" (APCOND_EMAILCONFIRMED) grants.
 * Talk pages, user pages and other namespaces outside the gate stay editable by any
 * logged-in user. This deliberately does not use $wgEmailConfirmToEdit (which blocks talk too).
 */
class Hooks implements GetUserPermissionsErrorsHook, SpecialPasswordResetOnSubmitHook {
	public const GATED_ACTIONS = [ 'edit', 'create', 'createpage', 'move', 'move-target', 'upload', 'reupload', 'editcontentmodel' ];

	public function __construct( private Config $config, private UserOptionsLookup $userOptionsLookup ) {
	}

	/** @return int[] */
	public function getGateNamespaces(): array {
		$ns = $this->config->get( 'GempAuthEmailGateNamespaces' );
		if ( is_array( $ns ) ) {
			return array_map( 'intval', $ns );
		}
		$ns = array_merge( $this->config->get( 'ContentNamespaces' ),
			[ NS_PROJECT, NS_TEMPLATE, NS_HELP, NS_CATEGORY, NS_FILE ] );
		foreach ( [ 'NS_CARD', 'NS_MODULE' ] as $c ) {
			if ( defined( $c ) ) {
				$ns[] = constant( $c );
			}
		}
		return array_values( array_unique( array_map( 'intval', $ns ) ) );
	}

	public function onGetUserPermissionsErrors( $title, $user, $action, &$result ) {
		if ( !in_array( $action, self::GATED_ACTIONS, true ) || !$user->isRegistered()
			|| !in_array( $title->getNamespace(), $this->getGateNamespaces(), true )
			|| $user->isAllowed( 'editcontent' )
		) {
			return true;
		}
		$result = [ 'gempauth-confirm-email-to-edit' ];
		return false;
	}

	public function onSpecialPasswordResetOnSubmit( &$users, $data, &$error ) {
		foreach ( $users as $user ) {
			$id = $this->userOptionsLookup->getOption( $user, GempPrimaryAuthenticationProvider::LINK_OPTION );
			if ( $id !== null && $id !== '' ) {
				$error = [ 'gempauth-password-on-gemp', $this->config->get( 'GempAuthAccountUrl' ) ];
				return false;
			}
		}
		return true;
	}
}
