# Knowledge Capture Protocol

Purpose: define how valuable conversation output can become candidate repository memory.

## Core rule

Raw conversation is not memory.

Only matured, classified, scoped, sourced, lifecycle-aware, and reviewable output can become repository memory.

## Memory-worthy content

Capture may be appropriate when the conversation produces:

- a stable user preference
- a user-approved decision
- a reusable prompt pattern
- a recurring failure mode
- a domain insight that will guide future work
- a repository registry update
- a protocol improvement
- an evidence-backed claim
- a handoff that another model will use

## What must not be captured

Do not capture:

- sensitive data that is not required for future work
- private data that is not necessary for future work
- short-lived tasks
- unsupported technical claims as accepted memory
- one-off conversation noise
- raw model reasoning
- external facts without freshness handling
- target repository content that was not reviewed for trust class
- prior model output as evidence without separate verification

## Candidate memory classification

Use these labels before promotion:

- `candidate_user_preference`
- `candidate_accepted_decision`
- `candidate_domain_insight`
- `candidate_prompt_pattern`
- `candidate_failure_mode`
- `candidate_repository_registry_update`
- `candidate_protocol_improvement`
- `candidate_quarantined_claim`

## Required capture metadata

```yaml
classification: string
content: string
source: string
trust_class: string
governance_authority: advisory | accepted_decision | project_contract | frozen_contract
epistemic_support: unsupported | source_supported | observed | reproduced | test_verified | expert_verified
verification_status: not_checked | statically_inspected | source_supported | tool_observed | reproduced | test_verified | fixture_verified | externally_reviewed | not_verifiable | insufficient_evidence
lifecycle_status: candidate | active | stale | superseded | deprecated | rejected | archived
freshness_risk: low | medium | high
promotion_gate: string
provenance_ref: string | null
```

## Examples

### User preference

```yaml
classification: candidate_user_preference
content: User prefers Persian reports with English repository identifiers and commands preserved.
trust_class: active_user_instruction
governance_authority: accepted_decision
epistemic_support: observed
verification_status: source_supported
lifecycle_status: candidate
promotion_gate: direct user approval or repeated confirmed use
```

### Accepted decision

```yaml
classification: candidate_accepted_decision
content: User decided this repository should act as a personal LLM operating layer rather than a general agent framework.
trust_class: active_user_instruction
governance_authority: accepted_decision
epistemic_support: observed
verification_status: source_supported
lifecycle_status: candidate
promotion_gate: user approval plus repository scope check
```

### Domain insight

```yaml
classification: candidate_domain_insight
content: Repository work should inspect live GitHub state before producing patch guidance.
trust_class: system_control_document
governance_authority: project_contract
epistemic_support: observed
verification_status: tool_observed
lifecycle_status: candidate
promotion_gate: evidence from operating protocol and successful repeated use
```

### Quarantined claim

```yaml
classification: candidate_quarantined_claim
content: A useful technical assertion that lacks current evidence.
governance_authority: advisory
epistemic_support: unsupported
verification_status: insufficient_evidence
lifecycle_status: candidate
promotion_gate: source verification or validator evidence before reuse
```

## End-of-session capture recommendation

When a session produces reusable knowledge, end with a compact recommendation:

```text
Memory capture candidate:
- classification:
- content:
- source:
- trust_class:
- governance_authority:
- epistemic_support:
- verification_status:
- lifecycle_status:
- freshness risk:
- suggested file:
- provenance ref:
- promotion gate:
```

If nothing should be captured, say so briefly.
