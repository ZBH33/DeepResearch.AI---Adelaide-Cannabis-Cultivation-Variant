#!/usr/bin/env bash
# local_build.sh — lint & spell-check

set -e

echo "Running codespell..."
codespell --ignore-words-list="bot,filepath,statute" || true

echo "Running markdownlint..."
markdownlint '**/*.md' || true

echo "All lint checks completed."
