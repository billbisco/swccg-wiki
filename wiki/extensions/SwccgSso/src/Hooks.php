<?php
namespace MediaWiki\Extension\SwccgSso;

use MediaWiki\Context\RequestContext;
use MediaWiki\Hook\BeforeInitializeHook;
use MediaWiki\Output\Hook\BeforePageDisplayHook;
use MediaWiki\Cache\Hook\HTMLFileCache__useFileCacheHook;
use HTMLFileCache;
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
	BeforeInitializeHook, UserLogoutHook, UserLogoutCompleteHook, BeforePageDisplayHook,
	HTMLFileCache__useFileCacheHook {

	/**
	 * #510: anonymous page copies saved in the wiki's HTML file cache before this time lack the
	 * tab-sync script tag. Such a copy is dropped (MediaWiki's own per-page invalidation, as after
	 * an edit) the first time it would be served, so the page is rendered and cached again.
	 */
	private const FILE_CACHE_EPOCH = '20261116012130';


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
		$issuer = rtrim( (string)$sktemplate->getConfig()->get( 'SwccgSsoIssuer' ), '/' );
		if ( $issuer === '' ) {
			return;
		}
		if ( $sktemplate->getUser()->isRegistered() ) {
			// #508: the wiki's Log out reads "Sign out" and is styled as a plain button (signout.css).
			if ( isset( $links['user-menu']['logout'] ) ) {
				$links['user-menu']['logout']['text'] = $sktemplate->msg( 'swccgsso-signout' )->text();
				$links['user-menu']['logout']['title'] = $sktemplate->msg( 'swccgsso-signout-tooltip' )->text();
				$links['user-menu']['logout']['class'] = trim( ( $links['user-menu']['logout']['class'] ?? '' ) . ' swccgsso-signout' );
			}
			// #587: an Account link to the swccg.com account page, just before Sign out.
			$account = [ 'swccgsso-account' => [
				'text' => $sktemplate->msg( 'swccgsso-account' )->text(),
				'title' => $sktemplate->msg( 'swccgsso-account-tooltip' )->text(),
				'href' => $issuer . '/account',
				'icon' => 'settings',
			] ];
			$links['user-menu'] = self::insertBefore( $links['user-menu'] ?? [], 'logout', $account );
			return;
		}
		$title = $sktemplate->getTitle();
		$q = [];
		if ( $title && !$title->isSpecialPage() ) {
			$q['returnto'] = $title->getPrefixedText();
		}
		$signIn = SpecialPage::getTitleFor( 'SwccgSignIn' )->getLocalURL( $q );
		if ( isset( $links['user-menu']['login'] ) ) {
			$links['user-menu']['login']['href'] = $signIn;
		}
		// #586: anonymous wiki account creation is off; "Create account" goes to the swccg.com sign-in
		// page (through Special:SwccgSignIn, so it comes back here), which has "Create a swccg.com account".
		$create = [
			'text' => $sktemplate->msg( 'swccgsso-createaccount' )->text(),
			'title' => $sktemplate->msg( 'swccgsso-createaccount-tooltip' )->text(),
			'href' => $signIn,
			'icon' => 'userAdd',
		];
		if ( isset( $links['user-menu']['createaccount'] ) ) {
			$links['user-menu']['createaccount'] = array_merge( $links['user-menu']['createaccount'], $create );
		} else {
			$links['user-menu'] = self::insertBefore( $links['user-menu'] ?? [], 'login', [ 'createaccount' => $create ] );
		}
	}

	/** Puts $add into $menu just before $key (or at the end when $key is missing). */
	private static function insertBefore( array $menu, string $key, array $add ): array {
		$out = [];
		foreach ( $menu as $k => $v ) {
			if ( $k === $key ) {
				$out += $add;
			}
			$out[$k] = $v;
		}
		return $out + $add;
	}

	/**
	 * #508: load the Sign out styles and the one-click handler for signed-in readers.
	 * The handler posts Special:UserLogout's own form (CSRF token included), so the sign-out goes
	 * through onUserLogoutComplete and on to the sign-in service with id_token_hint (#507),
	 * instead of core's API logout, which ends only the wiki session.
	 */
	public function onBeforePageDisplay( $out, $skin ): void {
		if ( (string)$out->getConfig()->get( 'SwccgSsoIssuer' ) === '' ) {
			return;
		}
		$out->addHeadItem( 'swccgsso-auth-sync', self::authSyncTag( $out ) );
		if ( !$out->getUser()->isRegistered() ) {
			return;
		}
		$out->addModuleStyles( 'ext.swccgSso.signout.styles' );
		$out->addModules( 'ext.swccgSso.signout' );
	}

	/**
	 * #510: every wiki page loads the site's shared tab-sync script (same origin, no inline JS),
	 * so an open wiki tab notices a sign-out in another tab. data-state:
	 *  - "in"  signed in through the site session: also checks /login/session/check when the tab
	 *          comes back into view;
	 *  - "out" anonymous: nothing to sign out of, so the page never reloads;
	 *  - none  signed in with a wiki password (bots, staff): reacts to a sign-out elsewhere, no check.
	 */
	public static function authSyncTag( $out ): string {
		$attrs = [
			'src' => '/login/static/auth-sync.js',
			'defer' => true,
			'data-check' => '/login/session/check',
			'data-cookie' => '__Host-swccg_out',
		];
		if ( !$out->getUser()->isRegistered() ) {
			$attrs['data-state'] = 'out';
		} elseif ( self::siteSessionTail( $out->getRequest() ) !== '' ) {
			$attrs['data-state'] = 'in';
		}
		return Html::element( 'script', $attrs );
	}

	/** Drop a file-cached page saved before FILE_CACHE_EPOCH (see the constant). Never blocks caching. */
	public function onHTMLFileCache__useFileCache( $context ) {
		static $seen = [];
		$title = $context->getTitle();
		if ( !$title || !$title->canExist() ) {
			return true;
		}
		$key = $title->getPrefixedDBkey();
		if ( isset( $seen[$key] ) ) {
			return true;
		}
		$seen[$key] = true;
		$cache = new HTMLFileCache( $title, 'view' );
		if ( !$cache->isCached() ) {
			return true;
		}
		$ts = $cache->cacheTimestamp();
		if ( $ts && $ts < self::FILE_CACHE_EPOCH ) {
			$cache->clearCache();
		}
		return true;
	}
}
