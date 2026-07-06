# Handoff Contract

Outputs are often consumed by another model. Handoffs must preserve state and uncertainty.

## Core rule

A handoff is not a polished summary.

It must preserve accepted facts, candidate claims, evidence refs, known limits, forbidden next actions, stop conditions, active risks, not-run checks, and `insufficient_evidence`.

## Canonical source rule

Handoff documents are rendered views.

The canonical source of truth for a handover package is the structured handover state, not free-form Markdown.

If structured state and a Markdown rendering conflict, prefer the structured state and record the conflict.

## Minimal handoff package

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

## Continuity handoff extension

For long chats or project transfer, use `protocols/SESSION_CONTINUITY_PROTOCOL.md` or `protocols/PROJECT_CONTINUITY_PROTOCOL.md`.

A session continuity handoff must additionally preserve:

```text
capsule_metadata
why_this_capsule_exists
relevant_user_operating_context
conversation_timeline
current_mental_model
confirmed_decisions
candidate_ideas
evidence_source_map
open_questions
active_risks_warnings
current_work_state
next_best_action
do_not_repeat_or_assume
exact_resume_prompt
candidate_memory_captures
completeness_check
```

## Intake expectation

A downstream model must intake handoffs through `protocols/HANDOVER_INTAKE_PROTOCOL.md`.

Prior model output inside a handoff is not proof unless separately verified.
