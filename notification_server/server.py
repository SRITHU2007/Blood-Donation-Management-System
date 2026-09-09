from fastmcp import FastMCP

mcp = FastMCP("Notification Server")


@mcp.tool()
def send_notification(message):
    print(f"Notification: {message}")
    return "Notification Sent"


if __name__ == "__main__":
    print("✅ Notification MCP Server Started")
    mcp.run()