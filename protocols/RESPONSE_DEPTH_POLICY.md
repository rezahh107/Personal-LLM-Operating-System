# Response Depth Policy

Purpose: choose how much reasoning, evidence, and structure a response needs.

## Depth levels

### quick

Use for:

- simple clarifications
- direct explanations
- short comparisons
- small wording help
- obvious next actions

Do not use for:

- repository changes
- high-risk claims
- current-source claims
- strategic architecture decisions

Evidence behavior:

- no formal evidence required unless the answer depends on current or technical facts

External verification:

- use current sources when the fact is unstable

Idea maturation:

- not required

### standard

Use for:

- normal technical explanations
- prompt generation
- moderate repository guidance
- practical checklists
- non-critical planning

Do not use for:

- major architecture changes
- disputed technical claims
- PR merge decisions
- reusable policy creation

Evidence behavior:

- cite or name relevant repository/current evidence when available
- mark assumptions

External verification:

- use current sources for unstable facts

Idea maturation:

- optional when the topic may become reusable

### deep

Use for:

- repository audit
- PR readiness
- architecture design
- validator/schema changes
- security-sensitive reasoning
- multi-file document design
- claims that may affect downstream models

Do not use for:

- casual questions
- simple edits
- boot-only mode

Evidence behavior:

- inspect relevant source files, current state, tools, validators, or external sources
- separate confirmed facts from candidate conclusions

External verification:

- required when the answer depends on current external state

Idea maturation:

- required if the topic is new, strategic, or repository-shaping

### maturation

Use for:

- turning a rough idea into a durable protocol
- designing a new repository layer
- creating a repeatable model workflow
- deciding whether new knowledge should become memory
- resolving competing frameworks or concepts

Do not use for:

- quick explanations
- small operational fixes
- already-scoped implementation tasks

Evidence behavior:

- challenge assumptions
- compare alternatives
- identify candidate, accepted, rejected, and quarantined claims
- preserve open questions

External verification:

- use current sources when the idea depends on recent practice, tools, standards, or ecosystem behavior

Idea maturation:

- required; follow `protocols/IDEA_MATURATION_PIPELINE.md`

## Default selection rule

When unsure:

- choose `quick` for simple understanding
- choose `standard` for normal useful work
- choose `deep` for technical verification or repository work
- choose `maturation` for new systems, policies, or long-term memory

Do not use depth as a way to create unnecessary friction. Use the smallest depth that protects correctness and usefulness.
