import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

export function measureLayout(selectors) {
  const rect = r => ({ x: r.x, y: r.y, width: r.width, height: r.height });
  const measure = element => {
    if (!element) throw new Error('Required selector did not match');
    const box = element.getBoundingClientRect();
    let visible = element.getClientRects().length > 0;
    const clips = [];
    for (let node = element; node; node = node.parentElement) {
      const style = getComputedStyle(node);
      visible &&= style.display !== 'none' && style.visibility === 'visible' && Number(style.opacity) > 0;
      if (node !== element) {
        const bounds = node.getBoundingClientRect();
        const content = { x: bounds.x + node.clientLeft, y: bounds.y + node.clientTop, width: node.clientWidth, height: node.clientHeight };
        clips.push({ rect: content, x: /hidden|clip|auto|scroll/.test(style.overflowX), y: /hidden|clip|auto|scroll/.test(style.overflowY) });
      }
    }
    return {
      rect: rect(box), visible, clips,
      clientRect: { x: box.x + element.clientLeft, y: box.y + element.clientTop, width: element.clientWidth, height: element.clientHeight },
      clientWidth: element.clientWidth, clientHeight: element.clientHeight,
      scrollWidth: element.scrollWidth, scrollHeight: element.scrollHeight,
    };
  };
  const unique = selector => {
    const matches = document.querySelectorAll(selector);
    if (matches.length !== 1) throw new Error(`Expected one match for ${selector}, found ${matches.length}`);
    return matches[0];
  };
  const frame = unique(selectors.frame);
  const log = unique(selectors.log);
  const rows = [...log.querySelectorAll(selectors.rows)].map(element => {
    const textRects = [];
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      if (!walker.currentNode.textContent.trim()) continue;
      const range = document.createRange();
      range.selectNodeContents(walker.currentNode);
      textRects.push(...[...range.getClientRects()].map(rect));
    }
    return { ...measure(element), text: element.textContent, textRects };
  });
  return {
    schema: 'layout-check/v1',
    evidence: { kind: 'dom-measurement', url: location.href, capturedAt: new Date().toISOString() },
    viewport: { width: innerWidth, height: innerHeight }, frame: measure(frame), log: { ...measure(log), rows },
  };
}

