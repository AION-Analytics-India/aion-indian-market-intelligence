# AION Indian Market Intelligence (IMI)

**Indian market intelligence API for caller supplied financial and policy events.** IMI adds structured context to a headline: how an event may relate to Indian market sectors and stakeholder groups. It is a hosted API product; this repository contains client and integration material, not the inference model or its weights.

## What IMI does

A polarity score can say that a headline reads positive or negative, but that single label does not show which sectors may be affected in different ways or which stakeholder perspectives matter. IMI accepts one caller supplied headline, with optional publication time and article body, and returns structured Indian market context, including a signed `sector_vector`, confidence, market context, sector summaries and stakeholder views.

The caller supplies the news text. The API does not ingest news feeds, fetch RBI or SEBI publications, parse PDFs or filings, or monitor markets continuously. Policy and regulatory examples are supported as caller supplied text; coverage depends on the input and is not guaranteed.

## Who can use it

- **AI and application developers** can add returned context to an LLM prompt or their own retrieval augmented generation (RAG) records.
- **SaaS and CRM teams** can join sector outputs to their own customer or account classifications. IMI does not connect to or enrich a CRM by itself.
- **Analysts and institutional teams** can process headlines from their own sources and route selected results to a review or reporting workflow.
- **MCP-compatible agents** can call the hosted API through the published MCP wrapper when their plan and API key allow it.

These are integration patterns built by the consumer around IMI's response. They are not bundled feed ingestion, CRM, RAG, alerting, reporting or risk-management products.

## Practical integration patterns

### LLM or RAG enrichment

Store the returned `sector_vector` and stakeholder context with the original item in your own retrieval system. When that item is retrieved, your application can supply the structured context to its LLM. IMI does not provide the vector database or retrieval layer.

### Policy and institutional monitoring

Send a headline and, where available, its article body from your own RBI, SEBI, government, company or news source. Your application can review the returned sector and stakeholder context alongside the original source. The API does not fetch or authenticate those publications.

### Sector aware SaaS and CRM workflows

Your application may compare returned sector values with its own customer or supplier classifications to prioritize human review. Any thresholds, account mapping and resulting actions are your application's logic; IMI does not supply a CRM connector or make business decisions.

### Research queues and alerts

Process your own headlines one request at a time, then sort or route results using the returned fields. The API does not provide a feed, batch job, scheduled alert service or research report.

### MCP agent workflows

The MCP package exposes `analyze_news` over the same hosted API. It is an API wrapper for MCP clients, not a model running locally or inside Hugging Face.

## API input and output

The managed endpoint accepts one headline, optional `published_at`, and optional `body` per request. The article body can add context when the headline is ambiguous. It does not accept a feed, PDF, filing, table or multi-event batch through this endpoint.

The documented public response includes:

- `headline` — the submitted headline.
- `confidence` — the system's classification confidence; it is not a probability of a market outcome.
- `macro_signal` and `vix_regime` — market-context fields when returned.
- `sector_vector` — signed sector values; this is the canonical sector-impact field.
- `top_positive_sectors` and `top_negative_sectors` — compact summaries when returned.
- `stakeholder_views` — structured stakeholder perspectives when returned.
- `cultural_context` — a plain-language indicator and explanation when a supported cultural or sovereign context applies.
- Internal assignment identifiers and execution-oriented fields are removed from the public response. Ignore unrecognized fields rather than depending on them.

API keys are model and plan scoped and require a verified email and server-verified passkey. The free API plan is available once per verified user/account and includes JSON REST access with `sector_vector` and `stakeholder_views`: 10 successful requests per rolling 30 days, with a maximum of 10 in any rolling 24 hours. Free key issuance is also limited by device and network. Other plan quotas and integration entitlements differ; consult the [current API catalogue](https://aionanalytics.in/apis) for current terms.

The website demo key is a separate browser-demo allowance, not an API key or a second free API plan. It is issued once per email and allows up to 3 IMI analyses per browser/device pass and 30 per network in a rolling 7 days. An optional passkey raises the demo allowance to 10 analyses per passkey. Passkey verification happens on the visitor's device; AION does not receive biometric data. The demo key does not authorize calls to the production API. See the [website demo access page](https://aionanalytics.in/demo/key) for current access terms.

## Integration options

### REST API

```text
POST https://api.aionanalytics.in/v1/analyze
X-API-Key: <your API key>
Content-Type: application/json
```

```json
{
  "headline": "RBI raises the policy repo rate",
  "published_at": "2026-06-05T09:00:00+05:30",
  "body": "Optional source text supplied by your application."
}
```

`published_at` and `body` are optional. Keep API keys on your server; do not embed them in a browser or public Space.

### Python client

Install the proprietary hosted API client:

```bash
pip install aion-indian-market-intelligence
export AION_API_KEY="<your API key>"
```

```python
from aion_indian_market_intelligence import analyze

result = analyze(
    "RBI raises the policy repo rate",
    published_at="2026-06-05T09:00:00+05:30",
)
print(result["sector_vector"])
```

The Python package sends requests to the managed API. It does not run inference locally.

**Client version 1.0.11:** The published Python `analyze()` interface accepts `headline` and optional `published_at`, but **not** `body`. To submit optional article-body text, use the documented REST API directly when supported by your entitlement. Do not pass `body=` to the Python client until a compatible client version is released.

### MCP wrapper

```bash
uvx aion-indian-market-intelligence-mcp
```

Configure `AION_API_KEY` in the MCP host's server-side environment. The MCP wrapper calls the same hosted API through the Python client; REST and Python clients expose the documented public response. MCP client behavior and available plan entitlements are described in the [MCP package documentation](https://github.com/AION-Analytics-India/aion-mcp-server).

## Limitations and access

- IMI interprets text supplied by the caller. It does not provide source feeds or verify the submitted source.
- One request analyzes one headline and optional body. Feed ingestion, continuous monitoring, PDF or filing extraction, and batch processing belong to your application.
- Event coverage and classification can be incomplete or uncertain. Sparse, ambiguous or unsupported inputs may produce limited context or no useful sector signal.
- Impact values are indicative context, not statistically calibrated forecasts. Confidence does not guarantee correctness or predict market movement.
- The product is information infrastructure, not investment advice, a trading signal, a buy/sell/hold recommendation, or an execution service. It does not connect to brokers or place orders.
- Hosted API access requires an API key and is quota and plan controlled. Current plan requirements and limits are listed at [aionanalytics.in/apis](https://aionanalytics.in/apis).
- The hosted model and its weights are proprietary and are not distributed. The Python client is proprietary hosted API software. The MCP wrapper has its own license; see its repository for the current license terms.

## Links

- [AION IMI product page](https://aionanalytics.in/models/indian-market-intelligence)
- [API catalogue and access](https://aionanalytics.in/apis)
- [API reference](https://aionanalytics.in/docs/api-reference.txt)
- [Python client on PyPI](https://pypi.org/project/aion-indian-market-intelligence/)
- [MCP wrapper on PyPI](https://pypi.org/project/aion-indian-market-intelligence-mcp/)
- [MCP server source](https://github.com/AION-Analytics-India/aion-mcp-server)
- [Hugging Face model card](https://huggingface.co/aion-analytics-india/aion-indian-market-intelligence)
- [Static Hugging Face Space](https://huggingface.co/spaces/aion-analytics-india/aion-indian-market-intelligence)
- [AION Analytics Private Limited](https://aionanalytics.in)

## Licensing

The hosted IMI model and Python client are proprietary. No model weights are distributed. The MCP wrapper and utility packages have separate licenses; check the license file in each repository before reuse.
