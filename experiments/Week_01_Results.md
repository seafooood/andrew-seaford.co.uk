# Week 01 Experiment Results: Docker Flask CTR Optimization

## Date: 2026-02-16

## Experiment Summary

- **Target Article:** `/docs/docker/How To Containerize A Python Flask Application`
- **Changes Made:** Added Docusaurus frontmatter (title, description, keywords, slug) on 2026-02-09
- **Experiment Period:** 2026-02-09 to 2026-02-16

## Result: Inconclusive

The Docker Flask article **does not appear** in the Google Search Console Pages report for either the Week 1 (2026-02-09) or Week 2 (2026-02-16) data exports. No Docker or Flask-related queries appear in the Queries report either.

**The article has not yet been indexed by Google.** This is not unexpected for a small site where the article previously had zero SEO metadata and zero search presence. Google typically takes 1-4 weeks to crawl, index, and begin showing a page in search results.

### Experiment-Period Daily Data (2026-02-08 to 2026-02-14)

| Date | Clicks | Impressions | CTR | Avg Position |
|------|--------|-------------|-----|-------------|
| 2026-02-08 | 0 | 40 | 0% | 73.9 |
| 2026-02-09 | 0 | 36 | 0% | 63.3 |
| 2026-02-10 | 0 | 25 | 0% | 73.0 |
| 2026-02-11 | 0 | 35 | 0% | 69.7 |
| 2026-02-12 | 0 | 56 | 0% | 74.3 |
| 2026-02-13 | 0 | 7 | 0% | 48.6 |
| 2026-02-14 | 0 | 0 | - | - |
| **Total** | **0** | **199** | **0%** | - |

Note: This is site-wide data. The target article contributed 0 impressions to these totals.

## Overall Site Performance Comparison

Both exports use a rolling 3-month window, so they overlap significantly. Changes are marginal.

| Metric | Week 1 Export (ending 2026-02-07) | Week 2 Export (ending 2026-02-14) | Change |
|--------|-----------------------------------|-----------------------------------|--------|
| Total Clicks | 19 | 19 | 0 |
| Total Impressions | 5,098 | 5,003 | -95 (-1.9%) |
| Overall CTR | 0.37% | 0.38% | +0.01pp |
| Desktop Clicks | 18 | 18 | 0 |
| Desktop Impressions | 4,679 | 4,595 | -84 |
| Mobile Clicks | 1 | 1 | 0 |
| Mobile Impressions | 394 | 380 | -14 |

### Top Pages Performance (Week 2)

| Page | Clicks | Impressions | CTR | Position |
|------|--------|-------------|-----|----------|
| /custom-inno-theme/ | 5 | 684 | 0.73% | 9.2 |
| /create-m3u-playlist-from-directory-list/ | 2 | 241 | 0.83% | 10.7 |
| /check-dotnet-framework-installed-inno-setup/ | 1 | 208 | 0.48% | 12.7 |
| Vacuum-Forming.pdf | 0 | 2,587 | 0% | 75.4 |
| /create-empty-folders-inno/ | 3 | 138 | 2.17% | 9.5 |
| /flood-fill-opencv/ | 1 | 272 | 0.37% | 12.9 |
| /how-to-mock-a-function-that-returns-a-value/ | 2 | 76 | 2.63% | 23.8 |
| CNC.pdf | 2 | 203 | 0.99% | 5.7 |
| Iterative-Design-Process.pdf | 1 | 182 | 0.55% | 59.0 |

## Page Indexing Trend (Concerning)

| Metric | Week 1 (2026-02-07) | Week 2 (2026-02-14) | Change |
|--------|---------------------|---------------------|--------|
| Indexed Pages | 14 | 12 | -2 |
| Not Indexed Pages | 130 | 132 | +2 |

### Indexing Issues Comparison

| Issue | Week 1 | Week 2 | Change |
|-------|--------|--------|--------|
| Not found (404) | 37 | 41 | +4 |
| Excluded by 'noindex' tag | 28 | 22 | -6 |
| Page with redirect | 17 | 16 | -1 |
| Alternative page with proper canonical tag | 7 | 6 | -1 |
| Blocked due to access forbidden (403) | 2 | 4 | +2 |
| Duplicate, Google chose different canonical | 18 | 17 | -1 |
| Crawled - currently not indexed | 18 | 24 | +6 |

Key observations:
- **Indexed pages decreased** from 14 to 12, which is a negative signal
- **"Crawled - currently not indexed" increased by 6 pages** — Google is crawling pages but choosing not to index them
- **404 errors increased by 4** — there may be broken links or removed pages that need attention
- **403 errors doubled** from 2 to 4 — some pages are blocking Google's crawler
- Validation has been "Started" for 404 and noindex issues in the Week 2 data

## Conclusions

1. **The Week 01 experiment is inconclusive.** The Docker Flask article has not been indexed by Google within the 7-day experiment window. This is a normal timeframe issue, not a failure of the approach.

2. **The site's overall performance is flat.** 19 clicks across both periods with ~5,000 impressions. The site-wide CTR of ~0.38% is very low.

3. **The indexing health is declining.** The drop from 14 to 12 indexed pages and the increase in "crawled but not indexed" pages is a concern that should be investigated.

4. **The biggest CTR opportunity is on pages that already rank.** Pages like `/custom-inno-theme/` (position 9.2, 0.73% CTR) and `/flood-fill-opencv/` (position 12.9, 0.37% CTR) have significant impression volume but very low CTR, likely due to missing or poor meta descriptions.

## Recommendations

1. **Continue monitoring the Docker Flask article** for another 1-2 weeks before concluding the experiment.
2. **Apply the same frontmatter optimization to pages that already have search presence**, where results can be measured immediately.
3. **Investigate the 404 and 403 errors** in the Page Indexing report to stop the decline in indexed pages.
4. **Address the "crawled but not indexed" issue** — 24 pages is a significant number for a small site.
