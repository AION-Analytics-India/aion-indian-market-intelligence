# aion-indian-market-intelligence

mcp-name: io.github.AION-Analytics/aion-indian-market-intelligence

Macro-event and sector impact intelligence for Indian financial markets.

[![PyPI version](https://img.shields.io/pypi/v/aion-indian-market-intelligence)](https://pypi.org/project/aion-indian-market-intelligence/)
[![Python](https://img.shields.io/pypi/pyversions/aion-indian-market-intelligence)](https://pypi.org/project/aion-indian-market-intelligence/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io)

## What it does

aion-indian-market-intelligence is a client package for AION Indian Market Intelligence. It sends Indian financial headlines to the managed AION API and returns structured macro event intelligence built around the canonical `sector_vector` key.

## Indian Market Intelligence for Macro Event Analysis

Built specifically for Indian markets. The managed API supports macro event analysis, policy impact analysis, sector exposure intelligence, and event-driven market intelligence for Indian financial headlines.

## NSE Sector Impact Analysis

For every headline, the API emits a `sector_vector`: a per-sector signed weight for sector impact analysis. The public package is an access layer only; production inference, coefficients, model weights, and private runtime logic are not distributed.

## Coverage

- Indian macro event intelligence
- sector impact analysis through `sector_vector`
- policy impact analysis for RBI, SEBI, fiscal, commodity, weather, and geopolitical events
- MCP-compatible Indian market intelligence server

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
  "event": "repo_rate_hike",
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

Use the dedicated MCP wrapper package when you want `uvx` to work directly:

```bash
uvx aion-indian-market-intelligence-mcp
```

The MCP wrapper depends on this hosted API client. It does not bundle a local
engine, taxonomy, rule files, models, or weights.

Claude Desktop config:

```json
{
  "mcpServers": {
    "aion-indian-market-intelligence": {
      "command": "uvx",
      "args": ["aion-indian-market-intelligence-mcp"],
      "env": {
        "AION_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

## Use Cases

- **Dashboards** — add structured macro event intelligence to Indian market dashboards.
- **Copilots** — ground LLM workflows in JSON sector impact analysis.
- **Internal research** — reduce the manual interpretation bottleneck after macro, policy, commodity, weather, and geopolitical events.
- **Policy impact analysis** — review RBI, SEBI, fiscal, and commodity events as sector incidence vectors.
- **Risk review** — inspect sector exposure intelligence before a human analyst makes a decision.

## Output Format

Every call returns a JSON object. The canonical key is `sector_vector` (a sector → signed-weight mapping), alongside event metadata, confidence fields, and market context when available.

```json
{
  "event": "sebi_regulation_tightening",
  "sector_vector": { "broking": -0.58, "amc": -0.49, "banking": -0.12 },
  "vix_regime": "normal",
  "confidence": 0.74
}
```

## Related AION packages

- [aion-indian-market-intelligence-mcp](https://pypi.org/project/aion-indian-market-intelligence-mcp/) — MCP server wrapper for this hosted API client
- [aion-indian-market-calendar](https://pypi.org/project/aion-indian-market-calendar/) — NSE/MCX/Muhurat trading calendar

---

AION Analytics — Built for Indian markets.
