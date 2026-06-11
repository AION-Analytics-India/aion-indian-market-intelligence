from __future__ import annotations

from aion_indian_market_intelligence.mcp_server import main as _main


def main() -> None:
    """Run the hosted API MCP server from the public client package."""
    _main()


if __name__ == "__main__":
    main()
