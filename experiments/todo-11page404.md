# 11. 404 Page Offers No Recovery Path

**Problem:** The 404 page shows a generic message ("We could not find what you were looking for.") with no suggestions, no search, and no links to popular content.

**Fix:** Create a custom 404 page (`src/pages/404.js`) that includes:
- Links to the tutorials index and popular articles
- A search box (if Docusaurus search is configured)
- Recent blog posts

**Impact:** Low-medium - improves user retention when landing on broken links.
