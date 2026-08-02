---
name: reliable-messaging
description: "Delivery discipline for application-to-broker-to-application boundaries. Use when designing or changing publish/consume behavior, diagnosing loss, duplicates, ordering, retries, redrive, or replay, or proving a broker-backed business effect across Kafka, RabbitMQ, Amazon SQS, NATS JetStream, or an equivalent broker. Broker operations belong here when they change that delivery boundary."
---

# Reliable Messaging

Delivery is an application lifecycle, not a broker feature:

`business state -> message identity -> durable publish -> broker acceptance -> consume -> durable effect -> acknowledge -> retry/redrive/replay -> reconcile -> prove`

Keep every guarantee bounded. State where it starts, the durable commit that establishes it, where it ends, and which business effect remains idempotent. Use “effectively once” only for a named business effect protected by a durable idempotency mechanism. Reserve “exactly once” for a proven atomic boundary; broker deduplication alone is not an end-to-end guarantee.

## Authority contract

- Review, diagnose, and design preserve repository, broker, application, and production state. Use available artifacts and bounded read-only inspection.
- Build and fix permit local in-scope edits plus safe, non-destructive checks.
- Production publishing, broker configuration changes, redrive, replay, purge, topic or queue deletion, and credential rotation are separate actions requiring explicit authorization for the exact environment and bounds.

When a material choice affects business identity, money, tenant isolation, loss tolerance, or recovery, obtain the missing rule or proceed with a clearly labelled assumption only when it is safe to revise. Keep proposed, implemented locally, deployed, and verified live states distinct.

## Broker context pointers

Each context pointer names the point where its broker-specific delivery rules become required:

- Read [references/kafka.md](references/kafka.md) after Kafka is selected or observed and before deciding producer acceptance, offsets or groups, partition ordering, retention, replay, or Kafka/client configuration.
- Read [references/rabbitmq.md](references/rabbitmq.md) after RabbitMQ is selected or observed and before deciding routing or publisher acceptance, acknowledgement or requeue behavior, prefetch, recovery topology, or RabbitMQ/client configuration.
- Read [references/sqs.md](references/sqs.md) after Amazon SQS Standard or FIFO is selected or observed and before deciding send acceptance, visibility or deletion, group ordering or deduplication, retention, redrive, or queue/client configuration.
- Read [references/jetstream.md](references/jetstream.md) after NATS JetStream is selected or observed and before deciding publish acceptance, consumer acknowledgement or redelivery, retention, replay, or stream/consumer/client configuration.

For an unfamiliar broker or version, derive the same lifecycle from its current primary documentation and label unverified behavior. Common application invariants remain inline below.

## Delivery ledger

Maintain one row for every publish and consume boundary. Populate observed or proposed facts as evidence arrives. Mark unknown cells as explicit delivery gaps and resolve them with evidence before claiming a guarantee.

| Boundary | Guarantee and start/end | Identity/scope | Durable commit point | Ambiguous outcome | Failure owner/recovery | Observable signal | Executable falsifier |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 1. Frame and route the delivery

Choose the branch from the requested work before populating the ledger:

- **Review:** reconstruct observed rows from contracts, code, configuration, telemetry, and tests; distinguish observed facts, inferences, and unknowns; report a verdict and recommended target while preserving state.
- **Diagnose:** reconstruct the affected row, locate the earliest durable boundary where observed behavior violates the guarantee, and identify its failure owner before recommending a change.
- **Design:** create target rows, label assumptions and unresolved business rules, and make every proposed mechanism falsifiable.
- **Build or fix:** reconstruct the current row, close the smallest owner-controlled gap in local scope, and verify the changed boundary.

The authority contract governs what the selected branch may mutate.

Inventory every boundary shallowly, then take one row through Steps 2–8 before deepening the next. This keeps feedback tied to one guarantee and grounds each next decision in a completed delivery slice.

Start with the business operation, protected effect, loss and duplicate tolerance, latency target, outage duration, fan-out, replay need, ordering scope, and throughput. Decide whether a broker earns its operational cost:

- use a synchronous call when the caller needs an immediate answer and both sides share availability;
- use a database-backed job table when one database already owns the work and independent fan-out or long replay is unnecessary;
- use a broker when durable buffering, failure isolation, independent consumers, fan-out, workload smoothing, or replay is a required property.

Classify each message:

- An **event** records an immutable fact; each interested consumer owns independent progress.
- A **command** requests one named capability; one logical handler owns the outcome and reports failure explicitly.
- A **work item** is claimed by one worker from a competing pool; retry transfers the same logical work, not a new operation.

Write each guarantee as:

`<semantic> from <start> after <durable evidence> through <end>; <named effect> is idempotent by <key and scope>`

Distinguish at-most-once, at-least-once transport, and effectively-once business effect. Include the accepted loss or duplicate window rather than selecting a label alone.

Choose at least one executable falsifier for the claimed boundary now; Step 8 runs it. A falsifier chosen while framing the guarantee tests the claim instead of merely confirming a preferred mechanism.

