# Model selection for this host

Updated 2026-10-06. Before using this file, read [CODEX.md](CODEX.md) and the global `AGENTS.md` it identifies. Global policy determines assignment eligibility, takeover triggers, deadlines, and authorization; `CODEX.md` supplies briefs and tool mechanics. This file owns exact model IDs, reasoning effort, configuration, and model-availability evidence. Reuse unchanged instructions already read in this session. Upstream role defaults do not apply.

## Model and effort mapping

| Assignment | Model | Reasoning effort |
| --- | --- | --- |
| Default Sol Primary | `gpt-6.1-sol` | `high` |
| Luna Executor | `gpt-6-luna` | `max` |
| Initial Sol ordinary consultation or failure takeover | `gpt-6.1-sol` | `medium` |
| First automatic Sol upgrade, using a fresh child | `gpt-6.1-sol` | `high` |
| Final automatic Sol upgrade, using a fresh child | `gpt-6.1-sol` | `xhigh` |
| Initial Astra Expert takeover | `gpt-6-astra` | `high` |
| Final automatic Astra escalation, using a fresh child | `gpt-6-astra` | `xhigh` |
| Bounded delegated ordinary judgment, proposal, plan, local design, or rule adaptation | `gpt-6.1-sol` | `medium` |
| New or substantively changed master or system architecture, key contracts, and consequential design tradeoffs, including substantive review | `gpt-6-astra` | `high` |
| Initial read-only Astra consultation on critical design or a question unresolved after an actual Sol `xhigh` attempt | `gpt-6-astra` | `high` |

Bounded ordinary consultations start at Sol `medium` without a Luna failure. Known execution stays with Luna; a consultation returns the decision and execution brief rather than continuing into implementation. Only a genuine failure takeover retains implementation and verification through completion. Luna failures also start a fresh Sol takeover at `medium`. Primary uncertainty or a technical-document label alone does not justify Astra. Critical design work can go directly to Astra without a Sol prerequisite. Each model-and-effort tier gets the global thirty-minute assessment from its first delegation, including direct Sol assignments. Same-tier replacements do not reset the deadline. Each new tier gets a new window. On actual inability or an unresolved assessment, transfer to a fresh child in order: Sol `medium`, Sol `high`, Sol `xhigh`, Astra `high`, then Astra `xhigh`. Ordinary work cannot skip a Sol tier. Only an actual failed or unresolved Sol `xhigh` attempt qualifies ordinary work for Astra. Advance immediately on actual inability and stop on success. Preserve read-only scope across all consultation upgrades. Release the previous owner and its processes before each handoff, and preserve evidence, failed attempts, paths, total elapsed time, owner, processes, and deadline. External access, authentication, permission, and service blockers do not escalate. Healthy long jobs continue their existing observation loop.

Luna may apply mechanical wording, link, version, formatting, or exact accepted-content changes in any document when meaning stays unchanged. Luna does not settle design choices or alter contracts. After a completed Expert assignment and accepted conclusion, a straightforward follow-up uses Luna and an unresolved ordinary question uses bounded Sol consultation. Astra is eligible again for a new critical question, a problem unresolved by Sol `xhigh`, or explicit user model selection. An active takeover stays with its owner through diagnosis, implementation, and verification.

Automatic escalation stops at Astra `xhigh`. If the Astra `xhigh` attempt cannot resolve the problem or remains unresolved at its 30-minute assessment, report the actual limit or evidence gap and stop escalation. Do not automatically use Sol or Astra at `max` or `ultra`, or restart the escalation cycle.

Explicit task-specific user model and effort selection takes precedence within actual tool and access limits. The cap governs automatic escalation, not an explicit task-specific selection. Critical design work also preserves explicit task-specific user selection. These defaults do not switch the active Primary. Luna does not support `ultra`.

For explicit spawn arguments, pass the table's ID as `model` and its effort as `reasoning_effort`. Follow the role and history constraints in `CODEX.md`. Global `AGENTS.md` authorizes the takeover sequence and defines when it stops; this table grants no additional escalation or mutation authority.

## Upstream role mapping

These are responsibility mappings, not a second routing engine. Every upstream role is resolved here before spawning. Missing role configuration uses this table, never an upstream Grok, Claude, or retired GPT default. Complexity alone does not change the tier. Lists for explicitly selected candidate or review workflows name separate assignments, not automatic permission to create a panel.

Ordinary Sol mappings below cover the unresolved decision or explicitly assigned design document; accepted execution returns to Luna unless the assignment is a genuine failure takeover.

