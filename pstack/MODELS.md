# Model selection for this host

Updated 2026-10-03. Global `AGENTS.md` owns Primary responsibility, delegation, and scheduling. `CODEX.md` supplies host mechanics. This file owns model IDs and reasoning effort. Upstream role defaults do not apply.

## Active routing

Preserve the active Primary and the user's explicit model selection. Problem-solving uses three tiers: Luna at `max` as Executor, Sol at `xhigh` as Senior Executor, and Astra at `high` as Expert. Unresolved Astra attempts advance to `xhigh`, then `max`, then `ultra`. Authoritative technical documents go directly to Astra at `high`, or a stronger model explicitly selected by the user. Explicit task-specific model choices remain authoritative.

During a bounded takeover, the Senior Executor or Expert owns technical decisions, independent diagnosis, solution selection, necessary implementation, and verification within the assigned scope and permissions. Return the completed result with evidence in one final handoff. Do not require per-step Primary approval or a return to Luna for implementation. Report early only for an actual external blocker, a genuine user decision, a required scope or permission change, or an urgent correctness or ownership issue. The Primary retains goals, constraints, resource coordination, and final acceptance. User Stop and the thirty-minute assessment still apply. Optional read-only consultations remain read-only.

| Work | Model and effort |
| --- | --- |
| Default general Primary | `gpt-6.1-sol`, `high`; preserve the active explicit selection |
| Executor: specified implementation, prescribed evidence collection, verification, routine authorized operations, and ordinary public prose | `gpt-6-luna`, `max` |
| Senior Executor: bounded takeover after Luna cannot resolve the problem or reaches an unresolved thirty-minute assessment | `gpt-6.1-sol`, `xhigh` |
| Expert: bounded takeover after the Senior Executor cannot resolve the problem or reaches an unresolved thirty-minute assessment | `gpt-6-astra`, `high`, then `xhigh`, `max`, and `ultra` if unresolved |
| Expert: authoritative technical-document authorship, substantive revision, restructuring, and review | `gpt-6-astra`, `high`, or a stronger model explicitly selected by the user |
| Expert: optional bounded read-only investigation or consultation | `gpt-6-astra`, `high`; any effort upgrade preserves read-only scope |

Implementation and refactoring default to Luna after the Primary selects the solution. Route authoritative technical documents directly to Astra under the global document policy. Neither Luna nor the Sol Senior Executor authors or revises those documents. An explicit task-specific user model selection takes precedence within actual tool and access limits. Complexity labels, file count, and incomplete decomposition do not trigger a takeover.

If Luna cannot solve the assigned problem, or problem-solving remains unresolved at its 30-minute assessment, transfer the bounded problem to a fresh Sol Senior Executor using `gpt-6.1-sol` at `xhigh`. If the Senior Executor cannot resolve it or remains unresolved at its own assessment, transfer it to a fresh Astra Expert using `gpt-6-astra` at `high`. Further unresolved Astra attempts advance through `xhigh`, `max`, and `ultra`. Use a general/default child with explicit model and effort for every takeover. The dedicated `astra-advisor` role remains read-only and pinned to `high`; never use it for takeover. Ordinary complexity, task size, or incomplete decomposition alone does not trigger escalation.

Each model-and-effort tier gets a 30-minute assessment window from its first delegation. Replacements and retries within that tier do not reset the deadline. A new tier gets its own window. Preserve total problem time, partial work, evidence, failed approaches, relevant paths, and missing evidence across transfers. Assess once at the deadline; if problem-solving is unresolved, end or interrupt the attempt and transfer it to the next tier. Before transfer, stop the previous operator and its owned processes or confirm that they have released affected resources. Keep one active owner per problem. These authorized upgrades require no renewed permission and preserve existing scope and permissions. If the required model or effort is unavailable, or Astra at `ultra` remains unresolved, report the actual limit or evidence gap without a silent substitute or another escalation cycle. Escalation does not authorize external deployment, messages, destructive actions, or panels.

