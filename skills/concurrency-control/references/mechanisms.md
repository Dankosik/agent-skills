# Mechanisms for a breaking schedule

Compare only plausible mechanisms for the selected invariant. This reference
inherits the task and production-action limits in [SKILL.md](../SKILL.md).

| Mechanism | When it can suffice | Obligation that remains |
| --- | --- | --- |
| Atomic conditional statement | One authority can express the full update predicate | Check the affected count/result; preserve the domain's conflict response |
| Unique or exclusion constraint | The contested business identity or overlap is declarative | Handle conflict, including concurrent submissions and idempotent retry |
| Optimistic version / ETag | Fresh state and compare-and-set protect the decision | Recompute on conflict; bound retries and preserve operation identity |
| Pessimistic row lock | Contended rows or a short critical section need serialization | Consistent acquisition order, real transaction scope, no remote/user wait inside |
| Serializable transaction | The invariant spans a predicate or several rows | Retry the whole transaction on serialization failure without duplicating effects |
| Advisory/application lock | The resource lacks an appropriate row arbiter | Every writer follows the protocol and ownership/release semantics are explicit |
| Distributed lease | No shared transactional arbiter can cover the resource | Overlap is possible; fence at the effect or use a sufficient idempotency/reconciliation contract |

A conditional stock decrement can close a lost-update window without a preceding
read. A uniqueness constraint can arbitrate a duplicate booking. Neither example
proves an arbitrary cross-row predicate safe; test the actual invariant at the
actual isolation level. Snapshot isolation and read committed admit different
schedules. Store product and version determine details.

A lease has an owner token, lifetime and renewal contract. Compare the owner when
releasing so an expired holder cannot release its successor. An owner token used
for release is not automatically a monotonic fencing token checked by the effect
owner. If that owner cannot fence, the lease may only suppress contention; explain
where correctness comes from instead of promising unconditional mutual exclusion.

Leadership or singleton scheduling must protect against overlapping old/new
actors. An occurrence identity differs from attempt identity; a unique occurrence
claim or business-effect key can preserve one effect even when two actors run.
Lease expiry does not undo a prior write, and idempotency does not validate a
stale but different write. Keep these claims separate.

For the selected mechanism, describe reachable failure windows: process or
connection loss, unknown commit, expired ownership, deadlock, arbiter outage and
hot-key conflict amplification. Attach a bounded disposition and observable signal
to each relevant window. Explain why a simpler realistic alternative fails when
that comparison changes the choice; no full ladder transcript is required.
