# Week 3 Tasks

## Experiment: Fix 404 Errors — Indexing Recovery

See full experiment details: [Week_03_Experiment_Fix_404_Indexing_Recovery.md](Week_03_Experiment_Fix_404_Indexing_Recovery.md)

### Tasks for This Week (Due by 2026-03-02):

1. **Export 404 URL List:** PENDING
   - In GSC → Index → Pages → filter by "Not found (404)"
   - Export or note all 42 URLs currently returning 404

2. **Map Old URLs to Current URLs:** PENDING
   - For each 404 URL, find the correct current URL on the site
   - Check git log for slug changes: `git log --all --oneline`
   - Cross-reference with sitemap

3. **Configure 301 Redirects:** PENDING
   - Add redirect rules to Docusaurus config using `@docusaurus/plugin-client-redirects`
   - Target: reduce 404 count from 42 to 0

4. **Deploy and Verify:** PENDING
   - Deploy changes to production
   - Manually test that old URLs redirect to new URLs with HTTP 301

5. **Submit Sitemap in GSC:** PENDING
   - Resubmit sitemap at Google Search Console → Sitemaps
   - Use URL Inspection tool to request re-indexing on 5-10 key pages

### Ongoing from Previous Weeks:

- **Week 02:** Monitor `/custom-inno-theme/` CTR (changes live, needs indexing to recover first)
- **Week 01:** Docker Flask article (`/how-to-containerize-a-python-flask-application/`) — still unindexed, use GSC URL Inspection to request indexing
