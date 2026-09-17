---
name: cache-engineering
description: "Use for cache key, freshness, fill, invalidation, failure behavior, or measured cache-value decisions across request, process, shared, or HTTP caches."
---

# Freshness-Oriented Cache Engineering

**Freshness.** A cache is a bounded copy, not authority. Follow the affected value
from source of truth through key, fill, serve and invalidation to recovery. Equal
keys must mean interchangeable values for the requesting principal.

## Choose scope and outcome

For a decide/design request, compare a cache with the simplest uncached path and
state the contract or a bounded measurement plan. For diagnosis/review, inspect
existing evidence read-only and locate the first violated link. For build/fix,
amend the affected contract and implementation, run focused local checks and
repair introduced failures. An accepted cache decision is not reopened merely
because a key or expiry needs fixing. For a performance claim, require comparable
baseline/candidate evidence; a correctness fix need not invent a benchmark.

Production flushes, bulk invalidation, eviction/configuration changes, resizing,
traffic cutover and load tests require explicit action, target and bounds
authorization. Preflight and freshly read back authorized operations. Keep host
permissions, secrets and user scope intact; installing this skill adds no authority.
Ask only for a material missing correctness, isolation or authority decision.

The contract and proof below apply to the cached values and guarantees in scope,
not every cache in the project. Full design/readiness or a material shared-cache
migration needs every relevant lifecycle field. A narrow change updates those it
affects, reuses established evidence and exposes consequential unknowns.

## Decide whether and where reuse pays

When the cache decision is open, pin workload, environment, time window, target
and origin work it could avoid. Distinguish latency, origin load and correctness.
Keep independent percentiles separate: subtracting origin p99 from end-to-end p99
does not establish removable tail latency. Use joint traces or a measured
counterfactual for that claim. No-cache or a collection plan is a valid outcome.

Choose the narrowest sharing boundary that meets the need: request memoization,
process-local reuse, shared remote state, or HTTP/private/shared-cache semantics.
Another layer must remove identifiable work and justify its failure surface.
Match cache-aside, read-through or write-through to ownership; refresh-ahead and
stale-while-revalidate require accepted staleness. Write-behind additionally needs
an explicit loss/durability budget and authoritative reconciliation.

Load only the layer whose mechanism affects the decision:

- [Request/process mechanics](references/request-process.md): local lifetime,
  memoization, single-flight, bounded memory and per-process invalidation.
- [Distributed mechanics](references/distributed.md): remote atomic operations,
  expiry, eviction, leases, failover and fallback.
- [HTTP/CDN mechanics](references/http-cdn.md): audience, headers, age,
  revalidation, effective keys and purge propagation.

Reference test and measurement menus are conditional on the affected property;
loading a reference does not authorize its operational examples or require its
whole test suite. Multi-layer claims retain each relevant layer's semantics.

## Keep one cached-value contract

For a material design, record one row per value with these fields. For a narrow
fix, reuse the existing row or state only changed fields and material gaps.

| Field | Decision |
| --- | --- |
| Authority | Source of truth, revision, create/update/delete owner |
| Value | Positive/negative/derived representation and serializer version |
| Key | Namespace, canonical inputs, resource, tenant, policy, representation and other response-varying dimensions |
| Freshness | Fresh lifetime, maximum age, permitted stale windows, read-your-writes and age source |
| Fill | Owner, deadline, admission, publication predicate and waiter behavior |
| Invalidate/expire | Mutation coverage, expiry backstop, delivery and reconciliation |
| Concurrency | Duplicate-fill scope and generation/version fence |
| Failure | Timeout, miss, eviction, corruption and partition dispositions; origin budget |
| Proof | Observable outcome, falsifier and actual evidence state |

Key scope includes the dimensions that change the returned value, not a ritual
list of fields. Canonicalize equivalent inputs; version incompatible key/value
meaning. Do not put raw tokens or sensitive data in keys/logs. Prefer reusable
policy-independent data plus current authorization at serving time when caching
final personalized responses cannot meet isolation and revocation requirements.

Classify serving as fresh, allowed-stale, forbidden-stale or unknown-age. Calculate
age from authoritative generation/validation, not just local insertion. Every
serve path enforces the stated bound. A negative result is not an origin error;
it has a defined lifetime and create-time invalidation. Unknown age follows an
explicit failure policy, not optimistic freshness.

## Make keys and fills safe

Trace producers, callers and invalidators implicated by a shared key change.
Test the actual lookup: equivalent requests reuse a value and response-varying
requests cannot retrieve each other's value. Key-string inequality alone does
not prove the cache path is isolated. Bound value size, decoding and retained
state; compression is a measured tradeoff, not an automatic improvement.

Bound active fills, queued work, waiter count/time and pending output. Collapse
equivalent work at the sufficient scope. A shared fill needs a bounded lifetime
independent of whichever caller happened to start it; caller cancellation may end
that wait without defining every peer's outcome. Specify shared error/retry behavior.

Publish only when the authority revision or generation still permits it. A
lease suppresses duplicate work but does not authorize stale publication. TTL
jitter spreads expirations; it does not establish ordering. Admit negative entries
only for authoritative absence, not timeouts or dependency failures.

## Invalidate, degrade and migrate

For cache-aside, commit authority before invalidating its copies. Lost invalidation
responses are ambiguous; retry idempotently or conditionally and reconcile. Close
the old-fill-after-writer-invalidation race with version/generation checks. TTL is
a bounded backstop, not a solution when missed delivery exceeds the age budget;
then use durable delivery and lag/reconciliation ownership.

Create supersedes negative entries; update/delete reach the dependent variants
and aggregates. Name each store's outcome unless a real atomic boundary includes
both. In an outage or cold fleet, bound origin fallback, retries and queueing.
Fail open only when capacity and semantics allow it; otherwise use safe allowed
stale data, bypass shared reuse, shed load or fail closed. Account for hot keys,
expiry/eviction skew and recovery demand where they can change the result.

For namespace, serializer or shared-isolation changes, preserve old/new coexistence
and define cold-fill cost, rollout observations, rollback/bypass and cleanup. A
multi-tenant incident needs meaningful same-ID separation, policy/revocation and
mixed-version evidence, not merely renamed keys. A request-local memoization change
does not need a distributed deployment plan.

## Verify and finish

Choose falsifiers for the changed property: equivalence/separation, update during
fill, negative-then-create, caller cancellation, late publication, corruption,
expiry, allowed/forbidden stale, outage, or recovery. Use controlled local fixtures
where sufficient and a real dependency when its semantics are the claim. Explicit
runnable-test requests need source, setup and assertions, not just test names.

For measured benefit, compare the same workload, data, concurrency, warmup, cache
state, duration and stopping rule. Report relevant latency distributions, errors,
origin cost and new resource/failure costs. Hit ratio explains a result; it does
not prove one. Full readiness includes the in-scope degraded, migration and
recovery paths. Unavailable production evidence stays a limit, not an inferred win.

Finish when the requested result and applicable checks are satisfied, or report
the precise blocker. Reuse evidence valid for the same revision/environment;
do not add unrelated test platforms, full outage campaigns or cleanup gates.
Report verdict, affected contract, change/cause, evidence and authority/gaps.
Distinguish proposed, implemented locally, tested, deployed and verified live.

Use `postgres-performance` for unresolved DB attribution and
`postgres-schema-design` for relational ownership when those decisions are
actually needed. Adjacent skills are optional expertise, not a compulsory chain.
