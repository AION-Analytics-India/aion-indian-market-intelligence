# aion-taxonomy

India macro event taxonomy for financial news classification and sector propagation.

![PyPI](https://img.shields.io/pypi/v/aion-taxonomy)
![Python](https://img.shields.io/pypi/pyversions/aion-taxonomy)
![License](https://img.shields.io/badge/License-Apache_2.0-blue)

`aion-taxonomy` provides the event ontology, primitive decomposition, and sector
dependency matrix used by `aion-indian-market-intelligence`. It supports
**Indian market taxonomy**, **macro event ontology**, **NSE sector matrix**, and
**financial event classification India** workflows.

> **Note:** This package is a dependency of `aion-indian-market-intelligence`.
> It is the rule and ontology layer, not a standalone end-user tool.

## What It Does

- Loads and validates the YAML taxonomy files
- Classifies headlines into macro events via keyword rules
- Computes macro and sector signals from classified events
- Blends rule confidence with model agreement

## Key Data Files

- `taxonomy_india_v2_calibrated.yaml` — calibrated event taxonomy
- `sector_matrix.yaml` — sector dependency matrix
- `cause_effect_rules_v3.yaml` — cause-effect propagation rules

## Installation

```bash
pip install aion-taxonomy
```

Requires Python 3.9+, `pyyaml>=6.0`, and `pandas>=2.0`. Optional sector mapping:

```bash
pip install "aion-taxonomy[sectormap]"
```

## Quick Start

```python
from aion_taxonomy import TaxonomyPipeline

pipeline = TaxonomyPipeline(
    taxonomy_path="taxonomy_india_v2_calibrated.yaml"
)

result = pipeline.process("RBI hikes repo rate by 25 bps")
print(result["macro_signal"])
```

## Lower-Level API

```python
from aion_taxonomy import (
    load_taxonomy,
    EventClassifier,
    get_macro_signal,
    get_sector_signal,
    compute_confidence,
)

taxonomy = load_taxonomy("taxonomy_india_v2_calibrated.yaml")

classifier = EventClassifier(taxonomy)
events = classifier.classify("Crude oil prices surge on supply concerns")

macro = get_macro_signal(events)
sector = get_sector_signal(events)
confidence = compute_confidence(events)
```

## Public API

- `TaxonomyPipeline` — end-to-end headline processing
- `EventClassifier` — keyword-based event classification
- `load_taxonomy` — load and validate a taxonomy YAML
- `get_macro_signal`, `get_sector_signal` — signal computation
- `compute_confidence` — confidence blending

## Related AION Packages

- `aion-indian-market-intelligence` — consumes this taxonomy
- `aion-sectormap` — NSE ticker → sector mapping
- `aion-volweight` — VIX-regime confidence weighting

## License

Apache-2.0.

---

*Part of the AION Analytics open-source ecosystem.*
