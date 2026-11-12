# Source and data notes

Reference repository: https://github.com/saloniprasad017/Bank_Loan_Analysis

The supplied CSV contains borrower-level fields including IDs, loan-detail URLs,
free-text descriptions, employee titles, and partial ZIP codes. Do not publish
the raw file until its provenance, license, and privacy implications are checked.
Prefer a documented source link and a minimized/aggregated dataset where possible.

The original MySQL import script contained a local filesystem path and hard-coded
credentials. That script has been replaced with an environment-variable template.
