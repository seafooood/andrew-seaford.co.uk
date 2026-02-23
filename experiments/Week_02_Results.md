# Week 02 Experiment Results: "Custom Inno Theme" CTR Optimization

## Date: 2026-02-23

## Experiment Summary

- **Target Article:** `/custom-inno-theme/`
- **Changes Made:** Updated frontmatter with optimized title, meta description, and keywords on 2026-02-16
- **Experiment Period:** 2026-02-16 to 2026-02-23 (7 days)

## Result: Inconclusive

The experiment **cannot be properly evaluated** within this 7-day window. While the CTR number decreased in the 3-month aggregate, this is overwhelmingly due to a site-wide collapse in impressions from mid-February — not the meta changes. The experiment needs more time and a stable indexing baseline to produce valid results.

---

## Target Page Performance

### 3-Month Aggregate Comparison

| Metric | Baseline (3mo to 2026-02-14) | Current (3mo to 2026-02-23) | Change |
|--------|------------------------------|-----------------------------|--------|
| Clicks | 5 | 3 | -2 (-40%) |
| Impressions | 684 | 640 | -44 (-6.4%) |
| CTR | 0.73% | 0.47% | -0.26pp |
| Avg Position | 9.2 | 9.3 | Stable |

### Why This Is Inconclusive

The 3-month rolling window means over 90% of the data pre-dates the changes made on 2026-02-16. The decline in clicks and impressions is consistent with the **site-wide impressions collapse** (see below), not a response to the meta changes.

---

## Site-Wide Performance

### Overall 3-Month Metrics

| Metric | Week 2 (3mo to 2026-02-14) | Week 3 (3mo to 2026-02-23) | Change |
|--------|----------------------------|----------------------------|--------|
| Total Clicks | 19 | 15 | -4 (-21%) |
| Total Impressions | ~5,003 | ~4,698 | -305 (-6.1%) |
| Overall CTR | 0.38% | 0.32% | -0.06pp |

### Daily Site-Wide Impressions (Post-Change Period)

| Date | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| 2026-02-15 | 0 | 1 | 0% | 1.0 |
| 2026-02-16 | 0 | 3 | 0% | 11.3 |
| 2026-02-17 | 0 | 4 | 0% | 1.0 |
| 2026-02-18 | 0 | 0 | - | - |
| 2026-02-19 | 0 | 3 | 0% | 5.7 |
| 2026-02-20 | 0 | 0 | - | - |
| 2026-02-21 | 0 | 0 | - | - |

**Critical finding:** Daily impressions collapsed to near-zero from 2026-02-15 onwards. This is a dramatic drop from the January average of ~70-120 impressions per day.

### Top Pages (Current 3-Month Period)

| Page | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| /custom-inno-theme/ | 3 | 640 | 0.47% | 9.3 |
| CNC.pdf | 2 | 186 | 1.08% | 5.55 |
| /create-empty-folders-inno/ | 2 | 128 | 1.56% | 9.8 |
| /how-to-mock-a-function-that-returns-a-value/ | 2 | 71 | 2.82% | 23.93 |
| /flood-fill-opencv/ | 1 | 249 | 0.40% | 13.22 |
| /create-m3u-playlist-from-directory-list/ | 1 | 201 | 0.50% | 10.51 |
| /check-dotnet-framework-installed-inno-setup/ | 1 | 194 | 0.52% | 12.78 |
| Vacuum-Forming.pdf | 0 | 2,454 | 0% | 75.9 |

---

## Page Indexing Status (Critical)

The indexed page count has been in severe decline since late January.

| Date | Indexed Pages | Change |
|------|---------------|--------|
| 2025-12-24 | 29 | peak |
| 2026-01-14 | 28 | -1 |
| 2026-01-21 | 26 | -2 |
| 2026-01-25 | 21 | -5 |
| 2026-01-28 | 20 | -1 |
| 2026-02-01 | 18 | -2 |
| 2026-02-04 | 14 | -4 |
| 2026-02-08 | 13 | -1 |
| 2026-02-11 | 12 | -1 |
| 2026-02-15 | 10 | -2 |
| 2026-02-18 | 8 | -2 |

**This is the primary cause of the impression collapse.** At peak the site had 29 indexed pages; it now has only 8.

### Indexing Issues (2026-02-23 Snapshot)

| Issue | Week 2 (Feb 14) | Week 3 (Feb 23) | Change |
|-------|----------------|----------------|--------|
| Not found (404) | 41 | **42** | +1 |
| Crawled - currently not indexed | 24 | **25** | +1 |
| Excluded by 'noindex' tag | 22 | 18 | -4 |
| Page with redirect | 16 | 18 | +2 |
| Duplicate, Google chose different canonical | 17 | 16 | -1 |
| Alternative page with proper canonical tag | 6 | 6 | 0 |
| Blocked (403) | 4 | 4 | 0 |
| Duplicate without user-selected canonical | - | 1 | new |

---

## Docker Flask Article (Week 01 Ongoing)

The Docker Flask article (`/how-to-containerize-a-python-flask-application/`) does not appear in the Pages report or Queries report. It remains **unindexed** after 3+ weeks.

---

## Conclusions

1. **Week 02 experiment is inconclusive.** The 7-day window is too short to evaluate meta description changes against a 3-month baseline, especially given the site-wide disruption.

2. **The site has a critical indexing emergency.** Indexed pages dropped from 29 (December peak) to 8 (February 23), causing daily impressions to collapse from ~70-120/day to near-zero. This is the most urgent issue.

3. **42 pages return 404 errors.** These are the primary driver of index loss and the root cause of the traffic collapse. These are likely old URLs where slugs were updated without redirect configuration.

4. **The Week 02 meta changes are in place** and should continue to be monitored once the 404 situation is resolved.

## Recommendations

1. **Priority 1 — Fix 404 errors.** Identify all 42 404-returning URLs from GSC, find their current equivalents, and add 301 redirects. This is the Week 03 experiment.
2. **Priority 2 — Continue monitoring custom-inno-theme CTR.** Re-evaluate once indexed pages have recovered and daily impressions return to normal levels.
3. **Priority 3 — Investigate Docker Flask indexing.** Consider requesting re-indexing via Google Search Console URL Inspection tool.
