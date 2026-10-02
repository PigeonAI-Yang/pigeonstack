# PigeonStack discoverability experiment

## Objective and authority

Improve the GitHub repository's sustainable search discovery and usefulness as a cited source in AI answers. The owner authorizes implementation and publication, including useful text and images. Do not substitute published content, a passing checker, or a search snippet for demonstrated ranking or citation improvement.

## Baseline: 2026-10-03 (Asia/Shanghai)

Repository: https://github.com/PigeonAI-Yang/pigeonstack

Source revision: `524ab07e6fa179817fbd4126186cc63576f81969`.

- Public repository; one star and zero forks at capture time.
- No topics, homepage, Pages site, workflows, or releases. No root license; preserve the existing upstream license notices and do not invent licensing rights.
- Authenticated GitHub traffic endpoints returned zero views and clones over the available 14-day window. These are observed API values, not a prediction.
- Two sampled web searches, `PigeonStack` and `site:github.com/PigeonAI-Yang/pigeonstack`, returned no exact target URL. This does not establish index status or rank.
- Onboarding is Windows/PowerShell and Python 3.11+. A separate-target preview copies files but does not install or activate the plugin. Real installation requires path adaptation and an existing local marketplace registration.

## Evidence and decisions

- [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features): apply ordinary SEO fundamentals, crawlable links and visible useful text; special AI files or schema are not required and inclusion is not guaranteed.
- [Google SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide): use useful original content, clear titles, descriptions and navigation.
- [GitHub topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics): accurately classify the repository for topic discovery.
- [GitHub Pages API](https://docs.github.com/en/rest/pages/pages): publish a project site from `main:/docs` with the existing account authorization.
- Public README patterns observed in [superpowers](https://github.com/obra/superpowers), [OpenAI skills](https://github.com/openai/skills), and [pinned pstack](https://github.com/cursor/plugins/tree/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d/pstack): concise purpose, getting started, concrete examples and attribution. These observations do not prove search success.

Selected changes: improve the two READMEs; publish four small static HTML pages (English/Chinese overview and getting started) with reciprocal language links, canonical URLs and a sitemap; add accurate repository topics and homepage; check local and live site health on changes and weekly. Keep existing installation limitations explicit. Use static files and Python's standard library rather than introducing a site framework.

## Work and acceptance

- [x] Publish accurate bilingual README improvements, preserving the original author's opening credit.
- [x] Publish all four documentation pages and stylesheet; verify HTTP responses and readable content, not just deployment receipts.
- [x] Verify unique titles/descriptions, canonical and language links, local links/assets, sitemap and absence of `noindex`.
- [x] Set and read back accurate repository topics, description and homepage.
- [x] Execute the documented isolated preview and record its actual boundary: file/config sync only.
- [x] Run the docs health workflow on GitHub and verify its receipt; retain the weekly schedule for regressions.
- [x] Record post-publication evidence, remaining measurement gaps and the next review.

## Measurement and follow-up

Separate three outcomes: (1) publication and crawl eligibility, (2) observed discovery/traffic, and (3) actual AI citations or search positions. A health workflow measures only the first. GitHub stars are not a ranking metric; views/clones are not evidence of AI citations or causal SEO uplift.

At subsequent reviews, record the observation date, source, query and result URL, and compare the same query set: `PigeonStack`, `PigeonStack Codex`, `Codex multi-agent workflow pstack`, and `Codex 多 Agent 协作 PigeonStack`. Note search location/engine limitations and do not report an exact rank from a partial result set. Save aggregate GitHub views/clones within their rolling retention window when access is available. Prefer verified Search Console/Bing Webmaster data if account/property access becomes available; no such access is established at baseline.

Review new evidence after seven days and after 28 days. Change content to answer observed onboarding or discovery gaps; do not generate repetitive keyword pages, manufactured endorsements, fake reviews, artificial traffic or unsolicited promotional messages. Do not update dates merely to imply freshness. The weekly health workflow should report failures through its normal run status, not produce content churn.

## Current state

The first implementation round was published in commit [`41f7dce`](https://github.com/PigeonAI-Yang/pigeonstack/commit/41f7dcef3a3a242ac417e2cebe76929eca45c842). Repository description and 11 accurate topics were updated and read back. The homepage now points to https://pigeonai-yang.github.io/pigeonstack/. GitHub Pages reports `built`, serving `main:/docs` with HTTPS. Both languages were rendered in Chromium: all four desktop pages plus both mobile overview pages loaded their stylesheet and expected headings without horizontal overflow, console errors or failed requests. The Primary inspected English desktop and Chinese mobile screenshots sequentially.

Acceptance uncovered and repaired a real onboarding defect: `patch_config` failed for an empty destination because multiple insertions at the same source offset could place a new TOML table before root assignments. A minimal empty-config reproduction and a comment-only reproduction both failed before any write. The repair groups insertions by source offset, placing existing-section additions before new table blocks. Four regression tests passed, covering parsed root/table scope, unmanaged-value preservation, BOM/line endings, repeat-call idempotence and the multiline guard. A new isolated CLI target then returned expected drift (exit 1), successful deployment (exit 0; 217 writes including configuration), and an aligned check (exit 0). No live Codex directory was modified. This repair makes the documented preview usable; it does not change installation scope or promise automatic marketplace setup.

The first docs checker was also corrected before release: GitHub repository identity was compared with inconsistent path case, and the implementation included unused general-purpose validation. The accepted direction is a small checker for the four actual pages, with fixture failures for missing canonical links and broken assets.

Search ranking and AI citation uplift remain unverified. This record remains the task's authoritative plan and evidence index.

## Publication observations: 2026-10-03

- Local site checks: 14 passed. Combined local and live checks: 24 passed, including four HTTP pages, sitemap, stylesheet and metadata checks. The live receipt checks do not simulate a search engine's indexing pipeline.
- [Push health run](https://github.com/PigeonAI-Yang/pigeonstack/actions/runs/37061797879) and [manual live health run](https://github.com/PigeonAI-Yang/pigeonstack/actions/runs/37062006260) succeeded. The downloaded artifact has `passed=true` and `source_mode=local+live`.
- The existing health workflow runs on relevant pushes/PRs and weekly on Monday at 03:17 UTC (11:17 Asia/Shanghai), retaining receipts for 90 days. It verifies technical health; it does not autonomously claim or optimize rankings.
- A post-publication sample of the four recorded queries still did not return the exact repository or Pages URL. The third query surfaced other pstack ports. No exact search position is inferred from these partial results.
- The web research tool returned an internal fetch error for both new overview URLs. Independent HTTP checks on the local machine and GitHub Actions passed. The research-tool error is an unresolved tool observation, not proof of an origin outage, crawler denial or index exclusion.
- No authenticated Google Search Console or Bing Webmaster property was inspected. Search impressions, query positions and AI citation reports therefore remain unavailable.

Next evidence reviews: 2026-10-10 and 2026-10-31 (Asia/Shanghai). Preserve this baseline and record observed changes before inferring impact. The experiment remains active; publication success is not the full ranking objective.
