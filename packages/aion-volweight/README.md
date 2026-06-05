# aion-volweight

VIX-regime confidence weighting for Indian market sector signals.

![PyPI](https://img.shields.io/pypi/v/aion-volweight)
![Python](https://img.shields.io/pypi/pyversions/aion-volweight)
![License](https://img.shields.io/badge/License-Apache_2.0-blue)

`aion-volweight` scales the confidence of sector signals based on the prevailing
**India VIX** **volatility regime**. When volatility is elevated, signal
confidence is discounted; in calm markets it is preserved. This is useful for
**Indian market volatility** adjustment and **sector signal confidence**
calibration.

## What It Does

Given a VIX value, the package classifies the market into a volatility regime
(low / normal / elevated / extreme) and applies a corresponding multiplier to a
confidence score or to a column of sector signals.

## Installation

```bash
pip install aion-volweight
```

Requires Python 3.9+, `pandas>=2.0.0`, and `numpy>=1.24.0`.

## Quick Start

```python
from aion_volweight import get_regime, get_multiplier, adjust_confidence

vix = 18.5
regime = get_regime(vix)              # VIXRegime enum member
multiplier = get_multiplier(regime)   # regime multiplier
adjusted = adjust_confidence(0.90, vix)  # confidence scaled for this VIX
```

## DataFrame Weighting

Adjust a column of signal confidences for the current VIX:

```python
import pandas as pd
from aion_volweight import weight_confidence

signals = pd.DataFrame({
    "sector": ["Banks", "IT", "Auto", "Energy"],
    "sentiment_confidence": [0.95, 0.80, 0.70, 0.85],
})

weighted = weight_confidence(signals, vix_value=22.0)
print(weighted[["sector", "sentiment_confidence",
                "sentiment_confidence_adjusted"]])
```

You can name the output column explicitly:

```python
weighted = weight_confidence(
    signals,
    vix_value=22.0,
    confidence_col="sentiment_confidence",
    output_col="vol_adjusted_confidence",
)
```

## Custom Regime Thresholds

```python
from aion_volweight import VIXRegimeConfig, get_regime, adjust_confidence

config = VIXRegimeConfig(
    low_threshold=10.0,
    normal_threshold=18.0,
    high_threshold=30.0,
    high_multiplier=0.7,
    panic_multiplier=0.4,
)

get_regime(22.0, config=config)
adjust_confidence(0.85, 22.0, config=config)
```

## Public API

- `get_regime(vix, config=None)` — classify a VIX value
- `get_multiplier(regime)` — multiplier for a regime
- `adjust_confidence(confidence, vix, config=None)` — scale one value
- `weight_confidence(df, vix_value=...)` — scale a DataFrame column
- `VIXRegime`, `VIXRegimeConfig` — regime enum and configuration

## Related AION Packages

- `aion-newsimpact` — pairs with VolWeight to discount similarity confidence
- `aion-sectormap` — NSE ticker → sector mapping
- `aion-taxonomy` — event taxonomy and sector matrix

## License

Apache-2.0.

---

*Part of the AION Analytics open-source ecosystem.*