Each takeover owns technical resolution through completion within scope. Optional consultations remain read-only even when Astra effort increases. Other effort changes require an explicit user request. Luna does not support `ultra`.

ComputerUse operations belong exclusively to the Primary because this host does not expose that capability to children. The Primary performs every action requiring ComputerUse, including screen inspection, clicks, and typing. Never assign such an operation to any child, including a Senior Executor or Expert, or ask a child to simulate or proxy the tool to bypass this boundary. Independent text, code, and normal CLI or API work remains delegable. If a child needs ComputerUse, it sends the Primary a concrete request naming the target, action, and expected observation. The Primary performs the authorized action and returns actual evidence so the child can continue its technical work. This is a tool-ownership request, not a request for the Primary to solve the problem. Missing child ComputerUse access does not justify reasoning escalation, halt unrelated work, or add a permission step for an already authorized action. Preserve the shared serial limit for image work.

## Active configuration and availability

The active `config.toml` and selected profile determine the actual Primary model. This routing policy does not switch the Primary. Ordinary child defaults remain `gpt-6-luna` at `max`; takeovers use explicit spawn arguments.

Verify actual session routing before reporting model use. A disk edit, model label, cached catalog, or model self-identification does not prove a server-side model mapping. If the required model or effort is unavailable, report that limit without silently substituting another model, generation, provider, or Primary execution.

## Spawn contract

- Use a fresh child and task name for every assignment. A completed child is retired. Do not use `followup_task`. Pass a concise handoff with the relevant evidence, failed approaches, total problem time, and current tier deadline.
- For Luna, pass `model: "gpt-6-luna"` and `reasoning_effort: "max"`. Use `worker`, `poteto-agent`, or the general/default role. Implementation requires the concrete brief in `CODEX.md`; prescribed read-only collection uses the named checklist. Do not assign Luna unresolved repair choices or open-ended diagnosis.
- For Senior Executor takeover, use the general/default role with `model: "gpt-6.1-sol"` and `reasoning_effort: "xhigh"`.
- For Expert takeover, authoritative technical documents, or bounded read-only investigation, use the general/default role with `model: "gpt-6-astra"` and `reasoning_effort: "high"`. Unresolved Astra attempts use a fresh general/default child at `xhigh`, then `max`, then `ultra`.
- A takeover brief gives the problem, decisive evidence, attempted approaches, allowed resources, permissions, exclusions, acceptance criteria, and return conditions. The Senior Executor or Expert chooses the solution. Neither takeover requires a Primary-prescribed fix or a later Luna implementation step.
- Use `astra-advisor` only for a specific read-only consultation at `high`. Its model and effort are pinned for compatibility. Never use it for takeover or writing. `worker` and `poteto-agent` also cannot perform takeovers or authoritative document work because their contracts permit only specified execution or read-only collection.
- When overriding a model or effort, use `fork_turns: "none"` or necessary finite history. Full-history inheritance does not accept overrides.
- Custom role files can override spawn arguments. Ordinary worker files omit model and effort; the read-only advisor pins Astra at `high`. No new role identifier is required for the general/default takeovers.
- Delegates do not spawn children or expand scope. The Primary coordinates escalation, ComputerUse, resource ownership, and final acceptance. Keep one active operator per problem and release resources before transfer.
- When no independent work remains, use interruptible `collaboration.wait_agent` with `timeout_ms: 1800000`, capped by the tool maximum or the time to the next required assessment or concrete action. Use existing clock tools and assignment context. Do not add timer services or claim runtime enforcement.
- A healthy long build, download, or training run stays in its existing observation loop. External access, credentials, permissions, and unavailable services are blockers, not reasoning failures. A timeout alone does not prove failure.
- Do not create extra planners, synthesizers, or panels. The Primary judges the completed result and evidence.
