# 00 · Project Charter  
DeepResearch.AI — Adelaide Cannabis Cultivation Variant  

---

## 1 · Mission Statement  *(≤ 40 words)*
Deliver audit-grade, bias-free research on single-plant, outdoor cannabis cultivation in South Australia, with every source traceable, quality-checked, and auto-synced to GitHub for public verification.

---

## 2 · Purpose & Core Goals
| Goal | Success KPI |
|------|-------------|
| **Truth & Clarity** | ≥ 95 % of reports pass QC with zero uncited claims. |
| **Legal Relevance** | All legal sections reference the current SA & Aus Federal statutes within 30 days of publication. |
| **Open Traceability** | 100 % of research commits visible on the bot branch within 5 minutes of file creation. |

---

## 3 · Out-of-Scope (Do Not Research)
1. **Multi-plant or commercial grows** (any method > 1 plant).  
2. **Psychoactive product manufacturing** (extraction, edibles, concentrates).  
3. **Indoor grow-room construction** (lighting rigs, HVAC, hydroponics).  
4. **Medical dosage or health advice** (pharmacology, prescriptions).  
5. **Non-SA climates or laws** (other Australian states or countries).  
6. **Personal data collection** (no identifying user info stored).  

---

## 4 · Legal Disclaimer
All content is informational only and must be interpreted in accordance with South Australian and Australian Federal law; it does **not** constitute legal advice.

---

## 5 · Alignment Checklist
| Check | Trigger | Module |
|-------|---------|--------|
| Claims uncited? | Sentence ends without `[SOURCE]` | *Source Verification* |
| Topic drifts into out-of-scope? | Tag `[OOS]` detected | *Consistency Police* |
| Reading level too high? | Flesch-Kincaid > 8 | *Concept Simplifier* |
| Bias wording? | Subjective adjective flagged | *Neutrality Lock* |
