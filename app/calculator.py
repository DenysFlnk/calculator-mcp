import os
from decimal import Decimal, getcontext

from mcp.server.fastmcp import FastMCP

port = int(os.getenv("HTTP_PORT", "8000"))
mcp = FastMCP(name="Calculator MCP Server", host="0.0.0.0", port=port)


@mcp.tool()
def set_precision(precision: int) -> str:
    """Set decimal precision for calculations (0-28)."""
    if not 0 <= precision <= 28:
        raise ValueError("Precision must be 0-28")

    getcontext().prec = precision

    return f"Precision set to {precision}"


@mcp.tool()
def add(numbers: list[float]) -> float:
    """Add an array of ≥2 numbers."""
    if len(numbers) < 2:
        raise ValueError("Need ≥2 numbers")

    return float(sum(Decimal(str(x)) for x in numbers))


@mcp.tool()
def subtract(numbers: list[float]) -> float:
    """Subtract numbers sequentially from first."""
    if len(numbers) < 2:
        raise ValueError("Need ≥2 numbers")

    result = Decimal(str(numbers[0]))

    for x in numbers[1:]:
        result -= Decimal(str(x))

    return float(result)


@mcp.tool()
def multiply(numbers: list[float]) -> float:
    """Multiply an array of ≥2 numbers."""
    if len(numbers) < 2:
        raise ValueError("Need ≥2 numbers")

    result = Decimal("1")

    for x in numbers:
        result *= Decimal(str(x))

    return float(result)


@mcp.tool()
def divide(numbers: list[float]) -> float:
    """Divide numbers sequentially. Raises on division by zero."""
    if len(numbers) < 2:
        raise ValueError("Need ≥2 numbers")

    result = Decimal(str(numbers[0]))

    for x in numbers[1:]:
        d = Decimal(str(x))

        if d == 0:
            raise ValueError("Cannot divide by zero")

        result /= d

    return float(result)


if __name__ == "__main__":
    use_http = os.getenv("USE_HTTP", "false").lower() == "true"

    if use_http:
        print(f"HTTP server on :{port}")
        mcp.run(transport="streamable-http")
    else:
        print("Stdio server")
        mcp.run()
