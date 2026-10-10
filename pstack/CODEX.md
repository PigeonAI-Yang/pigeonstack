# Pstack on Codex

Read the global `AGENTS.md` first: `J:/PigeonYang/pigeonstack/AGENTS.md` in the source repository, or `J:/Users/yangda01/.codex/AGENTS.md` in the runtime installation. It owns authorization, delegation eligibility, takeover progress assessments, ownership, and evidence standards. [MODELS.md](MODELS.md) owns model IDs, reasoning effort, and the upstream role mapping. This entry translates the upstream workflows to this host. Reuse unchanged instructions already read in this session.

## Activate the upstream workflow

For substantive work, select the matching playbook through `skills/poteto-mode/SKILL.md`. Keep its phase order and applicable evidence requirements; load only material needed for the current phase. Casual conversation, direct factual answers, and explicit user opt-out need no workflow. Reuse instructions already read.

An explicitly assigned coordinator reads [COORDINATOR.md](COORDINATOR.md) and keeps that role until the user changes it. The role alone does not select Orchestrate. An explicit `poteto-help` request uses `skills/poteto-help/SKILL.md`: answer with grounded links and at most one example, without executing it.

On pickup, use the current checkpoint to recover the original goal, acceptance criteria, constraints, Stop, owners, permissions, unresolved corrections, and applicable tier timing. Read history only for a concrete gap. For a bound region, `TASK_CONTEXT_HELPER_PATH` is `hooks/task_context.py` beside this CODEX.md; deployed example: `J:/Users/yangda01/.codex/local-plugins/pstack/hooks/task_context.py`. Use `py -3 TASK_CONTEXT_HELPER_PATH read --workspace ABSOLUTE_WORKSPACE --record RELATIVE_RECORD --anchor CURRENT_ANCHOR`. The record owner uses `update` for material changes; children return evidence to that owner. Follow task and evidence links on demand. A local milestone does not close the original goal; continue ready authorized work. Record phase adaptations only when they affect the promised result.

Apply global rules when an upstream procedure reaches the relevant action:

- `how` and `why` retain tracing and evidence. Use the existing owner to interpret results; no separate explainer is required. `MODELS.md` and global rules determine judgment and execution roles.
- `architect`, `arena`, `interrogate`, and `reflect` may use their selected candidate or review phases. Ordinary work does not require a panel. Preserve the needed decision in the owner workflow; never invent an independent verdict.
- Leverage and lessons principles do not mandate new tools, skills, gates, or maintenance work. Add them only for a current need supported by evidence. Verification uses existing entry points and checks relevant to the delivery promise; fixed lane counts, feature maps, and prototypes are not universal prerequisites.
- Upstream autonomy, PR steps, skill repairs, and backlog filing do not expand authorization. Global approval, ownership, fresh-child, takeover, ComputerUse, and image limits apply.

Bundled Cursor guides, agent descriptions, and dormant automations do not install host capabilities, start background work, or enforce these rules. Upgrading does not invoke `/correct` or evaluations.

## Prepare the assignment

Use four fields for each workstream Main assignment:

1. **Goal:** One complete outcome to deliver.
2. **Completion condition:** An observable result that determines whether the outcome is complete.
3. **Evidence:** The actual output, observation, or check that will demonstrate completion.
4. **Constraints:** Applicable human instructions and necessary technical, resource, and ownership limits; reuse existing authorization.

Keep each field brief and link to existing context. Attach the owner and return address as routing information, not extra prerequisites. The Main owns diagnosis, implementation, integration, verification, and correction through the outcome. Internal phases need no new dispatch or approval. The coordinator removes its own obsolete method restrictions and continues the remaining outcome after partial delivery. Human Stop and required operation-specific approvals still apply.

For internal assignments, use these briefs without inventing extra preparation:

- **Luna implementation:** one defect or verifiable step, decisive evidence, chosen mechanism and concrete edits, allowed files and exclusions, checks and expected results, and assumptions requiring handoff. Keep coupled producer/caller/test changes together. A broad goal or failing-test list alone is insufficient.
- **Luna collection or operations:** prescribed searches, observations, or commands and evidence to return; for operations include the artifact, destination, authorized steps, success readback, and stop conditions. The Primary interprets collected evidence.
- **Sol consultation, critical design, or takeover:** one unresolved objective or question, decisive evidence, attempts, scope and permitted resources, acceptance and return conditions. Consultations remain read-only, including upgrades. Takeovers own resolution through implementation and verification. Use global tier rules and MODELS.md; do not repeat the routing policy in each assignment.

