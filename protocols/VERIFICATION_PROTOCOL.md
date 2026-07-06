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

## Escalation conditions

Escalate or mark `insufficient_evidence` when:

- evidence and claim type do not match;
- source freshness is material and unknown;
- a tool result conflicts with repository memory;
- CI status is unavailable for a CI claim;
- security or correctness depends on a tool that was not run;
- a prior model output is the only support;
- model agreement is the only support.

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
