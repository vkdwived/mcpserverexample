To install the `add_tool` MCP Server, run the following command:

```json
{
  "mcpServers": {
    "add_tool": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/vkdwived/mcpserverexample.git",
        "mcp-server"
      ]
    }
  }
}
```

This will fetch and setup MCP Server on your local MCP Client.

