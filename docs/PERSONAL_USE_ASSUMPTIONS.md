# Personal Use Assumptions

This system is designed around the user's real workflow.

## Assumptions

- The user uses LLMs as the primary expert workforce.
- Analysis is usually performed by an LLM.
- Implementation is usually performed by an LLM.
- Reports are usually produced by an LLM.
- Outputs may become input to another LLM.
- The user is not expected to technically verify most specialist claims.
- The user coordinates direction, approvals, risk tolerance, and next actions.

## Consequence

The system must not rely on the user as the technical verifier.

When a technical claim cannot be verified, the system must escalate through tools, validators, fixtures, CI checks, second-model critique, stronger-model review, current-source research, quarantine, or explicit `not_verifiable` status.