export function checkLayout(measurement, requirement) {
  const failures = [];
  const metrics = {};
  const fail = (code, path, details) => failures.push({ code, path, details });
  const number = (value, path, positive = false) => {
    if (typeof value !== 'number' || !Number.isFinite(value) || value < 0 || (positive && value === 0)) {
      fail('invalid-input', path, 'Expected a finite nonnegative number' + (positive ? ' greater than zero' : ''));
      return false;
    }
    return true;
  };
  const validRect = (r, path) => {
    if (!r || typeof r !== 'object') { fail('invalid-input', path, 'Missing rectangle'); return false; }
    let valid = true;
    for (const key of ['x', 'y']) {
      if (typeof r[key] !== 'number' || !Number.isFinite(r[key])) { fail('invalid-input', `${path}.${key}`, 'Expected finite coordinate'); valid = false; }
    }
    for (const key of ['width', 'height']) valid = number(r[key], `${path}.${key}`, true) && valid;
    return valid;
  };
  if (!requirement || !Array.isArray(requirement.ratio) || requirement.ratio.length !== 2) {
    fail('invalid-input', 'requirement.ratio', 'Expected [width, height]');
  } else requirement.ratio.forEach((v, i) => number(v, `requirement.ratio[${i}]`, true));
  number(requirement?.ratioTolerancePx, 'requirement.ratioTolerancePx');
  number(requirement?.boundaryTolerancePx, 'requirement.boundaryTolerancePx');
  if (measurement?.schema !== 'layout-check/v1') fail('invalid-input', 'schema', 'Expected layout-check/v1');
  if (!['dom-measurement', 'fixture'].includes(measurement?.evidence?.kind)) fail('invalid-input', 'evidence.kind', 'Expected dom-measurement or fixture');
  number(measurement?.viewport?.width, 'viewport.width', true);
  number(measurement?.viewport?.height, 'viewport.height', true);
  const validElement = (element, path) => {
    if (!element) { fail('invalid-input', path, 'Missing element'); return; }
    validRect(element.rect, `${path}.rect`);
    validRect(element.clientRect, `${path}.clientRect`);
    for (const key of ['clientWidth', 'clientHeight', 'scrollWidth', 'scrollHeight']) number(element[key], `${path}.${key}`, key.startsWith('client'));
    if (typeof element.visible !== 'boolean') fail('invalid-input', `${path}.visible`, 'Expected boolean');
    if (!Array.isArray(element.clips)) fail('invalid-input', `${path}.clips`, 'Expected ancestor clip array');
    else element.clips.forEach((clip, i) => {
      validRect(clip.rect, `${path}.clips[${i}].rect`);
      if (typeof clip.x !== 'boolean' || typeof clip.y !== 'boolean') fail('invalid-input', `${path}.clips[${i}]`, 'Expected x and y booleans');
    });
  };
  validElement(measurement?.frame, 'frame');
  validElement(measurement?.log, 'log');
  if (!Array.isArray(measurement?.log?.rows) || measurement.log.rows.length === 0) fail('invalid-input', 'log.rows', 'Expected at least one measured row');
  else measurement.log.rows.forEach((row, i) => {
    const path = `log.rows[${i}]`;
    validElement(row, path);
    if (typeof row.text !== 'string') fail('invalid-input', `${path}.text`, 'Expected measured text');
    if (!Array.isArray(row.textRects) || (row.text?.trim() && row.textRects.length === 0)) fail('invalid-input', `${path}.textRects`, 'Missing measured text rectangles');
    else row.textRects.forEach((r, j) => validRect(r, `${path}.textRects[${j}]`));
  });
  if (failures.length) return { ok: false, evidence: measurement?.evidence ?? null, metrics, failures };
  const tolerance = requirement.boundaryTolerancePx;
  const outsideX = (a, b) => a.x < b.x - tolerance || a.x + a.width > b.x + b.width + tolerance;
  const outsideY = (a, b) => a.y < b.y - tolerance || a.y + a.height > b.y + b.height + tolerance;
  const checkElement = (element, path, checkAncestors) => {
    if (!element.visible) fail('hidden', path, 'Element or ancestor is hidden');
    if (checkAncestors) element.clips.forEach((clip, i) => {
      if ((clip.x && outsideX(element.rect, clip.rect)) || (clip.y && outsideY(element.rect, clip.rect))) fail('ancestor-clipping', path, { ancestor: i });
    });
  };
  const { frame, log, viewport } = measurement;
  metrics.expectedRatio = requirement.ratio[0] / requirement.ratio[1];
  metrics.actualRatio = frame.rect.width / frame.rect.height;
  metrics.heightErrorPx = frame.rect.height - frame.rect.width / metrics.expectedRatio;
  if (Math.abs(metrics.heightErrorPx) > requirement.ratioTolerancePx) fail('frame-ratio', 'frame.rect', { heightErrorPx: metrics.heightErrorPx, tolerancePx: requirement.ratioTolerancePx });
  const viewportRect = { x: 0, y: 0, ...viewport };
  for (const [path, element] of [['frame', frame], ['log', log]]) {
    checkElement(element, path, true);
    if (outsideX(element.rect, viewportRect) || outsideY(element.rect, viewportRect)) fail('viewport-clipping', path, 'Element extends outside viewport');
  }
  metrics.logHorizontalOverflowPx = log.scrollWidth - log.clientWidth;
  if (metrics.logHorizontalOverflowPx > tolerance) fail('log-scroll-overflow', 'log', { overflowPx: metrics.logHorizontalOverflowPx });
  metrics.rowCount = log.rows.length;
  log.rows.forEach((row, i) => {
    const path = `log.rows[${i}]`;
    checkElement(row, path, false);
    if (outsideX(row.rect, log.clientRect)) fail('row-overflow', path, 'Row extends horizontally outside log content');
    if (row.scrollWidth > row.clientWidth + tolerance || row.scrollHeight > row.clientHeight + tolerance) fail('row-scroll-overflow', path, 'Row text exceeds its client dimensions');
    row.textRects.forEach((text, j) => {
      if (outsideX(text, row.clientRect) || outsideX(text, log.clientRect) || outsideY(text, row.clientRect)) fail('text-overflow', `${path}.textRects[${j}]`, 'Text extends outside row or log content');
    });
  });
  return { ok: failures.length === 0, evidence: measurement.evidence, metrics, failures };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const [mode, first, second] = process.argv.slice(2);
    if (mode === 'expression' && first && !second) {
      const selectors = JSON.parse(readFileSync(first, 'utf8').replace(/^\uFEFF/, ''));
      if (['frame', 'log', 'rows'].some(key => typeof selectors[key] !== 'string' || !selectors[key].trim())) throw new Error('Selectors require nonempty frame, log and rows strings');
      console.log(`(${measureLayout.toString()})(${JSON.stringify(selectors)})`);
    } else if (mode === 'check' && first && second) {
      const read = path => JSON.parse(readFileSync(path, 'utf8').replace(/^\uFEFF/, ''));
      const result = checkLayout(read(first), read(second));
      console.log(JSON.stringify(result, null, 2));
      process.exitCode = result.ok ? 0 : 1;
    } else throw new Error('Usage: node layout-check.mjs expression selectors.json | check measurement.json requirements.json');
  } catch (error) {
    console.log(JSON.stringify({ ok: false, failures: [{ code: 'invalid-input', details: error.message }] }, null, 2));
    process.exitCode = 2;
  }
}
