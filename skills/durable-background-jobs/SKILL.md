---
name: durable-background-jobs
description: "Use for durable job acceptance, claims, leases, retries, schedules, checkpoints, cancellation, or crash-recovery decisions."
---

# Durable Background Jobs

**Lease.** A lease is expiring permission to attempt work, not proof that no other
attempt exists. Design overlapping attempts around stable business-effect
identity, conditional writes, a durable ledger or reconciliation; do not promise
exactly-once execution.

## Choose the branch

For audit/diagnosis, trace the affected producer-to-effect path read-only and
report the first supported illegal or ambiguous transition and a focused falsifier.
For design, provide the requested contract, matrix or code at the stated fidelity.
For build/fix, patch the relevant owner locally, run applicable checks and repair
introduced failures. Preserve accepted choices outside the requested change.

Production enqueue, requeue, schedules, cancellation, purge, drain, backfill,
repair and load/fault tests need explicit authorization for the action, targets
and bounds. Preflight and freshly read back authorized operations. Tools and
credentials do not expand authority. Keep secrets and sensitive payloads out of
artifacts. Ask only for a material missing decision, evidence or permission.

Scope the following criteria to the changed job and guarantee. A retry correction
does not require a new scheduler, engine comparison or full crash suite. A full
execution/recovery design must cover its reachable states and commit boundaries.

## Decide whether a job should exist

When acceptance is an open decision, retain synchronous work if the caller needs
the result and it reliably fits the request budget. Durable jobs earn their cost
when work must outlive the request/process or needs scheduling, bounded recovery,
checkpointing, throttling or latency isolation. Name completed-now, durably
accepted-with-ID or rejected-before-acceptance semantics. Do not reopen an agreed
job architecture for an unrelated narrow fix.

## Pin the engine and identities

Identify the engine/version, actual persistence and time source, producer, worker
and effect owner. Load only the relevant model before relying on its mechanics:
[database-backed](references/database-backed.md),
[visibility queue](references/visibility-queue.md), or
[durable execution engine](references/durable-engine.md).
Reference test menus remain conditional on the selected guarantee and authority.
Unknown engine behavior is a labelled assumption or gap, not a borrowed guarantee.

Keep logical job ID, producer deduplication key, attempt ID/lease generation,
schedule occurrence ID and business-effect key distinct. Define scope and retention
for identities in use. Payload/checkpoint versions, tenant and immutable input
references must remain meaningful across the worker versions that can receive them.

## Protect durable acceptance

When one database owns business state and job acceptance, commit them together.
Otherwise retain durable intent, such as an outbox, with the business decision
and reconcile publication. Enqueue-before-commit can create work for rolled-back
state; enqueue-after-commit can lose it. Treat a lost enqueue response as unknown,
retry with the same logical acceptance identity, and observe durable state.

## Define the lease and crash matrix

Use only states with distinct outcomes. A typical model has scheduled/queued,
leased, retry-wait, cancel-requested, succeeded, terminal-failed and quarantine.
Each transition has one atomic predicate/transaction/engine owner. Success means
the effect and required result committed before completion. Cancellation can lose
to an already committed effect; do not report that effect as reversed.

A lease names owner, attempt/generation, acquisition, expiry, renewal, time source
and maximum runtime. Condition renewal, checkpoint, completion and failure on
current ownership/state; observe stale-mutation rejection. A downstream effect
that cannot check a fence needs its own idempotency or reconciliation contract.
Size windows from relevant runtime/pause evidence. Uncertain renewal stops new
irreversible effects unless the existing effect contract makes them safe.

For a requested matrix or full recovery design, cover each reachable in-scope
acceptance, claim, effect/checkpoint, completion-loss and expiry boundary, plus
requested cancellation, schedule or deploy paths:

| State / crash point | Durable owner | Lease / commit fact | Next legal state | Disposition | Recovery | Signal | Executable test |
| --- | --- | --- | --- | --- | --- | --- | --- |

Preserve explicitly requested columns/counts. Mark impossible combinations with
the actual preventing constraint. Include terminal/quarantine dispositions when
retry/recovery is in scope; a narrow diagnosis may describe just the affected row.

## Make effects reentrant and failures bounded

Use stable business identity, not attempt identity. Prefer a transaction combining
effect and result, a unique effect ledger/conditional write, documented provider
idempotency with sufficient retention, or authoritative reconciliation. If effect
committed but completion is unknown, recover the recorded result before replay.

Distinguish transient, permanent, poison and operator-actionable failures. Give
reachable classes bounded retry, terminal, quarantine or owned recovery outcomes;
explain an impossible class only when a full classification is requested. Bound
attempts, elapsed/cost budget and tenant/global pressure, with backoff and jitter.
A delayed retry must not keep scarce capacity or multiply effects.

## Load operational branches only when needed

Read the relevant sections of [operations](references/operations.md) for fairness,
backpressure, civil schedules/misfires, checkpoints/cancellation, deploy/drain,
retention or operational/load proof. Do not load every branch because jobs exist.
Broker delivery, PostgreSQL schema/performance or cross-process orchestration may
need an adjacent skill, but names are routing hints, not mandatory calls. Keep
job transitions, identities and the requested result owned here.

## Prove the contract

Choose a test that would fail for the broken transition. Deterministic time and
logic tests can cover retry policy or civil-time calculations; real claim/renewal,
redelivery and stale-token claims need the relevant engine seam and competing
attempts. A handler mock or final counter alone does not prove lease expiry.
Use existing harnesses; include actual timing evidence when lease timing is claimed.

A full crash/recovery claim maps each in-scope invariant and matrix row to an
executable falsifier. A single requested proof stays one faithful scenario unless
omitting a named safety-critical condition invalidates it. Explicit executable
or runnable requests need test source, setup and exact assertions. Run suitable
local checks when available; label unrun proof and missing infrastructure honestly.
A sandbox/emulator does not automatically establish live provider behavior.

Finish the requested branch with findings/design, or implemented code and
applicable project checks, or authorized-operation readback. Reuse valid evidence
for the same revision/environment and fix introduced failures without repeated
approval. Missing live proof limits readiness, not unrelated local completion.
Do not invent new infrastructure or a full deploy/load campaign as a gate. Report
verdict, affected transitions/effects, actual proof, and authority/gaps; keep
proposed, implemented, tested and verified-live states distinct.
