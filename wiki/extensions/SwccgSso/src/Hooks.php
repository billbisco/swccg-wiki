<?php
namespace MediaWiki\Extension\SwccgSso;

use MediaWiki\Context\RequestContext;
use MediaWiki\Hook\BeforeInitializeHook;
use MediaWiki\Hook\SkinTemplateNavigation__UniversalHook;
use MediaWiki\Hook\UserLogoutCompleteHook;
use MediaWiki\Html\Html;
use MediaWiki\Logger\LoggerFactory;
use MediaWiki\MediaWikiServices;
use MediaWiki\Request\WebRequest;
use MediaWiki\SpecialPage\Hook\SpecialPageBeforeExecuteHook;
use MediaWiki\SpecialPage\SpecialPage;
use MediaWiki\User\Hook\UserLogoutHook;

class Hooks implements SpecialPageBeforeExecuteHook, SkinTemplateNavigation__UniversalHook,
	BeforeInitializeHook, UserLogoutHook, UserLogoutCompleteHook {

	/** id_token of the session being logged out (captured before the session is reset). */
	private static ?string $logoutIdToken = null;
	private static bool $logoutWasSso = false;

	/** Last 12 characters of the site sign-in session cookie (host-only __Host-swccg_sid, Path=/), or ''. */
	public static function siteSessionTail( WebRequest $request ): string {
		$raw = $_COOKIE['__Host-swccg_sid'] ?? '';
		return is_string( $raw ) && strlen( $raw ) >= 12 ? substr( $raw, -12 ) : '';
	}

	/**
	 * Sign-out everywhere: a wiki session that came from the site sign-in ends when the site session
	 * is gone (signed out at swccg.com/login or in Play/the forum) or belongs to someone else now.
	 */
	public function onBeforeInitialize( $title, $unused, $output, $user, $request, $mediaWiki ) {
		if ( !$user->isRegistered() ) {
			return;
		}
		$session = $request->getSession();
		$tail = $session->get( 'swccgsso-sid-tail' );
		if ( !is_string( $tail ) || $tail === '' ) {
			return; // local wiki password, BotPassword or older session: not ours to end
		}
		// #507: the sign-in service said (back-channel) that this site session ended
		$sid = $session->get( 'swccgsso-sid' );
		if ( is_string( $sid ) && $sid !== '' ) {
			$stash = MediaWikiServices::getInstance()->getMainObjectStash();
			if ( $stash->get( BackchannelLogoutHandler::sidKey( $stash, $sid ) ) !== false ) {
				$why = 'back-channel';
			}
		}
		// second line of defence: the site cookie changed or is gone
		if ( !isset( $why ) && self::siteSessionTail( $request ) === $tail ) {
			return;
		}
		LoggerFactory::getInstance( 'SwccgSso' )->info( 'site session ended ({why}): wiki sign-out of {id}',
			[ 'why' => $why ?? 'cookie', 'id' => $user->getId() ] );
		$session->remove( 'swccgsso-sid-tail' );
		$session->remove( 'swccgsso-sid' );
		$session->remove( 'swccgsso-id-token' );
		$user->logout();
		$output->redirect( $request->getFullRequestURL() );
	}

	public function onUserLogout( $user ) {
		$session = RequestContext::getMain()->getRequest()->getSession();
		$tail = $session->get( 'swccgsso-sid-tail' );
		self::$logoutWasSso = is_string( $tail ) && $tail !== '';
		$tok = $session->get( 'swccgsso-id-token' );
		self::$logoutIdToken = is_string( $tok ) && $tok !== '' ? $tok : null;
		return true;
	}

	/** Wiki sign-out also ends the site session (and with it Play and the forum, by back-channel). */
	public function onUserLogoutComplete( $user, &$inject_html, $oldName ) {
		$ctx = RequestContext::getMain();
		$cfg = $ctx->getConfig();
		$issuer = rtrim( (string)$cfg->get( 'SwccgSsoIssuer' ), '/' );
		if ( $issuer === '' || ( !self::$logoutWasSso && self::siteSessionTail( $ctx->getRequest() ) === '' ) ) {
			return;
		}
		$q = [
			'client_id' => $cfg->get( 'SwccgSsoClientId' ),
			'post_logout_redirect_uri' => 'https://swccg.com/wiki/Main_Page',
		];
		if ( self::$logoutIdToken !== null ) {
			$q['id_token_hint'] = self::$logoutIdToken;
		}
		$ctx->getOutput()->redirect( $issuer . '/end_session?' . http_build_query( $q, '', '&', PHP_QUERY_RFC3986 ) );
	}

	/** Big "site account" button above the local wiki login form. */
	public function onSpecialPageBeforeExecute( $special, $subPage ) {
		if ( $special->getName() !== 'Userlogin' || $special->getUser()->isRegistered()
			|| (string)$special->getConfig()->get( 'SwccgSsoIssuer' ) === '' ) {
			return;
		}
		$q = [];
		$rt = $special->getRequest()->getVal( 'returnto' );
		if ( $rt !== null && $rt !== '' ) {
			$q['returnto'] = $rt;
		}
		$url = SpecialPage::getTitleFor( 'SwccgSignIn' )->getLocalURL( $q );
		$special->getOutput()->addHTML(
			Html::rawElement( 'div', [ 'class' => 'swccgsso-box', 'style' => 'max-width:290px;margin:0 0 1.5em' ],
				Html::element( 'a', [ 'href' => $url, 'class' => 'cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--action-progressive cdx-button--weight-primary', 'style' => 'width:100%;justify-content:center' ],
					$special->msg( 'swccgsso-button' )->text() ) .
				Html::element( 'p', [ 'style' => 'font-size:90%;margin:.5em 0' ], $special->msg( 'swccgsso-button-help' )->text() ) .
				Html::element( 'p', [ 'style' => 'font-size:90%;color:#54595d' ], $special->msg( 'swccgsso-local' )->text() )
			)
		);
	}

	/** Personal tools: "Log in" goes to the site sign-in; the wiki password form stays at Special:UserLogin. */
	public function onSkinTemplateNavigation__Universal( $sktemplate, &$links ): void {
		if ( $sktemplate->getUser()->isRegistered() || (string)$sktemplate->getConfig()->get( 'SwccgSsoIssuer' ) === '' ) {
			return;
		}
		if ( isset( $links['user-menu']['login'] ) ) {
			$title = $sktemplate->getTitle();
			$q = [];
			if ( $title && !$title->isSpecialPage() ) {
				$q['returnto'] = $title->getPrefixedText();
			}
			$links['user-menu']['login']['href'] = SpecialPage::getTitleFor( 'SwccgSignIn' )->getLocalURL( $q );
		}
	}
}
