# Week 02 Experiment: "Custom Inno Theme" CTR Optimization

## Date: 2026-02-16

## Target Article
`/docs/inno/custom-inno-theme/`

## Rationale for Selection
This page was selected because it represents the **highest-impact CTR optimization opportunity** on the site:
- **684 impressions** (highest of any webpage, excluding PDFs)
- **Only 5 clicks** and **0.73% CTR** — very low for a page ranking at position 9.2
- Typical CTR for position ~9 in Google is 2-4%, so there is significant room for improvement
- The page already has a title and slug in its frontmatter but is **missing a meta description and keywords**
- Google is likely auto-generating a poor snippet from the page content

### Relevant Queries (from GSC Week 2 data)
These Inno Setup related queries are driving impressions across the site, many likely to this page:

| Query | Impressions | Position |
|-------|-------------|----------|
| inno setup wizardimagefile size 164 314 | 59 | 10.85 |
| inno setup wizardimagefile size | 29 | 4.59 |
| inno setup wizardimagefile size 164x314 | 11 | 10.36 |
| wizardimagefile | 6 | 11.0 |
| inno setup | 4 | 9.75 |
| inno setup installer | 2 | 13.0 |
| inno setup wizardsmallimagefile size 55x55 | 2 | 10.0 |

## Aim
To improve the organic Click-Through Rate (CTR) of the "Custom Inno Theme" page by optimizing its meta title, description, and keywords.

## Hypothesis
By adding an optimized meta description and keywords, and refining the meta title to better match user search intent, we will increase the page's CTR from 0.73% to at least 1.5% over the next week.

## Proposed Changes

### Meta Title Optimization
- **Current:** `Custom Inno Theme` (18 chars — too short, generic, doesn't match search intent)
- **Proposed:** `Customize Inno Setup Installer Images: WizardImageFile Guide` (60 chars — includes key search terms, action-oriented)

### Meta Description Optimization
- **Current:** None (Google auto-generates a snippet from page content)
- **Proposed:** `Customize your Inno Setup installer with custom images using WizardImageFile and WizardSmallImageFile. Includes correct image sizes and BMP format guide.` (154 chars — under 160 char limit, includes key terms and clear value proposition)

### Keywords Added
`inno setup custom images`, `wizardimagefile`, `wizardsmallimagefile`, `inno setup theme`, `inno setup installer images`, `inno setup wizard image size`

## Baseline Data
From Google Search Console Performance report (3 months ending 2026-02-14):

- **URL:** `http://www.andrew-seaford.co.uk/custom-inno-theme/`
- **Clicks:** 5
- **Impressions:** 684
- **CTR:** 0.73%
- **Average Position:** 9.2

## Metrics to Track
- **Primary:** Organic Click-Through Rate (CTR) for the `/custom-inno-theme/` URL
- **Secondary:** Impressions, Total Clicks, Average Position for WizardImageFile-related queries

## Changes to Implement

Update the frontmatter of `/docs/inno/custom-inno-theme/index.md`:

```yaml
---
title: "Customize Inno Setup Installer Images: WizardImageFile Guide"
description: "Customize your Inno Setup installer with custom images using WizardImageFile and WizardSmallImageFile. Includes correct image sizes and BMP format guide."
keywords: [inno setup custom images, wizardimagefile, wizardsmallimagefile, inno setup theme, inno setup installer images, inno setup wizard image size]
date: 2015-02-12
categories:
  - "inno"
slug: "custom-inno-theme"
---
```

## Experiment Duration
1 week (2026-02-16 to 2026-02-23), after which new data will be collected and analyzed.

## Expected Outcome
Unlike the Week 01 experiment (which targeted an unindexed page), this page **already ranks on page 1** and has significant impression volume. We should see measurable CTR changes within the experiment period because:
- The page is already indexed and receiving impressions
- Google typically updates snippets within days of meta description changes
- The improved title and description should better match the search queries driving impressions

## Advantages Over Week 01 Experiment
1. **Existing search presence** — the page is already indexed at position 9.2
2. **High impression volume** — 684 impressions gives statistical significance
3. **Clear baseline** — 0.73% CTR is a measurable starting point
4. **Strong keyword match** — the proposed title directly targets the queries appearing in GSC data

## Additional Notes
- Continue monitoring the Week 01 Docker Flask article for indexing progress
- Address the declining indexed page count (14 → 12) and rising 404 errors as a separate task
