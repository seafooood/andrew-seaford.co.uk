# Week 2 Experiment Tasks

## Experiment: "Custom Inno Theme" CTR Optimization

### Tasks for this Week (Due by next week's review):

1.  **Retrieve Baseline Data:** DONE
    *   Extracted and analysed GSC Performance data (3 months ending 2026-02-14).
    *   The `/custom-inno-theme/` page has 684 impressions, 5 clicks, 0.73% CTR, average position 9.2.
    *   Key queries: `inno setup wizardimagefile size` (position 4.59), `inno setup wizardimagefile size 164 314` (position 10.85).
    *   Baseline data recorded in `Week_02_Experiment_Inno_Theme_CTR_Optimization.md`.

2.  **Retrieve Current Meta Information:** DONE
    *   Inspected the article markdown file at `docs/inno/custom-inno-theme/index.md`.
    *   **Finding:** The article has a title (`Custom Inno Theme`) and slug, but **no meta description and no keywords**.
    *   The title is generic and doesn't match the specific search queries driving impressions (e.g., `wizardimagefile size`).

3.  **Perform Keyword Research:** DONE
    *   Reviewed GSC query data — identified key queries: `inno setup wizardimagefile size`, `wizardimagefile`, `inno setup wizardsmallimagefile size`.
    *   Target keywords: `inno setup custom images`, `wizardimagefile`, `wizardsmallimagefile`, `inno setup theme`, `inno setup installer images`, `inno setup wizard image size`.

4.  **Draft Optimized Meta Title and Description:** DONE
    *   **Title:** `Customize Inno Setup Installer Images: WizardImageFile Guide` (60 chars, at 60 char limit)
    *   **Description:** `Customize your Inno Setup installer with custom images using WizardImageFile and WizardSmallImageFile. Includes correct image sizes and BMP format guide.` (154 chars, under 160 char limit)
    *   Recorded in `Week_02_Experiment_Inno_Theme_CTR_Optimization.md`.

5.  **Implement Changes on Website:** PENDING
    *   Update frontmatter in `docs/inno/custom-inno-theme/index.md` with optimized title, description, and keywords.

6.  **Confirmation:** PENDING DEPLOYMENT
    *   After changes are implemented, verify the site builds correctly and the new meta tags are live.

### Ongoing from Week 01:
*   Continue monitoring the Docker Flask article (`/how-to-containerize-a-python-flask-application/`) for Google indexing progress.
*   Week 01 experiment is inconclusive — the article has not yet been indexed.

### Next Steps (Next Week):
*   Download new Google Search Console Performance and Page Indexing data.
*   Compare `/custom-inno-theme/` CTR against the 0.73% baseline.
*   Review Docker Flask article indexing status.
*   Design Week 03 experiment based on results.
