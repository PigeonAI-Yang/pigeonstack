# Pstack Codex adapter

This local plugin packages Lauren Tan's pstack v0.15.2 from the fixed upstream checkout.

- Upstream: https://github.com/cursor/plugins/tree/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d/pstack
- Upstream commit: `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`
- Upstream version: `0.15.2`
- Contents: 47 pstack skills plus `control-ui`, `control-cli`, and `deslop` from the same checkout (50 installed skills).
- `CURSOR-TEAM-KIT-LICENSE` preserves the selected Team Kit source license separately.

Adapter changes are intentionally narrow: Codex-compatible skill names/frontmatter; a short entry in each installed `SKILL.md` requiring the plugin-root `CODEX.md` and, for model work, `MODELS.md`; `disable-model-invocation: true` moved to each skill's `agents/openai.yaml` policy; project skill output paths changed from `.cursor/skills` to `.agents/skills`; pstack model-rule references point to the plugin-root `MODELS.md`; and `setup-pstack` states that Codex follows the `CODEX.md`/`MODELS.md` contract instead of writing a Cursor rule. The upstream `recall` transcript explanation remains in place with an explicit Codex history entry.

The dormant upstream `automations/` files are retained as reference material but are not registered or enabled by this plugin. No hooks, MCP servers, or apps are declared. `CODEX.md` and `MODELS.md` are supplied by the parent integration task.

Known upstream external dependencies remain explicit in the copied instructions. The workflows refer to host agent tools and model routing through `CODEX.md`/`MODELS.md`, optional GitHub CLI and MCP integrations, Playwright/Chromium/CDP or tmux/PTY/Node/Bun for the control skills, and a Grok webhook plus Tailscale for `make-bot-ui`. The dormant Benny pack refers to Slack, a tracker, and the host automation editor. The source contains one existing placeholder link, `[PR #123](url)`, in `skills/why/references/synthesizer-prompt.md`.

## Host rule consolidation on 2026-09-21

The user authorized six optimizations and required English-only global rule prose. Global AGENTS.md owns general constraints, delegation costs, evidence-based failure handoffs, and verification against the delivery promise. CODEX.md owns host workflow activation and tool conversion. MODELS.md owns model IDs and effort. Skill entry headers direct execution through that host scope; upstream workflow bodies remain attributed reference procedures rather than unconditional triggers. Global roles and plugin metadata use English. Existing instruction reads can be reused within a session when unchanged.

## Model routing revision on 2026-09-23

The user authorized Sol as the target default Primary, Luna for most bounded investigation and execution, and evidence-triggered Astra consultation. Global rules now account for token use by model and avoid duplicate Primary investigation. The Primary retains decisions and acceptance; Astra remains an option for difficult end-to-end work. Ordinary agent definitions inherit active model settings, while the dedicated advisor pins Astra at low effort. The setup-pstack host note permits explicitly requested unavailable targets in an inactive profile without repeated confirmation. The initial GPT-6 Sol request was rejected with the old client, so working defaults were preserved and GPT-6 defaults were staged separately pending availability. No model catalog, authentication, runtime permission, or automatic activation mechanism was changed.

## GPT-6 activation after the client update on 2026-09-23

After Codex updated to 26.917.6896.0 and exposed GPT-6 Sol and Luna, the user authorized removing the transition settings. Global defaults now select GPT-6 Sol at medium effort and GPT-6 Luna at high effort; the dedicated Astra advisor remains at low effort. The named gpt6-routing profile mirrors the active defaults. MODELS.md no longer instructs agents to use older-generation transition settings. Existing sessions retain their selected Primary, and model catalogs, authentication, permissions, and memories were not edited.

## Delegation and passive-wait correction on 2026-09-23

A real Sol task used repeated short waits despite the prior maximum-wait guidance. This revision specified a one-hour interruptible wait and direct renewal after an uneventful timeout. The 2026-10-03 revision below supersedes that duration and adds unresolved-problem assessments. The rules prohibit liveness polling and clarify that waiting does not cancel a child. Delegates return actionable events instead of periodic status. Bounded investigation is now delegated by default before the Primary has solved the root cause; the Primary retains decisions and acceptance. Existing exclusive live-operation and single-writer boundaries remain. This is an instruction change, not a runtime enforcement hook or a change to the wait tool implementation.

