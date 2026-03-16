# Week 04 Experiment: Improve Content Quality to Fix "Crawled – Currently Not Indexed" Pages

## Date: 2026-03-02

## Background

The site currently has 24 pages with the status "Crawled – currently not indexed". Google has crawled these pages but decided not to add them to its index. This is typically caused by:

- **Thin content** — too short, not enough unique value
- **Poor quality signals** — weak title, no meta description, unclear structure
- **Low E-E-A-T** — insufficient depth to demonstrate expertise
- **Missing frontmatter** — no title or description for Google to use as a snippet

These pages are costing the site significant ranking potential. Several of them already appear in the performance data with meaningful impressions — meaning Google's crawlers consider them relevant for searches, but the content isn't strong enough to warrant a permanent index position.

With the Week 03 404 fix already in Google's validation pipeline, this is the most productive parallel experiment to run while waiting for the indexing recovery.

## Target

**Primary:** `/flood-fill-opencv/`
- 220 impressions (3-month period ending 2026-03-02)
- Position 12.83 — first-page territory if properly indexed
- CTR: 0.45% — low, also needs a better title/description
- Currently: "Crawled – currently not indexed"

**Secondary targets** (all confirmed to exist in the current Docusaurus site):

| Page | Impressions | CTR | Position |
|------|-------------|-----|----------|
| /create-empty-folders-inno/ | 116 | 1.72% | 9.75 |
| /how-to-mock-a-function-and-confirm-the-function-was-called/ | 56 | 0% | 21.98 |
| /simple-box-code/ | 43 | 2.33% | 7.3 |
| /installing-inno-installer/ | 23 | 0% | 23.04 |
| /oracle-insert-date/ | unknown | — | — |
| /explicit-conversion-string-integer-csharp/ | unknown | — | — |
| /how-to-use-extension-methods-in-c/ | 3 | 0% | 16.67 |
| /automatically-target-exe-version-inno/ | unknown | — | — |

## Aim

To get key "Crawled – currently not indexed" pages into Google's main index by improving their content quality, which will increase the total indexed page count and restore organic traffic.

## Hypothesis

By expanding thin content and improving frontmatter (title, meta description, keywords) on the 5 highest-value "Crawled – currently not indexed" pages, Google will judge these pages as indexable within 2 weeks, resulting in:

1. At least 3–5 of the target pages moving from "Crawled – not indexed" to "Indexed"
2. Indexed page count recovering from 8 to 12–15+ (in combination with the ongoing 404 fix)
3. Daily impressions recovering from near-zero to 20–50+/day as more pages enter the index

## Baseline Data (2026-03-02)

- **Indexed pages:** 8
- **Crawled – currently not indexed:** 24
- **Daily impressions (last 7 days):** 0–2/day
- **Total weekly clicks:** 0

## Metrics to Track

- **Primary:** Number of "Crawled – currently not indexed" pages (target: reduce from 24 to 18 or fewer)
- **Secondary:** Indexed page count (target: 12+ in combination with 404 recovery)
- **Tertiary:** Daily impressions recovering (target: 20+/day)

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

Add internal links **to** the target pages from other related pages. This signals to Google that these pages are part of a coherent site structure:

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

2 weeks (2026-03-02 to 2026-03-16). Google typically processes URL inspection requests within a few days; the indexing decision may take up to 2 weeks.

## Week 04 Tasks

See [Week_04_Tasks.md](Week_04_Tasks.md)

## Ongoing Tasks from Previous Weeks

- **Week 03:** Continue monitoring 404 recovery — expected to show visible improvement by 2026-03-09. If 404 count is still 42 next week, investigate whether Google crawled the redirected URLs.
- **Week 02:** Monitor `/custom-inno-theme/` CTR once impressions recover
- **Week 01:** Monitor Docker Flask article for first GSC appearance

## Expected Outcome

Within 2 weeks of deploying content improvements and requesting re-indexing:

- 3–5 currently not-indexed pages move into the index
- Total indexed page count: 12–18 (combining 404 recovery + new indexing)
- Daily impressions: recovering from near-zero to 20–50+/day

## Risk Assessment

- **Low risk:** Content improvements are always beneficial — expanding thin content and improving frontmatter cannot hurt rankings
- **Reversible:** All changes are in markdown files and can be reverted via git
- **Cumulative benefit:** Even if some pages remain not-indexed, improving them sets a better foundation for future CTR experiments
- **Dependency:** Full recovery depends on both this experiment and the Week 03 404 fix completing together
