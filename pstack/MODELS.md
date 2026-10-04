# Model selection for this host

Updated 2026-10-04. Before using this file, read [CODEX.md](CODEX.md) and the global `AGENTS.md` it identifies. Global policy determines assignment eligibility, takeover triggers, deadlines, and authorization; `CODEX.md` supplies briefs and tool mechanics. This file owns exact model IDs, reasoning effort, configuration, and model-availability evidence. Reuse unchanged instructions already read in this session. Upstream role defaults do not apply.

## Model and effort mapping

| Assignment | Model | Reasoning effort |
| --- | --- | --- |
| Default Sol Primary | `gpt-6.1-sol` | `high` |
| Luna Executor | `gpt-6-luna` | `max` |
| Sol Senior Executor takeover | `gpt-6.1-sol` | `xhigh` |
| Initial Astra Expert takeover | `gpt-6-astra` | `high` |
| Further unresolved Astra attempts, in order | `gpt-6-astra` | `xhigh`, then `max`, then `ultra` |
| Authoritative technical-document authorship, substantive revision, restructuring, or review | `gpt-6-astra` | `high` |
| Initial bounded read-only Astra investigation or consultation | `gpt-6-astra` | `high` |

Explicit task-specific user model selection takes precedence within actual tool and access limits. The document policy permits a stronger model explicitly selected by the user. These defaults do not switch the active Primary. Luna does not support `ultra`.

For explicit spawn arguments, pass the table's ID as `model` and its effort as `reasoning_effort`. Follow the role and history constraints in `CODEX.md`. Global `AGENTS.md` authorizes the takeover sequence and defines when it stops; this table grants no additional escalation or mutation authority.

## Active configuration and availability

The active `config.toml` and selected profile determine the actual Primary model. Ordinary child defaults remain `gpt-6-luna` at `max`; takeovers use explicit spawn arguments.

Verify actual session routing before reporting model use. A disk edit, model label, cached catalog, or model self-identification does not prove a server-side model mapping. If the required model or effort is unavailable, report the limit under the global no-substitution rule.

Before activating new defaults, verify exposed model IDs and a successful request. An explicitly requested but unavailable model may be documented as a target and saved in a named, inactive profile. Preserve working defaults and report the gap. Do not fabricate catalog entries or retry access denials. Follow `CODEX.md` for authorized source edits and deployment.
