# Memory Review, Lifecycle, and Invalidation

Purpose: define how repository memory becomes active, stale, superseded, archived, or rejected without treating age alone as invalidation.

## Lifecycle status vocabulary

```yaml
lifecycle_status:
  - candidate
  - active
  - stale
  - superseded
  - deprecated
  - rejected
  - archived
```

## Core rules

- Old does not automatically mean invalid.
- Frozen contracts may remain authoritative while old.
- Fast-changing facts may become stale quickly.
- Archive or supersession is preferred over deletion for auditability.
- Deletion is reserved for sensitive data, privacy requests, duplicates, or explicit user request.

## Lifecycle meanings

- `candidate`: useful but not yet accepted or fully routed.
- `active`: currently usable within scope.
- `stale`: may be outdated; requires review before high-impact reuse.
- `superseded`: replaced by a newer item; keep pointer to replacement.
- `deprecated`: still historically meaningful but should not be used for new work.
- `rejected`: reviewed and not accepted.
- `archived`: preserved for audit/history, not active guidance.

## Invalidation triggers

```yaml
invalidation_triggers:
  - new_release
  - contract_revision
  - failed_fixture
  - user_profile_change
  - source_retraction
  - repository_state_change
  - tool_result_conflict
```

Also review memory when:

- the user says it is outdated;
- current external evidence conflicts with it;
- a workflow repeatedly fails;
- a better protocol replaced it;
- a downstream model misused it;
- the memory lacks source, scope, lifecycle, or freshness notes.

## Supersession handling

When a newer rule replaces an older rule:

1. Mark the older item as `superseded` or `deprecated`.
2. Add `superseded_by` pointing to the replacement.
3. Preserve why the replacement happened.
4. Do not leave conflicting active rules.
5. Prefer a short migration note over deleting history.

## Archival handling

Archive memory when it is no longer active but remains useful for audit, provenance, or historical understanding. Archived items must not be loaded as active instructions unless the task is explicitly historical or forensic.

## Deletion handling

Delete only when preservation is unsafe, harmful, duplicate, or explicitly requested by the user. When deletion happens, record a minimal non-sensitive deletion note when appropriate.

## Review frequency by knowledge type

High-frequency review:

- software versions
- CI behavior
- APIs
- package security
- product features
- public standards
- repository state claims

Medium-frequency review:

- repository workflows
- prompt patterns
- validation strategy
- domain adapters
- registry entries

Low-frequency review:

- stable user preferences
- core operating philosophy
- durable decision records
- frozen contracts

## Event-triggered invalidation

When an invalidation trigger fires, do not automatically rewrite memory. Instead:

1. identify affected entries;
2. classify the conflict;
3. update lifecycle status;
4. preserve provenance;
5. route technical claims through `protocols/VERIFICATION_PROTOCOL.md`;
6. route authority changes through `protocols/INSTRUCTION_TRUST_POLICY.md`.

## Current or unstable knowledge

For unstable knowledge, store freshness metadata or avoid promotion.

```yaml
freshness_risk: high
review_trigger: before reuse in technical decision
lifecycle_status: candidate
verification_status: not_checked
```

## Do not over-automate yet

This protocol defines review behavior only. Do not add automatic decay cron, crawler, vector database, external monitoring, or automatic memory promotion until the repository has explicit scope for that automation.
