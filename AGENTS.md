# AION Open Source — Project AGENTS.md

## 0. Project Identity & Scope
- **Project root:** `/Users/lokeshgupta/aion_open_source`
- **Runtime environment:** Root Python environment is `./venv` (`Python 3.13.9`). Root dependencies live in `requirements.txt`. Several publishable subprojects maintain their own `pyproject.toml` or `requirements.txt`.
- **Version control:** Git repository, `origin=https://github.com/AION-Analytics/aion-indian-market-intelligence.git`
- **Baseline backup:** `archive/` is the current archive root. No separate full-project baseline backup path is documented yet.

## 1. Documentation Authority
- **Single source of truth:** `docs/ARCHITECTURE.md`
- **Changelog:** `CHANGELOG.md`
- **Archived docs:** `archive/`

## 2. Deployment Targets (if applicable)
- **Local packaging and release workspace:** `/Users/lokeshgupta/aion_open_source`
- **GitHub source/release target:** `origin=https://github.com/AION-Analytics/aion-indian-market-intelligence.git`
- **API workflow credential file:** `/Users/lokeshgupta/.aion/api_tokens.json`. Use this file for approved GitHub/HF/PyPI/API workflow credentials; never print token values or write them into logs, docs, or changelogs.
- **MCP publisher credential file:** `/Users/lokeshgupta/.config/mcp-publisher/token.json`. Use this file only for approved MCP registry publisher workflows; never print token values or write them into logs, docs, or changelogs.
- **PyPI package surfaces:** `pypi_aion_news_to_signal/` and the public package contract documented in `README.md`
- **Hugging Face surfaces:** `hf_model_aion_news_to_signal/` and `hf_space_aion_news_to_signal/`

## 3. Non-Negotiable Doctrines
- `docs/ARCHITECTURE.md` and `CHANGELOG.md` must be updated in the same patch whenever the public package contract, pipeline stage mapping, or output schema changes.
- **GitHub visibility/name lock:** `https://github.com/AION-Analytics/aion-indian-market-intelligence.git` is off-limits for public exposure and further identity changes. Never make this repository public, rename it again, transfer it, or attempt GitHub-side marketplace fixes that require changing its visibility, owner, slug, or repository metadata. If a marketplace requires a public GitHub repo or another rename, stop and ask the owner instead of proceeding.
- The canonical public import is `from aion_indian_market_intelligence import analyze`. The legacy `from aion import analyze` path is compatibility-only and must not become the new authority.
- `sector_vector` is the canonical output key. Do not introduce or re-authorize `sector_impacts` as a competing public key.
- Preserve the architecture stage boundaries documented in `docs/ARCHITECTURE.md`: classifier -> disambiguation -> primitive decomposition -> sector matrix -> causal propagation -> VIX overlay -> stakeholder views -> output JSON.
- This repo is a source, packaging, and documentation surface. Production inference is the hosted API described in `README.md`; do not imply local repo contents include production model weights unless that contract is intentionally changed.

## 4. Change Rules
- Use `./venv` for root-level Python execution unless a subproject documents a different runtime.
- Before changing output JSON, package names, API shapes, or release metadata, trace every direct consumer in `README.md`, `docs/`, package directories, and release scripts.
- Keep changes narrow. If a change touches package metadata, release scripts, or public docs, verify the package surface and documentation stay aligned.
- Run at least a narrow compile/import proof before finishing any Python change.
- Do not create ad hoc `.bak` files. Move superseded docs or release artifacts into dated locations under `archive/`.

## 5. Key Dependencies Map
- `pypi_aion_news_to_signal/src/aion_indian_market_intelligence/__init__.py` -> canonical package surface exporting `analyze` for library consumers.
- `aion.py` -> local/public compatibility entrypoint and legacy alias surface.
- `sector_propagation_engine.py` -> core taxonomy, disambiguation, rule, and propagation engine consumed by the `analyze` path.
- `stakeholder_impact_mapper.py` -> consumes the post-VIX sector vector and reshapes it into stakeholder-facing views.
- `packages/aion_indian_market_calendar/` -> separate package surface for India market session logic; keep its package contract stable when editing shared calendar behavior.
- `packages/aion_indian_market_calendar/AGENTS.md` -> package-local operating doctrine for `aion-indian-market-calendar`, including the explicit ban on GitHub/GitHub Actions automation for calendar polling, live-delta mutation, and release-trigger workflows.

## 6. Backup & Archive Policy
- **Baseline backup path:** `archive/` until a dedicated full-project baseline path is established.
- **Archive directory:** `archive/`
- **No `.bak` files rule:** Do not create per-change backups. Archive superseded docs or artifacts into dated subdirectories under `archive/`.

## 7. Agent Role (if applicable)
- No project-specific role registry is defined at the root today.

## 8. Common Proof Commands
- `./venv/bin/python --version`
- `./venv/bin/python -m compileall aion.py pypi_aion_news_to_signal/src/aion_indian_market_intelligence`
- `./venv/bin/python -c "from aion_indian_market_intelligence import analyze; print(callable(analyze))"`
- `./venv/bin/python -c "from aion import analyze; print(callable(analyze))"`
- `rg -n "sector_vector|sector_impacts|analyze" README.md docs aion.py pypi_aion_news_to_signal/src/aion_indian_market_intelligence`
- `git status --short`
