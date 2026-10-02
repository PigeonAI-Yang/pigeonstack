---
name: "principle-redesign-from-first-principles"
description: "Apply when integrating a new requirement into an existing design. Redesign as if the requirement had been a foundational assumption from day one, instead of bolting it on."
---
> Codex entry: Apply [../../CODEX.md](../../CODEX.md) for workflow activation, delegation, authorization, and verification on this host. Use [../../MODELS.md](../../MODELS.md) for model IDs when delegation is needed. Reuse instructions already read in this session if unchanged. Follow the procedures below only within the scope selected by the host adapter.


# Redesign From First Principles

When integrating a change, don't bolt it onto the existing design. Redesign as if the requirement had been there from the start.

- Read all affected files and understand the current design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the whole redesign, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.
