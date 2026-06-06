# PyPI Long Description

mcp-name: io.github.AION-Analytics/aion-indian-market-intelligence

aion-indian-market-intelligence is an Indian market intelligence package that converts Indian financial news headlines into structured sector impact vectors. It performs macro event analysis for monetary policy, fiscal action, SEBI regulation, commodity shocks, weather events, policy changes, and corporate catalysts.

Every call returns structured sector intelligence as JSON, organised around the canonical `sector_vector` key. The output is intended for macro event analysis, sector impact analysis, policy impact analysis, event-driven market intelligence, economic propagation analysis, and sector exposure review for Indian markets.

The package ships an MCP server, so Claude and other MCP clients can turn Indian financial news into NSE sector impact vectors directly. Install with `pip install aion-indian-market-intelligence`, then call `analyze()` or run the bundled MCP server.

Built for the NSE and BSE by AION Analytics.
