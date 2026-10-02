# Model selection for this host

Updated 2026-10-02. Global `AGENTS.md` is authoritative for Primary responsibility, delegation and scheduling. `CODEX.md` supplies host mechanics; this file owns model IDs and reasoning effort. Upstream role defaults do not apply.

## Active routing

| Work | Model and starting effort |
| --- | --- |
| Preferred general Primary: goals, constraints, key decisions, assignments, integration, and final acceptance | `gpt-6-sol`, `high` |
| Implementation of an accepted design or Primary-specified repair, prescribed evidence collection and implementation verification | `gpt-6-luna`, `max` |
| Routine authorized operations and ordinary public prose without authoritative design decisions | `gpt-6-luna`, `max` |
| Authoritative technical-document authorship, restructuring, substantive revision and review | `gpt-6-astra`, `high`, or a stronger model explicitly selected by the user; never Luna |
| Bounded read-only investigation of one unresolved question | `gpt-6-astra`, `high` |
| A specific read-only advisory question | `gpt-6-astra`, `high` |

Implementation and refactoring, including webpage work, default to Luna after the Primary selects the solution. An unresolved question permits only bounded read-only Astra investigation, followed by a return to Luna for implementation. Other Astra execution requires the user's explicit task-specific model selection and a general/default execution role. Complexity labels, task size, and incomplete decomposition are not exceptions.

Route by required judgment, not by platform, publication status, file type, or operation count, as stated in global `AGENTS.md`.

The user explicitly selects high for Sol and Astra, including the read-only advisor, and max for every Luna assignment, including small evidence-collection tasks and checks. Do not change these efforts for routine cost or speed judgments; use a different supported effort only when the user explicitly requests it. Luna does not support ultra.

## Active configuration and availability

The active config.toml and selected profile determine the actual Primary model. Preserve that explicit selection; the preferred model above does not authorize changing it. Ordinary implementation and prescribed evidence-collection children use `gpt-6-luna` with `max`. Authoritative technical-document work follows its routing row and the policy in global `AGENTS.md`. Changing defaults does not switch a running Primary.

GPT-6 Sol and Luna are exposed by the updated client. Verify actual session routing when reporting model use. A disk edit, model label, cached catalog, or model self-identification does not prove a server-side model mapping. If a selected assignment model becomes unavailable, use another currently authorized model only when it fits the assignment boundaries; otherwise report a blocker. Do not silently take over with the current Primary or switch to another generation or provider.

## Spawn contract

- Every assignment starts a new child with a new task name. A completed child is retired; do not use `followup_task` or reuse its conversation for the next assignment. Carry forward only the necessary findings and evidence in a concise handoff.

- Luna implements one Primary-specified repair or accepted design step, or follows a prescribed read-only evidence checklist. Apply the authoritative technical-document policy in global `AGENTS.md` before routing document work. The brief in CODEX.md applies to Luna implementation; a checklist may be assigned before cause or repair is known. Do not give Luna open-ended diagnosis, architecture choices or a batch of unexplained failures.
- For ordinary children, pass `model: "gpt-6-luna"` and `reasoning_effort: "max"`. Every Luna call uses `max`; routine task-specific cost or speed judgments do not override this user requirement. These match the active global child defaults.
- For Astra authorship, substantive revision or review of authoritative technical documents, bounded read-only investigation of one unresolved question, use the supported general/default role with explicit `model: "gpt-6-astra"` and `reasoning_effort: "high"`. Define the objective, decisive context, resources, permissions, exclusions, acceptance evidence and return conditions. Keep major scope, product and architecture decisions and final acceptance with the Primary. Do not use `worker` or `poteto-agent` for these assignments because their contracts are limited to a prescribed implementation or read-only checklist.
- For a specific read-only advisory question, use `astra-advisor`, `model: "gpt-6-astra"`, and `reasoning_effort: "high"`. Never use the advisor role for writes or open-ended investigation.
- Use `fork_turns: "none"` or necessary finite history when selecting a model or effort. Do not use full-history inheritance with an override.
- Custom agent files may override explicit spawn choices. The ordinary worker and poteto-agent files intentionally omit model and effort so the active defaults or explicit assignment can select them. The dedicated advisor intentionally pins Astra and high effort.
- Explicit task-specific user choices take precedence within tool and access limits. If a selected model is unavailable, use another currently authorized model only if it fits the assignment boundaries; if none does, report a blocker. Do not silently use another generation or provider.
- Do not create extra planners, synthesizers, or model panels to duplicate Primary responsibility. Advisory findings inform the Primary's decision; they do not transfer final acceptance.
