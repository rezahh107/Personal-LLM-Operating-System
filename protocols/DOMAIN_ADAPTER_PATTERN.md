# Domain Adapter Pattern

Each repeated work domain should define a domain adapter that inherits the parent protocol.

Example domains:

- audit / post-merge scanning
- GitHub repair
- prompt engineering
- image workflow
- code review
- research
- document generation

Each adapter should define:

```text
domain goal
allowed model roles
domain-specific claim types
required evidence
banned claims
output schema
handoff schema
eval fixtures
promotion rules
quarantine rules
```

Domain adapters must not duplicate parent rules unless they intentionally narrow them.
