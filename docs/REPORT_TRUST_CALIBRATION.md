# Report Trust Calibration

Reports are a safety boundary. A polished report can create false confidence even when individual fields are cautious.

Every serious report should separate:

- what was checked
- what was not checked
- what is tool-backed
- what is model-inferred
- what is user-approved
- what is uncertain
- what is quarantined
- what a downstream model may use

## Restricted phrases

Avoid or explicitly scope these phrases:

```text
secure
safe
audited
certified
compliant
production-ready
fully verified
no vulnerabilities
all tests passed
```

Preferred phrasing:

```text
checked within this scope
tool reported
model inferred
not verified
requires escalation
not safe for downstream memory yet
```
