# MCP Marketplace Listing
# AION Indian Market Intelligence

**Name:** AION Indian Market Intelligence
**Tagline:** Indian macro-event and sector impact analysis for MCP workflows.
**Category:** Finance / Data Analysis

**Description:**
AION Indian Market Intelligence lets Claude convert Indian financial news headlines into structured NSE sector incidence vectors. It classifies each headline into a macro event type and returns a JSON `sector_vector` for sector impact analysis. Built specifically for Indian markets, it covers monetary policy, fiscal action, SEBI regulation, commodity events, weather shocks, and policy changes.

**Capabilities:**
- Classify an Indian financial news headline into a macro event type
- Generate an NSE sector impact vector for any headline
- Assess SEBI / RBI policy impact across sectors
- Apply a VIX-regime overlay to scale sector-vector confidence
- Return structured JSON sector intelligence for downstream models

**Example prompts:**
1. "Analyze this headline for NSE sector impact: 'RBI holds repo rate steady, indicates end of tightening cycle.'"
2. "How would a SEBI tightening of F&O margin rules affect Indian broking and AMC sectors?"
3. "Convert today's RBI policy headline into a sector_vector I can feed my premarket model."
