# Word the prompt

> Codex host: Apply [CODEX.md](../../../CODEX.md) and [MODELS.md](../../../MODELS.md). These are prompt-writing suggestions, not extra authorization or mandatory prerequisites.

A prompt states the intent and the check for done. The playbook supplies the steps, so a few plain sentences beat a spec.

## Put in

- The goal. Say what is wrong or what the user wants.
- The done check. It can pass or fail. "Make it better" and a duration are not checks.
- The proof to show. Ask for the real command output, a video of the flow, the stored value, or a before and after number.
- What the user already knows. A symptom, a repro step, a log, or a link saves the agent a search.
- The real constraints. "repro first", "don't change any code yet", "zero behavior change", and "let me review before proceeding" each change what the agent does.

## Leave out

- The how. Say what to achieve, and leave the agent room to find a better way.
- A list of skills or steps. A hand-written order drops or reorders steps the playbook keeps. Name a skill only to override one choice.
- The user's theory of the cause, until the agent restates the problem. A stated guess narrows the search.

## Load the context first

- For a noisy report, ask the agent to restate the underlying issue in its own words and in plain English before it does anything else. A misreading shows up before any code exists.
- In a fresh chat, `/recall` earlier work on the topic. Old chats hold context that the new agent lacks.
- Before a change to unfamiliar code, ask `/how` for the mechanics and `/why` for the reasons. An agent with no traced model fixes the symptom at the first plausible spot.
- Ask `/teach` to make the case for a choice, as in "convince me it fixes the cause and not the symptom". A case is easier to check than a summary.

## Design before the plan

- For unresolved design alternatives, request prototypes or an explicit comparison when they would settle the choice. Reuse an established design when the evidence already supports it.
- Let prototypes answer the open questions. Don't review an abstract plan adversarially, because reviewers invent risks that never happen.
- For a shared package or API, ask for the README or a tutorial first, then work back to the code. The doc becomes the target the agent checks itself against.
- Ask for the plan only after the design is settled. Each step of the plan ends in a check.

## Follow up short

- "do it", "continue", and "keep going until done" are whole prompts once the chat holds the task.
- Start with "new task" when the subject changes. Otherwise the mode treats the message as the next step.

## Before stepping away

- Say "im going to bed" or "im stepping away" to keep authorized work moving. Existing approval boundaries and the user Stop rule still apply.
- Write done as checks the active workflow can run. Cursor `/loop` is unavailable on this host; use supported operations and interruptible waits without inventing a wake service.
- Ask for a fresh worktree off a named base.
- Pre-answer what the agent would stop for, such as "don't ask me before committing".
- Ask for a decision log to audit later.
- Name external blockers and the required finish condition. The global thirty-minute progress assessment and model ceiling still apply; unfinished productive work continues with its current owner.

## Steer in one line

- Restate the goal: "i said the goal is to repro. i did not ask for a fix yet."
- Name the principle: "apply prove it works. show me the real output, not the build log."
- Read the relevant principle before applying or citing it. A name alone does not prove it was loaded. The reply names the decision it changed.
