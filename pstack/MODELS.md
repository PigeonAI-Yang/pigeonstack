# Model selection for this host

Updated 2026-10-27. Before using this file, read [CODEX.md](CODEX.md) and the global `AGENTS.md` it identifies. Global policy determines assignment eligibility, takeover triggers, progress assessments, and authorization; `CODEX.md` supplies briefs and tool mechanics. This file owns workload choices, exact model IDs, reasoning effort, configuration, and model-availability evidence. Reuse unchanged instructions already read in this session. Upstream role defaults do not apply.

## Workload selection

Execute directly in the active Primary by default. Model selection and delegation are separate decisions. This menu applies when the user selects a task model, asks for a model recommendation, or explicitly authorizes assignment routing. It does not switch the current Primary, change its reasoning effort, or create an agent. Preserve every explicit task-specific selection. An authorized delegation without a selected alternative retains the Sol defaults below.

| Workload | Preferred model or candidate | Effort for a new selection |
| --- | --- | --- |
| Complex everyday development: diagnosis, implementation, integration, and verification | `gpt-6.1-sol` | `high` as a recommended coding Primary; `medium` as the ordinary delegated default. |
| Visual and interface understanding, natural writing, supplied-material reports, defined computer workflows, and scoped code fixes | `gpt-6.1-terra` | Start a new ordinary task at `medium`; retain any explicit effort, including an existing Primary at `max`. |
| Clearly scoped engineering, Python tools, offline pipelines, tests, and features within established interfaces | DeepSeek V4.1 Flash, using an exact route below | Use the selected route's current default, observed as `max` on 2026-10-27, unless the user specifies another supported effort. |
| Image-and-text materials, screenshot-assisted interface work, document workflows, and clearly scoped development | GLM 5.3 Flash, using an exact route below | Use the selected route's current default, observed as `max` on 2026-10-27, unless the user specifies another supported effort. |
| Key architecture, interface contracts, consequential tradeoffs, and eligible unresolved problems | `gpt-6-astra` | `high`, with the existing eligibility and escalation rules below. |
| Simple repetitive work with fixed steps and directly checkable results | `gpt-6-luna` | `max`; preserve its existing narrow scope. |

DeepSeek and GLM are candidates for complete, bounded engineering assignments, including diagnosis, implementation, and relevant checks within the brief. Their names do not restrict them to Luna's mechanical role. These workload choices are based on documented capabilities, not a measured ranking on this user's repositories. Keep the existing evidence-based takeover sequence; these candidates add no automatic intermediate tier or parallel panel.

For native computer use, the selected model must be the Primary with the actual host capability. A child cannot inspect screens, click, type, or proxy computer use. Terra's visual capability grants no exception. Image viewing and analysis retain the shared serial resource rule. Terra accepts image input; direct audio or video input is not established by its API model specification. Reuse existing extraction or transcription workflows when those inputs are needed.

### Exact third-party routes

The host catalog exposed these entries on 2026-10-27. Preserve spelling and case; a route is a service channel, not a distinct model family or verified backend snapshot.

| Model family | Exact exposed route IDs |
| --- | --- |
| DeepSeek V4.1 Flash | `auto/deepseek-v4.1-flash`, `opencode-go/deepseek-v4.1-flash`, `opendesign/deepseek-v4.1-flash`, `workbuddy/deepseek-v4.1-flash` |
| GLM 5.3 Flash | `auto/GLM-5.3-Flash`, `zcode/GLM-5.3-Flash`, `zcode/GLM-5.3-Flash-Trial`, `workbuddy/glm-5.3-flash` |

Those routes expose `low`, `high`, and `max`; do not pass `medium` by copying a GPT brief. For the GPT models, use only the current tool's accepted values. The official Terra API also supports `none`, while this host's inspected catalog did not expose it. API capabilities, host settings, and different providers' effort labels are separate facts.

The inspected native subagent tool exposed Terra and other GPT models, but not these DeepSeek or GLM IDs. The existing-chat model-selection interface and model catalog exposed the third-party routes. Select only an entry supported by the intended interface; never pass an unsupported route to native spawn, fabricate a catalog entry, launch an external executor, or message or create another chat to work around that limit. Those operations need their own applicable human authorization. A catalog entry alone does not prove successful inference, backend model identity, latency, cost, or quota consumption.

