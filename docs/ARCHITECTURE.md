# Architecture

## AION Indian Market Intelligence

Public product identity:

- Public branded title: `AION Indian Market Intelligence for Macro Event & Sector Impact Analysis`
- Primary description: `Macro-event and sector impact intelligence for Indian financial markets.`
- Secondary description: `Structured analysis of how policy, economic, weather, and geopolitical events affect Indian market sectors.`
- Package distribution: `aion-indian-market-intelligence`
- Canonical import path: `aion_indian_market_intelligence`
- Canonical repository/model slug: `aion-indian-market-intelligence`
- Canonical output key: `sector_vector`, the sector impact analysis output

This layer converts Indian financial headlines into macro event analysis,
sector impact analysis, policy impact analysis, event-driven market
intelligence, economic propagation analysis, and sector effect modeling. It does
not emit executable guidance, broker orders, portfolio allocations, or order
instructions.

```text
[ HEADLINE INPUT ]
        ↓
[ EVENT CLASSIFIER ]
        ↓
[ DISAMBIGUATION (PMI + MARKOV) ]
        ↓
[ PRIMITIVE DECOMPOSITION ]
        ↓
[ SECTOR MATRIX ]
        ↓
[ CAUSAL PROPAGATION ]
        ↓
[ DYNAMIC MACRO FALLBACK ]
        ↓
[ VIX OVERLAY ]
        ↓
[ STAKEHOLDER VIEWS ]
        ↓
[ OUTPUT JSON ]
```

### Actual File Mapping

- `pypi_aion_news_to_signal/src/aion_indian_market_intelligence/__init__.py`
  - exports `analyze`
- `aion.py`
  - public local entrypoint
- `aion_news_to_signal_self_hosted/src/aion/pipeline.py`
  - versioned self-hosted package runtime consumed by installed environments
    that import `from aion import analyze, get_pipeline`
- `sector_propagation_engine.py`
  - taxonomy + rule + disambiguation + propagation + dynamic fallback gating
- `dynamic_macro_propagator.py`
  - template-level fallback for broad macro events not covered by specific rules
- `stakeholder_impact_mapper.py`
  - stakeholder reshaping of the post-VIX sector vector

### Stage Mapping

#### `[ HEADLINE INPUT ]`

Input enters via:

- `aion.analyze(headline, published_at=None)`
- or MCP tool `analyze_news(...)`

#### `[ EVENT CLASSIFIER ]`

Implemented by:

- `TaxonomyPipeline.process(...)`

Used from:

- `SectorPropagationEngine.propagate(...)`

This stage returns:

- taxonomy event
- sector signals
- macro signal
- taxonomy confidence

#### `[ DISAMBIGUATION (PMI + MARKOV) ]`

Implemented by:

- `EventHistoryModel.transition_score(...)`
- `EventHistoryModel.token_pmi_score(...)`
- `SectorPropagationEngine.disambiguate_event(...)`

This stage only activates when:

- `model_confidence < 0.7`
- and there are candidate events to compare

#### `[ PRIMITIVE DECOMPOSITION ]`

Implemented by:

- `CauseEffectRuleEngine.extract_conditions(...)`

Current primitive buckets:

- `weather_type`
- `crop_type`
- `commodity`
- `region`
- `month`
- `severity`
- `policy_action`
- `duration`

#### `[ SECTOR MATRIX ]`

Implemented by:

- taxonomy sector output from `TaxonomyPipeline`
- cause-to-sector mapping in `CAUSE_SECTOR_TO_MODEL_WEIGHTS`

#### `[ CAUSAL PROPAGATION ]`

Implemented by:

- `CauseEffectRuleEngine.propagation_timeline(...)`
- `CauseEffectRuleEngine.to_sector_vector(...)`

This stage activates only when:

- a cause-effect rule matched
- and `rule_match.score >= 0.5`

#### `[ DYNAMIC MACRO FALLBACK ]`

Implemented by:

- `DynamicMacroFallbackPropagator`
- `cause_effect_rule_classifier_v3/macro_event_templates.yaml`
- `DependencyWeightedPropagator`
- `VocabularyExpander`

This stage activates only when:

- no specific cause-effect YAML rule fired
- and the resolved event is missing or the combined sector vector is all zero

It selects a broad macro template by weighted expanded-keyword scoring, unique
keyword-family coverage, and a minimum meaningful-token density gate. Specific
terms such as `war`, `attack`, `crude oil`, or `repo rate` outrank generic terms
such as `rules` or `deadline`. The selected template then applies dependency
weights where relevant, marks the output in `raw_assignment.dynamic_fallback_*`,
and leaves the existing VIX overlay to the public `aion.analyze(...)` layer.
Dynamic fallback hits are telemetry, not final taxonomy authority; repeated
template hits are fed back into the review queue for specific-rule creation.

Learning automation:

- `src/api/null_event_logger.py` writes dynamic fallback hits to `aion_api.db`.
- `scripts/maintenance/weekly_rule_review.py` aggregates the last 7 days by
  `matched_template`. Templates with at least 20 hits append labeled headlines
  to `data/training/event_finetune.jsonl`.
- `scripts/maintenance/finetune_event_model.py` only trains when the JSONL has
  more than 100 previously unprocessed samples. It writes a versioned checkpoint
  under `models/aion_sentiment_unified_v4_1/versions/` and can deploy to the
  inference service path when explicitly invoked with `--deploy`.
- Launchd jobs: `com.aion.news-signal-weekly-rule-review` runs the weekly review
  with `--run-finetune`; `com.aion.news-signal-event-finetune` provides a
  monthly guarded fine-tune check.

