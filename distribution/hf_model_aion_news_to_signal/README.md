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

AION Indian Market Intelligence converts Indian financial news headlines into structured NSE sector impact vectors. It is built for quantitative researchers, algo traders, and risk teams working specifically in Indian markets, and serves as the macro-event intelligence layer between raw Indian financial news and downstream prediction models.

The model is the front of an ontology-driven pipeline. A headline is classified into one of 95 macro event types, disambiguated against an Indian-market event ontology, then propagated across 32 NSE sectors using input-output dependency weighting. A VIX overlay scales the resulting `sector_vector` to the prevailing volatility regime, so the same event produces sharper or softer signals depending on market conditions.

In production, AION Indian Market Intelligence feeds the AION Veritas premarket prediction model, supplying structured overnight-news features ahead of the Indian market open. Inference is available through the hosted AION API and via the `aion-indian-market-intelligence` Python package and MCP server.

## Intended uses

- Premarket prediction feature generation for Indian equities
- Sector signal generation for systematic / algorithmic strategies
- Portfolio risk attribution across NSE sectors from macro events
- SEBI and RBI policy impact analysis as sector impact vectors
- Event-driven strategy triggers from classified Indian financial news

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
