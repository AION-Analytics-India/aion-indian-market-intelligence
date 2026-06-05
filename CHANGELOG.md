# Changelog

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
