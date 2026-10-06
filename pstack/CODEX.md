# Pstack on Codex

Read the global `AGENTS.md` first: `J:/PigeonYang/pigeonstack/AGENTS.md` in the source repository, or `J:/Users/yangda01/.codex/AGENTS.md` in the runtime installation. It owns authorization, delegation eligibility, takeover deadlines, ownership, and evidence standards. [MODELS.md](MODELS.md) owns model IDs, reasoning effort, and the upstream role mapping. This entry translates the upstream workflows to this host. Reuse unchanged instructions already read in this session.

## Activate the upstream workflow

Use pstack for substantive work. Start from `skills/poteto-mode/SKILL.md` and select the matching upstream playbook. Read the selected skill and references needed for the current phase. Keep upstream phase order, grounding, evidence requirements, and output structure. Casual conversation, direct factual answers, and an explicit user opt-out need no workflow.

An explicit `poteto-help` invocation routes to `skills/poteto-help/SKILL.md`. Usage questions get grounded help, source links, and at most one example prompt without executing the example. An actual work request follows `poteto-mode` within the existing authorization. Cursor Custom Mode shortcuts do not establish persistence on Codex; this entry and the active global instructions determine activation.

Use the existing task record for the selected phases, dependencies, and material evidence. A simple task needs no new ledger. Record a skipped or adapted phase when it affects the promised result. Do not copy a second playbook into another record. The upstream throughput checkpoint is a way to identify ready work, shared state, and dependencies in that record, not a new reporting system.

An upstream trigger selects a procedure, not extra authorization or staffing. Apply these host adaptations at the point where the procedure calls for them:

- `how` and `why` keep their tracing and evidence procedures. The Primary frames the question, assigns prescribed collection, and explains the result. Use Sol first for a bounded ordinary read-only investigation. Astra is eligible for critical design, a question unresolved after an actual Sol `xhigh` attempt, or explicit user model selection under global policy. A separate explainer or synthesizer is not mandatory.
- `architect`, `arena`, `interrogate`, and `reflect` remain available. Explicit selection may call for their candidate or review phases within the authorized scope. An ordinary feature, function boundary, difficult task, or invocation of `poteto-mode` does not automatically authorize a panel. When a panel is not selected, retain the required design or review decision in the normal owner workflow and say which independent verdict was not obtained. Never simulate a panel result. Ordinary plans and local designs use Sol. New or substantively changed master or system architecture, key contracts, and consequential design tradeoffs use Astra. A document label alone does not choose the model.
- Reproduction and verification use existing production entry points. Create a verification skill, feature map, or prototype only for a current requirement or observed gap. Apply the global normal-workflow, bug-repair, and validation-gate rules before adding any gate or prerequisite. Fixed lane counts and unit/live/performance blocks describe upstream coverage ideas; select applicable checks from the delivery promise and report unavailable evidence. They do not require irrelevant checks or a new verification framework.
- Packaging, releasing, and a full test suite each need explicit approval for that operation. Commits, pushes, PRs, merges, publication, deployment, permission changes, destructive actions, and messages to others need current-task authorization. Upstream `just do it`, end-of-playbook PR steps, broken-skill repair PRs, automatic backlog filing, and full-autonomy wording cannot supply it. Complete authorized preparation first.
- Preserve fresh children, one owner, ready parallel dispatch, the global thirty-minute assessment and takeover sequence, Primary-only ComputerUse, and serial image operations. Upstream reuse exceptions, nested fan-out, cloud agents, polling loops, and heartbeat instructions do not override these host limits. A child returns its result and retires.

The bundled guide, Cursor manifest, agent descriptions, and dormant `automations/` are upstream material. They do not install Cursor tools, enable automation, register host roles, or change this contract. Apply the same boundaries when reading them directly. Installing an upgrade does not invoke `/correct`, run evaluations, or create enforcement rules.

## Prepare the assignment

Before Luna implementation, give one defect or independently verifiable step with decisive evidence, the Primary's selected mechanism and concrete edits, allowed files and exclusions, exact checks and expected observations, and assumptions that require handoff. Keep coupled producer, caller, and test changes together. A file list, broad goal, design report, or failing-test list alone is not an execution brief.

For Luna read-only collection, name the searches, observations, or commands and evidence to return. The Primary interprets them. Split upstream roles that combine collection, investigation, design, and implementation before dispatch. For routine operations, name the artifact, destination, authorized steps, success readback, and stop conditions.

