# Multi-Objective EVCS Siting and Sizing — Reproducibility Package

[![Published-Result Validation](https://github.com/khainguyentien555/multi-objective-evcs-siting-sizing/actions/workflows/validate.yml/badge.svg)](https://github.com/khainguyentien555/multi-objective-evcs-siting-sizing/actions/workflows/validate.yml)

**Published-result data, source workbook, figure assets, and automated validation accompanying GTSD 2026 Paper ID 517.**

## Associated paper

**Tien-Khai Nguyen, Thi-Minh-Chau Le, and Trong-Nghia Le**  
“**Multi-Objective Mixed-Integer Programming for Siting and Sizing Electric Vehicle Charging Stations in Phu Quoc, Vietnam**”  
The 8th International Conference on Green Technology and Sustainable Development (GTSD 2026), Ho Chi Minh City, Vietnam, July 30–31, 2026.  
**Paper ID:** 517 — accepted / proceedings record in press at package release.

> The final DOI, proceedings page range, and publisher bibliographic record should be added when officially assigned. No DOI or page range is invented in this repository.

## What this repository reproduces

This package preserves and validates the paper-facing numerical evidence for the district-scale EV charging-station planning benchmark:

1. published case-study inputs (Table I);
2. B&C and BIPSO-GR charger allocations (Table III);
3. normalized objectives, weighted objective, coverage, and runtime (Table IV);
4. 30-run BIPSO-GR statistical assessment (Table V);
5. B&C service-distance sensitivity (Table VI);
6. objective-weight robustness values reported in the text; and
7. paper-facing figures that can be regenerated directly from the frozen published tables (Fig. 3 and Fig. 5 data views).

The package also preserves the original result workbook used during paper preparation and selected author-created figure sources.

## Reproducibility boundary

**This is a published-results reproducibility package, not a full solver replay.** The camera-ready GTSD archive did not contain the exact final B&C/BIPSO-GR solver source used to produce every reported experiment. A broader development codebase exists in the master's-thesis project, but it is not presented here as the canonical conference implementation because it is not byte-for-byte/formulation-identical to the camera-ready model.

Accordingly, the automated workflow validates frozen numerical results, the source-workbook lineage, rounding/post-processing for Table III, figure regeneration, and SHA-256 integrity. It does **not** claim to rerun the full exact/heuristic optimization from raw inputs.

## Repository layout

```text
.
├── data/
│   ├── published/        # frozen paper-facing Tables I, III–VI + weight robustness
│   └── source/           # original results workbook from the GTSD archive
├── figures/
│   ├── source/           # selected author-created source assets
│   └── regenerated/      # figures generated from published CSVs
├── python/
│   ├── validate_repository.py
│   └── make_figures.py
├── docs/                 # provenance, paper-to-data map, release notes
├── checksums/            # SHA-256 manifest and file inventory
└── .github/workflows/    # automated validation + checksum generation
```

## Fast verification

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python python/validate_repository.py
python python/make_figures.py
```

A successful check ends with:

```text
PUBLISHED-RESULT VALIDATION: PASS
Figure regeneration: PASS
```

## Numerical anchors

- B&C: **8 open sites, 188 chargers** = 105 × 11 kW, 77 × 60 kW, 6 × 150 kW.
- BIPSO-GR: **6 open sites, 333 chargers** = 91 × 11 kW, 240 × 60 kW, 2 × 150 kW.
- Weighted objective: **−0.01765 (B&C)** vs **0.00883 (BIPSO-GR)**.
- Coverage ratio: **1.000** for both methods.
- Reported benchmark runtime: **0.11 s** vs **0.65 s**.
- 30-run BIPSO-GR mean gap to raw B&C reference: **3.78%**; stabilization iteration: **37**.
- Dmax sensitivity: loaded stations **8 → 7 → 6** for **0.5 → 0.8 → 1.2 km**.

## Source-workbook lineage

`data/source/result_3_methods_new.xlsx` is copied unchanged from the working GTSD archive. The BIPSO-GR charger values map directly to the paper. The B&C paper-facing integer charger counts are obtained by half-up rounding of the workbook's post-processing values; the validator checks this transformation station by station.

See `docs/NUMERICAL_LINEAGE.md` for details.

## Citation

Until the final proceedings record is available, use the provisional citation in `citation.bib.template`. Update `CITATION.cff`, the BibTeX file, and this README once DOI/pages are officially assigned.

## License status

No blanket open-source/open-data reuse license is granted by this package. See `LICENSE_NOTICE.md`. Third-party literature, publisher files, presentation photographs, stock icons, and third-party base-map imagery are intentionally excluded.