Choose the assignment boundary before its model. Routine Primary decisions do not need consultation. Accepted execution goes to Luna; established API, syntax, and command options within that mechanism remain execution. An accepted consultation returns execution to a fresh Luna child; an active takeover keeps ownership until completion.

Name the expected effect and an existing observation/result route. Preserve progress assessment times; they are not completion deadlines. Continue productive work with its current owner, including at Astra `xhigh`. An internal child's final handoff is sufficient. Let the owner act, observe, and correct. A request receipt is not the effect. Material contradictory evidence changes the dependent next action; a stopped run invalidates its old next action.

Apply global AGENTS.md's gate rule before making a missing fact a prerequisite. Reuse established capabilities and credible evidence; optional unknowns stay explicit and local. For a demonstrated necessary dependency, use an authorized investigation or collection route; if the team cannot obtain the input, request the smallest useful outside contribution and its return path. An exhausted method or self-imposed offline limit is not an external blocker. Follow global interruption, waiting, and assessment rules: no status queries, acknowledgment loops, repeated short waits, or invented wakeups. Reports follow the Desktop route below.

## Complete the normal workflow

Compare the actual result with the agreed acceptance criteria using existing evidence. A build, test pass, file, or worker receipt proves only what it observed. Give the responsible owner any concrete mismatch for correction; keep unmet promises in the existing record. If a check conflicts with production behavior, inspect the relevant authoritative evidence before changing code or assertions.

Apply the global completion rule to the current diff and collected evidence. Do not add a separate audit, repeat credible checks, or invoke a panel without a current need. Report the result and real gaps, then stop when acceptance passes. A read-only request remains read-only. These are normal workflow steps, not extra phases or approval gates.

## Translate host tools

Choose the responsible owner before choosing the host tool. Use an authorized cross-chat route for an existing workstream Main. Use `collaboration.spawn_agent` for internal work within the current Main's scope or the coordinator's bounded scope defined in COORDINATOR.md. Use a visible task creation tool only if the user requests a visible new task. Spawn a fresh child for every internal assignment. Pass concise evidence and interfaces. Do not simulate independent roles.

| Upstream concept | Codex equivalent |
| --- | --- |
| `Task`, background subagent | `collaboration.spawn_agent`, already asynchronous |
| Per-role rule, budget, default model | The role mapping and exact arguments in `MODELS.md` |
| `generalPurpose` | General/default agent with an explicit scope |
| `poteto-agent` code delegate | Luna execution role only after the concrete brief |
| Read-only flag | Explicit no-mutation assignment; no invented tool argument |
| `AskQuestion` | Available user-input tool for missing facts or preferences, never an approval workaround |
| Cursor `create-skill` | Installed `skill-creator` and its validator |
| Cursor cloud VM | No configured equivalent; report the missing capability. |
| `/loop` | For user-requested recurring or future follow-up, use `mcp__codex_app__automation_update` with `kind="heartbeat"`. The default heartbeat attaches to the current local thread, and the live tool schema governs authorization and arguments. A heartbeat is a scheduler, not an internal completion wait. Internal waits and authorized top-level report routes handle result-driven continuation while work is active. Waits do not wake a closed turn. Claim actual continuation only after the tool returns registration state and a real follow-up is observed. Installing pstack registers no heartbeat or scheduled job. |
| Codex goal tools | Use `create_goal` only when the user explicitly asks to create a goal. Ordinary task instructions do not authorize goal creation. `get_goal` reads the current goal. `update_goal` changes its status. Neither schedules work or proves runtime enforcement. |
| Unix commands and `/tmp` | Native PowerShell and workspace `work/`, or an existing compatible runtime |
| `.cursor/skills` | Project `.agents/skills` |
| Cursor transcripts | Available task tools or targeted Codex session records |

