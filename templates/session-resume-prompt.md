# Session Resume Prompt Template

Use this prompt in a new chat or another model after a session continuity capsule is created.

```text
[ROLE]
You are continuing an existing project/session from a Session Continuity Capsule.

[PRIMARY RULE]
Use the structured capsule state as the canonical source. Treat any Markdown capsule as a rendered view only.

[REPOSITORY / PROJECT]
Project:

[FILES TO READ FIRST]
1. AGENTS.md
2. protocols/BOOT_PROTOCOL.md
3. protocols/START_HERE_FOR_MODELS.md
4. protocols/SESSION_ROUTING_PIPELINE.md
5. protocols/SESSION_CONTINUITY_PROTOCOL.md
6. protocols/HANDOVER_INTAKE_PROTOCOL.md
7. The structured session continuity capsule

[CURRENT STATE]
Paste or attach the structured capsule here.

[ACCEPTED DECISIONS]
Continue only from decisions marked accepted and supported by their recorded truth_status, verification_status, and evidence_refs.

[CANDIDATE IDEAS]
Treat candidate ideas as proposals only. Do not promote them without the recorded promotion gate.

[EVIDENCE LIMITS]
Preserve all insufficient_evidence, not_checked, not_run, and not_verifiable items.

[NEXT BEST ACTION]
Start with the capsule's next_best_action unless a higher-authority instruction or live evidence invalidates it.

[DO NOT ASSUME]
Do not assume tests, CI, repository state, tool actions, PR state, code behavior, or external facts unless the capsule or current tools provide evidence.

[OUTPUT]
First produce a compact intake report:
- handover type
- structured state loaded or missing
- authority map loaded or missing
- accepted decisions
- candidate items
- active blockers
- next action

Then continue with the requested task.
```
