# Instruction-boundary evaluation

**Status: NOT RUN.** These are 20 authored scenario inputs with separate grading
criteria, not observed model results, runnable service fixtures or live-API tests.
The original ten per-skill suites remain unchanged.

Pass only the selected prompt from [prompts.json](prompts.json) to the subject
model, with the chosen instruction variant and declared tools. Keep case IDs,
[rubric.json](rubric.json), contrast grouping and grader notes out of that context.
Grade requested scope, useful technical content, correct authority and honest
evidence before token count, output length or latency.

Compare no pack, the baseline pack at
`f78fca42acfb51c20a8a218e05d2650ed7f6af67`, and an exact candidate commit. Keep model,
host, permissions, input, tool availability and budgets the same within a trial.
Record skill/resource selection and tool traces, not just the final answer.
Repeat comparisons with predetermined sampling and retain failures as well as wins.
Narrow/full cases are contrasts, not byte-identical A/B samples; each case gets
its own controlled baseline/candidate comparison.

Most prompts are self-contained analysis/design tasks. For implementation or live
operational trials, first materialize a disposable, pinned fixture, exact commands,
mocked/authorized tool results, expected state and cleanup. In particular B20 needs
an actual code/test fixture before claiming executed follow-through; B16 is a
controlled authority scenario, not permission to operate a real service. Never
use real credentials, production faults or private data to fill absent fixtures.

Structural checks validate IDs, JSON and links only. They do not score model
judgment or prove production security, latency, recovery or all host behavior.
Do not rewrite original evaluation expectations merely to favor the new wording.

## Record each actual run separately

| Field | Record |
| --- | --- |
| Status | NOT RUN until an actual trial completes |
| Case / variant | Input identity and exact instruction commit |
| Environment | Model/effort, host, permissions, tools, fixture revision |
| Result | Requested outcome, technical omissions, scope/authority violations |
| Evidence | Raw output and permitted trace location, check commands/results |
| Limits | Missing mechanisms, confounders, unavailable source or metrics |

The candidate does not claim a measured quality gain or speedup. A shorter skill
is a smaller file; a successful resource check is not a successful model review.
