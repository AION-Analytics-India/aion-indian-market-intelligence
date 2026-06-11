# MCP Marketplace Listing
# AION Indian Market Intelligence

**Name:** AION Indian Market Intelligence
**Tagline:** Macro-event and sector impact intelligence for Indian financial markets.
**Category:** Finance / Data Analysis

**Description:**
AION Indian Market Intelligence lets Claude request structured macro event analysis and sector impact analysis for Indian financial headlines. It returns a JSON object centered on `sector_vector`, with event metadata and sector exposure intelligence from the managed AION API. Built for Indian market workflows, it covers policy, economic, weather, commodity, and geopolitical event interpretation without exposing private runtime logic or presenting the output as investment advice.

**Capabilities:**
- Request macro event analysis for Indian financial headlines
- Return sector impact analysis through the canonical `sector_vector`
- Assess policy impact analysis for RBI, SEBI, fiscal, commodity, weather, and geopolitical events
- Provide event-driven market intelligence for dashboards, copilots, and review workflows
- Keep the tool boundary explicit: structured interpretation, not trade execution or advice

**Distribution:**
- MCP package: `aion-indian-market-intelligence-mcp`
- Run command: `uvx aion-indian-market-intelligence-mcp`
- API key: `AION_API_KEY`
- Managed endpoint: `POST https://api.aiondashboard.site/v1/analyze`
- Boundary: hosted API wrapper only; no local taxonomy, rule files, model weights, or inference engine

**Example prompts:**
1. "Analyze this headline for NSE sector impact: 'RBI holds repo rate steady and indicates the tightening cycle may pause.'"
2. "How would a SEBI tightening of F&O margin rules affect Indian broking and AMC sectors?"
3. "Convert today's RBI policy headline into a sector_vector for an internal market-intelligence dashboard."
