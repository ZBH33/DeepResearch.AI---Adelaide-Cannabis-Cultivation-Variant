# Continuous Lint & Docs Deployment

## 1 · Spell + Link Checker
Workflow file: `.github/workflows/spell-link-lint.yml`

* **codespell** — catches typos.
* **lychee** — checks every Markdown link.
* Runs on every push & PR to the bot branch.
* Fails build on critical errors; warnings show inline in PR.

## 2 · GitHub Pages Site
Workflow file: `.github/workflows/pages.yml`

* Copies everything in `/docs/` into `_site/` and deploys via GitHub Pages.
* Trigger: any push that modifies `/docs/**`.
* First time: enable Pages in repo settings  
  *Settings → Pages → Build from GitHub Actions*.

Docs will publish at  
`https://zbh33.github.io/DeepResearch.AI---Adelaide-Cannabis-Cultivation-Variant`
