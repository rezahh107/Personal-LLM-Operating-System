# Failure Modes

This file records recurring ways model-assisted work can fail in this repository.

The purpose is not blame. The purpose is to stop repeated failures from becoming permanent memory.

## Core failure modes

### FM-001 — Candidate becomes accepted memory

A model-generated idea is added to accepted docs without passing claim lifecycle, user approval, evidence, validation, or quarantine review.

Mitigation:

- require memory classification
- validate accepted claims for evidence or user approval
- use pull requests for promotion

### FM-002 — Uncertainty flattening in handoff

A handoff mixes accepted facts, candidate claims, and quarantined claims into one narrative.

Mitigation:

- enforce handoff schema
- require accepted/candidate/quarantined sections
- reject flattened handoffs in fixtures

### FM-003 — User treated as technical verifier

A model asks the user to judge exploitability, code correctness, CVE validity, security proof, or other specialist claims.

Mitigation:

- use escalation protocol
- ask the user only for coordination, direction, and approval decisions

### FM-004 — Prose-only enforcement

A critical behavior rule exists only in documentation with no schema, validator, fixture, CI check, or downstream rejection.

Mitigation:

- track critical rules in behavioral rule coverage
- add at least one mechanical carrier when risk is high

### FM-005 — Polished report creates false authority

A well-formatted report makes unsupported claims feel verified.

Mitigation:

- use report trust calibration
- show checked / unchecked / unknown
- ban assurance-like language unless scoped and evidence-backed

### FM-006 — Domain adapter ignored

A model works on audit, prompt engineering, repair, or another domain without loading its adapter.

Mitigation:

- require domain identification in `START_HERE_FOR_MODELS.md`
- add adapter-specific fixtures over time

### FM-007 — Automation becomes user burden

Scripts are designed as if the user must run CLI commands manually.

Mitigation:

- scripts are model-facing and CI-facing
- user interface remains natural language plus PR review summaries
