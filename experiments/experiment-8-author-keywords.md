# Experiment 8: Structured Data - Author and Keywords

**Date:** 2026-02-17

## Problem

The Blog schema JSON-LD on the homepage had empty `author` and `keywords` arrays for all blog posts, weakening E-E-A-T signals and rich snippet eligibility.

## Changes Made

### 1. Blog Post Authors

Added `authors: [andrewseaford]` front matter to all 6 blog posts. The `blog/authors.yml` file was already configured with the correct author profile.

**Files modified:**
- `blog/fod-detection-system.md`
- `blog/oculus.md`
- `blog/project-identity.md`
- `blog/woospeedy.md`
- `blog/preparing-for-battle/index.md`
- `blog/puzzle-vase.md`

### 2. Blog Post Tags

Added `tags` front matter to all 6 blog posts with content-relevant keywords:

| Post | Tags |
|------|------|
| FOD Detection System | aviation, safety, entrepreneurship |
| Oculus Released | accessibility, desktop-application |
| Project Identity Released | vs-code, extension, developer-tools |
| WooSpeedy Released | woocommerce, wordpress, e-commerce |
| Preparing for Battle | raspberry-pi, robotics, pi-wars |
| 3D Printed Puzzle Vase | 3d-printing, freecad, design |

### 3. Doc/Tutorial Keywords

Added `keywords` front matter to all doc/tutorial pages (~145 files) with 3-5 SEO-relevant keywords per page. Keywords were chosen based on each page's content and technology topic.

**Categories covered:** Docker, PostgreSQL, VirtualBox, Ubuntu, Python (Flask, Django, pip, venv, tkinter, etc.), JavaScript (React, Next.js, Jest), C#, PHP, OpenCV, Oracle, FreeCAD/3D printing, Pinecone, Langflow, n8n, Hugo, VS Code, MySQL, WooCommerce, Gemini, Flameshot, Inno Setup, CNC milling, Raspberry Pi, GitHub Actions, and more.

## Expected Impact

- Blog JSON-LD `author` arrays will now contain the author's name and URL
- Blog JSON-LD `keywords` arrays will now contain relevant tags
- Doc pages will have `<meta name="keywords">` tags for SEO
- Improved E-E-A-T signals for search engines
- Better rich snippet eligibility
