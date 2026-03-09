# Week 1 Experiment Tasks

## Experiment: "How To Containerize A Python Flask Application" CTR Optimization

### Tasks for this Week (Due by next week's review):

1.  **Retrieve Baseline Data:** DONE
    *   Extracted and analysed GSC Performance data (last 3 months ending 2026-02-07).
    *   The article does not appear in the GSC Pages report at all — 0 impressions, 0 clicks, 0% CTR.
    *   No Docker/Flask related queries appear in the site's query data either.
    *   Baseline data recorded in `Week_01_Experiment_Docker_Flask_CTR_Optimization.md`.

2.  **Retrieve Current Meta Information:** DONE
    *   Inspected the article markdown file at `docs/docker/How To Containerize A Python Flask Application/How To Containerize A Python Flask Application.md`.
    *   **Finding:** The article had **no frontmatter whatsoever** — no title, no description, no keywords, no slug.
    *   Docusaurus was auto-generating the title from the H1 heading (`How To Containerize A Python Flask App`) and providing no meta description.

3.  **Perform Keyword Research:** DONE
    *   Reviewed GSC query data — no Docker/Flask queries appearing for the site.
    *   Identified target keywords based on common search intent: `dockerize flask`, `containerize python flask`, `flask docker tutorial`, `dockerfile flask`, `python docker container`, `flask restful docker`.

4.  **Draft Optimized Meta Title and Description:** DONE
    *   **Title:** `Dockerize a Python Flask App: Step-by-Step Guide` (49 chars, under 60 char limit)
    *   **Description:** `Learn how to containerize a Python Flask application with Docker. Step-by-step guide covering Dockerfile setup, building images, and running containers.` (152 chars, under 160 char limit)
    *   Recorded in `Week_01_Experiment_Docker_Flask_CTR_Optimization.md`.

5.  **Implement Changes on Website:** DONE
    *   Added full Docusaurus frontmatter to the article markdown file including title, description, keywords, slug, and date.
    *   File modified: `docs/docker/How To Containerize A Python Flask Application/How To Containerize A Python Flask Application.md`

6.  **Confirmation:** PENDING DEPLOYMENT
    *   Changes have been made to the source markdown file. Verification that the meta tags are live should be done after the site is built and deployed.

### Next Steps (Next Week):
*   Download new Google Search Console Performance data for the period after changes were implemented.
*   We will then review the results against the baseline and discuss the next experiment.
*   Note: Since baseline is 0 impressions, any appearance in search results is a positive signal. True CTR optimisation can begin once the article is indexed and receiving impressions.