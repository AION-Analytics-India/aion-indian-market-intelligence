# aion_taxonomy — AGENTS.md
# Path: /Users/lokeshgupta/aion_open_source/aion_taxonomy/
# Last updated: 2026-06-05

## Identity
- India macro event taxonomy — backbone for aion_indian_market_intelligence pipeline
- Canonical file: taxonomy_india_v2_calibrated.yaml
- Also provides: events.yaml, primitives.yaml, sector_matrix.yaml, cause_effect_rules_v3.yaml
- Public package AND private pipeline dependency

## WARNING
This package is the hard backbone of the private inference pipeline.
Any change to taxonomy structure breaks aion_indian_market_intelligence.
Never change taxonomy without:
1. Testing against full pipeline
2. Version bump
3. CHANGELOG entry
4. Explicit approval

## Rules
- taxonomy_india_v2_calibrated.yaml is canonical — all other taxonomy files derive from it
- cause_effect_rules_v3.yaml is the active rules version — v1/v2 are fallbacks only
- sector_matrix.yaml defines sector dependency weights — never edit without backtest
- Update CHANGELOG.md at repo root after every change
- No .bak files
