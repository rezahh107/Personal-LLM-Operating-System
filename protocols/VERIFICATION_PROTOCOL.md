# Verification Protocol

Purpose: define claim-specific evidence requirements so repository memory does not mix accepted decisions, model confidence, and technical verification.

A claim is verified only for the exact subject, method, evidence, revision, environment, and scope limits that were checked.

## Claim taxonomy

Use these claim types for verification-sensitive work:

- `file_exists`
- `code_implemented`
- `build_passes`
- `tests_pass`
- `bug_fixed`
- `ci_green`
- `architecture_compliant`
- `security_checks_passed`
- `latest_version`
- `deterministic_behavior`
- `handover_state_complete`
- `session_continuity_preserved`

## Verification status vocabulary

```yaml
verification_status:
  - not_checked
  - statically_inspected
  - source_supported
  - tool_observed
  - reproduced
  - test_verified
  - fixture_verified
  - externally_reviewed
  - not_verifiable
  - insufficient_evidence
```

## Continuity truth status vocabulary

Use these truth statuses for factual project claims inside handover packages and session continuity capsules:

```yaml
truth_status:
  - evidence-backed
  - derived_with_lineage
  - explicitly_proposed
  - connected_to_structured_gap
  - not_applicable
```

Do not place `explicitly_proposed` or `connected_to_structured_gap` claims inside confirmed decisions unless the decision explicitly records that the factual claim is not accepted.

## Minimum evidence matrix

| Claim type | Minimum evidence |
|---|---|
| `file_exists` | repository path, revision, and file metadata or tool-observed fetch result |
| `code_implemented` | inspected file path, revision, relevant symbol/behavior, and implementation reference |
| `build_passes` | command, environment, revision, exit code, and logs or CI job reference |
| `tests_pass` | test harness, command, environment, revision, exit code, and result/log reference |
| `bug_fixed` | original failing behavior, fix revision, reproducer or test, and residual limits |
| `ci_green` | workflow name, run ID, commit SHA, job conclusions, and timestamp |
| `architecture_compliant` | named architecture rule, inspected artifact, revision, reviewer/method, and limits |
| `security_checks_passed` | named check, tool/source, scope, revision, environment, and exclusions |
| `latest_version` | source URL/name, retrieval timestamp, compared version, and freshness risk |
| `deterministic_behavior` | repeated runs, same input, same environment, observed outputs, and nondeterminism limits |
| `handover_state_complete` | structured state fields, manifest or schema reference, completeness check, and known gaps |
| `session_continuity_preserved` | capsule metadata, timeline, decisions, candidate ideas, evidence map, risks, next action, do-not-assume list, and exact resume prompt |

## Forbidden absolute claims

Do not make unscoped claims such as:

- `secure`
- `fully verified`
- `production ready`
- `all tests passed`
- `latest`

These may be used only when the exact scope, evidence, revision, environment, and limits are stated. Prefer scoped wording such as: `The foundation validator passed on commit <sha> in GitHub Actions run <id>.`.

## Tool-result requirements

Tool-supported claims must include:

```yaml
subject:
  repository: string
  revision: commit-sha-or-ref
method:
  tool_or_harness: string
  command_or_operation: string
  environment: string
  timestamp: string
evidence:
  result_ref: string
  exit_code: number-or-null
scope_limits: []
verification_status: string
```

## Not-run reporting

If a validation path was not executed, say so directly:

```yaml
command: python3 scripts/validate_foundation.py
executed: false
verification_status: not_checked
reason: local execution unavailable
```

Do not convert a planned command into an executed result.

## Handover verification rules

For handover and continuity artifacts:

1. A rendered Markdown view is not verification of structured state.
2. A source archive is not verification of repository transfer.
3. A repository transfer is not verification of project handover completeness.
4. A candidate idea is not an accepted decision.
5. A not-run check must remain `not_checked`.
6. A prior model output is not evidence unless separately verified.

Use `insufficient_evidence` when a required handover source, manifest, schema, live repository state, CI log, or validation output is unavailable.

## Escalation conditions

Escalate or mark `insufficient_evidence` when:

- evidence and claim type do not match;
- source freshness is material and unknown;
- a tool result conflicts with repository memory;
- CI status is unavailable for a CI claim;
- security or correctness depends on a tool that was not run;
- a prior model output is the only support;
- model agreement is the only support;
- a session continuity capsule lacks an exact resume prompt;
- a confirmed decision contains an unverified execution, CI, or repository-state claim.

## Verification claim example

```yaml
claim_id: "CLAIM-0042"
claim_type: "tests_pass"
statement: "The Firefox popup regression test passes."
subject:
  repository: "owner/repository"
  revision: "commit-sha"
method:
  harness: "Playwright"
  command: "npm run test:e2e:firefox"
  environment: "Ubuntu 24.04 / Firefox 128"
evidence:
  exit_code: 0
  log_ref: "ART-0091"
  result_ref: "ART-0092"
scope_limits:
  - "Only Firefox Desktop was tested."
  - "No Windows execution was performed."
verification_status: "test_verified"
```

## Multi-model review boundary

Agreement between models is a review signal. It can justify further inspection, but it is not factual verification, technical proof, CI evidence, fixture evidence, or tool evidence.
