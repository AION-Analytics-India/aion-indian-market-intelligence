# Changelog
*Auto-maintained by Qwen Code + aion_algo_trading rules*
*Revert any change by finding timestamp and restoring from .bkup_{date} backup*

## [Identity Alignment] — 2026-06-06
### Fixed
- Updated self-hosted pipeline Hugging Face repo ID and cache directory names to `aion-indian-market-intelligence`.
- Updated Docker MCP entrypoint to `aion_indian_market_intelligence.mcp_server`.
- Normalized public-facing docs, tutorial assets, release JSON, and release feed URLs to the canonical `aion-indian-market-intelligence` identity.
- Removed the legacy MCP console-script alias from the PyPI package metadata.

## [MCP Import Fix] — 2026-06-06
### Fixed
- Updated `publish_assets/aion-mcp-server/aion_mcp_server.py` to import `analyze` from `aion_indian_market_intelligence` instead of the legacy `aion_news_to_signal` package name.

## [Calendar Reorganization] — 2026-06-05
### Changed
- Relocated `aion-indian-market-calendar` source documentation references to `packages/aion_indian_market_calendar/`.
- Updated calendar source-map, extension, cleanup, system overview, and boundary-audit docs to remove stale root-level package locations.
- Confirmed calendar package import name remains `aion_indian_market_calendar` and PyPI package name remains `aion-indian-market-calendar`.
- Aligned calendar package metadata and release documentation links to the dashboard canonical page at `/open-source/indian-market-calendar`.

## [Package Cleanup] — 2026-06-05
### Changed
- Added package-local AGENTS.md doctrine for aion-sectormap, aion-volweight, aion-newsimpact, and aion-taxonomy.
- Normalized package README H1 headings to package names for aion-sectormap, aion-volweight, aion-newsimpact, and aion-taxonomy.
- Updated aion-sectormap package fallback data path from the old root-level location to packages/aion-sectormap.
- Bumped aion-indian-market-intelligence PyPI package metadata to 1.0.5 and wired the PyPI long description to PYPI_DESCRIPTION.md content.
- Aligned aion-taxonomy source examples and README with taxonomy_india_v2_calibrated.yaml as the canonical taxonomy file.
- Replaced package READMEs for aion-sectormap, aion-volweight, aion-newsimpact, and aion-taxonomy with approved API-accurate documentation.

## [Security] — 2026-06-04
### Fixed
- Added *.db, *.sqlite, *.sqlite3 to .gitignore (critical gap)
- Added *.parquet to .gitignore (critical gap)
- Added src/api/ to .gitignore
- Added confidential patent docs to .gitignore
- Added CODEX_TASK_*.md to .gitignore for internal Codex/AI agent task files

## [1.0.5] — 2026-06-04
### Changed
- Internal PyPI package module renamed from aion_news_to_signal to aion_indian_market_intelligence
- MCP entry points updated to load aion_indian_market_intelligence.mcp_server
- Legacy MCP console-script alias removed from current package metadata; `aion-indian-market-intelligence-mcp` is the only promoted entry point
- Updated root AGENTS.md to make aion_indian_market_intelligence the canonical public import
### Fixed
- Updated legacy aion compatibility shim to import from aion_indian_market_intelligence after the internal module rename

## [Reorganization] — 2026-06-04
### Changed
- Moved satellite packages to packages/ directory
- Moved distribution surfaces to distribution/ directory
- Moved review_queue to ops/
- Archived aion-sentiment to archive/
- Removed empty self_hosted_aion_news_to_signal/ directory
### Fixed
- Updated runtime/script references for moved packages/, distribution/, and ops/ paths before JSON config review
- Updated release JSON validation commands to import aion_indian_market_intelligence while preserving legacy/public URL references

## [Phase 5] — 2026-06-04
### Changed
- GitHub repo renamed from aion-news-to-signal to aion-indian-market-intelligence
- git remote updated to new URL
- All internal GitHub URL references updated

