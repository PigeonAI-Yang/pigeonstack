# Pstack on Codex

Use the global AGENTS.md already supplied by the host. Its maintained source is J:/PigeonYang/pigeonstack/AGENTS.md and its runtime copy is J:/Users/yangda01/.codex/AGENTS.md. It owns authorization, default direct execution, resource limits, completion, and communication. Reuse unchanged instructions already read.

## Choose only useful steps

Use pstack when explicitly requested or when its procedure addresses a concrete investigation, design, implementation, or verification need. Ordinary changes may proceed directly. A nontrivial label, function boundary, document type, commit, or review does not trigger another skill or a complete playbook.

When selecting a playbook from [poteto-mode](skills/poteto-mode/SKILL.md), use the steps relevant to the promised result and their real dependencies. Record a material adaptation only when it changes that promise. Do not copy skipped steps into a checklist or add a record for a simple task. Explicitly requested phases, established project checks, and evidence-backed dependencies still apply.

Upstream spawn, fan-out, consultation, and takeover steps are conditional on AGENTS.md's explicit delegation permission. Without it, investigate, implement, synthesize, and check directly where that satisfies the task. Do not perform every agent role yourself or claim independent review from self-review. Report a specifically required independent result that is unavailable.

Use existing entry points and credible evidence. A new harness, prototype, feature map, fixed candidate or lane count, benchmark, panel, or retrospective requires a current task requirement or a demonstrated need. Skill and playbook prose alone cannot create such a prerequisite. Permission-sensitive actions follow AGENTS.md regardless of workflow autonomy wording.

## Load conditional references

| Current need | Read only what applies |
| --- | --- |
| Explicitly requested agents, takeover, or agent waits | [MULTI_AGENT.md](MULTI_AGENT.md), then [MODELS.md](MODELS.md) for model selection. |
| Explicit coordinator role | [COORDINATOR.md](COORDINATOR.md), retaining its whole-outcome ownership. |
| Model setup, aliases, or availability | [MODELS.md](MODELS.md). Preserve existing choices. |
| A host tool or Cursor-to-Codex conversion | [Host tool reference](HOST_REFERENCE.md#translate-host-tools) and the current tool schema. |
| Bound saved-task context | [Prepared local checks](HOST_REFERENCE.md#prepared-local-checks). |
| Movement driven by live coordinates | [Position feedback](HOST_REFERENCE.md#position-feedback-for-live-control). |
| Authorized installation or runtime synchronization | [Maintain and install](HOST_REFERENCE.md#maintain-and-install). |

An explicit poteto-help request uses [poteto-help](skills/poteto-help/SKILL.md) to answer with grounded links and at most one example, without executing it. Bundled Cursor guides, agent descriptions, and dormant automations grant no host capability, background activity, or runtime enforcement. An upgrade does not invoke correct or evaluations.

## Prepare the assignment

Only for authorized delegation, use the [four-field assignment template](MULTI_AGENT.md#prepare-the-assignment). A Main's completion condition covers its assigned outcome; the user's completion condition controls overall acceptance.

## Translate host tools

Use actual supported arguments. Agent tool mechanics are in [MULTI_AGENT.md](MULTI_AGENT.md#translate-host-tools); other conversions are in [HOST_REFERENCE.md](HOST_REFERENCE.md#translate-host-tools). A missing tool is a concrete capability gap, not permission to substitute an agent or provider.

## Prepared local checks

TASK_CONTEXT_HELPER_PATH is `hooks/task_context.py` beside this entry. Bound-region owners use its read/update commands with a whole-record SHA-256 and recoverable archive as described in [the helper reference](HOST_REFERENCE.md#prepared-local-checks). No new ledger is required.

## Maintain and install

Edit maintained source, preview the narrowest authorized synchronization scope, preserve model settings, deploy, and read back the selected files and installed hashes. Exact commands and scope boundaries are in [the installation reference](HOST_REFERENCE.md#maintain-and-install).