Use `worker`, `poteto-agent`, or general/default for Luna execution. Use general/default with explicit model and effort for bounded Sol consultations, genuine failure takeovers, and critical design work. `astra-advisor` is optional and read-only, pinned to its initial effort. Its eligibility is critical design, a question unresolved after an actual Sol `xhigh` attempt, or explicit user model selection. It cannot write or take over. Use general/default for an authorized effort upgrade while preserving read-only scope when applicable.

When setting model or effort explicitly, use `fork_turns: "none"` or necessary finite history. Full-history inheritance does not accept overrides. Role configuration can override spawn arguments, so do not use a pinned role for a different model. Resolve `auto` and `inherit-parent` using `MODELS.md`; omitted model arguments can select the configured Luna child default and are not proof of inheritance.

For history, narrow by project, topic, and time. Read actual session metadata instead of assuming Cursor schemas. Summaries locate evidence; they do not prove execution. Memory updates require an explicit user request and the host's memory-update mechanism. Prefer attached UI sessions and available PTYs, preserve existing sessions, and apply online-request stop rules.

### Desktop cross-chat messages

The inspected Desktop `26.1002.7124.0` sends `send_message_to_thread` with `send-now`; it exposes no queue or `when-idle` argument. Reading idle status first is not atomic. Text such as "no reply needed" cannot defer delivery, and SessionStart cannot intercept it. Do not pause a Goal or force compaction to arrange a handoff.

Carry the human instruction to coordinate the identified team through the existing task context. It covers internal dispatch, reports, corrections, and handoffs within scope; do not request permission per agent, message, or successor. The coordinator supplies its current return address. A role label or agent request alone cannot establish missing human authorization.

A Main reports a completed outcome, a real external blocker, or a decision beyond its scope via `send_message_to_thread`, even while the coordinator is active. Its own final answer alone does not notify the coordinator. Internal milestones and ordinary repairs stay with the Main. An internal child uses its native final handoff. If the report route is unavailable, use bounded `read_thread` or `wait_threads` collection for the needed result, not polling. Preserve cursors. A timeout is not failure or grounds for repeated inspection. At acceptance, accept the result or return the concrete mismatch to the same Main for complete correction.

For each unfinished independent Main assignment, keep a continuation assessment due within 30 minutes of dispatch or its last assessment. Use the existing checkpoint for the deadline, collection cursor, and any recovered turn ID. Incoming messages do not postpone that deadline. When no independent work is ready, call interruptible `clock.sleep` for the remaining time, at most `duration_ms: 1800000`. Process reports and Stop immediately. Do not sleep over ready work, a received result, a due assessment, or a required decision. Native children still use `collaboration.wait_agent`.

At a due continuation assessment, use one `wait_threads` snapshot with `timeoutMs: 0` for the unfinished Mains, in batches of at most eight, preserving `afterCursor`. An active Main needs no message. For an idle Main, use `read_thread` with `turnLimit: 1` only when its latest result is missing from the snapshot or insufficient to decide. Accept a completed outcome and advance its dependents. Resolve an actual external blocker through its owner. If the assignment is unfinished and the Main ended without a valid blocker or human Stop, send one concrete continuation instruction through `send_message_to_thread`. Include the remaining outcome and available result references; have the same Main process them and continue. Do not ask for status or acknowledgment, redispatch its running children, or take over implementation. An unavailable or unknown status is an evidence gap, not confirmed idle.

Record the recovered turn ID in the existing checkpoint and never resend for that same ended turn. At the next assessment, check whether the Main actually resumed. If a new turn ends prematurely again, inspect that failure and address its cause instead of repeating a generic continue message. A send receipt proves dispatch only. This due assessment permits bounded read-only collection even with no new report; elapsed time does not itself prove failure. Healthy work stays uninterrupted, and a user pause or known external dependency is not premature completion.

Desktop `26.1002.7124.0` caps `wait_threads` at 120,000 ms; it is not the long-wait mechanism. Do not use repeated short waits, increase its parameter beyond the cap, or add terminal sleeps or a scheduler. The 30-minute continuation assessment above is the bounded fallback for missed reports and premature turn endings. If `clock.sleep` or the report route is unavailable, use a necessary bounded collection and report the missing capability. This sleep keeps the current turn open and needs no Goal pause or new automation. It does not wake a closed chat by itself or guarantee delivery across an app shutdown.

