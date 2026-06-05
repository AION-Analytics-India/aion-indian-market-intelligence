# aion-indian-market-intelligence

Convert Indian financial news headlines into structured NSE sector impact vectors — a macro-event intelligence layer for Indian markets.

[![PyPI version](https://img.shields.io/pypi/v/aion-indian-market-intelligence)](https://pypi.org/project/aion-indian-market-intelligence/)
[![Python](https://img.shields.io/pypi/pyversions/aion-indian-market-intelligence)](https://pypi.org/project/aion-indian-market-intelligence/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io)

## What it does

aion-indian-market-intelligence turns Indian financial news into machine-readable signals. It maps a headline to a macro-event ontology, propagates impact across NSE sectors, and applies a VIX volatility overlay to produce structured sector impact vectors. The output is a single JSON object built around the canonical `sector_vector` key.

## Indian Market Intelligence for Macro Event Analysis

Built specifically for Indian markets. The pipeline recognises 95 macro event types — monetary policy, fiscal action, SEBI regulation, commodity shocks, sector-specific catalysts — and resolves each into a weighted impact across 32 NSE sectors. It reads Indian financial news the way an Indian markets analyst would, not a generic Western-market model.

## NSE Sector Impact Analysis

For every headline, the engine emits a `sector_vector`: a per-sector signed weight indicating expected directional impact. Sector propagation uses input-output dependency weighting so that an event in one sector flows to its economically linked sectors, and a VIX overlay scales confidence to the prevailing volatility regime.

## Coverage

- 32 NSE sectors (banking, IT, auto, realty, FMCG, pharma, metals, energy, and more)
- 95 macro event types across monetary, fiscal, regulatory (incl. SEBI), commodity, and corporate-action categories
- Indian exchanges: NSE / BSE

## Quick Start

```bash
pip install aion-indian-market-intelligence
```

```python
from aion_indian_market_intelligence import analyze

result = analyze("RBI raises repo rate by 25 bps to tackle inflation")
print(result["sector_vector"])
```

Example output:

```json
{
  "headline": "RBI raises repo rate by 25 bps to tackle inflation",
  "event_type": "monetary_policy_tightening",
  "sector_vector": {
    "banking": 0.72,
    "realty": -0.65,
    "auto": -0.43,
    "fmcg": -0.18,
    "it": 0.11
  },
  "vix_regime": "elevated",
  "confidence": 0.81
}
```

*(Values shown are illustrative of the output schema, not a fixed model response.)*

## MCP Server for Indian Financial Markets

Run the analyzer as an MCP server so Claude and other MCP clients can convert Indian financial news into structured sector impact vectors on demand.

Claude Desktop config:

```json
{
  "mcpServers": {
    "aion-indian-market-intelligence": {
      "command": "uvx",
      "args": ["aion-indian-market-intelligence-mcp"]
    }
  }
}
```

## Use Cases

- **Premarket prediction** — feed overnight Indian financial news into a premarket model as structured features.
- **Algorithmic trading** — convert event flow into sector signals for systematic strategies.
- **Portfolio risk** — quantify how a macro event propagates across held NSE sectors.
- **Policy impact analysis** — assess SEBI and RBI actions as sector impact vectors.
- **Event-driven strategies** — trigger logic from classified Indian financial news events.

## Output Format

Every call returns a JSON object. The canonical key is `sector_vector` (a sector → signed-weight mapping), alongside `event_type`, `vix_regime`, and `confidence`.

```json
{
  "event_type": "sebi_regulation_tightening",
  "sector_vector": { "broking": -0.58, "amc": -0.49, "banking": -0.12 },
  "vix_regime": "normal",
  "confidence": 0.74
}
```

## Related AION packages

- [aion-indian-market-calendar](https://pypi.org/project/aion-indian-market-calendar/) — NSE/MCX/Muhurat trading calendar
- [aion-sectormap](https://pypi.org/project/aion-sectormap/) — NSE ticker → sector / industry lookup
- [aion-volweight](https://pypi.org/project/aion-volweight/) — VIX-regime confidence weighting
- [aion-newsimpact](https://pypi.org/project/aion-newsimpact/) — historical headline impact search

---

AION Analytics — Built for Indian markets.
