# Site Review: SEO & Traffic Improvement Opportunities

**Date:** 2026-02-10
**Site:** https://www.andrew-seaford.co.uk
**Hosting:** Vercel (static Docusaurus build)

---

## Critical Issues

### 1. Domain Mismatch: www vs non-www - DONE 11th Feb 26

**Problem:** The Docusaurus config sets `url: 'https://andrew-seaford.co.uk'` (non-www), but Vercel redirects all traffic to `https://www.andrew-seaford.co.uk` (www) via 307. This creates a conflict where:

- Canonical tags say: `https://andrew-seaford.co.uk/`
- OG URLs say: `https://andrew-seaford.co.uk/`
- Sitemap URLs say: `https://andrew-seaford.co.uk/...`
- Structured data (JSON-LD) says: `https://andrew-seaford.co.uk/...`
- But the server sends users to: `https://www.andrew-seaford.co.uk/`

Google sees conflicting signals about which domain is canonical. Every sitemap URL requires an extra redirect hop (non-www -> www) before being served.

**Fix:** Change `url` in `docusaurus.config.js` to `'https://www.andrew-seaford.co.uk'`. This single change fixes the sitemap, canonical tags, OG tags, and structured data simultaneously.

**Impact:** High - directly affects indexing and crawl efficiency.

---

### 2. Missing robots.txt - DONE 11th Feb 26

**Problem:** `https://www.andrew-seaford.co.uk/robots.txt` returns HTTP 404 (serves the Docusaurus 404 page). No robots.txt file exists in the `static/` directory.

**Fix:** Create `static/robots.txt`:
```
User-agent: *
Allow: /

Sitemap: https://www.andrew-seaford.co.uk/sitemap.xml
```

**Impact:** Medium - missing robots.txt generates crawl errors in Google Search Console and prevents pointing crawlers to the sitemap.

---

### 3. Blog/Homepage Meta Description is "Blog" - DONE 11th Feb 26

**Problem:** The homepage meta description and OG description are both just `"Blog"`. The structured data (JSON-LD) also has `"description": "Blog"` and `"headline": "Blog"`.

```html
<meta name="description" content="Blog">
<meta property="og:description" content="Blog">
```

This appears in Google search results as the page snippet, giving users no reason to click.

Note: The `themeConfig.metadata` in `docusaurus.config.js` does set a better description (`"Technical insights on 3D printing, Robotics, and software development by Andrew Seaford."`), but this is overridden by the blog plugin's default description for the homepage.

**Fix:** Configure the blog plugin's `blogDescription` option in `docusaurus.config.js` to provide a descriptive summary. For example:
```js
blog: {
  blogDescription: 'Technical tutorials and insights on Docker, Python, OpenCV, 3D printing, and robotics by Andrew Seaford.',
  // ... other options
}
```

**Impact:** High - directly affects click-through rate from search results.

---

## High Priority Issues

### 4. 141 out of 218 Sitemap URLs Contain `%20` Encoded Spaces - DONE 11th Feb 26


**Problem:** 65% of URLs in the sitemap contain `%20` encoded spaces because doc folder names have spaces. Examples:
- `/docs/programming%20c%20sharp/adding%20days%20datetime%20csharp/adding-days-datetime-csharp`
- `/docs/milling%20machine%20cnc/axis%20drops%20completing%20job/axis-drops-completing-job`

Spaces in URLs are problematic because:
- They look broken when shared on social media or in emails
- They reduce click-through rates (users don't trust URLs with `%20`)
- Some tools and crawlers handle them inconsistently

**Fix:** Rename doc source folders to use hyphens instead of spaces (e.g., `programming c sharp` -> `programming-c-sharp`). Add Vercel 301 redirects from old `%20` URLs to new hyphenated URLs in `vercel.json`.

**Impact:** High - affects URL quality, shareability, and user trust for the majority of pages.

---

### 5. Placeholder Page in Sitemap - DONE 11th Feb 26

**Problem:** `/markdown-page` is included in the sitemap and returns HTTP 200. This is the default Docusaurus example page from `src/pages/markdown-page.md`. It has no real content value.

**Fix:** Delete `src/pages/markdown-page.md`.

**Impact:** Low-medium - wastes crawl budget on a valueless page and looks unprofessional if discovered.

---

### 6. Large Unoptimised Images

**Problem:** Several images in blog/doc posts are very large and uncompressed:
- `20170204_163209.jpg` - 2.7 MB
- `20170204_151013.jpg` - 2.3 MB
- `20170202_220206.jpg` - 2.2 MB

These are served without WebP conversion or responsive sizing.

**Fix:**
- Compress JPGs to under 200 KB using a tool like `squoosh` or `sharp`
- Consider using Docusaurus's `@docusaurus/plugin-ideal-image` for automatic resizing
- Add `loading="lazy"` to below-the-fold images

**Impact:** Medium - affects Core Web Vitals (LCP), which is a Google ranking factor.

---

### 7. Missing/Poor Image Alt Text

**Problem:** Many images use filenames as alt text or have no descriptive alt text:
```markdown
![IMG_20161114_044023-300x300.jpg](images/IMG_20161114_044023-300x300.jpg)
![whited-toothbrush-flower](images/Whited-Toothbrush-Flower-182x300.png)
```

**Fix:** Update image alt text to be descriptive of the image content. For example:
```markdown
![3D printed toothbrush holder in white PLA](images/Whited-Toothbrush-Flower-182x300.png)
```

**Impact:** Medium - affects image search traffic and accessibility.

---

## Medium Priority Issues

### 8. Structured Data: Empty Author and Keywords

**Problem:** The Blog schema JSON-LD on the homepage has empty `author` and `keywords` arrays for all blog posts:
```json
{
  "@type": "BlogPosting",
  "author": [],
  "keywords": []
}
```

Search engines use author information for E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) signals.

