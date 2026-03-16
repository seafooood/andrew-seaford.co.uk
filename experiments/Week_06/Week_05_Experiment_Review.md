# Week 05 Experiment Review

## Summary

The Week 05 experiment focused on improving thin content and internal linking to recover indexed page count. The experiment was **not successful** — indexed pages fell from 6 to 4 during this period.

---

## Baseline vs Current Data

| Metric | Baseline (Week 05 start) | Current (2026-03-16) | Change |
|--------|--------------------------|----------------------|--------|
| Indexed pages | 6 | 4 | -2 (regression) |
| Total clicks | — | 1 | — |
| Total impressions | — | ~1,900+ | — |

The indexed page count dropped further despite the content improvements. Only four pages are currently indexed:

- `http://www.andrew-seaford.co.uk/revision/gsce-computer-science/` (14 Dec 2025)
- `http://www.andrew-seaford.co.uk/wp-content/uploads/2021/03/Smart-Materials.pdf` (26 Nov 2025)
- `http://www.andrew-seaford.co.uk/wp-content/uploads/2021/03/The-Six-Rs.pdf` (26 Nov 2025)
- `http://www.andrew-seaford.co.uk/wp-content/uploads/2021/03/Pulleys-and-Belts.pdf` (26 Nov 2025)

Note: all four indexed pages are from the old WordPress site, not the new Docusaurus site.

---

## Tasks Completed

- Expanded flood-fill blog post content
- Updated frontmatter (`title`, `description`, `keywords`) for:
  - `inno-setup-mock`
  - `inno-setup-simple-box`
  - `inno-setup-introduction`
- Added internal links between related blog posts

## Tasks Not Completed

- Frontmatter updates for `installing-inno-installer` and `automatically-target-exe-version-inno`
- Re-indexing was not confirmed as submitted in Google Search Console

---

## Conclusion

The experiment was **partially implemented and did not succeed**. Indexed pages fell from 6 to 4 — moving in the wrong direction.

The content quality improvements on the Docusaurus site were real, but they did not address the root cause. The GSC data points to a different problem entirely: **missing content, not thin content**.

---

## Key Insight from GSC Data

The top queries by impressions tell a clear story:

| Query | Clicks | Impressions |
|-------|--------|-------------|
| vacuum forming | 0 | 927 |
| vacuum form | 0 | 141 |
| vacuum formed | 0 | 127 |
| what is vacuum forming | 0 | 122 |
| vacuum moulding | 0 | 86 |

927 impressions for "vacuum forming" with 0 clicks means Google is showing the site in results but there is no page to land on. The GCSE revision content (including vacuum forming notes) existed on the old WordPress site but was never migrated to the new Docusaurus site.

The indexed URL `http://www.andrew-seaford.co.uk/revision/gsce-computer-science/` confirms Google remembers the old revision section. The PDFs (`Smart-Materials.pdf`, `Pulleys-and-Belts.pdf`, `The-Six-Rs.pdf`) are indexed at their old WordPress upload paths — but those URLs no longer serve content on the new site.

**The primary problem is missing GCSE revision content, not thin content on existing pages.** Week 06 will address this directly.
