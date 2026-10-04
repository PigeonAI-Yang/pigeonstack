# Pstack on Codex

Before using this entry, read global `AGENTS.md`: use `J:/PigeonYang/pigeonstack/AGENTS.md` when maintaining source, or `J:/Users/yangda01/.codex/AGENTS.md` in the runtime installation. It owns scope, authorization, roles, delegation, takeovers, scheduling, resource ownership, and evidence standards. This file owns workflow activation, host tools, and assignment briefs. Read [MODELS.md](MODELS.md) before selecting a model or effort. Reuse unchanged instructions already read in this session. Original skills supply procedures only for steps selected here; their broader triggers and mandatory staffing do not override these host rules.

## Select the necessary workflow

- Use pstack for substantive development, investigation, design, and review. Casual conversation, direct factual answers, and an explicit user opt-out need no playbook.
- Use `how` when the mechanism is not understood, `why` when historical decisions affect the answer, and `recall` when continuing prior work. The existing Primary explains and synthesizes findings.
- Select the focused playbook for the actual task. A known local change proceeds through relevant implementation and verification without extra exploration.
- Use `architect` or `arena` to compare alternatives only when a required change to a core boundary cannot be met by the existing design. Crossing function or file boundaries alone is not a trigger. Use a bounded prototype only to resolve material observable uncertainty, and `interrogate` only for a substantive unresolved tradeoff.
- Read only the selected skill, playbook, and references needed now. Read a principle's leaf only when it materially affects the decision; do not recursively load the principle index. Apply the writing and cleanup skills required by global `AGENTS.md`. Use the relevant control skill for actual UI or CLI operation.
- Use the existing task record. Do not copy playbooks verbatim, add throughput reports, or record every inapplicable step for routine work. Record consequential omissions that affect the result, and use a decision trail for long work when continuity needs it.
- Shipping, recurring automation, project-scale orchestration, and external publication require the corresponding scope and authorization. Upstream autonomy, PR, merge, external-message, and broken-skill repair steps do not grant it. Finish the authorized local result before reporting a remaining external action. Global approval requirements also apply to preparation requested by an upstream workflow.

These conditions govern every bundled skill and playbook, including `poteto-mode` and `how`. Do not create explainers, synthesizers, reviewers, panels, prototypes, verification skills, or pull requests merely to satisfy an upstream step.

## Prepare the assignment

Choose the assignment type under global `AGENTS.md`. Write the appropriate brief inline; do not add a planning artifact or approval step.

For Luna implementation, make all fields concrete before spawning:

- One defect or independently verifiable step, with the current failure and decisive evidence. For a new feature, state the current requirement and selected design.
- The Primary's chosen mechanism, required behavior, and concrete edit steps.
- Allowed files, interfaces, and ownership, including coupled callers and tests; state exclusions.
- Exact checks and observations that establish success.
- Assumptions whose failure requires immediate handoff, return conditions, and any known long-running check.

An Expert or architecture report, file list, broad goal, failing-test list, or instruction to make a subsystem work does not fill this brief. Apply the global assignment rule when grouping or splitting work.

A Luna read-only collection brief names the searches, observations, or commands and the evidence to return. It does not require a chosen repair mechanism. A routine operation brief names the artifact, destination, authorized steps, success readback, and stop conditions. Code repairs still require the full implementation brief.

For a bounded read-only Astra investigation, technical-document assignment, or Senior Executor or Expert takeover, state the objective or problem, decisive evidence, any attempted approaches and results, allowed resources and operations, permissions, exclusions, acceptance evidence, and return conditions. A takeover does not require a Primary-prescribed solution. For a read-only consultation, frame the unresolved issue as one explicit question. Global `AGENTS.md` defines the different ownership and mutation boundaries of these assignments.

## Use actual host tools

Use `collaboration.spawn_agent` for internal work. Use `create_thread` only when the user requests a visible new task. Never simulate a role or independent verdict. Pass concise evidence and interfaces instead of the whole parent history. Global `AGENTS.md` governs fresh children, parallel dispatch, ComputerUse, the shared image limit, waits, and takeovers; apply those rules without adding staffing stages.

| Assignment | Supported role |
| --- | --- |
| Luna implementation, routine operations, or prescribed read-only collection | `worker`, `poteto-agent`, or general/default |
| Senior Executor or Expert takeover, authoritative technical documents, bounded read-only Astra investigation, or other explicitly selected execution | General/default with explicit model and effort from `MODELS.md` |
| Optional read-only Astra consultation at its initial effort | `astra-advisor`, whose model and effort are pinned, or general/default with explicit arguments |

`astra-advisor` cannot write or take over implementation. `worker` and `poteto-agent` cannot perform takeovers or authoritative document work; their contracts permit specified execution or prescribed collection. Use general/default for any authorized Astra effort upgrade and preserve the assignment's read-only scope when applicable. No new role identifier is needed.

When overriding model or effort, use `fork_turns: "none"` or necessary finite history; full-history inheritance does not accept overrides. Custom role files can override spawn arguments. Ordinary worker files omit model and effort, while the read-only advisor pins Astra at its initial effort. Use the exact IDs and efforts in `MODELS.md`.

## Use existing verification entry points

Apply global `AGENTS.md` to reproduction, repair scope, authorization, and verification. Create a verification skill or feature map only when the current task needs a reusable entry point that does not exist. Project verification skills belong in `.agents/skills/verify-<app>/`. Run a newly created skill on a real feature before calling it verified. These artifacts are not prerequisites for ordinary changes.

## Translate tools and paths

| Upstream concept | Codex equivalent |
| --- | --- |
| `Task`, background subagent | `collaboration.spawn_agent`, already asynchronous |
| Role model defaults | `MODELS.md`, explicit supported tool arguments |
| Read-only investigation or review | Assignment forbids mutations to source and shared state; separate evidence output is allowed |
| `AskQuestion` | Available user-input tool for missing information or preferences |
| Cursor `create-skill` | Installed Codex `skill-creator` and its validation helper |
| Cursor cloud agent or VM | No configured equivalent; report the gap when cloud execution is required |
| Unix commands and `/tmp` | Native PowerShell and workspace `work/`; use an existing compatible runtime when needed |
| Cursor transcript stores | Codex task tools or targeted local session records |

For history, prefer task-list and task-read tools within the requested project, topic, and time window. Summaries locate evidence; they do not prove execution. Locate local records using actual session metadata, not assumed Cursor paths or schemas. Memory updates require an explicit user request and the host's memory-update mechanism.

Prefer existing UI automation and an available PTY. Inspect attached browsers before operating them and preserve existing sessions. Discover external capabilities only when needed. Apply global authorization and online-request stop rules.

## Maintain and install the adapter

The maintained source is `J:/PigeonYang/pigeonstack/pstack`. `J:/Users/yangda01/.codex/local-plugins/pstack` is its deployment mirror, and installed caches are generated copies. `/setup-pstack` updates the source `MODELS.md`; do not edit a runtime mirror or installed cache directly. Model activation checks are defined in `MODELS.md`.

Validate affected files after an authorized source change. When deployment is authorized, update the plugin version and any existing marketplace cachebuster, run `python scripts/sync.py deploy` from `J:/PigeonYang/pigeonstack`, and verify the installed copy against the source by hash. A source-edit authorization alone does not authorize deployment. Distinguish installation, current-task instruction reads, and behavior observed in a new session.

Preserve upstream attribution in `provenance.json` and record adaptations in `ADAPTATION.md`. This installation activates no timers, hooks, background agents, or remote services.
