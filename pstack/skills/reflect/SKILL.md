---
name: "reflect"
description: "Review the active conversation for durable learnings and route each to a concrete skill edit. Independent review agents require an explicit user request. Use when the user says reflect."
---
> Codex host: Follow [CODEX.md](../../CODEX.md) for applicability, permissions, and supported tools. Read only the references needed for the current action.

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Use CODEX.md's targeted history route for the active conversation. Do not scan unrelated chats or assume a Cursor transcript schema. If a supported transcript cannot be located, use a concise digest of this session.

## 2. Review the three lenses

The Primary reviews judgment, tooling, and divergent findings directly. Use the templates in `references/judgment-reviewer.md`, `references/tooling-reviewer.md`, and `references/divergent-reviewer.md`. Collect only evidence from the current conversation. Use CODEX.md's history route or a concise session digest, rather than assuming Cursor transcript paths.

If the user explicitly requests independent reviewers, assign those read-only scopes through `MODELS.md`. Use supported host tools and the authorized assignment count. Access to MCPs does not authorize edits or messages.

## 3. Synthesize

The Primary combines the findings with `references/synthesizer.md` into an Accepted / Rejected / Backlog list and spot-verifies citations. Do not create a separate synthesizer by default.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

File Backlog items to an external tracker only when that action is authorized. Otherwise report them locally.

Never edit a deployed mirror or plugin cache. Show the maintained source destination before approval. For this adapter, edit `J:/PigeonYang/pigeonstack` and follow CODEX.md for separately authorized deployment. An external skill is copied into the user-requested source location only when that is part of the approved change.

For each approved row, preserve its target skill and apply the Codex `skill-creator` procedure. The Primary makes the edit directly by default. Any explicitly authorized delegation follows `MODELS.md`. Existing authorization covers its stated scope without repeated per-edit approvals. Do not open a PR or push without authorization.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