## [2026-05-17 10:30:00 IST]
- [feat]: Added autonomous `aion-indian-market-calendar` NSE circular operations: deterministic gate evaluation, signed live-manifest refresh, scheduler-ready polling, generated-override rollback, and staged release-candidate preparation without autonomous PyPI publication. Added package-local doctrine that treats the wheel as a stable snapshot and `live_events.json` as the operational truth, with GitHub/GitHub Actions explicitly banned for this package's calendar workflows. (files: `packages/aion_indian_market_calendar/live_overrides.py`, `scripts/run_nse_calendar_auto_updates.py`, `scripts/apply_nse_circular_to_calendar.py`, `packages/aion_indian_market_calendar/AGENTS.md`, `AGENTS.md`, `packages/aion_indian_market_calendar/README.md`, `packages/aion_indian_market_calendar/CHANGELOG.md`, `docs/ARCHITECTURE.md`, `docs/API_SPEC.md`, `docs/EXTENSION_GUIDE.md`) | Task: market-calendar-autonomous-circulars-001
  type = feat
  task_id = market-calendar-autonomous-circulars-001

## [2026-05-16 09:35:00 IST]
- [fix]: Aligned public publishing surfaces around `AION Indian Market Intelligence`, `macro event analysis`, and `sector impact analysis`; published `aion-indian-market-intelligence==1.0.4` as the forward PyPI/MCP package identity while retaining `aion_news_to_signal` imports and `aion-news-to-signal` slugs as compatibility-only surfaces. Updated PyPI metadata, HF model/Space copy, MCP server metadata, Continue configs, release manifests, marketplace maintenance docs, and public docs to remove execution-oriented positioning from canonical copy. (files: `README.md`, `README_GITHUB.md`, `pypi_aion_news_to_signal/`, `hf_model_aion_news_to_signal/`, `hf_space_aion_news_to_signal/`, `aion_news_to_signal/mcp_server.py`, `wheel_build/`, `publish_assets/aion-mcp-server/`, `publish_assets/releases/`, `continue/`, `docs/`) | Task: indian-market-intelligence-identity-cleanup-001
  type = fix
  task_id = indian-market-intelligence-identity-cleanup-001

## [2026-05-15 11:41:00 IST]
- [feat]: Closed automation gaps across the self-evolving model loop: weekly AION Indian Market Intelligence fallback review now generates guarded event fine-tuning JSONL and can trigger the fine-tune gate, Veritas has a ClickHouse-backed weekly conformal-k recalibrator plus serving-time reload support in the premarket predictor, and Sentinel has an explicit Sunday full Screener refresh launchd job alongside the existing daily XBRL/alert pipeline checks (files: `scripts/maintenance/weekly_rule_review.py`, `scripts/maintenance/finetune_event_model.py`, `scripts/maintenance/recalibrate_veritas.py`, `plists/com.aion.news-signal-event-finetune.plist`, `plists/com.aion.veritas.recalibrate.plist`, external launchd/predictor/Sentinel pipeline files) | Task: self-evolving-automation-001
  type = feat
  task_id = self-evolving-automation-001

## [2026-05-12 00:00:00 IST]
- [docs]: Added explicit public verification commands for `aion-indian-market-calendar` adoption measurement. The README and architecture doc now show the exact `curl` commands for PyPIStats download events and the dashboard live-refresh telemetry summary, so public usage claims can be reproduced from source instead of inferred. (files: `packages/aion_indian_market_calendar/README.md`, `docs/ARCHITECTURE.md`) | Task: market-calendar-public-metrics-001
- [feat]: Added privacy-safe active-install telemetry to `aion-indian-market-calendar` live refresh. Bundled/offline usage stays silent; AION-owned refresh URLs receive only a random local install ID plus package/Python/OS version headers, with opt-out via `telemetry=False` or `AION_CALENDAR_TELEMETRY=0` (files: `packages/aion_indian_market_calendar/_calendar.py`, `packages/aion_indian_market_calendar/tests/test_calendar.py`, `packages/aion_indian_market_calendar/README.md`, `packages/aion_indian_market_calendar/CHANGELOG.md`, `packages/aion_indian_market_calendar/pyproject.toml`, `docs/ARCHITECTURE.md`) | Task: market-calendar-telemetry-001
- [docs]: Prepared `aion-indian-market-calendar` v1.1.3 metadata-only release with stronger LLM/search discovery terms for `pandas_market_calendars`, algorithmic trading, quantitative finance, NSE holidays, Indian trading holidays, BSE trading calendar, MCX evening session, market session validation, and India financial market calendar (files: `packages/aion_indian_market_calendar/README.md`, `packages/aion_indian_market_calendar/CHANGELOG.md`, `packages/aion_indian_market_calendar/pyproject.toml`) | Task: market-calendar-seo-001
  type = feat
  task_id = market-calendar-public-metrics-001,market-calendar-telemetry-001,market-calendar-seo-001

