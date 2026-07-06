# Handoff Contract

Outputs are often consumed by another model. Handoffs must preserve state and uncertainty.

Every handoff package should include:

```text
task_goal
source_context
accepted_facts
candidate_claims
quarantined_claims
evidence_refs
known_limits
allowed_next_actions
forbidden_next_actions
required_output_schema
stop_conditions
```

A downstream model must not receive a flattened report where accepted facts and candidate claims are mixed together.
