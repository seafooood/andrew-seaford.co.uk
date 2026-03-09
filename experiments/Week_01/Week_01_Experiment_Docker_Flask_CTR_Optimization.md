# Week 1 Experiment: "How To Containerize A Python Flask Application" CTR Optimization

## Date: 2026-02-09

## Target Article
`/docs/docker/How To Containerize A Python Flask Application`

## Aim
To improve the organic Click-Through Rate (CTR) of the "How To Containerize A Python Flask Application" article in Google Search results.

## Hypothesis
By optimizing the meta title and meta description of the "How To Containerize A Python Flask Application" article, we will increase its organic Click-Through Rate (CTR) by at least 10% over the next week.

## Proposed Changes
**Action:** The article had **no frontmatter at all** — no `<title>` tag, no `<meta name="description">`, and no keywords. Docusaurus was falling back to the H1 heading as the page title and generating no description. This was a major SEO gap.

*   **Meta Title Optimization:**
    *   **Current:** `How To Containerize A Python Flask App` (auto-generated from H1, no explicit title set)
    *   **Implemented:** `Dockerize a Python Flask App: Step-by-Step Guide` (49 chars — under 60 char limit, keyword-rich, action-oriented)
*   **Meta Description Optimization:**
    *   **Current:** None (no description set — Docusaurus would auto-generate a snippet or leave blank)
    *   **Implemented:** `Learn how to containerize a Python Flask application with Docker. Step-by-step guide covering Dockerfile setup, building images, and running containers.` (152 chars — under 160 char limit, includes key search terms and clear value proposition)
*   **Keywords Added:**
    *   `dockerize flask`, `containerize python flask`, `flask docker tutorial`, `dockerfile flask`, `python docker container`, `flask restful docker`
*   **Slug Optimized:**
    *   Set to `how-to-containerize-a-python-flask-application` for clean, SEO-friendly URL

## Metrics to Track
*   **Primary:** Organic Click-Through Rate (CTR) for the specific URL.
*   **Secondary:** Impressions, Total Clicks, Average Position for relevant keywords.

## Baseline Data
From Google Search Console Performance report (last 3 months ending 2026-02-07).

The article URL does **not appear** in the GSC Pages report at all, meaning it has received zero tracked impressions and zero clicks in the reporting period. This is consistent with the article having no SEO metadata.

*   CTR: 0% (not appearing in search results)
*   Impressions: 0
*   Clicks: 0
*   Average Position: N/A

**Note:** No Docker or Flask-related search queries appear in the site's GSC Queries report either, confirming this topic area is currently unserved by the site in search.

## Changes Implemented: 2026-02-09
Added full Docusaurus frontmatter to the article markdown file:
```yaml
---
title: "Dockerize a Python Flask App: Step-by-Step Guide"
description: "Learn how to containerize a Python Flask application with Docker. Step-by-step guide covering Dockerfile setup, building images, and running containers."
keywords: [dockerize flask, containerize python flask, flask docker tutorial, dockerfile flask, python docker container, flask restful docker]
slug: how-to-containerize-a-python-flask-application
date: 2024-01-01
---
```

## Experiment Duration
1 week (2026-02-09 to 2026-02-16), after which new data will be collected and analyzed.

## Expected Outcome
Since the article had zero SEO metadata, any improvement from this baseline is a success. The primary goal is to get the article indexed and appearing in search results for Docker/Flask related queries. We expect to see:
- The page appearing in GSC with impressions for relevant queries
- Initial CTR data to serve as a true baseline for future optimisation