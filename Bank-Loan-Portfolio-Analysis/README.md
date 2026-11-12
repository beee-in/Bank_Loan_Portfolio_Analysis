# Bank Loan Portfolio Analysis
## Project objective
Explore loan portfolio characteristics and repayment outcomes, including loan
status, loan grade, borrower income bands, and loan amounts.

## Current contents
- `python/loan_analysis.py` — baseline exploratory analysis from the reference project.
- `python/import_to_mysql.py` — rewritten configurable MySQL import template; credentials
  are read from environment variables rather than embedded in source code.
- `sql/queries.sql` — baseline SQL aggregations from the reference project.
- `data/` — local data directories; datasets are intentionally excluded from this
  staging package pending source, license, and privacy review.

## Planned work before presenting this as a portfolio project
- Verify dataset provenance, license, and permitted redistribution.
- Remove or aggregate borrower-level identifiers and free-text fields before sharing data.
- Reproduce and validate the analysis independently.
- Add meaningful portfolio metrics and documented findings.
- Add tests, dependency versions, and reproducible run instructions.

## Run status
This is an initial staging structure. It has not yet been validated end-to-end.
Do not describe planned work as completed work.
