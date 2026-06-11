# MCP Marketplace Maintenance

Last updated: 2026-06-11 IST.

The machine-readable register is `docs/mcp_marketplace_registry.json`. Keep
marketplace copy, Continue configs, standalone MCP repo copy, and registry
manifests aligned with that file.

## Canonical MCP Package

```bash
uvx aion-indian-market-intelligence-mcp
```

Installed entrypoint:

```bash
pip install aion-indian-market-intelligence-mcp
aion-indian-market-intelligence-mcp
```

The MCP wrapper calls the managed API:

```text
POST https://api.aiondashboard.site/v1/analyze
```

It requires `AION_API_KEY`, exposes `analyze_news`, and returns the public
`sector_vector` key.

## Public Copy Rules

- Title: `AION Indian Market Intelligence for Macro Event & Sector Impact Analysis`
- Description: `Macro-event and sector impact intelligence for Indian financial markets.`
- Secondary description: `Structured analysis of how policy, economic, weather, and geopolitical events affect Indian market sectors.`
- MCP package: `aion-indian-market-intelligence-mcp`
- Client package: `aion-indian-market-intelligence`

Do not publish taxonomy, rule files, dependency matrices, local inference
runtime, model weights, training artifacts, price-prediction claims, execution
claims, or brokerage/order-routing language.

## Marketplace Surfaces

| Surface | URL / Source | Current local action |
|---|---|---|
| PyPI MCP package | `https://pypi.org/project/aion-indian-market-intelligence-mcp/` | Published package used for direct `uvx` startup. |
| PyPI client package | `https://pypi.org/project/aion-indian-market-intelligence/` | Client remains hosted API only; published metadata may lag until the next client release, so marketplace copy should point MCP users to the MCP wrapper package. |
| Standalone MCP GitHub repo | `https://github.com/AION-Analytics/aion-mcp-server` | Source copy lives in `publish_assets/aion-mcp-server/README.md`. |
| MCP Market | `https://mcpmarket.com/server/aion-indian-market-intelligence` | Listing copy should match this document and the JSON register. |
| HOL / Pulse MCP mirror | `https://hol.org/registry/agent/uaid%3Aaid%3A52jjV7XZ41rVLWu8EpjeEszE3YViz5uUtFGBDt9VmpSbk7YnF7P4SJu9btt2bB8zXz` | Refresh after upstream marketplace metadata uses the dedicated MCP package. |
| Glama | `https://glama.ai/mcp/servers/io.github.AION-Analytics/aion-indian-market-intelligence` | Claim or refresh with the canonical package details. |
| Official MCP registry manifest | `distribution/mcp/server.json` | Prepared with `aion-indian-market-intelligence-mcp==1.0.0`. |
| Continue config | `distribution/continue/` | Prepared for installed entrypoint and direct `uvx` use. |
| CuratedMCP | `https://www.curatedmcp.com/` | Submit only after existing listings carry the same package details. |