**Completion criterion:** the branch and authority mode are explicit; every publish/consume boundary has a ledger row; the current row states broker necessity, message semantic, guarantee start/end, protected effect, loss/duplicate tolerance, ordering scope, outage window, and a red-capable falsifier; unknown cells are labelled gaps.

## 2. Define identity and schema

Give one logical message a producer-assigned identity that survives publish retries, redelivery, redrive, and replay. Keep it separate from broker delivery tags, offsets, sequence numbers, receipt handles, and broker-generated IDs.

Define an envelope with only fields that change behavior:

- message ID and message type;
- schema version and occurred-at time;
- correlation ID for one business interaction and causation ID for the direct predecessor;
- tenant or security scope;
- ordering or partition key when order is required;
- trace context and payload reference or integrity metadata when useful.

Set the idempotency scope as `(tenant, consumer/effect, message_id)` or a stronger immutable business key. A correlation ID groups work; it is not a deduplication key. A causation ID builds lineage; it is not a retry ID.

Name the schema owner and compatibility rule. Prefer additive evolution: deploy tolerant consumers before producers emit a new version, preserve unknown fields where the format requires it, and define the retirement condition for old readers and writers. Put sensitive or large data behind an authorized reference when practical; protect metadata because tenant and correlation fields can also be sensitive.

**Completion criterion:** the current delivery row has stable logical identity, tenant/idempotency scope, correlation and causation semantics, schema owner, compatibility rule, ordering key, data classification, and an example that distinguishes a retry from a new business operation.

## 3. Make publication durable

Locate the first durable commit point. When business state and publish intent share a transactional database, write the state change and outbox row in the same transaction. The outbox row carries the final message ID, type, tenant, ordering key, schema version, payload or stable payload reference, and creation time.

Relay the outbox with bounded claims and retries:

1. claim eligible rows without allowing two relays to own one attempt indefinitely;
2. publish using the broker's durable acceptance mechanism;
3. mark published only after acceptance is observed;
4. treat timeout or connection loss before that observation as ambiguous and retry the same logical message ID;
5. reclaim expired claims and retain enough state to diagnose stuck rows.

Broker transactions cannot close a transaction gap with an unrelated business database. When an outbox is unavailable, name the resulting loss or duplicate window and its reconciliation owner. For database change capture, identify which committed row is the source of truth and how connector offsets are recovered.

Bound publisher queues and in-flight requests. Backpressure reaches the business ingress or durable outbox instead of turning memory into an unbounded second queue.

**Completion criterion:** the current delivery row names business commit, publish-intent commit, broker acceptance evidence, ambiguous outcome, relay ownership, retry identity, backlog bound, and reconciliation path, backed by executable or concrete local artifacts.

## 4. Commit the business effect before acknowledgement

Assume at-least-once delivery whenever a lost acknowledgement, expired visibility window, consumer crash, or rebalance can cause another attempt.

For a transactional effect, atomically commit the effect and an inbox/deduplication record protected by a unique key at the declared scope. Concurrent duplicates then converge on one committed outcome. Store a status or result only when callers need to distinguish in-progress, completed, and failed attempts; use fencing or conditional state transitions where a stale worker could overwrite newer work.

Choose deduplication retention from the maximum of broker retention, redelivery, redrive, offline recovery, and replay horizons plus clock and operational margin. Keep a permanent business key when repeating the effect is never valid. Broker deduplication windows are only an optimization inside their documented boundary.

For an external effect, pass the same idempotency key to the downstream system or durably enqueue that effect in a local outbox. A check-then-act query without a unique constraint or atomic downstream operation leaves a concurrent duplicate gap.

Acknowledge, commit an offset, or delete the message only after the durable effect commits. Treat an acknowledgement timeout as ambiguous; reread durable effect state and accept redelivery safely. Record permanent failure durably before settling or quarantining the message.

**Completion criterion:** the current delivery row names the durable effect point, atomic dedup mechanism, concurrent-duplicate behavior, TTL rationale, acknowledgement point, lost-ack behavior, and external-side-effect owner, covered by an executable duplicate test.

## 5. Bound ordering, concurrency, and backpressure

Order only the business scope that needs it. Map that scope to a partition key, message group, subject partition, or single-consumer lane and state what can reorder across scopes. Make state application conditional on expected version or current state so a late delivery becomes a safe no-op, conflict, or reconciliation signal.

Size consumer concurrency from downstream capacity. Bound fetched-but-uncommitted work with batch size, prefetch, max pending acknowledgements, or in-flight messages. Align processing deadlines with acknowledgement, poll, or visibility deadlines and extend them only while the current worker still owns useful progress.

Handle ownership changes explicitly: stop accepting new work, stop or pause fetches, finish or abandon bounded in-flight work, commit only completed effects, and release the consumer cleanly. During deploys, drain old consumers before removing schema compatibility. Preserve a rollback reader and writer path until new-version lag and quarantine remain within the declared window.

