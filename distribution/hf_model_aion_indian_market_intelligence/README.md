---
language:
  - en
  - hi
license: agpl-3.0
tags:
  - finance
  - indian-markets
  - nse
  - sector-analysis
  - macro-events
  - news-classification
  - text-classification
  - event-driven
  - mcp-server
---

# AION Indian Market Intelligence

AION Indian Market Intelligence provides macro-event and sector impact intelligence for Indian financial markets. It converts Indian financial headlines into structured JSON centered on sector incidence vectors.

The public model card describes the managed intelligence surface. It does not distribute model weights, production coefficients, private taxonomy files, or runtime calibration logic.

Inference is available through the hosted AION API and through the `aion-indian-market-intelligence` Python package and MCP server.

## Intended uses

- Indian macro event intelligence
- Sector impact analysis for policy, economic, weather, commodity, and geopolitical events
- Structured sector exposure intelligence for dashboards and copilots
- RBI, SEBI, fiscal, commodity, and weather-event interpretation
- MCP-compatible Indian market intelligence workflows

## Out of scope

- No trade execution or order placement
- No real-time price or quote data
- No Western / non-Indian market coverage

## Example

**Input:** `"Government announces PLI scheme expansion for electronics manufacturing"`

**Output:**
```json
{
  "event_type": "fiscal_incentive_sector_specific",
  "sector_vector": { "electronics": 0.69, "capital_goods": 0.41, "it": 0.15 },
  "vix_regime": "normal",
  "confidence": 0.77
}
```
