---
name: distributed-system-design
description: "Use for cross-component topology, ownership, consistency, capacity, failure-isolation, migration, or multi-region architecture decisions."
---

# Forces-Driven Distributed System Design

**Forces.** Every component, edge and pattern earns its cost through a named
requirement. Prefer the simplest topology whose contracts meet the stated load,
failure and evolution needs, rather than working through a pattern catalog.

## Choose depth and authority

For end-to-end design, readiness, migration or a material guarantee change, trace
the full in-scope chain. For a narrow review or correction, follow only the journey
and dependencies that change its verdict or safety. Preserve accepted decisions
outside the requested change. A no-distribution result or bounded evidence plan
is valid; missing inputs remain variables, assumptions or gaps.

Review, diagnosis and design preserve state. A build/change request permits local
in-scope implementation and appropriate non-destructive checks, including repair
of introduced failures. Provisioning, deployment, traffic/failover changes, data
movement, credentials and production load/fault tests need exact target/action/
bounds authorization. Preflight and freshly verify authorized operations. Host
permissions and confidentiality remain binding.

Check material provider/version claims against current primary documentation.
Do not invent features or borrow another product's guarantees. Ask only for a
material missing user-owned choice or authority; use available evidence for
routine technical decisions and continue independent permitted work.

## Frame the forces and load

Identify the functional boundary, actors, invariants and critical journeys. Keep
supplied latency, availability, durability, freshness, throughput, RPO/RTO,
tenancy, residency and retention targets exact. Record current topology, operated
technologies and ownership when they constrain the requested decision. Expose
contradictions rather than silently replacing a target with an easier one.

Estimate only dimensions that can change the design: peak/burst rate, service
time and concurrency, payload/fan-out, retained storage and replication/index
amplification, hot-key skew, retries and recovery catch-up. Show units, assumptions,
ranges and sensitivity; keep independent quantities independent. Use
[capacity and topology](references/capacity-and-topology.md) when sizing,
decomposition, sharding or failure-domain capacity is actually at issue.

## Choose topology and contracts

Start from the current design, or one deployable and one authority for greenfield
work. Earn another network boundary, copy, queue, cache, region or control plane
through independent scale, ownership, isolation, lifecycle or a different contract.
For a full design, each component names responsibility, owned state, interfaces,
scaling/failure unit, trust boundary and operator. A narrow review amends only
those facts implicated by its finding.

For a critical interaction identify protocol, direction, operation/message
identity, schema compatibility, deadline, retry owner, ordering, admission,
authentication and acknowledgement meaning. For a stateful journey name authority,
transaction/commit, read/write consistency, derived copies, allowed lag/conflict,
uncertain outcomes and recovery. Load [data and coordination](references/data-and-coordination.md)
for the selected replica, partition, transaction or materialization question,
not to read every distributed mechanism in advance.

## Challenge failure and alternatives

Load [resilience and load](references/resilience-and-load.md) when remote failure,
retry amplification, queueing, failover or an availability guarantee changes the
verdict. Map each in-scope material failure to detection, containment/degradation,
recovery, user-visible result, signal and falsifier. Cover slow/partial failures,
resource exhaustion, shared dependencies, stale/duplicate data and recovery load
where reachable. A redundancy claim requires capacity in its stated failure mode.

Compare the simplest viable choice with its strongest practical alternative when
that can change the decision. Explain guarantee, new failure/cost, rejected
alternative and falsifier. Do not reconstruct an entire alternatives matrix for
a settled design's local fix or introduce distribution only because it is the
skill's topic.

## Evolution and proof

Use [evolution and multi-region](references/evolution-and-multi-region.md) for
actual mixed-version, migration, regional-loss, restore or failback decisions.
Changing any file in an existing system is not by itself that trigger.

For the selected transition identify old/new compatibility, migration/backfill,
verification, cutover, temporary owners/removal conditions and rollback. Name the
last rollback-safe state and first irreversible/new-only write, who can cross
that boundary and the roll-forward/repair path. Recovery claims include the state
and dependencies needed to restore service, not merely redundant compute.

Map high-risk assumptions to existing evidence or a validation plan specifying
environment, workload, expected observation and stop condition. Design can specify
fault/load/restore checks without running them. Local implementation uses the
smallest check retaining the mechanism; live guarantees require live evidence
within authority. Reference proof menus do not authorize operational execution
or require every listed test for a narrow design question.

## Report and finish

For narrow work, report verdict, affected contract, cause/decision, correction and
proof/gap. For full-chain work use [reporting](references/reporting.md), retaining
all material requirements, numeric envelopes or missing inputs, contracts,
failure/evolution decisions and evidence states. A diagram is useful when it
clarifies interacting boundaries; honor an explicit diagram request, not an
arbitrary component-count rule. Omit empty sections and repeated pattern tutorials.

Finish when the requested artifact and applicable criteria are satisfied or a
concrete blocker is reported. Implementation continues through applicable checks
and introduced-failure repair; reuse valid same-revision/environment evidence.
Separate proposed, locally validated, deployed and verified-live states. Do not
create a new infrastructure campaign to finish an otherwise bounded analysis.

Use `reliable-messaging`, `external-api-integration`, `durable-background-jobs`,
`cache-engineering`, `postgres-schema-design` or `postgres-performance` only for
an unresolved mechanism decision they own. Pass the requirement and evidence,
not a ceremonial handoff. Their absence does not block reasoning that can be
completed here, and their names do not require automatic invocation.
