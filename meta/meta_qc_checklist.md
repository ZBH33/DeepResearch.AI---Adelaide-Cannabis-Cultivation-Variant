# QC Checklist · DeepResearch.AI  
_Last revised: 2025-07-08_

| # | Check | Pass Criteria | Module |
|---|-------|---------------|--------|
| 1 | **Citation Coverage** | Every factual sentence ends with `[SOURCE]` tag or is common knowledge. | M1 |
| 2 | **Tag Compliance** | Domain tag present, order rules followed (Domain→Process→Quality→Meta). | M5 |
| 3 | **Readability** | Flesch‑Kincaid ≤ 8; jargon simplified. | M3 |
| 4 | **Bias Scan** | No persuasive/emotive adjectives; neutral tone. | M6 |
| 5 | **Logic Integrity** | No circular logic or non‑sequitur. | M4 |
| 6 | **Conflict Check** | No contradiction with existing repo data. | M5 |
| 7 | **Table Format** | Tables render correctly; blank line before & after. | M8 |
| 8 | **Filename Convention** | `YYYY-MM-DD_slug.md` in `/research/processed/`. | Pre‑commit |
| 9 | **Revision Log** | Section 6 present and updated. | Pre‑commit |
| 10 | **Export Gate** | No active Quality tags (`[UNCITED]`, `[BIAS]`, …). | M7 |

**QC Outcome Codes**

* **PASS** – All checks met; file moves to `/research/processed/`.  
* **WARN** – Minor style issues; commit allowed but flagged in log.  
* **FAIL** – Any critical check fails; export blocked until fixed.

---

## Review Flow
1. **Author Pass** – Writer runs `scripts/local_build.sh` locally.  
2. **Automated QC** – M7 runs in workflow; outputs report to `/meta/qc_reports/`.  
3. **Human Oversight** – Maintainer reviews FAIL reports weekly.
