# MCP Marketplace Listing
# AION Indian Market Intelligence

**Name:** AION Indian Market Intelligence
**Tagline:** Turn Indian financial news into NSE sector signals.
**Category:** Finance / Data Analysis

**Description:**
AION Indian Market Intelligence lets Claude convert Indian financial news headlines into structured NSE sector impact vectors. It classifies each headline into a macro event type, propagates the impact across 32 NSE sectors, and applies a VIX volatility overlay, returning a JSON `sector_vector`. Built specifically for Indian markets, it covers monetary policy, fiscal action, SEBI regulation, and commodity events — giving Claude a quantitative read on how any Indian financial news event is likely to move individual sectors.

**Capabilities:**
- Classify an Indian financial news headline into a macro event type
- Generate an NSE sector impact vector for any headline
- Assess SEBI / RBI policy impact across sectors
- Apply a VIX-regime overlay to scale signal confidence
- Return structured JSON signals for downstream models

**Example prompts:**
1. "Analyze this headline for NSE sector impact: 'RBI holds repo rate steady, signals end of tightening cycle.'"
2. "How would a SEBI tightening of F&O margin rules affect Indian broking and AMC sectors?"
3. "Convert today's RBI policy headline into a sector_vector I can feed my premarket model."
