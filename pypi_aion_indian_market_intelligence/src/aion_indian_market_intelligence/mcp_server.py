#!/usr/bin/env python3
from __future__ import annotations

import argparse
from typing import Any

from aion_indian_market_intelligence import analyze
from mcp.server.fastmcp import FastMCP


server = FastMCP(
    name="AION Indian Market Intelligence for Macro Event & Sector Impact Analysis",
    instructions=(
        "Use this integration to call AION Indian Market Intelligence for Macro Event & Sector Impact Analysis. "
        "Macro-event and sector impact intelligence for Indian financial markets. "
        "Structured analysis of how policy, economic, weather, and geopolitical events affect Indian market sectors. "
        "This is an MCP-compatible Indian market intelligence engine for macro event analysis, sector impact analysis, "
        "policy impact analysis, event-driven market intelligence, economic propagation analysis, and sector effect modeling. "
        "An API key is required through the AION_API_KEY environment variable. "
        "This system is quota-controlled and does not generate executable orders."
    ),
)


@server.tool(
    name="analyze_news",
    description=(
        "Analyze one Indian financial headline with Indian Market Intelligence for Macro Event & Sector Impact Analysis "
        "and return sector_vector for sector impact analysis. Requires API key configuration."
    ),
)
def analyze_news(headline: str, published_at: str | None = None) -> dict[str, Any]:
    result = analyze(headline, published_at=published_at)
    return {"sector_vector": result.get("sector_vector", {})}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run AION Indian Market Intelligence for Macro Event & Sector Impact Analysis.")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="MCP transport to run. Default: stdio",
    )
    args = parser.parse_args()
    server.run(transport=args.transport)


if __name__ == "__main__":
    main()
