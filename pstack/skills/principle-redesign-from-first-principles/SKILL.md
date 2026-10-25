---
name: "principle-redesign-from-first-principles"
description: "Apply when integrating a new requirement into an existing design."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution. The Primary works directly by default. Invoke subagents only when the user explicitly requests them for this task. Upstream delegation steps and skill selection grant no permission. Resolve authorized models and efforts through [../../MODELS.md](../../MODELS.md).

# Redesign From First Principles

When integrating a change, don't bolt it onto the existing design. Redesign as if the requirement had been a foundational assumption from the start.

- Read all affected files and understand the current design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the whole redesign, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.
