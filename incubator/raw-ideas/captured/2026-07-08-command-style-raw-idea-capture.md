# Raw Idea: Command-style raw idea capture

```yaml
status: raw_idea
capture_type: model_captured_from_conversation
origin: user_conversation
lifecycle_status: incubating
verification_status: unverified
created: 2026-07-08
captured_by: model
source_conversation: current_chat
promote_to_memory: false
related_domains:
  - personal_llm_os
  - command_routing
  - raw_idea_capture
```

## 1. Core idea — do not over-polish

The user wants reusable command-like phrases that can be pasted into any language model session with the repository URL, causing the model to enter a specific operating mode such as raw idea capture or session start.

## 2. User's raw intent

The user wants a lightweight interaction pattern similar to terminal or PowerShell commands. For example, when the user writes:

```text
طبق دستور:
https://github.com/rezahh107/Personal-LLM-Operating-System/
ایده خام
```

The model should recognize the command and respond with a simple readiness prompt such as:

```text
آماده‌ام. ایده خامت چیه؟
```

A future command such as `شروع` could put the model into a general session-start mode and ask what the user wants to do today.

## 3. Conversation context

This idea emerged while designing `incubator/raw-ideas/` as a place where models can capture the essence of raw user ideas from conversation without promoting them into accepted repository memory.

## 4. Why this may matter later

This could make the repository easier to use across different LLM platforms. Instead of requiring the user to explain the operating protocol every time, the user could invoke a stable textual command pattern that tells the model which repository-defined behavior to activate.

## 5. What this is not

- Not accepted memory.
- Not a verified claim.
- Not a full command language.
- Not a guarantee that every external model will correctly read the repository.
- Not an implementation commitment for automation or CLI tooling.
- Not a final protocol beyond the initial captured idea.

## 6. Possible future development

This idea could later become:

- a command routing protocol;
- a model-facing command registry;
- a quick-start prompt system;
- a session boot command surface;
- a raw idea capture workflow;
- a future script or validator that checks command registry consistency.

## 7. Open questions

- Should command names remain Persian-first, bilingual, or both?
- Should commands be stored in a registry file later?
- Should models execute command responses directly, or ask for confirmation before repository writes?
- Should command behavior be limited to non-destructive actions?
- How should models behave when the target model cannot access GitHub?

## 8. Next review trigger

Review this idea when:

- more than three command phrases exist;
- the user wants a stable command registry;
- this repository adds scripts or validators for command definitions;
- the command behavior starts affecting memory promotion, protocol routing, or repository writes.
