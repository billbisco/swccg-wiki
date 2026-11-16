/*!
 * #508/#507: Sign out signs out of the wiki, Play and the forum on this device.
 * Core turns the Log out link into an API logout, which ends only the wiki session and
 * never reaches the sign-in service. Instead, post Special:UserLogout's own form: SwccgSso's
 * UserLogoutComplete hook then sends the browser to the sign-in service's end_session with
 * id_token_hint, and the sign-in service signs out Play and the forum.
 */
( function () {
	'use strict';

	function post( action, fields ) {
		var form = document.createElement( 'form' );
		form.method = 'post';
		form.action = action;
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

	// Special:UserLogout's form carries its own token, so read the form and post it as is.
	function signOut( href ) {
		var url = mw.util.getUrl( 'Special:UserLogout' );
		fetch( url, { credentials: 'same-origin' } ).then( function ( r ) {
			return r.text();
		} ).then( function ( html ) {
			var doc = new DOMParser().parseFromString( html, 'text/html' );
			var f = doc.querySelector( '#mw-content-text form[method="post"], #mw-content-text form' );
			var tok = f && f.querySelector( '[name="wpEditToken"]' );
			if ( !tok ) {
				location.href = href;
				return;
			}
			var fields = {};
			Array.prototype.forEach.call( f.querySelectorAll( 'input[name]' ), function ( i ) {
				fields[ i.name ] = i.value;
			} );
			post( f.getAttribute( 'action' ) || url, fields );
		} ).catch( function () {
			location.href = href;
		} );
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
