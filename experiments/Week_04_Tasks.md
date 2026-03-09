# Week 4 Tasks

## Experiment: Improve "Crawled – Currently Not Indexed" Pages

See full experiment details: [Week_04_Experiment_Fix_Crawled_Not_Indexed.md](Week_04_Experiment_Fix_Crawled_Not_Indexed.md)

### Tasks for This Week (Due by 2026-03-09):

1. **Audit target pages:** PENDING
   - Review frontmatter and content quality for each page in the target list
   - Check word count, headings, introduction, code explanation, and conclusion
   - Note which pages need the most work

2. **Improve `/flood-fill-opencv/` (primary target):** PENDING
   - Expand the introduction to explain what flood fill is and its use cases
   - Add explanation of each `cvFloodFill` parameter
   - Add a section describing the expected output
   - Add/update frontmatter: title, description (120–160 chars), keywords, slug
   - Link to this page from at least 2 other OpenCV pages

3. **Update frontmatter on secondary target pages:** PENDING
   - `/create-empty-folders-inno/` — add/improve description and keywords
   - `/how-to-mock-a-function-and-confirm-the-function-was-called/` — add description
   - `/simple-box-code/` — add description and keywords
   - `/installing-inno-installer/` — add description and keywords
   - `/automatically-target-exe-version-inno/` — add description and keywords

4. **Add internal links:** PENDING
   - Add links to target pages from related content pages
   - Prioritise flood-fill (link from threshold, contour, and gaussian pages)
   - Link Inno Setup pages from the Inno Setup hub/index

5. **Deploy and request re-indexing in GSC:** PENDING
   - Deploy to production
   - Use GSC → URL Inspection → "Request Indexing" for each improved page
   - Prioritise: flood-fill, create-empty-folders-inno, simple-box-code, mock-function-confirm

### Ongoing from Previous Weeks:

- **Week 03 monitoring:** Check GSC Page Indexing on 2026-03-09 — look for 404 count to start decreasing. If still 42, investigate whether redirects are working correctly.
- **Week 02:** Monitor `/custom-inno-theme/` CTR — re-evaluate once daily impressions exceed 20/day
- **Week 01:** Check if Docker Flask article (`/how-to-containerize-a-python-flask-application/`) appears in GSC this week
