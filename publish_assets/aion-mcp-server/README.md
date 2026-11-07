# AION Indian Market Intelligence MCP Server

A Python MCP wrapper for the hosted AION Indian Market Intelligence (IMI) API. The server submits caller-provided Indian financial or policy headlines to the managed API; it does not load model weights or run inference locally. The hosted model and Python API client are proprietary. This MCP wrapper is licensed under AGPL-3.0-or-later.

AION Analytics Private Limited (India)  
Website: https://aionanalytics.in/  
Canonical source: https://github.com/AION-Analytics-India/aion-mcp-server

## What it does

The `analyze_news` tool accepts one headline and optional publication time, calls the hosted IMI API, and returns the `sector_vector` field. It is a Python integration wrapper to the model API, not a separate model or inference service. The caller supplies the text; the package does not ingest news feeds, fetch RBI or SEBI publications, parse PDFs or filings, or provide continuous monitoring.

The sector vector is contextual information for applications to review. It is not a forecast, trading signal, investment advice or broker execution.

## Install

Run with `uvx`:

```bash
uvx aion-indian-market-intelligence-mcp
```

Or install the published package:

```bash
pip install aion-indian-market-intelligence-mcp
aion-indian-market-intelligence-mcp
```

Package: [aion-indian-market-intelligence-mcp on PyPI](https://pypi.org/project/aion-indian-market-intelligence-mcp/).

## API access

Configure a production API key in the MCP host's server-side environment:

```bash
export AION_API_KEY="<your_api_key>"
```

API keys and entitlements are managed separately from the website demo. The free API plan requires a verified email and server-verified passkey and permits 10 successful requests per rolling 30 days, with at most 10 in any rolling 24 hours. Key issuance is subject to device and network limits. A website demo key is not an API key and cannot be used by this MCP server. See the [current API catalogue](https://aionanalytics.in/apis) for access and plan details. Never put an API key in public source or client-side code.

## Claude Desktop example

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

Use the secret-management mechanism provided by your MCP host rather than committing a real key.

## Tool contract

`analyze_news` takes a headline and optional `published_at` value. Illustrative input:

```json
{
  "headline": "Caller-supplied Indian financial or policy headline",
  "published_at": "2026-06-05T10:00:00+05:30"
}
```

The tool returns the public sector-impact vector, for example in this shape:

```json
{
  "sector_vector": "values returned by the hosted API"
}
```

The REST API and Python client expose a broader documented response. This published MCP tool currently returns only `sector_vector`; do not assume the other API fields are available through it. See the [API reference](https://aionanalytics.in/docs/api-reference.txt).

## Practical integration patterns

- **Agent research:** attach the returned sector context to a caller-supplied headline for a human-reviewed research workflow.
- **LLM or RAG applications:** store the vector with the source item in your own system and provide it to your own retrieval or language-model pipeline.
- **SaaS or CRM workflows:** compare sectors with classifications maintained by your application; this package does not connect to a CRM or make account decisions.
- **Policy monitoring:** submit policy text collected by your own process; the wrapper does not fetch regulator or government sources.

These are consumer-built workflows around the API result, not bundled ingestion, retrieval, CRM, alerting, reporting, risk or scenario products.

## Limitations

- One caller-supplied headline per tool call; event coverage and classification may be incomplete or uncertain.
- No local inference, downloadable model weights, source-feed ingestion, PDF/filing extraction, batch processing, broker connection or order placement.
- Returned context is not a calibrated prediction and does not guarantee correctness or market outcomes.
- This is information infrastructure, not investment advice or a trading recommendation.
- API quotas and available fields depend on the current plan and API contract.

## Links

- [AION IMI product page](https://aionanalytics.in/models/indian-market-intelligence)
- [API access and catalogue](https://aionanalytics.in/apis)
- [API reference](https://aionanalytics.in/docs/api-reference.txt)
- [Python client on PyPI](https://pypi.org/project/aion-indian-market-intelligence/)
- [MCP package on PyPI](https://pypi.org/project/aion-indian-market-intelligence-mcp/)
- [Canonical MCP source on GitHub](https://github.com/AION-Analytics-India/aion-mcp-server)
- [IMI source and documentation](https://github.com/AION-Analytics-India/aion-indian-market-intelligence)
- [Hugging Face IMI model card](https://huggingface.co/aion-analytics-india/aion-indian-market-intelligence)
- [Static Hugging Face product page](https://huggingface.co/spaces/aion-analytics-india/aion-indian-market-intelligence)
- [Website demo-key flow](https://aionanalytics.in/demo/key) (separate from API credentials; live inference has not been independently verified here)
