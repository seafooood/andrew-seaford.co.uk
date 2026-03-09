# Week 03 Experiment Review: Fix 404 Errors — Indexing Recovery

## Date: 2026-03-02

## Experiment Summary

- **Target:** Site-wide — all 42 pages returning 404 errors
- **Changes Made:** 301 redirects implemented from old slugs to current URLs (commits: "Resolved indexing issue", "slug update")
- **Experiment Period:** 2026-02-23 to 2026-03-02 (Week 1 of 2-week window)

## Result: In Progress — Early Positive Signal

The experiment **cannot yet be declared a success or failure**. Google typically takes 1–2 weeks to re-crawl and re-validate fixed pages after redirects are implemented. This is Week 1 of the expected 2-week recovery window.

**Key positive indicator:** The 404 validation status changed from `Failed` → `Started`, which confirms Google has acknowledged the fix attempt and is now re-processing those URLs.

---

## Indexing Status Comparison

| Metric | Baseline (2026-02-23) | This Week (2026-03-02) | Change |
|--------|----------------------|------------------------|--------|
| Indexed pages | 8 | 8 | — |
| Not found (404) | 42 (Validation: Failed) | 42 (Validation: **Started**) | ✓ Acknowledged |
| Crawled - currently not indexed | 25 | 24 | -1 |
| Page with redirect | 18 | 18 | — |
| Duplicate, Google chose different canonical | 16 | 16 | — |
| Alternative page with proper canonical tag | 6 | 6 | — |
| Excluded by 'noindex' tag | 18 | 18 | — |
| Blocked (403) | 4 | 4 | — |

### Indexed Page Count (Chart Data)

The most recent indexed page count available in the GSC export is from 2026-02-24 (GSC typically has a 5–7 day data lag):

| Date | Indexed Pages |
|------|--------------|
| 2026-02-18 | 8 |
| 2026-02-22 | 8 |
| 2026-02-23 | 8 |
| 2026-02-24 | 8 |

No recovery has been visible yet within the available data window. This is expected — Google must re-crawl each of the 42 URLs before the indexed count will change.

---

## Performance Data

### Daily Site-Wide Impressions (Week 3 Period)

| Date | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| 2026-02-22 | 0 | 0 | — | — |
| 2026-02-23 | 0 | 0 | — | — |
| 2026-02-24 | 0 | 2 | 0% | 7.5 |
| 2026-02-25 | 0 | 1 | 0% | 13.0 |
| 2026-02-26 | 0 | 2 | 0% | 8.0 |
| 2026-02-27 | 0 | 0 | — | — |
| 2026-02-28 | 0 | 0 | — | — |

Daily impressions remain near-zero. No meaningful recovery yet in the 7-day measurement window.

### 3-Month Aggregate (ending 2026-03-02)

| Metric | Week 3 (3mo to 2026-02-23) | Week 4 (3mo to 2026-03-02) | Change |
|--------|----------------------------|----------------------------|--------|
| Total Clicks | 15 | 15 | — |
| Total Impressions | ~4,698 | ~4,233 | -465 (-9.9%) |
| Overall CTR | 0.32% | 0.35% | +0.03pp |

The rolling 3-month window continues to roll off the high-impression period of late November/December 2025, causing total impressions to decline even as the site's recent daily impressions are near-zero.

### Top Pages (Current 3-Month Period)

| Page | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| /custom-inno-theme/ | 3 | 601 | 0.50% | 9.27 |
| /wp-content/uploads/.../CNC.pdf | 2 | 157 | 1.27% | 4.92 |
| /create-empty-folders-inno/ | 2 | 116 | 1.72% | 9.75 |
| /how-to-mock-a-function-that-returns-a-value/ | 2 | 65 | 3.08% | 24.18 |
| /flood-fill-opencv/ | 1 | 220 | 0.45% | 12.83 |
| /check-dotnet-framework-installed-inno-setup/ | 1 | 177 | 0.56% | 13.21 |
| /create-m3u-playlist-from-directory-list/ | 1 | 169 | 0.59% | 10.88 |
| /wp-content/uploads/.../Vacuum-Forming.pdf | 0 | 2,297 | 0% | 76.34 |

---

## What Was Implemented

Based on git commit history, the following was completed during Week 3:

1. **Resolved indexing issue** — 301 redirects added from old WordPress slugs to current Docusaurus URLs
2. **Slug updates** — Several URL slugs were standardised
3. **Related links** — Internal linking improved

The `@docusaurus/plugin-client-redirects` plugin was used to configure permanent redirects.

---

## Assessment Against Hypothesis

| Hypothesis | Status |
|-----------|--------|
| 301 redirects will be implemented | ✅ Done |
| Google will acknowledge the fix | ✅ Validation changed from "Failed" → "Started" |
| 404 count will decrease | ⏳ Pending (still 42, but being re-processed) |
| Indexed pages will recover towards 20+ | ⏳ Pending (still 8, within expected wait time) |
| Daily impressions will recover to 50+/day | ⏳ Pending |

---

## Conclusions

1. **Implementation is complete.** All 301 redirects have been deployed. The validation status change from "Failed" to "Started" is the expected first step in Google's recovery process.

2. **Results are pending.** The 1-week window is within the normal 1–2 week wait time for Google to re-crawl and re-index. The experiment should be re-evaluated next week (by 2026-03-09).

3. **One page moved from "Crawled - not indexed"** (25 → 24), which may indicate very early positive movement.

4. **Next review:** The Week 4 data (available 2026-03-09) should show whether the 404 count has decreased and whether indexed pages have begun to recover. If the count drops below 42, the experiment can be declared partially successful.

---

## Ongoing Monitoring

- **Week 02 experiment (custom-inno-theme CTR):** Still inconclusive. The changes are live. Will be re-evaluated once daily impressions recover to a measurable level.
- **Week 01 experiment (Docker Flask indexing):** Still unindexed. Continue monitoring.
