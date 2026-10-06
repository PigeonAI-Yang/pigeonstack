import assert from 'node:assert/strict';
import { test } from 'node:test';
import { Script } from 'node:vm';
import { checkLayout, measureLayout } from './layout-check.mjs';

const requirements = { ratio: [1366, 768], ratioTolerancePx: 0.05, boundaryTolerancePx: 1 };
const element = (x, y, width, height) => ({
  rect: { x, y, width, height }, clientRect: { x, y, width, height }, visible: true, clips: [],
  clientWidth: width, clientHeight: height, scrollWidth: width, scrollHeight: height,
});
const fixture = () => ({
  schema: 'layout-check/v1', evidence: { kind: 'fixture', name: 'synthetic bounded log' },
  viewport: { width: 1280, height: 720 }, frame: element(120, 80, 600, 600 * 768 / 1366),
  log: { ...element(120, 430, 600, 280), scrollHeight: 1200, rows: [
    { ...element(120, 690, 600, 20), text: 'complete message', textRects: [{ x: 124, y: 692, width: 180, height: 16 }] },
    { ...element(120, 400, 600, 20), text: 'scrolled row', textRects: [{ x: 124, y: 402, width: 180, height: 16 }] },
  ] },
});

test('valid ratio, contained text and intentional vertical log scrolling pass', () => {
  const result = checkLayout(fixture(), requirements);
  assert.equal(result.ok, true);
  assert.equal(result.evidence.kind, 'fixture');
  assert.equal(result.metrics.rowCount, 2);
});

const cases = [
  ['wrong 16:9 viewport ratio', 'frame-ratio', m => { m.frame.rect.height = 600 * 9 / 16; }],
  ['row escapes log', 'row-overflow', m => { m.log.rows[0].rect.width = 630; }],
  ['text clips inside otherwise bounded row', 'text-overflow', m => { m.log.rows[0].textRects[0].width = 650; }],
  ['log horizontal scrollbar', 'log-scroll-overflow', m => { m.log.scrollWidth = 720; }],
  ['row content clips vertically', 'row-scroll-overflow', m => { m.log.rows[0].scrollHeight = 40; }],
  ['hidden frame', 'hidden', m => { m.frame.visible = false; }],
  ['hidden row', 'hidden', m => { m.log.rows[0].visible = false; }],
  ['frame clipped by ancestor', 'ancestor-clipping', m => { m.frame.clips = [{ rect: { x: 120, y: 80, width: 500, height: 400 }, x: true, y: false }]; }],
  ['log clipped by viewport', 'viewport-clipping', m => { m.log.rect.y = 600; }],
  ['missing text measurement', 'invalid-input', m => { delete m.log.rows[0].textRects; }],
  ['empty rows cannot prove log bounds', 'invalid-input', m => { m.log.rows = []; }],
  ['invalid dimensions', 'invalid-input', m => { m.frame.rect.width = '600'; }],
  ['zero frame', 'invalid-input', m => { m.frame.rect.height = 0; }],
  ['unknown evidence origin', 'invalid-input', m => { delete m.evidence; }],
];
for (const [name, code, mutate] of cases) test(name, () => {
  const measurement = fixture();
  mutate(measurement);
  const result = checkLayout(measurement, requirements);
  assert.equal(result.ok, false);
  assert.ok(result.failures.some(f => f.code === code), JSON.stringify(result));
});

test('subpixel ratio rounding is accepted but 0.06px error is rejected', () => {
  const measurement = fixture();
  measurement.frame.rect.height += 0.049;
  assert.equal(checkLayout(measurement, requirements).ok, true);
  measurement.frame.rect.height += 0.011;
  assert.equal(checkLayout(measurement, requirements).ok, false);
});

test('requirement tolerance and ratio must be explicit finite numbers', () => {
  for (const requirement of [null, {}, { ...requirements, ratio: [0, 768] }, { ...requirements, ratioTolerancePx: -1 }, { ...requirements, boundaryTolerancePx: NaN }]) {
    const result = checkLayout(fixture(), requirement);
    assert.equal(result.ok, false);
    assert.ok(result.failures.every(f => f.code === 'invalid-input'));
  }
});

test('browser expression is self-contained JavaScript', () => {
  new Script(`(${measureLayout.toString()})({frame: '#frame', log: '#log', rows: '.row'})`);
});
