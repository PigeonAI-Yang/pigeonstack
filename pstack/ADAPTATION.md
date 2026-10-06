# Pstack Codex adapter

This source adapter imports Lauren Tan's pstack v0.15.13 from the pinned upstream checkout. Historical entries below describe earlier revisions; the final integration entry records the current source state.

- Upstream: https://github.com/cursor/plugins/tree/77526ffa67f8dafc698d14b5356e6d4fc78c3127/pstack
- Upstream commit: `77526ffa67f8dafc698d14b5356e6d4fc78c3127`
- Upstream version: `0.15.13`
- Contents: 51 pstack skills plus `control-ui`, `control-cli`, and `deslop` from the same checkout (54 source skills).
- `CURSOR-TEAM-KIT-LICENSE` preserves the selected Team Kit source license separately.

Adapter changes are intentionally narrow: Codex-compatible skill names/frontmatter; a short entry in each installed `SKILL.md` requiring the plugin-root `CODEX.md` and, for model work, `MODELS.md`; `disable-model-invocation: true` moved to each skill's `agents/openai.yaml` policy; project skill output paths changed from `.cursor/skills` to `.agents/skills`; pstack model-rule references point to the plugin-root `MODELS.md`; and `setup-pstack` states that Codex follows the `CODEX.md`/`MODELS.md` contract instead of writing a Cursor rule. The upstream `recall` transcript explanation remains in place with an explicit Codex history entry.

The dormant upstream `automations/` files are retained as reference material but are not registered or enabled by this plugin. No hooks, MCP servers, or apps are declared. `CODEX.md` and `MODELS.md` are the maintained Codex host contract.

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

## Automatic Expert escalation cap on 2026-10-04

The user caps automatic Astra Expert escalation at `xhigh`. An unresolved `high` attempt transfers to a fresh `xhigh` child. If that child cannot resolve the problem or remains unresolved at its 30-minute assessment, stop escalation and report the actual limit or evidence gap. Do not automatically escalate Astra to `max` or `ultra`, or restart the cycle. This supersedes the earlier escalation sequences recorded above. Explicit task-specific user model and effort selections remain authoritative. Luna stays at `max`, the Sol Senior Executor stays at `gpt-6.1-sol` and `xhigh`, and the active Primary and initial Astra `high` defaults remain unchanged. Global rules, the base prompt, injected developer instructions, MODELS.md, bilingual introductions, and workflow diagrams now state this cap. These are source instruction changes; deployment and behavior in a new session require separate verification.

## Full upstream 0.15.9 integration on 2026-10-04

The user selected upstream workflows as the new base while retaining the GPT ecosystem and host permissions. All upstream pstack paths at `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a` are represented in `provenance.json`. The three Team Kit skills and their license remain imported. Original hashes are separate from `adapted_sha256` and per-file adaptation notes. The unchanged logo and six guide images were checked against Git blob IDs without image viewing or transfer. The Cursor manifest and `.gitignore` are preserved as upstream material; only `.codex-plugin/plugin.json` is the Codex manifest.

The upstream comparison contains 50 modified paths, three additions, and no deletions. The additions are `correct`, `benchmark-checklist`, and `principle-explain-the-number`. Feature and bug-fix playbooks now retain the latest upstream phase structure rather than the previous local replacements. Upstream scripts were copied verbatim. The import also refreshes unchanged upstream material, so the integration does not depend on a cherry-picked subset of changes.

`CODEX.md` now translates workflow activation, tools, history, permissions, and assignment mechanics. It no longer replaces the upstream playbook phases. `MODELS.md` maps every upstream role to the existing GPT responsibilities and exact model/effort table. Combined investigation/design/implementation roles are split before dispatch. Required-model failures stop the affected assignment without model substitution or automatic repair PRs. `auto` and `inherit-parent` preserve the actual parent's model and effort through supported arguments; omitting a model is not evidence of inheritance because the host's child default is Luna.

The retired policies are upstream non-GPT defaults and generic budget rewrites, automatic model fallbacks, returned-child reuse exceptions, automatic panels, automatic external writes, and duplicated local feature/bug-fix workflows. Their procedures remain available where useful and authorized. The reasons are the user's GPT selection, fresh-child ownership, explicit action permissions, and the request to follow upstream phases. Global takeover tiers and thirty-minute assessments, authoritative-document ownership, Primary ComputerUse, serial images, ready parallel dispatch, and separate packaging/release/full-suite approvals remain intact. No new routing engine, gate framework, or timer was added.

`/correct` still requires two observed occurrences, prioritizes architecture, types, lint, tests, then documentation, and proves a check against a real past mistake. Class-by-class commits obey current-task authorization. A rule's existence does not count as a second occurrence. Importing the skill does not run it or authorize repository-wide enforcement work.

The prepared source manifest is `0.15.9+codex.20261004upstreamgpt`. Deployment, installation, runtime caches, commits, pushes, packaging, and full tests were not performed. Source checks and static role-case inspection do not establish behavior in a new session.

### Coverage of the 53 upstream changes

