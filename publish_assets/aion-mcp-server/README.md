# AION Indian Market Intelligence MCP Server

Macro-event and sector impact intelligence for Indian financial markets.

Connect AI agents and coding IDEs like ChatGPT, Claude, Gemini, Cursor, VS Code, Windsurf, Antigravity, Cline, and other MCP clients directly to Indian financial event intelligence.

Use it as an MCP-compatible Indian market intelligence server inside agent and IDE workflows.

# What it does

- Exposes a single tool: `analyze_news`
- Given a headline like `"RBI hikes repo rate by 25 bps"`
- Returns only the `sector_vector`
- Helps answer which sectors are exposed, pressured, or relatively supported
- Requires API key configuration through `AION_API_KEY`
- Enforces quota through the managed API
- Does not execute trades or generate executable orders

# Installation

Run directly with `uvx`:

```bash
uvx aion-indian-market-intelligence-mcp
```

Or install the dedicated MCP package:

```bash
pip install aion-indian-market-intelligence-mcp
```

# Usage

```bash
aion-indian-market-intelligence-mcp
```

Environment:

```bash
export AION_API_KEY="<your_api_key>"
```

Then connect your LLM client or IDE to the MCP server and ask:

```text
Analyze this Indian financial headline using AION Indian Market Intelligence and return the sector_vector only: <headline>
```

# Compatible clients

- ChatGPT
- Claude
- Gemini
- Cursor
- VS Code
- Windsurf
- Antigravity
- Cline
- Other MCP-compatible IDEs and agent runtimes

# Links

- Model surface: [AION Indian Market Intelligence](https://huggingface.co/AION-Analytics/aion-indian-market-intelligence)
- MCP PyPI package: [aion-indian-market-intelligence-mcp](https://pypi.org/project/aion-indian-market-intelligence-mcp/)
- Python client package: [aion-indian-market-intelligence](https://pypi.org/project/aion-indian-market-intelligence/)
- Live demo: [HuggingFace Space](https://huggingface.co/spaces/AION-Analytics/aion-indian-market-intelligence)
- API access page: [dashboard.aiondashboard.site/access/register](https://dashboard.aiondashboard.site/access/register)
- Documentation and MCP integration: [dashboard.aiondashboard.site/models/indian-market-intelligence](https://dashboard.aiondashboard.site/models/indian-market-intelligence)