## User-selected effort settings on 2026-09-23

The user subsequently selected high for Sol, max for every Luna assignment, and high for the Astra advisor. Global defaults, the reusable gpt6-routing profile, AGENTS.md, MODELS.md, and the dedicated advisor file agree. Ordinary agent files continue to inherit global child defaults; all Luna assignments must request max. These settings supersede the previous medium/high/low starting points without restarting running children.

## Fresh subagents for every assignment on 2026-09-23

The user requires a new subagent for every assignment and considers completed agents retired. Global instructions, the host spawn contract, and agent definitions now prohibit followup_task and reactivation of completed children, including follow-on fixes on the same module. Necessary evidence moves through a concise handoff to a fresh child. A running child may receive clarification for its current assignment; resource ownership transfers only after the prior child finishes or stops. No runtime destruction or transcript deletion is required by this workflow.

## Execution-only Luna assignments on 2026-09-29

The user rejected broad assignments that make Luna diagnose, design and implement a repair. This supersedes the 2026-09-23 default investigation delegation. The Primary now determines the cause and solution, splits independent defects and supplies a concrete execution brief before delegation. Luna may execute that solution or collect evidence through a specified read-only checklist. Refuted assumptions and unexplained failures return promptly to the Primary. Global rules, both execution roles, the active configuration, base instructions, CODEX.md, MODELS.md and the bug-fix/feature playbooks use this boundary. Existing model IDs, effort, authorization and single-owner rules remain in place. This revision changes instructions, not model capability or runtime enforcement.

## Proactive parallel delegation on 2026-10-02

The user authorized proactive parallel delegation. Global `AGENTS.md` is authoritative for delegation and scheduling; this adapter supplies host mechanics. The Primary remains accountable for diagnosis, decisions, decomposition, integration and acceptance while defaulting execution to children. Luna keeps the specified-solution brief and `max` setting. Astra may perform bounded investigation or complex execution at `high` through the supported general/default role; `astra-advisor` remains read-only for specific advisory questions. Dispatch ready independent work together and newly unlocked work as dependencies clear, while preserving fresh children, single ownership, permissions, failure handoffs and interruptible waits. This changes instructions only; new-session behavior is untested.

## PigeonStack source management on 2026-10-02

The maintained pstack source is J:/PigeonYang/pigeonstack/pstack; the runtime .codex plugin tree and installed caches are deployment copies. Edit the maintained source and deploy with python scripts/sync.py deploy. Review runtime changes deliberately before importing them into this source.

## Authoritative technical-document ownership on 2026-10-02

The user reserves architecture and technical-design documents, implementation plans, contracts, and authoritative ADRs and specifications for Astra at high effort or a stronger explicitly selected model. Global AGENTS.md defines the ownership and preservation policy. CODEX.md, MODELS.md and both execution roles apply it. Luna may collect prescribed read-only inputs and implement accepted designs, but may not author, restructure, substantively revise or review these documents. The author preserves verified constraints and rationale, and the Primary accepts the actual content diff against decisive evidence. The read-only advisor remains separate from the general execution role used for writing. Existing delegation, scheduling, permissions and model configuration remain unchanged. This revision changes disk instructions, not runtime enforcement; behavior in a new session is untested.

## Routine operation routing on 2026-10-02

Global `AGENTS.md`, `CODEX.md`, and `MODELS.md` route authorized routine operations, established platform procedures, and ordinary public README prose to Luna at `max`. Platform, publication status, unfamiliar tooling, or an operational error alone does not trigger Astra. Astra remains responsible for authoritative technical documents and work that needs sustained judgment. This changes disk instructions only; behavior in a new session is untested.

## Bounded Astra routing on 2026-10-03

This revision supersedes the earlier default authorization for complex Astra execution. Implementation and refactoring use Luna after Primary solution selection. Astra handles bounded read-only unresolved questions and authoritative technical documents; other execution requires explicit task-specific user model selection. Webpage scope, file count, visual complexity, and incomplete decomposition do not expand Astra authority. New-session routing behavior has not been tested.

## Serial image operations on 2026-10-03

