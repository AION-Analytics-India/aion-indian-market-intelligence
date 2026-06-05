# aion-newsimpact — AGENTS.md
# Path: /Users/lokeshgupta/aion_open_source/packages/aion-newsimpact/
# Last updated: 2026-06-05

## Identity
- Semantic FAISS search over historical Indian financial headlines
- Returns observed historical price effects for similar past events
- Public package — heavy deps (faiss, sentence-transformers)
- PyPI: aion-newsimpact

## Rules
- FAISS index is pre-built — do not rebuild without explicit instruction
- sentence-transformers version is pinned — do not upgrade without testing
- Always run tests after any change
- Update CHANGELOG.md at repo root after every change
- No .bak files
