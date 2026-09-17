# Tool routing for bounded evidence collection

Choose from tools the host actually exposes and the user has authorized. For
several independent sources, supported programmatic tool calling or native
parallel calls may reduce repeated transfer and join/filter work. Neither is a
prerequisite. If unavailable, use direct read-only calls and process already
retrieved data locally when allowed; do not install a runtime, invent tool names,
request broader access or block the diagnosis merely to use this pattern.

Name the target cluster/service, time window, record and cost limits, source
identities, concurrency and retry budget before collection. Keep within host
limits and source capacity. Four concurrent reads and one transient retry are
conservative starting bounds, not quotas to fill or overrides of tighter limits.
Dependent probes stay sequential when each observation changes the next action.

Preserve enough information to audit the result: window, statistics-reset
boundaries, comparable resource deltas, ranked workload, anomalies, missing or
truncated sources, and references back to evidence. Use the requested format;
a fixed JSON envelope is useful only when a consumer actually requires it. Never
turn an inaccessible or truncated source into a zero or a successful empty result.

Stop bounded collection when each selected source succeeded or its permitted
recovery is exhausted. Retain partial evidence and the specific gap. Keep causal
judgment, authority decisions, side effects and EXPLAIN safety in the direct
review path. Prefer direct calls when results are small, adaptive, or need native
citations/artifacts that batching would lose. Complete supplied evidence valid for
the same window need not be fetched again just to appear fresh.
