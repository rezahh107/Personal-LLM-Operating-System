# Repository as LLM Memory

The repository is persistent memory for future LLM sessions.

It is also an instruction surface, coordination state, protocol registry, claim ledger, evidence ledger, and handoff layer.

## Memory classes

| Memory type | Meaning | Downstream trust |
| --- | --- | --- |
| `accepted_protocol` | Stable behavior rule or workflow contract | Trusted within scope |
| `accepted_decision` | User-approved direction | Trusted within scope |
| `validated_claim` | Claim backed by evidence, validator, tool, or eval | Trusted within scope |
| `candidate_claim` | Model-generated claim not yet validated | Not trusted |
| `quarantined_claim` | Useful but unsafe or unsupported claim | Not trusted |
| `deprecated_memory` | Old memory kept for history | Historical only |
| `transient_report` | Temporary run output | Not trusted unless promoted |

## Central rule

```text
Raw conversation is not memory.
Matured, classified, and accepted output is memory.
```

Permanent memory should be short, stable, scoped, source-aware, and downstream-safe.
