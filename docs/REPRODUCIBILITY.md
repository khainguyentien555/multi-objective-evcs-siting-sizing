# Reproducibility instructions

## Automated verification

With Python 3.11+:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python python/validate_repository.py
python python/make_figures.py
```

The validator checks:

1. required archival structure;
2. SHA-256 integrity of canonical published/source files;
3. Table III totals and open-station counts;
4. station-by-station source-workbook lineage, including half-up rounding of B&C charger post-processing;
5. Table IV benchmark metrics;
6. Table V 30-run heuristic statistics; and
7. Table VI service-distance sensitivity.

## What is not automated

The exact final optimization replay is not claimed because the exact camera-ready solver source is absent from the GTSD archive. Do not interpret a green GitHub Actions badge as proof that B&C and BIPSO-GR were rerun from raw model inputs. The badge certifies the published-result archival checks described above.
