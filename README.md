# Calculator MCP Server 🧮

[![Docker Pulls](https://img.shields.io/docker/pulls/denysflnk/calculator-mcp)](https://hub.docker.com/r/denysflnk/calculator-mcp)
[![GitHub stars](https://img.shields.io/github/stars/DenysFlnk/calculator-mcp)](https://github.com/DenysFlnk/calculator-mcp/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://python.org)

**Tiny and precise decimal calculator for AI agents via Model Context Protocol (MCP)**. Add, subtract, multiply, divide arrays of numbers with exact precision. No more LLM math hallucinations!

## Why This Server? ✨

| Feature               | This Server                           | Others (GitHub/Docker Hub) |
| --------------------- | ------------------------------------- | -------------------------- |
| **Exact Decimal**     | ✅ `0.1+0.2=0.3`                      | ❌ Float errors common     |
| **Array Math**        | ✅ `add([1.1,2.2,3.3])`               | ❌ Single numbers only     |
| **Runtime Precision** | ✅ `set_precision(28)`                | ❌ Fixed/no control        |
| **Dual Transport**    | ✅ Stdio + HTTP                       | ❌ One or the other        |
| **Pre-built Docker**  | ✅ `docker pull && run`               | ❌ Manual build            |
| **Tool Descriptions** | ✅ Full docs (no model hallucination) | ❌ Minimal/None            |

**Perfect for**: Claude Desktop, LangChain agents, custom AI apps, finance/science calcs.

## 🚀 Quick Start

### Docker (Recommended)

**HTTP Mode** (apps/integrations):

```bash
docker run -d --name calc-mcp -p 8000:8000 -e USE_HTTP=true denysflnk/calculator-mcp:latest
```

Call: `POST http://localhost:8000/mcp`

**Stdio Mode** (Claude spawn):

```bash
docker run --rm -i denysflnk/calculator-mcp:latest
```

**Docker compose**:

```text
# docker-compose.yml
services:
  calculator:
    image: denysflnk/calculator-mcp:latest
    ports:
      - "8000:8000"
    environment:
      - USE_HTTP=true
      - HTTP_PORT=8000
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8000/mcp -d '{\"jsonrpc\":\"2.0\",\"method\":\"tools/list\",\"id\":1}' || exit 1"]
      interval: 30s
      timeout: 10s
```

```bash
docker compose up -d
```

### 🔧 Claude Desktop Integration

| Platform | Config File                                                       |
| -------- | ----------------------------------------------------------------- |
| macOS    | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows  | `%APPDATA%/Claude/claude_desktop_config.json`                     |
| Linux    | `~/.config/Claude/claude_desktop_config.json`                     |

```json
{
  "mcpServers": {
    "Calculator": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "denysflnk/calculator-mcp:latest"],
      "autoApprove": ["add", "subtract", "multiply", "divide", "pow", "sqrt", "sin", "cos", "set_precision"]
    }
  }
}
```

## 📋 Tools

| Tool          | Parameters                | Description                                          | Example                  |
| ------------- | ------------------------- | ---------------------------------------------------- | ------------------------ |
| add           | numbers: list[float] (≥2) | Sum array exactly                                    | add([0.1, 0.2]) → 0.3    |
| subtract      | numbers: list[float] (≥2) | Sequential subtract                                  | subtract([10, 3, 1]) → 6 |
| multiply      | numbers: list[float] (≥2) | Product of array                                     | multiply([2, 3, 4]) → 24 |
| divide        | numbers: list[float] (≥2) | Sequential divide (zero-check)                       | divide([100, 4]) → 25    |
| pow           | base: float, exponent: float | Exponentiation (rejects negative base + frac exp) | pow(2, 10) → 1024        |
| sqrt          | number: float             | Square root (rejects negative numbers)               | sqrt(9) → 3.0            |
| sin           | angle: float              | Sine of angle in radians                             | sin(0) → 0.0             |
| cos           | angle: float              | Cosine of angle in radians                           | cos(0) → 1.0             |
| set_precision | precision: int (0-28)     | Set decimal places                                   | set_precision(10)        |

**Test endpoint**:

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "add",
      "arguments": {"numbers": [0.1, 0.2]}
    }
  }'
```

## 📄 License

MIT License – Use freely!

## Questions?

[LinkedIn](https://www.linkedin.com/in/denys-filonenko-6a8632163/)
