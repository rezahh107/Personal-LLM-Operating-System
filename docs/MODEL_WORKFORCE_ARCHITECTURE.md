# Model Workforce Architecture

The system treats language models as a workforce with bounded roles, not as one all-purpose authority.

| Role | Purpose | Allowed output | Not allowed |
| --- | --- | --- | --- |
| `Framer` | Clarifies raw user intuition | Problem frame, scope, assumptions | Final decision |
| `Inspector` | Reads project state | Candidate findings, observations | Execution claims |
| `Skeptic` | Attacks assumptions and outputs | Critique, missing evidence, risks | Silent acceptance |
| `Builder` | Proposes or applies scoped changes | Patch plan, implementation | Broad rewrite without scope |
| `Reporter` | Produces user-facing summary | Plain-language report from structured state | New technical claims |
| `Handoff Writer` | Packages context for downstream models | Schema-preserving handoff | Flattening uncertainty |
| `Verifier` | Checks output against rules | Validation result | Inventing evidence |
| `Domain Specialist` | Works inside a domain adapter | Domain-specific output | Ignoring parent protocol |

A model may play multiple roles only when the output clearly separates the roles.
