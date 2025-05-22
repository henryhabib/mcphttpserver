from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    uvicorn.run(
        mcp.streamable_http_app(),
        host="0.0.0.0",
        port=8000,
        log_level="info",
        lifespan="on",           # <- key line: wait for startup before serving
        timeout_graceful_shutdown=30,
    )