# PyPI Long Description
# Add this as the [project] description field in pyproject.toml
# or as the content of a DESCRIPTION.md file

aion-indian-market-intelligence is an Indian market intelligence client package for macro event intelligence and sector impact analysis. It sends Indian financial headlines to the managed AION API and returns structured event intelligence centered on the canonical `sector_vector` key.

Every call returns structured JSON for downstream dashboards, copilots, analyst workflows, and internal review tools. The package is an access layer for macro event analysis, policy impact analysis, event-driven market intelligence, and sector exposure intelligence. It is not an execution product, advice product, or local model runtime.

For MCP clients, install the dedicated wrapper package with `uvx aion-indian-market-intelligence-mcp`. The wrapper depends on this hosted API client and does not bundle a local engine, taxonomy, rule files, models, or weights.

Built for the NSE and BSE by AION Analytics.
