# DeepResearch.AI — Adelaide Cannabis Cultivation Variant  
## Comprehensive Research Plan  
### Version 1 (9 July 2025)

---

### 1. Purpose
Establish a rigorous, well‑tagged research corpus to power the Adelaide Cannabis Cultivation Variant models with authoritative data on:  
* South Australian & Australian cannabis laws, penalties, and loopholes  
* Cutting‑edge single‑plant cultivation science tailored to Adelaide’s climate  
* Experimental influences of pH, light spectra, magnetism, geometry, and materials  
* Patent landscape and emerging technologies  
* Real‑world grow‑log evidence and community best practices  
* Myth vs fact reconciliation and biofield/EM insights  

---

### 2. Research Pillars & Key Questions
| Pillar | Goal | Key Questions |
| --- | --- | --- |
| **Legal & Compliance** | Guarantee every recommendation is lawful | What statutes regulate home cultivation? What penalties apply? Are there research or medical exemptions? |
| **Cultivation Science** | Optimise yield & quality for a single plant | How do soil composition, pH, nutrient schedules, and light spectra affect growth in Adelaide’s photoperiod? |
| **Patent Intelligence** | Track novel techniques & devices | Which patents describe single‑plant or micro‑grow methods? What IP might constrain or inspire us? |
| **Grow Journals** | Extract field‑tested tactics | What environmental parameters correlate with best outcomes in similar climates? |
| **Myth vs Fact** | Dispel misinformation | Which popular tips lack evidence? Which obscure practices have experimental support? |
| **Biofield & EM Research** | Assess electromagnetic influences | Do frequency, voltage, or geometric fields measurably impact plant physiology? |

---

### 3. Repository Folder Structure
```
/research
│
├──Legal_Compliance
│   ├──statutes
│   ├──penalties
│   └──case_studies
│
├──Cultivation_Science
│   ├──agronomy
│   ├──lighting
│   ├──magnetism_EM
│   └──geometric_structures
│
├──Patent_Library
│   ├──patents_pdf
│   └──patent_metadata.csv
│
├──Grow_Journals
│   ├──raw_logs
│   └──extracted_metrics.csv
│
├──Myth_vs_Fact
│
├──Biofield_Research
│
└──Data_Summaries
```

---

### 4. Data Collection Workflow
1. **Define search queries & keywords** per pillar.  
2. **Automated scraping & API pulls** where licenses permit (e.g., South Australian legislation website, WIPO, GrowDiaries API).  
3. **Manual download** of pay‑walled papers: store citation & abstract only.  
4. **Daily checksum & de‑duplication** of new files.  
5. **Metadata injection** (see §7).  

---

### 5. Model Tasking & Automation Cadence
| Model | Task | Frequency |
| --- | --- | --- |
| Patent Scanner AI | Query AU‑IPO, WIPO, USPTO, EPO for keywords | Weekly |
| Grow Journal Analyzer | Ingest new diaries, extract env metrics | Bi‑weekly |
| Myth vs Fact Mapper | Expand myth list, link evidence | Weekly |
| Biofield Detection Scanner | Harvest new EM field studies | Monthly |
| Legal Loophole Hunter | Audit SA & Federal updates, exemption rulings | Quarterly |

---

### 6. Timeline (Phase 1: 9 July – 6 Aug 2025)
| Week | Milestones |
| --- | --- |
| **W1** | Finalise folder structure • Pull SA statutes & penalties • Draft search keyword lists |
| **W2** | Bulk download cultivation science papers • Begin summarising key findings |
| **W3** | Complete first patent sweep • Classify patents by theme |
| **W4** | Ingest 50+ grow logs • Generate initial best‑practice matrix |
| **Ongoing** | Automated cycles per §5 • Continuous myth/fact validation |

---

### 7. Metadata & File Naming Standard
* **Filename**: `YYYY-MM-DD_short-title_source.ext`  
* **Front‑matter (YAML)** for docs:  
```yaml
title: ""
author: ""
source_url: ""
retrieved: "YYYY-MM-DD"
tags: []
pillar: ""
```
* **CSV/JSON metadata** mirrors for programmatic access.

---

### 8. Quality Control & Governance
* Nightly script checks for duplicates, 404 links, and missing metadata.  
* Version tag: `v1.0.[increment]`.  
* Deprecated files moved to `/archive` with rationale note.

---

### 9. Next Actions
1. Approve or modify this plan.  
2. Once approved, initialise folder skeleton in repo.  
3. Kick‑off Week‑1 milestones.  
4. Configure cron/CI jobs for automated model runs.

---

### 10. Repository Bootstrap Script (`scripts/bootstrap_research_repo.sh`)
```bash
#!/usr/bin/env bash
set -e

BRANCH="setup/research-plan-2025-07-09"
git checkout -b "$BRANCH"

# Folder skeleton
mkdir -p DRAFTS REPORTS/2025/07 DATA IMAGES META
for dir in DRAFTS REPORTS/2025/07 DATA IMAGES; do
  touch "$dir/.gitkeep"
done

# Copy plan to meta (assumes current path of plan markdown)
cp META/comprehensive_research_plan_2025-07-09-01.md META/comprehensive_research_plan_2025-07-09-01.md 2>/dev/null || echo "Ensure plan file copied manually if path differs"

# Meta log update
echo -e "## 2025-07-09\nModules Active: M07, S03\nGaps Identified: None at initialisation\nNext Topics: Week-1 milestones (legal statutes scrape, keyword list)\n" >> META/research_log.md

# Commit and push
git add DRAFTS REPORTS DATA IMAGES META
git commit -m "[DeepResearch.AI] v2025-07-09-01 — Modules: M07, S03 Tags: EXPORT READY"
git push -u origin "$BRANCH"

echo "Branch $BRANCH pushed. Open a PR to merge into main."
```

### 11. README Stub Template (drop into each new folder)
```markdown
# <FOLDER NAME>

This directory is part of the **DeepResearch.AI – Adelaide Cannabis Cultivation Variant** repository.

**Purpose:** <brief description>

Generated automatically on 2025-07-09.
```

---

*Prepared by ChatGPT on 9 July 2025 (AEST)*