## [2026-05-11 10:48:00 IST]
- [fix]: Added the versioned self-hosted `aion-news-to-signal` package source (`1.0.0.post2`) and moved intraday runtime fixes out of `.venv/site-packages`. The package-level `analyze()` path now deterministically handles geopolitical conflict, oil-supply shock, and commercial LPG/fuel price policy headlines, and suppresses low-confidence out-of-domain classifier fallback for non-financial nonsense headlines (files: `aion_news_to_signal_self_hosted/pyproject.toml`, `aion_news_to_signal_self_hosted/README.md`, `aion_news_to_signal_self_hosted/src/aion/pipeline.py`) | Task: package-runtime-fix-001
  type = fix
  task_id = package-runtime-fix-001

## [2026-05-11 10:35:00 IST]
- [feat]: Added `geopolitical_conflict` to the dynamic macro fallback template set and replaced simple overlap matching with weighted keyword-family scoring plus a 10% meaningful-token density gate, so conflict terms such as attack/truce/military outrank generic regulatory words such as rules/talks (files: `cause_effect_rule_classifier_v3/macro_event_templates.yaml`, `dynamic_macro_propagator.py`, `sector_propagation_engine.py`, `docs/ARCHITECTURE.md`) | Task: geopolitical-conflict-fallback-001
  type = feat
  task_id = geopolitical-conflict-fallback-001

## [2026-05-11 08:20:00 IST]
- [feat]: Added dynamic macro-event fallback propagation for headlines that do not trigger specific YAML rules or taxonomy sector vectors. The fallback uses broad macro templates, vocabulary expansion, entity extraction, dependency weighting, explicit `raw_assignment.dynamic_fallback_*` telemetry, SQLite fallback logging, and review-queue refinement from repeated template hits (files: `cause_effect_rule_classifier_v3/macro_event_templates.yaml`, `dynamic_macro_propagator.py`, `sector_propagation_engine.py`, `aion.py`, `src/api/null_event_logger.py`, `scripts/maintenance/gather_null_events.py`, `scripts/maintenance/suggest_new_rules.py`, `src/api/app.py`, `src/api/server.py`, `docs/ARCHITECTURE.md`) | Task: dynamic-macro-fallback-001
- [fix]: Corrected `macro_rbi_repo_hike` sector polarity so higher rates are negative for rate-sensitive sectors and only defensive/INR-support logic remains positive where explicitly intended (files: `aion_taxonomy/taxonomy_india_v2_calibrated.yaml`) | Task: random-headline-verification-001
  type = feat,fix
  task_id = dynamic-macro-fallback-001,random-headline-verification-001

## [2026-05-03 22:10:00 IST]
- [fix]: Standardized the market-intelligence output around `sector_vector` and `sector_directional_bias`; removed public execution-oriented framing from runtime, MCP descriptions, package docs, HF model card, and tutorial surfaces (files: `aion.py`, `aion_news_to_signal/mcp_server.py`, `hf_space_aion_news_to_signal/aion.py`, `wheel_build/aion/pipeline.py`, `README.md`, `docs/`, `pypi_aion_news_to_signal/`, `hf_model_aion_news_to_signal/`, `publish_assets/aion-zerodha-bot-tutorial/`) | Task: news-to-signal-contract-cleanup-001
  type = fix
  task_id = news-to-signal-contract-cleanup-001

