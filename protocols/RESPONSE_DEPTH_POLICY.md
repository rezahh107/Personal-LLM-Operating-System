# Response Depth Policy

Purpose: choose how much reasoning, evidence, and structure a response needs.

## Depth levels

### command-first

Use for:

- recognized command-style invocations;
- `شروع` command;
- `ایده خام` command;
- repository-wide command routing before a domain task is known.

Do not use for:

- full repository explanation unless asked;
- domain audit;
- technical verification;
- implementation work;
- memory promotion.

Evidence behavior:

- command itself is a routing hint, not evidence;
- no technical evidence required for the first command response;
- after the user provides the actual task, reroute and select the appropriate depth.

Expected behavior:

- `شروع` → `آماده‌ام. امروز می‌خوای چکار کنی؟`
- `ایده خام` → `آماده‌ام. ایده خامت چیه؟`

### quick

Use for:

- simple clarifications
- direct explanations
- short comparisons
- small wording help
- obvious next actions
- initial raw idea intake after the command response

Do not use for:

- repository changes
- high-risk claims
- current-source claims
- strategic architecture decisions
- promoting raw ideas into memory

Evidence behavior:

- no formal evidence required unless the answer depends on current or technical facts

External verification:

- use current sources when the fact is unstable

Idea maturation:

- not required

Raw idea behavior:

- preserve the core idea first;
- do not critique or mature unless asked.

### standard

Use for:

- normal technical explanations
- prompt generation
- moderate repository guidance
- practical checklists
- non-critical planning
- explaining command usage or raw idea capture

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
- adding or changing command protocol behavior
- changing raw idea capture boundaries

Do not use for:

- casual questions
- simple edits
- boot-only mode
- command-first response

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
- promoting a raw idea beyond `incubator/raw-ideas/`

Do not use for:

- quick explanations
- small operational fixes
- already-scoped implementation tasks
- preserving the initial raw idea before it has been captured

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

- choose `command-first` for recognized command-style prompts
- choose `quick` for simple understanding
- choose `standard` for normal useful work
- choose `deep` for technical verification or repository work
- choose `maturation` for new systems, policies, or long-term memory

Do not use depth as a way to create unnecessary friction. Use the smallest depth that protects correctness and usefulness.
