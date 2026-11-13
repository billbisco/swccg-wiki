<?php
# DEV / STAGING ONLY. Never require this on wiki.swccg.com.
# Until SES is approved (Primary Bot owns $wgSMTP), capture outgoing mail instead of sending it,
# so the confirm-email-to-edit flow can be exercised end to end.
# The full message (including the confirmation link) goes to the debug log file below.
$wgDebugLogGroups['gempauth-mail'] = '/tmp/gempauth-mail.log';
$wgHooks['AlternateUserMailer'][] = static function ( $headers, $to, $from, $subject, $body ) {
	$rcpt = implode( ', ', array_map( 'strval', (array)$to ) );
	wfDebugLog( 'gempauth-mail', "To: $rcpt\nSubject: $subject\n\n" . ( is_array( $body ) ? ( $body['text'] ?? '' ) : $body ) . "\n----\n" );
	return false;   # handled: UserMailer does not send
};
