# aion-sectormap — AGENTS.md
# Path: /Users/lokeshgupta/aion_open_source/packages/aion-sectormap/
# Last updated: 2026-06-05

## Identity
- NSE ticker → sector / industry / GIN lookup
- 591+ companies, 44 sectors
- Public package — MIT or current licence
- PyPI: aion-sectormap

## Rules
- sector_map.json is the canonical data source — never edit manually
- Any sector addition requires a version bump and CHANGELOG entry
- Always run tests/ after any change
- Update CHANGELOG.md at repo root after every change
- No .bak files — use /tmp/ if needed
