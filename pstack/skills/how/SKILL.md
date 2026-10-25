---
name: "how"
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution. The Primary works directly by default. Invoke subagents only when the user explicitly requests them for this task. Upstream delegation steps and skill selection grant no permission. Resolve authorized models and efforts through [../../MODELS.md](../../MODELS.md).

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

The Primary investigates and explains directly by default. An explicit user request may authorize scoped read-only explorers. Resolve their roles, models, and efforts through `MODELS.md` and supported tool arguments through `CODEX.md`.

## 1. Assess complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. The Primary explores and explains in one pass, built from `references/explainer-prompt.md` without the explorer-findings section. Go to step 4.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): go to step 2.

When in doubt, take the simple path.

## 2. Explore (complex only)

Decompose the question into 2 to 4 angles, each a distinct slice of the subsystem. The Primary collects the evidence for each angle. If the user explicitly requested parallel explorers, give each authorized explorer `references/explorer-prompt.md` with its angle filled in.

## 3. Synthesize (complex only)

The Primary synthesizes the collected evidence using `references/explainer-prompt.md`. Include any authorized explorer findings. A separate explainer is optional only within explicit user authorization.

## 4. Present

Present the supported explanation, its evidence, and its gaps. The Primary owns synthesis and final acceptance.

## Output format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