## [2026-04-12 18:50:00 IST]
- [release]: Pushed market intelligence layer to GitHub (commit f8f73d9) — 14 files, 1793 insertions; updated Hugging Face model card (commit 66fa66e) with 4-factor engine documentation (files: README.md, aion_taxonomy/README.md, aion-sentiment/src/aion_sentiment/__init__.py, aion_taxonomy/scripts/, scripts/, dataset/) | Task: task-018
  type = release
  task_id = task-018

## [2026-04-12 18:45:00 IST]
- [release]: Published aion-sentiment v0.3.0 to PyPI — added Market Intelligence Layer exports (classify_instrument, get_meta_factors, calculate_impact, rank_instruments_by_impact) with optional aion_taxonomy integration (files: aion-sentiment/src/aion_sentiment/__init__.py, dist/aion_sentiment-0.3.0-py3-none-any.whl, dist/aion_sentiment-0.3.0.tar.gz) | Task: task-017
  type = feat
  task_id = task-017

## [2026-04-12 18:30:00 IST]
- [docs]: Updated root README.md with Market Intelligence Layer section (4-factor model, Event Impact Engine examples, new platform components, v4.0.0 version history) and created aion_taxonomy/README.md; updated aion_sentiment/__init__.py to export classify_instrument, get_meta_factors, calculate_impact (files: README.md, aion_taxonomy/README.md, aion-sentiment/src/aion_sentiment/__init__.py, scripts/) | Task: task-016
  type = docs
  task_id = task-016

## [2026-04-12 18:00:00 IST]
- [feat]: 4-factor rolling correlations computed — aggregated 5-min VIX to daily (413 rows), merged with ClickHouse VIX (503 rows total), aligned all factors + 14 sectors (415 days), computed 90-day rolling correlations (interest_rate, crude_oil, rupee, risk_sentiment) (files: dataset/vix_daily_full.csv, dataset/aligned_4factor_daily.csv, aion_taxonomy/src/aion_taxonomy/data/sector_sensitivities.json) | Task: task-012,task-013,task-014,task-015
  type = feat
  task_id = task-012

## [2026-04-12 17:03:00 IST]
- [feat]: Scraped 538 trading days of FPI daily equity net flows from NSDL archive (Apr 2024 – Mar 2026) via batched month-end XHR requests with fresh viewstate tokens (files: dataset/fpi_daily_nsdl.csv) | Task: task-011
  type = feat
  task_id = task-011

## [2026-04-12 16:16:00 IST]
- [feat]: Backfilled G-Sec 10Y yield to 2 years (504 rows, Apr 2024 → Apr 2026) via 5 additional XHR batches to Investing.com (curr_id=24014) (files: dataset/India 10-Year Bond Yield Historical Data.csv) | Task: task-008
  type = feat
  task_id = task-008

## [2026-04-12 15:00:00 IST]
- [feat]: Layer 4 complete — dynamic sensitivity calibration via 90-day rolling correlations (files: aion_taxonomy/scripts/fetch_meta_data.py, aion_taxonomy/scripts/update_sensitivities.py, aion_taxonomy/scripts/scrape_gsec_yield.py, aion_taxonomy/scripts/refresh_sensitivities.py, aion_taxonomy/src/aion_taxonomy/instrument_classifier.py, aion_taxonomy/src/aion_taxonomy/data/sector_sensitivities.json, dataset/India 10-Year Bond Yield Historical Data.csv) | Task: task-008,task-009,task-010,task-011
  type = feat
  task_id = task-008

## [2026-04-10 12:45:00 IST]
- [feat]: Extended instrument_classifier.py to handle currency derivatives (CDS) and bond/G-Sec fixed income instruments (files: aion_taxonomy/src/aion_taxonomy/instrument_classifier.py) | Task: task-002
  type = feat
  task_id = task-002

## [2026-04-10 12:40:00 IST]
- [feat]: Extended instrument_classifier.py to handle commodity instruments (MCX/NCO) with precious metal, energy, base metal sub-classification (files: aion_taxonomy/src/aion_taxonomy/instrument_classifier.py) | Task: task-002
  type = feat
  task_id = task-002

## [2026-04-10 12:35:00 IST]
- [feat]: Added instrument_classifier.py to aion_taxonomy for equity spot and index derivative classification (files: aion_taxonomy/src/aion_taxonomy/instrument_classifier.py) | Task: task-002
  type = feat
  task_id = task-002

