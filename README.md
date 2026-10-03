# Senal Liyanage — Computational Science Portfolio

This repository hosts the public portfolio of Senal Liyanage, focused on computational chemistry, molecular simulation, scientific software, and reproducible scientific computing.

## Site structure

- `index.html` — professional landing page and selected work
- `projects.html` — curated case studies and public scientific software
- `research.html` — research practice organized around methods and public evidence
- `projects/salt-dissolution/` — molecular-dynamics case study using real simulation media and cluster analysis
- `projects/water-vaporization/` — scientific-visualization study based on an OpenMM water-slab model
- `assets/css/style.css` — shared visual system for the complete site
- `robots.txt` / `sitemap.xml` — search-engine discovery and indexing guidance
- `404.html` — GitHub Pages fallback page
- `scripts/check_site.py` — dependency-free structural and local-link audit
- `.github/workflows/site-audit.yml` — automatic QA on pull requests and pushes to `main`

## Editorial model

The portfolio is organized around **work rather than posts**. Case studies use a consistent research structure:

1. computational question
2. method / model
3. results or visualization
4. interpretation and limitations
5. reproducibility / related work

Poetic or science-communication framing is secondary to technical titles, methods, evidence, and explicit limitations.

## Public code represented on the site

The portfolio links to selected public repositories including:

- [qctddft](https://github.com/senal-liyanage/qctddft) — TDDFT post-processing, spectra, state assignment, and structural clustering
- [chemistry-analysis-tools](https://github.com/senal-liyanage/chemistry-analysis-tools) — molecular-file and trajectory-analysis utilities
- [AmberMD-Scripting](https://github.com/senal-liyanage/AmberMD-Scripting) — staged AMBER workflow helpers

## Public-content policy

This repository should contain only public, approved, and non-sensitive content. Do not commit private resumes, unpublished production trajectories, collaborator-owned data, manuscript-sensitive source material, credentials, home addresses, phone numbers, immigration details, or large simulation outputs that are not intended for public distribution.

The site may describe research methods at a portfolio-safe level while keeping unpublished results and restricted inputs outside the public repository.

## Quality assurance

Run the local structural audit before publishing substantial changes:

```bash
python scripts/check_site.py
```

The same audit runs automatically in GitHub Actions. It checks local links and asset references, fragment targets, one-`h1` page structure, unique IDs, image alt text, accessible labels for video/canvas media, meta descriptions, canonical URLs, favicons, and required production discovery files.

External scholarly and profile links should still be reviewed when their destinations change; the automated check intentionally avoids network-dependent validation.

## Deployment

The site is intentionally static and compatible with GitHub Pages without a build step. Canonical URLs, social-sharing metadata, a sitemap, robots policy, and a custom 404 page are maintained directly in the repository.

The portfolio should be treated as a stable public release rather than a continuously redesigned blog. New changes should primarily add stronger scientific work, correct factual information, or improve reliability/accessibility.
