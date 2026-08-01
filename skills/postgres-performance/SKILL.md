---
name: postgres-performance
description: "PostgreSQL performance optimization and diagnosis through a tight evidence loop. Use when PostgreSQL performance or capacity is the task: slow queries or regressions; high CPU, I/O, locks, connections, WAL, replication lag, vacuum/bloat, or temp-file load; or requests to reduce database load or improve latency, throughput, or capacity through SQL, indexes, planner statistics, pooling, maintenance, configuration, or architecture."
---

# PostgreSQL Performance

The skill is a **tight evidence loop**:

`baseline -> bottleneck -> falsifiable hypothesis -> smallest intervention -> comparable delta`

Optimization lowers end-to-end workload cost while preserving correctness. Account for writes, tail latency, replicas, and maintenance.

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

**Completion criterion:** one named, repeatable measurement — command, query, replay, or pinned dashboard comparison — has already been run or read. It captures the target metric, comparison window or workload, environment, and protected invariants. When that artifact is unavailable, the run's deliverable is a bounded collection plan; resume the loop when evidence exists.

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

**Completion criterion:** a ranked load profile naming the leading bottleneck, the evidence for it, and the strongest competing explanation. If the evidence cannot distinguish them, say exactly which bounded probe will.

## 3. Find the workload source

Rank work by total impact across the window. Retain dramatic single executions as tail evidence. Combine, where available:

- calls and total/mean execution time;
- p95/p99 latency from application telemetry;
- shared reads, temp I/O, WAL, rows, and planning time;
- wait events, blockers, long transactions, and replication lag;
- change-point correlation with deploys, traffic, and data distribution.

Preserve representative bind values and selectivities. Normalized SQL can hide parameter skew; averages can hide tail regressions.

**Completion criterion:** one query family, transaction, maintenance process, application queue, or capacity limit has a quantified share of the target symptom or a measured capacity ceiling. Otherwise state the attribution gap and the next bounded measurement.

## 4. Test the cause

For a target query, inspect the real SQL shape, schema, indexes, statistics, representative parameters, and plan. Use `EXPLAIN (ANALYZE, BUFFERS, WAL, SETTINGS, FORMAT JSON)` only when execution is safe and representative. `ANALYZE` executes the statement.

Test the leading hypothesis against its strongest competing explanation. Give each a discriminating prediction before probing it. Prefer the probe with the most information and least production cost; change one variable at a time.

Write each hypothesis as: `If <cause>, then <bounded probe> changes <observable>; falsified by <result>.`

**Completion criterion:** the leading hypothesis survives a targeted probe and explains both the symptom and the observed plan or wait. Keep correlation labelled as correlation when no causal probe is possible. A resolved hypothesis enters Step 5; an unresolved run continues with the next bounded probe.

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

**Completion criterion:** the selected intervention is the smallest one that attacks the proven bottleneck, and its failure signal and rollback are known before execution.

## 6. Prove the delta

Control or record differences in data, parameters, concurrency, cache state, and observation duration. Declare the repetitions or duration before the run, use the same stopping rule before and after, and report the distribution rather than the best run. Measure:

- correctness and error rate;
- p50/p95/p99 latency and throughput at the target concurrency;
- CPU, physical and temp I/O, memory, locks, connections, WAL, and replica lag as relevant;
- plan shape and estimate accuracy;
- write amplification, index size, and maintenance cost introduced by the change.

Use a representative application replay or custom `pgbench` script for throughput claims. A single `EXPLAIN ANALYZE` contributes execution evidence; representative replay establishes capacity.

**Completion criterion:** fresh comparable evidence shows the target improved without violating protected invariants. When the target is missed, execute the predeclared rollback within current authority; otherwise name rollback as the required next action. Retain the evidence and test the next hypothesis.

## 7. Report

Lead with the verdict. Include decision-changing evidence, material caveats, and the next action. Summarize raw artifacts by reference. Keep facts separate from inference:

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