## [2026-04-10 12:25:00 IST]
- [feat]: Published 3 packages to PyPI — aion-sectormap (v0.1.0), aion-volweight (v0.1.0), aion-taxonomy (v1.0.0) (files: aion-sectormap/dist/, aion-volweight/dist/, aion_taxonomy/dist/) | Task: pypi-publish-all-packages-001
  type = feat
  task_id = pypi-publish-all-packages-001

## [2026-04-06 14:00:00 IST]
- [fix]: Added inference-time override for high-impact negative events to fix false positive sentiment (files: models/aion_sentiment_unified_v1/README.md, src/zerodha/crawlers/gift_nifty_gap.py) | Task: fix-sentiment-false-positive-001
  type = fix
  task_id = fix-sentiment-false-positive-001
- [feat]: Generated 4,000 synthetic training examples for 8 underrepresented negative events (files: generate_synthetic_events.py, synthetic_events.csv) | Task: fix-sentiment-false-positive-001
  type = feat
  task_id = fix-sentiment-false-positive-001
- [feat]: Merged synthetic data with training_data_unified.csv → training_data_augmented.csv (104,470 rows) (files: merge_synthetic_data.py, training_data_augmented.csv) | Task: fix-sentiment-false-positive-001
  type = feat
  task_id = fix-sentiment-false-positive-001
- [fix]: Fixed sentiment labels in training data based on macro_signal sign (files: fix_sentiment_labels.py, training_data_fixed.csv) | Task: fix-sentiment-false-positive-001
  type = fix
  task_id = fix-sentiment-false-positive-001
- [chore]: Added --data and --sentiment-weight args to train_multitask.py (files: train_multitask.py) | Task: fix-sentiment-false-positive-001
  type = chore
  task_id = fix-sentiment-false-positive-001
- [docs]: Created GitHub issue #1 and HuggingFace discussion #1 documenting known issue and workaround (files: github_issue_false_positive.md, hf_discussion_override.md) | Task: fix-sentiment-false-positive-001
  type = docs
  task_id = fix-sentiment-false-positive-001
- [feat]: Trained 6 batch models (multi_task_v2_batch1-6) on 100K+ rows for v2.0 retraining (files: models/multi_task_v2_batch1-6/) | Task: fix-sentiment-false-positive-001
  type = feat
  task_id = fix-sentiment-false-positive-001
- [feat]: Created balanced sentiment dataset pipeline and batch splitting (files: training_data_fixed_batch_1-6.csv, balanced_sentiment.csv) | Task: fix-sentiment-false-positive-001
  type = feat
  task_id = fix-sentiment-false-positive-001

## [1.0.0] - 2026-04-05

AION Unified Sentiment Model v1 — multi-task transformer for Indian financial news.

### Multi-Task Model Architecture

- Built MultiTaskModel: DistilBERT encoder with 4 task heads
  - Sentiment head: 3-class classification (negative/neutral/positive), cross-entropy loss
  - Event head: 95-class classification (taxonomy events), cross-entropy loss
  - Macro head: regression (-1 to +1 market impact), MSE loss
  - Sector head: 32-dim regression (NSE sector impacts), MSE loss
- Base model: distilbert-base-uncased, 67M parameters, 270MB
- Max sequence length: 128 tokens

### Training Pipeline

- Extracted 100,470 raw headlines from ClickHouse aion_master
- Labeled sentiment via AION-Sentiment-IN-v3 model
- Merged with Nifty 100 labeled (6,910 headlines) and baptle labeled (248 headlines)
- Generated 200 synthetic rupee appreciation headlines with correct negative sentiment to fix "strengthens = positive" polarity flip
- Final training set: 42,214 rows (2,979 event-matched, 39,235 sentiment-only)
- Separated training strategy: event rows train all 4 heads at 10x weight, sentiment-only rows train sentiment head only
- Loss weights: event=10.0, macro=10.0, sector=10.0, sentiment=1.0
- Trained 5 epochs, batch_size=64, lr=2e-5
- 5 epochs, batch_size=64, lr=2e-5 on Apple M4 (MPS acceleration)

