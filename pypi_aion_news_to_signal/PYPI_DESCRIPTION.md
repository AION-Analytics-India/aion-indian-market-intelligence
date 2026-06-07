# aion-indian-market-intelligence

mcp-name: io.github.AION-Analytics/aion-indian-market-intelligence

`aion-indian-market-intelligence` is the canonical Python package for AION Indian Market Intelligence for Macro Event & Sector Impact Analysis.

It converts Indian financial news headlines into structured sector impact vectors. It performs macro event analysis for monetary policy, fiscal action, SEBI regulation, commodity shocks, weather events, policy changes, and corporate catalysts.

Every call returns structured sector intelligence as JSON, organised around the canonical `sector_vector` key. The output is intended for macro event analysis, sector impact analysis, policy impact analysis, event-driven market intelligence, economic propagation analysis, and sector exposure review for Indian markets.

Install:

```bash
pip install aion-indian-market-intelligence
```

Canonical import:

```python
from aion_indian_market_intelligence import analyze
```

The package ships an MCP server, so Claude and other MCP clients can turn Indian financial news into NSE sector impact vectors directly:

```bash
aion-indian-market-intelligence-mcp
```

The previous package name has been retired for new integrations. Use `aion-indian-market-intelligence` as the package name and `aion_indian_market_intelligence` as the Python import path.

Built for the NSE and BSE by AION Analytics.
