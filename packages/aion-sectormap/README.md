# aion-sectormap

NSE ticker to sector, industry, and GIN lookup for 591+ listed companies.

![PyPI](https://img.shields.io/pypi/v/aion-sectormap)
![Python](https://img.shields.io/pypi/pyversions/aion-sectormap)
![License](https://img.shields.io/badge/License-Apache_2.0-blue)

`aion-sectormap` maps NSE (National Stock Exchange of India) ticker symbols to
their sector, industry, business group, and Group Identification Number (GIN).
It is built for **NSE sector lookup**, **Indian stock sector mapping**, and
**NSE ticker classification** workflows.

## Coverage

- 591+ NSE-listed companies
- 44 sectors
- Business group identification with GIN codes
- Reverse lookups (sector → tickers) and company search

## Installation

```bash
pip install aion-sectormap
```

Requires Python 3.9+ and `pandas>=2.0.0`.

## Quick Start

```python
from aion_sectormap import SectorMapper

mapper = SectorMapper()

mapper.get_sector("RELIANCE")     # 'Oil, Gas & Consumable Fuels'
mapper.get_industry("TCS")        # 'Software & Services'
mapper.get_group("HDFCBANK")      # 'HDFC Bank Limited'
```

## DataFrame Mapping

Map an entire portfolio in one call:

```python
import pandas as pd
from aion_sectormap import SectorMapper

mapper = SectorMapper()

portfolio = pd.DataFrame({
    "ticker": ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ITC"],
    "quantity": [100, 50, 200, 100, 120],
})

mapped = mapper.map(portfolio, add_gin=True, add_company_name=True)
print(mapped[["ticker", "company_name", "sector", "group", "gin"]])
```

## Reverse Lookups & Search

```python
mapper = SectorMapper()

mapper.get_all_sectors()                      # list of 44 sectors
mapper.get_tickers_in_sector("Financial Services")
mapper.search_ticker("Tata")                  # DataFrame of matching companies
```

## Special Methods

```python
mapper = SectorMapper()

len(mapper)              # total tickers in database
"RELIANCE" in mapper     # True
"INVALID" in mapper      # False
```

Unknown tickers return a default you control:

```python
mapper.get_sector("INVALID", default="N/A")   # 'N/A'
```

## Related AION Packages

- `aion-taxonomy` — India macro event taxonomy and sector matrix
- `aion-volweight` — VIX-regime confidence weighting
- `aion-newsimpact` — historical headline impact search

## License

Apache-2.0.

---

*Part of the AION Analytics open-source ecosystem.*
