# SwccgSso

MediaWiki client of the swccg.com sign-in service (#267, #249). Deployed at
`/opt/swccg-wiki/extensions/SwccgSso` on gemp (copy these files; settings are in `extra-settings.php`).

- `Special:SwccgSignIn`: OIDC code + PKCE sign-in. The wiki account is the one whose id is the token's `sub`.
  A member with no wiki row gets one from the sign-in service when the wiki redeems the code (#516);
  if there is still none, the reader goes back to the page asked for, signed out, and the reason is logged.
- `rest.php/swccgsso/v1/backchannel-logout` (#507): OpenID Back-Channel Logout 1.0. A logout token with `sid`
  ends the wiki sessions started from that site session (checked on the next request); without `sid` it ends
  every wiki session of the account. Refused tokens (signature, issuer, audience `wiki`, `events`, `nonce`,
  replayed `jti`) get 400 and end nothing. The site-cookie check in `Hooks::onBeforeInitialize` stays as a
  second line of defence.
- Test-only fault switch (#516 AC2), off by default: membership ids listed one per line in
  `extensions/SwccgSso/.fault-no-row` are treated as having no wiki row. Delete the file to turn it off.
- Tests: `echo 'require "extensions/SwccgSso/tests/claims_check.php";' | php maintenance/run.php eval` in the wiki container.
