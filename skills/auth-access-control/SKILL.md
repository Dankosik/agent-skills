---
name: auth-access-control
description: "Use for authentication, permission enforcement, tenant isolation, identity propagation, or session and credential revocation decisions."
---

# Principal-First Auth and Access Control

**Principal.** Tie each protected effect to verified identity and an explicit
permission decision. Authentication establishes who acts; authorization decides
what that principal may do to this resource now. Deny when required identity,
tenant, scope, or context is missing or ambiguous.

## Choose the requested result

For review or diagnosis, inspect the affected credential-to-effect path read-only
and report the supported gap, escalation path, and smallest correction. For
design, deliver the requested contract and distinguish proposals from observations.
For build or fix, change the relevant enforcement or lifecycle owner and run
focused local checks, repairing failures introduced by the change. Do not stop
after the first patch merely to request review.

Production rotations, forced logout, revocation, permission backfills and live
security probes require authorization for the exact action, targets and bounds.
Preserve host permissions and unrelated work; a tool, credential, skill or test
result is not permission. Preflight and freshly verify authorized operations.
Never expose real credentials or personal data in code, fixtures or diagnostics.

Use the request and existing evidence to choose scope. An endpoint fix does not
require auditing every principal or redesigning sessions. A whole-system audit
must inventory its included entry points and disclose missing coverage. Keep
accepted decisions outside the requested change; ask only for a material missing
product decision, input or authority. Continue independent authorized work.

## Map identity to the effect

For the affected path, identify principal type, identifier, credential issuer,
verification, tenant membership, and lifecycle owner. Trace public, internal,
admin, job and consumer entry points when they can reach the same protected
effect. An internal name is not authentication; background work uses a narrow
service principal or a durably captured, revalidated user context, never ambient
superuser access. Delegation preserves both actor and subject identities.

Write the access rule before choosing RBAC, ABAC or ReBAC. Use roles for stable
bundles, attributes for contextual decisions, and relationships for ownership,
sharing or inheritance. Make principal, action, resource and decision context
explicit. Prefer a named, auditable rule over duplicated role-string policy;
syntax alone does not establish an escalation path.

Derive the allowed tenant scope from verified identity and current permissions.
A caller-supplied tenant or object ID is a selector to authorize, not authority to
widen that scope. Apply the boundary in queries, mutations, caches and background
work. Cross-tenant administration or guest sharing needs an explicit grant, not
a special-case bypass. Data-layer defenses do not replace the operation's rule.

## Enforce at the effect

Authorize the specific object and fields, not just the route. Reject fields the
caller may not set. Put enforcement where internal callers, jobs and consumers
cannot bypass the protected operation. Identify any other path that can perform
the same effect; do not claim whole-system coverage from one handler.

When a grant can change between check and effect and that gap is material,
coordinate the decision with the effect's transaction or supported concurrency
mechanism. A cached decision or token claim is a copy with a revocation/staleness
window, not permanently current authority.

## Credentials, sessions and propagation

Read [credential and revocation contracts](references/credentials-and-revocation.md)
when issue/verify/rotate/revoke/recover, sessions, tokens, OAuth, or stale access
is the decision. An object-level permission correction need not reopen these
mechanisms unless its safety depends on them.

For cross-service work, distinguish a service acting as itself from delegated
user access. Verify issuer, audience and the applicable credential contract at
each accepting boundary. Trust identity headers only across an enforced trusted
boundary that strips attacker-supplied values; otherwise use verifiable identity.
Use audience-restricted delegation or supported token exchange rather than
forwarding a credential to an unrelated audience. Async payloads retain needed
identity context, not a live user token assumed valid for the queue's lifetime.

Schema, cache freshness, external IdP transport and check/effect arbitration may
need `postgres-schema-design`, `cache-engineering`, `external-api-integration`
or `concurrency-control`. These names identify adjacent decisions, not required
skill calls or prerequisites. Keep auth semantics here and load a specialist
only for an unresolved question it can answer.

## Prove and finish

Choose a denial that would expose the affected flaw: cross-tenant or peer access,
privilege escalation, forged identity, missing rule, revoked session, stale claim,
or background access. Exercise the real enforcement path and assert that protected
data or effects did not escape, alongside intended allowed access. A UI denial or
fabricated principal does not prove credential verification.

For a lifecycle or system-readiness claim, cover every in-scope credential,
entry point and relevant revocation event, including observed maximum delays.
For a narrow fix, test its affected boundary rather than every item in this skill.
Runnable tests explicitly requested by the user need source, setup and assertions;
otherwise describe the discriminating check at the requested fidelity.

Finish analysis with supported findings or a precise evidence gap; finish a local
change with the requested result and applicable project checks. Reuse valid
results for the same revision and environment. Do not invent an integration
platform or claim live security from mocks. Missing live evidence limits the
claim, not unrelated work. Lead with verdict and impact, separating proposed,
implemented locally, tested and verified-live states.
