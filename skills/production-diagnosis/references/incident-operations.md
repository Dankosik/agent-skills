# Incident operations and recovery

Use the relevant sections for an active incident, an authorized intervention, a
recovery assessment or a requested prevention plan. This reference does not turn
a read-only diagnosis into operational authority.

## Mitigate without losing control

Choose from the accepted incident procedure and observed impact: rollback,
disabling a feature, shedding work, scaling or failover are alternatives, not a
sequence to execute. Check the exact target, authority, preconditions, blast radius,
stop signal and rollback or roll-forward boundary. Preserve data and credentials.
A missing operational approval does not stop independent safe diagnosis.

Capture perishable evidence before restarting or changing capacity when collection
is permitted, bounded and does not materially delay urgent mitigation. Prefer
existing lightweight logs/metrics before dumps or expensive traces. There is no
universal capture duration or requirement to delay an authorized emergency action
until every artifact exists. Record evidence that could not safely be retained.

Mitigation can hide the symptom without removing its cause. Record what changed,
when, who authorized it, what it masks and the remaining investigation or owner.
Do not silently broaden a rollback into credential rotation, data repair or a
traffic experiment.

## Correct and verify the requested change

Implement the smallest supported correction at its causal owner when authorized.
Keep one attributable change per observation window where feasible. If multiple
emergency changes are necessary, record the attribution limit rather than infer
causality from combined recovery.

Verify the original metric and affected cohort over a comparable window, including
load and configuration differences. Check relevant displacement into errors,
queues, resource exhaustion or another cohort. A local regression test is useful
but not evidence that live impact has ended. Mitigation-dependent recovery is not
proof that the underlying correction works without the mitigation.

Remove temporary mitigations only under the accepted authority and after checking
current risk. Retain an owner and removal condition when cleanup must wait. Do not
restart a completed diagnosis merely to force a live verification result.

## Prevention when requested

Select guards for the demonstrated failure: a leading signal, focused regression,
runbook correction or release check. Identify the detection gap and an owner for
each proposed follow-up. Do not require every possible alert, runbook and gate for
a narrow diagnostic answer; distinguish recommendations from artifacts actually
created or deployed.