`Exact` means the local bytes equal the pinned upstream original. `Adapted` means the original hash, current local hash, and adaptation notes are recorded in `provenance.json`.

| Change | Upstream path | Local destination | Treatment |
| --- | --- | --- | --- |
| M | `pstack/.cursor-plugin/plugin.json` | `.cursor-plugin/plugin.json` | Exact |
| M | `pstack/README.md` | `UPSTREAM-README.md` | Adapted |
| M | `pstack/agents/poteto-agent.md` | `agents/poteto-agent.md` | Adapted |
| M | `pstack/docs/guide/01-setup.md` | `docs/guide/01-setup.md` | Adapted |
| M | `pstack/docs/guide/07-overnight.md` | `docs/guide/07-overnight.md` | Adapted |
| M | `pstack/docs/guide/08-principles.md` | `docs/guide/08-principles.md` | Adapted |
| M | `pstack/docs/guide/README.md` | `docs/guide/README.md` | Adapted |
| M | `pstack/skills/architect/SKILL.md` | `skills/architect/SKILL.md` | Adapted |
| M | `pstack/skills/architect/references/design-red-flags.md` | `skills/architect/references/design-red-flags.md` | Exact |
| M | `pstack/skills/arena/SKILL.md` | `skills/arena/SKILL.md` | Adapted |
| A | `pstack/skills/benchmark-checklist/SKILL.md` | `skills/benchmark-checklist/SKILL.md` | Adapted |
| M | `pstack/skills/blast-radius/SKILL.md` | `skills/blast-radius/SKILL.md` | Adapted |
| A | `pstack/skills/correct/SKILL.md` | `skills/correct/SKILL.md` | Adapted |
| M | `pstack/skills/figure-it-out/SKILL.md` | `skills/figure-it-out/SKILL.md` | Adapted |
| M | `pstack/skills/how/SKILL.md` | `skills/how/SKILL.md` | Adapted |
| M | `pstack/skills/how/references/explorer-prompt.md` | `skills/how/references/explorer-prompt.md` | Exact |
| M | `pstack/skills/interrogate/SKILL.md` | `skills/interrogate/SKILL.md` | Adapted |
| M | `pstack/skills/interrogate/references/code-quality-review.md` | `skills/interrogate/references/code-quality-review.md` | Exact |
| M | `pstack/skills/interrogate/references/reviewer-prompt.md` | `skills/interrogate/references/reviewer-prompt.md` | Exact |
| M | `pstack/skills/interrogate/references/rubric.md` | `skills/interrogate/references/rubric.md` | Exact |
| M | `pstack/skills/poteto-mode/SKILL.md` | `skills/poteto-mode/SKILL.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/autopilot-full.md` | `skills/poteto-mode/playbooks/autopilot-full.md` | Exact |
| M | `pstack/skills/poteto-mode/playbooks/autopilot-stack.md` | `skills/poteto-mode/playbooks/autopilot-stack.md` | Exact |
| M | `pstack/skills/poteto-mode/playbooks/babysit.md` | `skills/poteto-mode/playbooks/babysit.md` | Exact |
| M | `pstack/skills/poteto-mode/playbooks/bug-fix.md` | `skills/poteto-mode/playbooks/bug-fix.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/feature.md` | `skills/poteto-mode/playbooks/feature.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/hillclimb.md` | `skills/poteto-mode/playbooks/hillclimb.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md` | `skills/poteto-mode/playbooks/multi-phase-plan.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/opening-a-pr.md` | `skills/poteto-mode/playbooks/opening-a-pr.md` | Exact |
| M | `pstack/skills/poteto-mode/playbooks/pause-safely.md` | `skills/poteto-mode/playbooks/pause-safely.md` | Exact |
| M | `pstack/skills/poteto-mode/playbooks/perf-issue.md` | `skills/poteto-mode/playbooks/perf-issue.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/refactoring.md` | `skills/poteto-mode/playbooks/refactoring.md` | Adapted |
| M | `pstack/skills/poteto-mode/playbooks/shipping.md` | `skills/poteto-mode/playbooks/shipping.md` | Exact |
| M | `pstack/skills/poteto-mode/scripts/check-plan.mjs` | `skills/poteto-mode/scripts/check-plan.mjs` | Exact |
| A | `pstack/skills/principle-explain-the-number/SKILL.md` | `skills/principle-explain-the-number/SKILL.md` | Adapted |
| M | `pstack/skills/principle-guard-the-context-window/SKILL.md` | `skills/principle-guard-the-context-window/SKILL.md` | Adapted |
| M | `pstack/skills/principle-never-block-on-the-human/SKILL.md` | `skills/principle-never-block-on-the-human/SKILL.md` | Adapted |
| M | `pstack/skills/principle-outcome-oriented-execution/SKILL.md` | `skills/principle-outcome-oriented-execution/SKILL.md` | Adapted |
| M | `pstack/skills/principle-prove-it-works/SKILL.md` | `skills/principle-prove-it-works/SKILL.md` | Adapted |
| M | `pstack/skills/principle-sequence-verifiable-units/SKILL.md` | `skills/principle-sequence-verifiable-units/SKILL.md` | Adapted |
| M | `pstack/skills/reflect/SKILL.md` | `skills/reflect/SKILL.md` | Adapted |
| M | `pstack/skills/reflect/references/divergent-reviewer.md` | `skills/reflect/references/divergent-reviewer.md` | Adapted |
| M | `pstack/skills/reflect/references/judgment-reviewer.md` | `skills/reflect/references/judgment-reviewer.md` | Adapted |
| M | `pstack/skills/reflect/references/tooling-reviewer.md` | `skills/reflect/references/tooling-reviewer.md` | Adapted |
| M | `pstack/skills/setup-pstack/SKILL.md` | `skills/setup-pstack/SKILL.md` | Adapted |
| M | `pstack/skills/show-me-your-work/SKILL.md` | `skills/show-me-your-work/SKILL.md` | Adapted |
| M | `pstack/skills/show-me-your-work/scripts/log.sh` | `skills/show-me-your-work/scripts/log.sh` | Exact |
| M | `pstack/skills/swarm/SKILL.md` | `skills/swarm/SKILL.md` | Adapted |
| M | `pstack/skills/tdd/SKILL.md` | `skills/tdd/SKILL.md` | Adapted |
| M | `pstack/skills/technical-writing/SKILL.md` | `skills/technical-writing/SKILL.md` | Adapted |
| M | `pstack/skills/typescript-best-practices/references/patterns.md` | `skills/typescript-best-practices/references/patterns.md` | Exact |
| M | `pstack/skills/unslop/SKILL.md` | `skills/unslop/SKILL.md` | Adapted |
| M | `pstack/skills/why/SKILL.md` | `skills/why/SKILL.md` | Adapted |

