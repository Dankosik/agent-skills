---
name: postgres-performance
description: "PostgreSQL performance optimization and diagnosis through a tight evidence loop. Use when PostgreSQL performance or capacity is the task: slow queries or regressions; high CPU, I/O, locks, connections, WAL, replication lag, vacuum/bloat, or temp-file load; or requests to reduce database load or improve latency, throughput, or capacity through SQL, indexes, planner statistics, pooling, maintenance, configuration, or architecture."
---

# PostgreSQL Performance

The skill is a **tight evidence loop**:

`baseline -> bottleneck -> falsifiable hypothesis -> smallest intervention -> comparable delta`

Optimization lowers end-to-end workload cost while preserving correctness. Account for writes, tail latency, replicas, and maintenance.

Choose depth from the requested decision. Use the full loop for an optimization, capacity claim, configuration change, or production-readiness decision. For a narrow diagnosis or review, enter at the earliest unresolved link and inspect only evidence that can change the bottleneck verdict or make the recommendation unsafe. When direct evidence places the constraint outside PostgreSQL, stop at that boundary and name the discriminating probe; do not manufacture a database intervention. When no baseline exists, deliver a bounded collection plan rather than settings.

The final evidence check below applies to the links used; the numbered sections are a causal sequence, not mandatory report headings.

## Authority

- For answer, review, diagnose, or plan requests, inspect available code, plans, telemetry, and logs; run bounded read-only diagnostics; and report the result. Preserve the database state.
- For change, fix, or optimize requests, make in-scope local changes and run non-destructive validation without pausing for routine steps. Treat production DDL/DML, configuration changes, restarts, session cancellation, maintenance commands, and load tests as separate production actions requiring explicit authority.
- When the user authorizes one exact production action, keep that action's target and limits exact. Verify it with a fresh readback.

Ask a question when missing information changes this authority boundary or makes the next probe unsafe. Otherwise proceed with available evidence and label gaps.

For change requests, complete the evidence loop while safe in-scope work remains. An authorization boundary or concrete blocker ends the current run with the missing next action named.

## 1. Build a tight baseline

Establish from available code, telemetry, plans, and user context:

- the user-visible goal and protected invariants;
- PostgreSQL version, provider, topology, and relevant extensions;
- workload and time window, including recent deploys or data-shape changes;
- baseline latency distribution, throughput, error rate, and suspected constraint;
- the allowed environment and action scope.

Prefer an application SLO or business operation over a generic goal such as “lower CPU.”

## 2. Build the load profile

Read [references/diagnostics.md](references/diagnostics.md) before querying a live database or interpreting a supplied snapshot.

Classify the dominant pressure using time-aligned database, host, and application evidence:

- compute;
- storage or temp I/O;
- locks, transaction contention, or hot rows;
- connection or worker saturation;
- WAL, checkpoint, or replication pressure;
- vacuum, stale statistics, or table/index growth;
- demand outside PostgreSQL, such as application queueing or network latency.

Use deltas over the incident or benchmark window. Annotate cumulative counters, estimates, and sampled plans with their evidence limits.

## 3. Find the workload source

Rank work by total impact across the window. Retain dramatic single executions as tail evidence. Combine, where available:

- calls and total/mean execution time;
- p95/p99 latency from application telemetry;
- shared reads, temp I/O, WAL, rows, and planning time;
- wait events, blockers, long transactions, and replication lag;
- change-point correlation with deploys, traffic, and data distribution.

Preserve representative bind values and selectivities. Normalized SQL can hide parameter skew; averages can hide tail regressions.

## 4. Test the cause

For a target query, inspect the real SQL shape, schema, indexes, statistics, representative parameters, and plan. Use `EXPLAIN (ANALYZE, BUFFERS, WAL, SETTINGS, FORMAT JSON)` only when execution is safe and representative. `ANALYZE` executes the statement.

Test the leading hypothesis against its strongest competing explanation. Give each a discriminating prediction before probing it. Prefer the probe with the most information and least production cost; change one variable at a time.

Write each hypothesis as: `If <cause>, then <bounded probe> changes <observable>; falsified by <result>.`

## 5. Choose the smallest intervention

Read the matching branch in [references/interventions.md](references/interventions.md).

Verify version- or provider-specific behavior against current primary documentation before relying on it.

Climb this ladder and stop at the first rung that meets the target:

1. remove unnecessary calls, rows, columns, round trips, or transaction time;
2. repair query shape, index fit, or planner statistics;
3. reduce contention and bound connections or concurrency;
4. tune maintenance or a narrowly evidenced resource setting;
5. change schema, partitioning, replication, caching, or hardware.

For every candidate, state causal fit, expected metric movement, correctness constraints, write/storage/operational cost, rollout, and rollback. Prefer a session- or table-local experiment to a global setting.

## 6. Prove the delta

Control or record differences in data, parameters, concurrency, cache state, and observation duration. Declare the repetitions or duration before the run, use the same stopping rule before and after, and report the distribution rather than the best run. Measure:

- correctness and error rate;
- p50/p95/p99 latency and throughput at the target concurrency;
- CPU, physical and temp I/O, memory, locks, connections, WAL, and replica lag as relevant;
- plan shape and estimate accuracy;
- write amplification, index size, and maintenance cost introduced by the change.

Use a representative application replay or custom `pgbench` script for throughput claims. A single `EXPLAIN ANALYZE` contributes execution evidence; representative replay establishes capacity.

## 7. Report

Lead with the verdict. Include decision-changing evidence, material caveats, and the next action. Summarize raw artifacts by reference. Keep facts separate from inference:

For a narrow diagnosis, prefer `verdict -> decisive evidence -> cause/competitor -> one bounded probe or smallest intervention -> authority/gap`. Use the full template for optimization or readiness work.

```markdown
## Verdict
[What is constrained, by how much, and whether the target was met]

## Evidence
- Baseline/window: ...
- Load profile and workload source: ...
- Plan/wait evidence: ...

## Cause
[Causal finding, confidence, and competing explanation]

## Intervention
[State: proposed, tested locally, applied, or verified live; exact change, tradeoffs, rollout, rollback]

## Proof
[Fresh before/after evidence, or “not run” with the exact validation plan]

## Gaps
[Missing access/data, unverified production behavior, or next bounded probe]
```

Before claiming an optimization proven, check once that: a named repeatable baseline and protected invariants exist; time-aligned deltas identify the leading bottleneck and strongest competitor; the workload source or capacity ceiling is quantified; a falsifiable probe supports the cause; the selected intervention is the smallest causal fit with costs, failure signal, and rollback; and fresh comparable evidence covers correctness, tails, throughput, relevant resources, and introduced write, WAL, replica, or maintenance cost. Otherwise report the exact missing link instead of implying completion.
