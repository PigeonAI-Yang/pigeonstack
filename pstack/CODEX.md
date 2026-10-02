# Pstack on Codex

This adapter owns workflow activation and host conversion. Global `AGENTS.md` is authoritative for scope, authorization, Primary accountability, delegation and scheduling; this file supplies host mechanics. `MODELS.md` owns model IDs and reasoning effort. Original skills supply procedures for steps selected here. Their broader triggers and mandatory staffing do not override these host rules.

## Select the necessary workflow

- Use pstack for substantive development, investigation, design, and review. Casual conversation, direct factual answers, and an explicit user opt-out need no playbook.
- Use `how` when the mechanism is not understood, `why` when historical decisions affect the answer, and `recall` when continuing prior work. The existing Primary explains and synthesizes findings.
- Select the focused playbook for the actual task. A known local change proceeds through the relevant implementation and verification steps without extra exploration.
- Use `architect` or `arena` to compare alternatives only when a required change to a core boundary cannot be met by the existing design. Crossing function or file boundaries alone is not a trigger. Use a bounded prototype only to resolve material observable uncertainty, and `interrogate` only for a substantive unresolved tradeoff.
- Read only the selected skill, playbook, and references needed now. Read a principle's leaf only when it materially affects the decision. Reuse unchanged instructions already read in this session; do not recursively load the principle index.
- Apply writing and cleanup skills as directed by global `AGENTS.md`. Use the relevant control skill when actual UI or CLI operation is required.
- Use the existing task record. Do not copy playbooks verbatim, add throughput reports, or record every inapplicable step for routine work. Record consequential omissions that affect the result.
- Use a decision trail for long work when continuity needs it. Shipping, recurring automation, project-scale orchestration, and external publication require the corresponding task scope and authorization.

These conditions govern triggers inside every bundled skill and playbook, including `poteto-mode` and `how`. Do not create explainers, synthesizers, reviewers, panels, prototypes, verification skills, or pull requests merely to satisfy an upstream step.

## Delegate through actual host tools

Apply global `AGENTS.md` first; it owns policy for Primary accountability, default delegation and scheduling. The Primary remains accountable for diagnosis, solution selection, decomposition, integration and final acceptance; that does not make bulk investigation or implementation a personal default. The Primary may read decisive evidence, interpret findings and prepare bounded assignments. Delegate execution by default. Luna (`gpt-6-luna`, `max`) implements one Primary-specified repair or accepted design step, or follows a prescribed read-only evidence checklist. Apply the "Protect authoritative technical documents" policy in global `AGENTS.md` before routing document work. The user authorizes Astra (`gpt-6-astra`, `high`) for bounded investigation or complex execution that needs sustained judgment; define the objective, decisive context, resources and permitted operations, permissions, exclusions, acceptance evidence and return conditions. Keep major scope, product and architecture decisions and final acceptance with the Primary. Use `astra-advisor` only for a specific read-only advisory question.

Before each Luna implementation assignment, write this brief inline:

- One defect or verifiable step, with the current failure and decisive evidence.
- The Primary's chosen mechanism, required behavior and concrete edit steps. For a new feature, state the selected design.
- Allowed files, interfaces and ownership; include coupled callers and tests, and state exclusions.
- The exact checks to run and the observations that establish success.
- The assumptions whose failure requires an immediate handoff, and any known long-running check.

Do not assign Luna to implement until these fields are concrete. An architecture report, a list of failing tests or an instruction to make a subsystem work does not fill this brief. Split independent defects before spawning workers. Keep a coherent producer/caller repair together; file count alone does not define task size. Do not add a new planning artifact or approval step for this brief. Prescribed read-only evidence collection and bounded Astra investigation do not require a chosen repair mechanism.

Routine packaging, marketplace ZIP uploads, installation, repository creation, commits, pushes, and established platform procedures use Luna at `max` with a concrete authorized operation brief. Public README prose and exact approved wording use Luna unless they change authoritative design decisions. These operations do not trigger Astra solely because they involve publication, an unfamiliar tool, or an operational failure. A concise operation brief names the artifact, destination, authorized steps, success readback, and stop conditions; code repairs still require the full brief above. Apply the global judgment-based routing boundary and do not add an advisor or review stage to routine operations.

