# Week 04 Experiment Review: Improve "Crawled – Currently Not Indexed" Pages

## Date: 2026-03-09

## Experiment Summary

- **Target:** 5 highest-value "Crawled – currently not indexed" pages
- **Primary target:** `/flood-fill-opencv/` (195 impressions, position 12.95)
- **Changes Made:** None — implementation was not started due to time constraints
- **Experiment Period:** 2026-03-02 to 2026-03-09 (planned)

## Result: Not Started

The Week 04 content improvement experiment **was not implemented**. All 5 tasks in `Week_04_Tasks.md` remain PENDING. No frontmatter, content quality, internal linking, or re-indexing requests were made during this period.

The Week 03 404-fix experiment continued to be monitored passively. Results from that experiment are documented below.

---

## Indexing Status Comparison

| Metric | Week 03 (2026-03-02) | Week 04 (2026-03-09) | Change |
|--------|----------------------|----------------------|--------|
| Indexed pages | 8 | 6 | -2 ⚠️ |
| Not found (404) | 42 (Validation: Started) | 43 (Validation: **Failed**) | +1 ⚠️ |
| Crawled - currently not indexed | 24 | 28 | +4 ⚠️ |
| Page with redirect | 18 | 21 | +3 |
| Duplicate, Google chose different canonical | 16 | 16 | — |
| Alternative page with proper canonical tag | 6 | 3 | -3 |
| Excluded by 'noindex' tag | 18 | 16 | -2 |
| Blocked (403) | 4 | 4 | — |

**All key metrics worsened this week.** The 404 validation status regressed from "Started" back to "Failed", and the indexed page count dropped from 8 to 6. The "Crawled – not indexed" count increased by 4, suggesting Google is crawling more pages but not promoting them to the index.

### Indexed Page Count (Chart Data)

Most recent data from the 2026-03-09 GSC export (GSC has a 5–7 day lag):

| Date | Indexed Pages |
|------|--------------|
| 2026-02-25 | 6 |
| 2026-03-01 | 6 |
| 2026-03-02 | 6 |
| 2026-03-03 | 6 |
| 2026-03-05 | 6 |
| 2026-03-07 | 6 |

> **Note:** The Week 03 review reported 8 indexed pages at 2026-03-02, based on data available in the earlier export (which only had data to 2026-02-24, when count was 8). The current export shows the indexed count had already dropped to 6 by 2026-02-25 — this was not visible at the time of the Week 03 review due to GSC data lag.

---

## Performance Data

### Daily Site-Wide Impressions (Week 4 Period)

| Date | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| 2026-03-02 | 0 | 0 | — | — |
| 2026-03-03 | 0 | 5 | 0% | 9.6 |
| 2026-03-04 | 0 | 0 | — | — |
| 2026-03-05 | 0 | 4 | 0% | 11.0 |
| 2026-03-06 | 0 | 0 | — | — |
| 2026-03-07 | 0 | 0 | — | — |

Daily impressions remain near-zero. No recovery signal.

### 3-Month Aggregate

| Metric | Week 03 (3mo to 2026-02-23) | Week 04 (3mo to 2026-03-02) | Week 05 (3mo to 2026-03-09) | Change (W04→W05) |
|--------|----------------------------|----------------------------|----------------------------|-----------------|
| Total Clicks | 15 | 15 | 13 | -2 |
| Total Impressions | ~4,698 | ~4,233 | ~3,967 | -266 (-6.3%) |
| Overall CTR | 0.32% | 0.35% | 0.33% | -0.02pp |

The rolling 3-month window continues to shed high-impression days from late 2025, causing aggregate impressions to decline. Clicks also fell.

### Top Pages (Current 3-Month Period, ending 2026-03-09)

| Page | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| /custom-inno-theme/ | 3 | 543 | 0.55% | 9.38 |
| /wp-content/uploads/.../CNC.pdf | 2 | 142 | 1.41% | 5.13 |
| /create-empty-folders-inno/ | 2 | 109 | 1.83% | 9.89 |
| /flood-fill-opencv/ | 1 | 195 | 0.51% | 12.95 |
| /wp-content/uploads/.../Iterative-Design-Process.pdf | 1 | 151 | 0.66% | 62.0 |
| /check-dotnet-framework-installed-inno-setup/ | 1 | 150 | 0.67% | 14.04 |
| /how-to-mock-a-function-that-returns-a-value/ | 1 | 62 | 1.61% | 25.1 |
| /simple-box-code/ | 1 | 39 | 2.56% | 7.67 |
| /wp-content/uploads/.../Vacuum-Forming.pdf | 0 | 2,129 | 0% | 76.84 |

---

## 404 Fix Status (Week 03 Experiment — Ongoing Monitoring)

The 404 validation status has **regressed from "Started" back to "Failed"**.

Key findings from the 2026-03-09 validation export:
- **43 of 43 URLs:** status "Pending" (not yet re-crawled by Google, crawl dates mostly from January–February)
- **1 URL:** `http://www.andrew-seaford.co.uk/tag/containerize/` — crawled 2026-03-03, status **Failed**

The "tag/containerize/" page is a WordPress tag archive that was never redirected in the Docusaurus implementation. This is a 404 that was not addressed by the Week 03 fix. The validation failure likely reflects Google evaluating this specific URL.

The remaining 43 URLs remain "Pending" — Google has not yet re-crawled them to verify the redirects. The 2-week re-crawl window has now elapsed with no confirmed improvement.

---

## Assessment Against Hypothesis

### Week 04 Experiment (Content Improvement)

| Hypothesis | Status |
|-----------|--------|
| Frontmatter will be updated on 5 target pages | ⏳ PENDING — not implemented |
| Content quality will be expanded on /flood-fill-opencv/ | ⏳ PENDING — not implemented |
| Internal links will be added to target pages | ⏳ PENDING — not implemented |
| Re-indexing will be requested in GSC | ⏳ PENDING — not implemented |
| 3–5 pages move from "Crawled – not indexed" to "Indexed" | ⏳ PENDING — not implemented |

### Week 03 Experiment (404 Fix — Monitoring)

| Hypothesis | Status |
|-----------|--------|
| 301 redirects implemented | ✅ Done |
| Google acknowledges fix | ✅ Validation changed to "Started" (then regressed to "Failed") |
| 404 count decreases | ❌ Increased by 1 (42 → 43) |
| Indexed pages recover towards 20+ | ❌ Decreased further (8 → 6) |
| Daily impressions recover to 50+/day | ❌ Still near-zero (0–5/day) |

---

## Conclusions

1. **Week 04 implementation did not happen.** All content improvement tasks carry forward to Week 05 unchanged.

2. **The 404 fix is in a worse state than expected.** Validation has reverted to "Failed". One confirmed bad URL (`/tag/containerize/`) indicates at least one redirect was missed. The remaining 43 pages are "Pending" — their redirect targets have not yet been re-verified by Google's crawlers.

3. **The indexed count continues to decline** (8 → 6), suggesting Google is actively removing pages from its index as it crawls and finds redirect issues or thin content. This is the most critical signal to address.

4. **Week 05 priorities:**
   - Investigate and fix the `/tag/containerize/` 404 (and any other missed WordPress tag/category URLs)
   - Carry forward all 5 content improvement tasks from Week 04
   - Continue monitoring 404 validation progress
