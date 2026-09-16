# Credential and revocation contracts

Use only the credential and event branches implicated by the task. The root skill
owns task scope and authority; these criteria do not authorize production actions.

## Credential lifecycle and storage

For each in-scope credential define issue, verify, rotate, revoke and recover,
plus owner, scope, expiry and abuse limits. Prefer supported identity platforms
and standard primitives, not custom cryptography. Account recovery is an
authentication path, and changing MFA or a recovery channel needs appropriate
reauthentication. Bound guessing and avoid account enumeration through responses
or avoidable timing differences.

Store passwords with a suitable password hash, not reversible encryption. For
credentials the service only verifies, retain a verifier/hash when the protocol
permits. A provider refresh token, client secret or signing key that must be used
later cannot be replaced by a one-way hash: retain necessary material in the
existing protected secret facility with encryption, access restrictions and audit.
This is not permission to store bearer material in logs or general application
records. Separate credential storage needs from exposure to callers.

Use provider-supported authorization-code flows with PKCE and proper session,
state/nonce and redirect binding; use the appropriate service grant or workload
identity for service principals. Define secure browser/mobile storage from the
client threat model rather than treating every credential as interchangeable.

## Derive sessions from revocation requirements

For logout, compromise, role/scope downgrade and tenant/member removal that the
task covers, state the event, mechanism stopping old access, and maximum delay.
A full lifecycle design covers all applicable events. An unrelated endpoint fix
does not require a new four-event table.

Server-side sessions can support prompt revocation through a checked authority.
Self-contained access tokens remain usable until expiry unless a checked
revocation or policy mechanism intervenes. Short access tokens plus a protected
refresh lifecycle can bound stale access; cached roles and tenant claims obey
the same window. Accept waiting for expiry only when it meets the stated event
budget. A deleted client cookie does not invalidate a copied token.

Verify the applicable issuer, audience, expiry, allowed algorithm and signature;
select keys from the issuer's trusted key set, allow only bounded skew, and plan
rotation overlap. Claims visible to a token holder contain no secrets. If a policy
cannot tolerate claim staleness, reread its authority at the decision boundary.

Protect refresh-token replay according to client type and the provider contract.
RFC 9700 permits sender-constrained tokens or rotation for public clients; do not
replace a valid sender-constrained design merely to satisfy a rotation checklist.
When rotation is selected, retain family/generation binding, reject displaced
refresh tokens, and revoke the affected family on reuse under that contract.
Preserve an explicit requirement for rotation rather than silently substituting
another design. Concurrent refresh and uncertain outcomes require safe generation
updates and an owned recovery path.

## Evidence

Check actual denial after the relevant revocation event, including caches and
accepting services on that path. Record the observation window and worst observed
delay rather than claiming the configured TTL was measured. Exercise stale refresh
reuse or the selected sender constraint, key overlap, and the intended recovery
failure where they are in scope. A local simulated clock checks logic, not all
production propagation or clock behavior. Label designs and unrun tests accurately.

## Primary sources

- [OAuth security BCP, refresh-token protection](https://www.rfc-editor.org/rfc/rfc9700.html#section-4.14)
- [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

These clarify credential-specific constraints, not mandatory browsing for every
auth task. Verify material provider/version details for the selected environment.
