# Numerical lineage

## 1. Canonical publication layer

The final camera-ready PDF is treated as the authority for the paper-facing values recorded in `data/published/`.

## 2. Source workbook

`data/source/result_3_methods_new.xlsx` is an unchanged copy of the results workbook found in the GTSD working archive. It contains CPLEX/B&C and MATLAB/BIPSO-GR charger post-processing tables.

For BIPSO-GR, the integer charger allocations in the workbook map directly to the published Table III values.

For B&C, the workbook preserves fractional post-processing values such as 10.25, 13.5, 14.5, and 19.75. The final paper reports integer charger counts. The publication transformation is **half-up rounding applied station-by-station**, e.g. 13.5 → 14 and 14.5 → 15. `python/validate_repository.py` checks this mapping for all eight stations and confirms the published totals 105 / 77 / 6.

## 3. Exact-solver and heuristic source boundary

The camera-ready archive does not contain the exact final solver scripts used for the full B&C and 30-run BIPSO-GR experiments. A related master's-thesis archive contains developmental CPLEX/MATLAB implementations, but those files are not formulation-identical to the final conference paper. They are therefore **not copied into this package as canonical code**.

This package intentionally prioritizes an auditable claim that can be supported by evidence: preservation and automated validation of the published numerical layer and its source workbook.
