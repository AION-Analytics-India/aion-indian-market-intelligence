# API Specification

## AION Indian Market Intelligence

AION Indian Market Intelligence is an API-first market-intelligence service for
macro event intelligence and sector impact analysis in Indian financial markets.

The public Python client package calls the hosted API. The MCP package is a
separate wrapper around that client for MCP-compatible runtimes. Neither public
package includes production model weights, private taxonomy files, calibration
coefficients, backend API server code, or training scripts.

## Python Client

Install:

```bash
pip install aion-indian-market-intelligence
```

Configure:

```bash
export AION_API_KEY="<your_api_key>"
```

Use:

```python
from aion_indian_market_intelligence import analyze

result = analyze("RBI hikes repo rate by 25 bps")
print(result["sector_vector"])
```

## Managed API

Endpoint:

```text
POST https://api.aiondashboard.site/v1/analyze
```

Headers:

```text
X-API-Key: <key>
Content-Type: application/json
```

Request:

```json
{
  "headline": "RBI hikes repo rate by 25 bps",
  "published_at": "2026-06-05T09:00:00+05:30"
}
```

`published_at` is optional.

Response shape:

```json
{
  "headline": "string",
  "event": "string|null",
  "confidence": "float",
  "vix_regime": "string|null",
  "sector_vector": {},
  "top_positive_sectors": {},
  "top_negative_sectors": {},
  "sector_directional_bias": {
    "positive_bias": [],
    "negative_bias": []
  },
  "stakeholder_views": {},
  "raw_assignment": {}
}
```

`sector_vector` is the canonical output key. There is no public
`sector_impacts` replacement key.

## MCP Server

Console entrypoint:

```bash
uvx aion-indian-market-intelligence-mcp
```

Installed entrypoint:

```bash
pip install aion-indian-market-intelligence-mcp
aion-indian-market-intelligence-mcp --transport stdio
```

The canonical MCP package identity is
`aion-indian-market-intelligence-mcp`. The canonical client package identity is
`aion-indian-market-intelligence`.

MCP tool:

```text
analyze_news(headline: str, published_at: str | None = None)
```

The MCP wrapper returns structured sector impact analysis from the managed API.
It does not execute trades, route orders, provide advice, or claim guaranteed
market outcomes.

## Public Boundary

Public surfaces document:

- macro event intelligence
- sector impact analysis
- policy impact analysis
- event-driven market intelligence
- sector exposure intelligence
- MCP-compatible Indian market intelligence workflows

Public surfaces do not disclose:

- model weights
- private taxonomy files
- production coefficients
- backend API server code
- autonomous review queues
- training scripts
- calibration scripts
- rule-generation logic
