# 8. Structured Data: Empty Author and Keywords

**Problem:** The Blog schema JSON-LD on the homepage has empty `author` and `keywords` arrays for all blog posts:
```json
{
  "@type": "BlogPosting",
  "author": [],
  "keywords": []
}
```

Search engines use author information for E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) signals.

**Fix:**

- [x] Add `authors: [andrewseaford]` front matter to all 6 blog posts (`/home/andrew/Code/andrew-seaford.co.uk/blog`). The `authors.yml` file already exists and is correctly configured.
- [x] Add `tags` front matter to all 6 blog posts with relevant keywords chosen based on each post's content.
- [x] Add `keywords` front matter to all docs/tutorials (`/home/andrew/Code/andrew-seaford.co.uk/docs`) for SEO meta tags. (Note: docs do not support `authors` in Docusaurus structured data, so author is blog-only.)
- [x] Write a markdown file in the folder `/home/andrew/Code/andrew-seaford.co.uk/experiments` that documents the changes.

**Scope decisions:**
- All posts attributed to `andrewseaford` (single author)
- Tags/keywords will be chosen based on content (not a predefined list)
- Author front matter: blog posts only (Docusaurus natively supports this for JSON-LD)
- Keywords front matter: both blog posts and docs

**Impact:** Medium - affects rich snippet eligibility and E-E-A-T signals.
