# Output Standards · DeepResearch.AI  
_Last revised: 2025-07-08_

Every published research file **must** follow the standard layout below.  
Copy the snippet, replace placeholders, and keep heading numbers intact.

---

## 1 · Universal Layout Snippet

```markdown
<!-- ====== METADATA ====== -->
Title: {CONCISE TITLE}             # ≤ 60 characters
Author: DeepResearch-Bot
Date: {YYYY-MM-DD}
Domain: [LEGAL] / [SCIENCE] / ...
Version: 0.1
Tags: {TAG LIST}                   # e.g., [LEGAL] [SOURCE]
<!-- ======================= -->

# 1 · Research Question
*State the question in one sentence.*

# 2 · Key Findings
| # | Finding | Tag(s) | Citation |
|---|---------|--------|----------|
| 1 |  |  |  |
| 2 |  |  |  |

# 3 · Evidence & Analysis
## 3.1 · Finding 1
Explain in plain language ≤ Grade 8. `[SOURCE]`

## 3.2 · Finding 2
Explanation. `[SOURCE]`

# 4 · Source Table
| Ref | Type | Year | Reliability (1‑5) | Link |
|-----|------|------|-------------------|------|

# 5 · Tag Summary
`[LEGAL] [SOURCE] ...`

# 6 · Revision Log
| Date | Author | Change |
|------|--------|--------|
| YYYY‑MM‑DD | Bot | Initial draft |
```

**Lint Rules**

* Heading numbers must be consecutive (1, 2, 3…).  
* Tables require a blank line before and after for GitHub renderer.  
* Tags in `Tags:` line must match those in the body.

---

## 2 · Snippet Examples

### 2.1 · Legal Brief (Section 33L Example)
```markdown
<!-- ====== METADATA ====== -->
Title: SA Section 33L Penalties for Outdoor Cannabis  
Author: DeepResearch-Bot  
Date: 2025-07-09  
Domain: [LEGAL]  
Version: 1.0  
Tags: [LEGAL] [SOURCE]
<!-- ======================= -->

# 1 · Research Question
What is the maximum penalty for cultivating one cannabis plant in soil in South Australia?

# 2 · Key Findings
| # | Finding | Tag(s) | Citation |
|---|---------|--------|----------|
| 1 | Section 33L sets a fine of up to AUD 2,000. | [LEGAL] | §33L(2) [SOURCE] |
| 2 | Offence is non‑criminal if no sale intent. | [LEGAL] | SA Gov Gazette 2024 [SOURCE] |

# 3 · Evidence & Analysis
## 3.1 · Section 33L Fine
The Controlled Substances Act (SA) lists a **$2,000** fine for cultivating **one plant** where no commercial intent is proven. `[SOURCE]`

## 3.2 · Non‑Criminal Offence
The 2024 amendment reclassified first‑time single‑plant offences as “simple offences,” not crimes. `[SOURCE]`

# 4 · Source Table
| Ref | Type | Year | Reliability | Link |
| §33L(2) | Statute | 2023 | 5 | <link> |
| SA Gazette 2024 | Govt Notice | 2024 | 4 | <link> |

# 5 · Tag Summary
`[LEGAL] [SOURCE]`

# 6 · Revision Log
| Date | Author | Change |
|------|--------|--------|
| 2025‑07‑09 | Bot | Initial draft |
```

---

### 2.2 · Soil Science Note (Optimal pH)
```markdown
<!-- ====== METADATA ====== -->
Title: Optimal Soil pH for Cannabis Growth  
Author: DeepResearch-Bot  
Date: 2025-07-09  
Domain: [SCIENCE]  
Version: 1.0  
Tags: [SCIENCE] [SOURCE]
<!-- ======================= -->

# 1 · Research Question
What soil pH maximizes nutrient uptake for a single outdoor cannabis plant?

# 2 · Key Findings
| # | Finding | Tag(s) | Citation |
|---|---------|--------|----------|
| 1 | pH 6.3–6.8 maximizes NPK uptake. | [SCIENCE] | Univ Adelaide 2023 [SOURCE] |

# 3 · Evidence & Analysis
## 3.1 · Nutrient Uptake Curve
Trials at the University of Adelaide showed peak chlorophyll at pH 6.5. `[SOURCE]`

# 4 · Source Table
| Ref | Type | Year | Reliability | Link |
| Univ Adelaide 2023 | Peer‑review | 2023 | 4 | <link> |

# 5 · Tag Summary
`[SCIENCE] [SOURCE]`

# 6 · Revision Log
| Date | Author | Change |
|------|--------|--------|
| 2025‑07‑09 | Bot | Initial draft |
```

---

### 2.3 · Myth Audit (Pyramid Power)
```markdown
<!-- ====== METADATA ====== -->
Title: Does a Pyramid Structure Accelerate Cannabis Growth?  
Author: DeepResearch-Bot  
Date: 2025-07-09  
Domain: [MYTH]  
Version: 1.0  
Tags: [MYTH] [SOURCE]
<!-- ======================= -->

# 1 · Research Question
Is there scientific evidence that growing a cannabis plant under a pyramid speeds growth?

# 2 · Key Findings
| # | Finding | Tag(s) | Citation |
|---|---------|--------|----------|
| 1 | No peer‑reviewed study supports growth acceleration. | [MYTH] | `[MYTH-UNCLEAR]` |
| 2 | Origin traces to 1970s New Age literature. | [MYTH] | Smith 1975 [SOURCE] |

# 3 · Evidence & Analysis
## 3.1 · Lack of Empirical Data
A literature search returned zero controlled studies. `[MYTH-UNCLEAR]`

## 3.2 · Historical Origin
Pyramid power craze began with Patrick Flanagan’s 1973 book, not with academic science. `[SOURCE]`

# 4 · Source Table
| Ref | Type | Year | Reliability | Link |
| Smith 1975 | Book | 1975 | 2 | <link> |

# 5 · Tag Summary
`[MYTH] [SOURCE] [MYTH-UNCLEAR]`

# 6 · Revision Log
| Date | Author | Change |
|------|--------|--------|
| 2025‑07‑09 | Bot | Initial draft |
```

---

## 3 · Commit Lint Hook
* `scripts/local_build.sh` should run spell-check (`codespell`) and style‑lint (`markdownlint`) before pushing.

---

_End of file_