### Taxonomy Integration

- Added context_rules to taxonomy_india_v2_calibrated.yaml for currency_appreciation, currency_depreciation, bank_npa, layoffs
- Context rules override polarity: e.g. rupee strengthens → negative sentiment (hurts exporters)
- Sector bias rules: inverse (IT, Healthcare) vs aligned (Oil, Aviation, Metals, Capital Goods)

### Ticker and Sector Mapping

- Created ticker_to_sector.json: 90 NSE tickers across 32 sectors
- _detect_ticker(headline): extracts NSE symbols from headlines (longest-match first + name variants)
- _unified_analysis(headline, ticker): returns sentiment, event_id, macro_signal, sector_impacts, active_sector_signal, active_sector_id

### Crawler Integration (gift_nifty_gap.py)

- Replaced legacy AION Sentiment v3 with unified MultiTaskModel in Zerodha Pulse crawler
- Added ticker detection and active sector resolution
- News published to Redis news:sorted_set with enriched fields: sentiment, event_id, macro_signal, 32-sector impacts, active_sector_id, relevant_indices
- ~30ms inference time per headline on MPS

### Temperature Scaling

- Added temperature scaling T=1.5 to softmax during inference
- Reduces overconfidence: 1.00 → 0.96 for strong signals, 0.64 → 0.57 for uncertain ones
- Applied to both sentiment and event logits
- Argmax predictions unchanged, only confidence values are calibrated

### Premarket Predictor Integration

- Updated nifty_open_predictor.py to read from indices_master_v3 (was v1)
- Migrated US500, GIFT NIFTY, NIFTY 50, INDIA VIX, NIFTY BANK from ticks_buffer_v1 to indices_master_v3 (34,677 rows)
- Migrated sectoral banks: NSENIFTYPVTBANK, NSENIFTYPSUBANK, NSENIFTYFINSERVICE (23,426 rows)
- Updated all 12 ClickHouse queries to v3 table
- Updated news sentiment reader to accept event_confidence field (was only confidence_adjusted/confidence_base)

### Model Evaluation

- 8/8 validation checks passed on live Zerodha Pulse headlines:
  - "Rupee strengthens..." → negative (0.94), IT=-0.34, Healthcare=-0.32, Aviation=+0.32
  - "RBI repo cut..." → positive (0.97), Banks=+0.06, Auto=+0.07
  - "Sensex crashes..." → negative (0.98), macro=-0.23
  - "Reliance profit..." → positive (1.00), macro=+0.26
- Sentiment accuracy: 97.2%
- Event classification accuracy: 99.5%
- Macro signal correlation: 0.990
- Sector impacts average MAE: 0.0043

### HuggingFace Deployment

- Model: https://huggingface.co/AION-Analytics/aion-sentiment-unified-v1
  - 9 files: pytorch_model.bin, config.json, event_mapping.json, sector_order.json, tokenizer.json, README.md
- Dataset: https://huggingface.co/datasets/AION-Analytics/indian_financial_news_42k
  - 42,214 rows with 32 sector columns, Apache 2.0 license

### PyPI Package

- Package: aion-sentiment v0.2.0
- URL: https://pypi.org/project/aion-sentiment/0.2.0/
- Updated description to reflect unified model capabilities
- Author email: aionlabs@tutamail.com

### GitHub Repository

- Repo: https://github.com/AION-Analytics/aion-indian-market-intelligence
- Removed legacy aion-sentiment-in/ (24 files, 147,374 lines of old v1/v2/v3 code)
- Removed emotions.py, NRC lexicons (141,893 lines), old tests, example.py
- Updated README with unified model quick start and HuggingFace links
- Updated pyproject.toml and setup.py descriptions

### Code Cleanup

- Deleted et_headlines.txt, et_scrape_progress.txt (scrape artifacts)
- Rewrote CHANGELOG.md with unified model documentation only
- Archived outdated legacy v3 contribution instructions; current extension guidance lives in docs/EXTENSION_GUIDE.md.

## [0.1.0] - 2026-03-14

- Initial release: aion-sentiment with transformer-based financial text classification
- Trained on 957K Indian financial news headlines