The user requires image generation, editing, viewing, visual analysis, and associated transfers to run serially to protect uplink bandwidth. The Primary schedules at most one such operation across itself and its children. This overrides generic parallelism for image work while preserving parallel progress on unrelated tasks. The change adds instructions, not runtime enforcement; bandwidth and new-session behavior have not been measured.

## Thirty-minute waits and advisor escalation on 2026-10-03

The user replaces the one-hour default wait with `1800000` ms, or 30 minutes. Early events return immediately. When an executor cannot solve a problem or remains unresolved at its 30-minute assessment, the Primary preserves evidence and transfers diagnosis to one fresh Astra advisor. Replacement executors do not reset elapsed problem time. If the advisor cannot resolve the question or remains unresolved at its own 30-minute assessment, a fresh advisor uses the same model at one higher effort, progressing from `high` through `xhigh` and `max` to `ultra`. The dedicated advisor role stays pinned to `high`; higher efforts use a general/default child with an explicit read-only advisory contract. This exception leaves other effort defaults unchanged. External blockers and confirmed healthy long commands do not trigger reasoning escalation. An unresolved `ultra` attempt or unavailable effort returns a concrete limit or evidence gap. The Primary retains acceptance, and fresh Luna implements accepted solutions. These are instruction changes, with no timers or runtime enforcement. Deployment and new-session behavior require separate verification.

## Tiered takeover and Primary ComputerUse on 2026-10-03

The user keeps the active Primary unchanged and authorizes three problem-solving tiers: Luna Executor at `max`, Sol Senior Executor at `xhigh`, then Astra Expert at `high`. Unresolved Astra attempts advance through `xhigh`, `max`, and `ultra`. Inability to solve the assigned problem or an unresolved thirty-minute assessment triggers the next tier. Each model-and-effort tier gets its own window; replacements within a tier do not reset it. Handoffs preserve total problem time, evidence, and failed approaches, and release the old operator's resources before transfer.

The Senior Executor and Expert own bounded technical decisions, diagnosis, necessary implementation, and verification through a completed result with evidence. No per-step Primary approval or mandatory return to Luna is required. This supersedes the earlier read-only failure handoff. The Primary retains goals, constraints, coordination, and final acceptance. Authoritative technical documents still go directly to Astra at `high`, or a stronger explicitly selected model. Optional consultations remain read-only. Takeovers use the general/default role with explicit model and effort; existing role identifiers and active model configuration remain unchanged.

Only the Primary performs operations requiring ComputerUse because children do not have that capability on this host. A child requests a concrete action and receives actual evidence from the Primary while retaining its technical responsibility. This tool boundary does not trigger reasoning escalation or stop independent work. The shared serial limit for image work remains. Existing authorization, user Stop, external-blocker, and healthy-long-command rules remain in force. These changes add instructions, not timers or runtime enforcement. Deployment and behavior in a new session require separate verification. Earlier committed entries retain their historical wording.

## Sol model ID correction on 2026-10-03

The user corrected the Sol model ID to `gpt-6.1-sol`. Current routing rules and deployment configuration now use this ID for the Primary and Senior Executor while preserving their existing `high` and `xhigh` efforts. This is a model ID and configuration correction; it does not verify server-side model mapping or change a running Primary.

## Approval before packaging, releases, and full test suites on 2026-10-03

The user requires explicit approval before packaging, releasing, or running a full test suite. Global AGENTS.md, the base prompt, and injected developer instructions use the same rule. Approval covers only the described operations, and existing explicit authorization in the current task avoids a repeated request. These operations cannot run as preparation for approval. Necessary targeted checks remain allowed within the authorized task. CODEX.md applies this boundary to upstream workflows. Existing model routing and delegation remain unchanged. This is an instruction change; behavior in a new session is untested.

## Instruction consolidation on 2026-10-04

This revision removes repeated policy text across the global AGENTS.md and host CODEX.md/MODELS.md, keeping global policy authoritative, host mechanics in CODEX.md, and model identifiers and effort in MODELS.md. The accepted routing, authorization, takeover, and verification rules were clarified without changing active model defaults, runtime configuration, or adding runtime enforcement. Deployment and behavior in a new session require separate verification.
