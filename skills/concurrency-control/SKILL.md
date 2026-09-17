---
name: concurrency-control
description: "Use for races on shared durable state: lost updates, conflicting writes, duplicate effects, leases, or stale-holder fencing."
---

# Interleaving-First Concurrency Control

**Interleaving.** Name the durable invariant and the schedule of reads and writes
that can break it. Choose the least complex sufficient mechanism under the real
store's isolation and failure model. Simultaneous activity alone is not a defect.

## Choose the requested result

For audit or diagnosis, inspect state, writers and evidence read-only; explain
the supported schedule and smallest closing mechanism. A plausible schedule is
not a claim that it was reproduced. For design, specify arbitration, conflict
and recovery at the requested fidelity. For build or fix, change the affected
owner and run focused local checks, repairing failures introduced by the change.

Releasing production locks, forcing leadership, repairing raced data and running
live load/fault tests require exact action, target and bounds authorization.
Preflight and freshly verify authorized operations. Host permissions still
apply; do not infer authority from credentials or a proposed test. Preserve
unrelated work and settled decisions outside the requested change.

## Identify the contested unit

Identify the row, key or cross-row invariant, and the writers that can affect it:
requests, retries, replicas, jobs, consumers, services and operators where relevant.
Reads feeding a write decision are part of the path. A missing writer is a
coverage gap, not evidence of a single-writer guarantee. Start from the affected
state rather than inventorying every writer in the entire system.

Construct the smallest counterexample: both actors read before either writes;
both pass a preflight check; they update disjoint rows after reading one predicate;
or a lease holder resumes after a successor acquires ownership. State the invalid
final state and the observation that distinguishes it from correct behavior.
If the invariant survives because effects commute, are idempotent or have a
verified single owner, retain that result rather than adding a lock by default.

## Select arbitration and conflict behavior

Read [mechanism choices](references/mechanisms.md) when choosing or reviewing
conditional writes, constraints, isolation, locks or fencing. It is a comparison
menu, not a requirement to reject every alternative one by one. Preserve an
existing sufficient mechanism unless the requested change exposes a concrete gap.

Check the actual isolation level, participating transaction/connection and
row-count or error result. All paths must use the arbiter. A preflight query,
process-local mutex or exclusive-looking lease name cannot establish durable
cross-process exclusion by itself.

Give losers an explicit disposition: surface conflict for a new decision, merge
when the domain permits, or retry from fresh state within time/attempt budgets.
Do not replay stale computations or multiply external effects. Preserve stable
operation identity, jitter retries, and consider starvation under the relevant
contention pattern. Cancellation or a timeout is not proof of rollback or absence
of a remote effect.

## Cover the selected failure windows

For a lease or leader, allow for pause, expiry, failover and return of a stale
holder. Reject stale durable effects with the authority's generation/fencing
check, or use effect idempotency and reconciliation that actually protect the
invariant. Give each scheduled occurrence its own stable identity.

For locks and transactions, identify relevant connection/crash cleanup, deadlocks,
acquisition ordering and bounded conflict recovery. A transaction-scoped row lock
is not a wall-clock lease. If the arbiter is unavailable, state fail-closed or
safe degraded behavior and the signal that reveals it. A hot-key retry storm
may need admission or serialization rather than more retries.

## Prove and finish

Force the implicated schedule with controlled coordination instead of relying
only on many randomly concurrent workers. Check the business invariant, conflict
result and committed state; the test should distinguish a missing mechanism.
For fencing, let the old holder resume after the new generation and verify its
effect cannot overwrite the successor. For deadlock handling, observe bounded
termination and the intended victim policy, not just a timeout in the test harness.

Use the real store when isolation, constraints or locks are the claim; in-memory
fakes can check orchestration, not those guarantees. Add bounded stress or load
work when contention, starvation or capacity is claimed or project policy requires
it, not as a gate for every diagnosis or narrow correctness change. Reuse existing
fixtures and valid results for the same revision/environment.

An analysis can finish with a supported schedule or precise missing evidence.
A requested runnable proof includes source, setup and assertions; label it unrun
when its dependency is absent. A local fix finishes with the requested change and
applicable checks, or the specific blocker. Do not invent a store cluster or
claim production safety from a weaker test. Report schedule, mechanism, conflict
path, observed evidence and residual windows without restating the whole ladder.

Adjacent job leases, broker ordering, provider idempotency, schema constraints and
PostgreSQL contention may use `durable-background-jobs`, `reliable-messaging`,
`external-api-integration`, `postgres-schema-design` or `postgres-performance`.
Load one only for a distinct unresolved decision; none is a prerequisite. Runtime
memory races belong to language-specific tooling, not this durable-state skill.
