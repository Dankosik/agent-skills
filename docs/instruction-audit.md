# Agent Skills instruction audit

Audited base: [f78fca42acfb51c20a8a218e05d2650ed7f6af67](https://github.com/Dankosik/agent-skills/tree/f78fca42acfb51c20a8a218e05d2650ed7f6af67).
Scope: README, all ten SKILL.md entry points and their existing domain references,
plus evaluation layout. This is a static instruction audit, not observed agent
behavior. Existing per-skill evaluation files are retained without edits; their
judgment expectations have not been revalidated through model trials.

## Basis and repository-specific choice

[OpenAI's September 11 article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
recommends distinct descriptions, selective context, less prescribed itinerary and
explicit authorized completion. Its model-specific observations do not justify
weakening production boundaries or assuming every host has the same tools.

Unlike the smaller language packs, this repository has ten cross-cutting domain
skills, long entry documents, substantial references and existing per-skill evals.
There is no package version/manifest, generated adapter tree or release workflow
at the audited base. Keep names and installation paths; do not add a framework,
shared mandatory policy, runtime, dependencies or an invented release version.

## Findings and changes

### Decision-specific discovery

Descriptions mix activation with long capability lists and adjacent-skill routing.
Shorten all ten around the unresolved decision. Keep neighboring domain names in
the body as optional expertise, not mandatory invocations or prerequisites. A job
can involve a broker without triggering a new messaging review by default.

### Task completion versus guarantee proof

Several roots already state that narrow work remains narrow, but later criteria
still say every lifecycle row must be complete, every mechanism rung rejected or
a stress run passed. These repeated gates can compete with the requested result.
Rewrite them around the affected invariant and actual mode. A full readiness or
migration request retains every material in-scope obligation; a focused fix does
not reopen accepted architecture or require unrelated infrastructure.

Implementation carries through applicable existing checks and repairs introduced
failures. Reuse evidence valid for the same revision/environment, without treating
stale metrics as fresh operational readback. Lack of a live environment limits
production claims; it does not invalidate a completed analysis or local patch.
Explicit runnable tests still need source, setup and assertions. A required check
that could not run remains a named gap, never a fabricated pass.

### Selective technical depth

Retain existing mechanism-specific references and their paths. Keep the cache's
common authority/key/freshness contract and durable-job heading anchors used by
its engine references. Split new credential/revocation, concurrency-mechanism and
incident-operation detail into local references. Each receiving skill remains
usable independently, without an obligatory common file or neighboring skill.
Reference test menus apply to the selected claim, not every scenario in a document.

### Incident diagnosis is not permission to fix

The original post-hoc branch requests a verified fix, and evidence capture before
state-changing mitigation uses an unsupported fixed-duration heuristic. Separate
read-only diagnosis, planning, local implementation and exactly authorized incident
action. Preserve causal uncertainty and mitigation debt. Bounded lightweight
capture is useful when safe, but must not automatically delay urgent authorized
mitigation. No asynchronous continuation or fabricated recovery is promised.

### Credential-specific constraints

The auth root's blanket ban on recoverable credentials conflicts with provider
credentials that must later be presented, already described in the external-API
reference. Distinguish password/verifier storage from protected retrievable secrets.
Keep encryption, least access and no credential exposure. The new auth reference
also follows [RFC 9700 section 4.14](https://www.rfc-editor.org/rfc/rfc9700.html#section-4.14):
public-client refresh protection can use sender-constraining or rotation. Preserve
explicit rotation requirements rather than switching designs silently. See also
[OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
These are narrow corrections to overgeneralized instructions, not a security audit
of an application or a claim that any live authentication system was tested.

### Host capabilities and evidence format

PostgreSQL tool-routing previously required Programmatic Tool Calling without
checking availability. Make it optional and provide native direct/parallel reads
or permitted processing of already supplied data. Keep bounded collection, reset
boundaries and provenance; missing sources are not successful zero-valued results.
Do not install a runtime or broaden access for this optimization.

The messaging proof receipt prescribed a private ledger and drafting sequence,
even for a request for one runnable test. Keep its path as an optional coverage aid
for interacting obligations, replacing the internal procedure with useful evidence
fields. Explicit user-requested ledgers and complete readiness proof remain intact.

## Per-skill disposition

| Entry | Main correction | Domain contract retained |
| --- | --- | --- |
| auth-access-control | Scoped review/build/operate; credential reference | Verified principal, deny at effect, tenant scope, revocation and propagation |
| cache-engineering | Compact core; accepted decisions and conditional proof | Semantic key equivalence/separation, age, fencing, invalidation and origin protection |
| concurrency-control | Comparison menu, no default stress gate | Breaking schedule, actual arbiter/isolation, conflict recovery and stale-holder protection |
| distributed-system-design | Relevant forces/references instead of fixed itinerary | Exact targets, units, ownership, failure capacity, irreversible boundary and recovery |
| durable-background-jobs | Mode-specific completion and selected engine proof | Durable acceptance, distinct identities, lease/effect/ACK, terminal states and occurrence semantics |
| external-api-integration | Select evidence stack, distinguish analysis from readiness | Immutable intent, bounded attempts, ambiguity, authenticated callback and reconciliation |
| postgres-performance | Evidence reuse and capability-aware collection | Reset epochs, bind skew, safe EXPLAIN, real capacity workload and comparable deltas |
| postgres-schema-design | In-scope invariants and migration fidelity | Row grain, business uniqueness, relational constraints, compatibility and actual enforcement |
| production-diagnosis | Diagnosis can finish without a fix; optional operations | Cohort/onset evidence, competing causes, mitigation versus recovery and exact authority |
| reliable-messaging | Optional receipt; no compulsory sibling chain | Durable intent/effect/ACK, stable replay identity, quarantine/redrive and recovery |

## Validation and limits

Add a small Python-standard-library resource suite and one read-only CI job. Check
ten skill names, portable entry metadata, internal paths/anchors, unchanged-suite
presence and new evaluator separation. This repository has no application build
or package generator to execute. No PostgreSQL/broker test stand or release
pipeline is added.

Add [20 contrast scenarios](../evals/instruction-boundaries/README.md) with neutral
inputs and separate expectations. They are NOT RUN; implementation/operation
trials require concrete isolated fixtures and tool results before execution.
Existing domain evals remain at their original paths and are not loaded as runtime
instructions. Moving them would be a separate compatibility/distribution decision.

Record actual resource-test and CI results in the PR. Neither those tests nor a
smaller entry file establishes model quality, latency, production readiness or a
measured optimization. Do not reattribute earlier repositories' results here.