**Completion criterion:** the current delivery row makes ordering scope, concurrency limit, downstream capacity assumption, in-flight bound, deadline/heartbeat behavior, ownership-transfer behavior, drain sequence, schema rollout, and rollback condition measurable.

## 6. Design retry and recovery

Classify failures before choosing a retry:

| Failure class | Delivery behavior | Recovery owner |
| --- | --- | --- |
| Transient dependency or transport failure | bounded exponential backoff with jitter and a total attempt/time budget | consumer or publisher |
| Rate or capacity pressure | delayed retry plus reduced intake/concurrency | service owner |
| Invalid schema, authorization, or payload | durable quarantine with safe diagnostic context | producer/schema/security owner |
| Business conflict or missing prerequisite | conditional retry only when a named signal can change; otherwise reconcile | domain owner |
| Unknown failure | small bounded retry budget, then quarantine and investigate | owning team |

A poison record preserves original identity, tenant, schema version, first and last failure, attempt count, source location, and a redacted payload or authorized pointer. Keep quarantine distinct from a normal retry queue.

Treat redrive and replay as migrations: pin source and destination, select immutable IDs or ranges, record schema/code version, snapshot counts, canary a bounded batch, rate-limit against live capacity, preserve original identity and causation, observe effects, and stop on a predeclared invariant. Prefer a new replay cursor or consumer so live progress remains recoverable.

Reconciliation compares authoritative business state with outbox, broker progress, inbox/effects, and quarantine. It repairs a named mismatch idempotently and records what changed.

**Completion criterion:** the current delivery row gives every failure class a budget, backoff, terminal state, owner, observable signal, and recovery action; redrive/replay has a bounded authorized plan; reconciliation detects and repairs each accepted gap.

## 7. Operate the boundary securely

Expose lifecycle signals, not just broker health:

- outbox backlog count and oldest age, publish acceptance latency, ambiguous outcomes, and terminal publish errors;
- consumer lag or oldest available age, in-flight/unacknowledged count, processing and acknowledgement latency, redeliveries, rebalance or visibility expiry, and stuck ownership;
- dedup conflicts, effect latency and failures, quarantine depth/age, redrive rate, retention headroom, and reconciliation mismatches;
- downstream saturation, worker concurrency, memory, connection pools, and broker capacity relevant to backpressure.

Authenticate workload identities, authorize producers, consumers, and operators separately at the smallest topic, queue, subject, consumer-group, and tenant scope available, encrypt in transit and at rest where the data classification requires it, and rotate credentials through a reversible overlap. Prevent tenant selection in an untrusted payload from granting access; derive or verify it against the authenticated principal. Expose only redacted diagnostic metadata in logs, traces, quarantine dashboards, and ad-hoc replay artifacts; retain secrets and sensitive payloads in authorized stores referenced by stable pointers.

Alerts name an owner and recovery action. Retention must exceed the worst credible detection plus recovery interval; capacity proof includes catch-up after that outage without starving live traffic.

**Completion criterion:** the current delivery row has an owner, least-privilege identity, encryption and payload policy, retention/capacity envelope, alert, dashboard signal, and runbook action that reaches a safe state.

## 8. Falsify the guarantee

Test the failure points between every two durable steps. Automate the smallest representative set that proves the claimed boundary:

- crash after business commit but before publish, and after broker acceptance but before outbox completion;
- duplicate publish, concurrent duplicate consumers, and retry after broker deduplication expires;
- crash before effect commit, during commit, and after commit but before acknowledgement;
- lost publish confirmation, lost consumer acknowledgement, acknowledgement timeout, and stale receipt or delivery ownership;
- reorder across workers, partition or group ownership change, rebalance, slow processing, and backpressure saturation;
- poison input, exhausted retry budget, quarantine, bounded redrive, historical replay, retention expiry, and reconciliation repair;
- mixed-version producer/consumer deploy, drain, rollback, authentication denial, and cross-tenant attempt.

Pin broker and client versions, topology, replication/durability settings, workload, concurrency, and fault injection. Verify business state, message/inbox identity, broker progress, retry counts, quarantine, and signals after recovery. Passing a happy-path publish/consume test proves none of the crash boundaries.

**Completion criterion:** the current delivery row has an executable falsifier that fails when its commit or idempotency mechanism is removed, and fresh evidence covers duplicates, ambiguous outcomes, crash recovery, ownership change, replay, and reconciliation; repeat Steps 2–8 until every inventoried row meets this criterion.

## Delivery report

Lead the final artifact with the verdict and current state: proposed, implemented locally, deployed, or verified live. Include only the sections that carry evidence:

```markdown
## Verdict
## Delivery lifecycle and assumptions
## Guarantee ledger
## Implementation or findings
## Failure and recovery plan
## Security, rollout, and rollback
## Proof and remaining gaps
## Authorization required
```

**Global completion criterion:** for every publish/consume boundary, guarantee, identity, durable commit point, ambiguous-outcome behavior, failure owner, recovery path, observable signal, and executable falsifier are defined.
