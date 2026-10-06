---
name: "reflect"
description: "Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect."
---
> Codex host: Read [../../CODEX.md](../../CODEX.md) before execution and [../../MODELS.md](../../MODELS.md) before assigning roles. Apply the upstream procedure below within that host contract.

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Locate the active transcript

The parent finds its own transcript file before fanning out. The system prompt names the active workspace's `agent-transcripts/` directory. Use that path. Do not glob across `~/.cursor/projects/*/`. That crosses workspace boundaries and reads private chats from unrelated projects.

```bash
ls -t <agent-transcripts>/*.jsonl <agent-transcripts>/*/*.jsonl <agent-transcripts>/*/subagents/*.jsonl 2>/dev/null | head -10
```

Three transcript layouts: legacy flat (`<id>.jsonl`), current nested (`<id>/<id>.jsonl`), and subagent (`<parent>/subagents/<child>.jsonl`).

For each candidate, read the first JSONL line and check that `message.content[0].text` contains the conversation's opening user prompt. Take the matching path. If no path resolves, write a tight digest of the session and pass that instead.

### 2. Spawn three reviewers in parallel

One message, three `Task` calls, `subagent_type: generalPurpose`, with `model` set as below, agent mode (`readonly: false`). Reviewers need MCP access for context lookups (tickets, chat threads, observability traces referenced in the transcript). Readonly strips MCPs.

Resolve each named role through the plugin-root `MODELS.md`. It defines responsibility splits, GPT models and efforts, parent aliases, and required-model failures. Do not substitute upstream defaults or create a repair PR when routing is unavailable.

| Lens | Role line | Host assignment | Prompt template |
|---|---|---|---|
| Judgment | `reflect judgment, divergent, synthesizer` | `MODELS.md`: scoped judgment review | `references/judgment-reviewer.md` |
| Tooling | `reflect tooling` | `MODELS.md`: prescribed tooling collection | `references/tooling-reviewer.md` |
| Divergent | `reflect judgment, divergent, synthesizer` | `MODELS.md`: scoped judgment review | `references/divergent-reviewer.md` |

Use each template for its selected responsibility, substituting the transcript path or digest. Give Luna only the prescribed collection checklist, and keep judgment with the role defined in `MODELS.md`. Reviewers return findings in the `Task` response body.

### 3. Synthesize

One `Task` call, `subagent_type: generalPurpose`, with `model` from the `reflect judgment, divergent, synthesizer` line (see `MODELS.md`), agent mode (`readonly: false`). The synthesizer's quality check includes spot-verifying citations, which can require MCP access. Readonly strips MCPs. Use `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. The synthesizer returns a structured Accepted / Rejected / Backlog list.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. See the **encode-lessons-in-structure** principle skill.

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

File backlog items to an external tracker only when that action is authorized. Otherwise report them locally.

For each approved Accepted item, preserve the Routing field's target skill and use the authoring procedure through the Codex `skill-creator`. Use Sol for routine adaptation of existing instructions and Luna for mechanical or exact accepted-content edits. Use Astra for new critical design decisions or an actual unresolved Sol `xhigh` attempt under `MODELS.md`. The instruction-file label alone does not require Astra. The Primary accepts the actual diff.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it doesn't.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
