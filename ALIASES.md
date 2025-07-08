# ALIASES · DeepResearch.AI  
_Last revised: 2025-07-08_

Aliases are short commands that speed up common tasks.  
Syntax: **`!alias [args]`** (always starts with `!`).

| Alias | Purpose | Modules Invoked | Sample Call | Safety Checks |
|-------|---------|-----------------|-------------|---------------|
| `!legal` | Generate or update **02-legal.md** entry. | M1 M3 M4 M5 | `!legal "single plant penalty"` | Checks: prompts must include statute name or keyword. |
| `!science` | Start a science report in **03-science.md**. | M1 M3 M4 M8 | `!science "optimal soil pH"` | Requires numeric variable (pH/temp) in args. |
| `!myth` | Add myth‑vs‑fact entry. | M13 M10 M1 | `!myth "pyramid power"` | Flags if `SOURCE` not provided. |
| `!patent` | Append to **05-patents.md**. | M14 M1 | `!patent AU-2025-12345` | Validates patent number regex. |
| `!export` | Force immediate research export & sync. | M7 workflow | `!export` | Blocks if QC FAIL. |
| `!audit` | Run Full Audit Mode on current draft. | M7 | `!audit` | None (read‑only). |
| `!index` | Regenerate `/research/index.md`. | Python step in workflow | `!index` | None, safe. |

**Alias Lifecycle**

1. User types `!alias` in chat.  
2. Pipeline routes command to Modules listed.  
3. Modules perform actions, produce output snippet.  
4. Output lands in correct domain file or triggers auto‑export.

---

## Adding New Aliases

1. Append a row to the table above.  
2. Define safety validation (regex or argument check).  
3. Update unit tests in `scripts/tests_alias.py`.  
4. Increment **PATCH** version.
