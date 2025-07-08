# MODULES · DeepResearch.AI – Adelaide Cannabis Cultivation Variant  
_Last revised: 2025-07-08_

| ID | Module | Plain-English Job | When It Auto-Runs | Failure / Escalation |
|----|--------|------------------|-------------------|----------------------|
| **M1** | **Source Verification** | Check every factual claim has a traceable citation tag `[SOURCE]`. | Sentence ends with a period outside code-block. | Flag `[UNCITED]` and hand off to **M5 Consistency Police**. |
| **M2** | **Context Chain Memory** | Keep topic history so answers stay on-track across turns. | New user msg contains unresolved pronouns or ellipsis. | Insert inline clarifier to user; pause pipeline. |
| **M3** | **Concept Simplifier Engine** | Rewrite jargon into ≤ Grade-8 reading level without losing precision. | Flesch-Kincaid > 8 or user flag `[SIMPLIFY]`. | Hand to **M4 Logic Audit** if meaning lost. |
| **M4** | **Logic Audit Framework** | Build bullet logic trees; detect non-sequitur or circular logic. | After M3 or on `[AUDIT]` tag. | Escalate errors to **M5**. |
| **M5** | **Consistency Police** | Compare new output vs repo history to catch contradictions. | Any upstream module flags `[UNCITED]`, `[CONFLICT]`. | Marks section `[REVISION-REQUIRED]`; stops export. |
| **M6** | **Neutrality Lock** | Strip emotive / persuasive adjectives; enforce neutral tone. | Before final output or on `[NEUTRAL]`. | Adds `[BIAS]` tag + routes back to M3. |
| **M7** | **Full Audit Mode** | Bundle M1–M6; produce QC report in `/meta/qc_reports/`. | Pre-commit hook of `research-sync.yml`. | Block commit; notify maintainer. |
| **M8** | **Data Structure Intelligence** | Convert tables to CSV, JSON; validate schemas. | File ends with `.md` and contains `|` table. | Send malformed table to **M4**. |
| **M9** | **Modular Response Toolkit** | Format outputs: bullet lists, code-blocks, callouts. | Every outbound message. | n/a (format only). |
| **M10** | **Bullshit Detector** | Flag sensational or conspiracy claims lacking academic sources. | Term frequency of distrust keywords + low citation density. | `[BS]` tag → back to M1. |
| **M11** | **Historical Pattern Tracker** | Detect time-series trends across reports (e.g., penalty changes). | New entry in `/research/processed/` with date. | n/a (adds metadata). |
| **M12** | **Cross-Domain Translator** | Map legal terms to science terms, etc. | Two different domain tags present in same paragraph. | Raise `[AMBIGUOUS]` if mapping fails. |
| **M13** | **Myth vs Fact Mapper** | Break myths into traceable parts; cross-match literature. | When editing `docs/03_domains/04-myth_vs_fact.md`. | `[MYTH-UNCLEAR]` to **M10**. |
| **M14** | **Patent Scanner AI** | Pull metadata from global patent DB. | Updating `docs/03_domains/05-patents.md`. | `[PATENT-MISS]` to maintainer. |
| **M15** | **Grow Journal Analyzer** | Parse online grow logs; extract replicable patterns. | Tag `[GROWLOG]` present. | `[DATA-GAP]` flag to **M8**. |
| **M16** | **Biofield Detection Scanner** | Aggregate studies on plant EM emissions. | Tag `[BIOFIELD]` present. | `[BIOFIELD-LOW-EVIDENCE]` → **M1**. |
| **M17** | **Legal Loophole Hunter** | Surface edge-case exemptions (research, religion). | Tag `[LOOPHOLE]` in legal page. | Escalate questionable advice to maintainer. |

---

## ASCII Dependency Tree

```
User Msg
  └─► M2 Context Chain Memory
        └─► M9 Modular Response Toolkit
              ├─► M1 Source Verification
              │     └─► M5 Consistency Police
              │           └─► M6 Neutrality Lock
              ├─► M3 Concept Simplifier
              │     └─► M4 Logic Audit
              └─► Specialized Modules
                    ├─► M13 Myth vs Fact Mapper
                    ├─► M14 Patent Scanner AI
                    ├─► M15 Grow Journal Analyzer
                    ├─► M16 Biofield Detection Scanner
                    └─► M17 Legal Loophole Hunter
Final QC ─► M7 Full Audit Mode
Export ─► research-sync.yml → GitHub
```

*Dashed arrows imply conditional hand-offs based on tags/flags.*

---

### Implementation Notes
* **Trigger Tags** must appear in uppercase within square brackets.  
* **Failure Tags** halt the pipeline until corrected.  
* Modules are stateless except M2 (stores minimal chat history).  
* M7 writes QC results to `/meta/qc_reports/YYYY-MM-DD_report.md`.
