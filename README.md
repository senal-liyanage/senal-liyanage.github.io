# Senal Liyanage — Computational Science Portfolio

This repository hosts the public portfolio of Senal Liyanage, focused on computational chemistry, molecular simulation, scientific software, and reproducible scientific computing.

## Site structure

- `index.html` — professional landing page and selected work
- `projects.html` — curated case studies and public scientific software
- `research.html` — research practice organized around methods and public evidence
- `projects/salt-dissolution/` — molecular-dynamics case study using real simulation media and cluster analysis
- `projects/water-vaporization/` — scientific-visualization study based on an OpenMM water-slab model
- `assets/css/style.css` — shared visual system for the complete site

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

## Deployment

The site is intentionally static and compatible with GitHub Pages without a build step. The current refactor keeps deployment simple while establishing a reusable visual and editorial system that can later be migrated to a component-based static-site generator if the number of case studies grows substantially.
