## Calculator MCP Server – tiny, precise math for AI agents

This image provides a lightweight **Model Context Protocol (MCP) calculator server** that exposes a small, focused math toolset to LLMs and AI agents. It uses Python + FastMCP to offer exact decimal arithmetic instead of error‑prone floating‑point math.

[📂 GitHub Repo](https://github.com/DenysFlnk/calculator-mcp) | [📖 Full README](https://github.com/DenysFlnk/calculator-mcp/blob/main/README.md)

### Why use this image?

- **Tiny and simple** – Single‑purpose server, minimal code and dependencies.
- **Precise math** – Uses decimal arithmetic so `0.1 + 0.2` really equals `0.3`, avoiding typical float rounding issues.
- **Agent‑friendly** – Full MCP tool descriptions so models know exactly how to call each tool (no guessing arguments).
- **Dual transport** – Run as a stdio MCP server for desktop tools, or as an HTTP server for your own apps and agents.
- **Docker‑first** – Prebuilt image, Docker Compose examples, and automated publishing from Git tags.

### Tools exposed

- `add(numbers: list[float])`  
  Add an array of numbers (at least 2).

- `subtract(numbers: list[float])`  
  Subtract numbers sequentially from the first element.

- `multiply(numbers: list[float])`  
  Multiply an array of numbers (at least 2).

- `divide(numbers: list[float])`  
  Divide numbers sequentially, with divide‑by‑zero protection.

- `pow(base: float, exponent: float)`
  Raise base to the given exponent. Rejects negative base with fractional exponent.

- `sqrt(number: float)`
  Square root of a number. Rejects negative numbers.

- `sin(angle: float)`
  Sine of an angle in radians.

- `cos(angle: float)`
  Cosine of an angle in radians.

- `set_precision(precision: int)`
  Configure decimal precision (0–28) for all subsequent calculations.

### How to run

#### HTTP mode (for apps, LangChain, etc.)

```bash
docker run -d \
  -p 8000:8000 \
  -e USE_HTTP=true \
  denysflnk/calculator-mcp:latest
```

Then send JSON‑RPC 2.0 requests to:

```text
http://localhost:8000/mcp
```

#### Stdio mode (for Claude Desktop / other MCP clients)

Configure your MCP‑compatible client to use:

```text
docker run --rm -i denysflnk/calculator-mcp:latest
```
as the command for this server.

Use this image whenever you need reliable, non‑hallucinated arithmetic inside AI agent workflows, with almost zero setup effort.
