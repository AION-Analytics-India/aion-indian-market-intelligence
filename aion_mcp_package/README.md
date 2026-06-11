# aion-indian-market-intelligence-mcp

MCP server wrapper for the hosted AION Indian Market Intelligence API.

This package does not contain a local market engine, taxonomy, rule files,
models, weights, or offline inference runtime. It installs a command that calls
the public `aion-indian-market-intelligence` client package, which sends
requests to the hosted API.

## Install

Run directly with `uvx`:

```bash
uvx aion-indian-market-intelligence-mcp
```

Or install it:

```bash
pip install aion-indian-market-intelligence-mcp
aion-indian-market-intelligence-mcp
```

## API Key

Set your hosted API key before starting the MCP server:

```bash
export AION_API_KEY="<your_api_key>"
```

The hosted API endpoint is:

```text
POST https://api.aiondashboard.site/v1/analyze
```

## Claude Desktop

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

## Tool

The MCP server exposes one tool:

```text
analyze_news
```

Input:

```json
{
  "headline": "RBI hikes repo rate by 25 bps",
  "published_at": "2026-06-11T09:00:00+05:30"
}
```

Output:

```json
{
  "sector_vector": {}
}
```

Full hosted API responses may include additional public response keys depending
on entitlement and API version. This wrapper is for integration only; it is not
investment advice, price prediction, or an execution system.
