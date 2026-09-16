---
name: production-diagnosis
description: "Use to localize an unknown production incident or regression, assess a causal diagnosis, or verify recovery from an authorized change."
---

# Evidence-First Production Diagnosis

**Causality.** Localize the symptom before attributing it. Progress is evidence
that distinguishes explanations, not a convincing story. Separate diagnosis,
mitigation, implementation and observed recovery.

## Choose the requested result

- **Diagnose or review:** inspect permitted evidence read-only. Finish with a
  supported cause, contributors or ranked hypotheses and the next discriminating
  observation. A post-hoc diagnosis does not authorize a fix or require live recovery.
- **Design a response:** provide the requested mitigation, correction or prevention
  plan with preconditions, failure signals and evidence gaps; label it proposed.
- **Fix locally:** implement the authorized correction, run applicable focused
  checks and repair failures it introduced. Report what local verification cannot
  establish about production.
- **Operate or verify live:** keep the exact authorized action, environment,
  targets and bounds. Rollback, restart, scaling, flag changes, failover, cache
  flush, session cancellation and production load/fault tests need that authority.

During live impact, prioritize an authorized reversible mitigation over a complete
investigation. Read [incident operations](references/incident-operations.md) when
mitigation, perishable evidence, rollout, recovery or prevention is in scope.
The cause can remain unresolved after impact stops; record the remaining work
rather than claiming it has been performed or promising background investigation.

Preserve host permissions and data confidentiality. Read-only probes can still
consume capacity or expose sensitive data; scope target, window and collection
cost. Tool access is not authorization. Ask only for a consequential missing
choice, input or authority, and continue independent permitted investigation.

## Contract the symptom from available evidence

Record metric and unit, baseline/comparison window, affected cohort, onset and
shape when available. Cohorts may be endpoints, tenants, regions, instances,
versions or payload classes. Note unaffected cohorts that distinguish causes.
Keep unavailable dimensions explicit; do not fabricate numbers or block useful
triage solely because a complete baseline is unavailable.

Build a relevant change timeline: deploy/config/flag changes, dependency events,
quotas or expirations, traffic mix, schedules and data growth. Do not assume the
last deploy caused the incident. Correlation nominates a hypothesis; it does not
establish the mechanism. Gather only sources that can change the current decision.

## Localize and discriminate

At the suspect request boundary, determine whether degradation is produced here
or inherited. Use aligned trace self/downstream time for latency, originating
error signatures for failures, utilization and queue evidence for saturation,
and cohort/key/instance comparisons for skew. Independent percentile subtraction
is not per-request attribution. Loud upstream alerts can be consequences of a
slower dependency, but onset alone is not proof of causality.

State a testable mechanism and prediction before the probe: if X causes the
symptom through Y, Z should be observable; result W would refute it. Choose the
cheapest safe observation distinguishing the leading explanation from a practical
competitor. Control causal variables where possible; label confounded changes.
Use supplied captures, traces or code before collecting them again.

A supported cause should account for the relevant onset, shape, cohort and
unaffected evidence. Some incidents have multiple contributors; explain what each
accounts for instead of forcing a single cause or claiming a reproduction ends
all uncertainty. Missing evidence permits a bounded plan, not blind tuning.

## Route only a localized unresolved decision

| Boundary | Optional specialist |
| --- | --- |
| PostgreSQL work or contention | `postgres-performance` |
| Cache freshness or origin amplification | `cache-engineering` |
| Broker delivery and recovery | `reliable-messaging` |
| Durable job execution and schedules | `durable-background-jobs` |
| External provider | `external-api-integration` |
| Conflicting durable writers | `concurrency-control` |
| Identity and permission enforcement | `auth-access-control` |
| Cross-service topology | `distributed-system-design` |

Carry the symptom, source/window identity, observations and missing question into
a needed deep dive. These are expertise boundaries, not automatic delegation or
a requirement to restart diagnosis under every matching skill. Retain service
code, configuration, network or other-store reasoning here when sufficient.

## Report and stop at the evidence boundary

Lead with cause or current hypothesis, decisive evidence, alternative explanation,
requested remedy/probe and limits. In a causal review, distinguish supported,
plausible-but-unproven and refuted links. During an incident, include actual
mitigation state, residual impact and unresolved cause without inventing closure.

A diagnostic task ends when its requested question is answered to the supported
level or the next necessary evidence is unavailable. A local fix ends with the
requested code and applicable checks, not a mandatory live deployment. Live
recovery requires fresh comparable readback on the affected cohort and relevant
displacement checks. Keep proposed, implemented, locally tested, applied and
verified-live states separate. Reuse valid evidence for the same source and
window; do not add unrelated runbooks, alerts or a test platform as new gates.
