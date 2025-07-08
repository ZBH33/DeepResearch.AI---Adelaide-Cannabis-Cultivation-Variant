# Weekly Self‑Audit Cron (GitHub Actions)

Add this to `.github/workflows/weekly-audit.yml`

```yaml
name: Weekly Self‑Audit

on:
  schedule:
    - cron: '0 1 * * MON'   # 01:00 UTC every Monday
  workflow_dispatch:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: DeepResearch.AI.AdelaideCannabisCultivationVariant
      - name: Generate weekly meta entry
        run: |
          week=$(date +'%G-%V')
          year=$(date +'%G')
          mkdir -p meta/weekly_audit
          cp meta_entry_template.md meta/weekly_audit/${year}-${week}_meta.md
      - name: Commit & push
        env:
          GH_TOKEN: ${{ secrets.DR_PAT }}
          GIT_AUTHOR_NAME: ${{ secrets.GIT_NAME }}
          GIT_AUTHOR_EMAIL: ${{ secrets.GIT_EMAIL }}
        run: |
          git config --global user.name  "$GIT_AUTHOR_NAME"
          git config --global user.email "$GIT_AUTHOR_EMAIL"
          git add meta/weekly_audit || true
          if git diff --cached --quiet; then
            echo "No weekly audit changes"
          else
            git commit -m "📈 Weekly self‑audit scaffold"
            git push https://$GH_TOKEN@github.com/${{ github.repository }} HEAD:DeepResearch.AI.AdelaideCannabisCultivationVariant
```
