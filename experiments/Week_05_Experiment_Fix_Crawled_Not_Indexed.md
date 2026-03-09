# Week 05 Experiment: Improve Content Quality to Fix "Crawled – Currently Not Indexed" Pages

## Date: 2026-03-09

## Background

This is a carry-forward of the Week 04 experiment, which was planned but never implemented. The hypothesis and target pages remain the same. The baseline data has been updated from the 2026-03-09 GSC export.

**Key context from Week 04 review:**
- Indexed pages dropped from 8 → 6 during the Week 04 period (no content improvements were made)
- "Crawled – not indexed" count increased from 24 → 28 (Google is crawling more pages but rejecting them)
- The 404 validation status regressed to "Failed" — this is a concurrent concern being tracked separately
- The Week 04 content improvement experiment was not started; all tasks remain PENDING

## Target

**Primary:** `/flood-fill-opencv/`
- 195 impressions (3-month period ending 2026-03-09)
- Position 12.95 — borderline first-page if properly indexed
- CTR: 0.51% — low, needs better title/description
- Currently: "Crawled – currently not indexed"

**Secondary targets** (all confirmed present in the current Docusaurus site):

| Page | Impressions | CTR | Position |
|------|-------------|-----|----------|
| /create-empty-folders-inno/ | 109 | 1.83% | 9.89 |
| /how-to-mock-a-function-and-confirm-the-function-was-called/ | 52 | 0% | 22.94 |
| /simple-box-code/ | 39 | 2.56% | 7.67 |
| /installing-inno-installer/ | 17 | 0% | 14.0 |
| /automatically-target-exe-version-inno/ | unknown | — | — |

## Aim

To get key "Crawled – currently not indexed" pages into Google's main index by improving their content quality, which will increase the total indexed page count and help restore organic traffic.

## Hypothesis

By expanding thin content and improving frontmatter (title, meta description, keywords) on the 5 highest-value "Crawled – currently not indexed" pages, Google will judge these pages as indexable within 2 weeks, resulting in:

1. At least 3–5 of the target pages moving from "Crawled – not indexed" to "Indexed"
2. Indexed page count recovering from 6 to 10+ (in combination with any 404 fix progress)
3. Daily impressions beginning to recover from near-zero

## Baseline Data (2026-03-09)

- **Indexed pages:** 6
- **Crawled – currently not indexed:** 28 (increased from 24 the prior week)
- **Daily impressions (last 7 days):** 0–5/day
- **Total weekly clicks:** 0

## Metrics to Track

- **Primary:** Number of "Crawled – currently not indexed" pages (target: reduce from 28 to 22 or fewer)
- **Secondary:** Indexed page count (target: 10+ in combination with 404 recovery)
- **Tertiary:** Daily impressions recovering (target: 10+/day as a first step)

## Changes to Implement

### Step 1: Audit Frontmatter on Target Pages

For each target page, check the current frontmatter. Each page should have:

```yaml
---
title: "Descriptive, keyword-rich title (50–60 characters)"
description: "Clear summary of what the page covers, including the primary keyword (120–160 characters)"
keywords: [keyword1, keyword2, keyword3]
slug: /page-slug/
---
```

### Step 2: Content Quality Review

For each target page, assess:

- **Word count:** Is the main content too thin? (target: 300+ meaningful words)
- **Structure:** Does it have clear headings (H2, H3)?
- **Code examples:** Are they complete, correct, and explained?
- **Introduction:** Does it clearly state what the page is about and who it's for?
- **Conclusion/summary:** Does it have a clear takeaway?

### Step 3: Content Improvements

For the primary target `/flood-fill-opencv/`:
1. Expand the introduction to explain what flood fill is and why it's useful
2. Add a brief explanation of each parameter in the `cvFloodFill` call
3. Add a section describing the output/expected result
4. Add a short conclusion linking to related OpenCV topics

For secondary targets, at minimum:
1. Update/add frontmatter with optimised title, description, and keywords
2. Ensure the introduction clearly states the page topic
3. Add any missing structural sections (intro, code, explanation, result)

### Step 4: Internal Linking

Add internal links **to** the target pages from other related pages:

- Link to `/flood-fill-opencv/` from other OpenCV pages (`/threshold-image-opencv/`, `/image-contour-detection-display-opencv/`, etc.)
- Link to Inno Setup pages from the Inno Setup index/hub
- Link to JavaScript mock pages from related testing pages

### Step 5: Request Re-indexing in GSC

After deploying the content improvements:
1. Open Google Search Console → URL Inspection
2. Search each improved URL
3. Click "Request Indexing"
4. Prioritise the primary target and the top 4–5 secondary targets

## Experiment Duration

2026-03-09 to 2026-03-16 (1 week).

## Week 05 Tasks

See [Week_05_Tasks.md](Week_05_Tasks.md)

## Concurrent Concerns

- **404 fix (Week 03):** The validation has regressed to "Failed". One confirmed broken URL (`/tag/containerize/`) needs a redirect. The remaining 43 pending URLs need to be recrawled. This is tracked separately but may interact with these results.
- **Week 02:** Monitor `/custom-inno-theme/` CTR once impressions recover
- **Week 01:** Monitor Docker Flask article for first GSC appearance

## Expected Outcome

Within 2 weeks of deploying content improvements and requesting re-indexing:

- 3–5 currently not-indexed pages move into the index
- Total indexed page count: 10–12 (combining content improvements + any 404 recovery)
- Daily impressions: beginning to recover from near-zero to 10–20+/day

## Risk Assessment

- **Low risk:** Content improvements are always beneficial — expanding thin content and improving frontmatter cannot hurt rankings
- **Reversible:** All changes are in markdown files and can be reverted via git
- **Cumulative benefit:** Even if some pages remain not-indexed, improving them sets a better foundation for future CTR experiments
- **Dependency:** Full recovery also depends on the 404 fix completing, but content improvements provide independent value
