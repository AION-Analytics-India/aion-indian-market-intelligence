# aion-taxonomy

Deterministic event classification and sector impact rules for Indian financial markets.

## Current Files

- `taxonomy_india_v2_calibrated.yaml` — legacy calibrated taxonomy surface used by older classifier paths
- `primitives.yaml` — 11 atomic causal primitives (`supply_shock`, `demand_shock`, etc.)
- `cause_effect_rules_v3.yaml` — 21 weather/crop cause-effect chains with historical evidence
- `sector_matrix.yaml` — 32-sector sensitivity matrix to primitive shocks
- `events.yaml` — human-approved primitive event registry

## Messaging Rule

Do not publish a single hard event-count claim from this directory until the legacy calibrated taxonomy, primitive event registry, sector matrix metadata, and live event feed are reconciled into one canonical taxonomy surface. Public wording should use terms such as "curated Indian-market event taxonomy" and "sector propagation rules" unless a validation artifact proves the current count.

## License

The taxonomy rule files are licensed under BSL 1.1 (source-available,
auto-converts to AGPLv3 in April 2030). See `../LICENSE.BSL11`.
