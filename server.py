from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server", host="127.0.0.1", port=8000)

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")