/*!
 * #508/#507: Sign out signs out of the wiki, Play and the forum on this device.
 * Core turns the Log out link into an API logout, which ends only the wiki session and
 * never reaches the sign-in service. Instead, post Special:UserLogout's own form: SwccgSso's
 * UserLogoutComplete hook then sends the browser to the sign-in service's end_session with
 * id_token_hint, and the sign-in service signs out Play and the forum.
 */
( function () {
	'use strict';

	function signOut( href ) {
		var form = document.createElement( 'form' );
		form.method = 'post';
		form.action = mw.util.getUrl( 'Special:UserLogout' );
		var fields = { wpEditToken: mw.user.tokens.get( 'csrfToken' ), title: 'Special:UserLogout' };
		try {
			var rt = new URL( href, location.href ).searchParams.get( 'returnto' );
			if ( rt ) {
				fields.returnto = rt;
			}
		} catch ( e ) {}
		Object.keys( fields ).forEach( function ( k ) {
			var i = document.createElement( 'input' );
			i.type = 'hidden';
			i.name = k;
			i.value = fields[ k ];
			form.appendChild( i );
		} );
		document.body.appendChild( form );
		form.submit();
	}

	function isSignOutLink( el ) {
		return el && el.closest && el.closest( '#pt-logout a, a.swccgsso-signout' );
	}

	// Capture phase, so this runs before core's handler on the link itself.
	document.addEventListener( 'click', function ( e ) {
		var a = isSignOutLink( e.target );
		if ( !a || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey ) {
			return;
		}
		e.preventDefault();
		e.stopImmediatePropagation();
		signOut( a.href );
	}, true );

	// Vector 2022 keeps the user menu in a dropdown: show a copy beside it.
	$( function () {
		var $menu = $( '.vector-user-links .vector-user-links-main, .vector-user-links-main' ).first();
		var $orig = $( '#pt-logout a' ).first();
		if ( !$menu.length || !$orig.length || $( '.swccgsso-signout-bar' ).length ) {
			return;
		}
		$( '<span>' ).addClass( 'swccgsso-signout-bar' ).append(
			$( '<a>' ).addClass( 'swccgsso-signout' ).attr( { href: $orig.attr( 'href' ), title: $orig.attr( 'title' ) } )
				.text( mw.msg( 'swccgsso-signout' ) )
		).appendTo( $menu );
	} );
}() );
