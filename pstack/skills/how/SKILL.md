---
name: "how"
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution and [../../MODELS.md](../../MODELS.md) before assigning roles. Apply the upstream procedure below within that host contract.

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Resolve each named role through the plugin-root `MODELS.md`. It defines responsibility splits, GPT models and efforts, parent aliases, and required-model failures. Do not substitute upstream defaults or create a repair PR when routing is unavailable.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. The Primary uses the direct explanation procedure, with prescribed evidence collection if needed. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): assign parallel prescribed evidence collection first, then synthesize through the role mapping. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Spawn all explorers in a single message:

- `subagent_type`: `generalPurpose`
- `model`: the `how explorer` line, resolved through `MODELS.md`
- `readonly`: `true`

Use `references/explorer-prompt.md` to frame the needed evidence. Before assigning Luna, turn each angle into named searches or observations. Keep unresolved interpretation with the Primary or a bounded read-only Astra investigation. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

The Primary follows the direct explanation procedure. An authoritative architecture document uses Astra; a bounded unresolved question may use the read-only investigation route in `MODELS.md`.

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once collection is complete, the Primary synthesizes the evidence. Route an authoritative document to Astra under `MODELS.md`.

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in.

## Step 4. Present

Present the accepted explanation with its evidence and gaps. The Primary owns final acceptance and the user-facing answer.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
