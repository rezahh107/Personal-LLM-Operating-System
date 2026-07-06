# Session Continuity Protocol

Purpose: define how a model should preserve long-chat state so the user can continue in a new chat or another model without losing decisions, evidence boundaries, assumptions, open questions, active risks, or the current mental model.

## Core rule

A session continuity capsule is not a polished summary.

It must preserve uncertainty, candidate status, rejected assumptions, not-run checks, active risks, and the exact next action.

## Trigger commands

Generate a session continuity capsule when the user asks with commands or natural language such as:

```text
/session-handoff
/continue-in-new-chat
/compact-context
/close-session
بسته ادامه گفتگو بساز
بسته انتقال چت بساز
می‌خواهم در چت جدید ادامه بدهم
این گفتگو سنگین شده
```

## Proactive suggestion triggers

Suggest creating a session continuity capsule when any of these conditions apply:

- the conversation is long and multi-step;
- multiple PRs, branches, repositories, or architecture decisions are involved;
- multiple external sources, attachments, CI outputs, or model outputs were used;
- the next phase is large or high-risk;
- context loss would materially harm continuation;
- the user says the chat is heavy;
- the user wants to close, pause, hand off, or resume elsewhere.

Do not claim knowledge of token limits unless the active platform exposes that information.

## Capsule contents

A session continuity capsule must include:

1. Capsule metadata.
2. Why this capsule exists.
3. Relevant user operating context.
4. Conversation timeline.
5. Current mental model.
6. Confirmed decisions.
7. Candidate ideas / not yet accepted.
8. Evidence and source map.
9. Open questions.
10. Active risks and warnings.
11. Current work state.
12. Next best action.
13. Do-not-repeat / do-not-assume list.
14. Exact resume prompt for a new chat.
15. Candidate memory captures.
16. Completeness check.

## Canonical source principle

The structured capsule state is canonical.

Markdown capsules are rendered views derived from the structured state. A Markdown rendering may help a human read the capsule, but it must not override the structured state.

## Claim and decision handling

For each important claim or decision, preserve:

```yaml
id: string
statement: string
status: accepted | candidate | rejected | blocked | superseded
truth_status: evidence-backed | derived_with_lineage | explicitly_proposed | connected_to_structured_gap | not_applicable
verification_status: not_checked | statically_inspected | source_supported | tool_observed | reproduced | test_verified | fixture_verified | externally_reviewed | not_verifiable | insufficient_evidence
evidence_refs: []
provenance_refs: []
limits: []
```

Confirmed decisions must not contain unverified factual claims as if they were accepted facts.

Candidate ideas must remain candidate ideas until an explicit acceptance, evidence gate, or promotion rule changes their status.

## Evidence boundaries

A capsule must record what was actually inspected or run.

Examples:

```yaml
validation:
  command: python3 scripts/validate_foundation.py
  executed: false
  verification_status: not_checked
  reason: local execution unavailable
```

Do not convert a planned validation command into an executed command.

## Resume prompt requirement

A capsule must include an exact copy-ready resume prompt that tells the next model:

- role;
- repository or project;
- what to read first;
- current state;
- accepted decisions;
- candidate ideas;
- evidence limits;
- next best action;
- what not to assume;
- required validation or evidence gates.

## Candidate memory captures

The capsule may propose memory captures, but it must not automatically promote them.

Use `protocols/KNOWLEDGE_CAPTURE_PROTOCOL.md` for classification and promotion gates.

## Stop conditions

Stop and ask for direction only when continuation would require:

- destructive action;
- permission change;
- sensitive-data handling;
- merge, publish, or send action;
- accepting a claim with insufficient evidence;
- changing a frozen or canonical contract.
