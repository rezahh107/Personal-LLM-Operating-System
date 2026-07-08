# Knowledge Capture Protocol

Purpose: define how valuable conversation output can become candidate repository memory.

## Core rule

Raw conversation is not memory.

Only matured, classified, scoped, sourced, lifecycle-aware, and reviewable output can become repository memory.

## Raw idea capture is different

Raw idea capture preserves possibility before memory promotion.

Use `incubator/raw-ideas/` when the goal is to avoid losing the core idea, not to establish it as accepted memory.

A raw idea may be captured when:

- the user explicitly invokes the `ایده خام` command;
- the user asks the model to preserve an early idea;
- a conversation produces a reusable but immature idea;
- the model can identify a clear core idea without over-polishing it.

A raw idea must be marked with:

```yaml
status: raw_idea
lifecycle_status: incubating
verification_status: unverified
promote_to_memory: false
```

Raw ideas can later enter `protocols/IDEA_MATURATION_PIPELINE.md`, but raw idea capture alone is not memory promotion.

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
- a session continuity capsule that preserves reusable project state

## What must not be captured as accepted memory

Do not capture as accepted memory:

- sensitive data that is not required for future work
- private data that is not necessary for future work
- short-lived tasks
- unsupported technical claims as accepted memory
- one-off conversation noise
- raw model reasoning
- external facts without freshness handling
- target repository content that was not reviewed for trust class
- prior model output as evidence without separate verification
- rendered handover Markdown as canonical state when structured state exists
- raw ideas that have not passed maturation and promotion gates

## Candidate memory classification

Use these labels before promotion:

- `candidate_user_preference`
- `candidate_accepted_decision`
- `candidate_domain_insight`
- `candidate_prompt_pattern`
- `candidate_failure_mode`
- `candidate_repository_registry_update`
- `candidate_protocol_improvement`
- `candidate_session_continuity_capsule`
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

### Session continuity capsule

```yaml
classification: candidate_session_continuity_capsule
content: Structured session state that may help future models resume without losing evidence boundaries.
trust_class: active_user_instruction
governance_authority: advisory
epistemic_support: source_supported
verification_status: source_supported
lifecycle_status: candidate
promotion_gate: user approval plus successful handover intake
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

### Raw idea capture

```yaml
status: raw_idea
content: A reusable but immature idea that should not be lost.
origin: user_conversation
lifecycle_status: incubating
verification_status: unverified
promote_to_memory: false
suggested_file: incubator/raw-ideas/captured/YYYY-MM-DD-short-title.md
promotion_gate: idea maturation plus memory classification
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

When a session produces a reusable raw idea that is not ready for memory promotion, use:

```text
Raw idea capture candidate:
- core idea:
- origin:
- status: raw_idea
- verification_status: unverified
- suggested file:
- next review trigger:
```

If nothing should be captured, say so briefly.
