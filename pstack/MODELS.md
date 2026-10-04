# Model selection for this host

Updated 2026-10-04. Before using this file, read [CODEX.md](CODEX.md) and the global `AGENTS.md` it identifies. Global policy determines assignment eligibility, takeover triggers, deadlines, and authorization; `CODEX.md` supplies briefs and tool mechanics. This file owns exact model IDs, reasoning effort, configuration, and model-availability evidence. Reuse unchanged instructions already read in this session. Upstream role defaults do not apply.

## Model and effort mapping

| Assignment | Model | Reasoning effort |
| --- | --- | --- |
| Default Sol Primary | `gpt-6.1-sol` | `high` |
| Luna Executor | `gpt-6-luna` | `max` |
| Sol Senior Executor takeover | `gpt-6.1-sol` | `xhigh` |
| Initial Astra Expert takeover | `gpt-6-astra` | `high` |
| Final automatic Astra escalation, using a fresh child | `gpt-6-astra` | `xhigh` |
| Authoritative technical-document authorship, substantive revision, restructuring, or review | `gpt-6-astra` | `high` |
| Initial bounded read-only Astra investigation or consultation | `gpt-6-astra` | `high` |

Automatic Astra escalation stops at `xhigh`. If that attempt cannot resolve the problem or remains unresolved at its 30-minute assessment, report the actual limit or evidence gap and stop escalation. Do not automatically use `max` or `ultra`, or restart the escalation cycle.

Explicit task-specific user model and effort selection takes precedence within actual tool and access limits. The cap governs automatic escalation, not an explicit task-specific selection. The document policy permits a stronger model explicitly selected by the user. These defaults do not switch the active Primary. Luna does not support `ultra`.

For explicit spawn arguments, pass the table's ID as `model` and its effort as `reasoning_effort`. Follow the role and history constraints in `CODEX.md`. Global `AGENTS.md` authorizes the takeover sequence and defines when it stops; this table grants no additional escalation or mutation authority.

## Upstream role mapping

These are responsibility mappings, not a second routing engine. Every upstream role is resolved here before spawning. Missing role configuration uses this table, never an upstream Grok, Claude, or retired GPT default. Complexity alone does not change the tier. Lists for explicitly selected candidate or review workflows name separate assignments, not automatic permission to create a panel.

| Upstream role | Assignment on this host |
| --- | --- |
| `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb` | Primary owns diagnosis and solution selection; Luna executes specified implementation and checks. Use the global takeover sequence when unresolved. |
| `judgment and prose` | Primary owns ordinary judgment; Luna writes ordinary prose from a specified brief; Astra authors or reviews authoritative technical documents. |
| `hardest tasks` | No difficulty-based model override. Apply the same responsibility split and evidence-triggered takeover sequence. |
| `how explorer`, `why investigators` | Luna collects named read-only evidence; Primary interprets it. One bounded unresolved question may go to a read-only Astra investigation. |
| `how explainer`, `why synthesizer` | Primary explains and synthesizes. An authoritative architecture document goes to Astra. Do not add a redundant agent merely for this label. |
| `reflect tooling` | Luna gathers prescribed tool, log, and configuration evidence; Primary judges it. Authoritative rule changes go to Astra. |
| `reflect judgment, divergent, synthesizer` | Primary normally judges and synthesizes. An explicitly selected review uses scoped Astra read-only assignments for unresolved judgments or authoritative instruction review; authorized edits are a separate responsibility. |
| `swarm workers` | Luna executes one specified change or evidence checklist per worker. Split investigation and design out before dispatch. Races require an explicitly selected comparison and actual supported models. |
| `architect runners` | Astra authors the authoritative design candidates within an explicitly selected comparison. Luna can collect their inputs and implement an accepted design. |
| `arena runners` | Resolve by artifact: Luna executes a Primary-specified candidate; Astra authors authoritative technical candidates. Open-ended implementation alternatives need a selected design or authorized takeover, not a blanket Luna assignment. |
| `arena cross-judge pool`, `interrogate reviewers` | Only an explicitly selected independent review. Astra reviews authoritative designs or a bounded unresolved question. Primary performs ordinary acceptance. State the actual candidate count and models; do not claim different model families when all use GPT. |

An upstream role that combines investigation, judgment, design, and implementation must be split at those responsibility boundaries. Preserve its workflow phases and evidence, not its original model defaults or unrestricted agent brief. If an explicitly selected panel cannot meet required independence, scope, or model availability, report that missing verdict instead of fabricating it or silently substituting another model.

## Parent aliases and setup

`auto` and `inherit-parent` mean the actual active parent's model and reasoning effort. Resolve both from the supported session configuration, then pass explicit `model` and `reasoning_effort` with compatible history arguments. A host-supported inheritance mode is also valid only when it demonstrably preserves both. Omitted model arguments alone are not inheritance on this host: ordinary children default to Luna at `max`. If the actual parent values or a supported route cannot be established, report the gap before spawning that role.

Aliases select model values, not assignment permissions. They do not turn a Luna execution role into an investigator or authorize a panel. Preserve the active Primary. Setup does not restart it or claim that a disk edit changed its model.

`/setup-pstack` reads this file and the actual host configuration, proposes only user-requested GPT model or effort changes, and writes accepted choices here. Do not restore upstream family defaults, parse effort from model-name suffixes, lower all roles with a generic budget preset, or erase a local role because upstream retired its label. Preserve explicit task-specific choices and the automatic escalation cap. Report unavailable required values without retries, substitution, or a repair PR. An unavailable requested target can be documented in an inactive profile as described below.

## Active configuration and availability

The active `config.toml` and selected profile determine the actual Primary model. Ordinary child defaults remain `gpt-6-luna` at `max`; takeovers use explicit spawn arguments.

Verify actual session routing before reporting model use. A disk edit, model label, cached catalog, or model self-identification does not prove a server-side model mapping. If the required model or effort is unavailable, report the limit under the global no-substitution rule.

Before activating new defaults, verify exposed model IDs and a successful request. An explicitly requested but unavailable model may be documented as a target and saved in a named, inactive profile. Preserve working defaults and report the gap. Do not fabricate catalog entries or retry access denials. Follow `CODEX.md` for authorized source edits and deployment.