For direct Sol technical work, critical design work, a bounded read-only consultation, or a takeover, state the objective, decisive evidence, attempted approaches, allowed resources and operations, permissions, exclusions, acceptance evidence, and return conditions. A direct Sol assignment starts at `medium` and needs no prior Luna failure. Ordinary consultations and Luna-failure takeovers also start at Sol `medium`. On actual inability or an unresolved tier assessment, transfer to fresh Sol `high`, then fresh Sol `xhigh`, before Astra `high` and finally Astra `xhigh`. Do not skip Sol tiers for ordinary work or wait out a window after actual inability. Stop on success. Preserve read-only scope across consultation upgrades. A takeover owns technical resolution within that scope through implementation and verification. A consultation stays read-only and answers one explicit unresolved question. Apply the thirty-minute assessment from the first assignment at each tier, including direct Sol work. After a completed Expert assignment and accepted conclusion, route a straightforward follow-up to Luna and an ordinary new technical choice to Sol. A new critical question, a problem unresolved by Sol `xhigh`, or explicit user model selection can use Astra again.

## Translate host tools

Use `collaboration.spawn_agent` for internal work. Use a visible task creation tool only if the user requests a visible new task. Spawn a fresh child for every assignment. Pass concise evidence and interfaces. Do not simulate independent roles.

| Upstream concept | Codex equivalent |
| --- | --- |
| `Task`, background subagent | `collaboration.spawn_agent`, already asynchronous |
| Per-role rule, budget, default model | The role mapping and exact arguments in `MODELS.md` |
| `generalPurpose` | General/default agent with an explicit scope |
| `poteto-agent` code delegate | Luna execution role only after the concrete brief |
| Read-only flag | Explicit no-mutation assignment; no invented tool argument |
| `AskQuestion` | Available user-input tool for missing facts or preferences, never an approval workaround |
| Cursor `create-skill` | Installed `skill-creator` and its validator |
| Cursor cloud VM or `/loop` | No configured equivalent; use supported local operations and interruptible waits within scope, or report the missing capability |
| Unix commands and `/tmp` | Native PowerShell and workspace `work/`, or an existing compatible runtime |
| `.cursor/skills` | Project `.agents/skills` |
| Cursor transcripts | Available task tools or targeted Codex session records |

Use `worker`, `poteto-agent`, or general/default for Luna execution. Use general/default with explicit model and effort for direct Sol technical assignments, ordinary Sol consultations, takeovers, and critical design work. `astra-advisor` is optional and read-only, pinned to its initial effort. Its eligibility is critical design, a question unresolved after an actual Sol `xhigh` attempt, or explicit user model selection. It cannot write or take over. Use general/default for an authorized effort upgrade while preserving read-only scope when applicable.

When setting model or effort explicitly, use `fork_turns: "none"` or necessary finite history. Full-history inheritance does not accept overrides. Role configuration can override spawn arguments, so do not use a pinned role for a different model. Resolve `auto` and `inherit-parent` using `MODELS.md`; omitted model arguments can select the configured Luna child default and are not proof of inheritance.

For history, narrow by project, topic, and time. Read actual session metadata instead of assuming Cursor schemas. Summaries locate evidence; they do not prove execution. Memory updates require an explicit user request and the host's memory-update mechanism. Prefer attached UI sessions and available PTYs, preserve existing sessions, and apply online-request stop rules.

## Maintain and install

Maintained source: `J:/PigeonYang/pigeonstack/pstack`. Deployment mirror: `J:/Users/yangda01/.codex/local-plugins/pstack`. Installed caches are generated copies. `/setup-pstack` updates source `MODELS.md` only within the requested configuration scope. Do not edit runtime mirrors or caches directly.

After authorized source changes, validate affected files. When deployment is authorized, update the plugin version and existing marketplace cachebuster, run `python scripts/sync.py deploy` from `J:/PigeonYang/pigeonstack`, and verify installed hashes. Source-edit authorization does not authorize deployment. Distinguish disk content, installed artifacts, instructions read in the current task, and behavior verified in a new session.

`provenance.json` records pinned original source hashes and local adaptations. `ADAPTATION.md` records the reasons and evidence. This adapter enables no timers, hooks, background agents, or remote services.
