 6. Large Unoptimised Images

**Problem:** Several images in blog/doc posts are very large and uncompressed:
- `20170204_163209.jpg` - 2.7 MB
- `20170204_151013.jpg` - 2.3 MB
- `20170202_220206.jpg` - 2.2 MB

These are served without WebP conversion or responsive sizing.

**Fix:**

- Install Docusaurus's `@docusaurus/plugin-ideal-image` for automatic resizing
- Add `loading="lazy"` to below-the-fold images

**Impact:** Medium - affects Core Web Vitals (LCP), which is a Google ranking factor.