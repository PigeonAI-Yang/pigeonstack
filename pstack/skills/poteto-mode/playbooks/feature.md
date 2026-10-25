### Feature

> Codex adaptation: Apply only task-relevant steps under [CODEX.md](../../../CODEX.md). Workflow text does not add authorization or universal prerequisites.

**You own the design, implementation, review, and verification.** Delegate only within an explicit user request.

1. Read the affected implementation. Use how if the behavior or ownership remains unclear.
2. Choose the local design. Use architect or a comparison only for a concrete unresolved choice within the user's scope.
3. Keep a short checkpoint when dependencies or pickup require it. Describe actual blockers and shared resources; no fixed item count is required.
4. Implement directly. If the user explicitly requests a subagent, use the feature model in `MODELS.md` with a specific scope (file paths, named data shape and its organizing structure per **principle-model-the-domain**, a state machine over scattered booleans, a table/registry over branching, a typed model over repeated shape assumptions, chosen before the delegate writes logic, and success criteria). When multiple valid shapes leave a material design decision unresolved, use the **arena** candidate procedure only within an explicitly selected comparison under `CODEX.md`. Otherwise the Primary selects the shape before the execution brief. Record any missing independent verdict instead of simulating review. A subagent forbidden to spawn satisfies this by owning the diff directly with the same review separation. No "standing by" reply that waits on a nested agent. Comments per **Comments**. Surgical edits, re-ground against the source for upstream-derived files. Port shared-primitive improvements to all consumers and verify each. Commit only within the authorized task.
5. Verify on the matching surface. "Inconclusive" or wrong-surface is not a pass. Flag it.
6. If commits or a stack are part of the authorized task, keep them small and ordered. Otherwise retain a reviewable patch.
   Use the **sequence-verifiable-units** principle skill, building, verifying, and committing each small unit before the next.
7. Use interrogate if an independent review is explicitly required. Otherwise resolve and verify the concrete design concern within the current task.
8. Use **Opening a PR** only when PR creation is authorized and part of the requested outcome.

For explicitly authorized multi-agent work, code-coupled changes (one feature, one migration) go to a single owner with the checkpoint inline. That owner fans out internally after the blocking phase. Parent-level fan-out is for slices that produce independent artifacts (audits, cross-subsystem investigations, competing experiments). Rewrite the checkpoint at phase boundaries. Spawn a fresh owner rather than chaining interrupts.

**Reply:** what you built, what you chose and why, the throughput checkpoint, open decisions. Tables for design alternatives.
