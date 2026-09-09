import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP
from services.emergency_service import process_request

mcp = FastMCP("Emergency Server")


@mcp.tool()
def emergency_request(blood_group, units):
    return process_request(blood_group, units)


if __name__ == "__main__":
    print("✅ Emergency MCP Server Started")
    mcp.run()