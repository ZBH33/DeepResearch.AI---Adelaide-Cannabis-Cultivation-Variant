# Tagging Standard · DeepResearch.AI  
_Last revised: 2025-07-08_

Tags are **UPPERCASE inside square brackets** and placed _inline_ right after the statement or section they qualify.

---

## 1 · Tag Classes  

| Class | Purpose | Example |
|-------|---------|---------|
| **Domain** | Identifies the subject area of a paragraph. | `[LEGAL]`, `[SCIENCE]` |
| **Process** | Directs workflow actions or module triggers. | `[SOURCE]`, `[SIMPLIFY]`, `[AUDIT]` |
| **Quality** | Flags issues that block publishing. | `[UNCITED]`, `[CONFLICT]`, `[BIAS]` |
| **Meta‑Event** | Raised by specialized modules. | `[PATENT-MISS]`, `[MYTH-UNCLEAR]` |

---

## 2 · Domain Tags  

| Tag | Meaning | Allowed With | Example |
|-----|---------|--------------|---------|
| `[LEGAL]` | Statutes, case‑law, penalties. | Process & Quality | “Section 33L carries a $2,000 fine. `[LEGAL] [SOURCE]`” |
| `[SCIENCE]` | Soil, pH, light, bio‑magnetism. | Process & Quality | “Optimal soil pH is 6.5. `[SCIENCE] [SOURCE]`” |
| `[MYTH]` | Folklore claims. | Process & Quality | “Some believe pyramid shape boosts growth. `[MYTH]`” |
| `[PATENT]` | Patent data. | Process & Quality | “AU‑2025‑12345 covers a solar dehydrator. `[PATENT]`” |
| `[GROWLOG]` | Info from online grow journals. | Process & Quality | |
| `[BIOFIELD]` | Plant EM field studies. | Process & Quality | |
| `[LOOPHOLE]` | Legal exemptions & edge cases. | Process & Quality | |

**Rule D‑1:** _Max one domain tag per paragraph._  
**Rule D‑2:** Domain tags cannot nest inside each other.

---

## 3 · Process Tags  

| Tag | Triggers Module | Auto‑Removes When |
|-----|-----------------|-------------------|
| `[SOURCE]` | M1 Source Verification | Citation validated |
| `[SIMPLIFY]` | M3 Concept Simplifier | F‑K ≤ 8 |
| `[AUDIT]` | M4 Logic Audit | Audit complete |
| `[NEUTRAL]` | M6 Neutrality Lock | No bias adjectives |
| `[EXPORT]` | research-sync.yml | Commit passes M7 |

---

## 4 · Quality & Issue Tags  

| Tag | Meaning | Resolution Path |
|-----|---------|-----------------|
| `[UNCITED]` | Missing citation. | Add source → run M1. |
| `[CONFLICT]` | Contradicts earlier repo data. | Resolve with M5. |
| `[REVISION-REQUIRED]` | Module halted pipeline. | Fix, then `[AUDIT]`. |
| `[BIAS]` | Emotive language detected. | Reroute M6. |
| `[BS]` | Sensational claim w/o evidence. | Provide sources or remove. |
| `[AMBIGUOUS]` | Cross-domain mapping failed. | Clarify terms. |
| `[DATA-GAP]` | Insufficient dataset. | Fetch more data. |

Quality tags **block export** until cleared.

---

## 5 · Meta‑Event Tags (Specialized Modules)

| Tag | Raised By | Meaning |
|-----|-----------|---------|
| `[MYTH-UNCLEAR]` | M13 | Myth lacks historic origin. |
| `[PATENT-MISS]` | M14 | Patent number missing/invalid. |
| `[BIOFIELD-LOW-EVIDENCE]` | M16 | Study quality score < 3/5. |

These auto‑route back to respective modules and then to M1 if unresolved.

---

## 6 · Nesting & Co‑existence Rules  

1. **One Domain Tag per paragraph** (Rule D‑1).  
2. Multiple **Process** or **Quality** tags may follow a Domain tag.  
3. **Quality** tags cannot co‑exist with `[EXPORT]`.  
4. Tags appear **in this order**: Domain → Process → Quality → Meta.  
5. Place tags at the **end of the sentence** unless it’s a block tag for entire section.

---

## 7 · Quick Cheat‑Sheet  

| Tag | Class | One‑line Purpose |
|-----|-------|------------------|
| `[LEGAL]` | Domain | SA statutes & penalties |
| `[SCIENCE]` | Domain | Empirical cultivation data |
| `[MYTH]` | Domain | Folklore or unverified belief |
| `[PATENT]` | Domain | Patent information |
| `[SOURCE]` | Process | Cite immediately before tag |
| `[SIMPLIFY]` | Process | Force readability pass |
| `[UNCITED]` | Quality | Missing citation red‑flag |
| `[BIAS]` | Quality | Emotive wording present |
| `[PATENT-MISS]` | Meta | Invalid patent ref |

*(Full table in /docs for complete list.)*
