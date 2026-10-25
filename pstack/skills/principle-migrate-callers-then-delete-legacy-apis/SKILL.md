---
name: "principle-migrate-callers-then-delete-legacy-apis"
description: "Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers."
---
> Codex host: Follow [CODEX.md](../../CODEX.md) for applicability, permissions, and supported tools. Read only the references needed for the current action.

# Migrate Callers Then Delete Legacy APIs

- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative
