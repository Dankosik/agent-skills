# Agent Skills

Evidence-driven skills for AI coding agents. Each skill turns a broad engineering task into a predictable process with explicit authority boundaries and fresh proof.

## Install

List the skills available in this repository:

```bash
npx skills add Dankosik/agent-skills --list
```

Install a specific skill:

```bash
npx skills add Dankosik/agent-skills --skill postgres-performance
```

The CLI supports Codex, Claude Code, Cursor, and other agents that consume `SKILL.md` skills.

## Skills

| Skill | Purpose |
| --- | --- |
| [`postgres-performance`](skills/postgres-performance) | Diagnose PostgreSQL bottlenecks, reduce database load, and improve latency, throughput, and capacity through a tight evidence loop. |

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