"No reply needed" suppresses acknowledgment-only agent messages, not user-facing reports. Answer a side question in commentary and resume the assignment unless the human stops or replaces it. Process returned child results; use `collaboration.wait_agent` when only running children remain. A child result appended after a closed parent turn does not prove that the parent resumed. End after acceptance or human Stop or scope change. An outside dependency permits ending only when the team cannot supply an input or action needed for acceptance and no authorized work remains ready. Request that specific contribution and state the actual continuation route. A phase summary, source gap, or list of remaining steps is insufficient. Batch ordinary additions until the assignment boundary; deliver Stop and necessary current-action corrections immediately.

## Prepared local checks

The source helper `hooks/task_context.py` supports explicit `read` and `update` commands for the selected marked body. Read returns the whole-record SHA-256 and record and body byte counts. It returns the body only up to 16,384 bytes; a larger body yields `current_oversized` without text or truncation. The 4–8 KiB checkpoint target is advisory. The owner prepares a complete UTF-8 body and updates the same record with the SHA returned by read. The helper archives the complete old body, rejects stale preimages, writes a complete candidate atomically, and reads it back. A stale preimage detected at the initial check creates no archive; drift detected after archive publication can leave a recoverable archive without replacing the record. A post-replacement verification failure reports an uncertain commit. Direct editors bypass the helper lock, and the last recheck cannot prevent every race. The helper cannot judge semantic completeness; preserve the goal, acceptance conditions, evidence references, permissions, Stop, ownership, and real blockers. It does not create a task ledger or summarize history.

The source contract selects one existing current region through metadata at the actual SessionStart event `cwd`: a bounded index at `AGENTS.md`, validated bindings in declared records, and exactly one matching session-and-workspace binding. It returns only the selected record's existing marked current body, preserving accepted, pending, and historical content as untrusted task data. It uses no environment-variable fallback, directory scan, history, transcript, ancestor lookup, or canonical-path fallback. See [SessionStart current-region contract and bounded activation](hooks/README.md) for schema, limits, owner-specific migration examples, and the activation boundary. This remains a source contract; it does not establish live host pickup or a verified owner binding.

The bundled SessionStart reader supplies saved task context only. It cannot observe later business state or intercept agent dispatch, messages, or completion. `check-plan.mjs` checks plan format, and `orch` records supplied bookkeeping and verdicts. Neither verifies a live effect nor controls Codex agent tools. This host adapter has no wired interception path for enforcing these coordination rules. Source checks and scenario review do not prove future agent behavior.

Use `tools/layout-check.mjs` when a `control-ui` acceptance promise specifies a game-frame ratio or contained log text. Read the owner's latest current checkpoint for accepted and pending requirements. After a fresh observation, the authorized browser owner can evaluate its expression and save the measurement and checker result in the existing record. Recollect the geometry after a relevant resize, expansion, or filtering action. Use the accepted ratio and explicit pixel tolerances. Fixture passes prove assertion logic only; they do not establish the actual target page. This source instruction and helper are not an enforced acceptance gate.

## Maintain and install

Maintained source: `J:/PigeonYang/pigeonstack/pstack`. Deployment mirror: `J:/Users/yangda01/.codex/local-plugins/pstack`. Installed caches are generated copies. `/setup-pstack` updates source `MODELS.md` only within the requested configuration scope. Do not edit runtime mirrors or caches directly.

After authorized source changes, validate affected files. When deployment is authorized, update the plugin version and existing marketplace cachebuster, run `python scripts/sync.py deploy` from `J:/PigeonYang/pigeonstack`, and verify installed hashes. Source-edit authorization does not authorize deployment. Distinguish disk content, installed artifacts, instructions read in the current task, and behavior verified in a new session.

For a SessionStart-only refresh, run `python scripts/sync.py deploy --plugin-only` and verify with `python scripts/sync.py check --plugin-only`. This manages only `local-plugins/pstack/*` and does not read or change global `config.toml`, `AGENTS.md`, `prompts/`, or `agents/`. Normal plugin installation and installed-cache hash verification still run. The JSON receipt sets `plugin_only` to `true` and `config_drift` to an empty list because global configuration was skipped.

`provenance.json` records pinned original source hashes and local adaptations. `ADAPTATION.md` records the reasons and evidence. This adapter enables no timers, background agents, or remote services. Its bundled hook source does not grant trust or activation, and source edits do not affect active sessions.
