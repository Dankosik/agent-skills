---
name: postgres-schema-design
description: "Use to design or review PostgreSQL relations, identities, constraints, or migrations from business invariants, rather than tune query performance."
---

# Invariant-First PostgreSQL Schema Design

**Invariant.** A schema models business facts and their enforcement. Follow
language, dependencies, relations, constraints and scenarios only as far as the
requested decision needs. Start normalized; deliberate duplicated facts require
an authority, synchronization, repair and justified benefit, not a blanket ban.

## Request and authority

Establish the requested schema boundary, artifact, work mode and relevant target
version from the request and existing evidence. Design/review/planning preserves
repository and database state. Build/change permits canonical migration/model/test
edits and appropriate non-destructive local validation, with repair of introduced
failures. Production DDL, backfill, data repair, constraint validation and migration
execution require separate exact action/target/bounds authorization and fresh
readback. Credentials, an available database or a generated migration grant none.

Ask when unresolved business meanings change identity, ownership, cardinality,
retention, money or time semantics. Otherwise use explicit assumptions and continue
independent work. Preserve settled choices outside the requested change. A column
constraint fix does not require redesigning every table or reopening an accepted
normalization decision; a full schema review covers all included invariants.

## Model the affected facts

Extract operations/states, identity and duplicate rules, cardinality/optionality,
ownership/lifecycle/deletion, current versus historical facts, tenant/privacy and
concurrent/retry behavior. Treat code and existing schemas as evidence; disclose
conflicts with an explicit product rule instead of silently changing that rule.

For each in-scope independently stored concept, name what one row means, candidate
keys, owner and lifecycle, mutable/immutable facts, and effective versus recorded
time when meaningful. A surrogate key does not replace business uniqueness.
Identify both directions of each material relationship, foreign-key/delete behavior
and any association's own attributes or identity.

Write the functional dependencies affecting decomposition. Prefer one authoritative
location for a mutable fact. Read the applicable [relational design branch](references/relational-design.md)
for normalization, composite keys, temporal/subtype models, tenancy, soft deletion,
JSON/EAV or denormalization. Explain actual update/insert/delete anomalies and
lossless decomposition rather than performing a normal-form recital for every edit.
Dependencies not enforced locally still need an explicit owner.

A duplicated or derived fact needs source, freshness/update, failure/repair and
workload justification. An accepted denormalization is context for a narrow fix,
not a new requirement to run a performance experiment. Unmeasured benefit stays
an assumption; do not call the model faster from its shape alone.

## Map to PostgreSQL and migration

Read the relevant [DDL reference](references/postgresql-ddl.md) when emitting SQL,
choosing concrete types/constraints or planning migration. Verify material syntax
and operational behavior for the selected PostgreSQL version, not an assumed
latest server.

Use NOT NULL, primary/unique/foreign keys, CHECK and exclusion constraints for
rules they can express. Match null, tenant, historical, numeric and time semantics
to the business invariant. Put other rules in one named concurrency-safe owner
with a falsifier; a preflight check alone cannot arbitrate competing writes.

For existing data, distinguish logical end state from rollout: inspect the
violations relevant to the new rule; preserve needed old/new compatibility;
choose supported lock/transaction behavior; bound resumable backfills; verify
before cutover; retain rollback or roll-forward and temporary-state ownership.
A new empty table does not need an invented production backfill campaign. Use the
project's existing migration framework and required checks.

## Challenge and finish

For each material changed invariant, choose representative valid and rejected or
conflicting scenarios: duplicate, orphan, competing write, cross-tenant reference,
null uniqueness, temporal boundary, historical mutation or dirty-data migration
when applicable. Use the actual engine when its constraint/isolation semantics
are claimed. A model mock or successful SQL parse does not establish enforcement.

Design-only work supplies proposed examples at the requested fidelity. Explicit
runnable proof needs SQL/test source, setup and assertions; unrun cases stay marked.
Local changes use existing focused schema/migration checks, repair introduced
failures and reuse valid same-revision/environment results. Missing infrastructure
is an explicit limit, not permission to fabricate success or build a new platform.

Report verdict, row grains/relationships, invariant-to-owner mapping, relevant
DDL/migration decisions, assumptions and gaps. Use a diagram when it clarifies
the relationships or is requested, not solely because a table count is reached.
A completed proposal is not a migrated or verified-live system. Finish when the
requested artifact and applicable checks are delivered or the precise blocker is
stated; no unrelated schema or performance gates are implied.

Use `postgres-performance` for a distinct unresolved load/query/index question.
The adjacent skill is not required to complete a relational decision here.
