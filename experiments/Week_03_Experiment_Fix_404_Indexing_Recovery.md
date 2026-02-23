# Week 03 Experiment: Fix 404 Errors to Recover Indexed Page Count

## Date: 2026-02-23

## Background

The site is experiencing a critical indexing collapse. Indexed pages have dropped from **29 (December 2025 peak) to 8 (February 2026)**, causing daily impressions to fall from ~70-120/day to near-zero. The primary cause is **42 pages returning 404 errors** — likely old URLs whose slugs were updated without corresponding 301 redirects being configured.

Until this is resolved, all other CTR experiments are undermined: there are simply not enough pages appearing in search results to measure any improvements.

## Target

**Site-wide:** All pages currently returning 404 as reported by Google Search Console Page Indexing.

## Aim

To recover the indexed page count and restore organic impressions to pre-decline levels by fixing 404 errors and ensuring Google can find the current versions of all pages.

## Hypothesis

By implementing 301 redirects from all 404 URLs to their current equivalents, Google will:
1. Re-crawl and re-index the redirected pages
2. Restore the indexed page count from 8 back towards the December peak of 29
3. Restore daily impressions from near-zero back to 70-120+ per day within 2-4 weeks

## Baseline Data

From Google Search Console Page Indexing (2026-02-23):

- **Indexed pages:** 8
- **Not found (404):** 42 pages
- **Page with redirect:** 18 pages (some redirects may already be misconfigured)
- **Crawled - currently not indexed:** 25 pages
- **Daily impressions (2026-02-16 to 2026-02-21):** 3, 4, 0, 3, 0, 0

## Metrics to Track

- **Primary:** Number of indexed pages (target: recover to 20+)
- **Secondary:** Daily impressions (target: recover to 50+ per day)
- **Tertiary:** Number of 404 errors (target: reduce from 42 to 0)

## Changes to Implement

### Step 1: Audit 404 URLs

Export the full list of 404 URLs from Google Search Console:
1. Go to GSC → Index → Pages
2. Filter by "Not found (404)"
3. Note all URLs that need to be redirected

### Step 2: Identify Current URL for Each 404 Page

For each 404 URL, determine the correct current URL by:
1. Checking the current site structure
2. Checking the git log for slug changes (`git log --all --oneline -- docs/`)
3. Cross-referencing with the sitemap

### Step 3: Configure 301 Redirects

The site uses Docusaurus. Add redirects in the Docusaurus config:

```js
// docusaurus.config.js
redirects: [
  {
    from: '/old-slug/',
    to: '/new-slug/',
  },
  // ... additional redirects
],
```

Or use the `@docusaurus/plugin-client-redirects` plugin if not already installed:

```bash
npm install @docusaurus/plugin-client-redirects
```

Then configure in `docusaurus.config.js`:

```js
plugins: [
  [
    '@docusaurus/plugin-client-redirects',
    {
      redirects: [
        { from: '/old-url/', to: '/new-url/' },
        // ...
      ],
    },
  ],
],
```

### Step 4: Submit Updated Sitemap

After deploying redirects:
1. Verify the sitemap at `/sitemap.xml` contains only valid current URLs
2. In Google Search Console → Sitemaps → resubmit the sitemap URL
3. Use URL Inspection tool on key pages to request re-indexing

### Step 5: Monitor Recovery

Check GSC Page Indexing weekly to track:
- 404 count decreasing
- Indexed page count recovering
- Daily impressions recovering

## Experiment Duration

2 weeks (2026-02-23 to 2026-03-09). Google typically takes 1-2 weeks to re-crawl and re-index after redirects are in place.

## Week 03 Tasks

1. [ ] Export full list of 404 URLs from GSC Page Indexing report
2. [ ] Map each 404 URL to its correct current URL
3. [ ] Configure 301 redirects in Docusaurus config
4. [ ] Deploy changes and verify redirects work
5. [ ] Resubmit sitemap in Google Search Console
6. [ ] Use GSC URL Inspection to manually request re-indexing for 5-10 key pages

## Ongoing Tasks from Previous Weeks

- Continue monitoring `/custom-inno-theme/` CTR (Week 02 experiment — result pending until indexing recovers)
- Continue monitoring Docker Flask article (`/how-to-containerize-a-python-flask-application/`) for first appearance in GSC (Week 01 experiment — still unindexed)

## Expected Outcome

Within 2 weeks of implementing redirects:
- 404 errors reduced to near-zero
- Indexed pages recovering towards 20+
- Daily impressions recovering towards 50-100/day
- The site's overall visibility in Google Search restored

## Risk Assessment

- **Low risk:** Adding 301 redirects is a standard, reversible change
- **No downside:** Fixing 404s cannot hurt rankings; it can only help
- **Time to results:** Google crawls are not instant — allow 1-2 weeks for full recovery

## Additional Notes

- The Week 02 custom-inno-theme changes are already live and will benefit once the site is properly indexed again
- The vacuum forming PDF (Vacuum-Forming.pdf) has 2,454 impressions but ranks at position 75.9 — this represents a future opportunity once technical issues are resolved
- Once indexed pages stabilize, consider Week 04 experiment targeting the `/flood-fill-opencv/` page (249 impressions, 0.4% CTR, position 13.22) or `/create-m3u-playlist-from-directory-list/` (201 impressions, 0.5% CTR, position 10.51)
