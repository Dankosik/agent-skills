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
| [`cache-engineering`](skills/cache-engineering) | Design freshness-first caches and prove their correctness, resilience, and measured value. |
| [`distributed-system-design`](skills/distributed-system-design) | Compose component boundaries, state contracts, capacity, failure behavior, and evolution into a forces-driven system design. |
| [`durable-background-jobs`](skills/durable-background-jobs) | Design and diagnose durable workers, retries, leases, schedules, backfills, cancellation, and crash recovery. |
| [`external-api-integration`](skills/external-api-integration) | Build and review resilient external API and webhook boundaries from request identity through reconciliation. |
| [`postgres-performance`](skills/postgres-performance) | Diagnose PostgreSQL bottlenecks, reduce database load, and improve latency, throughput, and capacity through a tight evidence loop. |
| [`postgres-schema-design`](skills/postgres-schema-design) | Turn business rules into normalized PostgreSQL tables, relationships, keys, constraints, and safe migrations through invariant-first design. |
| [`reliable-messaging`](skills/reliable-messaging) | Design and prove broker-backed delivery, ordering, retries, redrive, replay, and business effects. |

## Principles

- Predictable process over predetermined answers.
- Evidence before intervention.
- Explicit boundaries for production actions.
- Progressive disclosure for domain reference material.
- Comparable before/after proof for every optimization claim.

The collection is informed by OpenAI's [latest-model prompting guidance](https://developers.openai.com/api/docs/guides/latest-model) and Matt Pocock's [Building Great Skills glossary](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/GLOSSARY.md).

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
