[![Version](https://img.shields.io/badge/version-1.0.3-blue)](https://pypi.org/project/aion-indian-market-intelligence/)

# AION Indian Market Intelligence for Macro Event & Sector Impact Analysis

Indian Market Intelligence for Macro Event & Sector Impact Analysis.

Indian Market Intelligence for Macro Event & Sector Impact Analysis is the
single public identity for this product. It is an API for Indian SaaS
developers, professional coders, LLM tools, dashboards, and analyst workflows
that need macro event intelligence and sector impact analysis from Indian
financial headlines.

AION Indian Market Intelligence for Macro Event & Sector Impact Analysis
converts raw Indian financial headlines into market impact ontology output. It
answers: what happened, which sectors are exposed, which stakeholders are
affected, and which macro effects are in play. It does not tell you what to
trade.

## Install

```bash
pip install aion-indian-market-intelligence
```

## API Key Setup

```bash
export AION_API_KEY="<your_api_key>"
```

## Canonical Imports

```python
from aion_indian_market_intelligence import analyze
```

Legacy compatibility alias:

```python
from aion import analyze
```

This alias remains supported and routes through the managed AION API.

## API Contract

Production usage flows through the managed AION API:

- `POST https://api.aiondashboard.site/v1/analyze`
- header:
  - `X-API-Key: <key>`

```python
import requests

headers = {"X-API-Key": "YOUR_API_KEY"}
resp = requests.post(
    "https://api.aiondashboard.site/v1/analyze",
    headers=headers,
    json={"headline": "RBI hikes repo rate by 25 bps"},
    timeout=30,
)
resp.raise_for_status()
print(resp.json()["sector_vector"])
```

## Output Contract

Observed top-level output keys:

```json
{
  "headline": "string",
  "event": "string|null",
  "confidence": "float",
  "vix_regime": "string",
  "sector_vector": {},
  "top_positive_sectors": {},
  "top_negative_sectors": {},
  "sector_directional_bias": {
    "positive_bias": [],
    "negative_bias": []
  },
  "stakeholder_views": {},
  "raw_assignment": {
    "resolved_event_id": "string|null",
    "cause_effect_rule_id": "string|null",
    "weather_triggered": "bool"
  }
}
```

Canonical key note:

- `sector_vector` is the canonical output key for sector impact analysis
- there is no `sector_impacts` key in the public output contract

## Output-Centric Example

Input:

```text
RBI unexpectedly raises repo rate by 50 bps
```

Example view:

```json
{
  "event": "repo_rate_hike",
  "sector_vector": {
    "Information Technology": 0.18,
    "Realty": -0.52,
    "Financial Services": -0.31,
    "Automobile and Auto Components": -0.26
  },
  "top_positive_sectors": {
    "Information Technology": 0.18
  },
  "top_negative_sectors": {
    "Realty": -0.52,
    "Financial Services": -0.31,
    "Automobile and Auto Components": -0.26
  },
  "macro_effects": {
    "liquidity": "tightening",
    "credit_growth": "slowing",
    "policy_impact_mapping": "rate-sensitive sectors under pressure"
  }
}
```

This is macroeconomic event API output for Indian Market Intelligence for Macro
Event & Sector Impact Analysis. It is not broker execution guidance.

## Before / After

Headline:
> Unseasonal rainfall and hailstorm hit apple orchards in Himachal Pradesh in April

Typical polarity-only output:
- negative

AION Indian Market Intelligence for Macro Event & Sector Impact Analysis output:
- event / rule: `rain_apple_damage`
- likely losers: `Agriculture & Horticulture`, `Transportation`, `Consumer Services`
- potential second-order beneficiaries: storage-linked or substitute supply chains
- stakeholder view: producer losses, policymaker inflation watch, investor attention on downstream second-order effects

Market implication: agriculture-linked exposure under pressure, logistics
bottlenecks possible, substitute supply chains may benefit.

## What AION Indian Market Intelligence for Macro Event & Sector Impact Analysis Does

- provides Indian macro event intelligence from financial headlines
- provides sector impact analysis through the canonical `sector_vector`
- supports financial causality mapping and event-to-sector reasoning
- returns sector exposure intelligence for dashboards, agents, and internal tooling
- supports policy impact mapping and event-driven financial inference without
  collapsing into execution language

## Why Not Polarity-Only NLP?

Most open-source financial NLP tools stop at polarity scoring.

| Capability | AION Indian Market Intelligence for Macro Event & Sector Impact Analysis | Polarity-only NLP |
|---|---|---|
| Indian market event logic | Yes | No |
| Sector impact analysis | Yes | No |
| Sector exposure intelligence | Yes | No |
| Policy impact mapping | Yes | No |
| Stakeholder decomposition | Yes | No |
| Macroeconomic event API workflow | Yes | No |
| Financial event ontology | Yes | No |

Polarity-only NLP tells you whether a headline reads positive or negative.

AION Indian Market Intelligence for Macro Event & Sector Impact Analysis tells you:

- what happened
- which sectors are affected and in what direction
- who gains and who loses
- whether there is a flip side
- what the evidence layer suggests for further human or system review

## Canonical Vocabulary

Public docs, model cards, PyPI copy, MCP copy, and dashboard pages use
`Indian Market Intelligence for Macro Event & Sector Impact Analysis` as the
single identity phrase. Supporting vocabulary is maintained in
`docs/CANONICAL_VOCABULARY.yml`.

Primary phrases include:

- macro event intelligence
- sector impact analysis
- sector propagation engine
- financial causality mapping
- market impact ontology
- event-to-sector reasoning
- macroeconomic event API
- sector exposure intelligence
- policy impact mapping
- event-driven financial inference
- financial event ontology
- sectoral impact engine

These phrases are intentional for human search, PyPI discovery, Hugging Face
indexing, GitHub topics, MCP registry copy, and LLM retrieval embeddings.

## Pricing & Tiers (Draft — Current as of May 2026)

All tiers require an API key. Sign up at
`https://dashboard.aiondashboard.site/access/register`

| Tier | Requests/month | Latency |
|---|---:|---|
| Free | 1,000 | Shared |
| Builder | 15,000 | Shared |
| Pro | 75,000 | Priority |
| Power | 250,000 | Dedicated |

Enterprise: custom, GPU-dedicated. Contact via dashboard.

## Access And Links

- API gateway:
  - `https://dashboard.aiondashboard.site/systems/api-gateway`
- Website model page:
  - `https://dashboard.aiondashboard.site/models/indian-market-intelligence`
- API key registration:
  - `https://dashboard.aiondashboard.site/access/register`
- Managed API:
  - `https://api.aiondashboard.site/v1/analyze`
- PyPI package:
  - `https://pypi.org/project/aion-indian-market-intelligence/`
- GitHub repository:
  - `https://github.com/AION-Analytics/aion-indian-market-intelligence`
- Hugging Face model surface:
  - `https://huggingface.co/AION-Analytics/aion-indian-market-intelligence`
- Hugging Face demo Space:
  - `https://huggingface.co/spaces/AION-Analytics/aion-indian-market-intelligence`
- MCP server repo:
  - `https://github.com/AION-Analytics/aion-mcp-server`
- MCP marketplace maintenance register:
  - `docs/MCP_MARKETPLACE_MAINTENANCE.md`

## Current Limits

- production usage is quota-controlled at the API layer
- weather and crop coverage still depends on explicit cues in the headline
- sparse headlines can remain ambiguous
- pricing and latency tiers above are current commercial positioning and may evolve
- this repository does not contain model weights. The PyPI package provides client tooling only. Production inference requires the hosted API.

Canonical note: the public Python import path is `aion_indian_market_intelligence`.
Legacy slugs may remain visible only as redirects or historical records; they
are not the public product identity.
