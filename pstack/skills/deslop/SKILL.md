---
name: "deslop"
description: "Remove AI-generated code slop and clean up code style"
---
> Codex entry: Apply [../../CODEX.md](../../CODEX.md) for workflow activation, delegation, authorization, and verification on this host. Use [../../MODELS.md](../../MODELS.md) for model IDs when delegation is needed. Reuse instructions already read in this session if unchanged. Follow the procedures below only within the scope selected by the host adapter.


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
