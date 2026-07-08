# Context Loading Policy

Purpose: make selective context loading deterministic, evidence-aware, and bounded.

Context engineering is treated here as a practical discipline for deciding what context is loaded, when, and why. This repository does not treat it as a formal standard.

## Startup stages

Required startup order:

1. Read bootstrap manifest.
2. Detect command-style invocation, if present.
3. Identify active task and project.
4. Load control documents declared by manifest.
5. Search registry metadata.
6. Select candidate entries.
7. Check freshness and supersession.
8. Load full content only for selected entries.
9. Search external sources when triggered.
10. Stop when evidence threshold is satisfied.

## File selection criteria

Apply these criteria in order:

1. explicit user reference
2. active command route
3. active project
4. declared authority
5. task-type relevance
6. dependency relation
7. freshness
8. unresolved conflict
9. available context budget

A file should not be loaded merely because it exists.

## Context budget

Use the smallest context that protects correctness. Prefer metadata and targeted sections first. Load full files when the task depends on exact wording, schema shape, validation behavior, authority, unresolved conflict, command behavior, raw idea capture format, or structured handover state.

## Command loading triggers

Load `protocols/COMMAND_ROUTING_PROTOCOL.md` when the user writes a command-style phrase such as:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
<command>
```

Load `docs/COMMANDS_AND_RAW_IDEAS.md` when the user asks what the command system is, how to use it, or how raw idea capture works.

Command context is repository-wide. It should be loaded before domain-specific files, but it should not cause the model to load every domain adapter.

## Raw idea loading triggers

Load `incubator/raw-ideas/README.md` and `incubator/raw-ideas/_model_capture_template.md` when:

- the user invokes `ایده خام`;
- the user asks to preserve a raw idea;
- the conversation produces a reusable but immature idea;
- the model needs to create or propose a raw idea record.

Load `incubator/raw-ideas/INBOX.md` only when updating or inspecting fast-capture entries.

Load existing files under `incubator/raw-ideas/captured/` only when the user names them, asks to review raw ideas, or a maturation task depends on a specific captured idea.

## Freshness checks

Check freshness when the claim depends on:

- live repository state;
- CI/check status;
- software versions;
- public documentation;
- security or dependency status;
- legal/compliance facts;
- external API behavior;
- active project status;
- handover state that may have been superseded by live repository changes.

## Conflict detection

A conflict exists when two loaded sources disagree about authority, status, version, scope, validation, allowed next action, command behavior, raw idea boundary, or canonical handover state. High-authority conflicts must be preserved and resolved before using the affected claim as active guidance.

## Full-file loading triggers

Load a full file when:

- the user names the file;
- the file is a control document for the active route;
- the command route depends on exact command wording;
- raw idea capture depends on the exact template;
- schema or validator behavior depends on complete structure;
- a lifecycle or supersession decision depends on exact wording;
- a patch will modify that file;
- a quoted section is insufficient to evaluate the claim;
- a structured handover state, handover manifest, or session continuity capsule is the input to the task.

## Continuity loading triggers

Load continuity protocols when:

- the user asks to close, compact, transfer, or resume a session;
- the user provides a resume prompt, capsule, manifest, or handover package;
- the conversation includes multiple PRs, branches, architecture decisions, external sources, model outputs, command additions, or raw ideas that must persist;
- context loss would materially harm continuation.

For continuity tasks, load structured state before rendered Markdown views.

## External-search triggers

Search external sources when:

- the answer depends on current or unstable facts;
- the repository claims to follow a changing standard or public guidance;
- a source version or vendor behavior may have changed;
- security, legal, medical, financial, or dependency facts matter;
- the user asks for latest, current, today, or recent information.

## Retrieval stop conditions

```yaml
retrieval_stop_when:
  - applicable_authoritative_contract_loaded
  - command_route_loaded_when_invoked
  - raw_idea_template_loaded_when_capture_is_requested
  - required_claims_have_evidence
  - no_unresolved_high_authority_conflict
  - canonical_structured_handover_state_loaded_when_needed
  - additional_sources_are_redundant
  - context_budget_threshold_reached
```

## Insufficient evidence handling

If evidence threshold is not met:

1. Mark the specific claim as `insufficient_evidence`, `not_checked`, or `not_verifiable`.
2. State what is missing.
3. Do not convert uncertainty into a pass/fail result.
4. Continue only when the remaining action is safe and scoped.
5. Escalate when the missing evidence affects safety, correctness, permissions, publishing, destructive operations, accepted handover state, command behavior, or memory promotion.

## Determinism rule

For the same task, same active command, same active project, same repository state, same structured handover state, and same available context budget, the selection process should choose the same first-read files and the same evidence threshold.