**Fix:** Configure the blog author in Docusaurus using the `authors.yml` file and ensure each blog post references an author. Add tags/keywords to blog posts.

**Impact:** Medium - affects rich snippet eligibility and E-E-A-T signals.

---

### 9. Security Headers Missing

**Problem:** The following security headers are absent from responses:
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Content-Security-Policy`
- `Referrer-Policy`
- `Permissions-Policy`

While not a direct ranking factor, these contribute to overall site trustworthiness.

**Fix:** Add headers configuration to `vercel.json`:
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

**Impact:** Low-medium - improves security posture and Lighthouse score.

---

### 10. Limited Cross-Linking Between Related Content

**Problem:** Most doc pages only have a "Related Files" section linking to GitHub. There are no "See Also" or "Related Articles" links to other pages on the site. This reduces:
- Time on site
- Pages per session
- Internal link equity distribution
- Crawl depth

**Fix:** Add "Related Tutorials" sections at the bottom of doc pages linking to 2-3 related articles on the site.

**Impact:** Medium - improves user engagement and helps Google discover and rank more pages.

---

### 11. 404 Page Offers No Recovery Path

**Problem:** The 404 page shows a generic message ("We could not find what you were looking for.") with no suggestions, no search, and no links to popular content.

**Fix:** Create a custom 404 page (`src/pages/404.js`) that includes:
- Links to the tutorials index and popular articles
- A search box (if Docusaurus search is configured)
- Recent blog posts

**Impact:** Low-medium - improves user retention when landing on broken links.

---

### 12. Thin Heading Structure in Docs

**Problem:** Most doc pages have only an H1 (the title) and possibly one H2 ("Related Files"). Content lacks descriptive subheadings that help Google understand page structure and can appear as featured snippets.

**Fix:** Break up longer tutorials into sections with descriptive H2/H3 headings. For example, instead of a single code block, use headings like "Prerequisites", "Step 1: Configure the environment", "Expected output", etc.

**Impact:** Low-medium - improves content structure signals and featured snippet eligibility.

---

## Low Priority / Nice to Have

### 13. No PWA Manifest

No `manifest.json` exists. Adding one would enable "Add to Home Screen" on mobile and improve Lighthouse PWA score.

### 14. HTTP Link in Content

The blog post "Preparing for Battle" links to `http://piwars.org/` using HTTP. Update to HTTPS if the destination supports it.

### 15. `/blog` Route Returns 404

Since the blog is configured as the homepage (`routeBasePath: '/'`), visiting `/blog` returns 404. Users and search engines may expect `/blog` to work. Consider adding a redirect from `/blog` to `/` in `vercel.json`.

---

## Summary: Priority Action List

| Priority | Issue | Effort | Impact |
|----------|-------|--------|--------|
| 1 | Fix www domain mismatch in `docusaurus.config.js` | 1 min | High |
| 2 | Create `static/robots.txt` | 1 min | Medium |
| 3 | Set proper blog description | 5 min | High |
| 4 | Delete `src/pages/markdown-page.md` | 1 min | Low |
| 5 | Add `/blog` -> `/` redirect to `vercel.json` | 1 min | Low |
| 6 | Add security headers to `vercel.json` | 5 min | Low-Med |
| 7 | Compress large images | 30 min | Medium |
| 8 | Improve image alt text | 1 hr | Medium |
| 9 | Configure blog authors for structured data | 15 min | Medium |
| 10 | Rename doc folders to remove spaces from URLs | 2-3 hrs | High |
| 11 | Add related article links to docs | Ongoing | Medium |
| 12 | Improve heading structure in docs | Ongoing | Low-Med |
| 13 | Customise 404 page | 30 min | Low-Med |