### Source verification

Targeted static checks confirmed all 161 upstream pstack paths plus the four Team Kit imports, all 53 comparison paths, the 165 original/local provenance hashes, 53 installed skill folders, and 56 skill entry frontmatters including dormant automation skills. Three upstream executable helpers remain byte-identical. JSON and source TOML parse, the configured Primary and child defaults are unchanged, and `git diff --check` passes. Local Markdown links resolve except the pre-existing `[PR #123](url)` illustration in the why synthesizer template and its historical mention above.

The bundled `quick_validate.py` could not start because the available Python lacks PyYAML. A direct check of the generated JSON-quoted YAML fields verified names, allowed fields, string types, lengths, descriptions, and host-entry links instead. No dependency was installed for this check. This is a targeted metadata check, not a claim that the bundled validator passed.

Static role-case inspection covers a known implementation (Luna with a concrete brief), prescribed evidence collection (Luna without diagnosis), unresolved judgment (bounded read-only Astra), authoritative document work (Astra), takeover progression and final cap, selected panels with actual count and models, unavailable models without substitution, both parent aliases, explicit model choices, and external/full-suite permission boundaries. No live model request, new-session behavior test, cloud workflow, or UI operation was performed.

## Normal business workflow and confirmed bug repair on 2026-10-05

The user clarified that authorized normal business work takes priority over speculative preventive prerequisites. The global rules now require evidence, scoped diagnosis and repair, and a rerun of the affected real workflow with targeted regression when an actual bug is encountered or reported. Only affected and dependent actions stop. A new mandatory validation gate requires a confirmed problem or an explicit current requirement, and a confirmed bug does not automatically require a gate. Existing required checks and safety, permission, and data-integrity boundaries remain in force before any bug occurs. CODEX.md refers to these global rules, and the bilingual introductions describe the same behavior. No runtime deployment or new-session behavior test was performed.

## Upstream v0.15.13 help and guide integration on 2026-10-06

This source revision absorbs all 16 pstack paths changed between `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a` and the official snapshot `77526ffa67f8dafc698d14b5356e6d4fc78c3127`. The active Codex manifest is `0.15.13+codex.20261006potetohelp`. The upstream Cursor manifest retains `0.15.13` as provenance material. The import contains 164 upstream pstack files and four unchanged Team Kit files, with 54 exposed skills.

`poteto-help` preserves the upstream question-to-skill, playbook, principle, and guide mapping. It reads the actual source before answering, gives at most one example prompt, and keeps usage help read-only. An explicit request to perform work routes through `poteto-mode` under the existing host contract. Its `agents/openai.yaml` preserves upstream explicit-only invocation through `allow_implicit_invocation: false`. Ambiguous help uses the available host clarification mechanism and its actual option limit. It does not copy Cursor tool arguments or force a five-option payload.

The guide retains the new prompting, read-only investigation, prototype, benchmark, verification, overnight, correction, and customization material. Host adaptations explain the existing GPT responsibility split and parent aliases, distinguish Cursor Custom Modes, cloud agents, Projects, and `/loop` from configured Codex capabilities, and preserve current permission and ownership boundaries. Help and guide task starts use the existing authoritative record for applicable phases, evidence, and material skip reasons without a copied playbook or a new ledger for simple tasks. The pause guidance preserves work, requires existing authorization for checkpoint commits, and makes user Stop immediate with no subsequent mutations. Daily maintenance, new verification infrastructure, prototypes, and panels are not automatic prerequisites. Existing checks and confirmed requirements still apply. No new planner, gate, timer, schedule, service, or review panel was introduced.

