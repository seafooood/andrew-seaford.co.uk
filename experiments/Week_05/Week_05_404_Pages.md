# Week 05: 404 Pages — Full List and Status

## Source

GSC Page Indexing export — 2026-03-09 validation table (`Coverage-Validation-2026-03-09.zip`)

## Summary

43 pages are in 404 status. They fall into 5 distinct groups with very different causes and required actions.

---

## Are they WordPress tag/category pages?

Mostly **no** — only 4 of the 43 (9%) are WordPress auto-generated tag or category archive pages. The majority are real content pages or WordPress-generated garbage URLs (comment moderation, mobile plugin, trackbacks) that Google crawled and cached when the old WordPress site was live.

**Breakdown:**

| Group | Count | Action needed |
|-------|-------|---------------|
| Content pages — redirect in vercel.json (await re-crawl) | 23 | None — wait |
| WordPress comment/moderation spam URLs | 10 | None — let them 404 |
| WordPress mobile plugin (`?wptouch_switch`) | 4 | None — let them 404 |
| WordPress trackback URLs | 2 | None — let them 404 |
| Tag/category pages — missing redirect | 2 | Add redirects |
| Content page — missing redirect | 1 | Add redirect |
| Truncated/corrupted URLs | 1 | None — unresolvable |

---

## Group 1: Content Pages — Redirect Exists (Awaiting Google Re-Crawl)

These pages have a valid 301 redirect in `vercel.json`. They show as 404 because Google last crawled them **before** the redirects were added (Jan–Feb 2026). They should resolve automatically as Google re-crawls them.

- [ ] `/detecting-dominant-points-image-opencv/` — last crawled 2026-02-08
- [ ] `/displaying-an-image-with-python-tkinter/` — last crawled 2026-01-22
- [ ] `/free-disk-space-inno/` — last crawled 2026-02-02
- [ ] `/how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs/` — last crawled 2026-02-09
- [ ] `/my-first-3d-printing/` — last crawled 2026-02-06
- [ ] `/opencv-csharp-wpf-application/` — last crawled 2026-01-27
- [ ] `/ps3-controller/` — last crawled 2026-02-02
- [ ] `/c-open-file-dialog/` — last crawled 2026-02-02
- [ ] `/equal-c/` — last crawled 2026-02-04
- [ ] `/simple-box-code/` — last crawled 2026-02-02 *(redirect exists; `?wptouch_switch` variant below is separate)*
- [ ] `/generate-safe-filenames-using-python/` — last crawled 2026-01-30
- [ ] `/generate-safe-filenames-using-py` — last crawled 2026-01-30 *(truncated URL — redirect exists in vercel.json)*
- [ ] `/how-to-mock-a-function-that-returns-a-value/` — last crawled 2026-02-02
- [ ] `/how-to-change-the-label-font-in-tkinter/` — last crawled 2026-01-29
- [ ] `/create-m3u-playlist-from-directory-list/` — last crawled 2026-01-24
- [ ] `/image-contour-detection-display-opencv/` — last crawled 2026-01-24
- [ ] `/marlinfw-homing-direction/` — last crawled 2026-02-04
- [ ] `/threshold-image-opencv/` — last crawled 2026-02-03
- [ ] `/check-dotnet-framework-installed-inno-setup/` — last crawled 2026-02-05
- [ ] `/configuring-static-ip-address-raspberry-pi/` — last crawled 2026-02-06
- [ ] `/category/prog/digital-image-processing/` — last crawled 2026-02-08
- [ ] `/tag/m3u-playlist/` — last crawled 2026-02-06
- [ ] `/create-m3u-playlist-from-directory-list/trackback/` — last crawled 2026-02-02 *(redirect exists, points to base page)*
- [ ] `/how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs/trackback/` — last crawled 2026-02-09 *(redirect exists)*

---

## Group 2: Action Required — Missing Redirects

These pages have **no redirect in vercel.json** and need one adding.

### WordPress tag pages (no redirect)

