---
name: "poteto-help"
description: "Answer explicitly requested pstack usage questions about setup, skills, playbooks, principles, and prompts. Use when the user invokes poteto-help."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution and [../../MODELS.md](../../MODELS.md) before explaining or assigning roles. Apply the upstream help procedure below within that host contract.

# Poteto help

Answer the user's question about pstack, hand them a prompt they can send, and link the file the answer came from. For a help question, don't start the work. The user asked how, and a pstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use pstack to fix this bug", is an execution request. Read [`poteto-mode`](../poteto-mode/SKILL.md) and do the authorized work under [CODEX.md](../../CODEX.md). A proposed example prompt is not permission to execute it. This help skill is explicit-only through `agents/openai.yaml`.

This file maps questions to the skills and guide pages that hold the answers. Read the file you route to before quoting or recommending it. Its current procedure and the host contract take precedence over this map. Link the local adapted file with an absolute path when it is accessible. For upstream context, use `https://github.com/cursor/plugins/blob/77526ffa67f8dafc698d14b5356e6d4fc78c3127/pstack/` followed by the upstream path. `UPSTREAM-README.md` maps to upstream `README.md`. Label upstream links as Cursor documentation; they do not establish the local GPT or tool configuration.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. For a bare or ambiguous invocation, ask one short optional clarification using a supported host input tool when available, or in the final reply. The following are routing categories, not a required tool payload. Choose at most the number of options the actual tool schema permits. If no answer arrives, give a concise orientation without starting work.

- Get set up
- Start a task with `/poteto-mode`
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

Check the state that changes the answer, and mention it only when it does:

- For a model question, read [MODELS.md](../../MODELS.md). Inspect actual host configuration only when the answer depends on it. A missing Cursor rule says nothing about Codex setup, and disk configuration does not prove live routing.
- For a verification question, inspect the existing app entry points, checks, and any `verify-*` skill. Missing a skill alone does not mean the app cannot be driven. Recommend `/create-verification-skill` only for a current need or observed gap.

## Get set up

1. Explain the maintained source and authorized installation procedure in [CODEX.md](../../CODEX.md). `/add-plugin pstack` and Customize are upstream Cursor examples.
2. Explain [`/setup-pstack`](../setup-pstack/SKILL.md). It reads the GPT role mapping in [MODELS.md](../../MODELS.md) and changes only user-requested models or efforts in source. Deployment and new-session routing are separate.
3. Start a real task with `/poteto-mode`, a goal, and a check that can pass or fail.

Installing the plugin does not run its playbooks or enable its dormant automations. Skill discovery and the global substantive-work rule still apply on Codex. The [upstream README](../../UPSTREAM-README.md) and [guide page 1](../../docs/guide/01-setup.md) have the details. Help word the first prompt when requested, per [`references/prompting.md`](references/prompting.md).

If cost is the worry, explain that extra agents and selected review panels use more tokens. Preserve the GPT responsibilities and efforts in `MODELS.md`; generic budget presets do not override them. Luna executes a concrete brief or applies exact accepted content. Sol handles ordinary technical plans, local designs, routine rule adaptation, and ordinary unresolved questions. Astra is reserved for critical design decisions, problems unresolved after an actual Sol `xhigh` attempt, or explicit user model selection. A technical-document label alone does not justify Astra. Avoid redundant panels and repeated evidence collection. A user may request model changes through `/setup-pstack`. `auto` and `inherit-parent` require the actual parent model and effort to be resolved and passed through supported host arguments. Omitted model arguments can select Luna and do not prove inheritance or savings.

pstack originated in Cursor. This adapter translates delegation through `collaboration.spawn_agent` and GPT roles through `MODELS.md`. Cursor Custom Modes, cloud VMs, and `/loop` have no configured equivalent here. Explain that limitation instead of claiming that a Cursor command is installed.

## Start a task with `/poteto-mode`