Local source links resolve against the adapted tree, including `UPSTREAM-README.md`. Public source links in help use the pinned upstream snapshot and identify Cursor documentation separately from local behavior. Global rules and `MODELS.md` are unchanged. The fresh-child lifecycle, thirty-minute takeover assessments, Luna to Sol to Astra progression, final automatic Astra `xhigh` cap, Primary-only ComputerUse, serial images, and separate packaging, release, and full-suite approval remain in force.

### Coverage of the 16 upstream changes

| Change | Upstream path under `pstack/` | Local destination | Treatment |
| --- | --- | --- | --- |
| M | `.cursor-plugin/plugin.json` | `.cursor-plugin/plugin.json` | Exact original |
| M | `README.md` | `UPSTREAM-README.md` | Adapted host and model explanations |
| M | `docs/guide/README.md` | `docs/guide/README.md` | Adapted host entry |
| M | `docs/guide/01-setup.md` | `docs/guide/01-setup.md` | Adapted setup, cost, verification, and persistence |
| M | `docs/guide/02-poteto-mode.md` | `docs/guide/02-poteto-mode.md` | Adapted persistence and isolation |
| M | `docs/guide/03-understand.md` | `docs/guide/03-understand.md` | Adapted host entry |
| M | `docs/guide/04-design.md` | `docs/guide/04-design.md` | Adapted comparison and document review boundaries |
| M | `docs/guide/05-build-and-clean.md` | `docs/guide/05-build-and-clean.md` | Adapted bundled tooling and discovery |
| M | `docs/guide/06-verify-and-ship.md` | `docs/guide/06-verify-and-ship.md` | Adapted verification scope, ownership, and maintenance |
| M | `docs/guide/07-overnight.md` | `docs/guide/07-overnight.md` | Adapted unattended work, review, and automation limits |
| M | `docs/guide/08-principles.md` | `docs/guide/08-principles.md` | Adapted host entry |
| M | `docs/guide/09-make-it-yours.md` | `docs/guide/09-make-it-yours.md` | Adapted authoring and evidence-based correction |
| M | `docs/guide/10-recipes-and-pitfalls.md` | `docs/guide/10-recipes-and-pitfalls.md` | Adapted inheritance and isolation |
| A | `skills/poteto-help/SKILL.md` | `skills/poteto-help/SKILL.md` | Adapted explicit-only help and host routing |
| A | `skills/poteto-help/references/prompting.md` | Same path | Adapted scope, design, and unattended-work advice |
| A | `skills/poteto-help/references/recipes.md` | Same path | Adapted permissions and local continuation example |

### Targeted source verification

All 168 original source records match the pinned Git source content, and every local hash matches the current bytes. The inherited provenance records include 145 CRLF Windows snapshots. Their recorded hashes remain unchanged, and their contents match the pinned blobs after LF/CRLF normalization only. Updated originals use raw Git blob bytes. `hash_semantics` now states this convention instead of implying that all historical snapshot hashes are raw blob hashes. All four Team Kit imports are unchanged at the new pin.

The installed skill-creator `quick_validate.py` passed for `poteto-help`; PyYAML is available in this session and no dependency was installed. Targeted YAML checks confirmed the new frontmatter and explicit-only metadata. Both manifests parse and carry the intended versions. All 309 local file links in the affected guide, help, README, and host-entry Markdown resolved, and `git diff --check -- pstack` passed. The focused checks are reproducible with `python work/upstream-absorb-20261006/check_source.py` in this working tree; that scratch verifier is not part of the plugin. Git reported only the existing checkout policy that may convert LF text to CRLF.

Static review confirmed that a usage question only reads the needed source, an explicit work request uses the existing workflow, a bare invocation does not execute a suggested example, and model questions resolve through local `MODELS.md`. These are source checks, not a new-session behavior evaluation. This phase did not deploy, install, commit, push, package, release, run a full test suite, invoke an evaluation, or change a live model configuration. Deployment and fresh-session behavior remain separate acceptance evidence.

## Narrow Astra routing on 2026-10-06

This revision supersedes the earlier broad routing of authoritative technical documents and ordinary unresolved consultations to Astra. The user approved Sol as the direct default for ordinary technical judgment after reviewing recent child assignments. The supplied audit counted 30 requested child calls: 23 Luna, seven Astra, and no Sol. All seven Astra calls concerned rules, documents, or adaptation rather than an unresolved Sol attempt. Those counts describe the supplied audit sample, not cost or a quota prediction.

Global AGENTS.md now routes ordinary proposals, implementation plans, local designs, routine adaptation of existing rules or upstream material, and ordinary unresolved questions directly to Sol at `xhigh`. No failed Luna attempt is required. Astra at `high` remains responsible for new or substantively changed master or system architecture, key interface or data contracts, consequential design tradeoffs, a problem unresolved after an actual Sol attempt, or an explicit task-specific model request. A technical-document label or Primary uncertainty alone does not qualify. Critical design work has no mandatory Sol prerequisite.

