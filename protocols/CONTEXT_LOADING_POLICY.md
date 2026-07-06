# Context Loading Policy

Purpose: make selective context loading deterministic, evidence-aware, and bounded.

Context engineering is treated here as a practical discipline for deciding what context is loaded, when, and why. This repository does not treat it as a formal standard.

## Startup stages

Required startup order:

1. Read bootstrap manifest.
2. Identify active task and project.
3. Load control documents declared by manifest.
4. Search registry metadata.
5. Select candidate entries.
6. Check freshness and supersession.
7. Load full content only for selected entries.
8. Search external sources when triggered.
9. Stop when evidence threshold is satisfied.

## File selection criteria

Apply these criteria in order:

1. explicit user reference
2. active project
3. declared authority
4. task-type relevance
5. dependency relation
6. freshness
7. unresolved conflict
8. available context budget

A file should not be loaded merely because it exists.

## Context budget

Use the smallest context that protects correctness. Prefer metadata and targeted sections first. Load full files when the task depends on exact wording, schema shape, validation behavior, authority, or unresolved conflict.

## Freshness checks

Check freshness when the claim depends on:

- live repository state;
- CI/check status;
- software versions;
- public documentation;
- security or dependency status;
- legal/compliance facts;
- external API behavior;
- active project status.

## Conflict detection

A conflict exists when two loaded sources disagree about authority, status, version, scope, validation, or allowed next action. High-authority conflicts must be preserved and resolved before using the affected claim as active guidance.

## Full-file loading triggers

Load a full file when:

- the user names the file;
- the file is a control document for the active route;
- schema or validator behavior depends on complete structure;
- a lifecycle or supersession decision depends on exact wording;
- a patch will modify that file;
- a quoted section is insufficient to evaluate the claim.

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
  - required_claims_have_evidence
  - no_unresolved_high_authority_conflict
  - additional_sources_are_redundant
  - context_budget_threshold_reached
```

## Insufficient evidence handling

If evidence threshold is not met:

1. Mark the specific claim as `insufficient_evidence`, `not_checked`, or `not_verifiable`.
2. State what is missing.
3. Do not convert uncertainty into a pass/fail result.
4. Continue only when the remaining action is safe and scoped.
5. Escalate when the missing evidence affects safety, correctness, permissions, publishing, or destructive operations.

## Determinism rule

For the same task, same active project, same repository state, and same available context budget, the selection process should choose the same first-read files and the same evidence threshold.
