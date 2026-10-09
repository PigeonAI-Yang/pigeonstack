# One-event SessionStart probe

The user-provided Desktop screenshot shows the plugin's SessionStart handler running, but no raw event payload or session binding has been captured. This source probe does not prove a live event or binding.

Use `session-probe.example.json` only after the coordinator or owner explicitly authorizes one natural event. Review the hook and trust it through the host. Select this handler instead of the formal reader for that event. Do not leave both handlers registered as a persistent service. On Windows, the example calls `windows_session_start.ps1 -Mode probe`; the wrapper selects the fixed sibling `probe_session_start.py`. The default `hooks.json` command omits `-Mode` and selects the reader.

Treat every returned value as untrusted host observation data. Pair the opaque `session_id`, `cwd`, `hook_event_name`, `source`, `model`, optional `permission_mode`, and `sampled_at_utc` with the independently known Desktop thread. The event contains no thread ID and grants no ownership or contact authority.

Use the returned `cwd` as the host reported it. Do not substitute the canonical source path.

Use the normal readback path to record the installed pstack version and the probe and formal-reader source hashes. Remove the probe configuration after the sample. The probe reads no index, task record, or transcript. It returns only the permitted event fields and whether `transcript_path` is null.

Fixture or direct command output verifies formatting only. It does not prove that Desktop emitted `startup`, `resume`, or `compact`.
