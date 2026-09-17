---
name: postgres-performance
description: "Use to diagnose or improve PostgreSQL query latency, workload cost, contention, maintenance pressure, or database capacity."
---

# PostgreSQL Performance

**Evidence.** Use the unresolved part of the loop: baseline, bottleneck and source,
falsifiable cause, smallest intervention, comparable delta. A result locating the
constraint outside PostgreSQL is valid. Without enough baseline evidence, give a
bounded collection plan rather than invented settings or an unmeasured speedup.

## Requested result and authority

Answer, review, diagnose and plan requests preserve state while inspecting supplied
code, plans, telemetry and permitted bounded read-only probes. They do not require
implementation or a measured improvement to finish. Change/fix/optimize requests
permit in-scope local edits and non-destructive checks. Preserve accepted targets,
invariants and decisions outside the requested change.

Production DDL/DML, configuration, restarts, session cancellation, maintenance and
load tests require explicit authority for the action, target and bounds. Keep
that authorization exact, preflight the action and freshly read back its result.
A local test command is not safe merely because it runs from a local shell; check
its actual target. Preserve host permissions and protect sensitive evidence.

Ask only for missing inputs affecting authority, the decision or probe safety.
Otherwise proceed with labelled assumptions and gaps. Continue independent work
until the requested evidence bar or a concrete blocker is reached.

## Frame and attribute

Pin the user-visible target, protected invariants, environment, workload, window
and available repeatable baseline. Prefer the application operation over lower
CPU as an isolated objective. Do not request a full cluster inventory to interpret
one sufficiently documented plan.

Read the relevant [diagnostics section](references/diagnostics.md) when choosing a
live probe or interpreting its semantics. For multi-source bounded collection,
[tool routing](references/tool-routing.md) describes optional host-supported
batching and direct-call alternatives; it is not a required execution runtime.

Use aligned database, host and application evidence. Compare counter deltas within
one statistics epoch. Rank workload by total impact while retaining tails,
representative binds and selectivity; normalized SQL and averages can conceal
skew. Read only the supporting SQL, schema, indexes and statistics that can
change the proposed explanation.

## Test the cause and choose a correction

State the prediction before the cheapest safe probe distinguishing the leading
cause from a practical competitor. Label correlation until the evidence supports
causation. A blocked query can have a good plan; establish blocking ownership
before rewriting its victim.

`EXPLAIN ANALYZE` executes the statement. A surrounding rollback is not general
permission or a guarantee against side effects, locks and resource impact. Use
execution only within an understood safe target and bound; otherwise inspect
existing evidence or an appropriate non-executing plan. Preserve statistics-reset,
privacy and instrumentation-overhead safeguards in the diagnostics reference.

After causal support, read the matching [intervention branch](references/interventions.md)
and verify material version/provider behavior. Prefer removing unnecessary work,
repairing query/index/statistics fit, reducing contention/admission, then narrowly
justified maintenance/configuration or structural changes. Compare only plausible
alternatives; no transcript rejecting every ladder rung is required.

For a proposed change explain causal fit, expected movement, correctness,
write/storage/maintenance costs, failure signal and rollback. Prefer session/table
scope to a global setting when sufficient. An explicitly agreed local correction
need not restart discovery, but cannot be called faster without measurements.

## Verify at the claimed level

For local implementation, use existing relevant checks and repair introduced
failures, rather than stopping at the first patch or building a new database
platform. Reuse valid evidence for the same revision, environment and workload.
A skipped migration or absent target engine remains unverified.

For a measured optimization, use comparable data, parameters, concurrency, cache
conditions, observation window and stopping rule. Declare samples/duration before
running; report distributions, not the best rerun. Measure the target and relevant
correctness, write, replica and maintenance costs. Include p95/p99 for tail-latency
or capacity claims when the sample supports them; insufficient samples are a gap,
not a licence to invent tails. A single plan contributes execution evidence but
cannot establish application capacity; that needs representative workload replay.

## Report and finish

Lead with verdict, decisive evidence, cause/competitor, correction or next probe,
proof state and material gaps. Distinguish proposed, locally tested, applied and
verified live. Bound conclusions to the observed window. A diagnosis finishes
with its supported explanation or a precise next observation; a local change
finishes with its result and applicable checks. Full production or capacity proof
is required only when that is the promised result, not because this skill was
loaded. Keep raw artifacts referenced rather than copied into every section.
