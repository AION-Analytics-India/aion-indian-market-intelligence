# Changelog

## [MCP Marketplace Metadata] - 2026-06-11

### Added

- Added `docs/mcp_marketplace_registry.json` as the maintained marketplace surface register.
- Added `docs/MCP_MARKETPLACE_MAINTENANCE.md` as the human-readable maintenance note for MCP marketplaces.
- Added `distribution/mcp/server.json` for the official MCP registry manifest using the dedicated MCP PyPI package.

### Changed

- Updated Continue configs, marketplace listing copy, standalone MCP repo copy, and API docs to use `aion-indian-market-intelligence-mcp` directly.
- Removed stale MCP marketplace guidance that used `uvx --from aion-indian-market-intelligence==1.0.6`.

### Validation

- `./venv/bin/python -m json.tool docs/mcp_marketplace_registry.json`
- `./venv/bin/python -m json.tool distribution/mcp/server.json`
- `./venv/bin/python` YAML load check for `distribution/continue/*.yaml`
- `rg` scan for stale `uvx --from aion-indian-market-intelligence==1.0.6` marketplace guidance outside this changelog
- PyPI JSON check: `aion-indian-market-intelligence-mcp==1.0.0`, `aion-indian-market-intelligence==1.0.8`
- `UV_CACHE_DIR=/tmp/aion_uv_cache_mcp_marketplace uvx aion-indian-market-intelligence-mcp --help`

## [MCP Package Shim] - 2026-06-11

### Added

- Added `aion_mcp_package/` for the approved public `aion-indian-market-intelligence-mcp` PyPI distribution.
- Added a thin `aion_mcp.server` entry point that delegates to the hosted API client MCP server.
- Added `REPO_GOVERNANCE.md` with the approved public package surfaces and MCP wrapper boundary.

### Changed

- Updated public install documentation so `uvx aion-indian-market-intelligence-mcp` resolves to a real PyPI package.
- Documented that the MCP package is a wrapper only and must not bundle taxonomy files, rule YAMLs, model weights, dependency matrices, or local inference logic.

### Validation

- `./venv/bin/python -m py_compile aion_mcp_package/src/aion_mcp/server.py aion_mcp_package/src/aion_mcp/__init__.py`
- `../venv/bin/python -m build` from `aion_mcp_package/`
- inspected wheel contents: only `aion_mcp` shim files and dist-info metadata; no YAMLs, models, taxonomy resources, or local engine files
- temporary-venv install smoke test: `aion-indian-market-intelligence-mcp --help`
- `../venv/bin/python -m twine check dist/*` from `aion_mcp_package/`
- uploaded `aion-indian-market-intelligence-mcp==1.0.0` to PyPI and verified the live package page.

## [Marketplace Release] — 2026-06-06

### Changed

- Published `aion-indian-market-intelligence` 1.0.6 to PyPI with MCP registry ownership marker.
- Updated Continue/MCP distribution manifests to 1.0.6.
- Published official MCP registry entry `io.github.AION-Analytics/aion-indian-market-intelligence` and deprecated the legacy `aion-news-to-signal` entry.

## [Public Repo Hardening] — 2026-06-05

### Changed

- Public repository scope hardened to user documentation, demo wrappers, public package clients, and public package sources only.
- Local inference runtime, private taxonomy files, backend API code, review queues, release feeds, automation scripts, and internal agent governance files removed from public tracking.
- Public directory names normalized around `aion-indian-market-intelligence`.
- `aion-newsimpact` moved under `packages/`.
- Hugging Face Space directory renamed to `hf_space_aion_indian_market_intelligence/`.
- Hugging Face model-card distribution directory renamed to `distribution/hf_model_aion_indian_market_intelligence/`.
- PyPI package workspace renamed to `pypi_aion_indian_market_intelligence/`.
- Public copy aligned around "AION Indian Market Intelligence", "macro event intelligence", and "sector impact analysis".

### Security

- `.gitignore` expanded to keep private runtime, taxonomy, calibration, training, backend, review, calendar-source, archive, and agent-governance files local-only.
- Public docs now state that production weights, coefficients, private taxonomy files, and backend runtime logic are not distributed.

## [Rename] — 2026-06-04

### Changed

- GitHub repository identity moved to `aion-indian-market-intelligence`.
- PyPI public package identity moved to `aion-indian-market-intelligence`.
- MCP entrypoint `aion-indian-market-intelligence-mcp` established as the canonical public entrypoint.

## [Initial Public Contract]

### Added

- Managed API client for AION Indian Market Intelligence.
- MCP-compatible wrapper for agent and IDE workflows.
- Public output contract centered on `sector_vector`.