Installed self-hosted runtimes also include a package-level deterministic macro
overlay for high-priority events that previously polluted downstream crawlers
when the frozen classifier fallback was trusted directly. This package overlay
currently covers geopolitical conflict, oil-supply shock, and commercial
LPG/fuel price policy changes, and includes a narrow non-financial guard that
returns `event: null` with an all-zero `sector_vector` for low-confidence,
out-of-domain headlines.

#### `[ VIX OVERLAY ]`

Implemented by:

- `VIXOverlay.snapshot(...)`
- `VIXOverlay.apply(...)`

Data source:

- `dataset/india_vix_daily_spot.csv`

#### `[ STAKEHOLDER VIEWS ]`

Implemented by:

- `stakeholder_impact_mapper.map_views(...)`

#### `[ OUTPUT JSON ]`

Final shape is assembled in:

- `aion.analyze(...)`

## Market Calendar

```text
[ SYSTEM CLOCK ]
        ↓
[ MARKET CALENDAR ]
        ↓
[ NSE CIRCULAR POLLER ]
        ↓
[ VALIDATION GATES ]
        ↓
[ LIVE DELTA WRITER ]
        ↓
[ SIGNED MANIFEST ]
        ↓
[ SESSION STATE ]
        ↓
[ VALIDATION LAYER ]
```

### Actual File Mapping

- `packages/aion_indian_market_calendar/_calendar.py`
- `packages/aion_indian_market_calendar/models.py`
- `packages/aion_indian_market_calendar/__init__.py`
- `packages/aion_indian_market_calendar/live_overrides.py`
- `scripts/poll_nse_rss.py`
- `scripts/run_nse_calendar_auto_updates.py`
- `scripts/apply_nse_circular_to_calendar.py`

### Stage Mapping

#### `[ SYSTEM CLOCK ]`

Time enters through:

- caller-provided `date`, `datetime`, or ISO string
- or internal `datetime.now(self.tz)`

Normalization is done by:

- `_coerce_datetime(...)`

#### `[ MARKET CALENDAR ]`

Implemented by:

- `IndiaMarketCalendar`

Data sources:

- bundled `data/events_2026.json`
- optional live delta JSON from `refresh_url`
- optional local live-delta authoring through `aion_indian_market_calendar.live_overrides`

Authority split:

- bundled wheel data is the stable baseline snapshot
- `refresh_url` live delta is the operational truth
- release publication should follow operational stability, not replace it

Live-refresh telemetry:

- implemented in `IndiaMarketCalendar._refresh_headers(...)`
- active only when live refresh targets an AION-owned host
- bundled/offline package usage does not emit telemetry
- telemetry sends a random local install ID plus package/Python/OS version headers
- users can opt out with `telemetry=False` or `AION_CALENDAR_TELEMETRY=0`
- telemetry is never attached to arbitrary third-party refresh URLs
- public verification paths:
  - PyPI download events via `curl -sS https://pypistats.org/api/packages/aion-indian-market-calendar/recent | python3 -m json.tool`
  - active live-refresh installs via `curl -sS https://dashboard.aiondashboard.site/api/calendar/telemetry/summary | python3 -m json.tool`

#### `[ NSE CIRCULAR POLLER ]`

Implemented by:

- `scripts/poll_nse_rss.py`
- `scripts/run_nse_calendar_auto_updates.py`

Source:

- official NSE RSS feed and linked NSE circular documents

Operational rule:

- this package does not use GitHub Actions or GitHub-triggered automation for calendar polling or mutation
- scheduler surfaces are local `launchd`, `cron`, VPS daemons, or Kubernetes CronJobs

#### `[ VALIDATION GATES ]`

Implemented by:

- `aion_indian_market_calendar.live_overrides.evaluate_nse_circular(...)`

Autonomous mutation only proceeds when all of these are true:

- source host is official NSE
- exactly one bundled holiday name is extracted
- exactly one deterministic candidate date remains after filtering out the current effective holiday date
- the candidate date differs from the current effective state
- wording is not ambiguous
- parser confidence meets the configured threshold

If any gate fails, the job writes review artifacts and exits without mutating the live delta.

#### `[ LIVE DELTA WRITER ]`

Implemented by:

- `aion_indian_market_calendar.live_overrides.apply_holiday_date_change(...)`
- `scripts/apply_nse_circular_to_calendar.py`

Output:

- repo-root `live_events.json`

This stage is the fast operational path for unexpected holiday shifts such as Eid/Bakri Id date changes announced by NSE circulars.

#### `[ SIGNED MANIFEST ]`

Implemented by:

- `aion_indian_market_calendar.live_overrides.refresh_live_manifest(...)`

Output:

- repo-root `live_events.manifest.json`

The autonomous path is expected to sign the manifest with an HMAC key so downstream systems can verify the exact live delta state that was published.

#### `[ ROLLBACK ]`

Implemented by:

- `aion_indian_market_calendar.live_overrides.revoke_generated_override(...)`
- `scripts/run_nse_calendar_auto_updates.py`

Rollback applies to generated live overrides, not to bundled wheel history.

The autonomous path can revoke a generated override when repeated revalidation
fails, the official source disappears, or later evidence contradicts the live
delta state. After rollback, the manifest is regenerated so clients can refresh
to the corrected operational truth.

#### `[ SESSION STATE ]`

Derived by:

- `holidays(...)`
- `_session_overrides_for_day(...)`
- `get_session(...)`
- `active_sessions(...)`

#### `[ VALIDATION LAYER ]`

Exposed as:

- `is_trading_day(...)`
- `is_market_open(...)`
- `next_trading_day(...)`

These functions do not place trades or enforce broker rules. They only return deterministic calendar state.
