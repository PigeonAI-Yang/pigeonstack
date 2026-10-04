---
name: "setup-pstack"
description: "Configure the existing GPT model and effort mapping for pstack on Codex. Use for /setup-pstack or requested model changes. Preserve role responsibilities and the active Primary."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution and [../../MODELS.md](../../MODELS.md) before assigning roles. Apply the upstream procedure below within that host contract.

# Setup pstack

Configure the source `MODELS.md` for this Codex host. That file is the only role-to-model source. Read its current mapping and `CODEX.md` before proposing changes.

## 1. Detect available models

Inspect the session's supported model IDs, efforts, and spawn arguments. Use actual configuration and successful requests as evidence. Do not infer server routing from a model's self-description. Stop affected requests after an access denial, authentication challenge, or rate limit. Report unavailable required values without choosing a substitute.

## 2. Load current state

Read source `MODELS.md` and the active host configuration. Preserve the active Primary, explicit user choices, responsibility splits, and takeover cap. Upstream role labels map to responsibilities in `MODELS.md`; do not import Cursor defaults or delete local policy because a label changed upstream.

## 3. Propose the requested choices

Show affected roles with their actual model IDs and separate reasoning efforts. Change only the roles and efforts the user requested. Generic budget presets do not rewrite this user's GPT configuration. Explain any unavailable target and retain working defaults. Use `auto` or `inherit-parent` only when the actual parent's model and effort can be resolved and preserved through supported host arguments.

If the request leaves a material model preference undecided, ask for that preference. Existing explicit choices need no repeated confirmation. A panel configuration describes potential seats; execution still requires selection and scope under `CODEX.md`.

## 4. Validate

Verify each requested model and effort against available host evidence. An alias is not automatically valid: confirm how it resolves both parent values. Missing access blocks activation, not local documentation of an explicitly requested inactive target. Never fabricate a catalog entry or start a fallback model.

## 5. Write the source configuration

Apply authorized choices to source `MODELS.md`. If the requested change also requires host configuration, update the maintained source configuration within scope and preserve unrelated settings. Do not create a Cursor rule, another routing file, or a new routing engine. Runtime mirrors and caches are deployment outputs, and deployment requires separate authorization.

## 6. Report the result

State changed roles, verified availability, and unresolved limits. Distinguish source files from installed artifacts and from routing observed in a new session. Do not claim activation merely because a source file changed.

## 7. Offer verification only when needed

Check for an existing way to drive the real app. If the current task needs reusable verification and none exists, offer `/create-verification-skill` once. Do not make it a setup prerequisite.
