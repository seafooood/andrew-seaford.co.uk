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

**Fix:** Configure the blog author in Docusaurus using the `authors.yml` file and ensure each blog post (/home/andrew/Code/andrew-seaford.co.uk/blog) and tutorials (/home/andrew/Code/andrew-seaford.co.uk/docs) references an author. Add tags/keywords to blog posts.

**Impact:** Medium - affects rich snippet eligibility and E-E-A-T signals.