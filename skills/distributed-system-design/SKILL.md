---
name: distributed-system-design
description: "Forces-driven design and review of cross-component distributed systems. Use for service boundaries, interactions, data ownership, consistency, replication, partitioning, scalability, availability, multi-region behavior, failure isolation, capacity, migration, or architectural tradeoffs. Route a single messaging, external-API, background-job, cache, or PostgreSQL mechanism to its dedicated skill; use this skill to compose multiple mechanisms into one system contract."
---

# Forces-Driven Distributed System Design

Design from **forces**, not from a catalog:

`requirements -> forces -> estimates -> simplest topology -> contracts -> failure model -> evolution -> proof`

Every component and edge must pay for its complexity by satisfying a named requirement or constraint. A pattern is a candidate response to forces, not a default architecture.

## Run contract

Reuse supplied evidence and settled decisions; inspect only what can change the design. Read only reference branches whose stated conditions match the current forces.

- For design, review, diagnosis, or planning, inspect available requirements, code, schemas, diagrams, telemetry, incidents, and deployment artifacts; preserve repository, infrastructure, and production state.
- For build or change requests, make in-scope local changes and run safe, non-destructive validation.
- Treat provisioning, deployment, traffic changes, failover, data movement, production load or fault tests, credential changes, and destructive actions as separate production actions requiring explicit authorization. Keep an authorized target and its limits exact, then verify it with fresh readback.

Continue safe, in-scope inspection, local edits, and validation without pausing for routine approval. Ask only when two plausible meanings materially change identity, money, consistency, availability, security, data residency, or an irreversible boundary; otherwise continue with labelled assumptions. Verify material provider-, product-, version-, and pattern-specific claims against current primary documentation, and separate sourced facts from inference. Keep proposed, validated locally, deployed, and verified live states distinct.

Stop when the requested artifact and applicable completion criteria are satisfied, or when a concrete blocker or authorization boundary is reached. Name the exact missing evidence, decision, or next action rather than expanding the architecture speculatively.

This skill owns system composition and cross-component contracts. Hand detailed mechanism work to the matching skill while retaining the end-to-end requirement:

| Concern | Handoff |
| --- | --- |
| Broker delivery, ordering, redrive, replay | `reliable-messaging` |
| Third-party API or webhook boundary | `external-api-integration` |
| Durable worker, lease, schedule, backfill | `durable-background-jobs` |
| Cache key, freshness, invalidation, degradation | `cache-engineering` |
| PostgreSQL relations and constraints | `postgres-schema-design` |
| PostgreSQL query or capacity bottleneck | `postgres-performance` |

## 1. Frame the forces

Turn the request, supplied evidence, and settled decisions into:

- the functional boundary, actors, critical operations, and business invariants;
- latency, availability, durability, freshness, throughput, RPO, and RTO targets per critical journey;
- data classification, tenant and authorization boundaries, residency, retention, and audit requirements;
- current topology, migration constraints, team ownership, delivery horizon, budget, and operated technologies;
- the requested decision or artifact and the evidence needed to call it ready;
- facts, inferences, assumptions, and unresolved decisions.

Use precise targets where the user supplied them. When a target is missing, preserve it as a variable or bounded assumption rather than inventing precision.

**Completion criterion:** every supplied requirement is classified as a functional invariant, measurable quality target, hard constraint, explicit assumption, or open decision; conflicts are visible; the design question, protected invariants, requested artifact, and readiness bar are stated.

## 2. Quantify the load envelope

For every design-driving path, estimate the dimensions that can change the topology:

- average, peak, and burst request or event rate;
- service time and concurrent in-flight work;
- payload, fan-out, network throughput, and cross-region traffic;
- write/read ratio, storage growth, retention, replication, and index or derived-data amplification;
- tenant or key skew, hot partitions, batch size, and retry or replay amplification;
- degraded and recovery load after a dependency, zone, or region returns.

Show formulas, units, ranges, and sensitivity to the largest assumptions. Read [references/capacity-and-topology.md](references/capacity-and-topology.md) when capacity, decomposition, sharding, cells, or independent scaling may affect the design.

**Completion criterion:** each critical path has a numeric envelope or an explicit formula awaiting named inputs; dominant scale axes, skew, expected headroom, and the first plausible resource ceiling are identified.

## 3. Draw the simplest viable topology

Start from the current system, or from one deployable and one authoritative store for a greenfield design. Add a network boundary, copy, queue, cache, partition, service, region, or control plane only when a force requires independent scaling, failure containment, data or trust ownership, deployment lifecycle, geographic locality, or a different consistency or latency contract.

For every component, record:

- one responsibility and the force that requires it;
- owned state and source-of-truth status;
- synchronous and asynchronous interfaces;
- scaling unit, failure domain, trust boundary, and operator;
- dependencies needed to serve or recover.

**Completion criterion:** every component has one named responsibility, state owner, scaling and failure boundary, and requirement that justifies it; every critical operation is traceable through the topology and named handoff owners.

