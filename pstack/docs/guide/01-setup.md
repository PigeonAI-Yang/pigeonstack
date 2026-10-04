> Codex adapter: This is the upstream guide. Apply [../../CODEX.md](../../CODEX.md) for installation, GPT routing, permissions, and supported host tools. Cursor-specific commands are reference examples.

# Set up pstack

In this page you install the plugin, pick which models pstack uses, and run your first task. Setup is one command plus a short conversation.

## Install the plugin

In a Cursor chat, run:

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

Say yes and it writes `.agents/skills/verify-<app>/`, a project-local skill that teaches agents to drive your app the way a user does. It proves the skill works once before handing it over. Say no and setup moves on. You can run `/create-verification-skill` yourself any time. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers when it earns its place.

After setup, start a new chat. The model rule applies to new sessions.

## Run your first task

Pick something real but small, and describe it the way you'd describe it to a colleague:

```text
/poteto-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

Watch the todo list. Its first items are the matched playbook's steps copied in, the Feature playbook for this prompt. If `/poteto-mode` skips a step, the step stays in the list with `skip: <reason>`, so you can see what it chose not to do.

From here you can type normal follow-ups. `/poteto-mode` is sticky. It stays on for the conversation until you opt out by saying so.

Next: [Route work through `/poteto-mode`](./02-poteto-mode.md).
