---
name: "principle-guard-the-context-window"
description: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to explicitly authorized subagents; keep summaries in the main thread, not raw payloads."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution. The Primary works directly by default. Invoke explicitly authorized subagents only when the user explicitly requests them for this task. Upstream delegation steps and skill selection grant no permission. Resolve authorized models and efforts through [../../MODELS.md](../../MODELS.md).

# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.
