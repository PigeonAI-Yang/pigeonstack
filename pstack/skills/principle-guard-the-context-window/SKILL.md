---
name: "principle-guard-the-context-window"
description: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to explicitly authorized subagents; keep summaries in the main thread, not raw payloads."
---
> Codex host: Follow [CODEX.md](../../CODEX.md) for applicability, permissions, and supported tools. Read only the references needed for the current action.

# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.
