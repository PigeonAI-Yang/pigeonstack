> Codex adapter: This is the upstream guide with local host adaptations. Apply [../../CODEX.md](../../CODEX.md) for installation, GPT routing, permissions, and supported tools. Cursor Custom Modes, cloud agents, Projects, and `/loop` are reference examples, not configured Codex capabilities.

# Set up pstack

In this page you install the plugin, pick which models pstack uses, and run your first task. Setup is one command plus a short conversation.

## Install the plugin

For Codex installation, follow [CODEX.md](../../CODEX.md). Source edits, deployment, installed files, and behavior in a new session are separate outcomes. The upstream Cursor installation command is:

```text
/add-plugin pstack
```

Cursor confirms the plugin is installed.

## Pick your models on Codex

Run `/setup-pstack` to inspect the existing GPT role mapping in [MODELS.md](../../MODELS.md). Setup changes only requested roles and efforts in the maintained source. It preserves the active Primary and never restores upstream Grok or Claude defaults. Model IDs and reasoning efforts are separate host arguments.

`auto` and `inherit-parent` resolve to the actual active parent's model and effort. Omitting a model can select the configured Luna child default on this host; it does not prove inheritance. `MODELS.md` defines supported resolution and missing-evidence behavior.

Source changes and deployment are separate. Follow [CODEX.md](../../CODEX.md) for installation and report routing verified in a new session separately.

## Accept the verification offer, or don't

At the end of setup, `/setup-pstack` looks for a way to prove app behavior in your project, either a `verify-*` skill or an existing harness. If it finds neither, it offers once to generate one with [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md).

Say yes and it writes `.agents/skills/verify-<app>/`, a project-local skill that teaches agents to drive your app the way a user does. It proves the skill works once before handing it over. Say no and setup moves on. You can run `/create-verification-skill` yourself any time. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers it in depth.

A reusable verification skill helps when existing commands and app entry points cannot prove the requested result. Reuse those capabilities first. A missing skill alone does not require a new harness, feature map, or setup gate.

After an authorized model configuration deployment, verify routing in a new chat. A source edit alone does not change the active model.

## Keep the cost in check

Extra agents and selected review panels use more tokens. On Codex, preserve the responsibilities and efforts in [MODELS.md](../../MODELS.md).

- Use Luna for specified execution and evidence collection, and reuse credible current evidence.
- Avoid redundant reviewers and panels that the task did not select.
- Request any model or effort change explicitly through `/setup-pstack`; a generic budget preset does not override the GPT mapping.
- Resolve `auto` and `inherit-parent` to the actual parent model and effort. Omitting model arguments can select Luna instead.
- Casual conversation and direct factual answers need no workflow.

## Run your first task

Pick something real but small, and describe it the way you'd describe it to a colleague:

```text
/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

For this prompt, `/poteto-mode` follows the Feature playbook. On Codex, follow applicable phases and evidence in the existing authoritative task record. Material skips or adaptations include a reason. The agent does not copy the playbook into another record, and a simple task needs no new ledger.

From here you can type normal follow-ups. On Codex, `CODEX.md` and the active global instructions govern activation; no Custom Mode shortcut is configured. In Cursor, to keep `/poteto-mode` on for the whole chat, pick it from the `/` menu with Option+Enter (Mac) or Alt+Enter (Windows) instead of Enter. That makes it a [Custom Mode](https://cursor.com/docs/skills), which stays in context on every turn until you exit it. Custom Modes are available in the Agents Window and the CLI. Plain Enter attaches the skill to one message, and it fades as the chat moves on.

Next: [Route work through `/poteto-mode`](./02-poteto-mode.md).
