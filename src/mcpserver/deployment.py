from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AddNumbers")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers.
    """
    return a + b

