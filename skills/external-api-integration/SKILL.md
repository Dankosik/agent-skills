---
name: external-api-integration
description: "Use for external HTTP provider or webhook contracts, bounded retries, request identity, ambiguous outcomes, authentication, or reconciliation."
---

# External API Integration

**Boundary.** A provider can commit an effect while its response is lost. Keep
operation identity and evidence from request through callback/poll and
reconciliation; an HTTP client alone is not an end-to-end contract.

## Match scope and authority

For a whole side-effecting flow, readiness, migration, replay or recovery redesign,
cover the full in-scope boundary. For review/diagnosis or a narrow correction,
follow the affected stage and safety-relevant dependencies. Side-effect-free reads
need only their actual contract, bounded attempt and result handling unless another
stage matters. Preserve accepted architecture outside the requested change.

Review, diagnosis and design are read-only. Build/fix permits in-scope local
changes and safe checks, followed by repair of introduced failures. Real provider
effects, credential/scope changes, webhook registration, production replay and
authoritative/destructive synchronization need exact environment, account,
operation set and bounds authorization. Preflight and freshly verify approved
actions; credentials and tools are not permission. Keep real tokens, codes,
signed payloads and sensitive bodies out of fixtures, logs and reports.

Use current official provider/version evidence when it can change the decision.
Distinguish documented guarantees, observations, local choices, inferences and
gaps. Ask only for missing input affecting authority, effect identity, correctness
or duplicate risk that available evidence cannot resolve.

## Load relevant mechanics

- [HTTP resilience](references/http-resilience.md) for attempt loops, transport
  phases, rate limits, polling or resumable pagination.
- [Authentication](references/authentication.md) for OAuth/token lifecycle,
  credential binding or rotation; a static credential alone does not require a
  lifecycle redesign.
- [Webhooks](references/webhooks.md) for receiver authentication, raw envelope,
  durable acknowledgement, ordering and callback recovery.

Use only applicable sections and checks. A timeout-parser change does not require
all three documents, sandbox provisioning or a new end-to-end platform. An explicit
runnable-test request still needs real test source, setup and assertions.

## Pin the affected contract

Identify provider, account/environment, operation, API/SDK version, request/response
shape, authentication/audience, error meanings, limits and evidence origin. Add
idempotency scope/retention, callback, pagination or lookup semantics when used.
A sandbox demonstrates only what it exercises, not production quotas or effects.

For interacting side effects keep one boundary ledger; a narrow task may use a
single row or equivalent prose:

| Effect or sync | Provider evidence | Local invariant | Identity/checkpoint | Deadline/acceptance | Ambiguity/recovery | Inference or gap | Authority |
| --- | --- | --- | --- | --- | --- | --- | --- |

Choose synchronous completion when the caller needs it and the full deadline
allows it; otherwise a durably accepted pending operation may need independent
observation. Do not reopen that accepted choice for an unrelated field change.
Pin callback versions separately where supported. Tolerate documented additive
fields but retain an incompatible/owned failure for an unknown required schema,
state or signature version; do not invent familiar meaning.

## Identity, attempts and outcomes

Give an intended side effect a stable operation ID before attempting it. Retain
provider/environment binding, canonical intent, idempotency scope/expiry and
request/resource IDs needed for lookup. Retries keep equivalent intent and the
same identity; a newly requested effect gets a new one. Prevent concurrent workers
from creating independent provider operations for the same local intent.

Without documented idempotency or proof of non-transmission, disable automatic
after-possible-send retries for side effects. Resolve provider state, a supported
reconciliation key or compensation policy rather than treating a timeout as
non-execution. HTTP status alone does not prove retry safety.

Budget queueing, authentication, DNS/connect/TLS, sending, headers/body, backoff and
parsing inside an end-to-end deadline. Bound attempts, response/decompression
size and quota-scoped concurrency; cancellation reaches waits and I/O. Independent
reconciliation can outlive a caller only with its own owner and budget. Honor
provider retry delays only within those limits.

Keep operationally distinct outcomes: succeeded with authoritative evidence;
permanent requiring change; retryable with safe identity and remaining budget;
ambiguous after possible effect; incompatible when the contract cannot be read
safely. Preserve redacted phase/request evidence. Unknown effect state is not a
successful or permanently failed business result.

## Observe and reconcile

Use the authoritative lookup or authenticated callback the provider supports.
Poll a status endpoint rather than repeating the write. Correlate by local and
provider identity; timestamps or arrival order do not create undocumented ordering.

Reconciliation handles overdue, ambiguous, failed-callback and divergent records
within a lookback/checkpoint contract. Apply only permitted transitions and keep
unresolved or incompatible cases visible and owned. Page checkpoints cannot skip
undurable item effects; replay must preserve identity, including permanent item
failures and deletion semantics. A single safe read does not need an invented
reconciliation daemon.

## Prove the claim and finish

Select evidence for the changed mechanism: contract fixtures for payloads and
classification; scripted transport/time for retries and ambiguous phases; a
provider sandbox for its actual behavior; an end-to-end flow for a cross-stage
claim. These are alternatives or complementary checks, not four mandatory stages
for every correction. Real webhook authentication requires the exact signed bytes
and provider scheme, not a mocked authenticated result.

A full side-effecting readiness or migration assessment must cover each ledger
row's identity, durable commits, uncertainty, bounded recovery, failure tests,
signals and authority. Rollout needs old/new routing ownership, canary/stop rules,
quota headroom and rollback that retains recovery for in-flight effects. Stopping
new routing does not erase existing external work. Use bounded-cardinality metrics;
keep operation IDs in appropriate redacted logs/traces instead of labels.

Complete diagnosis/design at its requested fidelity, marking unrun proofs. Complete
a local fix with applicable project checks and introduced-failure repair; reuse
valid same-revision/environment evidence. Missing sandbox or live evidence limits
the guarantee, not unrelated work. Do not create new accounts, credentials or test
platforms to satisfy an invented completion gate.

Lead with verdict, affected contract, cause/decision, correction, proof and limits.
Use ready/not-ready only for the readiness actually being assessed; a completed
analysis is not a claim of production readiness. Distinguish proposed, implemented
locally, sandbox-tested, deployed and verified live.

Public API, business ledger, messaging and database concerns keep their own owners.
Use `reliable-messaging`, `postgres-schema-design`, `postgres-performance` or
`auth-access-control` for a distinct unresolved question, not as compulsory calls.
Pass identity, invariant and evidence without redesigning excluded internals.
