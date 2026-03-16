# Week 05 Tasks

## Experiment: Improve "Crawled – Currently Not Indexed" Pages

See full experiment details: [Week_05_Experiment_Fix_Crawled_Not_Indexed.md](Week_05_Experiment_Fix_Crawled_Not_Indexed.md)

### Tasks for This Week (Due by 2026-03-16):

1. **Audit target pages:** PENDING
   - Review frontmatter and content quality for each page in the target list
   - Check word count, headings, introduction, code explanation, and conclusion
   - Note which pages need the most work

2. **Improve `/flood-fill-opencv/` (primary target):** DONE 9th march 26
   - Expand the introduction to explain what flood fill is and its use cases
   - Add explanation of each `cvFloodFill` parameter
   - Add a section describing the expected output
   - Add/update frontmatter: title, description (120–160 chars), keywords, slug
   - Link to this page from at least 2 other OpenCV pages

3. **Update frontmatter on secondary target pages:** PENDING
   - `/create-empty-folders-inno/` — add/improve description and keywords - DONE 9th march 26
   - `/how-to-mock-a-function-and-confirm-the-function-was-called/` — add description - DONE 9th march 26
   - `/simple-box-code/` — add description and keywords - DONE 9th march 26
   - `/installing-inno-installer/` — add description and keywords
   - `/automatically-target-exe-version-inno/` — add description and keywords

4. **Add internal links:** DONE
   - Add links to target pages from related content pages
   - Prioritise flood-fill (link from threshold, contour, and gaussian pages)
   - Link Inno Setup pages from the Inno Setup hub/index

5. **Deploy and request re-indexing in GSC:** PENDING
   - Deploy to production
   - Use GSC → URL Inspection → "Request Indexing" for each improved page
   - Prioritise: flood-fill, create-empty-folders-inno, simple-box-code, mock-function-confirm

### Additional: Investigate 404 Regression

The Week 03 404 validation has reverted to "Failed". At least one URL (`/tag/containerize/`) was confirmed 404 on 2026-03-03:

- **Check whether `/tag/containerize/` has a redirect configured** — if not, add one
- **Review other WordPress tag and category URLs** to confirm they are all redirected
- **Check whether any other old WordPress URL patterns** may be missing from the redirect config

### Ongoing from Previous Weeks:

- **Week 03 monitoring:** 404 validation regressed to "Failed". Indexed pages dropped 8 → 6. Re-evaluate after content improvements are deployed and re-indexing is requested.
- **Week 02:** Monitor `/custom-inno-theme/` CTR — re-evaluate once daily impressions exceed 10/day
- **Week 01:** Check if Docker Flask article (`/how-to-containerize-a-python-flask-application/`) appears in GSC this week
