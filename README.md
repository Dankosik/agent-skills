# Agent Skills

Evidence-driven skills for AI coding agents. Each skill turns a broad engineering task into a predictable process with explicit authority boundaries and fresh proof.

## Install

List the skills available in this repository:

```bash
npx skills add Dankosik/agent-skills --list
```

Install a specific skill, for example:

```bash
npx skills add Dankosik/agent-skills --skill postgres-performance
```

The CLI supports Codex, Claude Code, Cursor, and other agents that consume `SKILL.md` skills.

## Skills

| Skill | Purpose |
| --- | --- |
| [`auth-access-control`](skills/auth-access-control) | Design and prove authentication, session/token lifecycle, permission models, tenant isolation, and identity propagation across services. |
| [`cache-engineering`](skills/cache-engineering) | Design freshness-first caches and prove their correctness, resilience, and measured value. |
| [`concurrency-control`](skills/concurrency-control) | Close lost updates, check-then-act races, and duplicate effects on shared durable state with the weakest sufficient mechanism, fencing, and forced-interleaving proof. |
| [`distributed-system-design`](skills/distributed-system-design) | Compose component boundaries, state contracts, capacity, failure behavior, and evolution into a forces-driven system design. |
| [`durable-background-jobs`](skills/durable-background-jobs) | Design and diagnose durable workers, retries, leases, schedules, backfills, cancellation, and crash recovery. |
| [`external-api-integration`](skills/external-api-integration) | Build and review resilient external API and webhook boundaries from request identity through reconciliation. |
| [`postgres-performance`](skills/postgres-performance) | Diagnose PostgreSQL bottlenecks, reduce database load, and improve latency, throughput, and capacity through a tight evidence loop. |
| [`postgres-schema-design`](skills/postgres-schema-design) | Turn business rules into normalized PostgreSQL tables, relationships, keys, constraints, and safe migrations through invariant-first design. |
| [`production-diagnosis`](skills/production-diagnosis) | Localize production incidents and regressions across services with an evidence loop, falsify the cause, and prove recovery. |
| [`reliable-messaging`](skills/reliable-messaging) | Design and prove broker-backed delivery, ordering, retries, redrive, replay, and business effects. |

## Principles

- Predictable process over predetermined answers.
- Evidence before intervention.
- Explicit boundaries for production actions.
- Progressive disclosure for domain reference material.
- Comparable before/after proof for every optimization claim.
- Decision criteria over rigid rules; each direction stated once, constraints reserved for high-stakes paths.

The collection is informed by OpenAI's [latest-model prompting guidance](https://developers.openai.com/api/docs/guides/latest-model), Matt Pocock's [Building Great Skills glossary](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/GLOSSARY.md), and Anthropic's [context-engineering guidance for Claude 5-generation models](https://x.com/trq212/article/2080710971228918066).

## Structure

Each skill is self-contained:

```text
skills/<skill-name>/
├── SKILL.md
├── references/
└── evals/
```

## License

[MIT](LICENSE)