A Luna read-only collection assignment names the searches, observations or commands and the evidence to return. The Primary interprets the result. If the repair mechanism is unknown, do not disguise open-ended Luna diagnosis as implementation or debugging. A bounded Astra investigation follows the objective, scope and return conditions above; its findings inform Primary decisions.

Luna may fix a mechanical mistake within the prescribed change. If evidence refutes the plan, a check fails for an unexplained reason or more scope is needed, it returns the evidence and unresolved decision promptly. It must not run its own sequence of alternative repair hypotheses. The Primary resumes diagnosis and keeps unrelated work moving.

Do not take over implementation because a task is small, a Luna assignment failed or the selected model is unavailable. Work directly only when the user explicitly asks or a non-model capability/resource restriction prevents delegation; state that reason. Minimal decision-critical reading and final acceptance inspection may remain with the Primary. If a selected model is unavailable, use another currently authorized model only when it fits the assignment boundaries; if none does, report a blocker. Never silently substitute a model generation or provider, or reduce Luna preparation to save time or increase concurrency.

Use `collaboration.spawn_agent` for internal work. `worker` and `poteto-agent` support Luna implementation or prescribed read-only evidence collection. A chosen solution and full execution brief are required only for implementation; evidence collection uses the named checklist. Use `astra-advisor` only for a specific read-only advisory question. For authoritative technical-document work, bounded investigation or complex execution needing sustained judgment, use the supported general/default role with explicit model and effort from `MODELS.md`, not `astra-advisor`, `worker` or `poteto-agent`. The global document policy also permits a stronger model explicitly selected by the user. Never simulate a role or independent verdict. Pass concise evidence and interfaces instead of the whole parent history.

Schedule ready independent work under global `AGENTS.md`: dispatch multiple nonconflicting assignments up to actual capacity before waiting, then dispatch newly unlocked work as each result arrives while unrelated work continues. Do not impose a full-batch barrier. Serialize only real dependencies or resource, permission and tool limits. Keep one owner per shared resource and use a fresh child for every assignment; never use `followup_task` to create new work. Do not invent busywork or artificial partitions to fill slots. When no independent work remains, use an interruptible `collaboration.wait_agent` call with `timeout_ms: 3600000` and follow the global renewal rule; do not poll for unchanged status. A completed child is retired. Messages to a running child may only clarify its current assignment; send follow-on work to a fresh child after ownership transfers. Batch nonurgent feedback; interrupt for a user stop, resource conflict, urgent correction or confirmed wrong direction. Use `create_thread` only when the user requests a visible new task. Existing project rules may retain exclusive live-operation ownership, but that does not prohibit read-only evidence collection on separate resources.

## Apply authorization and verification boundaries

Apply global `AGENTS.md` to reproduction evidence, repair scope, permissions, and verification. Upstream autonomy, PR, merge, external-message, and broken-skill repair steps do not expand authorization. Finish the authorized local result before reporting a remaining external action.

Use existing verification entry points. Create a verification skill or feature map only when the current task needs a reusable entry point that does not exist. Project verification skills belong in `.agents/skills/verify-<app>/`. Run a newly created skill on a real feature before calling it verified. Such artifacts are not prerequisites for ordinary changes.

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

Prefer existing UI automation and an available PTY. Inspect attached browsers before operating them and preserve existing sessions. Discover external capabilities only when needed. Follow the global stop rule for authentication challenges, denials, and rate limits.

## Maintain and install the adapter

The maintained source is `J:/PigeonYang/pigeonstack/pstack`. `J:/Users/yangda01/.codex/local-plugins/pstack` is a deployment mirror, and installed caches are generated copies. `/setup-pstack` updates the maintained source's `MODELS.md`, then deploy with `python scripts/sync.py deploy`; do not edit the runtime mirror or an installed cache directly. Verify exposed model IDs and a successful request before activating new defaults. An explicitly requested but unavailable model may be documented as a target and saved in a named, inactive profile. Preserve working defaults and report the gap; do not silently substitute generations, fabricate catalog entries, or retry access denials.

After an authorized source change, validate affected files, update the plugin version and any existing marketplace cachebuster, then deploy with `python scripts/sync.py deploy` and verify the installed copy against the maintained source by hash. Distinguish installation, current-task instruction reads, and behavior observed in a new session.

Keep global rules, roles, and adapter updates in English. Preserve upstream attribution in `provenance.json` and record adaptations in `ADAPTATION.md`. This installation activates no timers, hooks, background agents, or remote services.
