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
