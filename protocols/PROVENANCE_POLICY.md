# Provenance Policy

Purpose: define a lightweight internal provenance model for sources, claims, decisions, artifacts, model outputs, and handoffs.

This repository uses W3C PROV as conceptual inspiration only. It does not claim PROV compliance.

```yaml
provenance_model:
  inspiration: W3C_PROV
  compliance: false
  implementation: simplified_internal_model
```

## Entity / activity / agent mapping

### Entity

An entity is a thing that may be referenced, derived, reviewed, superseded, archived, or used as evidence.

Allowed entity categories:

- `source`
- `claim`
- `decision`
- `requirement`
- `artifact`
- `model_output`
- `handoff`
- `handover_manifest`
- `session_continuity_capsule`
- `open_question`

### Activity

An activity is a process that uses or generates entities.

Allowed activity categories:

- `research`
- `inspection`
- `implementation`
- `validation`
- `review`
- `approval`
- `promotion`
- `supersession`
- `archival`
- `handover_rendering`
- `handover_intake`
- `session_continuity_capture`

### Agent

An agent is an actor or system associated with an activity.

Allowed agent categories:

- `user`
- `llm`
- `tool`
- `ci`
- `external_source`
- `human_reviewer`

## Source references

A source reference should include as many of these as practical:

```yaml
source_ref:
  type: repository_file | tool_result | ci_run | external_source | attached_artifact | user_instruction | model_output | handover_manifest | structured_handover_state | rendered_handover_view
  locator: string
  revision: string | null
  timestamp: string | null
  content_hash: string | null
  trust_class: string
  provenance_limits: []
```

## Relationship fields

Use these fields when recording provenance:

```yaml
derived_from: []
used: []
generated_by: string | null
supersedes: []
superseded_by: []
```

## Handover provenance

A handover package or session continuity capsule should preserve:

```yaml
handover_provenance:
  structured_state_ref: string
  rendered_views: []
  source_refs: []
  evidence_refs: []
  generated_by: string | null
  derived_from: []
  provenance_limits: []
```

Rendered Markdown views should reference the structured state they were derived from. They should not be treated as canonical when a structured state exists.

## Content hashes

Use content hashes where practical for stable artifacts, generated packages, evidence logs, and handoffs. Hashes are not required for every Markdown note, but they are useful when later models must identify the exact artifact that was reviewed.

Do not invent hashes. If a hash was not computed, record `content_hash: null` and preserve the limit.

## Source timestamps

When a source can change, record the access or source timestamp. This is required for current-version, current-policy, CI-status, live-repository, and handover-intake claims.

## Provenance limits

Every provenance object may include limits such as:

- source was inspected only in part;
- no external source was consulted;
- CI result was pending;
- hash was unavailable;
- artifact was user-provided and not independently verified;
- model output was reviewed but not used as evidence;
- Markdown was rendered from structured state but not revalidated;
- live repository state was not rechecked after capsule creation.

## Minimal provenance object

```yaml
entity:
  id: ENT-0001
  type: claim
activity:
  id: ACT-0001
  type: validation
agent:
  id: AGT-0001
  type: tool
used:
  - ART-0001
generated_by: ACT-0001
derived_from:
  - SRC-0001
supersedes: []
superseded_by: []
provenance_limits:
  - Scope limited to inspected revision.
```

## Non-compliance statement

Do not say this repository implements W3C PROV unless a future version adds formal PROV semantics, serializations, and conformance checks. Current behavior is a simplified internal provenance model.
