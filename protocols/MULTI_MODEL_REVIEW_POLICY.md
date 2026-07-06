# Multi-Model Review Policy

Purpose: prevent model agreement from being treated as proof while preserving its value for critique and missing-issue detection.

## Core rule

Multiple models agreeing on an answer is a review signal, not verification evidence.

```yaml
multi_model_agreement:
  use_as:
    - consensus_signal
    - missing_issue_detection
    - alternative_review
  do_not_use_as:
    - factual_verification
    - technical_proof
    - CI_or_test_evidence
```

## Review independence fields

A multi-model review should record independence conditions:

```yaml
review_independence:
  prior_answer_visible: false
  sources_shared: false
  prompt_independent: true
```

If prior answers or shared sources were visible, the review may still be useful, but independence is lower.

## Appropriate uses

Use multi-model review to:

- find missing edge cases;
- challenge assumptions;
- compare interpretations;
- identify unclear instructions;
- detect possible hallucinations;
- prioritize claims for tool or source verification.

## Inappropriate uses

Do not use multi-model review to claim:

- tests passed;
- CI is green;
- code is correct;
- security checks passed;
- a repository file exists;
- a version is latest;
- a behavior is deterministic.

Those claims require the evidence type defined by `protocols/VERIFICATION_PROTOCOL.md`.

## Reporting template

```yaml
review_type: multi_model_review
models_or_reviewers: []
review_independence:
  prior_answer_visible: false
  sources_shared: false
  prompt_independent: true
findings: []
verification_status: insufficient_evidence
next_required_verification: tool_or_source_check
```

## Handoff rule

A downstream handoff may include multi-model agreement as a review note, but accepted facts must still point to source, tool, CI, fixture, validator, or human-review evidence.
