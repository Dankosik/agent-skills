# Proof receipt for interacting obligations

This is an optional coverage aid for a complex design, readiness assessment or
explicit ledger request. It is not a mandatory private reasoning procedure or
an extra review pass. A single-boundary diagnosis or one requested executable
test can report its claim and evidence directly without constructing this table.

## Useful evidence fields

Keep only independently meaningful obligations from the requested artifact and
its safety-relevant guarantees:

| Obligation | Claim or decision | Durable evidence or provider fact | Ambiguity and recovery | Falsifier or returned artifact | Status |
| --- | --- | --- | --- | --- | --- |

Distinguish documented provider behavior, observed evidence, local invariants,
inference and unknowns. Covered, gap and out-of-scope describe actual status;
unknown behavior is not a guarantee. An explicitly requested table or artifact
count remains binding, but the template does not impose one on every answer.

For runnable code, name the returned API and test that invokes it. Helpers must
be supplied or already exist; label fragments as pseudocode and unrun tests as
unrun. Readiness needs the mechanism whose removal would make the falsifier fail.
Useful coverage includes lost commit responses, replay identity, ordering versus
poison progress, and the specifically requested redrive rather than ordinary
redelivery. Assert durable state and relevant delivery progress.

Keep any proposed or executed operation within authorized environment, identities,
destination, rate and stop conditions. A missing permission or unrun proof limits
the operational claim; it does not make an otherwise delivered analysis incomplete.

Present supported conclusions, exact gaps and requested artifacts. Omit redundant
topology, locks, worker mechanics and rollout detail that no selected guarantee
needs. Do not output a reasoning transcript or repeat the ledger in every section;
its purpose is traceable evidence, not more scope or a required internal format.
