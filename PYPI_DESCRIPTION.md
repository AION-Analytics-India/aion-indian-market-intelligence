# PyPI Long Description
# Add this as the [project] description field in pyproject.toml
# or as the content of a DESCRIPTION.md file

aion-indian-market-intelligence is an Indian market intelligence package that converts Indian financial news headlines into structured sector impact vectors. It performs macro event analysis across 95 event types — monetary policy, fiscal action, SEBI regulation, commodity shocks, and corporate catalysts — and propagates each event across 32 NSE sectors using input-output dependency weighting, with a VIX overlay that scales output to the current volatility regime.

Every call returns structured signals as JSON, organised around the canonical `sector_vector` key, ready to feed premarket prediction models, algorithmic strategies, and portfolio risk systems for Indian markets.

The package ships an MCP server, so Claude and other MCP clients can turn Indian financial news into NSE sector impact vectors directly. Install with `pip install aion-indian-market-intelligence`, then call `analyze()` or run the bundled MCP server.

Built for the NSE and BSE by AION Analytics.
