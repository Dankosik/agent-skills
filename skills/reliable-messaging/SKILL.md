---
name: reliable-messaging
description: "Use for broker publish/consume guarantees, message identity, acknowledgement, ordering, redelivery, replay, or recovery of durable business effects."
---

# Reliable Messaging

**Delivery.** Follow the affected business state, message identity, publish,
broker acceptance, consume, durable effect and acknowledgement through recovery.
State every guarantee with its start, commit, end and accepted loss/duplicate
window. Broker deduplication is not an end-to-end exactly-once business effect.

## Choose depth and authority

Review/diagnosis reconstructs the affected boundary read-only and reports the
supported cause, minimal correction and falsifier. Design defines the in-scope
contracts at the requested fidelity. Build/fix changes the local owner and runs
applicable checks, repairing introduced failures. Production publication, broker
configuration, replay/redrive, purge/deletion, credentials and load/fault tests
require exact environment/action/range/bounds authorization, preflight and fresh
readback. A proposed recovery plan is not permission to execute it.

Preserve accepted decisions outside the requested change and explicit artifact or
test limits. A narrow acknowledgement fix does not trigger a full redesign. Full
readiness, migration or replay claims do require the complete relevant lifecycle.
Additional safety-critical dependencies must be named; unrelated concerns do not
become completion gates. Ask only for a material missing decision or authority.

## Load the selected broker contract

Read the reference for the actual broker and relevant concern, verifying material
version-specific behavior against current primary documentation:

- [Kafka](references/kafka.md): acceptance, offsets, transactions, partition order,
  retention and replay.
- [RabbitMQ](references/rabbitmq.md): routing/confirms, acknowledgements, prefetch,
  quorum/poison handling and recovery.
- [SQS](references/sqs.md): Standard/FIFO, identity, visibility/deletion and redrive.
- [JetStream](references/jetstream.md): publish ACK, consumer progress, retention,
  redelivery and replay.
- [Operations](references/operations.md): selected ordering, backpressure,
  quarantine, recovery, migration, security or capacity questions.

An unfamiliar broker needs its own documented contract, not a guess from one of
these examples. Reference checks are conditional on the claimed guarantee; they
do not authorize live operations or require reading all broker documents.

## Frame identity and durable intent

Name the protected effect, relevant loss/duplicate tolerance, latency, ordering,
fan-out and recovery horizon. When the architecture decision is open, compare
synchronous calls or a single-store job with the broker's needed buffering,
isolation, fan-out or replay. Do not repeat that comparison for a settled broker's
narrow bug fix.

Classify event, command or competing-worker item. Use one ledger row per interacting
publish/consume boundary, or just the affected row for a narrow task:

| Boundary | Guarantee/start/end | Identity/scope | Durable commit | Ambiguity | Recovery owner | Signal | Falsifier |
| --- | --- | --- | --- | --- | --- | --- | --- |

A logical message ID survives publish retry, redelivery, redrive and replay; offsets,
delivery tags, receipt handles and attempt IDs are not substitutes. Retain envelope
fields that affect behavior: type/version, tenant, ordering/causation, immutable
intent and safe trace references. Scope idempotency by stable logical effect and
tenant, not mutable deployment or consumer instance. A correlation ID is not a
deduplication key. A new dedup scheme must account for already-applied effects
before replay, or it can reapply the very effect it should preserve.

## Publish and commit the effect

When business state and publish intent share a database, commit state and outbox
together. Publish with the selected durable-acceptance contract, then mark relay
completion; lost responses remain ambiguous under the same identity. If no atomic
intent boundary exists, name the loss/duplicate window and reconciliation owner.
Bound publisher queues and in-flight work. Broker transactions do not join an
unrelated business database transaction.

For a transactional consumer, commit business effect and uniquely enforced
inbox/effect identity together. For an external effect, propagate the stable
idempotency key or durable downstream intent. Acknowledge/delete/commit recovery
progress only after the relevant durable effect. Concurrent completions cannot
acknowledge past unfinished work in an ordered lane. A preflight dedup read alone
leaves a race.

Effect-before-ACK crashes and lost ACK responses must converge on durable state
without multiplying effects. Retain dedup information across the longest
redelivery, redrive, retention and offline-replay horizon; never-repeatable effects
may require a permanent business key. Keep schema compatibility and retirement
conditions for the producers/consumers that can coexist.

## Prove the requested boundary

Use [proof receipt](references/proof-receipt.md) as an optional coverage aid when
several artifacts or guarantees interact. It is not a required hidden ledger,
reasoning procedure or extra self-review pass; one focused test need not load it.
Preserve explicit requested evidence rather than prescribing how to think.

Choose failures around the affected durable boundary: intent/acceptance loss,
effect-before-ACK, ACK loss, competing attempt, ownership expiry, poison/retry,
replay or mixed-version behavior where those paths matter. A full readiness claim
must cover both sides of each relevant commit. A new quarantine guarantee includes
bounded redrive preserving original identity and business state, not just a DLQ.

Pin engine/client, topology, durability settings and relevant workload. Assert
business state plus actual broker progress/identity for broker claims; a once-called
mock handler is insufficient. Use existing local harnesses and a test that would
distinguish the absent commit/idempotency mechanism. Explicit runnable requests
need source, setup and assertions; design/audit evidence may be proposed or unrun.
Unavailable infrastructure is a disclosed limit, not an inferred guarantee.

## Report and complete

Lead with verdict, affected guarantee, cause/design, recovery, observed proof and
authority/gaps. Keep all requested artifacts and distinguish proposed, locally
implemented, tested, deployed and verified-live states. A local fix can be complete
without claiming production readiness. Reuse valid same-revision/environment
results, repair introduced failures and stop when the requested result and
applicable checks are satisfied or a concrete blocker is reported. Do not invent
new clusters, full load campaigns or unrelated cleanup to finish a narrow task.

Adjacent job execution, schema, external API and cache decisions may use their
matching skills when genuinely unresolved. Names are navigation, not dependencies
or automatic handoffs; preserve this skill's identity and delivery ownership.