`/poteto-mode` matches the task to a playbook, follows its phases, and runs the other skills as needed. On Codex, track applicable phases and evidence in the existing authoritative task record. Record material skips or adaptations with a reason. Do not copy the playbook into another record, and do not create a ledger for a simple task. A good prompt states the goal and how to tell it's done. It doesn't list skills, because a hand-written sequence tends to drop or reorder steps the playbook would keep. Read [`references/prompting.md`](references/prompting.md) before you help word one. [Guide page 2](../../docs/guide/02-poteto-mode.md) has examples.

In Cursor, upstream persistence depends on how the user starts `/poteto-mode`:

- Enter on `/poteto-mode` attaches the skill to one message. It fades as the chat moves on.
- Option+Enter on Mac or Alt+Enter on Windows, or Use as Mode from the skill entry, makes it a Custom Mode. It stays in context every turn until the user exits the mode, and it stays out of casual turns.
- Cursor's docs list Custom Modes in the Agents Window and the CLI. Elsewhere, start each new task with `/poteto-mode`.

Link [Cursor's skills docs](https://cursor.com/docs/skills) for those Cursor controls. On Codex, follow the substantive-work activation in `CODEX.md`, reuse unchanged instructions already read, and honor an explicit opt-out. Do not claim persistent UI state or guaranteed reinjection. Mid-chat, "new task" selects a fresh playbook. Internal assignments use `collaboration.spawn_agent` with supported arguments and the responsibilities in `MODELS.md`; Cursor's `subagent_type` is not a Codex argument.

## Pick a skill

The default answer is `/poteto-mode`, which runs most of the others when its steps need them. Name a skill directly when the user wants more or less of something than the playbook gives. Read the skill before you recommend it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`/poteto-mode`](../poteto-mode/SKILL.md) |
| Know how code works now, or where new code should live | [`/how`](../how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`/why`](../why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`/teach`](../teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`/recall`](../recall/SKILL.md) |
| Know what a small diff could break outside itself | [`/blast-radius`](../blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`/architect`](../architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`/arena`](../arena/SKILL.md) |
| Run scoped parallel checks over independent slices, or an explicitly selected race | [`/swarm`](../swarm/SKILL.md) |
| Explicitly request independent review of a diff | [`/interrogate`](../interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`/tdd`](../tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`/typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| Strip comments before review, using a reviewer that didn't write them | [`/no-comments`](../no-comments/SKILL.md) |
| Clean AI tells out of prose | [`/unslop`](../unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`/technical-writing`](../technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`/bro`](../bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`/create-verification-skill`](../create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`/maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`/benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`/figure-it-out`](../figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`/show-me-your-work`](../show-me-your-work/SKILL.md) |
| Request GPT model or effort changes within the local role mapping | [`/setup-pstack`](../setup-pstack/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`/automate-me`](../automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`/reflect`](../reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`/correct`](../correct/SKILL.md) |
| Build a page whose buttons wake a Grok Bot over a webhook | [`/make-bot-ui`](../make-bot-ui/SKILL.md) |
| Find their way around pstack | `/poteto-help` |

If a skill directory next to this one is missing from the table, read its frontmatter and route by its description. The `principle-*` directories are covered under principles below.

Close calls:

- `/how` explains what the code does. `/why` explains the reasons. `/teach` runs one or both and explains the result plainly.
- `/arena` gives every worker the same brief and merges the best parts. `/swarm` splits work into slices or a race and returns one report.
- `/architect` proceeds to authorized implementation after the design. Add "with checkpoint" to review it first. Ordinary local design uses Sol; critical architecture, key contracts, and consequential design tradeoffs use Astra. Luna implements an accepted design.
- `/interrogate` reviews the diff. `/blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `/recall` rebuilds context across recent chats. Resuming one specific chat or branch is the Session pickup playbook.
- `/figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

Bundled tools and host limits:

- `/deslop`, `control-cli`, and `control-ui` originate in `cursor-team-kit` and are bundled in this adapter.
- `/loop` and `/create-skill` are Cursor built-ins. Use the installed `skill-creator` for authoring. Use supported local operations and interruptible waits for active work; do not invent a loop service.
- pstack has no `/orchestrate` skill. Orchestrate is a `/poteto-mode` playbook. If the slash menu shows `/orchestrate`, another plugin provides it.

## Playbooks and principles

Playbooks are step lists inside `/poteto-mode`, not skills, so they have no slash command. Inside `/poteto-mode`, describing the task picks one, and these phrases name one directly:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs Autopilot-full. "stack them, don't ship" runs Autopilot-stack.
- "run the eval playbook" runs Eval.

Without `/poteto-mode`, a phrase such as "babysit this pr" can start Cursor's own skill for the same job instead. The Playbooks section of [`poteto-mode`](../poteto-mode/SKILL.md) lists every playbook and when it applies. [Guide page 6](../../docs/guide/06-verify-and-ship.md) covers opening, babysitting, and landing a PR.

pstack has no planning skill. Cursor's Plan Mode is an upstream host feature, not a mode this skill can enable on Codex. For work that spans phases or stacked PRs, asking `/poteto-mode` for a plan runs the [Multi-phase plan playbook](../poteto-mode/playbooks/multi-phase-plan.md), which writes the plan and doesn't implement it. Ordinary implementation plans go directly to Sol. New or substantively changed master or system architecture, key contracts, and consequential design tradeoffs go directly to Astra. For an unresolved design question, the Prototype playbook or an explicitly selected `/architect` comparison can provide evidence under `CODEX.md`.

Principles are one-rule skills that `/poteto-mode` reads and cites in its replies. The user rarely invokes one. They steer with the names instead, as in "apply prove it works. show me the real output." Typing `/principle-<name>` still loads one on demand. [Guide page 8](../../docs/guide/08-principles.md) lists them.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| The mode stopped applying after a few turns | On Codex, read the active instructions and `CODEX.md` before inferring a cause. Name `/poteto-mode` to request it again. Custom Mode shortcuts apply only to Cursor. |
| A question got treated as the next step of the last task | Say "new task", or say the turn doesn't need the mode. |
| A new model choice had no effect | Distinguish maintained source, deployed files, installed cache, and the active session. Verify the requested model and effort through actual routing evidence. |
| Runs cost more than expected | See the cost paragraph under Get set up. |
| A skill didn't load on its own | Inspect its discovery and invocation metadata. `poteto-help` is explicit-only. Other skills follow their own policy and the selected workflow. |
| Parallel agents overwrote each other | Assign one writer per resource. Use separate worktrees for conflicting candidates and disjoint files for ordinary parallel work. Cloud agents are unavailable here. |
| An overnight run moved but finished nothing | Define a checkable finish condition and report missing evidence. Cursor `/loop` is unavailable here. See [guide page 7](../../docs/guide/07-overnight.md). |
| The reply claims success from a green build | Ask for the real command, flow, stored value, or profile. That's the prove-it-works principle. |

For a run that drifts, [`references/prompting.md`](references/prompting.md) has one-line steers. [Guide page 10](../../docs/guide/10-recipes-and-pitfalls.md) has more pitfalls and the recipes worth copying.

## Make pstack my own

- [`/automate-me`](../automate-me/SKILL.md) drafts a personal mode skill from the user's own history, to use alongside `/poteto-mode`.
- [`/reflect`](../reflect/SKILL.md) after a session turns its lessons into skill edits the user approves.
- `/poteto-mode write a skill for <workflow>` runs the authoring playbook. The eval playbook tests a skill change blind.
- Report a misbehaving skill and complete reachable authorized work. Repair it or open a separate PR only within the authorized scope.

[Guide page 9](../../docs/guide/09-make-it-yours.md) covers each of these.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from [`references/recipes.md`](references/recipes.md) when one fits, then link the actual source used. Keep it short unless the user asked for the whole map. Usage help performs only the source and state reads needed to answer; it does not execute examples, alter configuration, create agents, or start evaluations.
