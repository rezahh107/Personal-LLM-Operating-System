# Model-Facing Automation

This repository may include scripts that look like command-line tools. They are not intended as the user's primary interface.

## Interface rule

```yaml
user_facing: false
model_facing: true
ci_facing: true
automation_facing: true
```

The user should be able to work through natural language, short review summaries, and pull requests.

Models and GitHub Actions may use scripts to create, validate, and check repository memory artifacts.

## Why this exists

Without model-facing automation, the repository remains a policy book with no enforcement. Scripts make claim lifecycle, handoff contracts, memory indexes, and fixtures testable.

## User interaction pattern

The user says:

```text
Register this as a candidate claim and quarantine it if it is incomplete.
```

The model should then:

```text
1. create the structured file or ledger entry
2. run validation
3. report pass/fail in plain Persian
4. open or update a pull request
```

The user should not need to run terminal commands directly.
