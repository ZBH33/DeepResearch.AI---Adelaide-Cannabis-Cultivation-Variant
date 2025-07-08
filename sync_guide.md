# SYNC_GUIDE · Export & GitHub Sync  
_Last revised: 2025-07-08_

This guide explains how the **research‑sync** workflow moves new research files to
the branch `DeepResearch.AI.AdelaideCannabisCultivationVariant`.

## 1 · Secrets Required

| Secret | Purpose |
|--------|---------|
| `DR_PAT` | Fine‑grained PAT from bot account, **Contents: Read & Write** |
| `GIT_NAME` | Commit author name (e.g., `DeepResearch-Bot`) |
| `GIT_EMAIL` | Commit author email (`deepresearch.ai.a.c.c.v@gmail.com`) |

## 2 · Workflow Highlights
1. **Checkout** the target branch.
2. **Generate** `research/index.md` and append a line to
   `meta/research_log.md`.
3. **Commit & push** using the PAT—no passwords stored.

## 3 · Safety Features
* Pushes only if `git diff --cached` finds changes.
* Commit message pulled from `commit_message_template.txt` for consistency.
* Logs every auto‑index event with a date‑stamped line.

## 4 · Manual Trigger
Use the **Actions → research‑sync → Run workflow** button for out‑of‑band
syncs.