- [ ] **`/tag/image-processing/`** — last crawled 2026-02-16 *(WordPress tag archive for OpenCV/image processing posts — suggest redirect to `/docs/opencv/opencv-world` or similar hub)*
- [ ] **`/tag/containerize/`** — last crawled 2026-03-03, Status: **FAILED** *(WordPress tag archive for Docker/containerization posts — suggest redirect to `/docs/docker/how-to-containerize-a-python-flask-application` or Docker hub)*

### Content page (no redirect)

- [ ] **`/3d-printing/`** — last crawled 2026-02-15 *(WordPress category/page for 3D printing — different from `/my-first-3d-printing/` which already has a redirect. Suggest redirect to `/docs/freecad/3d-printed-puzzle-vase-for-flowers` or a 3D printing hub)*

---

## Group 3: WordPress Garbage URLs — No Action Needed

These are WordPress-specific URLs that Google crawled from the old site. They were never real content pages and should stay as 404. **No redirect needed.**

### Comment moderation / reply URLs

- [ ] ~~`/c-open-file-dialog/?unapproved=107849&moderation-hash=...&replytocom=102533`~~ — 404 is correct
- [ ] ~~`/c-open-file-dialog/?unapproved=102533&moderation-hash=...&replytocom=107849`~~ — 404 is correct
- [ ] ~~`/c-open-file-dialog/?unapproved=107849&moderation-hash=...&replytocom=107849`~~ — 404 is correct
- [ ] ~~`/c-open-file-dialog/?unapproved=107849&moderation-hash=...`~~ — 404 is correct
- [ ] ~~`/c-open-file-dialog/?unapproved=102533&moderation-hash=...&replytocom=114399`~~ — 404 is correct
- [ ] ~~`/c-open-file-dialog/?unapproved=102533&moderation-hash=...`~~ — 404 is correct
- [ ] ~~`/detecting-dominant-points-image-opencv/?replytocom=2074`~~ — 404 is correct
- [ ] ~~`/detecting-dominant-points-image-opencv/?replytocom=2148`~~ — 404 is correct
- [ ] ~~`/detecting-dominant-points-image-opencv/?unapproved=109681`~~ — 404 is correct
- [ ] ~~`/opencv-csharp-wpf-application/?replytocom=3725`~~ — 404 is correct

### WordPress mobile plugin URLs (`?wptouch_switch`)

- [ ] ~~`/generate-safe-filenames-using-python/?wptouch_switch=desktop`~~ — 404 is correct
- [ ] ~~`/create-m3u-playlist-from-directory-list/?wptouch_switch=mobile`~~ — 404 is correct
- [ ] ~~`/create-m3u-playlist-from-directory-list/?wptouch_switch=desktop`~~ — 404 is correct
- [ ] ~~`/simple-box-code/?wptouch_switch=desktop`~~ — 404 is correct

---

## Group 4: Truncated / Corrupted URLs — No Action Needed

Google somehow indexed partial/truncated URLs from the old WordPress site. These can never resolve and should remain 404.

- [ ] ~~`/detecting-dominant-points-image-opencv/?unap`~~ — truncated URL parameter, 404 is correct
- [ ] ~~`/generate-safe-`~~ — heavily truncated, 404 is correct
- [ ] ~~`/custom-`~~ — heavily truncated (likely `/custom-inno-theme/` but unresolvable as-is), 404 is correct

---

## Required Actions

1. Add to `vercel.json`:
   ```json
   { "source": "/tag/image-processing", "destination": "/docs/opencv/opencv-world", "permanent": true },
   { "source": "/tag/containerize", "destination": "/docs/docker/how-to-containerize-a-python-flask-application", "permanent": true },
   { "source": "/3d-printing", "destination": "/docs/freecad/3d-printed-puzzle-vase-for-flowers", "permanent": true }
   ```
2. After deploying, use GSC → URL Inspection → "Validate Fix" to trigger re-crawl of `/tag/containerize/` (the only confirmed Failed entry).
3. The remaining ~37 pages in "Pending" status should resolve naturally as Google re-crawls them over the coming weeks.
