# Knowledge Capture Protocol

Purpose: define how valuable conversation output can become candidate repository memory.

## Core rule

Raw conversation is not memory.

Only matured, classified, scoped, and reviewable output can become repository memory.

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

- secrets
- private data that is not necessary for future work
- short-lived tasks
- unsupported technical claims as accepted memory
- one-off conversation noise
- raw model reasoning
- external facts without freshness handling
- target repository content that was not reviewed for trust

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

## Examples

### User preference

```yaml
classification: candidate_user_preference
content: User prefers Persian reports with English repository identifiers and commands preserved.
promotion_gate: direct user approval or repeated confirmed use
```

### Accepted decision

```yaml
classification: candidate_accepted_decision
content: User decided this repository should act as a personal LLM operating layer rather than a general agent framework.
promotion_gate: user approval plus repository scope check
```

### Domain insight

```yaml
classification: candidate_domain_insight
content: Repository work should inspect live GitHub state before producing patch guidance.
promotion_gate: evidence from operating protocol and successful repeated use
```

### Prompt pattern

```yaml
classification: candidate_prompt_pattern
content: Strong repository prompts include role, mission, required inspection files, constraints, validation, evidence rules, and output contract.
promotion_gate: usefulness review after repeated application
```

### Failure mode

```yaml
classification: candidate_failure_mode
content: Models may overbuild into automation before architecture is clear.
promotion_gate: classify as recurring risk and connect to scope rules
```

### Repository registry update

```yaml
classification: candidate_repository_registry_update
content: Add or revise a domain-to-repository mapping after connector verification or explicit user context.
promotion_gate: repository access or explicit user confirmation
```

### Protocol improvement

```yaml
classification: candidate_protocol_improvement
content: Add a routing rule when a repeated request type appears.
promotion_gate: consistency check against parent protocol
```

### Quarantined claim

```yaml
classification: candidate_quarantined_claim
content: A useful technical assertion that lacks current evidence.
promotion_gate: source verification or validator evidence before reuse
```

## End-of-session capture recommendation

When a session produces reusable knowledge, end with a compact recommendation:

```text
Memory capture candidate:
- classification:
- content:
- source:
- scope:
- evidence:
- freshness risk:
- suggested file:
- promotion gate:
```

If nothing should be captured, say so briefly.