Luna keeps specified implementation, routine operations, prescribed evidence collection, and mechanical or exact accepted-content edits that preserve meaning, including edits to critical documents. Luna does not settle design decisions or alter contracts. After an Expert finishes and its conclusion is accepted, straightforward bounded follow-ups use Luna and new ordinary technical choices use Sol. An active takeover remains with its owner through diagnosis, implementation, and verification. Direct Sol assignments receive the existing thirty-minute assessment. The failure sequence, final automatic Astra `xhigh` cap, external-blocker rules, ownership, explicit selections, permissions, and host tool boundaries remain unchanged.

The source overlay updates AGENTS.md, the injected developer instructions and base prompt, the three existing role definitions, CODEX.md, MODELS.md, and the affected pstack help, how, architect, reflect, mode, guide, and introduction text. Role IDs, configured Primary and child defaults, the upstream workflow phases, and the plugin version remain unchanged. Existing provenance records keep their original hashes and the 145-snapshot CRLF convention. Seven edited imported files receive new exact local hashes and adaptation notes. Earlier entries in this log remain historical evidence.

### Targeted source verification

Four TOML files parse. A comparison against the preceding source revision confirms unchanged model defaults, role IDs and pinning, and configuration outside the routing instructions and advisor description. The injected and base-prompt routing paragraphs match. Seven unrelated global sections are unchanged, including authorization, normal business workflow, bug repair, ownership, and source management. The old blanket document trigger and renamed-heading references are absent from current operative text; earlier ADAPTATION.md entries retain the previous policy as history.

The existing `work/upstream-absorb-20261006/check_source.py` verifier passes all 168 original and local hash pairs, including 145 historical CRLF snapshots, both unchanged manifest versions, and 309 guide and help links. A separate focused check resolves all 176 local file links in the edited pstack documents. The installed skill-creator `quick_validate.py` passes for all five changed skills: architect, how, poteto-help, poteto-mode, and reflect. The validator used the existing PowerShell Python environment; no dependency was installed. `git diff --check` passes.

| Source case | Result |
| --- | --- |
| Ordinary technical proposal or implementation plan | Direct Sol at `xhigh`; no Luna failure required. |
| New or substantively changed master or system architecture | Direct Astra at `high`; no Sol prerequisite. |
| Routine help, existing-rule, or upstream adaptation | Sol; exact accepted wording uses Luna. |
| Mechanical link, version, or wording edit in a critical document | Luna when meaning stays unchanged. |
| Primary uncertainty about an ordinary question | Primary judgment or optional Sol consultation; uncertainty alone does not trigger Astra. |
| Problem unresolved after an actual Sol attempt | Fresh Astra at `high` with the attempt's evidence. |
| Active Senior Executor or Expert takeover | The owner completes diagnosis, implementation, and verification within scope. |
| Credentials, access, permissions, or unavailable services | External blocker; no reasoning escalation. |

These are source and static routing checks. This revision does not deploy, install, commit, push, package, release, run a full suite, invoke a model evaluation, or change instructions already loaded in the current chat. Installed behavior and new-session routing remain unverified.

## Start Sol at medium and upgrade effort in order on 2026-10-06

This revision supersedes the preceding Sol `xhigh` starting default. The user explicitly selected Sol `medium` for direct ordinary technical work, local designs, routine rule or upstream adaptation, ordinary consultations, and Senior Executor takeovers after Luna cannot resolve a problem. The Default Sol Primary remains `gpt-6.1-sol` at `high`. Luna remains `gpt-6-luna` at `max`.

On actual inability or an unresolved thirty-minute assessment, transfer the bounded problem to a fresh child in this order: Sol `medium`, Sol `high`, Sol `xhigh`, Astra `high`, then Astra `xhigh`. Ordinary work requires evidence of the preceding Sol attempts before Astra. Do not skip from Sol `medium` or `high` to Astra. Advance immediately when an attempt cannot resolve the problem and stop when successful. Automatic escalation uses neither Sol nor Astra at `max` or `ultra`.

Each model-and-effort tier has thirty minutes from its first delegation. Same-tier replacements do not reset the deadline. A new tier receives its own window. Before each transfer, release the previous owner and its processes. Preserve a concise handoff with evidence, failed approaches, paths, missing evidence, total elapsed time, active owner, processes, and the tier deadline. Healthy long jobs continue their existing observation loop. Access, authentication, permissions, and unavailable services remain external blockers.

Critical architecture, key contracts, and consequential design tradeoffs still qualify for direct Astra `high`. Explicit task-specific user model and effort selection remains authoritative. Optional consultations preserve read-only scope throughout every effort and model upgrade. After an Expert finishes and its conclusion is accepted, straightforward follow-ups use Luna and new ordinary technical choices start at fresh Sol `medium`. An active takeover retains the assigned problem through diagnosis, implementation, and verification. Authorization, business-workflow and bug-repair boundaries, Primary-only ComputerUse, serial image work, and fresh-child ownership rules remain unchanged.

