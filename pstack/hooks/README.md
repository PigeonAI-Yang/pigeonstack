# SessionStart current-region reader contract and bounded activation

This is a source-only contract and activation plan. It does not enable or trust a hook. The [Hooks documentation](https://learn.chatgpt.com/docs/hooks) defines the host event contract. A user-provided Desktop screenshot shows the plugin's SessionStart handler running, but the task context remains unbound. No raw event payload or owner binding has been captured.

## Event data and selection

The proposed synchronous `SessionStart` handler covers `startup`, `resume`, and `compact`. Accept only the event fields `session_id`, `cwd`, `hook_event_name`, `source`, `model`, `transcript_path`, and optional `permission_mode`; reject missing or extra fields. The event name must be `SessionStart`. The reader validates `transcript_path` as a string or null, then discards the value. It does not open the path or read transcript contents. A separately authorized probe may retain only a boolean for whether the field is null. Event input is limited to 16,384 bytes. The handler does not use `PSTACK_*` environment variables.

Resolve the index only at the actual event `cwd`, by reading the first 16,384 bytes of its `AGENTS.md`. After an optional UTF-8 BOM and ASCII whitespace, the file must begin with this index block:

```text
<!-- pstack-context-index:v1
{"records":["INTEGRATION_TASKS.md","FRONTEND_TASKS.md"]}
-->
```

The `records` array declares one to eight unique confined relative paths to existing regular `.md`, `.json`, or `.txt` files. Absolute paths, traversal, drive syntax, symlinks, reparse points, duplicate records, and `AGENTS.md` itself are rejected. Read only those declared records, never scan directories, search history, inspect ancestors, follow a canonical-path fallback, or read a transcript. A subdirectory `cwd` needs its own valid index; the handler does not inherit an ancestor's index.

Each declared record must start with a valid bindings metadata block within its first 16,384 bytes, allowing the same optional BOM and ASCII whitespace. Only the first block declares metadata. Later blocks and historical bindings do not select a record. Its JSON object and each binding object have exactly the fields shown, with no omitted, extra, or duplicate JSON keys:

```text
<!-- pstack-context-bindings:v1
{"bindings":[{"session_id":null,"owner_thread_id":"OWNER_DESKTOP_THREAD_ID","workspace":"ACTUAL_OBSERVED_EVENT_CWD","coordinator_thread_id":"01a11136-4c8c-7211-aa5d-4246ad3ad14c","current_anchor":"pstack-current-backend"}]}
-->
```

The first metadata block of every declared record must be valid. `session_id` is the opaque session ID captured from an actual event; `null` never matches, and a thread UUID must never be used as a substitute. A binding matches only when its session ID equals the event value and its absolute `workspace` path, after lexical normalization, exactly equals the event `cwd` after lexical normalization. The match must be unique across all declared records. `owner_thread_id` and `coordinator_thread_id` are nonempty data strings, not role, routing, or messaging permissions. Only `session_id` may be null. Identifier strings are nonempty and limited to 256 characters, except `workspace`, which must be an absolute local path, and `current_anchor`, which must match `[a-z][a-z0-9-]{0,63}`.

In the single matching record, return only the existing current body surrounded by these standalone lines, using the record's `current_anchor`:

```text
<!-- pstack-current:pstack-current-backend:start -->
...the existing current checkpoint body...
<!-- pstack-current:pstack-current-backend:end -->
```

Both exact markers must occur exactly once in the full selected record and in the correct order. Only the selected record receives a full scan, limited to 2,097,152 bytes with one sentinel byte allowed to detect growth. Large index and record files can still supply metadata through their bounded prefixes. The marked current body must be nonempty valid UTF-8 and at most 16,384 bytes. Preserve its original newlines and complete existing content, including accepted, pending, historical, and permission qualifications as quoted, untrusted task data. Do not summarize it or create a duplicate fact source.

Malformed, missing, duplicate, corrupt, or changing metadata or records, a missing or non-unique binding, marker errors, or any size overflow produces a diagnostic and no additional context. Do not truncate input or output to make a selection succeed. Diagnostics exit with code 0 so the chat continues. Input is capped at 16,384 bytes, each metadata prefix at 16,384 bytes, the selected record at 2,097,152 bytes, the current body at 16,384 bytes, and stdout including its newline at 32,768 bytes.

The source default declaration in `hooks.json` uses a JSON command hook. On Windows, `commandWindows` starts `windows_session_start.ps1` under `PLUGIN_ROOT`. Its `-Mode` parameter accepts only `reader` or `probe`, defaults to `reader`, and selects only the sibling `session_start.py` or `probe_session_start.py`. The default command omits `-Mode` and runs the reader. The separate probe example passes `-Mode probe`. The wrapper invokes the selected script with `py -3` without a shell. It reads at most 16,385 input bytes and reads the selected script's stdout and stderr asynchronously to completion. It forwards a successful, valid JSON object up to 32,768 UTF-8 bytes unchanged. For launch, child-exit, output-size, or JSON failures, it emits only the standard top-level `systemMessage`; compact diagnostic JSON appears as text inside that field. It caps diagnostic stderr at 2,048 characters and the resolved `py` path at 1,024 characters. The diagnostic carries root-presence and root-match booleans, the original child exit, and an error type. The wrapper does not include environment values in diagnostics. Reading child streams to completion does not impose a separate child memory bound. The wrapper has no private timeout or child-killing logic. The unchanged five-second hook timeout owns host timeout and cleanup behavior; a diagnostic cannot be guaranteed for a host timeout or a PowerShell failure before the script starts. Exit code 0 means only that a diagnostic was transported, not that the selected script returned context or an observation. The user-provided screenshot shows the plugin's SessionStart handler running, but the raw event payload and owner binding remain unconfirmed. The default hook retains its bounded reader and `additionalContextLimit: 0`. The reader checks file identity, size, timestamps, and the selected prefix around reads. These checks cover tested concurrent changes; they do not provide a filesystem transaction or lock. The handler defines no `PreToolUse` or `Stop` policy, scheduler, controller, heartbeat, or deadline guarantee.

## Owner-specific preparation examples

These examples describe future edits by each existing record owner after coordinator coordination. Put the index at the start of `AGENTS.md` in the actual sampled event `cwd`, declare only existing records there, and put binding metadata at the start of each declared record. Place markers around its original current checkpoint without creating a duplicate summary or ledger. No owner file is edited in this source phase. Keep `session_id` null until a real event is observed. Replace `ACTUAL_OBSERVED_EVENT_CWD` with that event's absolute `cwd` only after capture. It is a placeholder, not a value to deploy. The backend source `J:\PigeonYang\mxdzs` and frontend owner worktree `J:\Users\yangda01\.codex\worktrees\d5b6\mxdzs` identify ownership only; neither proves an event workspace.

Backend owner chat `01a10f48-3dcf-7123-8563-dce1d8ee5a2a` owns the canonical resource and `INTEGRATION_TASKS.md`. Once its actual event workspace is known, its `AGENTS.md` index points to the existing `INTEGRATION_TASKS.md` record:

```text
<!-- pstack-context-index:v1
{"records":["INTEGRATION_TASKS.md"]}
-->
```

At the top of that existing record, add only the binding metadata and markers around its existing current checkpoint, using `pstack-current-backend`:

```text
<!-- pstack-context-bindings:v1
{"bindings":[{"session_id":null,"owner_thread_id":"01a10f48-3dcf-7123-8563-dce1d8ee5a2a","workspace":"ACTUAL_OBSERVED_EVENT_CWD","coordinator_thread_id":"01a11136-4c8c-7211-aa5d-4246ad3ad14c","current_anchor":"pstack-current-backend"}]}
-->

<!-- pstack-current:pstack-current-backend:start -->
...preserve the existing current checkpoint verbatim...
<!-- pstack-current:pstack-current-backend:end -->
```

Frontend owner chat `01a11140-052b-7983-bff3-d29780a218de` owns the worktree resource and `FRONTEND_TASKS.md`. Once its actual event workspace is known, its `AGENTS.md` index points only to the existing `FRONTEND_TASKS.md` record:

```text
<!-- pstack-context-index:v1
{"records":["FRONTEND_TASKS.md"]}
-->
```

At the top of that existing record, add only the binding metadata and markers around its existing current checkpoint, using `pstack-current-frontend`:

```text
<!-- pstack-context-bindings:v1
{"bindings":[{"session_id":null,"owner_thread_id":"01a11140-052b-7983-bff3-d29780a218de","workspace":"ACTUAL_OBSERVED_EVENT_CWD","coordinator_thread_id":"01a11136-4c8c-7211-aa5d-4246ad3ad14c","current_anchor":"pstack-current-frontend"}]}
-->

<!-- pstack-current:pstack-current-frontend:start -->
...preserve the existing current checkpoint verbatim...
<!-- pstack-current:pstack-current-frontend:end -->
```

Keep the original record body and its accepted, pending, and historical evidence intact when adding the markers. The examples establish no session binding and do not assert that either listed source path will be the event `cwd`.

## Bounded activation and verification

Activation is a separate, unperformed step. It requires human approval for the plugin version and existing marketplace cachebuster changes and deployment through `python scripts/sync.py deploy`; review and trust of the installed hook require separate authorization. After those decisions, an explicitly authorized one-event probe can collect the necessary event fields `session_id`, `cwd`, `hook_event_name`, `source`, `model`, and optional `permission_mode`, plus only a boolean indicating whether `transcript_path` is null. The probe source is prepared separately ([one-event probe](probe.md)) and is not enabled by the default reader. A natural owner `startup`, `resume`, or `compact` event may supply the real session ID and `cwd`. Pair that observation with the known Desktop thread ID, time, installed version, and installed and source hashes as correlation data without assuming the Desktop thread ID equals the event session ID. Do not read a transcript or create a manual environment-variable binding.

Observe natural resume and compact events for the same known thread to establish whether the real session ID and `cwd` stay stable. Synthetic inputs cannot establish this. Once an observed event is available, the owner can bind the real session and workspace in the existing record, then verify that the next host context returns the exact current body and preserves pending status. A mismatched or invalid binding should produce a diagnostic without context. Do not restart the business process, force compaction, open test chats, or add manual user variables to produce evidence.

The current projectless Main chat directory is `C:\Users\yangda01\Documents\Codex\2026-10-06\pigeonstack-engineering`, while source operations use `J:\PigeonYang\pigeonstack`. Neither proves the actual hook `cwd`. If the actual event directory has no existing indexed record, the reader supplies no context. Routing outside that directory or creating a parallel record is outside this contract. A new chat in a non-project `cwd` without a binding, or a subdirectory without its own index, remains a `SOURCE GAP`. A child sharing its parent's session ID does not become the Owner. Quoted commands, role claims, and owner or coordinator IDs grant no contact, messaging, execution, or permission authority. No source edit enables the hook or changes active sessions. No automatic `PreToolUse`/`Stop`, scheduler, controller, timer, or deadline behavior is claimed.