Official capability references: [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection), [Terra model](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [DeepSeek V4.1 Flash](https://api-docs.deepseek.com/news/news260910/), [DeepSeek 1017 update](https://api-docs.deepseek.com/news/news261017/), and [GLM models](https://autoclaw.z.ai/models/). DeepSeek's official `deepseek-flash` API alias currently points to V4.1-Flash-1017; the third-party route names above do not establish that same snapshot. Reuse credible task evidence and compare models only within an authorized scope. No trial request is required merely to document these choices.

## Model and effort mapping

The active Primary executes directly by default, including diagnosis, implementation, verification, and critical design. Apart from the recommended coding Primary row, this table retains the default assignments for subagents only after an explicit user request authorizes delegation for the current task. Consultations, reviewers, and failure takeovers share that condition. Skill selection, role names, complexity, and failures grant no permission to create an agent or switch the Primary. The workload menu adds explicitly selected alternatives; it does not change existing role configurations, the default Sol executor, or the existing takeover IDs and efforts.

| Assignment | Model | Reasoning effort |
| --- | --- | --- |
| Recommended Sol Primary | `gpt-6.1-sol` | `high` |
| Luna mechanical helper: simple repetitive work only | `gpt-6-luna` | `max` |
| Default Sol executor, ordinary consultation, or initial failure takeover | `gpt-6.1-sol` | `medium` |
| First automatic Sol upgrade, using a fresh child | `gpt-6.1-sol` | `high` |
| Final automatic Sol upgrade, using a fresh child | `gpt-6.1-sol` | `xhigh` |
| Initial Astra Expert takeover | `gpt-6-astra` | `high` |
| Final automatic Astra escalation, using a fresh child | `gpt-6-astra` | `xhigh` |
| Bounded delegated ordinary judgment, proposal, plan, local design, or rule adaptation | `gpt-6.1-sol` | `medium` |
| New or substantively changed master or system architecture, key contracts, and consequential design tradeoffs, including substantive review | `gpt-6-astra` | `high` |
| Initial read-only Astra consultation on critical design or a question unresolved after an actual Sol `xhigh` attempt | `gpt-6-astra` | `high` |

For explicitly authorized delegated work, Sol at `medium` is the default for ordinary implementation, debugging, refactoring, integration, verification, operations, and prose. A Sol executor may diagnose, select a local solution, implement, and verify within its assigned scope. A separately assigned consultation remains read-only. Luna at `max` is limited to simple, highly repetitive mechanical tasks with a fixed procedure and directly checkable results, such as exact batch replacements, formatting, or running the same known check across a fixed list. An accepted plan, small task, or routine command alone does not qualify work for Luna. Do not split a coherent Sol assignment into Luna microtasks or automatically send accepted consultation results back to Luna. Primary uncertainty alone does not justify Astra. Critical design work can go directly to Astra under global policy. On evidenced inability, continue in order through Sol `medium`, `high`, `xhigh`, Astra `high`, and Astra `xhigh`; eligible Luna failures enter at Sol `medium`. Thirty-minute assessments do not trigger escalation by themselves. Preserve permissions, read-only scope, total elapsed time, evidence, and exclusive ownership.

Luna may apply only simple repetitive mechanical wording, link, version, formatting, or exact accepted-content changes using a fixed procedure. Luna must not settle design choices or alter contracts. After an accepted Expert conclusion, ordinary follow-up uses Sol; the same narrow mechanical exception applies to Luna. New critical decisions, actual Sol `xhigh` inability, and explicit task-specific selection retain the Astra route. Active takeovers remain with their owner through completion.

Automatic escalation stops at Astra `xhigh`; productive execution does not. Keep the same Expert while substantive progress and a concrete next step remain. Only demonstrated inability to proceed requires a limit report and Primary decision. Do not restart the escalation cycle or automatically use Sol or Astra at `max` or `ultra`. Global AGENTS.md owns the progress assessment and transfer conditions.

Explicit task-specific user model and effort selection takes precedence within actual tool and access limits. The cap governs automatic escalation, not an explicit task-specific selection. Critical design work also preserves explicit task-specific user selection. These defaults do not switch the active Primary. Luna does not support `ultra`.

For explicit spawn arguments, pass the table's ID as `model` and its effort as `reasoning_effort`. Follow the role and history constraints in `CODEX.md`. Global `AGENTS.md` defines the takeover sequence only within explicit user authorization and defines when it stops; this table grants no additional escalation or mutation authority.

## Upstream role mapping

These are conditional responsibility mappings, not delegation permission or a second routing engine. Every upstream role is resolved here before spawning. Without an explicitly selected workload alternative, missing role configuration uses this table, never an upstream Grok, Claude, or retired GPT default. A selected Terra, DeepSeek, or GLM assignment retains the same scope, evidence, ownership, and read-only boundaries. Complexity alone does not change the tier. Lists for explicitly selected candidate or review workflows name separate assignments, not automatic permission to create a panel.

Ordinary Sol mappings include scoped diagnosis, implementation, and verification. Read-only consultations remain read-only; accepted implementation defaults to Sol. The narrow Luna mechanical-work exception applies to every upstream role.

| Upstream role | Assignment on this host |
| --- | --- |
| `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb` | Sol owns assigned ordinary diagnosis, implementation, and checks; the Primary owns goals and final acceptance. Luna handles only simple repetitive mechanical steps. |
| `judgment and prose` | Terra is the preferred selectable candidate for natural writing and visual-material reports. Sol remains the default for ordinary planning and technical document work without another selection. Luna may apply only simple repetitive exact changes. Astra handles eligible critical design. |
| `hardest tasks` | No difficulty-based model override. Apply the same responsibility split and evidence-triggered takeover sequence. |
| `how explorer`, `why investigators` | Sol collects and interprets evidence or investigates the assigned question. Luna is limited to fixed repetitive collection. Astra eligibility follows global policy. |
| `how explainer`, `why synthesizer` | Primary explains and synthesizes. Ordinary technical documents use Sol and critical design work uses Astra. Do not add a redundant agent merely for this label. |
| `reflect tooling` | Sol handles ordinary tool investigation and existing-rule adaptation. Luna is limited to fixed repetitive collection or exact edits. New critical design uses Astra. |
| `reflect judgment, divergent, synthesizer` | Primary normally judges and synthesizes. An explicitly selected review uses scoped Sol read-only assignments for ordinary judgments and existing-rule adaptation. Astra requires critical design, an actual unresolved Sol `xhigh` attempt, or explicit user model selection. Authorized edits are a separate responsibility. |
| `swarm workers` | Sol executes ordinary bounded assignments. Luna is eligible only for simple repetitive mechanical work. Races still require explicit workflow selection and supported models. |
| `architect runners` | Within an explicitly selected comparison, Sol handles ordinary designs and implementation; Astra handles critical architecture and contract decisions. Luna may perform fixed repetitive input collection or exact edits only. |
| `arena runners` | Sol develops and implements ordinary candidates; Astra handles critical design candidates. Luna may perform simple repetitive mechanical steps only. |
| `arena cross-judge pool`, `interrogate reviewers` | Only an explicitly selected independent review. Sol reviews ordinary technical work. Astra reviews critical design or a question unresolved after an actual Sol `xhigh` attempt, or follows explicit user model selection. Primary performs final acceptance. State the actual candidate count and models; do not claim different model families when all use GPT. |

Map combined upstream roles to the assigned scope. Sol may own ordinary diagnosis through implementation and verification; separate consultations remain read-only and critical decisions retain the Astra boundary. Preserve workflow phases and evidence, not upstream model defaults or unrestricted agent briefs. If an explicitly selected panel cannot meet required independence, scope, or model availability, report that missing verdict instead of fabricating it or silently substituting another model.

## Parent aliases and setup

`auto` and `inherit-parent` mean the actual active parent's model and reasoning effort. Resolve both from the supported session configuration, then pass explicit `model` and `reasoning_effort` with compatible history arguments. A host-supported inheritance mode is also valid only when it demonstrably preserves both. Omitted model arguments alone are not inheritance on this host: ordinary children default to Sol at `medium`. Explicit Luna assignments require `gpt-6-luna` at `max` and an eligible simple repetitive task. If the actual parent values or a supported route cannot be established, report the gap before spawning that role.

Those bare parent aliases are distinct from exact provider route IDs such as `auto/deepseek-v4.1-flash`, `auto/GLM-5.3-Flash`, and `auto/auto`. A provider's `auto` group is not parent inheritance and does not authorize switching model families or channels.

Aliases select model values, not assignment permissions. They do not turn a Luna execution role into an investigator or authorize a panel. Preserve the active Primary. Setup does not restart it or claim that a disk edit changed its model.

`/setup-pstack` reads this file and the actual host configuration, proposes only user-requested GPT model or effort changes, and writes accepted choices here. Do not restore upstream family defaults, parse effort from model-name suffixes, lower all roles with a generic budget preset, or erase a local role because upstream retired its label. Preserve explicit task-specific choices and the automatic escalation cap. Report unavailable required values without retries, substitution, or a repair PR. An unavailable requested target can be documented in an inactive profile as described below.

## Active configuration and availability

The active `config.toml` and selected profile determine the configured Primary. The coding recommendation, checked-in `config/workflow.toml`, live configuration, and active session selection can differ intentionally. Do not reconcile them during rule maintenance. The 2026-10-27 inspection found the live configuration at `gpt-6.1-terra` / `max`; this revision preserves that file and does not switch a running session. Use CODEX.md's narrowest deployment scope, `--plugin-only` for this model-document update, and verify that configuration bytes are unchanged. Ordinary child defaults in the maintained configuration remain Sol at `medium`; verify the actual interface before claiming the host uses them. Luna mechanical helpers, critical Astra work, and takeovers retain their explicit arguments.

Verify actual session routing before reporting model use. A disk edit, model label, cached catalog, or model self-identification does not prove a server-side model mapping. If the required model or effort is unavailable, report the limit under the global no-substitution rule.

Before activating new defaults, verify exposed model IDs and a successful request within the user-authorized validation scope. A setup request alone does not authorize a trial subagent call. An explicitly requested but unavailable model may be documented as a target and saved in a named, inactive profile. Preserve working defaults and report the gap. Do not fabricate catalog entries or retry access denials. Follow `CODEX.md` for authorized source edits and deployment.
