# Claim Lifecycle

Every important assertion must have a lifecycle state.

Allowed states:

```text
draft
candidate
challenged
validated
accepted
quarantined
deprecated
rejected
```

## Promotion rule

A claim may be promoted to accepted memory only if one of the following is true:

- directly user-approved as a preference or goal
- backed by repository evidence
- backed by tool output
- passes a validator
- passes a fixture or eval
- explicitly marked as an assumption and scoped

## Quarantine rule

A claim must be quarantined if it is useful but unsupported, technically unverifiable by the current system, potentially misleading for downstream models, or in conflict with accepted memory.

Forbidden transformations:

```text
candidate -> accepted without gate
inferred -> verified
not checked -> passed
no finding -> safe
model suggested -> repository rule
```