The source overlay changes AGENTS.md, the injected developer instructions, the base prompt, the existing Astra advisor description and instructions, CODEX.md, MODELS.md, and the affected how, poteto-help, and reflect skill instructions. Three imported skill files receive updated local hashes and a new adaptation note. Original upstream hashes and the historical 145-snapshot CRLF convention are preserved. Previous log entries remain historical evidence. No runtime deployment copy, manifest version, source script, live model configuration, timer, service, quota gate, or verification framework is changed.

### Targeted source verification

Four TOML files parse. Comparison with the preceding revision confirms unchanged Primary and child defaults, role IDs, and model pinning. The injected routing paragraphs match the base prompt. Focused assertions confirm direct Sol `medium`, Luna failure to Sol `medium`, Sol `medium` to `high`, Sol `high` to `xhigh`, Sol `xhigh` to Astra `high`, critical-design direct Astra, external-blocker handling, and read-only scope preservation. Current operative text has no old Sol `xhigh` starting rule or unrestricted earlier-Sol-attempt bypass to Astra.

The existing `work/upstream-absorb-20261006/check_source.py` verifier passes all 168 source and local hash pairs, 145 historical CRLF snapshots, 54 exposed skills, unchanged manifest versions, and 309 guide and help links. Its older expected Codex manifest version was replaced with the actual unchanged source version only in the in-memory invocation. The verifier file was not edited. The installed skill-creator validator passes for all three changed skills. `git diff --check` passes.

These are source and static routing checks. They do not demonstrate model request routing or a fresh session applying the policy. This revision does not deploy, install, commit, push, package, release, run a full test suite, or change instructions already loaded in the current chat.

## Normal workflow reuse, observation, and recurrence handling on 2026-10-06

This source-only revision folds the approved points into normal task start, execution, and completion. AGENTS.md supplies the global decisions. CODEX.md applies them within the selected upstream phases and adds the relevant observation path to assignment briefs. Poteto mode points to those shared steps and bounds the Build the Lever and Encode Lessons in Structure triggers. Playbook phase order remains unchanged.

At task start, current context guides reuse of verified scripts, CLIs, and business entry points. Actual repeated deterministic steps can justify minimal tooling for the current authorized need. No project inventory, universal preflight, or new-script deliverable is required. During execution, the assigned owner observes the actual result through existing runs, logs, UI, or business entry points. An observed failure is distinguished from missing tools, feedback, environment, inputs, or ownership before model escalation. An authorized gap is resolved or reported without blocking independent work or adding an observability framework.

Normal completion uses evidence already collected to notice repeated actual errors and judge a small improvement within the authorized scope. Unrelated findings or work requiring new scope get a short note in the existing project record. No history scan, new ledger, automatic reflection, correction, panel, or special report for a task without such errors is required. Read-only requests remain read-only. Existing gate, Stop, approval, owner, ComputerUse, serial image, and model escalation rules remain unchanged.

