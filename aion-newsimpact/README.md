# aion-newsimpact

Semantic search over historical Indian financial headlines with observed price effects.

![PyPI](https://img.shields.io/pypi/v/aion-newsimpact)
![Python](https://img.shields.io/pypi/pyversions/aion-newsimpact)
![License](https://img.shields.io/badge/License-Apache_2.0-blue)

Given a headline, `aion-newsimpact` finds semantically similar past Indian
financial news and returns their observed sector and price effects. It powers
**historical news impact** analysis, **Indian market news search**,
**headline similarity** matching, and **NSE price effect** estimation using
FAISS vector search.

## What It Does

You supply a DataFrame of historical headlines with their realized returns. The
package embeds the headlines, builds a FAISS index, and lets you query with a
new headline to retrieve the most similar past events and their average impact.

## Installation

```bash
pip install aion-newsimpact
```

Requires Python 3.9+. Pulls in `sentence-transformers>=2.2.0`,
`faiss-cpu>=1.7.0`, `pandas>=2.0.0`, and `numpy>=1.24.0`. For GPU search:

```bash
pip install "aion-newsimpact[gpu]"
```

## Quick Start

```python
import pandas as pd
from aion_newsimpact import NewsImpact

history = pd.DataFrame({
    "headline": [
        "RBI hikes repo rate by 25 bps",
        "Infosys reports strong quarterly earnings beat",
        "Crude oil prices surge on supply concerns",
        "Banking sector under regulatory scrutiny",
    ],
    "date": ["2025-02-08", "2025-04-18", "2025-03-01", "2025-05-12"],
    "returns_1d": [-0.012, 0.034, 0.021, -0.018],
    "ticker": ["NIFTYBANK", "INFY", "ONGC", "NIFTYBANK"],
    "sector": ["Banks", "IT", "Energy", "Banks"],
})

analyzer = NewsImpact(history, text_column="headline")

results = analyzer.query("Reserve Bank raises interest rates", top_k=3)
print(results.average_similarity)
print(results.average_return)
print(results.return_std)
```

## Inspecting Results

`query()` returns an `ImpactQueryResult` with parallel lists and aggregates:

```python
results = analyzer.query("Strong quarterly earnings", top_k=5)

for headline, date, sim, ret, ticker in zip(
    results.headlines,
    results.dates,
    results.similarity_scores,
    results.returns_1d,
    results.tickers,
):
    print(f"[{sim:.3f}] {date} {ticker}: {headline} ({ret:+.2%})")

df = results.to_dataframe()   # same results as a DataFrame
```

## Impact Statistics

```python
stats = analyzer.get_impact_stats()
stats["total_headlines"]
stats["avg_return_1d"]
stats["positive_impact_pct"]
```

## Adding Headlines

```python
new = pd.DataFrame({
    "headline": ["Nifty hits fresh all-time high"],
    "date": ["2025-06-01"],
    "returns_1d": [0.011],
    "ticker": ["NIFTY"],
    "sector": ["Broad Market"],
})

analyzer.add_headlines(new, rebuild_index=True)
```

## Optional: Volatility-Adjusted Confidence

Combine with `aion-volweight` to discount similarity in turbulent markets:

```python
from aion_volweight import adjust_confidence

results = analyzer.query("Strong quarterly earnings", top_k=5)
adjusted = adjust_confidence(results.average_similarity, vix=18.5)
```

## Related AION Packages

- `aion-volweight` — VIX-regime confidence weighting
- `aion-sectormap` — NSE ticker → sector mapping
- `aion-taxonomy` — event taxonomy and sector matrix

## License

Apache-2.0.

---

*Part of the AION Analytics open-source ecosystem.*
