# Raw Ideas

Purpose: capture raw ideas before they are lost.

Use this directory for:

- sudden user thoughts;
- brainstorming fragments;
- early repo-shaping ideas;
- model-captured idea records extracted from two or more conversation turns;
- possible future workflows, protocols, registries, adapters, prompts, or tools.

## Command entry point

The command-style entry point for this area is:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
ایده خام
```

Expected first response:

```text
آماده‌ام. ایده خامت چیه؟
```

This command can be used for any domain. The model should capture the raw idea first, then route the domain or maturation task only after the core idea is preserved.

## Core rule

Preserve the core idea first. Do not over-polish, over-formalize, validate, or convert it into accepted memory during capture.

## Storage pattern

- `INBOX.md` is for very quick capture.
- `captured/` is for standalone model-captured idea records.
- `_model_capture_template.md` defines the preferred shape for a captured raw idea.

## Status boundary

A raw idea is not:

- accepted memory;
- project policy;
- a protocol;
- a verified claim;
- an implementation commitment;
- a final architecture;
- technical evidence.

Raw ideas may later enter `protocols/IDEA_MATURATION_PIPELINE.md`.

## Model behavior

When a conversation produces a reusable raw idea, the model may propose or create a raw idea record here if the active task allows repository writes.

If repository-write scope is unavailable, the model should provide a ready-to-save raw idea record instead of claiming it wrote to the repository.

The model must distinguish:

- the user's core idea;
- the model's interpretation;
- unknowns and risks;
- possible future shape.

The model must not silently promote a captured raw idea into accepted memory or protocol content.

## Capture priority

Order of priority during raw capture:

1. Preserve the core idea.
2. Preserve the user's raw intent.
3. Record the conversation context.
4. Mark boundaries and unknowns.
5. Suggest possible future development.
6. Stop before validation or implementation unless the user asks for the next stage.