The source review found no conflicting lifecycle instructions in config/workflow.toml, prompts/codex-event-driven-base.md, or agents/*.toml. Their existing model and ownership instructions remain unchanged. The poteto-mode local hash and adaptation note are updated in provenance.json. Original upstream hashes and historical entries are preserved. No version, script, runtime copy, hook, service, or runtime enforcement is introduced.

### Targeted source verification

The installed skill-creator validator passes for poteto-mode. The existing source verifier passes 168 source and local hash pairs, 145 historical CRLF snapshots, 54 exposed skills, unchanged manifest versions, and 309 guide and help links. Its old Codex version expectation is replaced with the actual unchanged source version only in memory. The verifier file is unchanged. Focused checks also resolve all CODEX.md and poteto-mode local links, preserve original upstream hash tuples, confirm unchanged model, prompt, role, and manifest files, and parse all four TOML files. `git diff --check` passes.

A source-level review covers reuse of an existing CLI without a new gate, missing result feedback before escalation, a scoped improvement for a repeated confirmed bug, an unrelated finding recorded without cleanup, completion without an error report, and a read-only request without edit authorization. These are static instruction checks, not agent-behavior evaluations or evidence of a new session following the workflow. No deployment or full test suite is run.

## Explicit Primary coordinator role entry on 2026-10-06

The Primary reads `COORDINATOR.md` when the user says "你是总控代理" or clearly assigns the same role, and retains that role through later turns of the same task until the user changes it. `AGENTS.md` and `CODEX.md` index this single host guide; existing global rules, host instructions, model mappings, and selected upstream phases remain authoritative.

This source adaptation adds one host guide and its indices, plus a local plugin version bump. It does not change upstream playbooks, model mappings, prompts, scripts, or provenance. Targeted source checks (`git diff --check`, manifest JSON and workflow TOML parsing, local links, and change-scope checks) passed. These are source checks; new-session behavior has not been exercised.

## Coordinator pickup, feedback, and acceptance on 2026-10-06

The accepted failure evidence identified transient cross-chat corrections, a Luna jumping assignment that exceeded 46 minutes without the required assessment handoff, and nominal UI acceptance despite overflowing log rows and an incorrect game viewport aspect ratio. CODEX.md and COORDINATOR.md now restore task context from the existing authoritative record, persist material corrections through its owner, and preserve pending design status and permissions. Assignment briefs name an available observation and result-return route, its feedback owner, and the tier's first-start time and deadline. Due assessments precede waits and resumed work. Healthy jobs, resource waits, and missing feedback remain distinct from unresolved reasoning. Authorized supported collection can replace an unavailable cross-chat send route. Internal final handoffs need no redundant status reports.

Primary acceptance compares the actual output with the latest accepted requirements and reference, retains unmet items, and reports mismatches and unverified promises. A conflicting test oracle requires minimal authoritative production evidence before implementation or assertions change. Credible prior RED, GREEN, and production evidence remain reusable. The selected upstream phase order, escalation paragraph, model mappings, resource ownership, fresh-child rules, and permissions remain unchanged. No new record, timer, hook, framework, or acceptance gate is added.

Targeted checks passed with `git diff --check`, an exact allowed-file and untracked-file scope check, resolution of all four local Markdown links in the affected host guides, and focused static assertions for pickup with pending corrections, due assessments, healthy resource waits, unavailable cross-chat sending, actual viewport or log mismatches despite proxy success, and a conflicting test oracle. These are source instruction checks, not agent behavior evaluations. Only CODEX.md, COORDINATOR.md, and this log changed. No deployment, version change, runtime or cache edit, commit, packaging, release, or full test suite was performed. New-session pickup, live deadline handling, and actual UI acceptance behavior remain unexercised.

## Interim environment-bound reader evidence (historical) on 2026-10-06

The goal is executable pickup from an explicitly selected current task record and measured acceptance evidence for the reported game-frame-ratio and log-overflow failures. The accepted Expert direction keeps pickup in a host SessionStart hook. The selected upstream Feature workflow uses the how phase for its use instructions and ordinary Sol for local adaptation. Two independent workstreams covered the hook and layout helper, with read-only host evidence kept separate. The event instructions and schema were the shared first dependency. The hook stayed coupled to its tests, layout checks stayed separate, and one owner held the shared documentation files. Architecture candidates or a panel, commit or PR, deployment, and a full suite were outside this authorized phase. No independent verdict is claimed.

The hook's offline results contain 36 cases across positive and negative inputs. Layout checks contain 18 cases. A generated expression was also executed against an isolated headless Playwright Chromium fixture on `about:blank`, with no external resources. The accepted ratio passed with a -0.00716 px height error. A 16:9 ratio failed with a 0.16471 px error. A 200-character row without wrapping failed with `row-scroll-overflow` and `text-overflow` while horizontal log overflow remained 0. The rendered fixture validates the expression and checker against that fixture only. It does not establish target-page behavior.

Read-only host evidence recorded Codex 26.930.7945.0 and matching source and cache version 0.15.13+codex.20261006coordinator. The runtime deployment mirror and cache for that version had no hook declaration, and the observed host configuration had no hook event or feature-enable flag. This is an absent-hook observation, not evidence that the host lacks hook support.

At this initial checkpoint, the environment-variable binding was an interim reader mechanism, not supported automatic integration or a user-maintained setup step; the per-session binding contract was still pending then. Actual host startup, resume, and compact invocation remain unverified. The historical mock wireframe receipt provides a ratio but omits row and text measurements, so it cannot establish target-page log behavior. No target browser or runtime resources were touched. This work activates no hook, heartbeat, timer, controller, or database and makes no deadline or reporting guarantee.

For this task, the Primary owns the source work and reports directly to the specified coordinator. The human-authorized destination is coordinator chat `01a11136-4c8c-7211-aa5d-4246ad3ad14c`; a checkpoint was delivered there successfully with `send_message_to_thread`. The coordinator owns coordination across workstreams, approval, and final acceptance. Authorization covers that recipient only and does not allow periodic unchanged messages. Restore points are `pstack/hooks/hooks.json`, `pstack/hooks/session_start.py`, `pstack/tools/layout-check.mjs`, `work/session-context-20261006/results.json`, `work/layout-check-20261006/summary.json`, `work/layout-check-20261006/rendered-fixture-summary.json`, and `work/host-hook-evidence-20261006/receipt.json`. Existing dirty source edits remain intact, and no other project was changed.

## Owner-record current-region contract and bounded activation on 2026-10-06

The accepted Expert contract replaces the interim environment-variable selector in the source instructions. A `SessionStart` event selects from a bounded index at the actual `cwd/AGENTS.md`, validates metadata on at most eight declared existing records, and returns only the current body from exactly one record whose opaque session ID and normalized absolute workspace match. The body is marked in place and preserved as untrusted task data; it is not summarized or duplicated. The complete schema, field and byte limits, diagnostics, and no-fallback rules are in `pstack/hooks/README.md`; `pstack/CODEX.md` points to that contract. The README's backend example points to the existing `INTEGRATION_TASKS.md` record and `pstack-current-backend`; its frontend example points only to existing `FRONTEND_TASKS.md` and `pstack-current-frontend`. They are preparation examples, not edits to those owners' records. Session IDs remain null and workspace paths remain placeholders until an actual event is observed. The mxdzs source and worktree paths are ownership references only.

The source owner reports 92 targeted subprocess cases passed with `py -3 pstack/hooks/test_session_start.py`; the owner's handoff and result receipt are `work/session-context-20261006/source-handoff.md` and `work/session-context-20261006/results.json`. The documentation takeover reviewed the production reader, default declaration, handoff, and result receipt against this contract without rerunning the accepted 92 checks. Coverage includes large metadata files, two sessions, canonical and worktree separation, untrusted pending text, byte limits, reparse rejection, and deterministic mutations. The earlier 36-case environment-variable result is historical initial-reader evidence only and is not a pass for this contract. Earlier layout evidence includes 18 checks and three rendered `about:blank` fixture cases; they exercise the helper and fixture, not the target page. The human has accepted the latest wireframe layout, while log-button classification remains under review. The frontend owner owns saving the newest accepted and pending decisions in the existing current checkpoint; this entry points to that checkpoint without copying or freezing its contents.

The host-binding gap remains: no real event `cwd` or owner binding has been captured, and the current projectless session directory differs from the canonical source worktree. The earlier read-only host evidence found no hook declaration in the then-observed runtime mirror/cache and no event enablement in the observed host configuration; it does not prove that the host lacks support. No owner `AGENTS.md` or task record was changed, no hook was deployed or trusted, and no live startup, resume, compact, or target-page behavior is claimed. A new chat in a non-project `cwd` without a binding, or a subdirectory without its own valid index, remains `SOURCE GAP`; a child sharing its parent's event session ID does not become the Owner. Record content and IDs grant no role, contact, messaging, execution, or permission authority.

Activation remains a bounded future plan only: obtain approval for the plugin version/cachebuster and `scripts/sync.py deploy`, then obtain separate authorization to review and trust the installed hook. A separately prepared one-event probe, disabled by default, can capture only necessary event fields and a boolean for whether the transcript path is null after scoped authorization. Pair a natural owner startup, resume, or compact observation with the known Desktop thread ID, timestamp, installed version, and installed and source hashes. Do not assume ID equivalence or retain or read a transcript path. Natural resume and compact observations must establish session and workspace stability. Bind the real values in the existing owner record, then verify the exact current body and preserved pending status in the next host context; a mismatched binding must yield a diagnostic. Do not restart business processes, force compaction, open test chats, or add manual variables. No `PreToolUse`/`Stop`, scheduler, controller, timer, or deadline guarantee is introduced.

Local documentation checks passed: `git diff --check` for tracked edits, a no-index whitespace check for the new README with no diagnostics, and resolution of all three local Markdown links. Hook-source results remain the source owner's reported evidence; live host binding, deployment/trust, and target-page acceptance remain unverified.

The separately prepared probe passed five targeted `unittest` cases, including multiple input subcases. The Windows compact-event example `pstack/hooks/session-probe.example.json` passed JSON parsing. The formal source default remains `pstack/hooks/hooks.json`; neither the manifest nor that default references the probe example. No Owner record or host configuration was changed, and no host effect is claimed. The existing test receipt is `work/host-hook-evidence-20261006/probe-results.json`.

## Cross-chat feedback and internal waits, 2026-10-06

The coordinator reported repeated `wait_threads` calls with `timeoutMs: 120000` and `afterCursor` across independent Desktop chats. Each timeout returned unchanged status and the latest assistant message. The cursor did not prevent repeated context. The generic wait and no-event renewal wording in the global rules, CODEX.md, and COORDINATOR.md could be applied to that separate contact route. The injected developer instructions and base prompt contained the same generic wording. No equivalent clause was found in the named agent configurations.

The source rules now limit `collaboration.wait_agent` long waits and no-event renewal to internal children. Independent top-level chats use an actually available, authorized proactive report route. Read or wait calls remain available for necessary bounded result collection, acceptance, a concrete assessment deadline, or a missing report route, with cursors and minimal output. A timeout alone supplies no failure evidence and does not justify another cross-chat wait, a status query, or a history reread. Due assessments take precedence. Messaging authorization, resource ownership, model routing, healthy-job observation, and external-blocker handling remain unchanged. No automatic closed-chat wakeup, timer, deployment, trust change, or runtime deadline guarantee is introduced.

Targeted static review covers six scenarios. An internal child with no actionable event renews a long wait bounded by its remaining assessment time. An independent Main with a report route and unchanged status does not start repeated waits. A missing report route permits necessary bounded authorized collection. A due assessment triggers assessment rather than repeated two-minute polls. A timeout does not prove failure or trigger a query on its own. Closed chats receive no automatic wakeup, and source edits grant no deployment, trust, or runtime enforcement. These are source-rule coverage checks, not proof of actual future agent behavior. The bounded receipt is `work/pstack-executable-20261006/cross-chat-rule-results.json`. The existing source handoff artifacts include the complete tracked working diff and all eleven untracked hook and tool files. The three document edits already present at assignment start are preserved; this change adds only the feedback-scope clauses and this evidence note. The prior reader, layout, probe, and browser-fixture results are reused without rerunning them.
