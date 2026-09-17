# Agent Skills

Evidence-driven skills for AI coding agents. Each skill supports a specific
engineering decision while preserving the user's task, project choices and
production-action boundaries. They are independent methods, not a mandatory
sequence of design, implementation and operational proof.

## Install

List the available skills:

```bash
npx skills add Dankosik/agent-skills --list
```

Install a specific skill:

```bash
npx skills add Dankosik/agent-skills --skill postgres-performance
```

Use the installer's supported destination for your coding agent. This repository
contains instructions and references, not credentials or an agent runtime.
Review updates before adopting them; record the chosen upstream commit when
reproducibility matters. No release/version manifest is introduced by this update.

## Choose the decision

| Skill | Use it for |
| --- | --- |
| [auth-access-control](skills/auth-access-control) | Authentication, permission enforcement, tenant scope and revocation |
| [cache-engineering](skills/cache-engineering) | Cache value, key, freshness, fill, invalidation and degraded behavior |
| [concurrency-control](skills/concurrency-control) | Interleavings and arbitration on shared durable state, not runtime memory races |
| [distributed-system-design](skills/distributed-system-design) | Composition of component, capacity, state, failure and evolution contracts |
| [durable-background-jobs](skills/durable-background-jobs) | Durable acceptance, attempts, leases, schedules, effects and recovery |
| [external-api-integration](skills/external-api-integration) | External HTTP/webhook identity, attempts, ambiguous outcomes and reconciliation |
| [postgres-performance](skills/postgres-performance) | PostgreSQL bottleneck attribution and evidence-backed workload improvements |
| [postgres-schema-design](skills/postgres-schema-design) | Relational identity, invariants, constraints and migration decisions |
| [production-diagnosis](skills/production-diagnosis) | Unknown incident/regression localization and causal or recovery assessment |
| [reliable-messaging](skills/reliable-messaging) | Broker publish/consume, acknowledgement, ordering and recovery boundaries |

Select by the unresolved decision, not by every technology mentioned in the
repository. A job executed from a broker may need both job and messaging guidance,
but loading one does not require loading the other. Adjacent skill names are
navigation, not automatic delegation or dependencies on separately installed skills.
Use only the references for the selected mechanism and reuse complete applicable
material already available in context.

## Outcomes and evidence

Diagnosis and review can finish with a supported explanation or a precise gap
without changing code. Design delivers the requested contract and validation plan.
Implementation continues through applicable local checks and repair of introduced
failures. An explicitly requested runnable test needs source, setup and assertions.

A narrow fix does not reopen an accepted architecture, create a new infrastructure
platform or require every test listed in a reference. A full readiness, migration
or recovery claim still needs every relevant in-scope guarantee covered. A missing
live environment limits the claim; it does not turn mocks into production evidence
or block unrelated local work.

Production actions retain exact authorization, preflight and fresh readback.
Read-only probes also need appropriate cost and data bounds. Keep observations,
inference, proposals, local checks and verified-live results distinct. Comparable
measurements are required for an optimization claim, not invented for every fix.

## Structure and maintenance

```text
skills/<skill-name>/
├── SKILL.md                 # decision, scope, invariants and completion
├── references/              # optional mechanism-specific detail, where needed
└── evals/evals.json          # existing evaluator material, not agent instructions

evals/instruction-boundaries/ # new neutral prompts and separate grading criteria
docs/instruction-audit.md     # audit rationale and limitations
tests/test_skill_resources.py # structural checks only
```

Do not load evaluation expectations as runtime guidance. The existing per-skill
evaluation paths remain unchanged for compatibility; their placement does not
make them required reading. New evaluation materials remain outside skills.

Run the standard-library-only resource checks from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

These check inventory, metadata, local links/anchors and evaluator integrity;
they do not run PostgreSQL, brokers, production probes or model comparisons.
The matching CI job performs the same checks without a packaging/release pipeline.
See [the audit](docs/instruction-audit.md) and
[evaluation protocol](evals/instruction-boundaries/README.md).

The instruction update is informed by OpenAI's
[skills and prompts article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
Its model-specific observations do not establish identical behavior in every host.
The earlier collection also drew on the
[latest-model guide](https://developers.openai.com/api/docs/guides/latest-model),
[Matt Pocock's skill glossary](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/GLOSSARY.md)
and the [context-engineering article supplied by the author](https://x.com/trq212/article/2080710971228918066).
Those historical links are attribution, not a claim of fresh verification here.

[MIT license](LICENSE).
