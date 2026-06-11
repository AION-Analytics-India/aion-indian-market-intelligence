# AION Repository Governance Standard

## Approved Public Package Surfaces

- `aion-indian-market-intelligence` - Python client for the hosted AION Indian Market Intelligence API.
- `aion-indian-market-intelligence-mcp` - MCP server wrapper for the hosted API client.
- `aion-indian-market-calendar` - standalone Indian market calendar package.

The MCP package is a wrapper only. It must not bundle taxonomy files, rule YAMLs,
model weights, dependency matrices, or local inference/runtime logic. All market
intelligence is provided by the hosted API through the public client package.

## Public Boundary

Public packages may document endpoint wiring, authentication, install commands,
and response keys required for integration. They must not expose proprietary
implementation details, private resources, training artifacts, or duplicated IMI
engine trees.
