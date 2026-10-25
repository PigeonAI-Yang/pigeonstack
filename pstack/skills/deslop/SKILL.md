---
name: "deslop"
description: "Remove AI-generated code slop and clean up code style"
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution. The Primary works directly by default. Invoke subagents only when the user explicitly requests them for this task. Upstream delegation steps and skill selection grant no permission. Resolve authorized models and efforts through [../../MODELS.md](../../MODELS.md).

# Remove AI code slop

Check the diff against main and remove AI-generated slop introduced in the branch.

## Focus Areas

- Extra comments that are unnecessary or inconsistent with local style
- Defensive checks or try/catch blocks that are abnormal for trusted code paths
- Casts to `any` used only to bypass type issues
- Deeply nested code that should be simplified with early returns
- Other patterns inconsistent with the file and surrounding codebase

## Guardrails

- Keep behavior unchanged unless fixing a clear bug.
- Prefer minimal, focused edits over broad rewrites.
- Keep the final summary concise (1-3 sentences).