## 4. Define state and interaction contracts

For each edge, specify protocol and direction, operation or message identity, schema and compatibility, deadline, retry ownership, ordering, concurrency or backpressure, idempotency, acknowledgement or response semantics, authentication and authorization, and observability.

For each critical operation, trace the read and write path and name:

- the authoritative state and transaction boundary;
- the consistency and freshness required by that operation;
- replicas, partitions, derived copies, and their lag or conflict behavior;
- the response exposed during success, uncertainty, degradation, and recovery;
- reconciliation for any state that can diverge.

Read [references/data-and-coordination.md](references/data-and-coordination.md) when state crosses a process, partition, replica, datastore, or region, or when ordering, consensus, distributed transactions, sagas, CQRS, or materialized views are considered.

**Completion criterion:** every stateful flow has one authority, explicit commit points, bounded guarantees on every edge, and a named divergence and reconciliation model; every correctness claim names the mechanism and guarantee that establish it.

## 5. Break the design

Read [references/resilience-and-load.md](references/resilience-and-load.md) whenever the design has a remote dependency, retry, queue, failover, autoscaling, or availability target.

Build a failure matrix for critical components and edges:

| Failure or overload | Detection | Containment/degraded behavior | Recovery/reconciliation | User-visible result | Signal and test |
| --- | --- | --- | --- | --- | --- |

Include slow and partial failures, exhausted resources, retry amplification, backlog growth, stale or duplicate data, process and host loss, dependency and control-plane loss, zone or region loss where applicable, and security or tenant-isolation failures. Recalculate remaining capacity under the failure scenario; redundancy that cannot carry failover load does not meet an availability target.

**Completion criterion:** every critical journey has a bounded failure and overload response, remaining-capacity assumption, recovery owner, observable signal, and executable test; required outcomes remain bounded under unreliable networks, delayed failover, and finite queues.

## 6. Compare alternatives and earn patterns

When the choice is material, compare the simplest viable design with its strongest practical alternative; for a review, compare the current design with the smallest viable correction. Evaluate both against requirements, capacity, consistency, failure containment, operational burden, security, cost, delivery time, and future change. If no alternative could change the decision, record that and end the comparison.

Record each material pattern decision as:

`forces -> chosen pattern -> guarantee -> cost/new failure mode -> rejected alternative -> falsifier`

Prefer a managed or already-operated primitive when it provides the required contract. A familiar pattern that changes no decision is reference, not architecture.

**Completion criterion:** the selected design wins on stated priorities or exposes an explicit unresolved tradeoff; every material pattern resolves named forces and its added failure modes and falsifier are recorded; the comparison contains only alternatives that could change the decision.

## 7. Design evolution and proof

Read [references/evolution-and-multi-region.md](references/evolution-and-multi-region.md) when the design changes an existing system, spans regions, promises disaster recovery, or requires mixed-version operation.

Define:

- version compatibility and coexistence of old and new components;
- data migration, backfill, validation, cutover, rollback or roll-forward, and cleanup;
- deployment order, blast-radius controls, and abort signals;
- load, consistency, fault, recovery, security, and restore tests;
- production signals that prove SLOs and reveal saturation or divergence.

Map each high-risk assumption to current evidence or to a named validation with environment, workload, expected observation, stopping rule, and owner.

**Completion criterion:** every high-risk assumption and quality target has evidence or an executable validation plan; rollout, mixed-version behavior, recovery, and rollback or roll-forward are defined before the design is called ready.

## 8. Report the design

Lead with the verdict. Preserve the requirements, decisions, evidence, material caveats, and next action; trim introductions, repetition, generic pattern explanations, and optional background first. Keep facts separate from inference. Include a Mermaid diagram when three or more components or failure domains interact. Use this template as a menu and omit empty sections:

```markdown
## Verdict
[Recommended design, boundary, readiness state, and decisive forces]

## Requirements and assumptions
| Item | Target or assumption | Evidence/status |
| --- | --- | --- |

## Capacity envelope
| Flow | Peak/burst | Data and fan-out | First ceiling/headroom |
| --- | --- | --- | --- |

## Architecture
[Mermaid diagram plus component responsibility and data ownership]

## Interaction and state contracts
| Edge/flow | Identity and commit | Consistency/ordering | Deadline/backpressure | Recovery |
| --- | --- | --- | --- | --- |

## Failure and recovery
[Failure matrix, degraded modes, remaining capacity, RPO/RTO]

## Decisions and tradeoffs
[Forces, patterns earned, strongest alternative, and falsifiers]

## Evolution and proof
[Compatibility, migration, rollout, rollback/roll-forward, and tests]

## Handoffs and gaps
[Dedicated skills, missing evidence, open decisions, and next action]
```

**Completion criterion:** every material requirement, component, state owner, interaction guarantee, capacity assumption, failure response, decision, validation, and gap is traceable in the report, and the verdict makes readiness unambiguous.
