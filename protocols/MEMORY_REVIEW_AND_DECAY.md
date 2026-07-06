# Memory Review and Decay

Purpose: define how repository memory becomes stale, gets reviewed, gets deprecated, or is superseded.

## Review status categories

Use these review statuses:

- `current`
- `review_needed`
- `stale_candidate`
- `superseded`
- `deprecated`
- `quarantined`
- `rejected`

## Review triggers

Review memory when:

- the user says it is outdated
- current external evidence conflicts with it
- a tool, API, dependency, law, product, or standard changed
- a repository role changed
- a workflow repeatedly fails
- a better protocol replaced it
- a downstream model misused it
- the memory lacks source, scope, or freshness notes

## Stale memory handling

When memory may be stale:

1. Do not delete it immediately.
2. Mark it as review-needed or stale candidate.
3. Use current evidence for the immediate task when appropriate.
4. Recommend a scoped review.
5. Preserve what changed and why.

## Superseded memory handling

When a newer rule replaces an older rule:

1. Mark the older item as superseded or deprecated.
2. Point to the replacement.
3. Keep historical context only if useful.
4. Do not leave two active rules that conflict.

## Domain-specific review frequency

Different memory decays at different speeds.

High-frequency review:

- software versions
- CI behavior
- APIs
- package security
- product features
- public standards

Medium-frequency review:

- repository workflows
- prompt patterns
- validation strategy
- domain adapters

Low-frequency review:

- stable user preferences
- core operating philosophy
- durable decision records

## Current or unstable knowledge

For unstable knowledge, store freshness metadata or avoid promotion.

A useful pattern is:

```yaml
freshness_risk: high
review_trigger: before reuse in technical decision
status: candidate
```

## Do not over-automate yet

This protocol defines review behavior only.

Do not add automatic decay cron, crawler, vector database, or external monitoring until the repository has a mature review model and explicit scope for automation.
