# AION Indian Market Intelligence for Macro Event & Sector Impact Analysis Continue Configs

Continue Hub and local config assets for using `AION Indian Market Intelligence for Macro Event & Sector Impact Analysis` inside Continue.

Macro-event and sector impact intelligence for Indian financial markets.

Structured analysis of how policy, economic, weather, and geopolitical events affect Indian market sectors.

Files:

- `aion-indian-market-intelligence.yaml`:
  Uses the installed console entrypoint:
  `aion-indian-market-intelligence-mcp`

- `aion-indian-market-intelligence-uvx.yaml`:
  Uses `uvx` to run the dedicated MCP package from PyPI without a manual package install.

Recommended install path for the standard config:

```bash
pip install aion-indian-market-intelligence-mcp
```

Then add the YAML to:

```text
~/.continue/mcpServers/
```

Or publish the same YAML as a public Continue Hub config.

The MCP package is a hosted API wrapper. It requires `AION_API_KEY` and does
not bundle taxonomy files, rule files, model weights, or a local inference
engine.
