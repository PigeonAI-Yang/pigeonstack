---
name: "setup-pstack"
description: "Configure which models pstack uses per role. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, \"configure pstack models\", or changing pstack's model choices."
---
> Codex entry: Apply [../../CODEX.md](../../CODEX.md) for workflow activation, delegation, authorization, and verification on this host. Use [../../MODELS.md](../../MODELS.md) for model IDs when delegation is needed. Reuse instructions already read in this session if unchanged. Follow the procedures below only within the scope selected by the host adapter.


# Setup pstack

In Codex, use the plugin-root [MODELS.md](../../MODELS.md) as the source of truth for pstack's model per role. Do not write a Cursor rule. Preserve choices already authorized in the current task; do not ask for the same confirmation again. Follow CODEX.md for unavailable targets: document them separately and stage an inactive profile while preserving working defaults. The availability checks below govern active selections, not explicitly requested pending targets. Retain the host's Primary, execution, and advisor roles rather than copying the upstream panel mapping.

## Steps

### 1. Detect available models

Enumerate the model slugs you can pass to a `Task` subagent in this session. That is the dependable source. If Cursor also exposes a models API or CLI that lists the user's entitled models, prefer it for completeness. If you cannot detect any, ask the user to paste the slugs they have access to. Never write a real slug you have not confirmed is available. The aliases `inherit-parent` and `auto` are always valid even though they are not detected slugs.

### 2. Load current state

The default role-to-model mapping is the shape shown in step 5 below. If [MODELS.md](../../MODELS.md) already exists, read it and treat its values as the current choices. Otherwise start from those defaults.

### 3. Map and confirm

Show every role with its current model, marking any real slug not in the detected set as needing a choice. Ask whether to accept as-is or change specific roles, offering the detected models plus `inherit-parent` and `auto` (both mean: this role runs on the parent chat model, which is how Auto users stay on Auto) as the options. Prefer AskQuestion over free text. For panel roles (arena runners, architect runners, interrogate reviewers) the value is a list, and one subagent runs per entry, alias entries included, so the list length sets the count. `arena cross-judge pool` is also a list, but Arena selects one value from it whose model family differs from the parent's when possible. `swarm workers` is the default model for every worker unless a race or comparison assigns another model per arm.

### 4. Validate

Every real slug written must be in the detected set. `inherit-parent` and `auto` always pass. If a chosen real slug is not available, stop and ask again.

### 5. Write the rule

In Codex, update [MODELS.md](../../MODELS.md) with one line per role, using the same labels poteto-mode uses. Keep the host's CODEX/MODELS contract and do not create a Cursor rule. Shape:

```
---
description: pstack per-role model choices (overrides skill defaults)
alwaysApply: true
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
feature, refactoring: grok-4.6-fast-xhigh
bug-fix: claude-fable-5-1-thinking-max
perf-issue: claude-fable-5-1-thinking-max
hillclimb: claude-fable-5-1-thinking-max
judgment and prose: claude-fable-5-1-thinking-max
hardest tasks: claude-fable-5-1-thinking-max
how explorer: grok-4.6-fast-xhigh
how explainer: claude-fable-5-1-thinking-max
why investigators: grok-4.6-fast-xhigh
why synthesizer: claude-fable-5-1-thinking-max
reflect tooling: gpt-5.6-sol-max
reflect judgment, divergent, synthesizer: claude-fable-5-1-thinking-max
arena runners: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
arena cross-judge pool: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
swarm workers: grok-4.6-fast-xhigh
architect runners: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
interrogate reviewers: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
```

### 6. Confirm

Tell the user the Codex model mapping was updated and applies to new sessions. Re-running this skill updates it.

### 7. Offer a verification skill (optional)

Check whether the project has a way to drive the real app for proof (a `verify-*` skill, or an existing harness). If not, offer once: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work? I can generate one with /create-verification-skill." On yes, invoke `/create-verification-skill` (resolves wherever pstack is installed: workspace, user, or plugin). On no, move on without pushing.
