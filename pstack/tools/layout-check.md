# Deterministic frame and log checks

This optional local helper checks the two observed failures: a frame with the wrong source ratio and overflowing log rows. It does not launch a browser, attach to a port, install dependencies, or enforce an acceptance gate. It is not wired into a production workflow.

Use an existing authorized browser owner's evaluate or CDP `Runtime.evaluate` entry point. Select the correct page using its existing stable root marker. Wait for the app's existing ready condition and loaded fonts/images before collecting geometry. The helper evaluates the currently rendered DOM without navigation, resizing, scrolling, clicks, or backend requests.

Create a selectors JSON file using selectors from the surface under test:

```json
{"frame":"[data-game-frame]","log":"[data-log]","rows":"[data-log-row]"}
```

`frame` and `log` must each match exactly one element. `rows` is evaluated inside the log and must select the rendered rows intended for this check. Filtered rows excluded from display should be excluded by the selector. At least one row with complete measured text is required. These example selectors are placeholders, not verified selectors for a specific app.

Create a requirements JSON file from the actual agreed requirement:

```json
{"ratio":[1366,768],"ratioTolerancePx":0.05,"boundaryTolerancePx":1}
```

The frame height error is `measured height - measured width * required height / required width`. The tolerance is in CSS pixels, not a rounded ratio or percent. At a 600px width, a 16:9 frame differs from 1366:768 by about 0.165px. The 0.05px example distinguishes that error while allowing the observed wireframe's approximately 0.015px rounding error. Choose tolerance from the actual requirement and measured rounding allowance; do not widen it to make an incorrect ratio pass.

Generate the reusable evaluate expression:

```powershell
node pstack/tools/layout-check.mjs expression work/selectors.json
```

Pass the printed expression to the existing browser tool's evaluate operation. For CDP, use `Runtime.evaluate` with `returnByValue: true`. Reject `exceptionDetails` before saving `result.result.value` as `measurement.json`. The expression requires one frame and log, and collects every selected row, its text ranges, scroll dimensions, and ancestor visibility and clipping bounds.

Run the deterministic check:

```powershell
node pstack/tools/layout-check.mjs check work/measurement.json work/requirements.json
node --test pstack/tools/layout-check.test.mjs
```

Check output is JSON with `ok`, the unchanged evidence origin, computed `metrics`, and coded `failures`. Exit codes are 0 for a passing check, 1 for failed assertions or malformed measurement fields, and 2 for CLI, JSON, or file errors. Preserve this output alongside the existing UI evidence. A nonzero result means the measured requirement was not demonstrated; it is not a browser crash or a claim that the backend failed.

The measurement shape is `schema: "layout-check/v1"`, `evidence`, `viewport`, `frame`, and `log`. Each measured element contains `rect`, `clientRect`, `visible`, `clips`, `clientWidth`, `clientHeight`, `scrollWidth`, and `scrollHeight`. Rectangles contain `x`, `y`, `width`, and `height` in CSS pixels. `clips` records ancestor rectangles and their `x`/`y` clipping flags. `log.rows` additionally contains `text` and `textRects`. The capture expression supplies this shape directly. Fixtures must use `evidence.kind: "fixture"`; capture uses `"dom-measurement"` plus URL and timestamp. Evidence metadata is attribution, not authentication.

Assertions check positive finite geometry, explicit requirements, frame ratio, frame/log viewport and ancestor clipping, hidden elements, log horizontal scroll overflow, row horizontal containment, row internal scroll overflow, and text containment. A vertically scrollable log may contain rows outside its current vertical viewport. That normal scrolling is permitted; clipping text inside an individual row fails. Occlusion by overlays, image content, business behavior, game delivery, and human design approval remain outside this checker.

## Recommended existing-workflow boundary

In the `control-ui` interaction loop, collect and check geometry after the fresh post-action observation whenever the current acceptance promise includes a specified game-frame ratio or contained log text. Recollect after layout-affecting resize/expand or filtering actions. Before reporting those particular requirements as met, attach the saved geometry and result to the existing task record. Continue independent work after a failed check and correct only the affected requirement. Do not turn this into a universal frontend prerequisite.

This recommendation is documentation for the owning Primary to wire into the existing control-ui instructions. Until that wiring is accepted and deployed, invocation remains manual. Passing fixture tests validates assertion logic only. A DOM measurement from an interactive mock wireframe demonstrates that mock's measured layout only; it does not prove React implementation, the actual game view, or final user acceptance.
