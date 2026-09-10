from fastmcp import Client

SERVER_PATH = "mcp_server/server.py"

async def call_mcp(tool_name, arguments=None):
    if arguments is None:
        arguments = {}

    async with Client(SERVER_PATH) as client:
        result = await client.call_tool(tool_name, arguments)
        return result