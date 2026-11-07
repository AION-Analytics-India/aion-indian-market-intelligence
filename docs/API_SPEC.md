# API Specification

## AION Indian Market Intelligence

AION Indian Market Intelligence (IMI) is a hosted API for Indian financial event
context. It interprets one caller-supplied headline, optionally with its
publication time and article body, and returns structured sector and stakeholder
context. The caller supplies the news text; this endpoint does not ingest feeds,
fetch regulatory publications, parse PDFs or filings, or monitor markets.

The public package is a client and MCP wrapper. It does not include production
model weights, private taxonomy files, calibration coefficients, backend API
server code, or training scripts.

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
POST https://api.aionanalytics.in/v1/analyze
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
  "published_at": "2026-06-05T09:00:00+05:30",
  "body": "Optional article text supplied by the caller."
}
```

`published_at` and `body` are optional. The body can add context when a
headline is ambiguous. One request analyzes one item.

Scope:

- one headline per request
- optional caller-supplied article body and publication time
- no feed ingestion, webhook stream, PDF parsing, filing parsing, or table parsing in this endpoint
- regulatory or market text must be supplied by the caller; this client does not fetch source feeds

Response shape:

```json
{
  "headline": "string",
  "confidence": "float",
  "macro_signal": "float|null",
  "vix_regime": "string|null",
  "sector_vector": {},
  "top_positive_sectors": {},
  "top_negative_sectors": {},
  "stakeholder_views": {},
  "cultural_context": {
    "detected": "boolean",
    "explanation": "string"
  }
}
```

`sector_vector` is the canonical output key. There is no public
`sector_impacts` replacement key.

The public response omits internal event identifiers and execution-oriented
fields. The IMI free API plan is available once per verified user/account and
includes JSON REST access with `sector_vector` and `stakeholder_views`: 10
successful requests per rolling 30 days, up to 10 in any rolling 24 hours.
It requires a verified email and server-verified passkey; free key issuance is
also limited by device and network. Other quotas and integration entitlements
depend on the plan. See the [current API catalogue](https://aionanalytics.in/apis).

The website demo key is separate from an API key: it is issued once per email,
allows up to 3 IMI analyses per browser/device pass and 30 per network per
rolling 7 days, and cannot call this endpoint. An optional passkey raises the
demo allowance to 10 analyses per passkey. Passkey verification happens on the
visitor's device; AION receives no biometric data. See the [website demo access
page](https://aionanalytics.in/demo/key).

## MCP Server

Console entrypoint:

```bash
aion-indian-market-intelligence-mcp --transport stdio
```

Legacy console aliases may exist for compatibility, but the canonical public
identity is `aion-indian-market-intelligence`.

MCP tool:

```text
analyze_news(headline: str, published_at: str | None = None)
```

The published MCP server exposes `analyze_news(headline, published_at)` and
returns `sector_vector`. It calls the hosted API; it is not local inference. The
REST API and Python client expose the documented public response. The MCP
wrapper does not execute orders, route orders, provide advice, or claim
guaranteed market outcomes.

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
