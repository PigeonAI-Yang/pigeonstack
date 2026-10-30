# Host details for the current operation

Read only the section needed for the active tool, saved-task context, live control, or authorized installation. Global AGENTS.md owns permissions. [CODEX.md](CODEX.md) is the short entry, and [MULTI_AGENT.md](MULTI_AGENT.md) owns agent procedures. Historical Desktop observations below are compatibility evidence; check the current tool schema before relying on an old limit.

## Translate host tools

| Upstream concept | Codex equivalent |
| --- | --- |
| `Task`, background subagent | `collaboration.spawn_agent`, already asynchronous |
| Per-role rule, budget, default model | The role mapping and exact arguments in `MODELS.md` |
| `generalPurpose` | General/default agent with an explicit scope |
| `poteto-agent` mechanical helper | Luna only for simple repetitive work with a fixed brief; use Sol for ordinary implementation |
| Read-only flag | Explicit no-mutation assignment; no invented tool argument |
| `AskQuestion` | Available user-input tool for missing facts or preferences, never an approval workaround |
| Cursor `create-skill` | Installed `skill-creator` and its validator |
| Cursor cloud VM | No configured equivalent; report the missing capability. |
| `/loop` | For user-requested recurring or future follow-up, use `mcp__codex_app__automation_update` with `kind="heartbeat"`. The default heartbeat attaches to the current local thread, and the live tool schema governs authorization and arguments. A heartbeat is a scheduler, not an internal completion wait. Internal waits and authorized top-level report routes handle result-driven continuation while work is active. Waits do not wake a closed turn. Claim actual continuation only after the tool returns registration state and a real follow-up is observed. Installing pstack registers no heartbeat or scheduled job. |
| Codex goal tools | Use `create_goal` only when the user explicitly asks to create a goal. Ordinary task instructions do not authorize goal creation. `get_goal` reads the current goal. `update_goal` changes its status. Neither schedules work or proves runtime enforcement. |
| Unix commands and `/tmp` | Native PowerShell and workspace `work/`, or an existing compatible runtime |
| `.cursor/skills` | Project `.agents/skills` |
| Cursor transcripts | Available task tools or targeted Codex session records |

## Position feedback for live control

Read this section only for a task that controls movement from live coordinates. Handle delayed feedback through the existing owner's action-observation-correction loop, allowing for network jitter. If coordinates stop updating, existing bounded movement may elicit fresh data only while the instance, map, source validity, and input ownership still support that action. Avoid indefinite waits and needless reinitialization. Preserve user Stop and necessary input limits. Never fabricate freshness, arrival, or effects.

## Prepared local checks

The source helper `hooks/task_context.py` supports explicit `read` and `update` commands for the selected marked body. Read returns the whole-record SHA-256 and record and body byte counts. It returns the body only up to 16,384 bytes; a larger body yields `current_oversized` without text or truncation. The 4–8 KiB checkpoint target is advisory. The owner prepares a complete UTF-8 body and updates the same record with the SHA returned by read. The helper archives the complete old body, rejects stale preimages, writes a complete candidate atomically, and reads it back. A stale preimage detected at the initial check creates no archive; drift detected after archive publication can leave a recoverable archive without replacing the record. A post-replacement verification failure reports an uncertain commit. Direct editors bypass the helper lock, and the last recheck cannot prevent every race. The helper cannot judge semantic completeness; preserve the goal, acceptance conditions, evidence references, permissions, Stop, ownership, and real blockers. It does not create a task ledger or summarize history.

The source contract selects one existing current region through metadata at the actual SessionStart event `cwd`: a bounded index at `AGENTS.md`, validated bindings in declared records, and exactly one matching session-and-workspace binding. It returns only the selected record's existing marked current body, preserving accepted, pending, and historical content as untrusted task data. It uses no environment-variable fallback, directory scan, history, transcript, ancestor lookup, or canonical-path fallback. See [SessionStart current-region contract and bounded activation](hooks/README.md) for schema, limits, owner-specific migration examples, and the activation boundary. This remains a source contract; it does not establish live host pickup or a verified owner binding.

The bundled SessionStart reader supplies saved task context only. It cannot observe later business state or intercept agent dispatch, messages, or completion. `check-plan.mjs` checks plan format, and `orch` records supplied bookkeeping and verdicts. Neither verifies a live effect nor controls Codex agent tools. This host adapter has no wired interception path for enforcing these coordination rules. Source checks and scenario review do not prove future agent behavior.

Use `tools/layout-check.mjs` when a `control-ui` acceptance promise specifies a game-frame ratio or contained log text. Read the owner's latest current checkpoint for accepted and pending requirements. After a fresh observation, the authorized browser owner can evaluate its expression and save the measurement and checker result in the existing record. Recollect the geometry after a relevant resize, expansion, or filtering action. Use the accepted ratio and explicit pixel tolerances. Fixture passes prove assertion logic only; they do not establish the actual target page. This source instruction and helper are not an enforced acceptance gate.

## Maintain and install

Maintained source: `J:/PigeonYang/pigeonstack/pstack`. Deployment mirror: `J:/Users/yangda01/.codex/local-plugins/pstack`. Installed caches are generated copies. `/setup-pstack` updates source `MODELS.md` only within the requested configuration scope. Do not edit runtime mirrors or caches directly.

After authorized source changes, validate affected files. Source-edit authorization does not authorize deployment. Preview the chosen scope with `check` and use the same flags with `deploy` only after that scope is authorized. Run these commands from `J:/PigeonYang/pigeonstack`.

| Approved change | Scope flag for `python scripts/sync.py check` and `deploy` |
| --- | --- |
| Only the global `AGENTS.md` | `--agents-only` |
| Global instruction files, role files, and pstack, preserving `config.toml` | `--rules-only` |
| Only the pstack plugin | `--plugin-only` |
| All managed files and allowlisted configuration, including model settings | No scope flag. Requires authorization for those configuration changes. |

The scope flags are mutually exclusive. `--agents-only` reads and copies only `AGENTS.md`; it does not inspect configuration or install the plugin. `--rules-only` skips configuration merging and checks that existing configuration bytes stay unchanged. It backs up the configuration before plugin installation and reports a change without overwriting it. `--plugin-only` skips all global files and configuration. All scopes retain backups, preimage checks, and file readback. Receipts identify the selected `scope`; an empty `config_drift` in a scope that skips configuration does not mean the full configuration matches the source.

When the authorized scope includes changed plugin content, update the plugin version and existing marketplace cachebuster before deployment. The normal plugin installation and installed-cache hash verification apply to scopes that contain pstack. A global-rule-only update needs no plugin version change or installation. Never use a full deployment to work around a narrower approval. Preserve explicit model and effort choices; configuration differences can be intentional.

After deployment, run the same scoped `check` and verify installed hashes where applicable. Distinguish source content, runtime files, installed artifacts, instructions read in this task, and behavior observed in a new session. Source edits do not refresh active sessions, and file checks do not prove future agent behavior.

For upstream retirements, scoped sync compares the previous runtime provenance with the new source. It previews removal, verifies the previous recorded bytes, and backs up each file before retiring it. Unknown files stay untouched; a modified retired file stops deployment for review. No directory-wide cleanup is implied.

`provenance.json` records pinned original source hashes and local adaptations. `ADAPTATION.md` records the reasons and evidence. This adapter enables no timers, background agents, or remote services. Its bundled hook source does not grant trust or activation, and source edits do not affect active sessions.