| Upstream role | Assignment on this host |
| --- | --- |
| `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb` | Primary owns diagnosis and solution selection; Luna executes specified implementation and checks. Use the global takeover sequence when unresolved. |
| `judgment and prose` | Primary retains goals and acceptance; Luna writes prescribed prose or exact accepted content. Sol authors or reviews ordinary technical plans and designs. Astra handles critical design decisions. |
| `hardest tasks` | No difficulty-based model override. Apply the same responsibility split and evidence-triggered takeover sequence. |
| `how explorer`, `why investigators` | Luna collects named read-only evidence; Primary interprets it. Ordinary unresolved questions use a bounded read-only Sol assignment. Astra requires critical design, an actual unresolved Sol `xhigh` attempt, or explicit user model selection. |
| `how explainer`, `why synthesizer` | Primary explains and synthesizes. Ordinary technical documents use Sol and critical design work uses Astra. Do not add a redundant agent merely for this label. |
| `reflect tooling` | Luna gathers prescribed tool, log, and configuration evidence. Sol handles routine existing-rule or upstream adaptation. Exact accepted-content changes use Luna; new critical design decisions use Astra. |
| `reflect judgment, divergent, synthesizer` | Primary normally judges and synthesizes. An explicitly selected review uses scoped Sol read-only assignments for ordinary judgments and existing-rule adaptation. Astra requires critical design, an actual unresolved Sol `xhigh` attempt, or explicit user model selection. Authorized edits are a separate responsibility. |
| `swarm workers` | Luna executes one specified change or evidence checklist per worker. Split investigation and design out before dispatch. Races require an explicitly selected comparison and actual supported models. |
| `architect runners` | Within an explicitly selected comparison, Sol authors ordinary local designs and plans; Astra authors critical architecture or contract decisions and consequential design tradeoffs. Luna can collect inputs and implement an accepted design. |
| `arena runners` | Resolve by the decision required. Luna executes a Primary-specified candidate; Sol develops ordinary technical alternatives; Astra handles critical design candidates. Do not give Luna open-ended alternatives. |
| `arena cross-judge pool`, `interrogate reviewers` | Only an explicitly selected independent review. Sol reviews ordinary technical work. Astra reviews critical design or a question unresolved after an actual Sol `xhigh` attempt, or follows explicit user model selection. Primary performs final acceptance. State the actual candidate count and models; do not claim different model families when all use GPT. |

An upstream role that combines investigation, judgment, design, and implementation must be split at those responsibility boundaries. Preserve its workflow phases and evidence, not its original model defaults or unrestricted agent brief. If an explicitly selected panel cannot meet required independence, scope, or model availability, report that missing verdict instead of fabricating it or silently substituting another model.

## Parent aliases and setup

`auto` and `inherit-parent` mean the actual active parent's model and reasoning effort. Resolve both from the supported session configuration, then pass explicit `model` and `reasoning_effort` with compatible history arguments. A host-supported inheritance mode is also valid only when it demonstrably preserves both. Omitted model arguments alone are not inheritance on this host: ordinary children default to Luna at `max`. Direct Sol assignments therefore need explicit Sol model and effort arguments. If the actual parent values or a supported route cannot be established, report the gap before spawning that role.

Aliases select model values, not assignment permissions. They do not turn a Luna execution role into an investigator or authorize a panel. Preserve the active Primary. Setup does not restart it or claim that a disk edit changed its model.

`/setup-pstack` reads this file and the actual host configuration, proposes only user-requested GPT model or effort changes, and writes accepted choices here. Do not restore upstream family defaults, parse effort from model-name suffixes, lower all roles with a generic budget preset, or erase a local role because upstream retired its label. Preserve explicit task-specific choices and the automatic escalation cap. Report unavailable required values without retries, substitution, or a repair PR. An unavailable requested target can be documented in an inactive profile as described below.

## Active configuration and availability

The active `config.toml` and selected profile determine the actual Primary model. Ordinary child defaults remain `gpt-6-luna` at `max`; direct Sol assignments, critical Astra design work, and takeovers use explicit spawn arguments.

Verify actual session routing before reporting model use. A disk edit, model label, cached catalog, or model self-identification does not prove a server-side model mapping. If the required model or effort is unavailable, report the limit under the global no-substitution rule.

Before activating new defaults, verify exposed model IDs and a successful request. An explicitly requested but unavailable model may be documented as a target and saved in a named, inactive profile. Preserve working defaults and report the gap. Do not fabricate catalog entries or retry access denials. Follow `CODEX.md` for authorized source edits and deployment.
